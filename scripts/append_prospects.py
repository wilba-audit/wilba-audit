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

# 16 Nov 2026: the DEFERS check cannot read negation, and it fired on two of five rows in one
# batch - both on the sentence a worker writes when it HAS decided: "no further check is
# required before sending". That is the opposite of a deferral, so the phrase is removed from
# the text before DEFERS is tested. Kept deliberately narrow: only an explicit "no further /
# no additional / nothing further ... before sending" form is exempted, because widening it
# would start letting real deferrals through, and this check failing safe is the whole point.
NEGATED_DEFERRAL = re.compile(
    r'(?:and\s+)?(?:no (?:further|additional)|nothing (?:further|more))\s+'
    r'(?:check|checks|verification|confirmation|work)?\s*'
    r'(?:is|are)?\s*(?:required|needed|necessary|outstanding)?\s*'
    r'before (?:sending|pitching|any approach)', re.I)

# 18 Nov 2026, and it is the second thing removed from the text before DEFERS is tested.
#
# THE DISCRIMINATOR IS WHO IS SUPPOSED TO ANSWER THE QUESTION, and it is a real distinction
# rather than a hedge. The disease this predicate exists to catch is a row that hands a
# QUALIFICATION decision to a person who will never see it: "eyeball the review history before
# sending" is addressed to us, and nobody is assigned, so it is never done. But ICP.md
# explicitly sanctions ONE question being left open and even supplies its wording - the
# must-have 2 cash-pay question, "Do you bill any insurance or Medicare electronically?" -
# because that one is addressed to THE CLINIC, on a call that is part of the offer, and the
# clinic certainly will see it. A row that says "ask the cash-pay question on the first call"
# has not deferred anything; it has scheduled it with the one party who can answer.
#
# So the exemption is narrow and keyed to the asking, not to the topic: an instruction to ASK
# or RAISE something ON A CALL / WITH THEM / AT DISCOVERY. Widening it past that would start
# excusing real deferrals, and this check failing safe is the whole point. Anything a worker
# wants exempted beyond this gets the explicit RESOLVED stamp, per the 4 Nov rule that a guess
# at how a note would be worded does not match the note actually written.
#
# MEASURED THE SAME NIGHT, AND IT IS UNEXERCISED CODE: THIS EXEMPTION FIRES ON 0 OF 1,305 ROWS.
# I wrote it because I predicted the widened DEFERS would false-positive on the sanctioned
# cash-pay discovery question, and named row 369 as the instance. It is not an instance. Row
# 369 says "sclerotherapy is cash-pay in Australia, but check before pitching" - which assigns
# the check to nobody and is a genuine deferral, so DEFERS is right about it and I was wrong.
# That is the same shape as the six claims retracted on 17 Nov: a predicted boundary reported
# as an observed fact. The exemption is kept because the distinction it encodes is correct and
# because ICP.md tells workers to write exactly the sentence it exempts, so new rows may well
# carry it - but it has never matched a real row, so do not treat it as a tested path, and
# re-measure it before trusting it.
DISCOVERY_QUESTION = re.compile(
    r'(?:ask|raise|put|confirm|clarify)\b[^.;|]{0,80}?'
    r'(?:on the (?:first )?call|on a call|at discovery|in discovery|on the discovery call|'
    r'with (?:them|the clinic|the owner)|of (?:them|the clinic|the owner))'
    r'|(?:discovery|first-call|first call) question'
    r'|but ask\b|, ask\b|ask the cash-pay question', re.I)
