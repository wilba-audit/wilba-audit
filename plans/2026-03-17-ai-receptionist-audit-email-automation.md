# Plan: AI Receptionist Audit + Automated Email Response System

**Created:** 2026-03-17
**Status:** Implemented (pending deployment — see outputs/audit/MORNING-CHECKLIST.md)
**Request:** Use the AAA audit framework to create service-business audit questions for the AI receptionist direction, then build a Claude-powered script that generates a personalised email response and sends it automatically to the recipient.

---

## Overview

### What This Plan Accomplishes

This plan creates two connected outputs: (1) a set of structured audit questions — built on the AAA framework — that quantify exactly how much money a service business is losing from missed calls and slow lead response, and (2) a Python script powered by Claude that receives those answers, calculates a personalised revenue loss estimate, and automatically emails the prospect a compelling, tailored report with a call-to-action to book with Jess.

### Why This Matters

This is WILBA's fastest path to first revenue. The audit is the lead magnet. The automated email is the closer. Together they create a self-running sales funnel: prospect fills out a form → gets a personalised "you're losing $X/month" email within minutes → books a call. Jess can post the audit link everywhere and let the system work while she sleeps — proving the exact value of AI receptionists by demonstrating it in the process of selling them.

---

## Current State

### Relevant Existing Structure

```
context/
  business-info.md         — WILBA overview, pivot to AI receptionists confirmed
  strategy.md              — First client by April 2026; free audits as primary lead gen
  current-data.md          — Revenue $0, urgency high
reference/
  wilba-launch-plan.md     — Existing launch plan (content-focused, pre-pivot)
.claude/commands/
  task-audit.md            — AAA task audit framework (9 areas + scoring system)
scripts/                   — Empty, ready for new automation scripts
outputs/                   — Ready for audit reports
plans/                     — This plan lives here
```

### Gaps or Problems Being Addressed

- **No audit exists** for the AI receptionist / voice agent direction. Current audit thinking was content-focused.
- **No automated follow-up system** — Jess would have to manually email every audit respondent, which doesn't scale and loses the "wow" moment of instant response.
- **No quantified ROI calculator** — businesses don't know what missed calls cost them. This system shows them in dollars, which is far more powerful than generic positioning.
- **No lead gen asset** — Jess needs something shareable to post in local Facebook groups, LinkedIn, Instagram, and to DM directly to service businesses.

---

## Proposed Changes

### Summary of Changes

- Create `outputs/audit/` directory for audit assets
- Create the 18-question audit (`reference/ai-receptionist-audit-questions.md`) using the AAA framework adapted for service businesses
- Create the email template (`reference/ai-receptionist-email-template.md`)
- Create the Python automation script (`scripts/audit_email_responder.py`)
- Create a `.env.example` update with required API keys
- Create a setup/run guide (`reference/audit-automation-guide.md`)

### New Files to Create

| File Path | Purpose |
|-----------|---------|
| `reference/ai-receptionist-audit-questions.md` | The 18-question audit, structured in AAA phases, ready to copy into Wix |
| `reference/ai-receptionist-email-template.md` | Email template structure Claude uses to generate personalised responses |
| `scripts/audit_email_responder.py` | Python script: receives webhook, calls Claude, sends email |
| `scripts/requirements_audit.txt` | Python dependencies for the audit script |
| `reference/audit-automation-guide.md` | Plain-English setup guide for Jess + her developer |
| `outputs/audit/` | Directory for storing audit responses and generated emails |

### Files to Modify

| File Path | Changes |
|-----------|---------|
| `CLAUDE.md` | Add audit + email automation to workspace structure and capabilities |
| `.env` (if exists) | Add ANTHROPIC_API_KEY, SENDGRID_API_KEY (or SMTP creds), FROM_EMAIL |

---

## Design Decisions

### Key Decisions Made

1. **AAA Framework adapted for service businesses**: The standard AAA task-audit has 9 business areas. This audit focuses on 3 phases — Awareness (current state), Analysis (the gaps/losses), Action (quantify + solution fit) — applied specifically to call handling, lead response, and booking rates. This matches how service businesses think and makes the ROI obvious.

2. **Revenue Loss Calculator built into Claude's prompt**: Rather than a static formula, Claude interprets the answers holistically and produces a nuanced, believable estimate. It also adjusts language based on business type (e.g., dentist vs. roofer vs. physio).

