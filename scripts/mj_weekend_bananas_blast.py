#!/usr/bin/env python3
"""
Monkey Joe's — Weekend BANANAS campaign blast.

Sends $10-arcade-credits weekend invitation to opted-in MJ contacts.
Runs for BOTH locations (POL + WP). Default mode is dry-run; pass --execute to send.

Usage:
    python3 scripts/mj_weekend_bananas_blast.py --mode email --dry-run
    python3 scripts/mj_weekend_bananas_blast.py --mode email --execute
    python3 scripts/mj_weekend_bananas_blast.py --mode sms   --execute

Scheduled by:
    ~/Library/LaunchAgents/com.wilba.mj-weekend-bananas-email.plist  (Fri 22:00 AEST = Fri 8am ET)
    ~/Library/LaunchAgents/com.wilba.mj-weekend-bananas-sms.plist    (Sun 00:00 AEST = Sat 10am ET)
"""
from __future__ import annotations

import argparse
import json
import os
import sys
import time
from datetime import datetime
from pathlib import Path
from urllib import error, request

ROOT = Path(__file__).resolve().parent.parent
ENV_PATH = ROOT / ".env"
LOG_DIR = ROOT / "outputs/monkey-joes/weekend-bananas-logs"
LOG_DIR.mkdir(parents=True, exist_ok=True)

GHL_BASE = "https://services.leadconnectorhq.com"
GHL_VERSION = "2021-07-28"
GHL_CONV_VERSION = "2021-04-15"
THROTTLE = 0.30  # seconds between GHL calls

# Tags the campaign uses
EXCLUDE_TAG = "unsubscribed"
AUDIENCE_TAG_POL = "voucher-delivered"   # broadest opted-in audience for POL
AUDIENCE_TAG_WP = "voucher-delivered"    # broadest opted-in audience for WP
COHORT_TAG = {
    ("email", "POL"): "weekend-stars-email-pol-2026-06-30",
    ("sms",   "POL"): "weekend-stars-sms-pol-2026-07-02",
    ("email", "WP"):  "weekend-stars-email-wp-2026-06-30",
    ("sms",   "WP"):  "weekend-stars-sms-wp-2026-07-02",
}

SUBJECT = "🇺🇸 $10 arcade credits this 4th of July weekend — say STARS at the door"

