"""
WILBA AI Receptionist Audit — Email Responder v2

What this does:
1. Receives Wix form webhook (POST /audit-webhook)
2. Parses form data including optional website URL
3. Fetches and analyses prospect's website if provided
4. Sends to Claude Opus for deep analysis:
   - Revenue loss calculation with breakdown
   - Top 3 specific gaps
   - 5-step implementation roadmap
   - Personalised email body
5. Generates branded WILBA PDF audit report (WeasyPrint)
6. Sends personalised email with PDF attached
7. Logs lead to CSV

Required env vars:
  ANTHROPIC_API_KEY  — Claude API key
  SENDGRID_API_KEY   — SendGrid API key
  FROM_EMAIL         — e.g. hello@wilba.ai
  CALENDLY_URL       — e.g. https://calendly.com/hello-wilba
  TEST_EMAIL         — email to receive test audits (defaults to FROM_EMAIL)
"""

import os
import json
import csv
import re
import base64
import urllib.request
from datetime import datetime
from html.parser import HTMLParser
from flask import Flask, request, jsonify
import anthropic
import sendgrid
from sendgrid.helpers.mail import (
    Mail, Email, To, Content,
    Attachment, FileContent, FileName, FileType, Disposition
)
from dotenv import load_dotenv

try:
    import weasyprint
    WEASYPRINT_AVAILABLE = True
except ImportError:
    WEASYPRINT_AVAILABLE = False
    print("WeasyPrint not available — PDF generation disabled")

load_dotenv()

app = Flask(__name__)
client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

CALENDLY_URL = os.environ.get("CALENDLY_URL", "https://calendly.com/hello-wilba")
FROM_EMAIL = os.environ.get("FROM_EMAIL", "hello@wilba.ai")

# ---------------------------------------------------------------------------
# WILBA Brand
# ---------------------------------------------------------------------------

BRAND_DARK      = "#394F6A"
BRAND_DARKER    = "#2D3E52"
BRAND_BLUE      = "#87ABDD"
BRAND_LIGHT     = "#C7D7EA"
BRAND_STEEL     = "#5E7998"
BRAND_BG        = "#F0F4F8"
BRAND_TEXT      = "#1A1A2E"

# ---------------------------------------------------------------------------
# System Prompt — Claude Opus
# ---------------------------------------------------------------------------