3. **SendGrid for email delivery** (with SMTP fallback): SendGrid has a free tier (100 emails/day), is reliable, and works well for transactional email. SMTP via Gmail is documented as an alternative if Jess prefers.

4. **Wix webhook trigger**: Wix forms can be connected to a webhook URL via Wix Automations (no code needed on the Wix side). The Python script runs on a server and listens for POST requests.

5. **Simple server using Flask**: Flask is lightweight, easy for Jess's developer to understand and deploy, and handles the webhook endpoint cleanly.

6. **Deploy to Render.com**: Free tier works for low-volume use. Easy to deploy from GitHub. No server management required. Alternative: Railway, Fly.io.

7. **Email tone matches WILBA brand**: McConaughey-meets-direct-response. Confident, clear, not corporate. The email opens with the revenue number front and centre, not a generic "thanks for completing our form."

### Alternatives Considered

- **Zapier/Make instead of custom script**: Would work but costs money monthly, gives less control over email personalisation, and doesn't let Claude generate truly custom copy. The custom script is better and proves WILBA's capabilities.
- **Typeform instead of Wix form**: Better UX but requires another tool subscription. Wix is already paid for.
- **Static email template**: Rejected — the power is in personalisation. A generic "you might be losing money" email converts poorly. A "Hi Sarah, based on your answers, Smith Physio is likely losing $4,200/month from missed calls" is what books calls.

### Open Questions (if any)

1. **Does Jess want the email to come from her personal email (jess@wilba.ai) or a generic one (hello@wilba.ai)?** — affects SMTP setup
2. **Does her developer have a preferred hosting platform?** — Render vs Railway vs a VPS they already have
3. **Should the audit response also be stored somewhere** (Google Sheet, Notion, Airtable) for Jess to track leads? — recommend yes, plan for CSV/Sheet option

---

## Step-by-Step Tasks

### Step 1: Create the Audit Questions (AAA Framework — Service Business Version)

Create `reference/ai-receptionist-audit-questions.md` with the full 18-question audit, structured in 3 AAA phases. These questions are designed to be copied directly into a Wix form.

**The 3 Phases:**
- **Phase 1 — AWARENESS** (5 questions): Who they are, what their business looks like, current setup
- **Phase 2 — ANALYSIS** (9 questions): Where they're losing leads — missed calls, slow response, no after-hours, poor conversion
- **Phase 3 — ACTION** (4 questions): Quantify pain, qualify readiness, invite the solution

**Actions:**
- Write all 18 questions with field types (dropdown, multiple choice, short text, number, scale)
- Include Wix-specific setup notes (field labels, required/optional flags)
- Include scoring notes so Claude knows how to weight each answer
- Include a section on the revenue loss formula Claude will use

**The 18 Questions:**

