"""Monkey Joe's — 180-day birthday nurture sequence, run as an API drip engine.

Routes around the GHL workflow-builder (which can't be automated via the API).
A cohort is tagged with `birthday-{loc}-lead` + a dated `bday-start-YYYY-MM-DD`
tag; a daily job computes each contact's day-offset and sends the matching
touchpoint via the GHL messages API. Idempotent: each sent touchpoint stamps a
`bday-sent-d{N}` tag so it never resends. Exits on `birthday-{loc}-booked` or
`unsubscribed`.

Design source: outputs/monkey-joes/MJ-180Day-Birthday-Sequence-2026-06-22.md

Commands:
  # 1) Tag the starting cohort (dry-run unless --execute)
  python3 scripts/mj_birthday_sequence.py tag-cohort --loc POL --execute
  python3 scripts/mj_birthday_sequence.py tag-cohort --loc WP  --execute

  # 2) Daily drip — sends whatever is due today (dry-run unless --execute)
  python3 scripts/mj_birthday_sequence.py run --execute

  # Status snapshot
  python3 scripts/mj_birthday_sequence.py status
"""
from __future__ import annotations

import argparse
import importlib.util
import os
import sys
from datetime import date, datetime, timezone
from pathlib import Path

from dotenv import load_dotenv

ROOT = Path(__file__).resolve().parent.parent
load_dotenv(ROOT / ".env")

# Reuse the proven GHL helpers from the weekend blast module.
_spec = importlib.util.spec_from_file_location("blast", str(ROOT / "scripts/mj_weekend_bananas_blast.py"))
blast = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(blast)

LOCS = {
    "POL": (os.getenv("GHL_API_KEY_POL"), os.getenv("GHL_LOCATION_ID_POL")),
    "WP":  (os.getenv("GHL_API_KEY_WP"),  os.getenv("GHL_LOCATION_ID_WP")),
}
AUDIENCE_TAG = "voucher-delivered"      # warm, opted-in parents at each location
EXCLUDE = "unsubscribed"
FROM_EMAIL = "Monkey Joe's <hello@monkeyjoespo.com>"

BOOK_LINK = "https://monkeyjoespo.com/birthday-party"   # LP (both locations route here today)

# ── Email shell ─────────────────────────────────────────────────────────────
def email_html(first: str, body: str) -> str:
    hi = f"Hi {first}," if first else "Hi there,"
    return f"""<div style="font-family:-apple-system,'Segoe UI',Arial,sans-serif;max-width:560px;margin:0 auto;color:#1A1A1A;line-height:1.55;font-size:16px">
<p>{hi}</p>
{body}
<p style="margin-top:22px"><a href="{BOOK_LINK}" style="background:#F7B500;color:#1A1A1A;font-weight:800;text-decoration:none;padding:12px 22px;border-radius:999px;display:inline-block">Plan the party →</a></p>
<p style="color:#6b6b6b;font-size:13px;margin-top:26px">Monkey Joe's · the easiest birthday you'll ever throw 🎈<br>
<a href="{{{{unsubscribe_url}}}}" style="color:#9a9a9a">Unsubscribe</a></p>
</div>"""

