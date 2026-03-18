"""
WILBA AI Receptionist Audit — Email Responder

What this does:
1. Listens for form submissions from Wix (webhook POST to /audit-webhook)
2. Parses the audit answers from the 18-question form
3. Sends to Claude with a revenue calculation + email writing prompt
4. Sends the personalised audit email to the respondent
5. Logs the lead to outputs/audit/leads.csv

How to run locally: python scripts/audit_email_responder.py
How to deploy: Deploy to Render/Railway, set env vars, point Wix webhook at the URL

Required env vars:
  ANTHROPIC_API_KEY  — Claude API key
  SENDGRID_API_KEY   — SendGrid API key for sending emails
  FROM_EMAIL         — e.g. hello@wilba.ai
  CALENDLY_URL       — e.g. https://calendly.com/hello-wilba
"""

import os
import json
import csv
import re
from datetime import datetime
from flask import Flask, request, jsonify
import anthropic
import sendgrid
from sendgrid.helpers.mail import Mail, Email, To, Content
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

CALENDLY_URL = os.environ.get("CALENDLY_URL", "https://calendly.com/hello-wilba")
FROM_EMAIL = os.environ.get("FROM_EMAIL", "hello@wilba.ai")

# ---------------------------------------------------------------------------
# Claude System Prompt — this is the brain of the audit
# ---------------------------------------------------------------------------

SYSTEM_PROMPT = """You are an AI analyst for WILBA.ai, an AI automation agency run by Jess Morrell on the Surf Coast, Australia.

Your job: analyse a completed AI Receptionist Audit from a service business owner and produce a personalised audit email that makes the opportunity crystal clear.

The email must feel like Jess personally reviewed their answers. It should be warm, confident, direct — like a smart friend who happens to know exactly how much money they're leaving on the table.

REVENUE LOSS FORMULA:
  weekly_enquiries x missed_rate x conversion_rate x avg_booking_value x 4.33 = monthly_loss

  - weekly_enquiries: from Q2 and Q9 (use the higher signal)
  - missed_rate: derive from Q6 + Q7 (if they miss 5-15 calls AND rarely call back, that's 60-80% loss rate)
  - conversion_rate: from Q10 (use midpoint of their range)
  - avg_booking_value: from Q11 (use midpoint of their range)

  Provide a LOW estimate (conservative — best case) and HIGH estimate (realistic worst case).
  Round to nearest $50. Never say "exactly" — say "somewhere between".
  Make the number FEEL real by connecting it to their specific business type.

THE EMAIL MUST:
1. Open with their name and a bold revenue loss number — this is what gets attention
2. Show the working (how you got the number) in 3-4 bullet points — builds credibility
3. Identify their TOP 3 specific gaps based on their actual answers (not generic)
4. Paint a picture of what changes with an AI receptionist (outcomes, not features)
5. End with ONE clear CTA — a button or bold linked text to the Calendly URL. The CTA copy must be punchy and specific to their situation. Examples of good CTA copy (pick the best fit, don't copy word-for-word):
   - "Let's map your 30-day fix →"
   - "Claim your free implementation call →"
   - "Show me the money (I'm in) →"
   - "Let's turn that $X,XXX leak into a system →"
   - "Book my free 20-min strategy call →"
   The surrounding sentence should frame it as easy, fast, and valuable — not salesy. e.g. "If you want to see exactly how this looks for [their business type], I've kept 20 minutes free this week. No pitch, just a plan."
6. Include a P.S. that creates urgency or curiosity — hint at what's possible or what others like them have done

TONE:
- Confident but not aggressive. Think trusted advisor, not used car salesman.
- Short paragraphs. Scannable. No walls of text.
- Use their business type to make examples specific ("For a physio clinic like yours...")
- Australian English (enquiries not inquiries, organise not organize)
- Don't over-explain the tech — explain the outcome
- Bold the key numbers and insights

CRITICAL: The email should make the prospect think "holy shit, I need to fix this" — not through fear, but through clarity. Show them the opportunity they're missing.

IMPORTANT FORMATTING RULES FOR THE HTML EMAIL:
- Use ONLY plain ASCII characters. No Unicode arrows, bullets, dashes, or smart quotes.
- For bullet points use <li> tags inside <ul> or <ol> — NOT Unicode bullets or arrow characters.
- For emphasis use <strong> tags — NOT Unicode dashes or special characters.
- The email_html must start with: <div style="font-family: Arial, sans-serif; max-width: 600px;">
- Do NOT include Unicode characters like →, •, —, ", ", ', ' in the HTML. Use HTML entities (&bull;, &rarr;, &mdash;, &ldquo;, &rdquo;) or plain ASCII equivalents (-, >, --) instead.

OUTPUT FORMAT — return valid JSON only, no markdown fences:
{
  "revenue_loss_low": 1200,
  "revenue_loss_high": 3800,
  "top_gaps": [
    "Gap 1 — specific to their answers (1-2 sentences)",
    "Gap 2 — specific to their answers",
    "Gap 3 — specific to their answers"
  ],
  "email_subject": "Subject line — personal, curiosity-driven, includes their name",
  "email_html": "Full HTML email body with inline styling for bold text, bullet points, and clean formatting"
}
"""