# 18 Nov 2026: REBUILT AS A CROSS-PRODUCT, because the hand-written alternation had THREE
# independent defects and every one of them was invisible until the whole file was measured.
#
# The old pattern reported 0 deferrals across 1,305 rows. A plain-language audit of the same
# file found 36 sendable rows whose notes ask a human to check something before a send. The
# pattern was not wrong about those rows; it could not see them.
#
#   1. A LITERAL-SPACE OFF-BY-ONE. `(check) .{0,40} before (sending)` is verb, space, 0-40
#      chars, SPACE, "before" - so it cannot match the bare form "check before sending",
#      which needs two spaces to satisfy it. The commonest construction in the file was
#      unmatchable by the branch written for it.
#   2. THE VERB SET WAS WHAT I HAD IN FRONT OF ME. The file's single commonest phrasing is
#      "EYEBALL THE REVIEW HISTORY BEFORE SENDING" - about 15 of the 36 - and "eyeball" was
#      in no branch. Nor were read, resolve, or "sanity check" ("worth a (glance|look|check)"
#      cannot match "worth a sanity check", because the words sit between).
#   3. THE TRAILING PHRASE SET LIKEWISE: "before a send", "before any send", "before anything
#      is sent", "before it is ever sent", and the whole "do not send ... without X" shape.
#
# This is ICP.md's own rule about the Australian billing screen, turned on my own code:
# A SCREEN WRITTEN FROM ONE OBSERVED PHRASE WILL MISS THE SAME SCHEME UNDER ANY OTHER
# PHRASING - screen for the SCHEME and list several of its names. It is also the project's
# most-repeated failure mode (a check scoped to where the problem usually is will not see it
# where it survives) firing in this file for the third night running, and the 16 Nov fix
# above - one predicate, three call sites - did nothing to prevent it, because the defect was
# never in HOW MANY copies there were. It was in the ONE copy's vocabulary.
#
# So the fix is structural in a different direction: a VERB set and a PHRASE set, crossed.
# Adding a verb or a phrasing is one edit in one list; no branch can carry a space bug that
# its neighbours do not, because there are no hand-written branches left to drift apart.
_DEFER_VERB = (r'(?:eyeball(?:ed|ing|s)?|check(?:ed|ing|s)?|verif(?:y|ied|ying)|confirm(?:ed|ing|s)?'
               r'|resolv(?:e|ed|ing)|read|re-read|look(?:ed|ing)?(?:\s+at)?|decid(?:e|ed)'
               r'|establish(?:ed)?|sanity[-\s]check(?:ed|ing)?)')
_DEFER_WHEN = (r'before\s+(?:any\s+|a\s+|the\s+|it\s+is\s+ever\s+|anything\s+is\s+)?'
               r'(?:send|sends|sending|sent|pitch|pitching|approach|approaching|contact|'
               r'contacting|anything\s+goes)')
DEFERS = re.compile(
    # "someone / somebody / a human / Jess should <verb>"
    r'(?:someone|somebody|a human|anyone|Jess)\s+(?:really\s+)?(?:should|must|needs to|has to)\s+' + _DEFER_VERB
    # "<verb> ... before sending" - the gap is \s*.{0,60}\s* so the bare form matches too
    + r'|' + _DEFER_VERB + r'\s*.{0,60}?\s*' + _DEFER_WHEN
    # "before sending ... <verb>" - the same sentence written the other way round
    + r'|' + _DEFER_WHEN + r'\s*.{0,60}?\s*' + _DEFER_VERB
    # "should be checked / resolved / read before a send"
    + r'|should\s+(?:be\s+)?(?:\w+\s+){0,3}?' + _DEFER_WHEN
    # "do not send ... without <someone looking>" - a hold-back, not a question
    + r"|(?:do not|don't|never)\s+(?:send|email|pitch|approach)\b.{0,80}?\bwithout\b"
    # explicit hand-offs upward
    + r'|if Jess (?:narrows|decides|disagrees|agrees|widens)'
    + r'|needs a (?:decision|ruling) from'
    + r'|awaiting a (?:decision|ruling)'
    + r'|leaving this (?:open|undecided) for',
    re.I)
OWN_SITE = re.compile(r"(their|its|her|his|the clinic's|clinic's) own|own (site|page|website|homepage|domain)", re.I)