```
--- PHASE 1: AWARENESS (Current State) ---

Q1. What type of service business do you run?
    [Dropdown] Physiotherapy / Chiropractic / Dentistry / Beauty & Aesthetics /
    Gym & Fitness / Roofing / Plumbing & Trades / Real Estate / Law Firm /
    Medical / Veterinary / Other (please specify)

Q2. How many calls does your business receive per week on average?
    [Dropdown] Less than 20 / 20–50 / 50–100 / 100–200 / 200+

Q3. What are your business hours?
    [Multiple choice — tick all that apply]
    Mon–Fri standard hours (9am–5pm) / Extended weekday hours / Saturday /
    Sunday / Public holidays / We're available 24/7

Q4. Do you have a dedicated receptionist or front desk person?
    [Single choice]
    Yes — full time / Yes — part time / We take turns answering / Voicemail only /
    No system in place

Q5. How many staff members handle incoming calls and enquiries?
    [Number field]

--- PHASE 2: ANALYSIS (The Gaps) ---

Q6. How many calls per week do you estimate go unanswered or to voicemail?
    [Dropdown] Almost none / 1–5 / 5–15 / 15–30 / More than 30 / I honestly don't know

Q7. What typically happens when a call is missed?
    [Single choice]
    We always call back same day / We call back the next business day /
    We rely on voicemail — most people leave a message / Many don't leave messages and we lose them /
    We rarely get back to missed calls

Q8. How quickly do you respond to website enquiries or contact form submissions?
    [Single choice]
    Within 1 hour / Same day / Next business day / Longer than that /
    We don't have a consistent process

Q9. How many new enquiries or leads do you receive per week? (calls + web + social combined)
    [Number field or dropdown] Less than 5 / 5–10 / 10–20 / 20–50 / 50+

Q10. What percentage of enquiries convert to a booked appointment or paid job?
     [Dropdown] Less than 10% / 10–25% / 25–50% / 50–75% / Over 75%

Q11. What is the average value of a new client or booking for your business?
     [Dropdown — AUD]
     Under $100 / $100–$300 / $300–$600 / $600–$1,000 / $1,000–$3,000 / Over $3,000

Q12. Do you have any system for handling after-hours enquiries?
     [Single choice]
     Yes — someone is on call / Voicemail only / We use an answering service /
     No — if they call after hours, we miss them

Q13. How do most clients contact you? (tick all that apply)
     [Multiple choice]
     Phone call / Text/SMS / Email / Website contact form /
     Instagram/Facebook DM / Walk-in / Google Business message

Q14. Do you currently use any automated follow-up for missed calls or enquiries?
     [Single choice]
     Yes — we have a system / Partially — we follow up manually when we remember /
     No — nothing automated

--- PHASE 3: ACTION (Quantify + Readiness) ---

Q15. Have you ever knowingly lost a client because of a missed call or slow response?
     [Single choice]
     Yes — happens regularly / Yes — a few times / Not sure — probably /
     Rarely or never

Q16. What is your biggest frustration with how your business handles incoming calls and leads?
     [Open text — short answer]

Q17. If an AI could answer every call, respond to every text, and book appointments
     automatically — 24 hours a day, 7 days a week — what would that be worth to
     your business?
     [Single choice]
     It would be transformational / Significant — we'd book noticeably more clients /
     Useful but not critical / Not sure yet

Q18. What's your first name and the best email address to send your results to?
     [Two short text fields: First Name + Email]
```

**Files affected:**
- `reference/ai-receptionist-audit-questions.md` (create)

---

### Step 2: Create the Email Template

Create `reference/ai-receptionist-email-template.md` with the email structure Claude will follow, including tone guidelines, the revenue loss frame, and the CTA.

**Email Structure:**

```
Subject: [First Name], here's what your audit found — and it's not good news

---

Hi [First Name],

Thanks for completing the WILBA AI Receptionist Audit for [Business Name/Type].

I've run your answers through our analysis and I want to give it to you straight.

--- THE NUMBER ---
Based on your responses, [Business Name/Type] is likely losing somewhere between
$[LOW_ESTIMATE] and $[HIGH_ESTIMATE] every month in missed leads.

Here's how I got there:
- You receive approximately [X] calls/enquiries per week
- An estimated [Y] of those go unanswered or don't convert
- With an average booking value of $[Z], that's [N] missed opportunities per month

That's not a technology problem. That's a front desk problem.

--- YOUR TOP 3 GAPS ---
[Claude generates 3 specific observations based on their answers, e.g.:]
1. You're missing after-hours calls — [X]% of service business bookings happen
   outside standard hours
2. Your follow-up window is too long — leads that aren't contacted within 5 minutes
   are 10x less likely to convert
3. You rely on voicemail — 80% of callers who reach voicemail don't leave a message

--- THE FIX ---
An AI receptionist handles all of this automatically:
✓ Answers every call, 24/7
✓ Responds to texts and web enquiries instantly
✓ Books appointments directly into your calendar
✓ Sends missed-call texts within 60 seconds
✓ Follows up with leads who didn't book

No staff. No after-hours stress. No missed bookings.

--- NEXT STEP ---
I'd love to show you exactly how this would work for [their business type].
It's a 20-minute call — no pitch, just clarity on what's possible.

👉 [Book a call here — Calendly link]

Talk soon,
Jess Morrell
Founder, WILBA.ai
[Phone] | jess@wilba.ai | wilba.ai

P.S. The AI receptionist demo takes about 2 minutes. I'll show you on the call.
```

**Tone notes for Claude:**
- Confident but not aggressive
- Lead with the number — that's what gets attention
- Short paragraphs, scannable
- Don't over-explain the tech — explain the outcome
- One CTA only (the Calendly link)

**Files affected:**
- `reference/ai-receptionist-email-template.md` (create)

---

### Step 3: Create the Python Automation Script