EMAIL_HTML = {
    "POL": """<!DOCTYPE html>
<html><body style="margin:0;padding:0;font-family:-apple-system,'Segoe UI',Roboto,sans-serif;background:#FFF8E7;color:#1A1A1A;">
<table width="100%" cellpadding="0" cellspacing="0" style="max-width:600px;margin:0 auto;background:#FFFFFF;padding:32px;border-radius:14px;">
<tr><td>
<h2 style="font-size:24px;margin:0 0 16px;color:#1A1A1A;font-weight:800;">Hi {first_name},</h2>
<p style="font-size:16px;line-height:1.5;margin:0 0 16px;">It's the <strong>4th of July weekend</strong> — and we want to help you keep the kids entertained between fireworks and family time at <strong>Monkey Joe's Pointe Orlando</strong>.</p>
<p style="font-size:16px;line-height:1.5;margin:0 0 20px;">Walk in any time Friday, Saturday, or Sunday this weekend, say <strong>"STARS"</strong> at the front desk, and we'll add <strong>$10 in arcade credits</strong> straight to your card. On us.</p>
<table cellpadding="12" cellspacing="0" style="background:linear-gradient(135deg,#FFF8E7 0%,#FFE9B0 100%);border-radius:8px;margin:20px 0;width:100%;border:2px solid #E63946;">
<tr><td style="font-size:15px;line-height:1.8;">
🇺🇸 <strong>Fri July 3 · Sat July 4 · Sun July 5</strong><br>
🎮 <strong>$10 free arcade credits per family</strong><br>
⭐ <strong>Magic word: STARS</strong>
</td></tr></table>
<p style="font-size:16px;line-height:1.5;margin:20px 0 16px;">No code to print, no form to fill — just walk in and say the word. Air-conditioned indoor play in case the weather decides to surprise you, and a great way to tire the kids out before the evening fireworks.</p>
<p style="font-size:16px;line-height:1.5;margin:0 0 24px;">Have a fantastic 4th!</p>
<p style="font-size:16px;line-height:1.5;margin:0 0 24px;"><strong>The Monkey Joe's Pointe Orlando team</strong></p>
<table cellpadding="0" cellspacing="0" style="border-top:1px solid #EADFC0;padding-top:16px;margin-top:24px;width:100%;">
<tr><td style="font-size:13px;color:#6B7280;line-height:1.5;">
📍 9101 International Dr Suite 2410, Orlando, FL 32819<br>
⏰ Open Fri-Sun 10am-8pm<br><br>
Not coming this weekend? Reply STOP and we'll quit emailing you.
</td></tr></table>
</td></tr></table>
</body></html>""",

    "WP": """<!DOCTYPE html>
<html><body style="margin:0;padding:0;font-family:-apple-system,'Segoe UI',Roboto,sans-serif;background:#FFF8E7;color:#1A1A1A;">
<table width="100%" cellpadding="0" cellspacing="0" style="max-width:600px;margin:0 auto;background:#FFFFFF;padding:32px;border-radius:14px;">
<tr><td>
<h2 style="font-size:24px;margin:0 0 16px;color:#1A1A1A;font-weight:800;">Hi {first_name},</h2>
<p style="font-size:16px;line-height:1.5;margin:0 0 16px;">It's the <strong>4th of July weekend</strong> — and we want to help you keep the kids entertained between fireworks and family time at <strong>Monkey Joe's Winter Park</strong>.</p>
<p style="font-size:16px;line-height:1.5;margin:0 0 20px;">Walk in any time Friday, Saturday, or Sunday this weekend, say <strong>"STARS"</strong> at the front desk, and we'll add <strong>$10 in arcade credits</strong> straight to your card. On us.</p>
<table cellpadding="12" cellspacing="0" style="background:linear-gradient(135deg,#FFF8E7 0%,#FFE9B0 100%);border-radius:8px;margin:20px 0;width:100%;border:2px solid #E63946;">
<tr><td style="font-size:15px;line-height:1.8;">
🇺🇸 <strong>Fri July 3 · Sat July 4 · Sun July 5</strong><br>
🎮 <strong>$10 free arcade credits per family</strong><br>
⭐ <strong>Magic word: STARS</strong>
</td></tr></table>
<p style="font-size:16px;line-height:1.5;margin:20px 0 16px;">No code to print, no form to fill — just walk in and say the word. Air-conditioned indoor play in case the weather decides to surprise you, and a great way to tire the kids out before the evening fireworks.</p>
<p style="font-size:16px;line-height:1.5;margin:0 0 24px;">Have a fantastic 4th!</p>
<p style="font-size:16px;line-height:1.5;margin:0 0 24px;"><strong>The Monkey Joe's Winter Park team</strong></p>
<table cellpadding="0" cellspacing="0" style="border-top:1px solid #EADFC0;padding-top:16px;margin-top:24px;width:100%;">
<tr><td style="font-size:13px;color:#6B7280;line-height:1.5;">
📍 480 N Orlando Ave, Winter Park, FL 32789<br>
⏰ Open Fri-Sun 10am-8pm<br><br>
Not coming this weekend? Reply STOP and we'll quit emailing you.
</td></tr></table>
</td></tr></table>
</body></html>""",
}

SMS_BODY = {
    "POL": "MJ POL 🇺🇸 4th of July weekend at Monkey Joe's! Walk in Fri/Sat/Sun, say STARS at the desk = $10 free arcade credits. Tire the kids before fireworks 🎆 Reply STOP to opt out.",
    "WP":  "MJ WP 🇺🇸 4th of July weekend at Monkey Joe's! Walk in Fri/Sat/Sun, say STARS at the desk = $10 free arcade credits. Tire the kids before fireworks 🎆 Reply STOP to opt out.",
}


def load_env() -> None:
    if not ENV_PATH.exists():
        return
    for line in ENV_PATH.read_text().splitlines():
        if "=" in line and not line.strip().startswith("#"):
            k, v = line.split("=", 1)
            os.environ.setdefault(k.strip(), v.strip().strip('"').strip("'"))


def ghl_post(path: str, api_key: str, payload: dict, version: str = GHL_VERSION) -> tuple[int, dict]:
    req = request.Request(
        f"{GHL_BASE}{path}",
        data=json.dumps(payload).encode(),
        method="POST",
        headers={
            "Authorization": f"Bearer {api_key}",
            "Version": version,
            "Content-Type": "application/json",
            "Accept": "*/*",
            "User-Agent": "wilba-mj/1.0",
        },
    )
    try:
        with request.urlopen(req, timeout=30) as resp:
            return resp.status, json.loads(resp.read())
    except error.HTTPError as e:
        body = e.read().decode("utf-8", errors="replace")[:300]
        return e.code, {"error": body}
    except Exception as e:
        return 0, {"error": str(e)}


def fetch_audience(api_key: str, location_id: str, audience_tag: str) -> list[dict]:
    """Return contacts tagged with audience_tag, excluding those tagged 'unsubscribed'."""
    contacts = []
    page = 1
    while True:
        time.sleep(THROTTLE)
        status, data = ghl_post(
            "/contacts/search",
            api_key,
            {
                "locationId": location_id,
                "pageLimit": 100,
                "page": page,
                "filters": [
                    {"field": "tags", "operator": "contains", "value": audience_tag},
                ],
            },
        )
        if status not in (200, 201):
            print(f"  ⚠ search failed page {page}: {status}  {data}", file=sys.stderr)
            break
        batch = data.get("contacts", [])
        if not batch:
            break
        # Filter out unsubscribed
        filtered = [c for c in batch if EXCLUDE_TAG not in (c.get("tags") or [])]
        contacts.extend(filtered)
        if len(batch) < 100:
            break
        page += 1
    return contacts


