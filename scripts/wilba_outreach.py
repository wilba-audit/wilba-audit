#!/usr/bin/env python3
"""
WILBA outreach pipeline operations.

Deterministic half of the daily outreach engine: works out how many emails may go
out today, picks who they go to, and keeps the pipeline file honest. The judgement
half (sourcing, qualifying, writing) is done by the session that calls this.

    python3 scripts/wilba_outreach.py status
    python3 scripts/wilba_outreach.py batch [--size N]
    python3 scripts/wilba_outreach.py due
    python3 scripts/wilba_outreach.py mark --ids 4,6,8 --status "Draft ready"
    python3 scripts/wilba_outreach.py ramp

Pipeline lives in outputs/pipeline/clinic-pipeline.csv.
Send history lives in outputs/pipeline/send-log.json.
"""
import argparse, csv, io, json, os, re, sys
from datetime import date, datetime, timedelta

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSV_PATH = os.path.join(ROOT, 'outputs/pipeline/clinic-pipeline.csv')
# The send ledger is NOT ours. The GoHighLevel thread owns the sends, so it owns the
# record of them, and this script reads its file straight out of git, read-only. We keep
# no copy: a copy drifts, and a drifted copy is what let this script claim for seventeen
# days that the domain had never sent. Agreed with that thread on 1 Nov 2026.
LEDGER_REF = 'claude/project-thread-ptytul'
LEDGER_PATH = 'outputs/pipeline/ghl/send-state.json'

# send_days semantics, confirmed by the sending thread on 1 Nov 2026 - RAMP counts these
# entries, so what one entry means is load-bearing:
#   * Each entry is ONE SENDING DAY in Australia/Melbourne, Jess's own timezone. The
#     sender computes today in Melbourne and appends that date.
#   * It runs at most once a day, so one sending day is always exactly one entry. The
#     count cannot double or merge, which is what makes the ramp trustworthy.
#   * The first entry, '2026-10-15', is the ONLY UTC-dated one, left as it is because it
#     is one entry for one day either way. It is Melbourne 16 Oct - the date to quote to
#     Jess for the ten clinics (ids 85-89, 93, 94, 96, 97, 98) that received email 1.
# So: do not reinterpret, shift or deduplicate these dates here. Read the list, count it,
# and if the convention ever changes it changes in the sending thread, not in this file.

# Cold domain warm-up: volume ramps by the number of days we have actually sent on,
# not by calendar date.
#
# This comment used to assert that jess@wilba.ai had never sent anything. That stopped
# being true on 15 Oct 2026, when the GoHighLevel thread sent email 1 to ten clinics,
# and nothing here noticed for seventeen days because send-log.json did not exist and
# an absent file reads identically to a file saying zero. The authoritative ledger is
# the sending channel's own, outputs/pipeline/ghl/send-state.json on branch
# claude/project-thread-ptytul; send-log.json here mirrors its send days so this ramp
# does not restart from day 1 on a domain that is no longer cold. Two ledgers for one
# domain is the actual defect, and unifying them belongs to the sending thread.
RAMP = [(5, 5), (10, 10), (15, 15)]   # (through send-day N, daily cap)
RAMP_MAX = 20

# Only these statuses mean "still to be approached".
OPEN_STATUSES = {'New', 'Draft ready'}

# Follow-up cadence, in days after the initial send. A reply at any point ends the
# sequence - nobody gets chased after they have answered.
SEQUENCE = [
    ('Follow-up 1', 3),
    ('Follow-up 2', 7),
    ('Follow-up 3', 14),
]
SEQUENCE_END = 'Lost'

# Statuses that mean the sequence has stopped and must not resume.
STOPPED = {'Replied', 'Call booked', 'Proposal sent', 'Won', 'Lost', 'Disqualified'}


def load_rows():
    with open(CSV_PATH, newline='') as f:
        rows = list(csv.DictReader(f))
    if not rows:
        sys.exit('pipeline is empty')
    return rows


def save_rows(rows):
    fields = list(rows[0].keys())
    out = io.StringIO()
    w = csv.DictWriter(out, fieldnames=fields)
    w.writeheader()
    for r in rows:
        w.writerow({k: r.get(k, '') for k in fields})
    with open(CSV_PATH, 'w') as f:
        f.write(out.getvalue())


