# Plan: Baha Baha Villas — AI Receptionist & Daily Briefing Agent

**Created:** 2026-03-23
**Status:** Implemented
**Request:** Build an AI agent for Baha Baha Villas (West Sumbawa) that handles multi-language guest communications, responds to emails, and delivers a daily operations briefing to the owner and team each morning.

---

## Overview

### What This Plan Accomplishes

Design and build an AI Receptionist system for Baha Baha Villas that aggregates booking data from Booking Layer and third-party surf vendors, sends a daily morning briefing email to the owner and team summarising check-ins, check-outs, transfers, and packages, and handles incoming guest email inquiries in multiple languages. The system runs autonomously — the team wakes up informed and ready without any manual admin.

### Why This Matters

This is WILBA's first hospitality/retreat AI Automation client and a proof-of-concept case study for the broader retreat and surf resort niche. It directly demonstrates WILBA's pitch ("We find where you're bleeding time and fix it") applied to a real, scrappy hospitality operation. A working system here becomes a reusable template sold to other retreat and surf resort operators globally.

---

## Current State

### Relevant Existing Structure

- `context/business-info.md` — Baha Baha Villas mentioned as potential WILBA case study and retreat venue
- `scripts/audit_email_responder.py` — Existing Flask email automation pattern to follow
- `reference/ai-receptionist-audit-setup.md` — Audit pipeline setup guide (reference for similar architecture)
- `outputs/audit/` — Existing automation output patterns

### Gaps or Problems Being Addressed

