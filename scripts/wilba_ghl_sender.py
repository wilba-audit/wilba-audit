"""Daily sender for WILBA's 10-email clinic outreach, sent through Jess's GHL.

Each run (weekdays only):
  1. For every clinic already in the sequence whose next email is due, check GHL for a
     reply or an opt-out. Anyone who replied or unsubscribed stops for good.
  2. Send the next email to everyone still due.
  3. Start up to the daily cap of new clinics on email 1 (10 a day for the first week,
     then 20), best grade first.

State lives in outputs/pipeline/ghl/send-state.json, committed back by the Action, so
every send is on record.

Modes (first line of outputs/pipeline/ghl/send-request.txt, or --mode):
  dry   work out who is due and what they'd get, send nothing (default)
  test  send email 1 for the first clinic to TEST_EMAIL only, to check how it lands
  live  really send

Env: WILBA_GHL_TOKEN, WILBA_GHL_LOCATION_ID, TEST_EMAIL (test mode).
"""
from __future__ import annotations

import argparse
import csv
import datetime as dt
import json
import os
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from wilba_ghl_load import _req  # noqa: E402
from wilba_ghl_sequence import EMAILS, html_email  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
GHL_DIR = ROOT / "outputs" / "pipeline" / "ghl"
CSV_PATH = GHL_DIR / "ghl-import.csv"
STATE_PATH = GHL_DIR / "send-state.json"
REPORT_PATH = GHL_DIR / "send-report.md"

FROM_NAME = "Jess Morrell"
RAMP = [(5, 10), (None, 20)]  # first 5 send-days: 10 new a day, then 20
GRADE_ORDER = {"A": 0, "B": 1, "C": 2}


def render(text: str, row: dict) -> str:
    values = {
        "cold_subject": row["cold_subject"], "cold_opener": row["cold_opener"],
        "crm_phrase": row["crm_phrase"], "timezone_line": row["tz_line"],
        "currency": row["currency"], "company_name": row["company_name"],
    }
    for k, v in values.items():
        text = text.replace("{{contact.%s}}" % k, v)
    return text


def build_email(step: int, row: dict) -> tuple[str, str]:
    """Return (subject, html) for email number `step` (1-10) for this clinic."""
    _, subject, body, button = EMAILS[step - 1]
    html = html_email(body, button)
    # the opener has paragraph breaks; keep them as separate paragraphs in HTML
    opener_html = row["cold_opener"].replace("\n\n", '</p><p style="margin:0 0 16px">')
    html = html.replace("{{contact.cold_opener}}", opener_html)
    return render(subject, row), render(html, row)


def daily_cap(send_days: int) -> int:
    for upto, cap in RAMP:
        if upto is None or send_days < upto:
            return cap
    return RAMP[-1][1]


def find_contact(token: str, loc: str, email: str) -> dict | None:
    s, d = _req("GET", f"/contacts/search/duplicate?locationId={loc}&email={email}", token)
    return (d or {}).get("contact") if s == 200 else None


def has_replied(token: str, loc: str, contact_id: str) -> bool:
    s, d = _req("GET", f"/conversations/search?locationId={loc}&contactId={contact_id}", token)
    if s != 200:
        return False
    return any(c.get("lastMessageDirection") == "inbound" for c in d.get("conversations", []))