class LedgerUnavailable(Exception):
    """We could not read the send ledger. Never treat this as 'nothing has been sent'."""


def load_log():
    """Read the sending thread's ledger out of git. Raises rather than guessing.

    The one thing this must never do is return an empty ledger when it simply could not
    read one. An absent ledger used to read identically to a ledger saying zero, which is
    exactly how this script reported "send-day 1, days sent so far 0" for a domain that
    had already sent to ten clinics. Silence is not evidence of no sends.
    """
    import subprocess
    refs = ['origin/' + LEDGER_REF, LEDGER_REF]
    errors = []
    for ref in refs:
        try:
            out = subprocess.run(['git', '-C', ROOT, 'show', '%s:%s' % (ref, LEDGER_PATH)],
                                 capture_output=True, text=True, timeout=30)
        except (OSError, subprocess.SubprocessError) as exc:
            errors.append('%s: %s' % (ref, exc)); continue
        if out.returncode != 0:
            errors.append('%s: %s' % (ref, (out.stderr or '').strip().splitlines()[:1])); continue
        try:
            log = json.loads(out.stdout)
        except ValueError as exc:
            raise LedgerUnavailable('%s:%s is not valid JSON (%s). The ledger is the sending '
                                    'thread\'s file - do not edit it here; tell that thread.'
                                    % (ref, LEDGER_PATH, exc))
        if 'send_days' not in log:
            raise LedgerUnavailable('%s:%s has no send_days key. Do not assume zero; ask the '
                                    'sending thread what changed.' % (ref, LEDGER_PATH))
        log['_ref'] = ref
        return log
    raise LedgerUnavailable(
        'could not read %s from %s. Fetch it first:\n'
        '    git fetch origin %s\n'
        'Until it reads, the number of days this domain has sent on is UNKNOWN - which is '
        'not the same as zero, and must not be reported as zero.\n  %s'
        % (LEDGER_PATH, ' or '.join(refs), LEDGER_REF, '\n  '.join(errors)))


def save_log(log):
    """Refused by design: the ledger belongs to the sending thread."""
    raise LedgerUnavailable(
        'this script does not write the send ledger. %s on %s belongs to the GoHighLevel '
        'thread, which does the sending; it records its own send days. If a send happened '
        'here, tell that thread rather than writing a second record of it.'
        % (LEDGER_PATH, LEDGER_REF))


def todays_cap(log):
    """Daily cap for today, based on how many days we have already sent on."""
    sent_days = len(log.get('send_days', []))
    already_today = date.today().isoformat() in log.get('send_days', [])
    day_number = sent_days if already_today else sent_days + 1
    for through, cap in RAMP:
        if day_number <= through:
            return cap, day_number
    return RAMP_MAX, day_number


def is_contactable(r):
    return bool(r.get('contact_email', '').strip())


def is_open(r):
    return r.get('status', '').strip() in OPEN_STATUSES


def on_profile(r):
    """Clears the current ICP. Rows are tagged by the qualification pass."""
    return r.get('icp_fit', '').strip().lower() in {'a', 'b'}


def cmd_status(args):
    rows = load_rows()
    try:
        log = load_log()
        cap, day_number = todays_cap(log)
    except LedgerUnavailable as exc:
        # Print the pipeline counts, which do not depend on the ledger, and say plainly
        # that the send state is unknown. Do NOT fill in a zero.
        log, cap, day_number = None, None, None
        print('SEND LEDGER UNREADABLE - send state unknown, NOT zero.')
        print('  %s\n' % exc)

    contactable = [r for r in rows if is_contactable(r)]
    on_icp = [r for r in contactable if on_profile(r)]
    ready = [r for r in on_icp if is_open(r)]

    print(f'Pipeline           {len(rows)} rows')
    print(f'  contactable      {len(contactable)}')
    print(f'  on current ICP   {len(on_icp)}')
    print(f'  ready to approach{len(ready):>4}')
    print()
    print(f'Warm-up            send-day {day_number}, cap {cap}/day')
    print(f'  days sent so far {len(log.get("send_days", []))}')
    if ready:
        print(f'  runway           {len(ready) / cap:.1f} days at today\'s cap')
    else:
        print('  runway           0 days - SOURCE MORE PROSPECTS')

    by_status = {}
    for r in rows:
        by_status[r.get('status', '')] = by_status.get(r.get('status', ''), 0) + 1
    print()
    print('By status:')
    for s, n in sorted(by_status.items(), key=lambda kv: -kv[1]):
        print(f'  {n:>3}  {s or "(blank)"}')

    if len(ready) < cap * 5:
        print()
        print(f'LOW: fewer than a week of prospects at {cap}/day. Source more before drafting.')


