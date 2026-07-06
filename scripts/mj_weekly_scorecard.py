"""Monkey Joe's — weekly scorecard, auto-emailed to Jess.

Refreshes the consolidated data pull (GHL always; Meta + Google once tokens are
set), builds a short HTML scorecard, and emails it to Jess via Resend. Designed
to run every Monday via launchd. Degrades gracefully — sources that aren't wired
yet show "pending" instead of failing.

Run:
  ./.venv/bin/python3 scripts/mj_weekly_scorecard.py            # send
  ./.venv/bin/python3 scripts/mj_weekly_scorecard.py --dry-run  # print, don't send
"""
from __future__ import annotations

import json
import os
import subprocess
import sys
from pathlib import Path
from urllib.request import Request, urlopen
from urllib.error import HTTPError

from dotenv import load_dotenv

ROOT = Path(__file__).resolve().parent.parent
load_dotenv(ROOT / ".env")

CONSOLIDATED = ROOT / "outputs/monkey-joes/reporting/consolidated.json"
RESEND_KEY = os.getenv("RESEND_API_KEY")
TO = "jjessmorrell@gmail.com"
FROM = "MJ Operator <hello@wilba.ai>"


def refresh_data() -> dict:
    """Re-pull consolidated reporting; degrade gracefully if unavailable.

    Uses the current interpreter (sys.executable) so it works in the cloud
    runner as well as the local venv. Never crashes on a missing data file.
    """
    CONSOLIDATED.parent.mkdir(parents=True, exist_ok=True)
    try:
        subprocess.run(
            [sys.executable, str(ROOT / "scripts/fetch_consolidated_reporting.py"), "--days", "30"],
            cwd=ROOT, check=True, capture_output=True, timeout=180,
        )
    except Exception as e:  # noqa: BLE001 — best-effort refresh; carry on with whatever we have
        print(f"⚠ refresh failed: {e}", file=sys.stderr)
    if CONSOLIDATED.exists():
        return json.loads(CONSOLIDATED.read_text())
    print("⚠ no consolidated.json — sending minimal scorecard", file=sys.stderr)
    return {"ghl": {"locations": {}}, "blended_30d": {}, "meta": {}, "google_ads": {}}


def kpi(label: str, value: str, sub: str = "") -> str:
    sub_html = f'<div style="font-size:11px;color:#6b6b6b;margin-top:3px">{sub}</div>' if sub else ""
    return (f'<td style="padding:14px 16px;background:#fff;border:1px solid #EADFC0;border-radius:10px">'
            f'<div style="font-size:24px;font-weight:800;color:#1A1A1A">{value}</div>'
            f'<div style="font-size:12px;color:#6b6b6b;margin-top:4px">{label}</div>{sub_html}</td>')


def build_html(data: dict) -> str:
    ghl = data.get("ghl", {}).get("locations", {})
    pol = ghl.get("POL", {}).get("leads", {})
    wp = ghl.get("WP", {}).get("leads", {})
    opt_30d = data.get("blended_30d", {}).get("leads_ghl", 0)
    meta_on = data.get("meta", {}).get("available")
    google_on = data.get("google_ads", {}).get("available")
    gen = data.get("generated_at", "")[:10]

    spend = data.get("blended_30d", {}).get("spend", {})
    spend_line = (f"Meta ${spend.get('meta',0):.0f} · Google ${spend.get('google',0):.0f}"
                  if (meta_on or google_on) else "pending platform tokens")
    cpl = data.get("blended_30d", {}).get("blended_cpl", 0)
    cpl_str = f"${cpl:.2f}" if cpl else "—"

    flags = []
    if not meta_on:
        flags.append("Meta live reporting <b>not yet wired</b> — paste META_ACCESS_TOKEN to activate.")
    if not google_on:
        flags.append("Google Ads live reporting <b>not yet wired</b> — add GOOGLE_ADS_* creds to activate.")
    flags_html = "".join(f"<li style='margin:4px 0'>{f}</li>" for f in flags)

    return f"""<div style="font-family:-apple-system,Arial,sans-serif;max-width:640px;margin:0 auto;color:#1A1A1A">
  <div style="background:#1A1A1A;color:#fff;padding:20px 24px;border-radius:12px 12px 0 0">
    <div style="font-size:11px;letter-spacing:.12em;text-transform:uppercase;color:#F7B500;font-weight:800">MJ Growth Operator</div>
    <div style="font-size:20px;font-weight:800;margin-top:4px">Weekly Scorecard</div>
    <div style="font-size:12px;color:#c9c9c9;margin-top:4px">Data as of {gen} · last 30 days</div>
  </div>
  <div style="background:#FFFBF2;padding:20px 24px;border:1px solid #EADFC0;border-top:none;border-radius:0 0 12px 12px">
    <table style="width:100%;border-collapse:separate;border-spacing:8px"><tr>
      {kpi("New opt-ins (30d)", str(opt_30d), f"POL {pol.get('last_30d',0)} · WP {wp.get('last_30d',0)}")}
      {kpi("Ad spend (30d)", spend_line if (meta_on or google_on) else "—", spend_line if not (meta_on or google_on) else "")}
      {kpi("Blended cost / opt-in", cpl_str)}
    </tr></table>
    <p style="font-size:14px;margin:16px 0 6px"><b>This week:</b> POL last-7d {pol.get('last_7d',0)} opt-ins · WP last-7d {wp.get('last_7d',0)} opt-ins.</p>
    {"<div style='background:#FFF3F4;border-left:4px solid #E63946;border-radius:0 8px 8px 0;padding:12px 16px;margin-top:12px'><b style='color:#E63946'>Setup to unlock full reporting:</b><ul style='margin:8px 0 0 4px;padding-left:16px;font-size:13px'>" + flags_html + "</ul></div>" if flags else ""}
    <p style="font-size:12px;color:#6b6b6b;margin-top:16px">Automated by the MJ Growth Operator · reply with anything you want changed.</p>
  </div>
</div>"""


def send(html: str) -> int:
    if not RESEND_KEY:
        print("ERROR: RESEND_API_KEY not set", file=sys.stderr); return 1
    payload = json.dumps({
        "from": FROM, "to": [TO], "reply_to": TO,
        "subject": "MJ — weekly scorecard", "html": html,
    }).encode()
    req = Request("https://api.resend.com/emails", method="POST", data=payload,
                  headers={"Authorization": f"Bearer {RESEND_KEY}",
                           "Content-Type": "application/json", "Accept": "application/json"})
    try:
        r = urlopen(req, timeout=30)
        print(f"✓ scorecard sent — HTTP {r.status}"); return 0
    except HTTPError as e:
        print(f"✗ HTTP {e.code} {e.read().decode()[:400]}", file=sys.stderr); return 1


def main() -> int:
    dry = "--dry-run" in sys.argv
    data = refresh_data()
    html = build_html(data)
    if dry:
        out = ROOT / "outputs/monkey-joes/reporting/weekly-scorecard-preview.html"
        out.write_text(html)
        print(f"(dry-run) wrote preview: {out}")
        return 0
    return send(html)


if __name__ == "__main__":
    sys.exit(main())