def defers(notes):
    """Does this row's notes hand a qualification decision to a person who will never see it?

    One definition, three call sites. It was two definitions for about four hours on 16 Nov
    2026, and that is the whole reason this function exists. The negation fix above was written
    into the per-row gate alone, so Revenge MD and Pretti Aesthetics passed the gate that had
    rejected them and then appeared in the whole-file audit as deferring - the same two rows,
    the same sentence, one check fixed and the other not.

    That is this project's most-repeated failure mode, recorded about a dozen times in ICP.md
    and the sourcing brief: A CHECK SCOPED TO WHERE THE PROBLEM USUALLY IS WILL NOT SEE IT WHERE
    IT SURVIVES. The corollary adopted on 15 Nov - that the 11 Nov strike "fixed the paragraph
    it stood in and never asked which other paragraphs said the same thing" - describes this
    exact slip, written down the night before I made it. The lesson is not "be careful"; it is
    that three copies of a predicate is three places for it to be wrong, so there is now one.

    Both exemptions are applied by DELETING the exempt sentence from the text before DEFERS is
    tested, rather than by testing the whole notes field for an exempt phrase anywhere in it.
    That matters: a row may carry a sanctioned discovery question AND a real deferral in two
    different sentences, and a whole-field test would let the first excuse the second.
    """
    notes = notes or ''
    scrubbed = DISCOVERY_QUESTION.sub(' ', NEGATED_DEFERRAL.sub(' ', notes))
    return bool(DEFERS.search(scrubbed)) and not RESOLVED.search(notes)


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
                    and defers(r.get('notes')):
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

    # The same check over the OTHER field a drafter builds copy from, added 9 Nov 2026.
    # The audit above has printed zero every night for days and was telling the truth about
    # the field it reads. It reads one field. A recovery worker found "$11-a-unit tox" sitting
    # in dormant_lead_signal, and a scan of every column then found 70 sendable rows with a
    # price in that field and 14 with a medicine name.
    #
    # The distinction that matters, and the reason this is a WARNING and not a rejection:
    # services, notes and scale_signals legitimately record what a clinic sells and what it
    # published - "Injectables/threads/fillers/skin" is a true research note and rewriting it
    # would destroy the asset. The copy rules govern what we SEND, not what we know.
    # But dormant_lead_signal is different in kind: it is the field the drafting channel reads
    # to build an opener, so a published price sitting in it is the single most quotable thing
    # in the row, and the copy rules specifically forbid quoting a clinic's own prices back at
    # them. So: never silently rewrite these, and never let one reach a draft unread.
    feeder = [r['id'] for r in sendable
              if BANNED.search(r['dormant_lead_signal'] or '')
              or PRICE.search(r['dormant_lead_signal'] or '')]
    print('sendable rows with copy-unsafe material in dormant_lead_signal '
          '(a true record, NOT to be quoted): %d%s'
          % (len(feeder), (' ' + str(feeder)) if len(feeder) <= 20 else ''))

    # price_point has been under a standing "leave it empty" instruction for weeks.
    # Widened from `sendable` to EVERY row on 16 Nov 2026. The narrow version had been reporting
    # 27 for weeks and was read as 27 legacy rows to get round to; the true figure was 102, and
    # the 75 it did not count were parked and off-ICP rows - which is where the hazard SURVIVES,
    # because a C row is parked rather than dropped and carries its columns with it when it is
    # re-graded to B. Same lesson as the deferral predicate above, found the same night: an audit
    # scoped to where the problem does the most damage will not show you where it lasts longest.
    priced = [r['id'] for r in after if (r['price_point'] or '').strip()]
    print('rows with anything in price_point, any grade (should be empty): %d%s'
          % (len(priced), (' ' + str(priced)) if len(priced) <= 20 else ''))

    # Keep DO-NOT-SEND.txt in step with the CSV. The real work lives in
    # scripts/refresh_do_not_send.py, which is standalone deliberately: a GRADE CHANGE is
    # not an append and never reaches this function, and ten rows changed grade by direct
    # CSV edit on 9 Nov. Run that script after any such edit; this call only covers appends.
    try:
        sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
        from refresh_do_not_send import refresh
        refresh()
    except Exception as exc:
        print('WARNING: could not regenerate DO-NOT-SEND.txt (%s)' % exc)

    # A site count the row itself admits to, above the one-to-four must-have.
    #
    # 17 Nov 2026: this now PRINTS THE SENTENCE IT MATCHED, and the reason is a false positive it
    # produced the same day. Row 1284 (Ahern Aesthetics) is one site in Park City, and the match
    # was on its founder's CV - "grew the franchise to over 10 locations" - which the row had
    # flagged itself, in terms, as a trap for whoever writes the email. The id alone sent me to
    # open the row and read the field; the sentence would have answered it in the audit output.
    #
    # The regex is deliberately NOT narrowed. It exists to catch a real chain and it should fail
    # safe, which means over-flagging; what was wrong was that a flag cost a lookup to interpret.
    # A crude check whose evidence is visible beats a clever check whose verdict you must trust -
    # the same principle as the QUESTION RESOLVED marker above.
    #
    # And the false positive is an instance of something worth naming, because three independent
    # cases turned up in one night: A NUMBER ON A CLINIC'S PAGE MAY BELONG TO A DIFFERENT BUSINESS
    # THAN THE ONE YOU ARE GRADING. Jewell Medical Spa's only trading-life sentence is about the
    # owner's PREVIOUS spa; Ahern's site count is its founder's former franchise; and a
    # grep-before-fetch hit on "Ahern" landed inside another row's prose rather than on a row.
    # Owner CVs, prior ventures and franchise histories all generate confident figures - site
    # counts, founding years, career lengths - about the wrong entity. Always ask whose business
    # the number is about.
    chain = re.compile(r'\b(\d+)\s*(?:sites|locations|clinics)\b', re.I)
    many = []
    for r in sendable:
        blob = ' '.join([r['city'], r['scale_signals'], r['notes']])
        for m in chain.finditer(blob):
            if int(m.group(1)) >= 5:
                lo = max(0, m.start() - 90)
                snippet = ' '.join(blob[lo:m.end() + 60].split())
                many.append((r['id'], snippet))
                break
    print('sendable rows admitting to five or more sites: %d' % len(many))
    for rid, snippet in many:
        print('    %s: ...%s...' % (rid, snippet))

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
            and defers(r.get('notes'))]
    print('sendable rows that defer a decision to a person: %d%s'
          % (len(defr), (' ' + str(defr)) if defr else ''))

    # And the same check over PARKED rows, added 8 Nov 2026. The audit above reads only sendable
    # rows, which is where a deferred decision does the most damage - but not where it survives
    # longest. Seven C rows were found carrying questions for Jess that nobody would ever see,
    # because a parked row is not re-read the way a sendable one is before a send. A question in
    # a C row is still a question nobody answers.
    pdefr = [r['id'] for r in after
             if (r.get('icp_fit') or '').strip().lower() not in ('a', 'b')
             and defers(r.get('notes'))]
    print('parked rows that defer a decision to a person: %d%s'
          % (len(pdefr), (' ' + str(pdefr)) if pdefr else ''))

    # GRADE A ROWS WHOSE OWN NOTES SAY MUST-HAVE 4 IS INFERRED RATHER THAN READ.
    # Added 18 Nov 2026 after measuring the whole file for the first time.
    #
    # The 5 Nov evidence ladder says in terms that it "is what separates a grade A from a grade B
    # on otherwise identical rows": a dated or quantified artifact on the clinic's own site
    # satisfies must-have 4; a practitioner's career length alone KEEPS THE ROW AT B; no proxy of
    # any kind parks it at C. The ladder has three rungs and none of them is "the operation looks
    # busy". But 33 of 202 grade-A rows carry a note saying established is inferred or not
    # verified, and about 23 of those name no rung at all - they reached A on team size, a device
    # fleet, a membership programme, a shopfront fit-out or a count of booking locations.
    #
    # This matters operationally and not just tidily: `wilba_outreach.py batch` selects A before
    # B, so these rows sit at the FRONT of the send queue holding the weakest age evidence in the
    # file - and must-have 4 is the one must-have whose failure means the offer has nothing to
    # work, because a clinic with no lapsed list cannot have its lapsed list reactivated.
    #
    # Almost all of them predate the ladder, so this is one more instance of the standing job that
    # is bigger than any market: A RULE CHANGE REACHES THE RUN THAT MAKES IT AND NOTHING BEHIND IT.
    #
    # IT PRINTS THE MATCHING SENTENCE, NOT JUST THE ID, and that is deliberate - the same choice
    # made for the site-count audit on 17 Nov after it false-positived on a founder's CV. A flag
    # that costs a lookup to interpret gets ignored; one that shows its evidence gets judged. The
    # regex is NOT narrowed to cut its false positives, because it should fail safe: row 894 is a
    # known false positive (it publishes "Founded Feb 2021" and the word "inferred" in its notes
    # refers to the patient count, not the date), and printing the sentence is what makes that
    # obvious in one glance instead of one fetch.
    inferred = re.compile(r'(?:established|must[- ]have\s*4|trading (?:history|length)|age)\s*'
                          r'(?:is|was|remains)?\s*'
                          r'(?:entirely\s+|completely\s+|wholly\s+)?'
                          r'(?:NOT VERIFIED|not verified|unverified|not established|inferred)',
                          re.I)
    ladder = re.compile(r'\b\d{2,4}\s*\+?\s*(?:google\s*)?reviews?\b|review count|based on \d+ review'
                        r'|founded (?:in )?(?:19|20)\d\d|established (?:in )?(?:19|20)\d\d'
                        r'|since (?:19|20)\d\d|opened (?:in )?(?:19|20)\d\d'
                        r'|(?:19|20)\d\d\s*[-–]\s*20\d\d', re.I)
    weak_a = []
    for r in after:
        if (r.get('icp_fit') or '').strip().lower() != 'a':
            continue
        notes = r.get('notes') or ''
        if not notes.strip() or RESOLVED.search(notes):
            continue
        m = inferred.search(notes)
        if not m:
            continue
        rung = ladder.search(notes)
        lo = max(0, m.start() - 70)
        weak_a.append((r['id'], bool(rung),
                       ' '.join(notes[lo:m.end() + 90].split())))
    norung = [w for w in weak_a if not w[1]]
    print('grade A rows whose notes call must-have 4 inferred or unverified: %d '
          '(of which %d name no ladder artifact anywhere)' % (len(weak_a), len(norung)))
    for rid, rung, snippet in norung:
        print('    %s: ...%s...' % (rid, snippet))


if __name__ == '__main__':
    main()