def cmd_ramp(args):
    log = load_log()
    cap, day_number = todays_cap(log)
    print(json.dumps({'send_day': day_number, 'cap_today': cap,
                      'days_sent': len(log.get('send_days', [])),
                      'ledger': '%s:%s' % (log.get('_ref'), LEDGER_PATH)}))


# The copy rules ban prescription-medicine brand and category names and ban prices
# outright, including a clinic's own published prices quoted back at it. But
# scale_signals, dormant_lead_signal and services are TRUE RECORDS of the clinic and
# are supposed to contain that material - a membership scheme is a real dormant-lead
# signal and it is usually named after a product. append_prospects.py --audit-only
# counts those rows at the whole-file level. The gap this closes: the drafter does not
# read the audit, the drafter reads THIS output, and until now the material printed with
# no marker beside it. The warning has to sit where the writing happens.
# These two patterns are deliberately the same as append_prospects.py's, and must stay
# the same - if one is widened, widen both, or the audit and the drafter disagree about
# what is safe.
UNSAFE_WORDS = re.compile(r'\b(botox|dysport|xeomin|jeuveau|bocouture|azzalure|filler|fillers|'
                          r'anti-?wrinkle|wrinkle[- ]relax|tox|toxin|rejuran|profhilo|sculptra|'
                          r'kybella|glp-?1|semaglutide|ozempic)\b', re.I)
UNSAFE_PRICE = re.compile(r'(\$|AUD\s*\d|NZ\$|CAD\s*\d|\u00a3|\d+\s*%|\bper cent\b)', re.I)


def unsafe_to_quote(text):
    """What in this field the email may NOT repeat. Empty when the field is safe."""
    text = text or ''
    hits = []
    if UNSAFE_WORDS.search(text):
        hits.append('medicine name')
    if UNSAFE_PRICE.search(text):
        hits.append('price')
    return hits


def print_field(label, text, flag=True):
    """Print one fact for the drafter, marked if the email may not repeat it."""
    text = text or ''
    hits = unsafe_to_quote(text) if flag else []
    print(f'   {label:<9} {text}')
    if hits:
        print(f'   {"":<9} ^^ DO NOT QUOTE: contains a {" and a ".join(hits)}. '
              f'The fact is true and the record is right; the EMAIL may not name it. '
              f'Build the opener from the practice, not from this line.')


# A caution recorded for the sender is worthless if the sender never reads it. notes is
# where every qualification finding lands, and notes is the one field this printer did not
# show - so on 23 Nov 2026 a count found 19 sendable rows carrying an explicit "hold out of
# the first live send" recommendation, four of them grade A and therefore at the front of
# the oldest-first queue, plus 11 more carrying a named caution for whoever writes or sends.
# None of it reached the drafter. These patterns lift those sentences out and print them
# beside the row. They are deliberately narrow: they match the phrasings workers have
# actually used, and a phrasing nobody has used yet will be missed, which is why the
# sentence printed is the evidence rather than a verdict.
HOLD_PATTERNS = (
    re.compile(r'[^.|]*\b(?:hold (?:it |this |them )?(?:out|back)|hold out of|'
               r'do not send|do not draft)\b[^.|]*[.]?', re.I),
    re.compile(r'[^.|]*\bCOULD NOT BE RE-?VERIFIED\b[^.|]*[.]?', re.I),
    re.compile(r'[^.|]*\b(?:CAUTION|NOTE|WARNING|COPY WARNING) FOR WHOEVER\b[^.|]*[.]?', re.I),
    re.compile(r'[^.|]*\bnot monitored\b[^.|]*[.]?', re.I),
)