SYSTEM_PROMPT = """You are an AI analyst for WILBA.ai — an AI automation agency run by Jess Morrell on the Surf Coast, Australia.

Your job: Analyse a completed AI Receptionist Audit from a service business owner. Produce:
1. A revenue loss estimate with calculation breakdown
2. Top 3 specific gaps (based on their actual answers)
3. A 5-step personalised implementation roadmap
4. A personalised audit email

REVENUE LOSS FORMULA:
  weekly_enquiries x missed_rate x conversion_rate x avg_booking_value x 4.33 = monthly_loss
  - weekly_enquiries: from Q2 and Q9 (use the higher signal)
  - missed_rate: derive from Q6 and Q7 (missing 5-15 calls + voicemail = 60-80% loss rate)
  - conversion_rate: from Q10 (use midpoint)
  - avg_booking_value: from Q11 (use midpoint)
  - Provide LOW (conservative) and HIGH (realistic worst case) rounded to nearest $50
  - Include calculation_breakdown: exactly 4 bullet points showing the key numbers used

ROADMAP: Generate exactly 5 steps from diagnosis to full AI implementation:
  - Step 1: Immediate win (Days 1-7)
  - Step 2: Core AI setup (Week 2)
  - Step 3: Automation layer (Weeks 3-4)
  - Step 4: Optimise and learn (Month 2)
  - Step 5: Scale (Month 3+)
  Each step: title, description (2 sentences max), timeline, impact (one punchy outcome line)

EMAIL RULES:
1. Open with their name + bold revenue loss number — make it land
2. Show the working (3-4 bullet points) — builds credibility
3. Name their TOP 3 gaps from their actual answers — no generic filler
4. Paint the picture of what changes with AI receptionist (outcomes, not features)
5. ONE CTA — bold linked text to Calendly, punchy and specific to their situation
6. P.S. line with urgency or a curiosity hook

Tone: Confident trusted advisor. Australian English (enquiries not inquiries). Short paragraphs. Scannable.
Think: smart friend who reviewed their business and genuinely wants to help — not a salesperson.

CRITICAL — HTML EMAIL FORMATTING:
- Use ONLY plain HTML with inline styles. NO Unicode special characters whatsoever.
- For bullets use &bull; or HTML list tags. For dashes use &mdash; or plain hyphens.
- For bold use <strong> tags. For emphasis use <em> tags.
- The email_html field must start with: <div style="font-family: Arial, sans-serif; max-width: 600px; color: #1a1a2e; line-height: 1.6;">
- Do NOT use: arrows (->), Unicode bullets (•), smart quotes, em dashes (—) as raw characters.
- Use HTML entities only: &bull; &mdash; &ldquo; &rdquo; &rarr;

OUTPUT FORMAT — return ONLY valid JSON, no markdown fences, no explanation:
{
  "revenue_loss_low": 1200,
  "revenue_loss_high": 3800,
  "calculation_breakdown": [
    {"label": "Weekly enquiries", "value": "50+"},
    {"label": "Estimated missed rate", "value": "65%"},
    {"label": "Your conversion rate", "value": "37%"},
    {"label": "Average booking value", "value": "$200"}
  ],
  "top_gaps": [
    "Gap title — 1-2 sentence description specific to their answers",
    "Gap title — description",
    "Gap title — description"
  ],
  "roadmap": [
    {"step": 1, "title": "Deploy AI Receptionist", "description": "Two sentence description.", "timeline": "Days 1-7", "impact": "Zero missed calls from day one"},
    {"step": 2, "title": "...", "description": "...", "timeline": "Week 2", "impact": "..."},
    {"step": 3, "title": "...", "description": "...", "timeline": "Weeks 3-4", "impact": "..."},
    {"step": 4, "title": "...", "description": "...", "timeline": "Month 2", "impact": "..."},
    {"step": 5, "title": "...", "description": "...", "timeline": "Month 3+", "impact": "..."}
  ],
  "email_subject": "Subject line — personal, curiosity-driven, includes their first name",
  "email_html": "Full HTML email body starting with <div style=...>"
}"""


# ---------------------------------------------------------------------------
# Website Fetcher
# ---------------------------------------------------------------------------

class _TextExtractor(HTMLParser):
    def __init__(self):
        super().__init__()
        self._parts = []
        self._skip = False
        self._skip_tags = {'script', 'style', 'nav', 'footer', 'head', 'noscript'}

    def handle_starttag(self, tag, attrs):
        if tag in self._skip_tags:
            self._skip = True

    def handle_endtag(self, tag):
        if tag in self._skip_tags:
            self._skip = False

    def handle_data(self, data):
        if not self._skip:
            t = data.strip()
            if t:
                self._parts.append(t)

    def get_text(self):
        return ' '.join(self._parts)


def fetch_website_text(url: str, max_chars: int = 3000) -> str:
    """Fetch a website and return its readable text content."""
    if not url:
        return ""
    if not url.startswith(('http://', 'https://')):
        url = 'https://' + url
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=8) as resp:
            html = resp.read().decode('utf-8', errors='ignore')
        parser = _TextExtractor()
        parser.feed(html)
        text = re.sub(r'\s+', ' ', parser.get_text()).strip()
        return text[:max_chars]
    except Exception as e:
        print(f"Website fetch error ({url}): {e}")
        return ""


# ---------------------------------------------------------------------------
# Form Parser
# ---------------------------------------------------------------------------

