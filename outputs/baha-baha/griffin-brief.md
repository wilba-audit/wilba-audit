# Baha Baha Villas — Developer Brief for Griffin

**From:** Jess Morrell, WILBA
**To:** Griffin (Developer)
**Date:** March 2026
**Project:** AI Receptionist & Daily Ops Brief — Baha Baha Villas, West Sumbawa, Indonesia
**Deal value:** USD $1,800 setup + $300/month retainer

---

## What This Is

WILBA's first hospitality client. Sean owns a surf/accommodation property in West Sumbawa, Indonesia called Baha Baha Villas. We did a discovery call and scoped two AI automations:

1. **Daily Ops Brief** — Every morning at 6am WITA, a script pulls all booking data and emails the team a structured summary: who's checking in, who's checking out, transfers, guests currently in-house, and upcoming arrivals. No more opening five systems every morning.

2. **AI Email Receptionist** — Monitors the Gmail inbox every 15 minutes. Detects the guest's language, classifies their intent (availability, pricing, FAQ, etc.) and drafts a reply in the guest's language. Owner reviews drafts before sending. Auto-send enabled for simple FAQs.

Both run on Render — same setup as the WILBA audit pipeline you already know.

---

## Tech Stack

| Layer | Tool |
|-------|------|
| Hosting | Render.com (Cron Jobs) |
| Property Management System | Booking Layer (REST API) |
| Channel Manager | Channex (connects Booking Layer to OTAs — we don't touch this directly) |
| Surf vendor bookings | World Surfaris (email parser, Phase 2) |
| AI | Claude API (claude-opus-4-6 or haiku for daily brief, sonnet for email responder) |
| Email delivery | SendGrid (already in our stack) |
| Guest email inbox | Gmail (OAuth 2.0) |
| Language | Python 3.11 |
| Timezone | WITA (UTC+8) |

---

## What's Already Built

All scripts are written and sitting in the repo ready to go. Placeholders are flagged with ⚠️ wherever we need real data from Sean.

| File | Status | Notes |
|------|--------|-------|
| `scripts/baha_baha_daily_brief.py` | Built | Needs Booking Layer API key to test |
| `scripts/baha_baha_email_responder.py` | Built | Needs Gmail OAuth to test |
| `scripts/requirements-baha-baha.txt` | Done | All Python deps listed |
| `outputs/baha-baha/system-design.md` | Done | Full architecture, API endpoints, email format |
| `outputs/baha-baha/booking-data-model.md` | Done | Unified booking schema — room/package names are placeholders |
| `outputs/baha-baha/discovery-notes.md` | Done | Tech stack, open questions, what World Surfaris sends |
| `outputs/baha-baha/proposal.md` | Done | Sent to Sean — scope, pricing, timeline |

---

## What We're Waiting On From Sean

Nothing moves to deployment until we have these. I'm chasing Sean for them now.

| # | Item | Who provides it | Why it's needed |
|---|------|----------------|----------------|
| 1 | **Booking Layer API key** | Sean (account settings → API → Generate) | Core data source — Phase 1 can't run without it |
| 2 | **Gmail OAuth setup** | Sean + us on a call (5 min) | Email responder needs access to the bookings inbox |
| 3 | **World Surfaris booking email (sample)** | Sean (forward one to us) | Need to design the email parser for Phase 2 |
| 4 | **Exact room/villa names** | Sean (as they appear in Booking Layer) | Placeholders in data model — brief won't make sense with wrong names |
| 5 | **Exact package names** | Sean (accommodation only, surf, meals, etc.) | Same — need real names from the PMS |
| 6 | **Daily brief recipient list** | Sean | Who gets the morning email — names + addresses |
| 7 | **Brief send time** | Sean | What time WITA should it land (our default: 6:00am) |

---

## Booking Layer API

Modern cloud PMS. They have a REST API.

**Base URL:** `https://api.bookinglayer.io/v2/`
**Auth:** Bearer token (the API key Sean generates)

Key endpoints we're using:
```
GET /reservations?check_in_from=YYYY-MM-DD&check_in_to=YYYY-MM-DD   → today's check-ins
GET /reservations?check_out_from=YYYY-MM-DD&check_out_to=YYYY-MM-DD  → today's check-outs
GET /reservations?status=checked_in                                    → currently in-house
```

We'll need to confirm the exact Booking Layer API v2 docs — worth double-checking field names once Sean shares the key and we can hit a live endpoint.

---

## Render Deployment Plan

Two cron jobs on Render, same account as the audit pipeline:

| Service name | Type | Schedule | Script |
|---|---|---|---|
| `baha-daily-brief` | Cron Job | `0 22 * * *` (= 6am WITA / UTC+8) | `scripts/baha_baha_daily_brief.py` |
| `baha-email-responder` | Cron Job | `*/15 * * * *` | `scripts/baha_baha_email_responder.py` |

### Environment Variables to Add in Render

```
ANTHROPIC_API_KEY          # already set — shared with audit pipeline
SENDGRID_API_KEY           # already set — shared with audit pipeline
BOOKING_LAYER_API_KEY      # from Sean's Booking Layer account
GMAIL_CREDENTIALS_JSON     # OAuth credentials for the bookings Gmail
GMAIL_TOKEN_JSON           # OAuth refresh token
BRIEF_RECIPIENTS           # comma-separated emails for daily brief
BRIEF_SEND_TIME            # e.g. "06:00" WITA
```

---

## Gmail OAuth Setup Process

When we get Sean on a call to do the Gmail auth:

1. Enable Gmail API in Google Cloud Console (under Sean's Google account or a WILBA service account)
2. Create OAuth 2.0 credentials → Web Application type
3. Download `credentials.json`
4. Run the one-time auth flow to generate `token.json`
5. Store both as Render environment variables (not files in repo)

Required OAuth scopes:
```
https://www.googleapis.com/auth/gmail.readonly
https://www.googleapis.com/auth/gmail.compose
https://www.googleapis.com/auth/gmail.send
```

---

## Phase Breakdown

**Phase 1 (Weeks 1–2): Daily Morning Brief**
- Booking Layer API connection live
- World Surfaris manual Google Sheet as fallback (MVP — email parser in Phase 2)
- Morning brief tested with real data, send time confirmed
- Deployed to Render, running unattended

**Phase 2 (Weeks 3–4): AI Email Receptionist**
- Gmail OAuth live on Sean's bookings inbox
- Language detection + intent classification tested with sample emails in 3+ languages
- Draft mode working (owner sees drafts in Gmail before sending)
- World Surfaris email parser added if sample email received

**Phase 3 (Future):** WhatsApp integration — not in scope yet.

---

## Meeting Notes Reference

Discovery call was recorded on Fireflies:
`https://app.fireflies.ai/view/Jess-Sean-AI-setup::01KMCH6K2GHZNAK5YAJ4AVJK35`

This is behind a Fireflies login — I'll pull the summary and send it through separately. In the meantime, all key info from the call is captured in `outputs/baha-baha/discovery-notes.md`.

---

## Questions for Griffin

Before you dive into the scripts, a couple of things worth checking:

1. **Booking Layer API v2** — once Sean sends the key, can you hit the `/reservations` endpoint and confirm field names match what's in the script? The docs suggest standard REST but worth validating.
2. **World Surfaris MVP approach** — I'm proposing a manual Google Sheet for Phase 1 (Sean's team enters them manually). Does that work with how the script currently handles it, or do you want to use a different fallback?
3. **Gmail OAuth on Render** — any preference on how we store the OAuth token (env var vs. secret file)? The audit pipeline uses env vars — assuming same approach here.

---

## New Intel from the Discovery Call (Fireflies Summary)

Full meeting summary saved at `outputs/baha-baha/fireflies-summary.md`. Key things that affect your work:

**Team members confirmed:**
- **Sean** — owner, decision-maker
- **Mashi** — handles Booking Layer coordination, system cleanup, is the point of contact for BL support
- **Danny** — manages transport and flight bookings daily

**New rooms confirmed (add to data model):**
- Baja room
- Studio
- Note: studio + 2-bed need to be linkable as a combined "deluxe" unit — Booking Layer currently can't do this automatically. Mashi is working on it.

**Agencies & commissions:**
- One Wave (~12.5% commission)
- World Safaris (~20% commission)
- Channel manager is **ChanX** (not just Channex)
- Most agency bookings still arrive manually despite ChanX

**Booking Layer access:**
- Jess needs to be re-added as Manager (jessmorrell@gmail.com)
- Developer (you) also needs to be added before we can get API credentials
- Sean has a deadline of 25 Mar to action this — may already be done, worth checking

**Scope clarification — Phase 1:**
The meeting described Phase 1 as a chatbot on **website + WhatsApp + Instagram**, with the daily ops brief as Phase 2. Our existing proposal has it the other way around. I need to align with Sean on this. For now, keep building both — but flag if the WhatsApp integration changes your architecture significantly.

**WhatsApp is the primary guest channel** — more than email. Phase 1 chatbot should prioritise WA.

**Google Drive is a mess** — content automation is blocked until Sean cleans it up. Not your problem for now, but worth knowing.

**Accounting:** Journal.co.id + Moka POS are disconnected. Out of scope for Phase 1, but don't build anything that assumes accounting integration.

---

## Bigger Picture

Once this is live and working, this system becomes WILBA's **Hospitality AI Receptionist template** — we resell it to other surf resorts, retreat centres, and boutique properties. Baha Baha is the pilot that proves the model. Let's make it bulletproof.

---

*Brief prepared by Jess Morrell · WILBA · wilba.ai*
*Questions? Jess@wilba.ai*
