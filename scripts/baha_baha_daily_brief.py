"""
Baha Baha Villas — Daily Morning Brief Generator
=================================================
Pulls booking data from Booking Layer API + World Surfaris manual sheet,
formats a daily ops brief using Claude AI, and sends it to the team via SendGrid.

Runs daily at 6:00am WITA (UTC+8) via Render cron job.

Environment variables required:
    ANTHROPIC_API_KEY       — Claude API key
    SENDGRID_API_KEY        — SendGrid API key
    BOOKING_LAYER_API_KEY   — Booking Layer REST API key
    BRIEF_RECIPIENTS        — Comma-separated list of recipient emails
    WORLD_SURFARIS_SHEET_ID — Google Sheet ID for manual WS bookings (optional)
    GOOGLE_SHEETS_CREDS     — Google service account JSON (optional)

Author: WILBA (wilba.ai) for Baha Baha Villas
"""

import os
import json
import logging
import requests
from datetime import date, timedelta, datetime
from zoneinfo import ZoneInfo
import anthropic
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail, Content

# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
log = logging.getLogger(__name__)

WITA = ZoneInfo("Asia/Makassar")  # Sumbawa timezone (UTC+8, same as Bali/WITA)

BOOKING_LAYER_BASE = "https://api.bookinglayer.io/v2"
BOOKING_LAYER_KEY = os.environ.get("BOOKING_LAYER_API_KEY", "")
ANTHROPIC_KEY = os.environ.get("ANTHROPIC_API_KEY", "")
SENDGRID_KEY = os.environ.get("SENDGRID_API_KEY", "")
RECIPIENTS = [e.strip() for e in os.environ.get("BRIEF_RECIPIENTS", "").split(",") if e.strip()]
FROM_EMAIL = os.environ.get("BRIEF_FROM_EMAIL", "ops@bahavillas.com")
FROM_NAME = os.environ.get("BRIEF_FROM_NAME", "Baha Baha Daily Brief")

# ---------------------------------------------------------------------------
# Booking Layer API client
# ---------------------------------------------------------------------------

def bl_headers():
    return {
        "Authorization": f"Bearer {BOOKING_LAYER_KEY}",
        "Accept": "application/json",
        "Content-Type": "application/json",
    }


def bl_get(endpoint: str, params: dict = None) -> list:
    """
    GET from Booking Layer API. Returns list of records or empty list on error.
    Booking Layer uses cursor-based pagination — handles automatically.
    """
    url = f"{BOOKING_LAYER_BASE}/{endpoint.lstrip('/')}"
    all_records = []
    page = 1

    while True:
        p = {**(params or {}), "page": page, "per_page": 100}
        try:
            resp = requests.get(url, headers=bl_headers(), params=p, timeout=15)
            resp.raise_for_status()
            data = resp.json()

            # Booking Layer returns {"data": [...], "meta": {"last_page": N}}
            records = data.get("data", data) if isinstance(data, dict) else data
            if isinstance(records, list):
                all_records.extend(records)
            else:
                all_records.append(records)

            # Pagination
            meta = data.get("meta", {}) if isinstance(data, dict) else {}
            if page >= meta.get("last_page", 1):
                break
            page += 1

        except requests.RequestException as e:
            log.error(f"Booking Layer API error [{endpoint}]: {e}")
            break

    return all_records


# ---------------------------------------------------------------------------
# Fetch today's bookings
# ---------------------------------------------------------------------------

def fetch_checkins(today: date) -> list:
    """Reservations checking in today."""
    return bl_get("reservations", {
        "check_in_from": today.isoformat(),
        "check_in_to": today.isoformat(),
    })


def fetch_checkouts(today: date) -> list:
    """Reservations checking out today."""
    return bl_get("reservations", {
        "check_out_from": today.isoformat(),
        "check_out_to": today.isoformat(),
    })


def fetch_inhouse(today: date) -> list:
    """All guests currently in house (checked in, not yet checked out)."""
    return bl_get("reservations", {
        "check_in_to": today.isoformat(),
        "check_out_from": (today + timedelta(days=1)).isoformat(),
        "status": "checked_in",
    })