# A SECOND DETECTOR, ADDED 24 Nov 2026, AND IT KEYS ON THE ADDRESS INSTEAD OF ON PROSE.
# The patterns above have a limitation their own comment admits: they match phrasings
# workers have actually used. On 24 Nov a worker published a row whose mailbox is printed
# by the clinic as `info @ cosmedikate.com.au`, spaces either side of the @, and wrote the
# warning as "THE MAILBOX IS PUBLISHED WITH SPACES AROUND THE @ AND MUST NOT BE NORMALISED."
# That sentence is exactly right and matches NONE of the patterns above, so a grade-B row
# whose address cannot be sent as written would have reached the drafter with no flag at all.
# The danger is specific and worse than a bounce: the likeliest "fix" at the keyboard is to
# close the spaces up, which is the one thing the standing rule forbids, done by whoever is
# least likely to know the rule.
#
# So this check derives the fault from contact_email itself. A warning written as prose
# depends on someone choosing the words; a warning derived from the data depends on nothing.
# It is not a grade and not a hold on the clinic - the row is well qualified and the address
# is honestly recorded. It is a stop on SENDING THIS STRING, which is a different claim.
SENDABLE_ADDRESS = re.compile(r'^[^\s@,;:<>()\[\]]+@[^\s@,;:<>()\[\]]+\.[^\s@,;:<>()\[\]]+$')


def address_fault(email):
    """Why this string cannot go in a To: header as it stands, or None if it can.

    Deliberately says only what is wrong. It never proposes the corrected address,
    because the correction is the construction the sourcing rules forbid: an address
    is recorded as published, and only a person reading the clinic's own page may
    decide what the clinic actually meant.
    """
    e = (email or '').strip()
    if not e:
        return 'no address recorded'
    if SENDABLE_ADDRESS.match(e):
        return None
    # Order matters: the comma test runs first, because a two-address field also contains
    # whitespace and 'more than one address' is the diagnosis the reader can act on.
    if ',' in e or ';' in e:
        return 'looks like more than one address in one field'
    if e.count('@') != 1:
        return 'does not contain exactly one @'
    if re.search(r'\s', e):
        return ('published with whitespace inside the address, and recorded as published - '
                'DO NOT close it up yourself, that is constructing an address nobody published')
    return 'not a single plain address'


def print_address(r):
    """The To: line, plus why it cannot be used if that is the case.

    Used by both readers that print an address. `due` needs it as much as `batch`:
    a follow-up is a send too, and until 24 Nov it printed neither this stop nor the
    cautions in notes.
    """
    print(f'   to:       {r["contact_email"]}')
    fault = address_fault(r.get('contact_email', ''))
    if fault:
        print(f'   {"STOP":<9} THIS ADDRESS CANNOT BE SENT AS WRITTEN: {fault}.')
        print(f'   {"":<9} Do not draft from it. Jess settles it by opening the page:')
        print(f'   {"":<9} {r.get("email_source", "") or "no source recorded"}')


# THE MIRROR OF THE CONCEALED-WARNING DEFECT, FOUND 25 Nov 2026: THE DETECTOR CRIED WOLF.
# `notes` is a chronological record joined with " | ", and sender_cautions lifts a sentence out
# of that order. So a row held on 3 Nov for "COULD NOT BE RE-VERIFIED" still printed that hold
# after the 24 Nov sweep re-verified it and confirmed the address - on ELEVEN of the twenty-nine
# flagged rows. The sender had no way to see the resolution, because the extractor showed the
# worry and not the answer.
#
# A warning that is wrong a third of the time is worse than no warning: it teaches the one
# reader who acts to skim past the other two thirds. But SUPPRESSING a caution risks hiding a
# real hold, which is the original defect again in the other direction. So this prints both and
# lets the reader resolve it in one glance: the caution, then the later sentence that bears on
# it, labelled as possibly superseding rather than asserted to supersede.
SUPERSEDE_PATTERNS = (
    re.compile(r'[^.|]*\bRE-?VERIFIED\b[^.|]*[.]?', re.I),
    re.compile(r'[^.|]*\bQUESTION (?:RESOLVED|WITHDRAWN)\b[^.|]*[.]?', re.I),
    re.compile(r'[^.|]*\bMISDIAGNOSIS\b[^.|]*[.]?', re.I),
    re.compile(r'[^.|]*\bRESCUED\b[^.|]*[.]?', re.I),
)