def parse_wix_form_data(raw_data: dict) -> dict:
    """Parse incoming Wix form webhook payload into standard keys."""

    fields = raw_data.get("formData", raw_data.get("data", raw_data))

    if isinstance(fields, list):
        field_map = {}
        for field in fields:
            label = field.get("label", field.get("fieldName", "")).lower()
            value = field.get("value", field.get("fieldValue", ""))
            field_map[label] = value
        fields = field_map

    mapping = {
        "first name":                                       "first_name",
        "first_name":                                       "first_name",
        "name":                                             "first_name",
        "email":                                            "email",
        "email*":                                           "email",
        "what is the link to your website":                 "website_url",
        "website":                                          "website_url",
        "website url":                                      "website_url",
        "what type of service business do you run":         "q1_business_type",
        "how many calls does your business receive per week": "q2_weekly_calls",
        "what are your business hours":                     "q3_hours",
        "do you have a dedicated receptionist":             "q4_receptionist",
        "how many staff members handle incoming calls":     "q5_staff_count",
        "how many calls per week go unanswered":            "q6_missed_calls",
        "what typically happens when a call is missed":     "q7_missed_handling",
        "how quickly do you respond to website enquiries":  "q8_response_time",
        "how many new enquiries or leads":                  "q9_total_enquiries",
        "what percentage of enquiries convert":             "q10_conversion",
        "what is the average value of a new client":        "q11_avg_value",
        "do you have any system for handling after-hours":  "q12_after_hours",
        "how do most clients contact you":                  "q13_contact_channels",
        "do you currently use any automated follow-up":     "q14_automation",
        "have you ever knowingly lost a client":            "q15_lost_clients",
        "what is your biggest frustration":                 "q16_frustration",
        "if an ai could answer every call":                 "q17_value_perception",
    }

    audit_data = {}
    if isinstance(fields, dict):
        for wix_key, value in fields.items():
            wix_key_lower = wix_key.lower().strip("?*. ")
            if wix_key_lower in mapping:
                audit_data[mapping[wix_key_lower]] = value
                continue
            for map_key, our_key in mapping.items():
                if map_key in wix_key_lower or wix_key_lower in map_key:
                    audit_data[our_key] = value
                    break

    return audit_data


# ---------------------------------------------------------------------------
# Claude Analysis
# ---------------------------------------------------------------------------

def calculate_and_write_email(audit_data: dict, website_text: str = "") -> dict:
    """Send audit data to Claude Opus. Returns analysis + email content."""

    website_section = ""
    if website_text:
        url = audit_data.get('website_url', 'their website')
        website_section = f"\nWEBSITE CONTENT (scraped from {url}):\n{website_text}\nUse this to make the analysis even more specific to their actual business.\n"

    user_prompt = f"""Analyse this completed audit and produce the full response.

RESPONDENT: {audit_data.get('first_name', 'there')}
BUSINESS TYPE: {audit_data.get('q1_business_type', 'Service business')}
CALENDLY URL FOR CTA: {CALENDLY_URL}
{website_section}
AUDIT ANSWERS:
Q1  Business type: {audit_data.get('q1_business_type', 'Not specified')}
Q2  Weekly calls received: {audit_data.get('q2_weekly_calls', 'Not specified')}
Q3  Business hours: {audit_data.get('q3_hours', 'Not specified')}
Q4  Receptionist setup: {audit_data.get('q4_receptionist', 'Not specified')}
Q5  Staff handling calls: {audit_data.get('q5_staff_count', 'Not specified')}
Q6  Missed calls per week: {audit_data.get('q6_missed_calls', 'Not specified')}
Q7  What happens when missed: {audit_data.get('q7_missed_handling', 'Not specified')}
Q8  Response time to web enquiries: {audit_data.get('q8_response_time', 'Not specified')}
Q9  Total weekly enquiries: {audit_data.get('q9_total_enquiries', 'Not specified')}
Q10 Conversion rate: {audit_data.get('q10_conversion', 'Not specified')}
Q11 Average booking value: {audit_data.get('q11_avg_value', 'Not specified')}
Q12 After-hours handling: {audit_data.get('q12_after_hours', 'Not specified')}
Q13 Contact channels: {audit_data.get('q13_contact_channels', 'Not specified')}
Q14 Automated follow-up: {audit_data.get('q14_automation', 'Not specified')}
Q15 Lost clients from slow response: {audit_data.get('q15_lost_clients', 'Not specified')}
Q16 Biggest frustration: {audit_data.get('q16_frustration', 'Not specified')}
Q17 Value of AI receptionist: {audit_data.get('q17_value_perception', 'Not specified')}

Return ONLY valid JSON. Make this feel like Jess personally reviewed their business.
The email should mention: "I've attached your full audit report and roadmap as a PDF."
"""

    message = client.messages.create(
        model="claude-opus-4-6",
        max_tokens=4000,
        system=SYSTEM_PROMPT,
        messages=[{"role": "user", "content": user_prompt}]
    )

    response_text = message.content[0].text.strip()
    if response_text.startswith("```"):
        response_text = re.sub(r'^```(?:json)?\s*', '', response_text)
        response_text = re.sub(r'\s*```$', '', response_text)

    return json.loads(response_text)


