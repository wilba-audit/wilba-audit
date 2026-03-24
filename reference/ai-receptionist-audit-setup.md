# AI Receptionist Audit — Setup Guide

## What This Is

An automated lead generation system for WILBA's AI Receptionist service:

1. Prospect fills out the 18-question audit form on wilba.ai
2. Wix sends form data to our webhook
3. Claude analyses the answers, calculates revenue loss, writes a personalised email
4. Email lands in their inbox showing exactly how much money they're losing
5. One CTA: book a 20-minute call with Jess

## The Flow

```
[Wix Form] → [Wix Automation webhook] → [Flask API on Render] → [Claude API] → [SendGrid] → [Prospect inbox]
                                              ↓
                                        [leads.csv log]
```

## Setup Steps

### 1. SendGrid (Email Delivery)

1. Go to https://app.sendgrid.com — create free account (100 emails/day free)
2. Settings → API Keys → Create API Key (Full Access)
3. Copy the key to `.env` as `SENDGRID_API_KEY`
4. Settings → Sender Authentication → verify `hello@wilba.ai` domain
   - Add the DNS records SendGrid gives you to your Wix domain settings
   - Or use Single Sender Verification as a quick start

### 2. Deploy the Script

**Option A: Render (Recommended — free tier available)**

1. Push the repo to GitHub (or just the scripts folder)
2. Go to https://render.com → New → Web Service
3. Connect your repo
4. Settings:
   - Build command: `pip install -r scripts/requirements-audit.txt`
   - Start command: `gunicorn scripts.audit_email_responder:app`
   - Add all env vars from `.env`
5. Note your URL: `https://your-app.onrender.com`

**Option B: Railway**

1. Go to https://railway.app → New Project
2. Deploy from GitHub
3. Add env vars
4. Note your URL

**Option C: Run locally with ngrok (for testing)**

```bash
cd /path/to/aios-starter-kit
python scripts/audit_email_responder.py
# In another terminal:
ngrok http 5000
# Use the ngrok URL as your webhook
```

### 3. Connect Wix Form to Webhook

1. In Wix Dashboard → Automations → New Automation
2. Trigger: "Wix Forms — Form submitted" → select "Free AI Audit"
3. Action: "Send an HTTP request"
   - URL: `https://your-app.onrender.com/audit-webhook`
   - Method: POST
   - Headers: `Content-Type: application/json`
   - Body: Include all form field values as JSON
4. Save and activate

### 4. Test the Flow

1. Visit `https://your-app.onrender.com/test-audit` to preview a sample email
2. Submit a test entry on the Wix form
3. Check the webhook logs on Render
4. Verify the email arrives
5. Check `outputs/audit/leads.csv` for the logged lead

## Environment Variables

| Variable | Required | Description |
|----------|----------|-------------|
| `ANTHROPIC_API_KEY` | Yes | Claude API key for analysis |
| `SENDGRID_API_KEY` | Yes | SendGrid for email delivery |
| `FROM_EMAIL` | Yes | Sender email (must be verified in SendGrid) |
| `CALENDLY_URL` | Yes | Booking link for the email CTA |
| `TEST_EMAIL` | No | Where test emails go (defaults to jess@wilba.ai) |
| `PORT` | No | Server port (defaults to 5000) |

## Files

| File | Purpose |
|------|---------|
| `scripts/audit_email_responder.py` | The main Flask webhook server |
| `scripts/requirements-audit.txt` | Python dependencies |
| `outputs/audit/leads.csv` | Lead tracking log (auto-created) |
| `reference/ai-receptionist-audit-setup.md` | This file |
