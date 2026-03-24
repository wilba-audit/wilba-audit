# Baha Baha Villas — AI Receptionist System Design

**Version:** 1.0
**Last updated:** 2026-03-23
**Status:** Draft — pending Booking Layer API access and room/package confirmation

---

## System Overview

Two core automations running autonomously:

1. **Daily Morning Brief** — Pulls all booking data each morning, compiles an ops summary, emails the team before they start their day
2. **Multi-Language Email Responder** — Monitors the Gmail inbox, detects the language of each guest email, and drafts (or auto-sends) a contextually accurate reply

Both run on a hosted server (Render.com — same as WILBA's existing audit pipeline).

---

## Architecture Diagram

```
BOOKING SOURCES
├── Booking Layer (PMS) ──────────────────┐
│   └── OTAs via Channex channel manager  │
│       (Booking.com, Agoda, etc.)        │
├── World Surfaris (email confirmations)  ├──► AGGREGATOR SCRIPT
├── Manual bookings (Instagram/WhatsApp)  │    (Python, runs daily)
│   └── Manual entry spreadsheet         │
└── Walk-ins                              │
    └── Manual entry spreadsheet         ┘
                                          │
                                          ▼
                               UNIFIED BOOKING DATA
                               (normalised to data model)
                                          │
                    ┌─────────────────────┼──────────────────────┐
                    ▼                     ▼                      ▼
            DAILY BRIEF            EMAIL RESPONDER        (FUTURE)
            GENERATOR              (Gmail Listener)       WHATSAPP
                    │                     │               RESPONDER
                    │                     │
                    ▼                     ▼
              CLAUDE API             CLAUDE API
           (format + write)     (detect lang + draft)
                    │                     │
                    ▼                     ▼
              SENDGRID             GMAIL DRAFTS
          (deliver to team)       (or auto-send)
```

---

## Component 1: Daily Morning Brief

### What it does
Every morning at a configured time, the script:
1. Calls the Booking Layer API to get today's bookings
2. Fetches World Surfaris bookings (from parsed email or manual Google Sheet)
3. Normalises all data to the unified booking model
4. Calls Claude API to write a friendly, readable brief in plain English
5. Sends the brief via SendGrid (or Gmail SMTP) to all configured recipients

### Technical Stack
| Layer | Tool | Notes |
|-------|------|-------|
| Language | Python 3.11 | Consistent with existing WILBA scripts |
| Booking data | Booking Layer REST API | Requires API key from Sean |
| Surf vendor data | Google Sheets (manual) OR email parser | MVP = manual sheet |
| AI formatting | Claude API (claude-3-5-haiku-20241022) | Fast + cheap for daily formatting |
| Email delivery | SendGrid | Already in WILBA stack |
| Scheduler | Render Cron Job | Same platform as audit pipeline |
| Timezone | Asia/Makassar (WITA, UTC+8) | Sumbawa timezone |

### Booking Layer API

**Base URL:** `https://api.bookinglayer.io/v2/`
**Auth:** Bearer token (API key from Sean's account settings)
**Key endpoints:**
```
GET /reservations
  ?check_in_from=YYYY-MM-DD
  &check_in_to=YYYY-MM-DD
  → Returns all reservations checking in on that date

GET /reservations
  ?check_out_from=YYYY-MM-DD
  &check_out_to=YYYY-MM-DD
  → Returns all reservations checking out on that date

GET /reservations?status=checked_in
  → Returns all currently in-house guests
```

### Daily Brief Email Format
```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🏄 BAHA BAHA DAILY OPS BRIEF
[Day], [Date] | WITA

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CHECKING IN TODAY (X guests)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
• [Guest Name] — [Room] | [Package] | [Meal plan]
  Transfer: [Yes — arriving [TIME] from [AIRPORT/FERRY] | No]
  Notes: [Special requests or none]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CHECKING OUT TODAY (X guests)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
• [Guest Name] — [Room] | [X nights]
  Transfer: [Yes — departing [TIME] to [AIRPORT] | No]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
TRANSFERS TODAY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
• [TIME] — PICKUP: [Guest Name] from [Airport/Ferry]
• [TIME] — DROP: [Guest Name] to [Airport/Ferry]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CURRENTLY IN HOUSE (X guests)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
• [Guest Name] — [Room] | [Package] | Day [X] of [Y]
  Notes: [Any active special requests]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
NEXT 48 HOURS (Upcoming arrivals)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
• [Tomorrow] [Guest Name] — [Room] | [Package]
  Transfer: [Yes/No]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
⚠️  FLAGS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
• [Any issues, missing info, or action items]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Powered by WILBA · wilba.ai
```

### Fallback Logic
- If Booking Layer API is down → send brief with error notice + last known data
- If no bookings for today → send brief saying "All clear — no arrivals, departures, or transfers today"
- If World Surfaris data missing → flag in the brief "⚠️ World Surfaris: no data received"

---

## Component 2: Multi-Language Email Responder

### What it does
Monitors the Gmail inbox (`bookings@[bahavillas].com`) for new guest emails. For each new email:
1. Detects the sender's language
2. Classifies the intent (availability inquiry / pricing / transfer / FAQ / complex booking)
3. Generates a contextually accurate reply in the same language
4. Saves as Gmail Draft (owner reviews and sends) OR auto-sends for simple FAQs

### Technical Stack
| Layer | Tool | Notes |
|-------|------|-------|
| Email monitoring | Gmail API (OAuth 2.0) | Watches inbox via polling or push |
| Language detection | Claude API | No language list needed — detects automatically |
| Response generation | Claude API (claude-3-5-sonnet-20241022) | Better quality for guest-facing comms |
| Draft saving | Gmail API | Saves replies as drafts for review |
| Auto-send (FAQs) | Gmail API + flag | Owner can enable per intent category |
| Run frequency | Every 15 minutes | Via Render cron |

### Intent Categories

| Intent | Description | Default Mode | Auto-send criteria |
|--------|-------------|-------------|-------------------|
| `availability` | "Do you have rooms on X dates?" | Draft | Simple yes/no after lookup |
| `pricing` | "How much for X nights?" | Draft | Rate card query |
| `transfer` | "Can you pick us up from the airport?" | Draft | Standard transfer |
| `surf_inquiry` | "What surf packages do you have?" | Draft | Standard package info |
| `faq` | "Do you have WiFi / what's the food like?" | Auto-send | Purely informational |
| `booking_request` | "I'd like to book X" | Draft | Always draft — needs confirmation |
| `modification` | Change to existing booking | Draft | Always draft |
| `cancellation` | Cancel request | Draft | Always draft |
| `other` | Anything unclassified | Draft | Flag for manual review |

### Language Support
Claude API handles all languages automatically. No explicit list required. The response is generated in the same language as the guest's email. For Indonesian-language emails from local contacts, it responds in Indonesian (Bahasa Indonesia).

### Claude System Prompt (Email Responder)
```
You are the AI receptionist for Baha Baha Villas, a premium surf and accommodation property
in West Sumbawa, Indonesia. You are warm, professional, and enthusiastic about surfing and
the island lifestyle.

Property details:
- Location: West Sumbawa, Indonesia (near world-class surf breaks)
- Booking system: Booking Layer
- Contact email: bookings@[bahavillas]
- Transfers: Airport pickups available (Sumbawa Besar / Taliwang)

When responding to guest emails:
1. Always respond in the SAME LANGUAGE as the guest's email
2. Be warm, helpful, and reflect the surf/island vibe of the property
3. For availability/pricing questions, note that exact rates are confirmed upon booking
4. For booking requests, confirm you've received their request and will confirm shortly
5. Always include contact details and website for follow-up

Do not make up specific prices, availability, or details you are not certain about.
Flag anything uncertain with [CONFIRM] so the owner can review before sending.
```

### Gmail API Setup
```
Required OAuth scopes:
- gmail.readonly    — read incoming emails
- gmail.compose     — create draft replies
- gmail.send        — send auto-replies (FAQs only)

Setup steps:
1. Enable Gmail API in Google Cloud Console (Sean's Google account)
2. Create OAuth 2.0 credentials (Web Application type)
3. Download credentials.json
4. Run auth flow once to generate token.json
5. Store credentials securely in Render environment variables
```

---

## Component 3: World Surfaris Booking Parser (Phase 2)

### What it does
Monitors Gmail for booking confirmation emails from World Surfaris. Extracts booking details, normalises to the unified data model, and makes them available for the daily brief.

### Trigger
Any email in Gmail matching:
- From: `*@worldsurfaris.com` OR
- Subject containing: "booking confirmation" OR "reservation"

### Data Extraction
Claude API reads the email body and extracts the booking fields defined in the data model. Returns structured JSON that the daily brief script consumes.

---

## Deployment

### Hosting: Render.com
Consistent with WILBA's existing audit pipeline. Two services:

| Service | Type | Schedule | Purpose |
|---------|------|---------|---------|
| `baha-daily-brief` | Cron Job | 6:00am WITA daily | Morning brief generation + send |
| `baha-email-responder` | Cron Job | Every 15 minutes | Gmail inbox monitor + draft replies |

### Environment Variables Required
```
ANTHROPIC_API_KEY        — Claude API (shared with WILBA audit pipeline)
SENDGRID_API_KEY         — Email delivery (shared with WILBA audit pipeline)
BOOKING_LAYER_API_KEY    — From Sean's Booking Layer account
GMAIL_CREDENTIALS_JSON   — OAuth credentials for baha villas Gmail
GMAIL_TOKEN_JSON         — OAuth refresh token
BRIEF_RECIPIENTS         — Comma-separated email list for daily brief
BRIEF_SEND_TIME          — Time in WITA (default: 06:00)
```

### Timezone Configuration
All times displayed in **WITA (Waktu Indonesia Tengah)** = UTC+8 (same as Bali / WITA)

---

## Data Flow Summary

```
[6:00am WITA]
    │
    ▼
baha_daily_brief.py runs
    │
    ├── GET Booking Layer API → today's check-ins
    ├── GET Booking Layer API → today's check-outs
    ├── GET Booking Layer API → current in-house guests
    ├── GET Google Sheet → World Surfaris bookings (MVP)
    │
    ▼
Normalise all bookings to unified data model
    │
    ▼
Call Claude API → generate morning brief in plain English
    │
    ▼
Send via SendGrid to [BRIEF_RECIPIENTS]

[Every 15 minutes]
    │
    ▼
baha_email_responder.py runs
    │
    ├── Check Gmail inbox for unread emails
    ├── Filter: not from team, not spam, not automated
    │
    ▼
For each new guest email:
    ├── Claude API → detect language + classify intent
    ├── Claude API → generate reply in guest's language
    │
    ▼
Save as Gmail Draft (owner reviews + sends)
OR
Auto-send if intent = 'faq' and owner has enabled auto-send
```

---

## Security & Data Handling

- All API keys stored as Render environment variables (never in code)
- Gmail OAuth tokens stored as environment variables (not files)
- No guest data stored permanently — each run fetches fresh
- No PCI data handled (payments stay in Booking Layer / Mockapos)
- Logs: only booking IDs and timestamps (no PII in logs)

---

## Estimated Monthly Running Costs

| Service | Cost | Notes |
|---------|------|-------|
| Render Cron Jobs | ~$7/month | Starter plan |
| Claude API (daily brief) | ~$2/month | Haiku model, once daily |
| Claude API (email responder) | ~$5–10/month | Sonnet model, ~50 emails/month est. |
| SendGrid | $0 | Free tier (100 emails/day) |
| **Total** | **~$15–20/month** | Passed to client or absorbed in retainer |

---

_This document is a living spec. Update as Booking Layer API details are confirmed._
