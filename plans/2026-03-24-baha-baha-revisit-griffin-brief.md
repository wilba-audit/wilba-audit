# Plan: Baha Baha Villas — Project Revisit & Developer Brief for Griffin

**Created:** 2026-03-24
**Status:** In Progress
**Request:** Revisit Baha Baha Villas project status, pull Fireflies meeting summary, and send a project brief to developer Griffin to pick up the build.

---

## Overview

### What This Plan Accomplishes

Review the current state of the Baha Baha Villas AI Receptionist & Daily Ops Brief project, compile everything Griffin needs to understand the scope and start building, and send a clear developer handoff brief. Once the Fireflies meeting summary is available from Jess, fold it into the brief for additional context.

### Why This Matters

Scripts are built and sitting ready. The only things blocking deployment are information and access items from Sean (Booking Layer API key, room names, World Surfaris email sample, Gmail OAuth). Griffin needs a clear picture of the architecture, what's already built, and what still needs doing to move this forward as soon as Sean provides credentials.

---

## Current Project Status

### What's Done

| Item | Status |
|------|--------|
| Discovery call with Sean | Done (2026-03-23) |
| Discovery notes | Written — `outputs/baha-baha/discovery-notes.md` |
| Booking data model | Written — `outputs/baha-baha/booking-data-model.md` |
| System design document | Written — `outputs/baha-baha/system-design.md` |
| Client proposal | Written — `outputs/baha-baha/proposal.md` |
| Phase 1 script: Daily Brief | Built — `scripts/baha_baha_daily_brief.py` |
| Phase 2 script: Email Responder | Built — `scripts/baha_baha_email_responder.py` |
| Python dependencies | Written — `scripts/requirements-baha-baha.txt` |
| Fireflies meeting link | Saved in discovery notes — behind auth wall |

### What's Blocking

All blockers are on Sean's side — nothing for Griffin to wait on except these items arriving:

1. **Booking Layer API key** — Sean needs to go to account settings → API → Generate key
2. **World Surfaris sample booking email** — one forwarded confirmation email so Griffin can design the parser
3. **Exact room/villa names** — as they appear in Booking Layer (placeholders currently in data model)
4. **Exact package names** — accommodation only, surf included, meals, combos (as in Booking Layer)
5. **Gmail OAuth setup** — one-time 5-minute process; Jess walks Sean through it on a call
6. **Recipient list for daily brief** — who gets the email (names + addresses)
7. **Preferred delivery time** — what time WITA should the brief land in their inbox?

---

## Step-by-Step Tasks

### Step 1: Draft Griffin Brief ✅ (this document)

Write a clean, structured developer brief that gives Griffin full context on the project — what it does, what's built, what needs doing, and what to wait for.

**Output:** `outputs/baha-baha/griffin-brief.md`

---

### Step 2: Fold in Fireflies Summary (Pending Jess)

The Fireflies meeting recording from the Sean discovery call is at:
`https://app.fireflies.ai/view/Jess-Sean-AI-setup::01KMCH6K2GHZNAK5YAJ4AVJK35`

This URL requires a Fireflies login — Claude cannot access it directly.

**Action for Jess:** Open Fireflies, find the "Jess-Sean AI setup" meeting, copy the summary/transcript section, and paste it back here. Claude will fold it into the Griffin brief and update the discovery notes if anything new comes up.

---

### Step 3: Send Brief to Griffin

Once the brief is drafted (and optionally the Fireflies summary is added), Jess sends it to Griffin via email or Slack. The brief should give Griffin everything he needs to:
- Understand the full system architecture
- Review and test the existing scripts
- Know exactly what info is needed from Sean before deployment
- Start Render deployment config when ready

---

## Connections & Dependencies

- `scripts/baha_baha_daily_brief.py` — Phase 1 script (ready, needs Booking Layer API key to test)
- `scripts/baha_baha_email_responder.py` — Phase 2 script (ready, needs Gmail OAuth to test)
- `outputs/baha-baha/system-design.md` — Full architecture doc for Griffin's reference
- `outputs/baha-baha/booking-data-model.md` — Data schema with placeholder room/package names
- `outputs/baha-baha/proposal.md` — Client-facing proposal (pricing, scope, timeline)

---

## Notes

- Fireflies link is behind auth — Jess needs to manually export/copy the summary
- All scripts follow the same pattern as `scripts/audit_email_responder.py` — Griffin already knows this codebase
- Render deployment config (Procfile, render.yaml) already exists for the audit pipeline — same approach applies here
- Priority: get this live ASAP. Sean said yes in principle. The deal is $1,800 setup + $300/month retainer.