def send(token: str, contact_id: str, subject: str, html: str) -> tuple[bool, str]:
    s, d = _req("POST", "/conversations/messages", token, {
        "type": "Email", "contactId": contact_id, "subject": subject,
        "html": html, "emailFromName": FROM_NAME})
    return s in (200, 201), "" if s in (200, 201) else f"{s}: {str(d)[:200]}"


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--mode", choices=["dry", "test", "live"])
    args = ap.parse_args()
    mode = args.mode
    if not mode:
        req = GHL_DIR / "send-request.txt"
        mode = req.read_text().split()[0].strip() if req.exists() else "dry"
    if mode not in ("dry", "test", "live"):
        sys.exit(f"unknown mode {mode}")

    token, loc = os.environ.get("WILBA_GHL_TOKEN"), os.environ.get("WILBA_GHL_LOCATION_ID")
    if not token or not loc:
        sys.exit("WILBA_GHL_TOKEN and WILBA_GHL_LOCATION_ID must be set.")

    today = dt.date.today()
    rows = {r["pipeline_id"]: r for r in csv.DictReader(CSV_PATH.open(encoding="utf-8"))}
    state = json.loads(STATE_PATH.read_text()) if STATE_PATH.exists() else {"send_days": [], "clinics": {}}
    log: list[str] = []

    if mode == "test":
        test_email = os.environ.get("TEST_EMAIL")
        if not test_email:
            sys.exit("TEST_EMAIL must be set for a test send.")
        row = sorted(rows.values(), key=lambda r: (GRADE_ORDER.get(r["icp_grade"], 9), int(r["pipeline_id"])))[0]
        s, d = _req("POST", "/contacts/upsert", token, {
            "locationId": loc, "email": test_email, "name": "WILBA outreach test",
            "tags": ["outreach-test"]})
        if s not in (200, 201):
            sys.exit(f"could not create test contact ({s}): {d}")
        subject, html = build_email(1, row)
        ok, err = send(token, d["contact"]["id"], f"[TEST] {subject}", html)
        log.append(f"- Test email 1 (as {row['company_name']}) to {test_email}: {'sent' if ok else 'FAILED ' + err}")
        write_report(mode, today, log, state)
        return

    if today.weekday() >= 5:
        log.append("- Weekend: nothing sent.")
        write_report(mode, today, log, state)
        return

    sent_today = 0
    # 1. follow-ups that are due
    for cid, st in sorted(state["clinics"].items()):
        if st.get("stopped") or st["step"] >= len(EMAILS) or st["next_date"] > today.isoformat():
            continue
        row = rows.get(cid)
        if not row:
            continue
        if has_replied(token, loc, st["contact_id"]):
            st["stopped"] = "replied"
            log.append(f"- {row['company_name']}: replied, sequence stopped")
            continue
        nxt = st["step"] + 1
        subject, html = build_email(nxt, row)
        if mode == "live":
            ok, err = send(token, st["contact_id"], subject, html)
            if not ok:
                log.append(f"- {row['company_name']}: email {nxt} FAILED {err}")
                continue
            st["step"] = nxt
            if nxt < len(EMAILS):
                gap = EMAILS[nxt][0] - EMAILS[nxt - 1][0]
                st["next_date"] = (today + dt.timedelta(days=gap)).isoformat()
            time.sleep(1)
        sent_today += 1
        log.append(f"- {row['company_name']}: email {nxt} \"{subject}\"")

    # 2. new clinics on email 1
    cap = daily_cap(len(state["send_days"]))
    fresh = [r for r in rows.values() if r["pipeline_id"] not in state["clinics"]]
    fresh.sort(key=lambda r: (GRADE_ORDER.get(r["icp_grade"], 9), int(r["pipeline_id"])))
    started = 0
    for row in fresh[:cap]:
        contact = find_contact(token, loc, row["email"])
        if not contact:
            log.append(f"- {row['company_name']}: not found in GHL, skipped")
            continue
        if contact.get("dnd"):
            log.append(f"- {row['company_name']}: marked do-not-disturb, skipped")
            continue
        subject, html = build_email(1, row)
        if mode == "live":
            ok, err = send(token, contact["id"], subject, html)
            if not ok:
                log.append(f"- {row['company_name']}: email 1 FAILED {err}")
                continue
            state["clinics"][row["pipeline_id"]] = {
                "contact_id": contact["id"], "step": 1, "started": today.isoformat(),
                "next_date": (today + dt.timedelta(days=EMAILS[1][0])).isoformat()}
            time.sleep(1)
        started += 1
        sent_today += 1
        log.append(f"- {row['company_name']} (new): email 1 \"{subject}\"")

    if mode == "live" and started and today.isoformat() not in state["send_days"]:
        state["send_days"].append(today.isoformat())
    log.insert(0, f"- New clinics started: {started} (cap {cap}) · Emails {'sent' if mode == 'live' else 'that would send'}: {sent_today}")
    if mode == "live":
        STATE_PATH.write_text(json.dumps(state, indent=1) + "\n")
    write_report(mode, today, log, state)


def write_report(mode: str, today: dt.date, log: list[str], state: dict) -> None:
    active = sum(1 for s in state["clinics"].values() if not s.get("stopped") and s["step"] < len(EMAILS))
    replied = sum(1 for s in state["clinics"].values() if s.get("stopped") == "replied")
    head = [f"# Outreach send report ({mode.upper()}, {today.isoformat()})", "",
            f"- In sequence: {active} · Replied: {replied} · Started so far: {len(state['clinics'])} of 100", ""]
    REPORT_PATH.write_text("\n".join(head + log) + "\n", encoding="utf-8")
    print("\n".join(head + log))


if __name__ == "__main__":
    main()
