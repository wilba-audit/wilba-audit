# 🌅 Good Morning Jess — AI Audit Setup Checklist

Everything is built and wired up. Here's what's done and the 3 things you need to finish (15 min total).

---

## ✅ What's Done (you slept, I shipped)

| Component | Status |
|-----------|--------|
| **18-question Wix audit form** | ✅ Built — "Free AI Audit" in Wix Forms |
| **Flask webhook server** (`scripts/audit_email_responder.py`) | ✅ Written and tested locally |
| **Claude-powered email generation** | ✅ Revenue loss calculator + personalised email prompt |
| **Wix Automation** | ✅ Created — "AI Audit — Send to Webhook" (saved, not activated) |
| **Deployment config** | ✅ `Procfile`, `render.yaml`, `runtime.txt` ready |
| **Environment variables** | ✅ Template in `.env` — ANTHROPIC_API_KEY already set |
| **Lead logging** | ✅ Auto-logs to `outputs/audit/leads.csv` |
| **Setup guide** | ✅ `reference/ai-receptionist-audit-setup.md` |

---

## 🔧 What You Need To Do (3 steps, ~15 min)

### Step 1: Get a SendGrid API Key (5 min)

1. Go to **https://app.sendgrid.com** — create a free account (100 emails/day)
2. Go to **Settings → API Keys → Create API Key** (Full Access)
3. Copy the key
4. Open your `.env` file and paste it after `SENDGRID_API_KEY=`
5. **Sender verification**: Go to Settings → Sender Authentication
   - Option A (quick): Single Sender Verification → verify `hello@wilba.ai`
   - Option B (better): Domain Authentication → add DNS records to Wix

### Step 2: Deploy to Render (5 min)

1. **Push to GitHub** (if you haven't already):
   ```
   cd /Users/jessmorrell/Documents/AAA/aios-starter-kit
   git init
   git add scripts/audit_email_responder.py scripts/requirements-audit.txt scripts/__init__.py Procfile render.yaml runtime.txt
   git commit -m "AI Receptionist Audit webhook server"
   git remote add origin YOUR_GITHUB_REPO_URL
   git push -u origin main
   ```

2. Go to **https://render.com** → New → **Web Service**
3. Connect your GitHub repo
4. Settings:
   - **Build command**: `pip install -r scripts/requirements-audit.txt`
   - **Start command**: `gunicorn scripts.audit_email_responder:app`
5. Add environment variables:
   - `ANTHROPIC_API_KEY` = (your key from .env)
   - `SENDGRID_API_KEY` = (the one you just created)
   - `FROM_EMAIL` = `hello@wilba.ai`
   - `CALENDLY_URL` = `https://calendly.com/hello-wilba`
   - `TEST_EMAIL` = `jess@wilba.ai`
6. Deploy!
7. Note your URL (e.g. `https://wilba-audit-responder.onrender.com`)

**Important**: If your Render URL is different from `wilba-audit-responder`, update the Wix Automation:
   - Wix Dashboard → Automations → "AI Audit — Send to Webhook" → Edit
   - Click the "Send HTTP request" action
   - Update the Webhook URL to: `https://YOUR-APP.onrender.com/audit-webhook`

### Step 3: Activate & Test (5 min)

1. **Test the server first**: Visit `https://YOUR-APP.onrender.com/test-audit` in your browser
   - You should see a preview of the audit email for "Sarah" (sample physio client)
   - If it works, the Claude + email generation pipeline is live ✅

2. **Activate the Wix Automation**:
   - Wix Dashboard → Automations → "AI Audit — Send to Webhook"
   - Click **Activate** (top right)

3. **Publish the audit form page** (if not already published):
   - Go to the Wix Editor → find the page with the Free AI Audit form
   - Make sure it's published and accessible at your desired URL

4. **End-to-end test**:
   - Open the audit form on wilba.ai
   - Fill it out with test data
   - Check your inbox (jess@wilba.ai or hello@wilba.ai) for the audit email
   - Check Render logs for any errors
   - Check `outputs/audit/leads.csv` for the logged lead

---

## 🔗 The Complete Flow

```
Prospect fills out Free AI Audit form on wilba.ai
        ↓
Wix Automation fires → POST to your Render webhook
        ↓
Flask server receives form data → sends to Claude
        ↓
Claude analyses answers → calculates revenue loss → writes personalised email
        ↓
SendGrid delivers email to prospect's inbox
        ↓
Lead logged to CSV for your tracking
        ↓
Email CTA: "Book a 20-minute call" → Calendly link
```

---

## 📊 What the Prospect Gets

A personalised email showing:
- **Their specific revenue loss** (conservative and realistic estimates)
- **Their top 3 gaps** based on their actual audit answers
- **What changes** with an AI receptionist (outcomes, not features)
- **One CTA**: Book a 20-minute call with you

The tone is warm, confident, direct — like a smart friend showing them the money they're leaving on the table.

---

## 🚨 If Something Goes Wrong

- **Email not sending**: Check SendGrid API key and sender verification
- **Claude error**: Check ANTHROPIC_API_KEY is correct in Render env vars
- **Webhook not firing**: Check the Wix Automation is activated + URL is correct
- **Form data not parsing**: Check Render logs — the parser handles multiple Wix data formats
- **Test endpoint**: Always test at `/test-audit` first before going live

---

*Built overnight by Claude. Go get that first client.* 🚀