def later_bearing_on(notes, cautions, limit=2):
    """Sentences that may answer a caution already printed, newest-looking last.

    Deliberately does not decide. It cannot: "re-verified" in a row's history may refer to a
    different question than the one the caution raises. Naming the sentence is enough, because
    the person reading has the whole row in front of them and a second to spend.
    """
    notes = notes or ''
    seen = {c[:60] for c in cautions}
    out = []
    for rx in SUPERSEDE_PATTERNS:
        for m in rx.finditer(notes):
            t = ' '.join(m.group(0).split()).strip(' .|')
            if len(t) < 12 or t[:60] in seen:
                continue
            seen.add(t[:60])
            out.append(t if len(t) <= 240 else t[:237] + '...')
            if len(out) >= limit:
                return out
    return out


def print_cautions(r):
    """The sentences someone meant the sender to read, if any."""
    notes = r.get('notes', '')
    cautions = sender_cautions(notes)
    if cautions:
        print(f'   {"HOLD?":<9} {len(cautions)} caution(s) recorded against this row '
              f'- read before drafting, and do not mark it Draft ready if one says hold:')
        for c in cautions:
            print(f'   {"":<9}  - {c}')
        later = later_bearing_on(notes, cautions)
        if later:
            print(f'   {"":<9} BUT the row says this LATER - check whether it answers the above '
                  f'before you hold:')
            for t in later:
                print(f'   {"":<9}  + {t}')


def sender_cautions(notes, limit=3):
    """The sentences in notes that someone meant the sender to read, deduplicated."""
    notes = notes or ''
    out = []
    for rx in HOLD_PATTERNS:
        for m in rx.finditer(notes):
            t = ' '.join(m.group(0).split()).strip(' .|')
            if len(t) < 12:
                continue
            if any(t[:60] == o[:60] for o in out):
                continue
            out.append(t if len(t) <= 300 else t[:297] + '...')
            if len(out) >= limit:
                return out
    return out


def cmd_batch(args):
    rows = load_rows()
    log = load_log()
    cap, day_number = todays_cap(log)
    size = args.size or cap

    ready = [r for r in rows if is_contactable(r) and on_profile(r) and is_open(r)]
    # A grade first, then B; oldest additions first so nothing rots at the bottom.
    ready.sort(key=lambda r: (r.get('icp_fit', 'z').lower(), r.get('date_added', '')))
    batch = ready[:size]

    if not batch:
        print('NOTHING TO DRAFT - no qualified, contactable, unapproached prospects.')
        print('Source and qualify more against outputs/pipeline/ICP.md first.')
        return

    print(f'# Batch for {date.today().isoformat()} - send-day {day_number}, cap {cap}, drafting {len(batch)}')
    print()
    for r in batch:
        print(f'## {r["id"]} | {r["clinic_name"]} ({r.get("icp_fit","?").upper()})')
        print_address(r)
        print(f'   who:      {r.get("lead_doctor") or "not named"}')
        print(f'   where:    {r.get("city","")}, {r.get("country","")}')
        print(f'   crm:      {r.get("crm_detected") or "UNKNOWN - grade C, do not draft"}')
        print_cautions(r)
        print_field('scale:', r.get('scale_signals', ''))
        print_field('dormant:', r.get('dormant_lead_signal', ''))
        # opening_angle is the drafted line itself, not a record of the clinic, so
        # anything unsafe in it is a breach rather than a fact to avoid quoting.
        angle_hits = unsafe_to_quote(r.get('opening_angle', ''))
        print(f'   {"angle:":<9} {r.get("opening_angle","")}')
        if angle_hits:
            print(f'   {"":<9} ^^ COPY-RULE BREACH, not a caution: the opening angle itself '
                  f'names a {" and a ".join(angle_hits)}. Rewrite it before drafting.')
        print()
    print(f'IDS: {",".join(r["id"] for r in batch)}')