# ── The 10 touchpoints (day offset from cohort start) ───────────────────────
TOUCHPOINTS = [
    {"day": 0, "channel": "both",
     "subject": "Your Monkey Joe's birthday — let's plan it 🎉",
     "body": "<p>Throwing a birthday your kid will actually remember shouldn't take a spreadsheet and three weekends of stress. At Monkey Joe's, we do the setup, the fun, and the cleanup — you just show up.</p>"
             "<p>Our <strong>Jungle Experience party starts at $234</strong> and includes dedicated party space, a host who runs the whole thing, unlimited play, and happy, worn-out kids by the end.</p>",
     "sms": "Monkey Joe's 🎉 Got a birthday coming up? Our Jungle Experience parties start at $234 — we do it all, you just show up. Details: " + BOOK_LINK + " Reply STOP to opt out."},

    {"day": 2, "channel": "email",
     "subject": "What's included in the Jungle Experience ($234)",
     "body": "<p>Here's exactly what you get in the <strong>Jungle Experience</strong>:</p>"
             "<ul><li>Private party room + a dedicated party host</li><li>Unlimited play on the inflatables the whole time</li><li>Plates, cups, napkins & setup — sorted</li><li>A stress-free hour and a half that runs itself</li></ul>"
             "<p>Add pizza, slushies, or an upgraded package if you want — but the base already covers the essentials.</p>"},

    {"day": 5, "channel": "email",
     "subject": "Why parents say MJ birthdays are the easiest",
     "body": "<p>The #1 thing parents tell us after their party: <em>\"I didn't have to do anything.\"</em></p>"
             "<p>No decorating your living room. No 12 kids in your house. No cleanup at 8pm. Just a host who runs the show while you actually enjoy it and take the photos.</p>"},

    {"day": 10, "channel": "both",
     "subject": "Book by Friday — host upgrade on us",
     "body": "<p>Quick one: book your party this week and we'll add the <strong>upgraded host package free</strong> — extra hands so you don't lift a finger.</p>"
             "<p>Weekend suites book out first, so if you've got a date in mind, now's the time to lock it.</p>",
     "sms": "MJ 🎈 Book your birthday party by Friday & get the host upgrade FREE. Weekend slots go fast — lock your date: " + BOOK_LINK + " Reply STOP to opt out."},

    {"day": 21, "channel": "email",
     "subject": "We held a slot for you",
     "body": "<p>Still thinking about the birthday? We get it — life's busy. We've kept a party slot open for you.</p>"
             "<p>Tell us the rough date and we'll check availability and hold it, no commitment. Easiest text you'll send all week.</p>"},

    {"day": 45, "channel": "email",
     "subject": "What month is the big day?",
     "body": "<p>Planning ahead pays off — the best weekend times go early.</p>"
             "<p>If your child's birthday is coming up in the next few months, reply with the month and we'll flag the prime slots before they're gone.</p>"},

    {"day": 75, "channel": "email",
     "subject": "Weekday parties from $194 — same Jungle Experience",
     "body": "<p>Weekends filling up? A <strong>weekday party starts at just $194</strong> — the exact same Jungle Experience, quieter floor, and often the kids' favourite because they get more run of the place.</p>"},

    {"day": 120, "channel": "email",
     "subject": "Quick hello from Monkey Joe's 👋",
     "body": "<p>Just checking in! We've got new party packages and a few seasonal add-ons since we last spoke.</p>"
             "<p>Whenever a birthday (or any excuse for a party) rolls around, we're here and it's easy.</p>"},

    {"day": 150, "channel": "email",
     "subject": "Booking next quarter? Lock in a Saturday suite",
     "body": "<p>If there's a birthday on the horizon, Saturday suites for next quarter are opening up now.</p>"
             "<p>Grab your preferred time early and it's one less thing on your list.</p>"},

    {"day": 180, "channel": "both",
     "subject": "Your child's birthday is coming up again 🎉",
     "body": "<p>Around this time last year you looked into a Monkey Joe's birthday — which means another one might be right around the corner!</p>"
             "<p>Want us to make it easy again? Same Jungle Experience, same zero-stress setup. Just say the word.</p>",
     "sms": "MJ 🎉 Birthday season again? Let's make it easy like last time — Jungle Experience from $234. Plan it: " + BOOK_LINK + " Reply STOP to opt out."},
]


def today() -> date:
    return datetime.now(timezone.utc).date()


def start_tag(d: date) -> str:
    return f"bday-start-{d.isoformat()}"


def parse_start(tags: list[str]) -> date | None:
    for t in tags:
        if t.startswith("bday-start-"):
            try:
                return date.fromisoformat(t[len("bday-start-"):])
            except ValueError:
                continue
    return None


