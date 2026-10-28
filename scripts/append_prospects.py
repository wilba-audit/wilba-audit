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
    names = {r['clinic_name'].strip().lower() for r in existing}
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
            elif cn.lower() in names:
                why = 'duplicate clinic already in the pipeline'
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
            if fit.upper() not in ('A', 'B', 'C') and flag.upper() in ('A', 'B', 'C'):
                fit, flag = flag, fit
            if fit.upper() not in ('A', 'B', 'C'):
                rejected.append((cn, 'no A/B/C grade in icp_fit or fit_flag')); continue

            names.add(cn.lower()); emails.add(em.lower())
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


if __name__ == '__main__':
    main()