# ---------------------------------------------------------------------------
# Core Functions
# ---------------------------------------------------------------------------

def parse_wix_form_data(raw_data: dict) -> dict:
    """
    Parse incoming Wix form webhook data into our standard format.

    Wix Forms sends data in a specific structure. The field names
    depend on how the form was built — we handle both standard
    Wix field names and our custom field titles.
    """
    # Wix webhook payload can come in different formats
    # Try to extract from common structures

    fields = raw_data.get("formData", raw_data.get("data", raw_data))

    # If Wix sends fields as a list of {label, value} pairs
    if isinstance(fields, list):
        field_map = {}
        for field in fields:
            label = field.get("label", field.get("fieldName", "")).lower()
            value = field.get("value", field.get("fieldValue", ""))
            field_map[label] = value
        fields = field_map

    # Map from Wix field titles to our internal keys
    # This mapping handles variations in how Wix sends field names
    mapping = {
        "first name": "first_name",
        "first_name": "first_name",
        "name": "first_name",
        "email": "email",
        "email*": "email",
        "what type of service business do you run": "q1_business_type",
        "how many calls does your business receive per week": "q2_weekly_calls",
        "what are your business hours": "q3_hours",
        "do you have a dedicated receptionist": "q4_receptionist",
        "how many staff members handle incoming calls": "q5_staff_count",
        "how many calls per week go unanswered": "q6_missed_calls",
        "what typically happens when a call is missed": "q7_missed_handling",
        "how quickly do you respond to website enquiries": "q8_response_time",
        "how many new enquiries or leads": "q9_total_enquiries",
        "what percentage of enquiries convert": "q10_conversion",
        "what is the average value of a new client": "q11_avg_value",
        "do you have any system for handling after-hours": "q12_after_hours",
        "how do most clients contact you": "q13_contact_channels",
        "do you currently use any automated follow-up": "q14_automation",
        "have you ever knowingly lost a client": "q15_lost_clients",
        "what is your biggest frustration": "q16_frustration",
        "if an ai could answer every call": "q17_value_perception",
    }

    audit_data = {}

    if isinstance(fields, dict):
        for wix_key, value in fields.items():
            wix_key_lower = wix_key.lower().strip("?*. ")

            # Direct match
            if wix_key_lower in mapping:
                audit_data[mapping[wix_key_lower]] = value
                continue

            # Partial match — check if any mapping key is contained in the field name
            for map_key, our_key in mapping.items():
                if map_key in wix_key_lower or wix_key_lower in map_key:
                    audit_data[our_key] = value
                    break

    return audit_data


def calculate_and_write_email(audit_data: dict) -> dict:
    """Send audit data to Claude, get back revenue estimate + personalised email."""

    user_prompt = f"""Here are the completed audit answers. Analyse them and produce the revenue estimate and email.

RESPONDENT: {audit_data.get('first_name', 'there')}
BUSINESS TYPE: {audit_data.get('q1_business_type', 'Service business')}
CALENDLY URL FOR CTA: {CALENDLY_URL}

AUDIT ANSWERS:
Q1  Business type: {audit_data.get('q1_business_type', 'Not specified')}
Q2  Weekly calls: {audit_data.get('q2_weekly_calls', 'Not specified')}
Q3  Business hours: {audit_data.get('q3_hours', 'Not specified')}
Q4  Receptionist setup: {audit_data.get('q4_receptionist', 'Not specified')}
Q5  Staff handling calls: {audit_data.get('q5_staff_count', 'Not specified')}
Q6  Missed calls/week: {audit_data.get('q6_missed_calls', 'Not specified')}
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

Remember: Return ONLY valid JSON. Make the email feel like Jess personally reviewed this. The opportunity should be massive and clear — show them the money they're leaving on the table and exactly how to fix it."""

    message = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=3000,
        system=SYSTEM_PROMPT,
        messages=[{"role": "user", "content": user_prompt}]
    )

    response_text = message.content[0].text

    # Clean up response — sometimes Claude wraps JSON in markdown fences
    response_text = response_text.strip()
    if response_text.startswith("```"):
        response_text = re.sub(r'^```(?:json)?\s*', '', response_text)
        response_text = re.sub(r'\s*```$', '', response_text)

    return json.loads(response_text)