Create `scripts/audit_email_responder.py` — a Flask webhook receiver that:
1. Receives form data from Wix (via webhook POST)
2. Passes the data to Claude with a carefully constructed prompt
3. Claude calculates revenue loss and writes the personalised email
4. Sends the email via SendGrid (or SMTP fallback)
5. Logs the response to a local CSV for Jess's lead tracking

**Script Architecture:**

```python
# scripts/audit_email_responder.py
#
# What this does:
# 1. Listens for form submissions from Wix (webhook POST to /audit-webhook)
# 2. Parses the audit answers
# 3. Sends to Claude with a revenue calculation + email writing prompt
# 4. Sends the personalised email to the respondent
# 5. Logs the lead to outputs/audit/leads.csv
#
# How to run: python audit_email_responder.py
# How to deploy: see reference/audit-automation-guide.md

import os
import json
import csv
from datetime import datetime
from flask import Flask, request, jsonify
import anthropic
import sendgrid
from sendgrid.helpers.mail import Mail
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

SYSTEM_PROMPT = """
You are an AI analyst for WILBA.ai, an AI automation agency run by Jess Morrell.
Your job is to analyse a completed AI Receptionist Audit from a service business owner
and produce two things:

1. A revenue loss estimate (low and high range, in AUD) based on their answers
2. A personalised email that Jess will send to the prospect

The email should:
- Open with the revenue loss estimate, stated clearly and confidently
- Identify their top 3 specific gaps based on their answers
- Explain what an AI receptionist would do for their specific situation
- End with a single CTA to book a 20-minute call (use the Calendly URL provided)
- Match WILBA's tone: confident, direct, clear. Think McConaughey meets direct response.
  Warm but not fluffy. Bold but not pushy. One paragraph max per section.

Revenue loss formula:
  weekly_enquiries × missed_rate × conversion_rate × avg_value × 4.33 = monthly_loss

  missed_rate: derive from Q6 and Q7 answers
  conversion_rate: use Q10 answer (midpoint of range)
  avg_value: use Q11 answer (midpoint of range)

  Provide LOW estimate (conservative) and HIGH estimate (realistic worst case).
  Round to nearest $100. Never say "exactly" — say "somewhere between X and Y".

Output format — return valid JSON:
{
  "revenue_loss_low": 1200,
  "revenue_loss_high": 3800,
  "top_gaps": [
    "Gap 1 description (1-2 sentences, specific to their answers)",
    "Gap 2 description",
    "Gap 3 description"
  ],
  "email_subject": "Subject line here",
  "email_body": "Full email body here (plain text, use line breaks)"
}
"""

def calculate_and_write_email(audit_data: dict, calendly_url: str) -> dict:
    """Send audit data to Claude, get back revenue estimate + email copy."""

    user_prompt = f"""
Here are the completed audit answers. Analyse them and produce the revenue estimate and email.

RESPONDENT: {audit_data.get('first_name', 'there')} — {audit_data.get('business_type', 'service business')}
CALENDLY URL FOR CTA: {calendly_url}

AUDIT ANSWERS:
Q1 Business type: {audit_data.get('q1_business_type')}
Q2 Weekly calls: {audit_data.get('q2_weekly_calls')}
Q3 Business hours: {audit_data.get('q3_hours')}
Q4 Receptionist setup: {audit_data.get('q4_receptionist')}
Q5 Staff handling calls: {audit_data.get('q5_staff_count')}
Q6 Missed calls/week: {audit_data.get('q6_missed_calls')}
Q7 What happens when missed: {audit_data.get('q7_missed_handling')}
Q8 Response time to web enquiries: {audit_data.get('q8_response_time')}
Q9 Total weekly enquiries: {audit_data.get('q9_total_enquiries')}
Q10 Conversion rate: {audit_data.get('q10_conversion')}
Q11 Average booking value: {audit_data.get('q11_avg_value')}
Q12 After-hours handling: {audit_data.get('q12_after_hours')}
Q13 Contact channels: {audit_data.get('q13_contact_channels')}
Q14 Automated follow-up exists: {audit_data.get('q14_automation')}
Q15 Lost clients from slow response: {audit_data.get('q15_lost_clients')}
Q16 Biggest frustration: {audit_data.get('q16_frustration')}
Q17 Value of AI receptionist: {audit_data.get('q17_value_perception')}
"""

    message = client.messages.create(
        model="claude-opus-4-6",
        max_tokens=2000,
        system=SYSTEM_PROMPT,
        messages=[{"role": "user", "content": user_prompt}]
    )

    response_text = message.content[0].text
    return json.loads(response_text)

def send_email(to_email: str, to_name: str, subject: str, body: str) -> bool:
    """Send the personalised email via SendGrid."""

    sg = sendgrid.SendGridAPIClient(api_key=os.environ.get("SENDGRID_API_KEY"))

    message = Mail(
        from_email=(os.environ.get("FROM_EMAIL"), "Jess @ WILBA"),
        to_emails=[(to_email, to_name)],
        subject=subject,
        plain_text_content=body
    )

    try:
        response = sg.send(message)
        return response.status_code in [200, 201, 202]
    except Exception as e:
        print(f"Email send error: {e}")
        return False

def log_lead(audit_data: dict, email_result: dict):
    """Save lead to CSV for Jess's tracking."""

    log_file = "outputs/audit/leads.csv"
    os.makedirs("outputs/audit", exist_ok=True)

    file_exists = os.path.isfile(log_file)

    with open(log_file, "a", newline="") as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow([
                "timestamp", "name", "email", "business_type",
                "revenue_loss_low", "revenue_loss_high", "email_sent"
            ])
        writer.writerow([
            datetime.now().isoformat(),
            audit_data.get("first_name"),
            audit_data.get("email"),
            audit_data.get("q1_business_type"),
            email_result.get("revenue_loss_low"),
            email_result.get("revenue_loss_high"),
            "yes"
        ])

@app.route("/audit-webhook", methods=["POST"])
def handle_audit_submission():
    """Main webhook endpoint — receives Wix form data."""

    try:
        data = request.json

        # Wix sends data in a nested structure — flatten it
        # Adjust field names to match your actual Wix form field IDs
        audit_data = {
            "first_name": data.get("first_name", "there"),
            "email": data.get("email"),
            "business_type": data.get("q1_business_type"),
            "q1_business_type": data.get("q1_business_type"),
            "q2_weekly_calls": data.get("q2_weekly_calls"),
            "q3_hours": data.get("q3_hours"),
            "q4_receptionist": data.get("q4_receptionist"),
            "q5_staff_count": data.get("q5_staff_count"),
            "q6_missed_calls": data.get("q6_missed_calls"),
            "q7_missed_handling": data.get("q7_missed_handling"),
            "q8_response_time": data.get("q8_response_time"),
            "q9_total_enquiries": data.get("q9_total_enquiries"),
            "q10_conversion": data.get("q10_conversion"),
            "q11_avg_value": data.get("q11_avg_value"),
            "q12_after_hours": data.get("q12_after_hours"),
            "q13_contact_channels": data.get("q13_contact_channels"),
            "q14_automation": data.get("q14_automation"),
            "q15_lost_clients": data.get("q15_lost_clients"),
            "q16_frustration": data.get("q16_frustration"),
            "q17_value_perception": data.get("q17_value_perception"),
        }

        if not audit_data.get("email"):
            return jsonify({"error": "No email provided"}), 400

        calendly_url = os.environ.get("CALENDLY_URL", "https://calendly.com/jess-wilba")

        # Get Claude to analyse and write the email
        email_result = calculate_and_write_email(audit_data, calendly_url)

        # Send the email
        sent = send_email(
            to_email=audit_data["email"],
            to_name=audit_data["first_name"],
            subject=email_result["email_subject"],
            body=email_result["email_body"]
        )

        # Log the lead
        log_lead(audit_data, email_result)

        return jsonify({
            "status": "success",
            "email_sent": sent,
            "revenue_loss_estimate": f"${email_result['revenue_loss_low']}–${email_result['revenue_loss_high']}/month"
        }), 200

    except Exception as e:
        print(f"Error processing audit: {e}")
        return jsonify({"error": str(e)}), 500

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"}), 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5001))
    app.run(host="0.0.0.0", port=port, debug=False)
```