# ---------------------------------------------------------------------------
# PDF Generator
# ---------------------------------------------------------------------------

def _get_logo_html() -> str:
    """Return either an embedded logo image or styled text fallback."""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)
    logo_path = os.path.join(project_root, 'reference', 'brand', 'logo.png')
    if os.path.exists(logo_path):
        with open(logo_path, 'rb') as f:
            b64 = base64.b64encode(f.read()).decode()
        return f'<img src="data:image/png;base64,{b64}" style="height:38px;" alt="wilba.ai">'
    return '<span style="font-size:26px;font-weight:bold;color:#ffffff;letter-spacing:-0.5px;">wilba<span style="color:#87ABDD;">.ai</span></span>'


def generate_pdf(audit_data: dict, email_result: dict) -> bytes | None:
    """Generate a branded WILBA audit report PDF using WeasyPrint."""

    if not WEASYPRINT_AVAILABLE:
        return None

    name     = audit_data.get('first_name', 'Business Owner')
    business = audit_data.get('q1_business_type', 'Your Business')
    low      = email_result.get('revenue_loss_low', 0)
    high     = email_result.get('revenue_loss_high', 0)
    date     = datetime.now().strftime('%B %d, %Y')

    # Calculation breakdown (table layout — WeasyPrint-safe)
    breakdown_html = ""
    for item in email_result.get('calculation_breakdown', []):
        breakdown_html += f"""
        <table width="100%" style="border-bottom:1px solid #E0E9F4;padding:9px 0;" cellpadding="0" cellspacing="0">
          <tr>
            <td style="font-size:13px;color:#394F6A;">{item.get('label','')}</td>
            <td style="font-size:13px;font-weight:bold;color:#2D3E52;text-align:right;">{item.get('value','')}</td>
          </tr>
        </table>"""

    # Gaps (table layout)
    gaps_html = ""
    for i, gap in enumerate(email_result.get('top_gaps', []), 1):
        parts = re.split(r'\s*[—\-]{1,2}\s*', gap, maxsplit=1)
        title = parts[0]
        desc  = parts[1] if len(parts) > 1 else ""
        gaps_html += f"""
        <table width="100%" style="margin-bottom:12px;background:white;border-left:4px solid #87ABDD;padding:14px;" cellpadding="0" cellspacing="0">
          <tr>
            <td width="36" style="font-size:26px;font-weight:bold;color:#87ABDD;vertical-align:top;padding-right:10px;">{i}</td>
            <td style="vertical-align:top;">
              <div style="font-size:13px;font-weight:bold;color:#394F6A;">{title}</div>
              {f'<div style="font-size:12px;color:#5E7998;margin-top:4px;line-height:1.5;">{desc}</div>' if desc else ''}
            </td>
          </tr>
        </table>"""

    # Roadmap (table layout)
    roadmap_html = ""
    for step in email_result.get('roadmap', []):
        roadmap_html += f"""
        <table width="100%" style="margin-bottom:18px;" cellpadding="0" cellspacing="0">
          <tr>
            <td width="40" style="vertical-align:top;padding-right:14px;padding-top:2px;">
              <div style="background:#394F6A;color:white;width:30px;height:30px;text-align:center;font-weight:bold;font-size:13px;line-height:30px;">{step.get('step','')}</div>
            </td>
            <td style="vertical-align:top;">
              <div style="font-size:14px;font-weight:bold;color:#394F6A;">{step.get('title','')}</div>
              <div style="font-size:10px;color:#5E7998;background:#E0E9F4;padding:2px 8px;margin:4px 0;display:inline;">{step.get('timeline','')}</div>
              <div style="font-size:12px;color:#555;line-height:1.5;margin-top:4px;">{step.get('description','')}</div>
              <div style="font-size:12px;color:#394F6A;font-weight:bold;margin-top:5px;">&#10003; {step.get('impact','')}</div>
            </td>
          </tr>
        </table>"""

    logo_html = _get_logo_html()

    html = f"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
  @page {{ size: A4; margin: 0; }}
  * {{ box-sizing: border-box; margin: 0; padding: 0; }}
  body {{ font-family: Arial, Helvetica, sans-serif; color: #1a1a2e; background: white; }}
</style>
</head>
<body>

<!-- HEADER -->
<table width="100%" style="background:#394F6A;color:white;padding:35px 45px;" cellpadding="0" cellspacing="0">
  <tr>
    <td style="vertical-align:middle;">{logo_html}</td>
    <td style="vertical-align:middle;text-align:right;">
      <div style="font-size:12px;letter-spacing:2px;text-transform:uppercase;color:#C7D7EA;">AI Receptionist Audit</div>
      <div style="font-size:11px;color:#87ABDD;margin-top:4px;">Prepared exclusively for {name}</div>
    </td>
  </tr>
</table>

<!-- META BAR -->
<table width="100%" style="background:#2D3E52;padding:11px 45px;" cellpadding="0" cellspacing="0">
  <tr>
    <td style="font-size:11px;color:#C7D7EA;"><strong style="color:#87ABDD;">Business: </strong>{business}</td>
    <td style="font-size:11px;color:#C7D7EA;text-align:center;"><strong style="color:#87ABDD;">Date: </strong>{date}</td>
    <td style="font-size:11px;color:#C7D7EA;text-align:right;"><strong style="color:#87ABDD;">Analyst: </strong>Jess Morrell, wilba.ai</td>
  </tr>
</table>

<!-- HERO -->
<div style="background:#394F6A;padding:42px 45px;text-align:center;">
  <div style="font-size:11px;letter-spacing:3px;text-transform:uppercase;color:#C7D7EA;margin-bottom:10px;">Estimated Monthly Revenue Loss</div>
  <div style="font-size:56px;font-weight:bold;color:#87ABDD;line-height:1;">${low:,} &ndash; ${high:,}</div>
  <div style="font-size:18px;color:#C7D7EA;margin-top:8px;">per month</div>
  <div style="font-size:12px;color:#87ABDD;margin-top:12px;">Based on your audit responses &mdash; this is what is currently walking out the door.</div>
</div>

<!-- HOW WE GOT THIS NUMBER -->
<div style="padding:28px 45px;">
  <div style="font-size:13px;font-weight:bold;color:#394F6A;text-transform:uppercase;letter-spacing:1px;border-bottom:2px solid #87ABDD;padding-bottom:8px;margin-bottom:16px;">How We Got This Number</div>
  {breakdown_html}
</div>

<!-- TOP 3 GAPS -->
<div style="padding:28px 45px;background:#F0F4F8;">
  <div style="font-size:13px;font-weight:bold;color:#394F6A;text-transform:uppercase;letter-spacing:1px;border-bottom:2px solid #87ABDD;padding-bottom:8px;margin-bottom:16px;">Your 3 Biggest Gaps</div>
  {gaps_html}
</div>

<!-- ROADMAP -->
<div style="padding:28px 45px;">
  <div style="font-size:13px;font-weight:bold;color:#394F6A;text-transform:uppercase;letter-spacing:1px;border-bottom:2px solid #87ABDD;padding-bottom:8px;margin-bottom:20px;">Your AI Receptionist Roadmap</div>
  {roadmap_html}
</div>

<!-- FOOTER -->
<div style="background:#394F6A;color:white;padding:30px 45px;text-align:center;">
  <div style="font-size:16px;color:white;margin-bottom:8px;">Ready to plug the leak? Let&rsquo;s map your 30-day fix.</div>
  <div style="font-size:13px;color:#87ABDD;margin-bottom:18px;">{CALENDLY_URL}</div>
  <div style="border-top:1px solid #5E7998;padding-top:16px;font-size:10px;color:#C7D7EA;">
    wilba.ai &bull; hello@wilba.ai &bull; Surf Coast, Victoria, Australia
  </div>
</div>

</body>
</html>"""

    # Run WeasyPrint in a subprocess to isolate C library crashes (segfaults)
    # from the gunicorn worker process.
    import subprocess, sys, tempfile, json as _json
    script = (
        "import sys, weasyprint, json\n"
        "html = sys.stdin.read()\n"
        "pdf = weasyprint.HTML(string=html).write_pdf()\n"
        "sys.stdout.buffer.write(pdf)\n"
    )
    try:
        result = subprocess.run(
            [sys.executable, "-c", script],
            input=html.encode("utf-8"),
            capture_output=True,
            timeout=60
        )
        if result.returncode == 0 and result.stdout:
            return result.stdout
        else:
            print(f"WeasyPrint subprocess failed (rc={result.returncode}): {result.stderr.decode()[:500]}")
            return None
    except subprocess.TimeoutExpired:
        print("WeasyPrint subprocess timed out")
        return None


# ---------------------------------------------------------------------------
# Email Sender
# ---------------------------------------------------------------------------

def send_email(to_email: str, to_name: str, subject: str, html_body: str,
               pdf_bytes: bytes = None) -> bool:
    """Send the personalised audit email via SendGrid with optional PDF attachment."""

    sg_api_key = os.environ.get("SENDGRID_API_KEY")
    if not sg_api_key:
        print("WARNING: No SENDGRID_API_KEY set. Email not sent.")
        return False

    sg = sendgrid.SendGridAPIClient(api_key=sg_api_key)

    message = Mail(
        from_email=Email(FROM_EMAIL, "Jess from WILBA"),
        to_emails=To(to_email, to_name),
        subject=subject,
        html_content=Content("text/html; charset=utf-8", html_body)
    )

    if pdf_bytes:
        attachment = Attachment()
        attachment.file_content = FileContent(base64.b64encode(pdf_bytes).decode())
        attachment.file_name = FileName(f"WILBA-AI-Audit-{to_name.replace(' ', '-')}.pdf")
        attachment.file_type = FileType('application/pdf')
        attachment.disposition = Disposition('attachment')
        message.add_attachment(attachment)
        print(f"PDF attached — {len(pdf_bytes):,} bytes")

    try:
        response = sg.send(message)
        print(f"Email sent to {to_email} — Status: {response.status_code}")
        return response.status_code in [200, 201, 202]
    except Exception as e:
        print(f"Email send error: {e}")
        return False


# ---------------------------------------------------------------------------
# Lead Logger
# ---------------------------------------------------------------------------

def log_lead(audit_data: dict, email_result: dict, email_sent: bool):
    """Append lead to outputs/audit/leads.csv"""
    project_root = os.environ.get(
        "PROJECT_ROOT",
        os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    )
    log_dir = os.path.join(project_root, "outputs", "audit")
    os.makedirs(log_dir, exist_ok=True)
    log_file = os.path.join(log_dir, "leads.csv")

    file_exists = os.path.isfile(log_file)
    with open(log_file, "a", newline="") as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow([
                "timestamp", "name", "email", "business_type", "website",
                "weekly_calls", "missed_calls", "avg_value",
                "revenue_loss_low", "revenue_loss_high", "email_sent"
            ])
        writer.writerow([
            datetime.now().isoformat(),
            audit_data.get("first_name", ""),
            audit_data.get("email", ""),
            audit_data.get("q1_business_type", ""),
            audit_data.get("website_url", ""),
            audit_data.get("q2_weekly_calls", ""),
            audit_data.get("q6_missed_calls", ""),
            audit_data.get("q11_avg_value", ""),
            email_result.get("revenue_loss_low", ""),
            email_result.get("revenue_loss_high", ""),
            "yes" if email_sent else "no"
        ])
    print(f"Lead logged: {audit_data.get('first_name')} ({audit_data.get('email')})")


# ---------------------------------------------------------------------------
# Webhook Endpoint
# ---------------------------------------------------------------------------

@app.route("/audit-webhook", methods=["POST"])
def handle_audit_submission():
    """Main webhook — receives Wix form, generates analysis, sends email + PDF."""
    try:
        raw_data = request.json
        print(f"\n{'='*60}")
        print(f"Audit submission at {datetime.now().isoformat()}")

        audit_data = parse_wix_form_data(raw_data)
        print(f"Parsed: {audit_data.get('first_name','?')} — {audit_data.get('q1_business_type','?')}")

        if not audit_data.get("email"):
            return jsonify({"error": "No email address found in submission"}), 400

        # Fetch website if provided
        website_text = ""
        if audit_data.get("website_url"):
            print(f"Fetching website: {audit_data['website_url']}")
            website_text = fetch_website_text(audit_data["website_url"])
            print(f"Website text: {len(website_text)} chars")

        # Claude Opus analysis
        print("Sending to Claude Opus for analysis...")
        email_result = calculate_and_write_email(audit_data, website_text)
        print(f"Revenue estimate: ${email_result.get('revenue_loss_low','?'):,} - ${email_result.get('revenue_loss_high','?'):,}/month")

        # Generate PDF
        pdf_bytes = None
        if WEASYPRINT_AVAILABLE:
            try:
                print("Generating PDF...")
                pdf_bytes = generate_pdf(audit_data, email_result)
                print(f"PDF generated: {len(pdf_bytes):,} bytes" if pdf_bytes else "PDF generation failed")
            except Exception as pdf_err:
                print(f"PDF generation failed (non-fatal): {pdf_err}")
                pdf_bytes = None

        # Send email with PDF attached
        email_sent = send_email(
            to_email=audit_data["email"],
            to_name=audit_data.get("first_name", "there"),
            subject=email_result["email_subject"],
            html_body=email_result["email_html"],
            pdf_bytes=pdf_bytes
        )

        log_lead(audit_data, email_result, email_sent)
        print(f"{'='*60}\n")

        return jsonify({
            "status": "success",
            "email_sent": email_sent,
            "pdf_generated": pdf_bytes is not None,
            "revenue_loss_estimate": f"${email_result['revenue_loss_low']:,}-${email_result['revenue_loss_high']:,}/month",
            "gaps_identified": len(email_result.get("top_gaps", []))
        }), 200

    except json.JSONDecodeError as e:
        print(f"JSON parse error from Claude: {e}")
        return jsonify({"error": "Failed to parse Claude response"}), 500
    except Exception as e:
        import traceback
        print(f"Error: {e}")
        traceback.print_exc()
        return jsonify({"error": str(e)}), 500


# ---------------------------------------------------------------------------
# Health Check
# ---------------------------------------------------------------------------

@app.route("/health", methods=["GET"])
def health_check():
    return jsonify({
        "status": "healthy",
        "service": "WILBA Audit Email Responder v2",
        "weasyprint_available": WEASYPRINT_AVAILABLE,
        "model": "claude-opus-4-6",
        "timestamp": datetime.now().isoformat()
    }), 200


# ---------------------------------------------------------------------------
# Test Endpoint — fires the FULL pipeline including sending real email
# ---------------------------------------------------------------------------

@app.route("/test-audit", methods=["GET"])
def test_audit():
    """
    Full pipeline test — generates analysis, PDF, and sends real email to TEST_EMAIL.
    Visit /test-audit in your browser to test.
    """
    test_email = os.environ.get("TEST_EMAIL", FROM_EMAIL)

    sample_data = {
        "first_name": "Sarah",
        "email": test_email,
        "website_url": "",
        "q1_business_type": "Physiotherapy clinic",
        "q2_weekly_calls": "50-100",
        "q3_hours": "Weekdays 9am-5pm, Saturdays until 1pm",
        "q4_receptionist": "Yes — part time (leaves at 2pm)",
        "q5_staff_count": "2",
        "q6_missed_calls": "5-15",
        "q7_missed_handling": "Voicemail — most people don't leave a message",
        "q8_response_time": "Same day if we remember",
        "q9_total_enquiries": "20-50",
        "q10_conversion": "25-50%",
        "q11_avg_value": "$100-$300",
        "q12_after_hours": "Voicemail only",
        "q13_contact_channels": "Phone, website form, Instagram DMs",
        "q14_automation": "We do it manually when we remember",
        "q15_lost_clients": "Yes — at least once that I know of",
        "q16_frustration": "We miss calls after 2pm when the receptionist leaves. We know it costs us but don't have the bandwidth.",
        "q17_value_perception": "It would be a complete game changer"
    }

    skip_pdf = request.args.get("skip_pdf", "0") == "1"
    mock_claude = request.args.get("mock_claude", "0") == "1"

    try:
        print(f"\n--- TEST AUDIT RUNNING (skip_pdf={skip_pdf}, mock_claude={mock_claude}) ---")
        website_text = fetch_website_text(sample_data.get("website_url", ""))

        if mock_claude:
            print("Using mock Claude response (mock_claude=1)")
            email_result = {
                "revenue_loss_low": 1300,
                "revenue_loss_high": 4350,
                "calculation_breakdown": [
                    {"label": "Missed calls per week × avg booking value", "value": "$1,300–$2,600"},
                    {"label": "Slow follow-up lead decay", "value": "$0–$1,750"},
                ],
                "top_gaps": [
                    "After-hours coverage — calls go to voicemail and most people don't leave messages",
                    "Slow web enquiry response — leads go cold within 5 minutes",
                    "No automated follow-up — manual process means leads fall through the cracks",
                ],
                "roadmap": [
                    {"step": 1, "title": "AI Phone Receptionist", "timeline": "Week 1", "impact": "Capture every call 24/7", "description": "Deploy an AI that answers every call, qualifies leads, and books appointments."},
                    {"step": 2, "title": "Instant Web Enquiry Response", "timeline": "Week 2", "impact": "5-minute response rate", "description": "Automated reply within 5 minutes of any form submission."},
                    {"step": 3, "title": "Follow-up Sequences", "timeline": "Week 3", "impact": "30% more conversions", "description": "Automated SMS/email follow-up for unclosed leads."},
                    {"step": 4, "title": "Appointment Reminders", "timeline": "Week 4", "impact": "Reduce no-shows by 40%", "description": "Automated reminders 24h and 1h before appointments."},
                    {"step": 5, "title": "Review Collection", "timeline": "Week 5-6", "impact": "5-star Google reviews", "description": "Automated post-visit review requests."},
                ],
                "email_subject": "Sarah, your physio clinic is leaking $1,300–$4,350/month [Mock Test]",
                "email_html": "<p>Hi Sarah,</p><p>This is a <strong>mock test email</strong> — Claude API was bypassed.</p><p>If you received this, the email pipeline works!</p><p>Jess</p>",
            }
        else:
            email_result = calculate_and_write_email(sample_data, website_text)
        pdf_bytes = None
        if WEASYPRINT_AVAILABLE and not skip_pdf:
            try:
                pdf_bytes = generate_pdf(sample_data, email_result)
            except Exception as pdf_err:
                print(f"PDF generation failed (non-fatal): {pdf_err}")
                pdf_bytes = None

        email_sent = send_email(
            to_email=test_email,
            to_name=sample_data["first_name"],
            subject=email_result["email_subject"],
            html_body=email_result["email_html"],
            pdf_bytes=pdf_bytes
        )

        gaps_html = ''.join(f'<li>{g}</li>' for g in email_result.get('top_gaps', []))
        roadmap_html = ''.join(
            f'<li><strong>Step {r["step"]}: {r["title"]}</strong> ({r["timeline"]}) &mdash; {r["impact"]}</li>'
            for r in email_result.get('roadmap', [])
        )
        pdf_status = f"YES ({len(pdf_bytes):,} bytes)" if pdf_bytes else "NO (WeasyPrint not installed)"

        return f"""
        <html><head><meta charset="utf-8"><title>WILBA Audit Test</title></head>
        <body style="font-family:Arial,sans-serif;max-width:800px;margin:40px auto;padding:20px;">
            <h1 style="color:#394F6A;">Audit Test Result</h1>
            <p><strong>Email sent to:</strong> {test_email} &mdash; <strong style="color:{'green' if email_sent else 'red'}">{'SENT' if email_sent else 'FAILED'}</strong></p>
            <p><strong>PDF generated:</strong> {pdf_status}</p>
            <p><strong>Revenue Loss:</strong> ${email_result['revenue_loss_low']:,} &ndash; ${email_result['revenue_loss_high']:,}/month</p>
            <p><strong>Subject:</strong> {email_result['email_subject']}</p>
            <h2 style="color:#394F6A;">Top Gaps:</h2><ol>{gaps_html}</ol>
            <h2 style="color:#394F6A;">Roadmap:</h2><ol>{roadmap_html}</ol>
            <hr>
            <h2 style="color:#394F6A;">Email Preview:</h2>
            <div style="border:2px solid #394F6A;padding:30px;border-radius:8px;background:#fafafa;">
                {email_result['email_html']}
            </div>
        </body></html>
        """, 200

    except BaseException as e:
        import traceback
        return f"<pre>Error ({type(e).__name__}): {e}\n\n{traceback.format_exc()}</pre>", 500


# ---------------------------------------------------------------------------
# Run
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    print(f"\nWILBA Audit Email Responder v2 starting on port {port}")
    print(f"Model: claude-opus-4-6")
    print(f"WeasyPrint: {'available' if WEASYPRINT_AVAILABLE else 'NOT available'}")
    print(f"Webhook: http://localhost:{port}/audit-webhook")
    print(f"Test: http://localhost:{port}/test-audit")
    print(f"Health: http://localhost:{port}/health\n")
    app.run(host="0.0.0.0", port=port, debug=True)
