"""
Baha Baha Villas — Multi-Language AI Email Responder
=====================================================
Monitors the Baha Baha Gmail inbox for new guest emails.
Detects language, classifies intent, and saves a draft reply
in the guest's language for the owner to review and send.

Runs every 15 minutes via Render cron job.

Environment variables required:
    ANTHROPIC_API_KEY       — Claude API key
    GMAIL_CREDENTIALS_JSON  — OAuth2 client credentials JSON (as string)
    GMAIL_TOKEN_JSON        — OAuth2 refresh token JSON (as string)
    GMAIL_USER              — Gmail address to monitor (e.g. bookings@bahavillas.com)
    AUTO_SEND_FAQS          — 'true' to auto-send FAQ replies (default: false)
    TEAM_EMAILS             — Comma-separated team email addresses (to skip monitoring)

Author: WILBA (wilba.ai) for Baha Baha Villas
"""

import os
import json
import base64
import logging
from datetime import datetime, timezone
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

import anthropic
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
log = logging.getLogger(__name__)

ANTHROPIC_KEY = os.environ.get("ANTHROPIC_API_KEY", "")
GMAIL_USER = os.environ.get("GMAIL_USER", "")
AUTO_SEND_FAQS = os.environ.get("AUTO_SEND_FAQS", "false").lower() == "true"
TEAM_EMAILS = [e.strip().lower() for e in os.environ.get("TEAM_EMAILS", "").split(",") if e.strip()]

# Gmail API scopes
SCOPES = [
    "https://www.googleapis.com/auth/gmail.readonly",
    "https://www.googleapis.com/auth/gmail.compose",
    "https://www.googleapis.com/auth/gmail.send",
    "https://www.googleapis.com/auth/gmail.modify",
]

# Intent categories and their auto-send eligibility
INTENT_CONFIG = {
    "faq": {"label": "FAQ", "auto_send": True, "description": "General questions about the property"},
    "availability": {"label": "Availability Inquiry", "auto_send": False, "description": "Asking about room availability"},
    "pricing": {"label": "Pricing Inquiry", "auto_send": False, "description": "Asking about rates"},
    "transfer": {"label": "Transfer Request", "auto_send": False, "description": "Airport/ferry transfer"},
    "surf_inquiry": {"label": "Surf Package Inquiry", "auto_send": False, "description": "Questions about surf packages"},
    "booking_request": {"label": "Booking Request", "auto_send": False, "description": "Wants to make a booking"},
    "modification": {"label": "Booking Modification", "auto_send": False, "description": "Change to existing booking"},
    "cancellation": {"label": "Cancellation", "auto_send": False, "description": "Cancel a booking"},
    "other": {"label": "Other", "auto_send": False, "description": "Unclassified — needs review"},
}

# Property knowledge base for Claude
PROPERTY_KNOWLEDGE = """
BAHA BAHA VILLAS — Property Information for AI Receptionist

Location: West Sumbawa, Indonesia
Setting: Surf and accommodation property near world-class wave breaks
Email: bookings@[bahavillas]  [UPDATE WITH REAL EMAIL]
Website: [UPDATE WITH REAL WEBSITE]

Booking System: Booking Layer
Channel Manager: Channex (connects to Booking.com, Agoda, and other OTAs)
Surf Partner: World Surfaris (packages available)

Transfers: Airport pickups available from Sumbawa Besar / Taliwang airports

General:
- Check-in: [CONFIRM TIME] | Check-out: [CONFIRM TIME]
- WiFi available
- On-site restaurant / meals available (confirm current meal plan options with owner)
- Located near [CONFIRM NEAREST SURF BREAKS]

For pricing and exact availability: Always direct guests to book via website or
say "we'll confirm availability and rates by email shortly."

Do NOT quote specific prices unless owner updates this file with confirmed rates.
Flag any complex or unusual requests with [REVIEW NEEDED] for the owner.
"""