def fetch_upcoming(today: date) -> list:
    """Arrivals in the next 48 hours (tomorrow and day after)."""
    tomorrow = today + timedelta(days=1)
    day_after = today + timedelta(days=2)
    return bl_get("reservations", {
        "check_in_from": tomorrow.isoformat(),
        "check_in_to": day_after.isoformat(),
    })


# ---------------------------------------------------------------------------
# Normalise a Booking Layer reservation to readable summary
# ---------------------------------------------------------------------------

def parse_guest_name(res: dict) -> str:
    guest = res.get("guest", {})
    first = guest.get("first_name", "")
    last = guest.get("last_name", "")
    name = f"{first} {last}".strip()
    return name or "Unknown Guest"


def parse_room(res: dict) -> str:
    acc = res.get("accommodation", {})
    return acc.get("name") or res.get("room_type", "Room TBC")


def parse_package(res: dict) -> str:
    """Extract package name from extras or product name."""
    extras = res.get("extras", [])
    if extras:
        names = [e.get("name", "") for e in extras if e.get("name")]
        if names:
            return ", ".join(names)
    return res.get("product_name") or res.get("package_name") or "Accommodation"


def parse_transfer(res: dict, direction: str) -> str:
    """
    direction: 'in' or 'out'
    Returns a readable transfer string or 'No transfer'.
    """
    notes = (res.get("notes") or res.get("internal_notes") or "").lower()
    extras = res.get("extras", [])

    # Check extras for transfer items
    for extra in extras:
        name = (extra.get("name") or "").lower()
        if "transfer" in name or "pickup" in name or "airport" in name:
            return f"Yes — {extra.get('name', 'Transfer')} ({extra.get('notes', 'time TBC')})"

    # Check notes for transfer keywords
    if "transfer" in notes or "pickup" in notes or "airport" in notes:
        return "Yes — check notes for details"

    return "No transfer"


def parse_nights(res: dict) -> int:
    try:
        ci = date.fromisoformat(res.get("check_in", ""))
        co = date.fromisoformat(res.get("check_out", ""))
        return (co - ci).days
    except (ValueError, TypeError):
        return 0


def format_reservation(res: dict, mode: str) -> str:
    """
    mode: 'checkin' | 'checkout' | 'inhouse' | 'upcoming'
    Returns a formatted string for the brief.
    """
    name = parse_guest_name(res)
    room = parse_room(res)
    package = parse_package(res)
    notes = res.get("notes") or res.get("special_requests") or ""
    pax = res.get("pax") or res.get("guest_count") or 1

    if mode == "checkin":
        transfer = parse_transfer(res, "in")
        result = f"• {name} ({pax} pax) — {room} | {package}"
        result += f"\n  Transfer: {transfer}"
        if notes:
            result += f"\n  Notes: {notes}"
        return result

    elif mode == "checkout":
        nights = parse_nights(res)
        transfer = parse_transfer(res, "out")
        result = f"• {name} — {room} | {nights} night{'s' if nights != 1 else ''}"
        result += f"\n  Transfer: {transfer}"
        return result

    elif mode == "inhouse":
        ci = res.get("check_in", "")
        co = res.get("check_out", "")
        nights_remaining = 0
        try:
            today_dt = date.today()
            co_dt = date.fromisoformat(co)
            nights_remaining = (co_dt - today_dt).days
        except (ValueError, TypeError):
            pass
        result = f"• {name} — {room} | {package} | Checking out in {nights_remaining} day{'s' if nights_remaining != 1 else ''}"
        if notes:
            result += f"\n  Notes: {notes}"
        return result

    elif mode == "upcoming":
        ci = res.get("check_in", "")
        transfer = parse_transfer(res, "in")
        result = f"• {ci}: {name} ({pax} pax) — {room} | {package}"
        result += f"\n  Transfer: {transfer}"
        return result

    return f"• {name} — {room}"


# ---------------------------------------------------------------------------
# World Surfaris — manual data (MVP: Google Sheet or JSON file)
# ---------------------------------------------------------------------------