- No AI layer exists at Baha Baha Villas today
- Bookings are split across Booking Layer + surf vendor partners — no unified view
- Morning ops prep is manual (checking systems, compiling who's arriving/leaving)
- Guest inquiries arrive in multiple languages — manual reply is slow and error-prone
- Owner and team are time-constrained in a remote location with limited admin bandwidth

---

## Discovery — Questions to Ask on the Call

> Use this section during the discovery call with the Baha Baha owner. Answers feed directly into the technical design.

### Bookings & Data Sources

1. **Booking Layer:** Does it have an API? Can it export daily reports (CSV, webhook, scheduled email)?
2. **Surf vendors:** How do they send booking info — email, spreadsheet, their own portal?
3. **Single source of truth:** Is there one central calendar where all bookings live, or are they siloed?
4. **Volume:** Roughly how many bookings per month? Peak season vs. low season?

### Guest Experience

5. **Languages:** What languages do most guests speak? (English, French, Spanish, German, Indonesian, Japanese, Brazilian Portuguese?)
6. **Guest comms channel:** Do guests contact you by email, WhatsApp, booking platform inbox, or all three?
7. **Reply preference:** Auto-reply vs. AI drafts a reply for human review and send?
8. **Common inquiries:** What questions do guests ask most? (Transfers, meal options, surf conditions, visa, equipment?)

### Operations & Packages

9. **Room types:** What are all room/villa options and their names?
10. **Meal options:** Breakfast only, half-board, full-board, self-catering? How is this tracked in Booking Layer?
11. **Transfer types:** Airport pickup, surf spots, other locations? How are these currently logged?
12. **Surf packages:** What packages exist? (Surf lessons, guided trips, equipment rental, combo packages?)
13. **Vendor structure:** Which vendors send surf packages — how many, how often, in what format?

### The Morning Brief

14. **Recipients:** Just owner, or the whole team? What are their names and email addresses?
15. **Internal language:** What language does the team use internally?
16. **Delivery time:** What time should it arrive? (e.g., 6:30am WITA / Bali time)
17. **Current morning routine:** What does the owner currently check every morning to prepare for the day?

### Tech & Access

18. **Email platform:** Gmail, Outlook, or other?
19. **Booking Layer access:** Do you have API credentials or a developer/admin login?
20. **Tech budget:** Open to $30–100/month in tools (SendGrid, OpenAI API, hosting)?
21. **WhatsApp:** Is WhatsApp the main guest communication channel? Would automating WhatsApp replies be valuable?

---

## Proposed System Architecture

### Component 1: Daily Morning Briefing Email

**What it does:** Every morning at a set time, the system pulls booking data, compiles a structured summary, and emails the owner and team.

**Email structure:**
```
BAHA BAHA DAILY OPS BRIEF — [Date]

CHECKING IN TODAY (X guests)
- [Guest Name] | [Room/Villa] | [Package] | [Arrival time] | [Transfer: Yes/No + details]

CHECKING OUT TODAY (X guests)
- [Guest Name] | [Room] | [Nights stayed] | [Departure time] | [Transfer: Yes/No]

TRANSFERS TODAY
- [Time] | [Type: Airport/Surf spot] | [Guest name] | [Notes]

CURRENTLY IN HOUSE (X guests)
- [Guest name] | [Room] | [Package] | [Nights remaining]

UPCOMING (Next 48 hours)
- [Guest name] | [Check-in date] | [Package summary]

NOTES / FLAGS
- [Any special requests, dietary needs, VIP notes]
```

**Technical approach:**
- Booking Layer API (or scheduled CSV export) → Python script → Claude API (to format/summarize) → SendGrid → Team inboxes
- Scheduled via cron job (daily at configured time)
- Handles missing data gracefully (flags gaps rather than crashing)

### Component 2: Multi-Language Guest Email Responder

**What it does:** Incoming guest emails trigger an AI response drafted in the guest's language.

**Language detection:** Claude API detects language of incoming email and responds in kind
**Supported languages (based on discovery):** English, French, Spanish, Indonesian, Japanese, German — TBD

**Response modes:**
- **Auto-reply:** AI sends immediately (best for FAQs — pricing, availability, transfers)
- **Draft mode:** AI drafts reply, owner reviews before sending (best for complex bookings)

**Technical approach:**
- Gmail API (or email forwarding hook) triggers script on new inbound email
- Claude API: detect language → classify intent → generate appropriate response
- SendGrid (or Gmail API) sends reply or saves as draft

### Component 3: Booking Data Aggregator

**What it does:** Pulls and normalizes data from multiple sources into one unified daily snapshot.

**Sources:**
- Booking Layer (primary PMS) — API or export
- Surf vendor bookings — email parsing or manual CSV upload (MVP)
- Future: WhatsApp Business API

**Data model (per booking):**
```
Guest name | Email | Language | Room type | Check-in | Check-out
Package (accommodation only / surf / food incl.) | Meal plan
Transfer in (time, from) | Transfer out (time, to)
Special requests | Vendor source | Notes
```

---

## Proposed Changes

### Summary of Changes

- Create `outputs/baha-baha/` directory for all Baha Baha project files
- Create discovery notes file from call
- Create system design document
- Create proposal document for the owner
- Create implementation plan (this document evolves into technical spec)
- Build MVP scripts (Phase 2 — after discovery confirmed)

### New Files to Create

| File Path | Purpose |
|-----------|---------|
| `outputs/baha-baha/discovery-notes.md` | Notes from today's discovery call — raw answers |
| `outputs/baha-baha/system-design.md` | Full technical architecture (updated after discovery) |
| `outputs/baha-baha/proposal.md` | Client-facing proposal with scope, pricing, timeline |
| `outputs/baha-baha/booking-data-model.md` | Schema for unified booking data (room types, packages, etc.) |
| `scripts/baha_baha_daily_brief.py` | Morning briefing script (Phase 2) |
| `scripts/baha_baha_email_responder.py` | Guest email AI responder (Phase 2) |
| `scripts/requirements-baha-baha.txt` | Python dependencies for Baha Baha scripts |

### Files to Modify

| File Path | Changes |
|-----------|---------|
| `CLAUDE.md` | Add Baha Baha project under Active Automations |
| `context/current-data.md` | Add Baha Baha as active project in status table |

---

## Design Decisions

### Key Decisions Made

1. **Booking Layer API first:** Assume Booking Layer has an API (they're a modern PMS — they do). If not, fall back to scheduled email export parsing. Confirm on call.
2. **SendGrid for email delivery:** Consistent with existing WILBA stack (audit pipeline uses SendGrid). Reduces new dependencies.
3. **Claude API for language detection + response generation:** Best-in-class multilingual understanding. Can detect language without pre-specifying it.
4. **MVP = daily brief first:** Simpler to ship, immediately valuable, builds trust before the more complex email responder.
5. **Draft mode default for email responder:** Lower risk for the owner — AI drafts, human reviews. Can switch to auto-reply for specific query types once trusted.
6. **Surf vendor data as manual CSV upload (MVP):** Avoid over-engineering the integration until we know how vendors send data. Parse their emails in Phase 2.

### Alternatives Considered

- **Zapier/Make instead of custom Python:** Faster to set up but less flexible for multilingual logic and data normalization. Custom gives WILBA more control and creates a more defensible product.
- **Booking Layer webhook:** Ideal but requires developer access. CSV export is a safe fallback.
- **WhatsApp automation (MVP):** Powerful but complex (WhatsApp Business API approval process). Defer to Phase 2.

### Open Questions (Need Call Answers)

1. Does Booking Layer have a public API? What's the auth method?
2. How do surf vendors send booking data — email, portal, spreadsheet?
3. What languages do most guests speak? (Determines translation priority)
4. Gmail or other email provider? (Determines email trigger method)
5. Is WhatsApp the main guest channel? (Could change MVP scope)
6. What's the owner's preferred reply flow — auto-send or review drafts?
7. Tech budget available per month?

---

## Step-by-Step Tasks

### Step 1: Capture Discovery Notes

After the call, create a discovery notes document with all answers.

**Actions:**
- Create `outputs/baha-baha/` directory
- Create `outputs/baha-baha/discovery-notes.md` with all call answers organized by category
- Note any surprises, constraints, or opportunities not anticipated in this plan

**Files affected:**
- `outputs/baha-baha/discovery-notes.md` (create)

---

### Step 2: Build Unified Booking Data Model

Define the schema for all booking data — this is the foundation everything else is built on.

**Actions:**
- Document all room types, package types, and meal options (from discovery)
- Map Booking Layer field names to the unified data model
- Map surf vendor booking fields to the unified data model
- Create `outputs/baha-baha/booking-data-model.md`

**Files affected:**
- `outputs/baha-baha/booking-data-model.md` (create)

---

### Step 3: Build System Design Document

Translate discovery answers + data model into a full technical architecture.

**Actions:**
- Document the data flow diagram (Booking Layer → Script → Claude → Email)
- Specify API endpoints needed from Booking Layer
- Specify email parsing approach for surf vendors
- Document the daily brief email template (with property-specific room/package names)
- Document email responder logic (language detection → intent classification → response)
- Create `outputs/baha-baha/system-design.md`

**Files affected:**
- `outputs/baha-baha/system-design.md` (create)

---

### Step 4: Create Client Proposal

Translate the system design into a client-facing proposal document.

**Actions:**
- Write executive summary (plain English — what it does, what problem it solves)
- Define Phase 1 scope: Daily Morning Brief
- Define Phase 2 scope: Multi-Language Email Responder
- Define Phase 3 scope: Surf vendor email parsing + WhatsApp (if relevant)
- Set pricing (suggested: $1,500 USD setup + $300–400/month retainer)
- Set timeline (Phase 1: 2 weeks; Phase 2: 2 weeks after)
- Create `outputs/baha-baha/proposal.md`

**Files affected:**
- `outputs/baha-baha/proposal.md` (create)

---

### Step 5: Build Phase 1 — Daily Morning Brief Script

Build the Python script that pulls booking data and sends the daily email.

**Actions:**
- Set up Booking Layer API connection (or CSV parser if no API)
- Build data normalization function (maps raw fields to unified model)
- Build daily brief email template (HTML, branded for Baha Baha)
- Build Claude API call to format/summarize the brief in natural language
- Set up SendGrid delivery to owner + team
- Set up cron job / scheduler (Render, or simple cron)
- Create `scripts/baha_baha_daily_brief.py`
- Create `scripts/requirements-baha-baha.txt`

**Files affected:**
- `scripts/baha_baha_daily_brief.py` (create)
- `scripts/requirements-baha-baha.txt` (create)

---

### Step 6: Build Phase 2 — Multi-Language Email Responder

Build the script that monitors the inbox and responds to guest inquiries.

**Actions:**
- Set up Gmail API connection (OAuth) or email forwarding to webhook
- Build language detection (Claude API — no explicit language list needed)
- Build intent classifier (pricing inquiry / availability / transfer / FAQ / complex booking)
- Build response templates for each intent category (translated dynamically)
- Build draft-mode flow (save to Gmail Drafts for review)
- Build auto-reply flow for FAQs (optional — owner decides)
- Create `scripts/baha_baha_email_responder.py`

**Files affected:**
- `scripts/baha_baha_email_responder.py` (create)

---

### Step 7: Update Workspace Documentation

**Actions:**
- Add Baha Baha project to CLAUDE.md under Active Automations
- Add Baha Baha to `context/current-data.md` as active project
- Update `context/business-info.md` to note Baha Baha as first hospitality WILBA client

**Files affected:**
- `CLAUDE.md`
- `context/current-data.md`
- `context/business-info.md`

---

## Connections & Dependencies

### Files That Reference This Area

- `context/business-info.md` — Baha Baha mentioned as potential case study
- `context/personal-info.md` — Baha Baha Villas listed as Jess's other venture

### Updates Needed for Consistency

- `CLAUDE.md` Active Automations section — add Baha Baha project
- `context/current-data.md` — add to Active Work table once confirmed

### Impact on Existing Workflows

- None — this is a new, independent project
- Reuses existing patterns from `scripts/audit_email_responder.py` (Flask, SendGrid, Claude API)
- Could share `.env` variables (ANTHROPIC_API_KEY, SENDGRID_API_KEY) — add BOOKING_LAYER_API_KEY

---

## Pricing Recommendation

> Use this in the proposal and on the call.

| Phase | Scope | Setup Fee | Monthly Retainer |
|-------|-------|-----------|-----------------|
| Phase 1 | Daily Morning Brief | USD $800 | USD $150/month |
| Phase 2 | Multi-Language Email Responder | USD $1,200 | USD $200/month |
| Full Bundle | Both phases | USD $1,800 | USD $300/month |

**Notes:**
- Tool costs (~$30–50/month) are either included in retainer or passed to client
- If Baha Baha expands to other properties or refers other resorts, that's a case study + referral arrangement
- This becomes a productized "Hospitality AI Receptionist" template WILBA can resell to surf resorts, retreat centers, and boutique properties globally

---

## Validation Checklist

- [ ] Discovery call notes captured in `outputs/baha-baha/discovery-notes.md`
- [ ] Booking Layer API access confirmed (or fallback CSV approach documented)
- [ ] Email platform confirmed (Gmail assumed)
- [ ] Guest languages confirmed and response templates planned
- [ ] Room types and packages fully documented in data model
- [ ] Proposal sent and reviewed with owner
- [ ] Phase 1 script tested end-to-end with real booking data
- [ ] Daily brief email received correctly by owner and team
- [ ] Language detection tested with sample guest emails in 3+ languages
- [ ] CLAUDE.md updated with Baha Baha project
- [ ] current-data.md updated with Baha Baha as active client

---

## Success Criteria

The implementation is complete when:

1. Owner wakes up every morning to a clean, accurate daily ops brief in their inbox — zero manual prep required
2. Guest emails in any language receive a contextually accurate, friendly reply (drafted or auto-sent) within minutes
3. Surf vendor bookings are captured in the same briefing as Booking Layer reservations
4. System runs unattended — owner's only job is to review drafts (or just check that auto-replies are sent)

---

## Notes

**Strategic angle — the sales pitch for the call:**
> "You're running a world-class surf and yoga property in one of the most remote and beautiful places on earth. The last thing you should be doing is manually checking booking systems and typing emails in three languages before sunrise. We build you a system that does all of that. You and your team wake up with everything you need — who's arriving, who's leaving, what transfers are booked, what packages are active. And guests get a reply in their language within minutes of asking. This is your AI front desk."

**Upsell opportunities:**
- WhatsApp automation (biggest channel for hospitality in Southeast Asia)
- Booking.com / Airbnb review response AI
- Automated post-stay follow-up email (reviews, rebooking offer)
- Revenue management: AI monitors competitor pricing and suggests rate adjustments
- Content pipeline: pull surf conditions data and auto-post to Instagram

**WILBA case study potential:**
This is a high-visibility niche — surf resort + AI receptionist + multilingual. Once live, package it as a case study and pitch to:
- Other surf resorts in Sumbawa, Bali, G-Land, Mentawais
- Yoga retreat centers globally
- Boutique eco-lodges and glamping operators

**Booking Layer API:**
Booking Layer (bookinglayer.com) is a modern cloud PMS built for activity and accommodation operators. They have a REST API. Likely requires an API key from their account settings. Documentation at their developer portal. This is a favorable starting point — much easier than legacy hotel PMS systems.

---

## Implementation Notes

**Implemented:** 2026-03-23

### Summary

- Created `outputs/baha-baha/` directory with discovery notes, booking data model, system design, and client proposal
- Built `scripts/baha_baha_daily_brief.py` — full Phase 1 daily morning brief script (Booking Layer API + World Surfaris + Claude + SendGrid)
- Built `scripts/baha_baha_email_responder.py` — full Phase 2 multi-language email responder (Gmail API + Claude intent detection + draft creation)
- Created `scripts/requirements-baha-baha.txt` — all Python dependencies
- Updated `CLAUDE.md` with Baha Baha project under Active Automations and Context Summary
- Updated `context/current-data.md` — added Baha Baha to Active Work table
- Updated `context/business-info.md` — updated Baha Baha description to reflect active client status

### Deviations from Plan

- Fireflies.ai meeting link was behind authentication (could not be accessed) — implemented using tech stack info provided directly by Jess instead
- Scripts built in Phase 1 (plan said Phase 2 for scripts) — built all scripts now while context is fresh, ready to deploy once API keys received

### Issues Encountered

- Fireflies link inaccessible without login — worked from Jess's typed notes instead
- Room types and package names not yet confirmed — placeholders used in data model with clear ⚠️ flags

### Next Actions Required Before Deployment

1. **Sean to provide:** Booking Layer API key
2. **Sean to provide:** One World Surfaris booking confirmation email (to design parser)
3. **Sean to confirm:** Exact room names and package names as they appear in Booking Layer
4. **Sean to confirm:** Recipient email addresses for daily brief + preferred send time
5. **Setup required:** Gmail OAuth (one-time 5-minute process with Sean)
6. **Jess to send:** Proposal (`outputs/baha-baha/proposal.md`) to Sean