# ---------------------------------------------------------------------------
# Gmail authentication
# ---------------------------------------------------------------------------

def get_gmail_service():
    """Authenticate and return Gmail API service."""
    creds = None

    # Load credentials from environment variables
    creds_json = os.environ.get("GMAIL_CREDENTIALS_JSON", "")
    token_json = os.environ.get("GMAIL_TOKEN_JSON", "")

    if token_json:
        try:
            token_data = json.loads(token_json)
            creds = Credentials.from_authorized_user_info(token_data, SCOPES)
        except Exception as e:
            log.error(f"Failed to load Gmail token: {e}")

    # Refresh if expired
    if creds and creds.expired and creds.refresh_token:
        try:
            creds.refresh(Request())
            log.info("Gmail credentials refreshed")
        except Exception as e:
            log.error(f"Failed to refresh Gmail token: {e}")
            return None

    if not creds or not creds.valid:
        log.error("Gmail credentials invalid — run setup to re-authenticate")
        return None

    return build("gmail", "v1", credentials=creds)


# ---------------------------------------------------------------------------
# Email fetching and parsing
# ---------------------------------------------------------------------------

def get_unread_guest_emails(service) -> list:
    """
    Fetch unread emails from guests (not from team, not automated).
    Returns list of email dicts with id, from, subject, body, date.
    """
    try:
        # Search for unread emails not from the team
        query = "is:unread -is:draft"
        if TEAM_EMAILS:
            for team_email in TEAM_EMAILS:
                query += f" -from:{team_email}"

        # Also skip common automated senders
        query += " -from:noreply -from:no-reply -from:donotreply"

        results = service.users().messages().list(
            userId="me",
            q=query,
            maxResults=20,
        ).execute()

        messages = results.get("messages", [])
        emails = []

        for msg_meta in messages:
            msg = service.users().messages().get(
                userId="me",
                id=msg_meta["id"],
                format="full",
            ).execute()

            parsed = parse_email(msg)
            if parsed:
                emails.append(parsed)

        return emails

    except HttpError as e:
        log.error(f"Gmail API error fetching emails: {e}")
        return []


def parse_email(msg: dict) -> dict | None:
    """Parse Gmail message into a clean dict."""
    headers = {h["name"]: h["value"] for h in msg.get("payload", {}).get("headers", [])}

    from_addr = headers.get("From", "")
    subject = headers.get("Subject", "(no subject)")
    date_str = headers.get("Date", "")

    # Skip if from ourselves
    if GMAIL_USER and GMAIL_USER.lower() in from_addr.lower():
        return None

    # Extract body
    body = extract_body(msg.get("payload", {}))

    if not body or len(body.strip()) < 10:
        return None

    return {
        "id": msg["id"],
        "thread_id": msg.get("threadId"),
        "from": from_addr,
        "subject": subject,
        "date": date_str,
        "body": body[:3000],  # Truncate very long emails
        "snippet": msg.get("snippet", ""),
    }


def extract_body(payload: dict) -> str:
    """Recursively extract plain text body from Gmail message payload."""
    mime_type = payload.get("mimeType", "")
    body_data = payload.get("body", {}).get("data", "")

    if body_data and "text/plain" in mime_type:
        return base64.urlsafe_b64decode(body_data).decode("utf-8", errors="ignore")

    # Try HTML if no plain text
    if body_data and "text/html" in mime_type:
        html = base64.urlsafe_b64decode(body_data).decode("utf-8", errors="ignore")
        # Basic HTML strip (no beautifulsoup dependency)
        import re
        return re.sub(r"<[^>]+>", " ", html)

    # Recurse into parts
    for part in payload.get("parts", []):
        result = extract_body(part)
        if result:
            return result

    return ""


# ---------------------------------------------------------------------------
# Claude AI — language detection, classification, response generation
# ---------------------------------------------------------------------------