# ── tag-cohort ──────────────────────────────────────────────────────────────
def cmd_tag_cohort(args) -> int:
    loc = args.loc
    key, lid = LOCS[loc]
    if not key:
        sys.exit(f"ERROR: GHL creds for {loc} missing.")
    lead_tag = f"birthday-{loc.lower()}-lead"
    contacts = blast.fetch_audience(key, lid, AUDIENCE_TAG)
    fresh = [c for c in contacts
             if lead_tag not in (c.get("tags") or [])
             and EXCLUDE not in (c.get("tags") or [])]
    st = start_tag(today())
    print(f"{loc}: {len(contacts)} {AUDIENCE_TAG} · {len(fresh)} to enroll (start={st})")
    if not args.execute:
        print("  (dry-run) add --execute to tag + enroll."); return 0
    for c in fresh:
        blast.apply_cohort_tag(key, c["id"], lead_tag)
        blast.apply_cohort_tag(key, c["id"], st)
    print(f"  ✓ enrolled {len(fresh)} contacts. Day-0 fires on the next `run --execute`.")
    return 0


# ── run (daily drip) ────────────────────────────────────────────────────────
def _send_touchpoint(key: str, c: dict, tp: dict, execute: bool) -> str:
    first = (c.get("firstName") or "").strip()
    cid = c["id"]
    if tp["channel"] in ("email", "both") and c.get("email"):
        if execute:
            blast.send_message(key, "Email", cid, subject=tp["subject"],
                               html=email_html(first, tp["body"]))
    if tp["channel"] in ("sms", "both") and c.get("phone") and tp.get("sms"):
        if execute:
            blast.send_message(key, "SMS", cid, body=tp["sms"])
    if execute:
        blast.apply_cohort_tag(key, cid, f"bday-sent-d{tp['day']}")
    return f"d{tp['day']}"


def cmd_run(args) -> int:
    locs = [args.loc] if args.loc else ["POL", "WP"]
    t = today()
    grand = 0
    for loc in locs:
        key, lid = LOCS[loc]
        if not key:
            continue
        lead_tag = f"birthday-{loc.lower()}-lead"
        booked = f"birthday-{loc.lower()}-booked"
        contacts = blast.fetch_audience(key, lid, lead_tag)
        sent_here = 0
        for c in contacts:
            tags = c.get("tags") or []
            if EXCLUDE in tags or booked in tags:
                continue
            start = parse_start(tags)
            if not start:
                continue
            days = (t - start).days
            due = [tp for tp in TOUCHPOINTS
                   if tp["day"] <= days and f"bday-sent-d{tp['day']}" not in tags]
            for tp in due:
                label = _send_touchpoint(key, c, tp, args.execute)
                sent_here += 1
                grand += 1
        mode = "SENT" if args.execute else "would send"
        print(f"{loc}: {mode} {sent_here} touchpoint(s) across {len(contacts)} enrolled (day-of-cohort basis, {t})")
    if not args.execute:
        print("(dry-run) add --execute to send.")
    return 0


def cmd_status(_args) -> int:
    t = today()
    for loc in ("POL", "WP"):
        key, lid = LOCS[loc]
        if not key:
            continue
        enrolled = blast.fetch_audience(key, lid, f"birthday-{loc.lower()}-lead")
        booked = blast.fetch_audience(key, lid, f"birthday-{loc.lower()}-booked")
        print(f"{loc}: {len(enrolled)} enrolled · {len(booked)} booked")
    print(f"(as of {t})")
    return 0


def main() -> int:
    p = argparse.ArgumentParser(description="MJ birthday drip engine")
    sub = p.add_subparsers(dest="cmd", required=True)

    tc = sub.add_parser("tag-cohort"); tc.add_argument("--loc", required=True, choices=["POL", "WP"])
    tc.add_argument("--execute", action="store_true"); tc.set_defaults(func=cmd_tag_cohort)

    r = sub.add_parser("run"); r.add_argument("--loc", choices=["POL", "WP"])
    r.add_argument("--execute", action="store_true"); r.set_defaults(func=cmd_run)

    sub.add_parser("status").set_defaults(func=cmd_status)

    args = p.parse_args()
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
