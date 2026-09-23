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
import argparse, csv, io, json, os, sys
from datetime import date, datetime, timedelta

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSV_PATH = os.path.join(ROOT, 'outputs/pipeline/clinic-pipeline.csv')
LOG_PATH = os.path.join(ROOT, 'outputs/pipeline/send-log.json')

# Cold domain warm-up. jess@wilba.ai has never sent anything, so volume ramps by
# the number of days we have actually sent on, not by calendar date.
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


def load_log():
    if not os.path.exists(LOG_PATH):
        return {'send_days': [], 'note': 'Days on which outreach actually went out. Drives the warm-up ramp.'}
    with open(LOG_PATH) as f:
        return json.load(f)


def save_log(log):
    with open(LOG_PATH, 'w') as f:
        json.dump(log, f, indent=2)
        f.write('\n')


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
    log = load_log()
    cap, day_number = todays_cap(log)

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
                      'days_sent': len(log.get('send_days', []))}))


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
        print(f'   to:       {r["contact_email"]}')
        print(f'   who:      {r.get("lead_doctor") or "not named"}')
        print(f'   where:    {r.get("city","")}, {r.get("country","")}')
        print(f'   crm:      {r.get("crm_detected") or "UNKNOWN - grade C, do not draft"}')
        print(f'   scale:    {r.get("scale_signals","")}')
        print(f'   dormant:  {r.get("dormant_lead_signal","")}')
        print(f'   angle:    {r.get("opening_angle","")}')
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
        print(f'   to:       {r["contact_email"]}')
        print(f'   who:      {r.get("lead_doctor") or "not named"}')
        print(f'   last sent:{r.get("date_last_contact")} ({gap}+ days ago)')
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
        log = load_log()
        if today not in log['send_days']:
            log['send_days'].append(today)
            log['send_days'].sort()
        save_log(log)

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
    args.fn(args)


if __name__ == '__main__':
    main()