def analyse_and_respond(email: dict) -> dict | None:
    """
    Use Claude to:
    1. Detect the language of the email
    2. Classify the intent
    3. Generate a reply in the guest's language

    Returns dict with: language, intent, reply_subject, reply_body
    """
    client = anthropic.Anthropic(api_key=ANTHROPIC_KEY)

    analysis_prompt = f"""You are the AI receptionist for Baha Baha Villas, a surf and accommodation
property in West Sumbawa, Indonesia.

PROPERTY INFORMATION:
{PROPERTY_KNOWLEDGE}

INCOMING EMAIL:
From: {email['from']}
Subject: {email['subject']}
Date: {email['date']}
Body:
{email['body']}

---

Please do the following:

1. DETECT THE LANGUAGE of this email (return the language name in English, e.g. "French", "Indonesian")

2. CLASSIFY THE INTENT as exactly one of:
   - faq (general questions: WiFi, check-in time, food, location, amenities)
   - availability (asking if rooms are free on specific dates)
   - pricing (asking about rates, costs, packages)
   - transfer (airport/ferry pickup or drop requests)
   - surf_inquiry (surf packages, surf guiding, equipment)
   - booking_request (wants to make a new booking)
   - modification (change to existing booking)
   - cancellation (cancel a booking)
   - other (anything that doesn't fit above)

3. WRITE A REPLY in the SAME LANGUAGE as the guest's email.
   - Be warm, friendly, and reflect a laid-back surf/island vibe
   - Be helpful and informative
   - For availability/pricing: say you'll confirm shortly, don't invent numbers
   - For bookings: thank them and say you'll confirm availability ASAP
   - For FAQs: answer based on the property information provided
   - Add [REVIEW NEEDED] at the start if anything needs owner attention
   - Sign off as "The Baha Baha Team"

Return your response as valid JSON with these exact keys:
{{
  "language": "English",
  "intent": "faq",
  "reply_subject": "Re: [original subject]",
  "reply_body": "Full reply text in the guest's language..."
}}

Return ONLY the JSON object, no other text."""

    try:
        message = client.messages.create(
            model="claude-sonnet-4-5",
            max_tokens=1000,
            messages=[{"role": "user", "content": analysis_prompt}],
        )

        response_text = message.content[0].text.strip()

        # Extract JSON (handle any wrapping)
        if response_text.startswith("```"):
            response_text = response_text.split("```")[1]
            if response_text.startswith("json"):
                response_text = response_text[4:]

        result = json.loads(response_text)
        return result

    except json.JSONDecodeError as e:
        log.error(f"Claude returned invalid JSON: {e}")
        return None
    except Exception as e:
        log.error(f"Claude API error for email {email['id']}: {e}")
        return None


# ---------------------------------------------------------------------------
# Gmail draft creation and sending
# ---------------------------------------------------------------------------

def create_draft(service, original_email: dict, reply: dict) -> str | None:
    """Save a draft reply to Gmail. Returns draft ID."""
    try:
        # Build MIME message
        msg = MIMEMultipart("alternative")
        msg["To"] = original_email["from"]
        msg["Subject"] = reply.get("reply_subject", f"Re: {original_email['subject']}")
        msg["In-Reply-To"] = original_email["id"]
        msg["References"] = original_email["id"]

        # Plain text body
        text_part = MIMEText(reply["reply_body"], "plain", "utf-8")
        msg.attach(text_part)

        # Encode
        raw = base64.urlsafe_b64encode(msg.as_bytes()).decode()

        draft_body = {
            "message": {
                "raw": raw,
                "threadId": original_email.get("thread_id"),
            }
        }

        draft = service.users().drafts().create(userId="me", body=draft_body).execute()
        log.info(f"Draft created for email from {original_email['from']} — draft ID: {draft['id']}")
        return draft["id"]

    except HttpError as e:
        log.error(f"Failed to create Gmail draft: {e}")
        return None


