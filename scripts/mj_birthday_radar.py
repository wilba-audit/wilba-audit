"""Monkey Joe's — birthday-anchored reminder engine ("birthday radar").

The precision play: for every contact with a CHILD's birthday on file, reach out
on a weekly cadence at fixed windows BEFORE the birthday — 90 days (start
planning), 60 days (lock your date), 30 days (final call). This is different from
mj_birthday_sequence.py, which drips from enrollment date; this one anchors to
the child's actual birthday.

Run it WEEKLY. It scans the list, finds anyone whose child's birthday lands
inside a target window this run, and sends the matching reminder once per year
(idempotent via `bday-radar-{window}-{year}` tags).

DATA REQUIREMENT: needs each child's birthday. It reads, in order:
  1. a custom field id (CHILD_BDAY_FIELD_ID in .env) — preferred, set this once
  2. the GHL contact `dateOfBirth` field — fallback (often the parent's, so only
     used if no custom field is configured)
Most contacts don't have this yet — run the data-capture campaign first
(mj_birthday_capture) to populate it. Until then this sends to very few people,
which is correct, not broken.

Usage:
  python3 scripts/mj_birthday_radar.py run            # dry-run: who is due this week
  python3 scripts/mj_birthday_radar.py run --execute  # send the due reminders
  python3 scripts/mj_birthday_radar.py coverage       # how many contacts have a usable birthday
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

_spec = importlib.util.spec_from_file_location("blast", str(ROOT / "scripts/mj_weekend_bananas_blast.py"))
blast = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(blast)

LOCS = {
    "POL": (os.getenv("GHL_API_KEY_POL"), os.getenv("GHL_LOCATION_ID_POL")),
    "WP":  (os.getenv("GHL_API_KEY_WP"),  os.getenv("GHL_LOCATION_ID_WP")),
}
AUDIENCE_TAG = "voucher-delivered"
EXCLUDE = "unsubscribed"
CHILD_BDAY_FIELD_ID = os.getenv("CHILD_BDAY_FIELD_ID")  # set once you create the field
BOOK_LINK = "https://monkeyjoespo.com/birthday-party"

# Weekly cadence: a birthday falling this many days out (± half a week) gets the reminder.
WINDOWS = [
    {"days": 90, "grace": 4, "key": "90",
     "subject": "3 months to the big day — let's start planning 🎉",
     "body": "<p>Your child's birthday is about <strong>three months away</strong> — the perfect time to lock in the date before the best weekend slots go.</p>"
             "<p>Our Jungle Experience party (from $314) does it all: private room, a dedicated host, unlimited play, and zero cleanup for you.</p>",
     "sms": "Monkey Joe's 🎉 Birthday's ~3 months out — prime time to book the date! Jungle Experience from $314, we do it all: " + BOOK_LINK + " Reply STOP to opt out."},
    {"days": 60, "grace": 4, "key": "60",
     "subject": "2 months out — lock in your party date",
     "body": "<p>The birthday's about <strong>two months away</strong>. Weekend suites are booking up — grab your preferred time now and it's one less thing to think about.</p>"
             "<p>Tell us the date and we'll hold it, no commitment.</p>"},
    {"days": 30, "grace": 4, "key": "30",
     "subject": "One month to go — let's make it easy 🎈",
     "body": "<p>The big day is about <strong>a month away</strong>! If you haven't sorted the party yet, we can still make it the easiest thing on your list.</p>"
             "<p>Pick a time, we handle the rest — setup, host, play, cleanup.</p>",
     "sms": "MJ 🎈 Birthday's ~1 month away! Still need a venue? We've got you — book in minutes: " + BOOK_LINK + " Reply STOP to opt out."},
]


def today() -> date:
    return datetime.now(timezone.utc).date()


def child_birthday(c: dict) -> date | None:
    """Return the child's birthday as a date (year ignored downstream)."""
    raw = None
    if CHILD_BDAY_FIELD_ID:
        for f in (c.get("customFields") or []):
            if f.get("id") == CHILD_BDAY_FIELD_ID:
                raw = f.get("value") or f.get("fieldValue")
                break
    if not raw:
        raw = c.get("dateOfBirth")
    if not raw:
        return None
    for fmt in ("%Y-%m-%d", "%Y-%m-%dT%H:%M:%S.%fZ", "%m/%d/%Y", "%m-%d-%Y"):
        try:
            return datetime.strptime(str(raw)[:len("2020-01-01T00:00:00.000Z")], fmt).date() \
                if "T" in str(raw) else datetime.strptime(str(raw), fmt).date()
        except ValueError:
            continue
    return None