def fetch_world_surfaris_bookings(today: date) -> list:
    """
    MVP: Reads from a local JSON file or Google Sheet.
    File path: data/world_surfaris_bookings.json
    Format: list of booking dicts matching unified data model.
    Returns bookings relevant to today (check-in, check-out, or in-house).
    """
    # Try loading from local file first (manual upload method)
    local_path = os.path.join(os.path.dirname(__file__), "data", "world_surfaris_bookings.json")
    if os.path.exists(local_path):
        try:
            with open(local_path) as f:
                all_bookings = json.load(f)
            # Filter to today-relevant bookings
            relevant = []
            for b in all_bookings:
                try:
                    ci = date.fromisoformat(b.get("check_in_date", ""))
                    co = date.fromisoformat(b.get("check_out_date", ""))
                    if ci == today or co == today or (ci < today < co):
                        relevant.append(b)
                except (ValueError, TypeError):
                    continue
            return relevant
        except Exception as e:
            log.warning(f"Could not load World Surfaris local file: {e}")

    log.info("No World Surfaris data source configured — skipping")
    return []


# ---------------------------------------------------------------------------
# Build the brief text for Claude
# ---------------------------------------------------------------------------

def build_data_summary(
    today: date,
    checkins: list,
    checkouts: list,
    inhouse: list,
    upcoming: list,
    ws_bookings: list,
) -> str:
    """Build a raw structured summary for Claude to reformat."""

    checkin_lines = [format_reservation(r, "checkin") for r in checkins]
    checkout_lines = [format_reservation(r, "checkout") for r in checkouts]
    inhouse_lines = [format_reservation(r, "inhouse") for r in inhouse]
    upcoming_lines = [format_reservation(r, "upcoming") for r in upcoming]

    # Add WS bookings to relevant sections
    ws_checkins_today = [b for b in ws_bookings if b.get("check_in_date") == today.isoformat()]
    ws_checkouts_today = [b for b in ws_bookings if b.get("check_out_date") == today.isoformat()]

    for b in ws_checkins_today:
        name = b.get("guest_name", "WS Guest")
        room = b.get("room_type", "Room TBC")
        pkg = b.get("package_type", "World Surfaris Package")
        checkin_lines.append(f"• {name} — {room} | {pkg} [World Surfaris]")

    for b in ws_checkouts_today:
        name = b.get("guest_name", "WS Guest")
        checkout_lines.append(f"• {name} — [World Surfaris booking]")

    sections = []
    sections.append(f"Date: {today.strftime('%A, %d %B %Y')} (WITA)")

    sections.append(f"\nCHECKING IN TODAY ({len(checkin_lines)} arrival{'s' if len(checkin_lines) != 1 else ''}):")
    sections.append("\n".join(checkin_lines) if checkin_lines else "None")

    sections.append(f"\nCHECKING OUT TODAY ({len(checkout_lines)} departure{'s' if len(checkout_lines) != 1 else ''}):")
    sections.append("\n".join(checkout_lines) if checkout_lines else "None")

    sections.append(f"\nCURRENTLY IN HOUSE ({len(inhouse_lines)} guest{'s' if len(inhouse_lines) != 1 else ''}):")
    sections.append("\n".join(inhouse_lines) if inhouse_lines else "None")

    sections.append(f"\nUPCOMING (next 48 hours — {len(upcoming_lines)} arrival{'s' if len(upcoming_lines) != 1 else ''}):")
    sections.append("\n".join(upcoming_lines) if upcoming_lines else "None")

    # Flags
    flags = []
    if not BOOKING_LAYER_KEY:
        flags.append("⚠️  Booking Layer API key not configured")
    if not checkins and not checkouts and not inhouse:
        flags.append("ℹ️  No bookings data found — verify API connection")
    if ws_bookings == [] and not os.path.exists(
        os.path.join(os.path.dirname(__file__), "data", "world_surfaris_bookings.json")
    ):
        flags.append("⚠️  World Surfaris: no data source configured")

    if flags:
        sections.append("\nFLAGS:")
        sections.append("\n".join(flags))

    return "\n".join(sections)


# ---------------------------------------------------------------------------
# Generate brief with Claude
# ---------------------------------------------------------------------------