def cmd_due(args):
    """Who is due a follow-up today, and which touch it is."""
    rows = load_rows()
    today = date.today()
    due = []
    for r in rows:
        status = r.get('status', '').strip()
        if status in STOPPED or status in OPEN_STATUSES or not status:
            continue
        sent = r.get('date_last_contact', '').strip()
        if not sent:
            continue
        try:
            sent_on = datetime.strptime(sent, '%Y-%m-%d').date()
        except ValueError:
            continue
        # Which touch comes next after the current status?
        names = [n for n, _ in SEQUENCE]
        if status == 'Emailed':
            nxt, gap = SEQUENCE[0]
        elif status in names:
            i = names.index(status)
            if i + 1 >= len(SEQUENCE):
                # Final touch already sent; retire it once the last gap has passed.
                if (today - sent_on).days >= SEQUENCE[-1][1]:
                    due.append((r, SEQUENCE_END, 0))
                continue
            nxt, gap = SEQUENCE[i + 1]
        else:
            continue
        if (today - sent_on).days >= gap:
            due.append((r, nxt, gap))

    if not due:
        print('Nothing due today.')
        return

    print(f'# Follow-ups due {today.isoformat()}')
    print()
    for r, nxt, gap in due:
        if nxt == SEQUENCE_END:
            print(f'## {r["id"]} | {r["clinic_name"]} -> retire as Lost (sequence complete, no reply)')
            continue
        print(f'## {r["id"]} | {r["clinic_name"]} -> {nxt}')
        print_address(r)
        print(f'   who:      {r.get("lead_doctor") or "not named"}')
        print(f'   last sent:{r.get("date_last_contact")} ({gap}+ days ago)')
        print_cautions(r)
        print(f'   angle:    {r.get("opening_angle","")}')
        print()
    print(f'IDS: {",".join(r["id"] for r, n, g in due if n != SEQUENCE_END)}')
    retire = [r["id"] for r, n, g in due if n == SEQUENCE_END]
    if retire:
        print(f'RETIRE: {",".join(retire)}')


def cmd_mark(args):
    rows = load_rows()
    ids = {i.strip() for i in args.ids.split(',') if i.strip()}
    today = date.today().isoformat()
    hit = 0
    for r in rows:
        if r['id'] in ids:
            r['status'] = args.status
            names = [n for n, _ in SEQUENCE]
            if args.status == 'Emailed' or args.status in names:
                r['date_last_contact'] = today
                if args.status == 'Emailed':
                    nxt, gap = SEQUENCE[0]
                else:
                    i = names.index(args.status)
                    nxt, gap = SEQUENCE[i + 1] if i + 1 < len(SEQUENCE) else (SEQUENCE_END, SEQUENCE[-1][1])
                r['next_action'] = nxt
                r['next_action_date'] = (date.today() + timedelta(days=gap)).isoformat()
            elif args.status in STOPPED:
                r['next_action'] = 'Sequence stopped'
                r['next_action_date'] = today
            elif args.status == 'Draft ready':
                r['next_action'] = 'Jess to review and send'
                r['next_action_date'] = today
            hit += 1
    save_rows(rows)

    if args.status == 'Emailed':
        # The send day is recorded by whoever sent, in their own ledger. This script used
        # to append it to a local copy, which is how two ledgers for one domain came to
        # exist. Say what needs recording and where, rather than recording it here.
        print('NOTE: %s is now the send ledger, owned by the thread that sends.\n'
              '      If mail genuinely went out today (%s), that thread records it - this\n'
              '      script no longer keeps a second copy.' % (LEDGER_PATH, today))

    print(f'{hit} rows set to {args.status}')
    missing = ids - {r['id'] for r in rows}
    if missing:
        print(f'WARNING: no such ids: {",".join(sorted(missing))}')


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest='cmd', required=True)
    sub.add_parser('status').set_defaults(fn=cmd_status)
    sub.add_parser('ramp').set_defaults(fn=cmd_ramp)
    sub.add_parser('due').set_defaults(fn=cmd_due)
    b = sub.add_parser('batch'); b.add_argument('--size', type=int); b.set_defaults(fn=cmd_batch)
    m = sub.add_parser('mark')
    m.add_argument('--ids', required=True)
    m.add_argument('--status', required=True,
                   choices=['New', 'Draft ready', 'Emailed', 'Follow-up 1', 'Follow-up 2',
                            'Replied', 'Call booked', 'Proposal sent', 'Won', 'Lost', 'Disqualified'])
    m.set_defaults(fn=cmd_mark)
    args = p.parse_args()
    try:
        args.fn(args)
    except LedgerUnavailable as exc:
        # A clear refusal beats a traceback, and beats a guess by much more than that.
        sys.stderr.write('%s: %s\n' % (type(exc).__name__, exc))
        raise SystemExit(1)


if __name__ == '__main__':
    main()