def days_until_next_birthday(bday: date, ref: date) -> int:
    """Days from ref until the next occurrence of this month/day."""
    this_year = bday.replace(year=ref.year)
    if this_year < ref:
        this_year = bday.replace(year=ref.year + 1)
    return (this_year - ref).days


def cmd_coverage(_args) -> int:
    for loc, (key, lid) in LOCS.items():
        if not key:
            continue
        contacts = blast.fetch_audience(key, lid, AUDIENCE_TAG)
        have = sum(1 for c in contacts if child_birthday(c))
        src = "custom field" if CHILD_BDAY_FIELD_ID else "dateOfBirth fallback (likely parent)"
        print(f"{loc}: {have}/{len(contacts)} have a usable birthday  (source: {src})")
    if not CHILD_BDAY_FIELD_ID:
        print("\n⚠ CHILD_BDAY_FIELD_ID not set — run the data-capture campaign, then set it in .env.")
    return 0


def cmd_run(args) -> int:
    ref = today()
    yr = ref.year
    for loc, (key, lid) in LOCS.items():
        if not key:
            continue
        contacts = blast.fetch_audience(key, lid, AUDIENCE_TAG)
        sent = 0
        for c in contacts:
            tags = c.get("tags") or []
            if EXCLUDE in tags:
                continue
            bday = child_birthday(c)
            if not bday:
                continue
            dtn = days_until_next_birthday(bday, ref)
            for w in WINDOWS:
                stamp = f"bday-radar-{w['key']}-{yr}"
                if abs(dtn - w["days"]) <= w["grace"] and stamp not in tags:
                    if args.execute:
                        first = (c.get("firstName") or "").strip()
                        hi = f"Hi {first}," if first else "Hi there,"
                        html = (f"<div style=\"font-family:-apple-system,Arial,sans-serif;max-width:560px;margin:0 auto;color:#1A1A1A;line-height:1.55;font-size:16px\">"
                                f"<p>{hi}</p>{w['body']}"
                                f"<p style='margin-top:20px'><a href='{BOOK_LINK}' style='background:#F7B500;color:#1A1A1A;font-weight:800;text-decoration:none;padding:12px 22px;border-radius:999px;display:inline-block'>Plan the party →</a></p>"
                                f"<p style='color:#6b6b6b;font-size:13px;margin-top:24px'><a href='{{{{unsubscribe_url}}}}' style='color:#9a9a9a'>Unsubscribe</a></p></div>")
                        if c.get("email"):
                            blast.send_message(key, "Email", c["id"], subject=w["subject"], html=html)
                        if c.get("phone") and w.get("sms"):
                            blast.send_message(key, "SMS", c["id"], body=w["sms"])
                        blast.apply_cohort_tag(key, c["id"], stamp)
                    sent += 1
                    break  # one reminder per contact per run
        mode = "SENT" if args.execute else "would send"
        print(f"{loc}: {mode} {sent} birthday reminder(s) this week ({ref})")
    if not args.execute:
        print("(dry-run) add --execute to send.")
    return 0


def main() -> int:
    p = argparse.ArgumentParser(description="MJ birthday radar (birthday-anchored reminders)")
    sub = p.add_subparsers(dest="cmd", required=True)
    r = sub.add_parser("run"); r.add_argument("--execute", action="store_true"); r.set_defaults(func=cmd_run)
    sub.add_parser("coverage").set_defaults(func=cmd_coverage)
    args = p.parse_args()
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