def send_message(api_key: str, message_type: str, contact_id: str, *, subject: str = "", html: str = "", body: str = "") -> tuple[int, dict]:
    """Send an email or SMS via GHL conversations/messages."""
    if message_type == "Email":
        payload = {
            "type": "Email",
            "contactId": contact_id,
            "subject": subject,
            "html": html,
            "emailFrom": "Monkey Joe's <hello@monkeyjoespo.com>",
        }
    else:
        payload = {
            "type": "SMS",
            "contactId": contact_id,
            "message": body,
        }
    return ghl_post("/conversations/messages", api_key, payload, version=GHL_CONV_VERSION)


def apply_cohort_tag(api_key: str, contact_id: str, tag: str) -> None:
    time.sleep(THROTTLE)
    ghl_post(
        f"/contacts/{contact_id}/tags",
        api_key,
        {"tags": [tag]},
    )


def run_for_location(loc_name: str, api_key: str, location_id: str, audience_tag: str, mode: str, execute: bool) -> dict:
    print(f"\n--- {loc_name} {mode.upper()} ---")
    contacts = fetch_audience(api_key, location_id, audience_tag)
    print(f"  Audience: {len(contacts)} opted-in contacts (tag={audience_tag}, excluding {EXCLUDE_TAG})")

    cohort = COHORT_TAG[(mode, loc_name)]
    sent = 0
    skipped = 0
    failed = 0
    for c in contacts:
        contact_id = c.get("id") or c.get("_id")
        first = (c.get("firstName") or c.get("contactName") or "there").split(" ")[0]
        if mode == "email":
            if not c.get("email"):
                skipped += 1
                continue
            html = EMAIL_HTML[loc_name].format(first_name=first)
            if not execute:
                continue
            status, _ = send_message(api_key, "Email", contact_id, subject=SUBJECT, html=html)
        else:  # sms
            if not c.get("phone"):
                skipped += 1
                continue
            if not execute:
                continue
            status, _ = send_message(api_key, "SMS", contact_id, body=SMS_BODY[loc_name])
        time.sleep(THROTTLE)
        if status in (200, 201, 202):
            sent += 1
            apply_cohort_tag(api_key, contact_id, cohort)
        else:
            failed += 1

    print(f"  {'(dry-run) would have sent' if not execute else 'sent'}: {sent if execute else len([c for c in contacts if (mode == 'email' and c.get('email')) or (mode == 'sms' and c.get('phone'))])}")
    print(f"  skipped (no contact channel): {skipped}")
    if execute:
        print(f"  failed: {failed}")
    return {
        "location": loc_name,
        "mode": mode,
        "audience": len(contacts),
        "would_send": len([c for c in contacts if (mode == 'email' and c.get('email')) or (mode == 'sms' and c.get('phone'))]),
        "sent": sent,
        "skipped_no_channel": skipped,
        "failed": failed,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", required=True, choices=["email", "sms"])
    parser.add_argument("--execute", action="store_true", help="actually send (default is dry-run)")
    parser.add_argument("--dry-run", action="store_true", help="alias for default behaviour")
    parser.add_argument("--location", choices=["POL", "WP", "BOTH"], default="BOTH")
    args = parser.parse_args()
    execute = args.execute and not args.dry_run

    load_env()

    results = []
    if args.location in ("POL", "BOTH"):
        results.append(run_for_location(
            "POL",
            os.environ["GHL_API_KEY_POL"],
            os.environ["GHL_LOCATION_ID_POL"],
            AUDIENCE_TAG_POL,
            args.mode,
            execute,
        ))
    if args.location in ("WP", "BOTH"):
        results.append(run_for_location(
            "WP",
            os.environ["GHL_API_KEY_WP"],
            os.environ["GHL_LOCATION_ID_WP"],
            AUDIENCE_TAG_WP,
            args.mode,
            execute,
        ))

    log = {
        "timestamp": datetime.now().isoformat(),
        "mode": args.mode,
        "execute": execute,
        "results": results,
    }
    log_file = LOG_DIR / f"blast-{args.mode}-{datetime.now().strftime('%Y-%m-%d-%H%M')}.json"
    log_file.write_text(json.dumps(log, indent=2))
    print(f"\nLog saved: {log_file}")

    print("\n=== SUMMARY ===")
    for r in results:
        if execute:
            print(f"  {r['location']} {r['mode']}: sent={r['sent']}  skipped={r['skipped_no_channel']}  failed={r['failed']}")
        else:
            print(f"  {r['location']} {r['mode']}: would send={r['would_send']}  skipped={r['skipped_no_channel']}  audience={r['audience']}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