def send_reply(service, original_email: dict, reply: dict) -> bool:
    """Auto-send a reply (used only for FAQ intent when AUTO_SEND_FAQS=true)."""
    try:
        msg = MIMEMultipart("alternative")
        msg["To"] = original_email["from"]
        msg["Subject"] = reply.get("reply_subject", f"Re: {original_email['subject']}")
        msg["In-Reply-To"] = original_email["id"]
        msg["References"] = original_email["id"]

        text_part = MIMEText(reply["reply_body"], "plain", "utf-8")
        msg.attach(text_part)

        raw = base64.urlsafe_b64encode(msg.as_bytes()).decode()

        message_body = {
            "raw": raw,
            "threadId": original_email.get("thread_id"),
        }

        service.users().messages().send(userId="me", body=message_body).execute()
        log.info(f"Auto-reply sent to {original_email['from']} (intent: FAQ)")
        return True

    except HttpError as e:
        log.error(f"Failed to send auto-reply: {e}")
        return False


def mark_as_read(service, email_id: str):
    """Mark email as read so we don't process it again."""
    try:
        service.users().messages().modify(
            userId="me",
            id=email_id,
            body={"removeLabelIds": ["UNREAD"]},
        ).execute()
    except HttpError as e:
        log.warning(f"Could not mark email {email_id} as read: {e}")


def add_label(service, email_id: str, label_name: str):
    """Add a Gmail label to the email for tracking."""
    try:
        # Get or create label
        labels_result = service.users().labels().list(userId="me").execute()
        labels = labels_result.get("labels", [])
        label_id = next((l["id"] for l in labels if l["name"] == label_name), None)

        if not label_id:
            new_label = service.users().labels().create(
                userId="me",
                body={"name": label_name, "labelListVisibility": "labelShow",
                      "messageListVisibility": "show"}
            ).execute()
            label_id = new_label["id"]

        service.users().messages().modify(
            userId="me",
            id=email_id,
            body={"addLabelIds": [label_id]},
        ).execute()
    except HttpError as e:
        log.warning(f"Could not add label to email {email_id}: {e}")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def run():
    log.info("Baha Baha Email Responder starting...")

    if not ANTHROPIC_KEY:
        log.error("ANTHROPIC_API_KEY not set — exiting")
        return

    if not GMAIL_USER:
        log.error("GMAIL_USER not set — exiting")
        return

    # Connect to Gmail
    service = get_gmail_service()
    if not service:
        log.error("Could not connect to Gmail — check credentials")
        return

    # Fetch unread guest emails
    emails = get_unread_guest_emails(service)
    log.info(f"Found {len(emails)} unread guest email(s) to process")

    if not emails:
        log.info("No new guest emails — done")
        return

    for email in emails:
        log.info(f"Processing email from {email['from']} — subject: {email['subject'][:60]}")

        # Analyse and generate reply
        result = analyse_and_respond(email)

        if not result:
            log.warning(f"Could not generate reply for email {email['id']} — skipping")
            continue

        language = result.get("language", "Unknown")
        intent = result.get("intent", "other")
        reply_body = result.get("reply_body", "")

        log.info(f"  Language: {language} | Intent: {intent}")

        if not reply_body:
            log.warning(f"  Empty reply generated — skipping email {email['id']}")
            continue

        # Decide: auto-send or draft
        intent_cfg = INTENT_CONFIG.get(intent, INTENT_CONFIG["other"])
        should_auto_send = AUTO_SEND_FAQS and intent_cfg.get("auto_send", False)

        if should_auto_send:
            success = send_reply(service, email, result)
            if success:
                add_label(service, email["id"], "AI-Auto-Sent")
        else:
            draft_id = create_draft(service, email, result)
            if draft_id:
                add_label(service, email["id"], "AI-Draft-Created")

        # Mark as read so we don't process it again
        mark_as_read(service, email["id"])

        log.info(f"  Done — {'auto-sent' if should_auto_send else 'draft saved'}")

    log.info("Email responder run complete ✓")


if __name__ == "__main__":
    run()
