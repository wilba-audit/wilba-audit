#!/usr/bin/env python3
"""Append sourced prospect rows to the clinic pipeline, validating first.

Sourcing workers hand back a JSON array of row objects. This appends them to
outputs/pipeline/clinic-pipeline.csv, assigning ids itself and refusing anything
that would put a bad row in front of whoever writes the email.

    python3 scripts/append_prospects.py --date 2026-10-20 --dry-run a.json b.json
    python3 scripts/append_prospects.py --date 2026-10-20 a.json b.json

It lives in the repo on purpose. It used to live in the session scratchpad, which
was wiped between runs on 20 Oct 2026, taking the validator and the sourcing brief
with it - three workers that day ran with neither.

What it refuses, and why each rule exists:

* No email, or an unreadable one. A row with no address once carried a sendable
  grade for weeks; see the 19 Oct audit.
* A Cloudflare placeholder ("[email protected]"). That is an address we have not
  seen, so recording it would be a fabrication.
* A builder placeholder (filler@godaddy.com, contact@wix.com). Furniture an owner
  never replaced, not an address.
* No email_source. The URL and date the address was read on is the only thing
  standing between us and a guessed address.
* A duplicate clinic name or email already in the pipeline.
* A prescription-medicine name or a price in the opening angle. ICP v2 bans both
  in anything clinic-facing, and the opener is built from that field.

It also finds the A/B/C grade wherever the worker put it, because workers
reliably disagree about whether it belongs in icp_fit or fit_flag.
"""
import argparse, csv, io, json, os, re, sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PIPELINE = os.path.join(REPO, 'outputs/pipeline/clinic-pipeline.csv')

BANNED = re.compile(r'\b(botox|dysport|xeomin|jeuveau|bocouture|azzalure|filler|fillers|'
                    r'anti-?wrinkle|wrinkle[- ]relax|tox|toxin|rejuran|profhilo|sculptra|'
                    r'kybella|glp-?1|semaglutide|ozempic)\b', re.I)
PRICE = re.compile(r'(\$|AUD\s*\d|NZ\$|CAD\s*\d|£|\d+\s*%|\bper cent\b)', re.I)
MUSTHAVE = re.compile(r'must[- ]have\s*\d', re.I)


def dom(url):
    """Registrable-ish domain of a website field, for duplicate detection."""
    if not url:
        return ''
    m = re.search(r'(?:https?://)?(?:www\.)?([^/\s]+)', url.strip(), re.I)
    return m.group(1).lower().rstrip('.') if m else ''
NOTICE = re.compile(r'unsolicited|anti-spam|spam act|\bUEMA\b|no spam notice', re.I)
# Added 3 Nov 2026. NOTICE and OWN_SITE look for the WORDS of a consent finding, and five rows
# passed that test while stating the opposite: "nobody has checked the site for a 'no
# unsolicited commercial email' notice" contains the very word NOTICE hunts for. A keyword
# regex cannot tell a finding from a denial that one was ever made, so the denial has to be
# matched explicitly. SCREENED is the override: a row that was once held and has since been
# re-read carries both the old denial and the new stamp, and the stamp wins.
# Added 4 Nov 2026, the provenance twin of DENIAL below. Row 25 carried an email_source
# reading "published on contact page - verified 20 Sep 2026" while its own notes said the
# address was "inferred from search snippets" and the clinic's website was never located. The
# whole-file provenance scan reads email_source, so it passed that row every time: it asked the
# field that was making the claim. Same failure mode as DENIAL - a check that interrogates the
# claim instead of the evidence. VERIFIED is the override, for a row since re-read.
INVENTED = re.compile(r'inferred from (a )?search snippet|from search snippets|address was inferred'
                      r'|could not locate the clinic|never located the (clinic|site)'
                      r'|snippet-derived', re.I)