**Files affected:**
- `scripts/audit_email_responder.py` (create)

---

### Step 4: Create requirements file

Create `scripts/requirements_audit.txt`:

```
anthropic>=0.40.0
flask>=3.0.0
sendgrid>=6.11.0
python-dotenv>=1.0.0
```

**Files affected:**
- `scripts/requirements_audit.txt` (create)

---

### Step 5: Create the Setup & Run Guide

Create `reference/audit-automation-guide.md` — a plain-English guide for Jess and her developer covering:

1. **What this system does** (2-paragraph overview)
2. **What you need** (API keys: Anthropic, SendGrid, Calendly URL)
3. **How to set up the Wix form** (step by step: create form, set field IDs, connect webhook)
4. **How to configure the .env file** (copy from .env.example, fill in keys)
5. **How to run locally for testing** (`pip install -r`, `python audit_email_responder.py`, use Postman or ngrok to test)
6. **How to deploy to Render.com** (create web service, connect GitHub repo, set env vars, deploy)
7. **How to connect Wix to the live webhook** (Wix Automations → webhook → paste Render URL)
8. **How to view leads** (open `outputs/audit/leads.csv`)
9. **Customisation notes** (how to change the Calendly link, email sender, tone)

**Files affected:**
- `reference/audit-automation-guide.md` (create)