def generate_brief_with_claude(raw_data: str, today: date) -> str:
    """Call Claude to turn raw booking data into a polished brief."""
    client = anthropic.Anthropic(api_key=ANTHROPIC_KEY)

    system_prompt = """You are writing the daily operations brief for Baha Baha Villas,
a surf and accommodation property in West Sumbawa, Indonesia.

Your job is to take raw booking data and format it into a clear, readable morning brief
for the property team. The tone is professional but relaxed — surf vibe.

Format using plain text with clear section headers using divider lines.
Keep it scannable — the team reads this in 60 seconds over their morning coffee.
Flag anything that needs attention clearly with ⚠️.
If there's nothing on for the day, say so warmly — "All clear today."
Always note the source of bookings (e.g. [World Surfaris] or [Booking.com]).
Show times in WITA (Sumbawa time) where available."""

    user_prompt = f"""Please format this into the Baha Baha daily ops brief:

{raw_data}

Include sections: Checking In, Checking Out, Transfers Today, Currently In House, Next 48 Hours, Flags.
Add a short one-line summary at the top ("Today at a glance: X arrivals, Y departures, Z in house").
End with a footer: "Powered by WILBA · wilba.ai"
"""

    try:
        message = client.messages.create(
            model="claude-haiku-4-5",
            max_tokens=1500,
            system=system_prompt,
            messages=[{"role": "user", "content": user_prompt}],
        )
        return message.content[0].text
    except Exception as e:
        log.error(f"Claude API error: {e}")
        # Fallback: send raw data without Claude formatting
        return f"BAHA BAHA DAILY OPS BRIEF — {today.strftime('%d %B %Y')}\n\n{raw_data}\n\n[Claude formatting unavailable]"


# ---------------------------------------------------------------------------
# Send via SendGrid
# ---------------------------------------------------------------------------

def send_brief(brief_text: str, today: date) -> bool:
    """Send the daily brief to all recipients via SendGrid."""
    if not RECIPIENTS:
        log.error("No recipients configured in BRIEF_RECIPIENTS")
        return False

    subject = f"🏄 Baha Baha Daily Brief — {today.strftime('%A %d %B')}"

    # HTML version
    html_body = brief_text.replace("\n", "<br>").replace("━", "─")
    html = f"""<html><body style="font-family: monospace; font-size: 14px;
    background: #f9f9f9; padding: 20px; max-width: 700px; margin: auto;">
    <div style="background: white; padding: 24px; border-radius: 8px;
    border-left: 4px solid #1a1a2e;">
    {html_body}
    </div></body></html>"""

    sg = SendGridAPIClient(api_key=SENDGRID_KEY)
    success = True

    for recipient in RECIPIENTS:
        try:
            message = Mail(
                from_email=(FROM_EMAIL, FROM_NAME),
                to_emails=recipient,
                subject=subject,
            )
            message.content = [
                Content("text/plain", brief_text),
                Content("text/html", html),
            ]
            response = sg.send(message)
            log.info(f"Brief sent to {recipient} — status {response.status_code}")
        except Exception as e:
            log.error(f"Failed to send brief to {recipient}: {e}")
            success = False

    return success


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def run():
    now_wita = datetime.now(tz=WITA)
    today = now_wita.date()

    log.info(f"Starting daily brief for {today} (WITA)")

    if not BOOKING_LAYER_KEY:
        log.warning("BOOKING_LAYER_API_KEY not set — brief will have no Booking Layer data")

    # Fetch all booking data
    log.info("Fetching check-ins...")
    checkins = fetch_checkins(today)

    log.info("Fetching check-outs...")
    checkouts = fetch_checkouts(today)

    log.info("Fetching in-house guests...")
    inhouse = fetch_inhouse(today)

    log.info("Fetching upcoming arrivals...")
    upcoming = fetch_upcoming(today)

    log.info("Fetching World Surfaris bookings...")
    ws_bookings = fetch_world_surfaris_bookings(today)

    log.info(f"Data fetched — {len(checkins)} checkins, {len(checkouts)} checkouts, "
             f"{len(inhouse)} inhouse, {len(upcoming)} upcoming, {len(ws_bookings)} WS bookings")

    # Build and format
    raw_summary = build_data_summary(today, checkins, checkouts, inhouse, upcoming, ws_bookings)
    log.info("Generating brief with Claude...")
    brief = generate_brief_with_claude(raw_summary, today)

    # Send
    log.info(f"Sending brief to {len(RECIPIENTS)} recipient(s)...")
    success = send_brief(brief, today)

    if success:
        log.info("Daily brief sent successfully ✓")
    else:
        log.error("Daily brief send failed — check logs")


if __name__ == "__main__":
    run()