def send_email(to_email: str, to_name: str, subject: str, html_body: str) -> bool:
    """Send the personalised audit email via SendGrid."""

    sg_api_key = os.environ.get("SENDGRID_API_KEY")
    if not sg_api_key:
        print("WARNING: No SENDGRID_API_KEY set. Email not sent.")
        print(f"Would have sent to: {to_email}")
        print(f"Subject: {subject}")
        return False

    sg = sendgrid.SendGridAPIClient(api_key=sg_api_key)

    message = Mail(
        from_email=Email(FROM_EMAIL, "Jess from WILBA"),
        to_emails=To(to_email, to_name),
        subject=subject,
        html_content=Content("text/html; charset=utf-8", html_body)
    )

    try:
        response = sg.send(message)
        print(f"Email sent to {to_email} — Status: {response.status_code}")
        return response.status_code in [200, 201, 202]
    except Exception as e:
        print(f"Email send error: {e}")
        return False


def log_lead(audit_data: dict, email_result: dict, email_sent: bool):
    """Save lead to CSV for Jess's lead tracking dashboard."""

    # Use project root (works both locally and on Render)
    project_root = os.environ.get("PROJECT_ROOT", os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    log_dir = os.path.join(project_root, "outputs", "audit")
    os.makedirs(log_dir, exist_ok=True)
    log_file = os.path.join(log_dir, "leads.csv")

    file_exists = os.path.isfile(log_file)

    with open(log_file, "a", newline="") as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow([
                "timestamp", "name", "email", "business_type",
                "weekly_calls", "missed_calls", "avg_value",
                "revenue_loss_low", "revenue_loss_high",
                "value_perception", "frustration", "email_sent"
            ])
        writer.writerow([
            datetime.now().isoformat(),
            audit_data.get("first_name", ""),
            audit_data.get("email", ""),
            audit_data.get("q1_business_type", ""),
            audit_data.get("q2_weekly_calls", ""),
            audit_data.get("q6_missed_calls", ""),
            audit_data.get("q11_avg_value", ""),
            email_result.get("revenue_loss_low", ""),
            email_result.get("revenue_loss_high", ""),
            audit_data.get("q17_value_perception", ""),
            audit_data.get("q16_frustration", ""),
            "yes" if email_sent else "no"
        ])

    print(f"Lead logged: {audit_data.get('first_name')} ({audit_data.get('email')})")


# ---------------------------------------------------------------------------
# Webhook Endpoint
# ---------------------------------------------------------------------------

@app.route("/audit-webhook", methods=["POST"])
def handle_audit_submission():
    """Main webhook — receives Wix form data, generates & sends audit email."""

    try:
        raw_data = request.json
        print(f"\n{'='*60}")
        print(f"New audit submission received at {datetime.now().isoformat()}")
        print(f"Raw data keys: {list(raw_data.keys()) if raw_data else 'None'}")

        # Parse the Wix form data
        audit_data = parse_wix_form_data(raw_data)

        print(f"Parsed: {audit_data.get('first_name', 'Unknown')} — {audit_data.get('q1_business_type', 'Unknown business')}")

        if not audit_data.get("email"):
            return jsonify({"error": "No email address provided"}), 400

        # Get Claude to analyse and write the email
        print("Sending to Claude for analysis...")
        email_result = calculate_and_write_email(audit_data)

        print(f"Revenue estimate: ${email_result.get('revenue_loss_low', '?')}–${email_result.get('revenue_loss_high', '?')}/month")
        print(f"Top gaps: {len(email_result.get('top_gaps', []))}")

        # Send the email
        email_sent = send_email(
            to_email=audit_data["email"],
            to_name=audit_data.get("first_name", "there"),
            subject=email_result["email_subject"],
            html_body=email_result["email_html"]
        )

        # Log the lead
        log_lead(audit_data, email_result, email_sent)

        print(f"{'='*60}\n")

        return jsonify({
            "status": "success",
            "email_sent": email_sent,
            "revenue_loss_estimate": f"${email_result['revenue_loss_low']}–${email_result['revenue_loss_high']}/month",
            "gaps_identified": len(email_result.get("top_gaps", []))
        }), 200

    except json.JSONDecodeError as e:
        print(f"JSON parse error from Claude: {e}")
        return jsonify({"error": "Failed to parse Claude response"}), 500
    except Exception as e:
        print(f"Error processing audit: {e}")
        import traceback
        traceback.print_exc()
        return jsonify({"error": str(e)}), 500


@app.route("/health", methods=["GET"])
def health_check():
    """Health check endpoint for monitoring."""
    return jsonify({
        "status": "healthy",
        "service": "WILBA Audit Email Responder",
        "timestamp": datetime.now().isoformat()
    }), 200


@app.route("/test-audit", methods=["GET"])
def test_audit():
    """
    Test endpoint — simulates a form submission with sample data.
    Visit /test-audit in your browser to test the full flow.
    """
    sample_data = {
        "first_name": "Sarah",
        "email": os.environ.get("TEST_EMAIL", "jess@wilba.ai"),
        "q1_business_type": "Physiotherapy",
        "q2_weekly_calls": "50-100",
        "q3_hours": "Weekdays 9am-5pm, Saturdays",
        "q4_receptionist": "Yes — part time",
        "q5_staff_count": "2",
        "q6_missed_calls": "5-15",
        "q7_missed_handling": "We rely on voicemail — most people leave a message",
        "q8_response_time": "Same day",
        "q9_total_enquiries": "20-50",
        "q10_conversion": "25-50%",
        "q11_avg_value": "$100-$300",
        "q12_after_hours": "Voicemail only",
        "q13_contact_channels": "Phone call, Website contact form, Instagram / Facebook DM",
        "q14_automation": "We do it manually when we remember",
        "q15_lost_clients": "Yes — at least once that I know of",
        "q16_frustration": "We know we're missing calls but don't have the bandwidth to answer them all. The receptionist is part time and after 2pm it all goes to voicemail.",
        "q17_value_perception": "It would be a game-changer"
    }

    try:
        print("\n--- TEST AUDIT RUNNING ---")
        email_result = calculate_and_write_email(sample_data)

        # Don't actually send email in test — just show the result
        return f"""
        <html>
        <head><meta charset="utf-8"><title>WILBA Audit Test</title></head>
        <body style="font-family: Arial, sans-serif; max-width: 800px; margin: 40px auto; padding: 20px;">
            <h1>Audit Email Preview</h1>
            <p><strong>Recipient:</strong> {sample_data['first_name']} ({sample_data['email']})</p>
            <p><strong>Revenue Loss:</strong> ${email_result['revenue_loss_low']}–${email_result['revenue_loss_high']}/month</p>
            <p><strong>Subject:</strong> {email_result['email_subject']}</p>
            <h2>Top Gaps:</h2>
            <ol>{''.join(f'<li>{gap}</li>' for gap in email_result.get('top_gaps', []))}</ol>
            <hr>
            <h2>Email Preview:</h2>
            <div style="border: 2px solid #ccc; padding: 30px; border-radius: 8px; background: #fafafa;">
                {email_result['email_html']}
            </div>
        </body>
        </html>
        """, 200

    except Exception as e:
        import traceback
        return f"<pre>Error: {e}\n\n{traceback.format_exc()}</pre>", 500


# ---------------------------------------------------------------------------
# Run
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    print(f"\nWILBA Audit Email Responder starting on port {port}")
    print(f"Webhook URL: http://localhost:{port}/audit-webhook")
    print(f"Test URL: http://localhost:{port}/test-audit")
    print(f"Health: http://localhost:{port}/health")
    print(f"Calendly CTA: {CALENDLY_URL}")
    print(f"From email: {FROM_EMAIL}\n")

    app.run(host="0.0.0.0", port=port, debug=True)