---

### Step 6: Update CLAUDE.md

Add to the workspace structure section and commands section to reflect:
- New `outputs/audit/` directory and its purpose
- The audit automation capability
- Where to find the audit questions and email template

**Files affected:**
- `CLAUDE.md` (modify — workspace structure + notes sections)

---

### Step 7: Create outputs/audit directory marker

Create `outputs/audit/.gitkeep` to ensure the directory exists in version control.

**Files affected:**
- `outputs/audit/.gitkeep` (create)

---

## Connections & Dependencies

### Files That Reference This Area

- `CLAUDE.md` — workspace overview, needs updating
- `context/strategy.md` — free audits as primary lead gen strategy; this directly executes that
- `reference/wilba-launch-plan.md` — old launch plan (content-focused); this supersedes it for the AI receptionist pivot

### Updates Needed for Consistency

- After implementation, Jess should update `context/business-info.md` to reflect the AI receptionist pivot as the primary WILBA offer
- `context/strategy.md` should note the audit funnel as the primary lead gen mechanism

### Impact on Existing Workflows

- This creates WILBA's first operational automation
- The audit CSV becomes the start of a CRM / lead tracking system
- Future plan: connect the CSV to a Google Sheet via the Google Sheets API for easier lead management

---

## Validation Checklist

- [ ] `reference/ai-receptionist-audit-questions.md` created with all 18 questions, field types, and scoring notes
- [ ] `reference/ai-receptionist-email-template.md` created with full email structure and Claude tone instructions
- [ ] `scripts/audit_email_responder.py` created and runs without errors locally
- [ ] `scripts/requirements_audit.txt` created
- [ ] `reference/audit-automation-guide.md` created with complete setup instructions
- [ ] `outputs/audit/` directory created
- [ ] Script tested locally: submit test JSON → Claude generates email → email sends successfully
- [ ] `CLAUDE.md` updated to reflect new files and capability
- [ ] `.env.example` updated with new required keys

---

## Success Criteria

The implementation is complete when:

1. Jess can copy the 18 audit questions directly into a Wix form, publish it, and share the link
2. When a test submission is made, the Python script receives it, calls Claude, and sends a personalised email to the test address within 60 seconds
3. The lead is logged to `outputs/audit/leads.csv` with the revenue loss estimate
4. The setup guide is clear enough that Jess's developer can deploy to Render.com without needing to ask Jess any questions

---

## Notes

**Revenue Loss Formula (reference):**
```
weekly_missed = weekly_calls × missed_rate
monthly_missed = weekly_missed × 4.33
monthly_revenue_lost = monthly_missed × conversion_rate × avg_value

Example: 80 calls/week × 30% missed × 25% conversion × $500 avg = $2,598/month
```

**Distribution channels for the audit link (Jess's to-do list):**
- Local Facebook groups (tradies, small business, BNI)
- LinkedIn DMs to local service businesses
- Instagram story / link in bio
- Direct outreach message with the link
- Google Business profiles of target businesses

**Future enhancements (not in this plan):**
- Add a Google Sheet integration to replace the CSV
- Add a Jess-notification email (BCC or separate) so she knows immediately when a lead comes in
- Build a PDF version of the audit report using the AIOS pdf skill
- Add SMS notification (Twilio) for Jess when a high-value lead submits

**The narrative this sells:**
Every audit email is a demonstration that AI automation works — because an AI just wrote a personalised sales email and sent it automatically. That's the meta-pitch. Jess should mention this on calls: "By the way, that email you received 2 minutes after filling out the form? That was AI. That's what we build."