# The override is an explicit dated stamp, not a guess at prose. Matching loose wording was
# tried first and matched the wrong things; a stamp is a deliberate act by whoever re-read the
# page, which is what the override should require.
VERIFIED = re.compile(r'must[- ]have 5 re-verified', re.I)
DENIAL = re.compile(r'has not been (run|checked|done)|have not been (run|checked|done)'
                    r'|nobody has checked|nobody ever (checked|recorded|looked)'
                    r'|cannot be demonstrated|never been (run|checked|screened)'
                    r'|not been screened|HELD at C', re.I)
SCREENED = re.compile(r'must[- ]have 6 screened', re.I)
# Added 5 Nov 2026. On 4 Nov seven rows were found sitting out of the sending wave because their
# own notes asked a question - "someone should decide whether that is disqualifying before
# sending", "verify cash-pay before pitching". A row that asks a question is a row nobody will
# ever answer: the sending side cannot, because the question is about qualification, and the
# sourcing side never looks at an existing row again. The rule recorded that day was "resolve the
# question, or grade on it". It lived only in SOURCING-LOG.md, which workers are not told to read,
# and on 5 Nov a worker wrote another one ("if Jess narrows must-have 2 to billing only, this
# becomes a B immediately"). So it is enforced here and stated in the worker brief.
#
# This fires only on SENDABLE rows. A parked row saying "must-have 2 unresolved" is doing exactly
# what it should - naming the test it fails so the row is recoverable. What is forbidden is a row
# that defers the decision to a person who will never see it.
# The override, and it is an EXPLICIT STAMP rather than a guess at prose - because on 4 Nov the
# first version of the provenance override was a guess at how a resolution note would be worded
# and it did not match the note actually written. A row whose question has been answered carries
# the literal phrase "QUESTION RESOLVED" or "QUESTION WITHDRAWN" in its notes. Nothing else counts,
# and that convention is stated in the worker brief so it is not folklore.
RESOLVED = re.compile(r'QUESTION RESOLVED|QUESTION WITHDRAWN', re.I)
DEFERS = re.compile(r'someone should (decide|check|verify|confirm|look)'
                    r'|somebody should (decide|check|verify|confirm|look)'
                    r'|should be (decided|checked|verified|confirmed) before sending'
                    r'|worth a (glance|look|check) before sending'
                    r'|(verify|confirm|check) .{0,40} before (sending|pitching|any approach)'
                    r'|if Jess (narrows|decides|disagrees|agrees|widens)'
                    r'|needs a (decision|ruling) from'
                    r'|awaiting a (decision|ruling)'
                    r'|leaving this (open|undecided) for', re.I)
OWN_SITE = re.compile(r"(their|its|her|his|the clinic's|clinic's) own|own (site|page|website|homepage|domain)", re.I)
COUNTRY_OK = {'AU', 'NZ', 'US', 'CA', 'UK', 'IE'}
COUNTRY_MAP = {'United States': 'US', 'USA': 'US', 'Australia': 'AU', 'Canada': 'CA',
               'New Zealand': 'NZ', 'United Kingdom': 'UK', 'Great Britain': 'UK',
               'England': 'UK', 'Scotland': 'UK', 'Wales': 'UK', 'Ireland': 'IE'}

PLACEHOLDER = re.compile(r'(filler@godaddy|contact@wix|example\.com|yourdomain|'
                         r'\[email\s*protected\])', re.I)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('files', nargs='+')
    ap.add_argument('--date', required=True, help='date_added, e.g. 2026-10-20')
    ap.add_argument('--dry-run', action='store_true')
    args = ap.parse_args()

    with open(PIPELINE, newline='') as f:
        fields = next(csv.reader(f))
    existing = list(csv.DictReader(open(PIPELINE)))
    # Keyed on (name, country), not name alone. On 2 Nov a name-only check rejected a
    # grade-A Siloam Springs clinic as a duplicate of a grade-C clinic in Mildura, Victoria:
    # both are called "The Skin Clinic" and they share nothing else - different country,
    # different domain, different mailbox. Clinic names in this trade are extremely generic,
    # so name alone is not identity. A genuinely re-sourced clinic is still caught, by the
    # domain in its website field or by its email address, both checked separately below.
    names = {(r['clinic_name'].strip().lower(), (r.get('country') or '').strip().upper())
             for r in existing}
    domains = {dom(r.get('website')) for r in existing if dom(r.get('website'))}
    emails = {r['contact_email'].strip().lower() for r in existing if r['contact_email'].strip()}
    next_id = max(int(r['id']) for r in existing if r['id'].strip().isdigit()) + 1

    accepted, rejected = [], []
    for path in sorted(args.files):
        if not os.path.exists(path):
            print('MISSING %s' % path); continue
        try:
            data = json.load(open(path))
        except Exception as e:
            print('BAD JSON %s: %s' % (path, e)); continue
        print('%s: %d rows' % (os.path.basename(path), len(data)))
        for r in data:
            cn = (r.get('clinic_name') or '').strip()
            em = (r.get('contact_email') or '').strip()
            src = (r.get('email_source') or '').strip()
            angle = r.get('opening_angle') or ''
            why = None
            if not cn:
                why = 'no clinic_name'
            elif (cn.lower(), (r.get('country') or '').strip().upper()) in names:
                why = 'duplicate clinic already in the pipeline (same name, same country)'
            elif dom(r.get('website')) and dom(r.get('website')) in domains:
                why = ('duplicate: %s is already in the pipeline under another name'
                       % dom(r.get('website')))
            elif not em:
                why = 'no email address'
            elif PLACEHOLDER.search(em):
                why = 'placeholder, not an address we have seen: %r' % em
            elif '@' not in em or '.' not in em.split('@')[-1]:
                why = 'not a readable address: %r' % em
            elif em.lower() in emails:
                why = 'email already in the pipeline'
            elif not src:
                why = 'no email_source - we cannot say where the address was read'
            elif not re.search(r'20\d\d', src):
                # Five rows from the earliest batch said only "published on site". The
                # address was probably fine, but probably is not what we send on.
                why = 'email_source names no date - must-have 5 wants the URL and the date'
            elif BANNED.search(angle):
                why = 'opening angle names a prescription medicine or treatment category'
            elif PRICE.search(angle):
                why = 'opening angle contains a price or percentage'
            elif (r.get('icp_fit') or '').strip().lower() in ('a', 'b') \
                    and DEFERS.search(r.get('notes') or '') \
                    and not RESOLVED.search(r.get('notes') or ''):
                why = ('sendable row defers a qualification decision to a person who will never '
                       'see it - resolve the question or grade on it, per the 4 Nov rule')
            elif (r.get('icp_fit') or '').strip().lower() not in ('a', 'b') \
                    and not MUSTHAVE.search(r.get('notes') or ''):
                # Found 1 Nov 2026: four rows had sat disqualified for a fortnight on the
                # retired 22 Sep scale test, recoverable only because their notes recorded
                # the test applied rather than a bare verdict. A parked row that says "not a
                # fit" cannot be re-judged when the standard moves; one that names the number
                # can be re-read in seconds.
                why = ('parked row names no must-have by number - say which test it fails, '
                       'or the reason cannot be audited when the standard moves')
            if why:
                rejected.append((cn or '(unnamed)', why)); continue

            country = (r.get('country') or '').strip()
            if country in COUNTRY_MAP:
                # Workers write country names; the file uses two-letter codes, and the
                # consent regimes (AU/NZ, CASL, PECR) are keyed off the code.
                r['country'] = country = COUNTRY_MAP[country]
            if country and country not in COUNTRY_OK:
                rejected.append((cn, 'country %r is not one of %s'
                                 % (country, ', '.join(sorted(COUNTRY_OK)))))
                continue

            fit = (r.get('icp_fit') or '').strip()
            flag = (r.get('fit_flag') or '').strip()
            if fit.upper() in ('A', 'B') and country in ('AU', 'NZ'):
                # The AU Spam Act and NZ UEMA screen is the one consent finding that cannot
                # be reconstructed later from the row: it is a statement about what was NOT
                # on the page, so if nobody wrote it down at the time, nobody can. Both
                # findings have to be in notes in words - the address came off the clinic's
                # own site, and the site carries no notice refusing unsolicited commercial
                # email - or the row is not sendable. Checked here rather than trusted,
                # because a worker reporting "consent OK" has told us nothing.
                n = r.get('notes') or ''
                have_own = OWN_SITE.search(n)
                # Widened 3 Nov: this looked for 'unsolicited' alone and so would have
                # rejected three correctly-screened rows whose finding was recorded as
                # "no anti-spam notice". The finding is what matters, not the wording.
                have_notice = NOTICE.search(n)
                if INVENTED.search(n) and not VERIFIED.search(n):
                    rejected.append((cn, 'row graded %s admits its address was inferred rather '
                                         'than read off a page - must-have 5 is the one rule that '
                                         'never bends' % fit.upper()))
                    continue
                # A denial outranks both, unless the row has since been re-read.
                if DENIAL.search(n) and not SCREENED.search(n):
                    rejected.append((cn, 'AU/NZ row graded %s has consent wording that says '
                                         'the check was NOT made - a row cannot be cleared by '
                                         'a note recording that nobody looked' % fit.upper()))
                    continue
                if not (have_own and have_notice):
                    rejected.append((cn, 'AU/NZ row graded %s states %s - both consent '
                                         'findings must be in notes, in words'
                                     % (fit.upper(),
                                        'neither consent finding' if not (have_own or have_notice)
                                        else 'no "unsolicited" finding' if have_own
                                        else "nothing about the clinic's own site")))
                    continue
            if fit.upper() not in ('A', 'B', 'C') and flag.upper() in ('A', 'B', 'C'):
                fit, flag = flag, fit
            if fit.upper() not in ('A', 'B', 'C'):
                rejected.append((cn, 'no A/B/C grade in icp_fit or fit_flag')); continue

            names.add((cn.lower(), (r.get('country') or '').strip().upper()))
            emails.add(em.lower())
            if dom(r.get('website')):
                domains.add(dom(r.get('website')))
            r['icp_fit'] = fit.upper()
            r['fit_flag'] = flag or 'ICP v2'
            r['priority'] = r['icp_fit']
            r['price_point'] = ''          # v2 bans prices in anything clinic-facing
            r['status'] = 'New'
            r['date_added'] = args.date
            r['next_action_date'] = args.date
            r['owner'] = 'Jess'
            r.setdefault('segment', 'Med spa / aesthetics')
            r.setdefault('services', r.get('segment'))
            r.setdefault('contact_route', 'email published')
            r.setdefault('next_action', 'Draft lapsed-patient intro')
            accepted.append(r)

    print('\naccepted %d, rejected %d' % (len(accepted), len(rejected)))
    for cn, why in rejected:
        print('  REJECTED %s - %s' % (cn, why))
    if not accepted or args.dry_run:
        if args.dry_run:
            print('\n(dry run, nothing written)')
        return

    with open(PIPELINE, 'a', newline='') as f:
        w = csv.DictWriter(f, fieldnames=fields)
        for r in accepted:
            r['id'] = next_id; next_id += 1
            w.writerow({k: (r.get(k) or '') for k in fields})
    print('\nwrote ids %s-%s' % (accepted[0]['id'], accepted[-1]['id']))
    print('grades: ' + ', '.join('%s=%d' % (g, sum(1 for a in accepted if a['icp_fit'] == g))
                                 for g in ('A', 'B', 'C')))

    # re-read, because a write that never reached disk once produced a commit
    # message claiming a change the commit did not contain
    after = list(csv.DictReader(open(PIPELINE)))
    print('pipeline now %d rows' % len(after))
    sendable = [r for r in after if r['icp_fit'].strip().lower() in ('a', 'b')]
    bad = [r['id'] for r in sendable if not r['contact_email'].strip()]
    print('sendable rows with no email address: %d%s' % (len(bad), (' ' + str(bad)) if bad else ''))

    # The copy rules apply to every sendable row, not just the ones added today.
    # Fifty rows written before this validator existed carried a price or a
    # medicine name into opening_angle, the field the opener is built from, and
    # only a scan of the whole file found them.
    dirty = [r['id'] for r in sendable
             if BANNED.search(r['opening_angle'] or '') or PRICE.search(r['opening_angle'] or '')]
    print('sendable rows whose opening_angle breaks the copy rules: %d%s'
          % (len(dirty), (' ' + str(dirty)) if dirty else ''))

    # A site count the row itself admits to, above the one-to-four must-have.
    chain = re.compile(r'\b(\d+)\s*(?:sites|locations|clinics)\b', re.I)
    many = []
    for r in sendable:
        blob = ' '.join([r['city'], r['scale_signals'], r['notes']])
        if any(int(m.group(1)) >= 5 for m in chain.finditer(blob)):
            many.append(r['id'])
    print('sendable rows admitting to five or more sites: %d%s'
          % (len(many), (' ' + str(many)) if many else ''))

    # Provenance is the guarantee the whole list rests on, so check it over the whole
    # file: the page may be named in email_source or in notes, but it must be somewhere.
    url = re.compile(r'https?://|\b[\w-]+\.(?:com|net|org|au|nz|ca|uk|ie)\b', re.I)
    thin = [r['id'] for r in sendable
            if not url.search(r['email_source'] or '') and not url.search(r['notes'] or '')]
    print('sendable rows naming no page for the address: %d%s'
          % (len(thin), (' ' + str(thin)) if thin else ''))

    # Not a failure, a trend line. The early batches recorded their rule-outs in prose, and
    # backfilling them is not worth the effort when most are plainly plastic surgery or
    # chains. But this number should fall over time and never rise: every row parked from
    # 1 Nov 2026 names its must-have, because the validator now refuses one that does not.
    parked = [r for r in after if (r.get('icp_fit') or '').strip().lower() not in ('a', 'b')]
    vague = [r['id'] for r in parked if not MUSTHAVE.search(r.get('notes') or '')]
    print('parked rows predating the numbered-reason rule: %d of %d'
          % (len(vague), len(parked)))

    # Whole-file consent audit. The per-row check above only ever sees rows being appended,
    # and the five rows that slipped through on 3 Nov were already in the file. Anything this
    # prints above zero is a row somebody could send to on a finding nobody made.
    au = [r for r in after if (r.get('icp_fit') or '').strip().lower() in ('a', 'b')
          and (r.get('country') or '').strip().upper() in ('AU', 'NZ')]
    denied = [r['id'] for r in au
              if DENIAL.search(r.get('notes') or '') and not SCREENED.search(r.get('notes') or '')]
    silent = [r['id'] for r in au
              if not (NOTICE.search(r.get('notes') or '') and OWN_SITE.search(r.get('notes') or ''))]
    print('AU/NZ sendable rows whose notes deny the consent check: %d%s'
          % (len(denied), (' ' + str(denied)) if denied else ''))
    print('AU/NZ sendable rows with no consent finding at all: %d%s'
          % (len(silent), (' ' + str(silent)) if silent else ''))

    # Provenance, every market. A sendable row whose own notes say the address was inferred is
    # the one thing this pipeline must never contain.
    inv = [r['id'] for r in after
           if (r.get('icp_fit') or '').strip().lower() in ('a', 'b')
           and INVENTED.search(r.get('notes') or '')
           and not VERIFIED.search(r.get('notes') or '')]
    print('sendable rows whose notes admit an inferred address: %d%s'
          % (len(inv), (' ' + str(inv)) if inv else ''))

    # Deferred decisions, every market. The per-row check above only sees rows being appended,
    # so this is how rows written before 5 Nov 2026 become visible rather than staying lost in
    # the notes column. A non-zero count here is a list of rows nobody will ever send.
    defr = [r['id'] for r in after
            if (r.get('icp_fit') or '').strip().lower() in ('a', 'b')
            and DEFERS.search(r.get('notes') or '')
            and not RESOLVED.search(r.get('notes') or '')]
    print('sendable rows that defer a decision to a person: %d%s'
          % (len(defr), (' ' + str(defr)) if defr else ''))


if __name__ == '__main__':
    main()
