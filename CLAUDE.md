# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

---

## What This Is

This is **Jess Morrell's AIOS workspace** — built to launch and run WILBA (wilba.ai), an AI automation and content agency. The workspace is a layer of AI automation wrapped around the business, powered by plug-and-play modules installed one at a time.

**This file (CLAUDE.md) is the foundation.** It is automatically loaded at the start of every session. Keep it current — it is the single source of truth for how Claude should understand and operate within this workspace.

> From the AAA Accelerator — the #1 AI business launch & AIOS program. [aaaaccelerator.com](https://aaaaccelerator.com)

---

## The Claude-User Relationship

Claude operates as an **agent assistant** with access to the workspace folders, context files, commands, and outputs. The relationship is:

- **User**: Jess Morrell — founder of WILBA, entrepreneur, strategist, and content creator based on the Surf Coast, Victoria, Australia. Non-technical. Prefers voice-first, big-picture thinking. Directs work through commands and plain English.
- **Claude**: Reads context, understands Jess's objectives, executes commands, produces outputs, and maintains workspace consistency.

Claude should always orient itself through `/prime` at session start, then act with full awareness of who Jess is, what she's building, and how this workspace supports that.

---

## AIOS Mission

You are helping a business owner build an **AI Operating System (AIOS)** — an autonomous intelligence layer wrapped around their entire business. Everything in this workspace serves that goal.

### The Problem: The Operator Trap
Most business owners are stuck working IN their business — firefighting, admin, managing people, checking dashboards, sitting in meetings just to stay informed. 80% of bandwidth goes to "must-dos." Nothing left for growth, strategy, or the life they actually wanted. The old model says hire more people, buy more tools, work more hours. AIOS says the answer is less — less manual work, less people needed, less time in operations. More bandwidth for the work that matters.

### The Solution: Five Layers
The AIOS gives it back — one layer at a time:
1. **Context** — Your AI understands the business (strategy, team, processes, history)
2. **Data** — Your AI sees the numbers in real-time (collectors pull from your actual data sources daily)
3. **Intelligence** — Your AI watches everything (meetings, messages, signals) and synthesizes into a daily brief
4. **Automate** — Audit every task, score each one, automate them away one by one. Each task automated = bandwidth recovered.
5. **Build** — Freed bandwidth applied to growth, new initiatives, or life. Work ON the business, not IN it.

### Five Principles
1. **Just Ask** — If you can describe it in plain English, Claude can build it. Don't self-censor. Ask for the impossible.
2. **Talk, Don't Type** — Voice-first. Hold FN, speak for 60 seconds, let Claude format it. 3x faster than typing.
3. **Layers, Not Leaps** — One layer at a time. Each independently valuable. Through gradual exposure, you become technical without even trying.
4. **Build for Scale & Security** — Human-in-the-loop by default. Your data stays local. Plan before you build.
5. **Borrow Before You Build** — 80% modules, 20% custom. Check the library before building from scratch.

### Three KPIs
These are how you know your AIOS is working:
- **Away-From-Desk Autonomy** — Hours per day you can step away and nothing falls apart. Target: business runs while you sleep.
- **Task Automation %** — Percentage of recurring tasks automated. Use the Task Audit (`context/task-audit.md`) as your scoreboard.
- **Revenue Per Employee** — Total revenue ÷ team members. Not bigger companies — leaner, faster, more profitable ones.

### How You Should Help
- Be patient. Assume the user is non-technical unless told otherwise.
- Explain what you're doing in plain English BEFORE doing it.
- Celebrate wins — every module installed, every task automated is real progress toward freedom.
- When suggesting solutions, check existing modules and the community first (Borrow Before You Build).
- Keep the three KPIs in mind — every automation should move at least one KPI.
- Never dump error logs or technical jargon. Find the problem, explain it simply, fix it.

---

## Workspace Structure

```
.
├── CLAUDE.md                # This file — core context, always loaded
├── .env                     # API keys and credentials (gitignored, never commit)
├── .claude/
│   └── commands/            # Slash commands Claude can execute
│       ├── prime.md         # /prime — session initialization
│       ├── install.md       # /install — install an AIOS module
│       ├── create-plan.md   # /create-plan — create implementation plans
│       ├── implement.md     # /implement — execute plans
│       └── share.md         # /share — package systems for sharing
├── context/                 # Background context about the user and business
│   ├── business-info.md     # What the business does
│   ├── personal-info.md     # Who you are, your role
│   ├── strategy.md          # Current priorities and goals
│   ├── current-data.md      # Key metrics and current state
│   └── import/              # Drop documents here for Claude to analyze
├── module-installs/         # AIOS modules — drop module folders here, install with /install
├── plans/                   # Implementation plans created by /create-plan
├── outputs/                 # Work products and deliverables
├── reference/               # Templates, examples, reusable patterns
├── scripts/                 # Automation scripts (added by modules)
└── shares/                  # Packaged systems for sharing (created by /share)
```

**Key directories:**

| Directory          | Purpose                                                                                |
| ------------------ | -------------------------------------------------------------------------------------- |
| `context/`         | Who you are, your business, current priorities, strategies. Read by `/prime`.           |
| `context/import/`  | Drop any docs here (business plans, ChatGPT exports, etc.) for Claude to analyze.      |
| `module-installs/` | AIOS modules go here. Install them with `/install module-installs/{module-name}`.      |
| `plans/`           | Detailed implementation plans. Created by `/create-plan`, executed by `/implement`.    |
| `outputs/`         | Deliverables, analyses, reports, and work products.                                    |
| `outputs/audit/`   | AI Receptionist Audit lead log and setup checklist.                                    |
| `reference/`       | Helpful docs, templates and patterns to assist in various workflows.                   |
| `scripts/`         | Automation scripts — added by modules as you install them.                             |
| `shares/`          | Packaged systems for sharing. Created by `/share`, ready to hand off.                  |

---

## Active Automations

### AI Receptionist Audit (Lead Generation)

An automated lead generation pipeline for WILBA's AI Receptionist service:

1. Prospect fills out the 18-question "Free AI Audit" form on wilba.ai
2. Wix Automation sends form data to the webhook (`/audit-webhook`)
3. Claude analyses the answers, calculates revenue loss, writes a personalised email
4. Resend delivers the email to the prospect's inbox
5. Lead is logged to `outputs/audit/leads.csv`

**Files:**
- `scripts/audit_email_responder.py` — Flask webhook server (the brain)
- `scripts/requirements-audit.txt` — Python dependencies
- `reference/ai-receptionist-audit-setup.md` — Full setup guide
- `outputs/audit/MORNING-CHECKLIST.md` — Quick-start deployment checklist
- `Procfile` + `render.yaml` + `runtime.txt` — Render deployment config

**Status:** Pipeline complete. WeasyPrint PDF with branded AI use cases report enabled. Deployed on Render at https://wilba-audit.onrender.com. Needs: Wix form added to Free AI Audit page + Wix Automation activated (webhook URL: https://wilba-audit.onrender.com/audit-webhook) + end-to-end test.

---

### Baha Baha Villas — AI Receptionist & Daily Ops Brief (Client Project)

WILBA's first hospitality client. Two automations for Sean's surf/accommodation property in West Sumbawa, Indonesia:

**Phase 1 — Daily Morning Brief:**
1. Pulls all bookings from Booking Layer API (PMS) + World Surfaris (manual sheet)
2. Normalises data across OTA sources via Channex channel manager
3. Claude formats a readable ops brief (check-ins, check-outs, transfers, in-house, upcoming)
4. Sends to owner + team Gmail inboxes at 6am WITA every morning

**Phase 2 — Multi-Language Email Responder:**
1. Monitors bookings Gmail inbox every 15 minutes
2. Claude detects language and classifies intent (availability, pricing, FAQ, booking request, etc.)
3. Drafts a reply in the guest's language (any language — auto-detected)
4. Saves to Gmail Drafts for owner review (or auto-sends for simple FAQs)

**Client tech stack:** Squarespace (website) · Booking Layer (PMS) · Channex (channel manager) · Gmail · World Surfaris (surf vendor) · Mockapos (POS) · Jurnal.co.id (accounting) · Google Drive

**Files:**
- `scripts/baha_baha_daily_brief.py` — Morning brief generator script
- `scripts/baha_baha_email_responder.py` — Multi-language email responder script
- `scripts/requirements-baha-baha.txt` — Python dependencies
- `outputs/baha-baha/discovery-notes.md` — Call notes and tech stack
- `outputs/baha-baha/system-design.md` — Full technical architecture
- `outputs/baha-baha/proposal.md` — Client-facing proposal
- `outputs/baha-baha/booking-data-model.md` — Unified booking schema
- `plans/2026-03-23-baha-baha-ai-receptionist-booking-agent.md` — Implementation plan

**Status:** Scripts built. Proposal ready to send. Needs: Booking Layer API key from Sean + Gmail OAuth setup + World Surfaris sample email + room/package name confirmation. Deploy to Render once API access confirmed.

---

### Monkey Joe's — Growth Operator (Client Pilot: POL + WP)

WILBA's marketing-execution pilot for Michael Carter's two Orlando Monkey Joe's locations —
**Pointe Orlando (POL)** and **Winter Park (WP)** — via William Milner / Lanyu. The stack runs on
**GoHighLevel (GHL / LeadConnector)** as the CRM (one sub-account per location, driven entirely by
contact tags), **Meta Marketing API** for Facebook/Instagram ads, and **Google Ads API** for
reporting (pending dev-token approval). Everything keys off two audiences: `voucher-delivered`
(opted-in) and `unsubscribed` (excluded).

**Live automations (GitHub Actions — creds in repo Secrets, not `.env`):**
- `mj-birthday-drip.yml` (daily) → `scripts/mj_birthday_sequence.py` — 180-day, 10-touchpoint birthday nurture from enrollment date
- `mj-birthday-radar.yml` (weekly) → `scripts/mj_birthday_radar.py` — 90/60/30-day reminders before the child's actual birthday (needs `CHILD_BDAY_FIELD_ID`)
- `mj-weekly-scorecard.yml` (Mon) → `scripts/mj_weekly_scorecard.py` — emails Jess a GHL+ads scorecard via Resend

**Other scripts:**
- `scripts/mj_weekend_bananas_blast.py` — the core GHL helper (fetch_audience / send_message / apply_cohort_tag) + one-off blasts
- `scripts/mj_meta_manage.py` — Meta ads write control (list / pause / enable / budget, $60/day guardrail)
- `scripts/fetch_consolidated_reporting.py` — joins GHL + Meta + Google into `outputs/monkey-joes/reporting/consolidated.json`

**Docs:** `outputs/monkey-joes/`. The dated July docs are current: `ADS-AUDIT-2026-07.md`,
`BIRTHDAY-ACQUISITION-STRATEGY-2026-07.md`, and the rewritten `promo-codes.md` (v2). The other
(March) docs describe the pre-migration Aluvii/Constant Contact plan — GHL is the current reality.

**Real codes (July 2026):** `WELCOME` ($25 opt-in voucher) · `BOGO/` (Wacky Wednesday) · `50% off`
(best Google performer) · `FJP/` (Frequent Jumper, not for parties) · `BDAY25` ($25 off a party,
redeemed in **Aluvii**). The old `WACKY-*`/`COMEBACK` scheme is dead.

**Redemption tracking:** codes are redeemed **in-store on William's external verification page**,
and **party sales via `BDAY25` in Aluvii** (no API) — **NOT via GHL tags by default**. Reporting
redemptions needs an export from William + an Aluvii count until William tags redeemed back to GHL.

**Commands:** `/mj-ghl` · `/mj-redemptions` · `/mj-birthday` · `/mj-ads` · `/mj-report` (see Commands section).

**Status:** Meta ads live (~$1,071 spend, ~298 leads @ ~$3.50); Google live (~$2,950 spend). Ads
audit done. Open items: (1) **birthday scripts hard-code unconfirmed `$234/$194` party prices — fix
or remove**; (2) reconcile our birthday drip with William's GHL-native workflow (double-send risk);
(3) confirm how redemptions export from William/Aluvii; (4) WP has no birthday data yet; (5) this
cloud session's **network policy blocks GHL/Meta/Google APIs** — live pulls run via GitHub Actions
or from CSV exports.

---

## Context Summary

**Business:** WILBA (wilba.ai) — AI automation and content generation agency. Two services: Content Generation Machine (Perplexity → Script → ElevenLabs → HeyGen → CreatorMate) and AI Automation Audits. Developer partner handles technical fulfillment.

**Role:** Jess is founder, face, and sales/strategy lead. Non-technical — she designs systems and directs projects; her US-based developer builds them.

**Current focus:** Close Baha Baha Villas as WILBA's first hospitality client. Get WILBA's first paying client by April 2026. Finalize the Content Generation Machine. Build personal brand on Instagram/YouTube. Wind down IHF role (ends March 2026).

**Key metric to watch:** WILBA monthly revenue — currently $0, needs to replace ~USD $1,500/month from IHF ASAP. Baha Baha deal = $1,800 USD setup + $300/month retainer.

**Active retainer:** Danielle Colley podcast management — AUD $1,500/month, ~2 hrs/day. Temporary bridge income.

**Live prospect:** Sean (Baha Baha Villas, West Sumbawa) — discovery call done 2026-03-23, proposal ready to send.

---

## Commands

### /install [module-path]

**Purpose:** Install an AIOS module into this workspace.

Point it at a module folder in `module-installs/` and Claude walks you through the guided setup. Each module adds a new capability to your AIOS.

Example: `/install module-installs/context-os`

### /prime

**Purpose:** Initialize a new session with full context awareness.

Run this at the start of every session. Claude will:

1. Read CLAUDE.md and context files
2. Summarize understanding of the user, workspace, and goals
3. Confirm readiness to assist

### /create-plan [request]

**Purpose:** Create a detailed implementation plan before making changes.

Use when adding new functionality, commands, scripts, or making structural changes. Produces a thorough plan document in `plans/` that captures context, rationale, and step-by-step tasks.

Example: `/create-plan add a competitor analysis command`

### /implement [plan-path]

**Purpose:** Execute a plan created by /create-plan.

Reads the plan, executes each step in order, validates the work, and updates the plan status.

Example: `/implement plans/2026-01-28-competitor-analysis-command.md`

### /share [system or feature]

**Purpose:** Package a system or feature from your workspace for sharing.

Deep-dives the code first to fully understand it, then produces a self-contained, beginner-friendly package with a Claude-guided installer (INSTALL.md + README.md + scripts). The recipient gives the folder to Claude Code and says "read INSTALL.md and set this up" — Claude walks them through everything step by step. Runs a 6-stage interactive flow: Research → Scope → Frame → Write → Validate → Deliver. Outputs to `shares/`.

Example: `/share the daily brief system`

### Monkey Joe's commands

Four operator commands for the Monkey Joe's pilot. Each runs a repeatable procedure so Jess can
check or operate the account without needing the developer. All follow **dry-run → confirm →
execute** for anything that sends or changes live data.

- **`/mj-ghl`** — GHL account health check & operations (audience counts, tag/custom-field audit, blasts)
- **`/mj-redemptions`** — promo-code redemption tracking & channel attribution (reconciles the code scheme)
- **`/mj-birthday`** — birthday-party funnel status & controls (drip + radar; reconciles the GHL-native workflow)
- **`/mj-ads`** — Google + Facebook ads status, spend, audit, and Meta controls (pause/enable/budget)
- **`/mj-report`** — weekly ops report + monthly on-brand corporate report (codes, redemptions, ads, parties)

---

## Getting Started

**First time?** Start here:

1. Run `/install module-installs/context-os` — this builds your context layer (Claude learns your business)
2. After ContextOS is done, run `/prime` — verify Claude knows you
3. Install more modules from `module-installs/` as you're ready

**Returning?** Run `/prime` at the start of every session.

---

## Critical Instruction: Maintain This File

**Whenever Claude makes changes to the workspace, Claude MUST consider whether CLAUDE.md needs updating.**

After any change — adding commands, scripts, workflows, or modifying structure — ask:

1. Does this change add new functionality users need to know about?
2. Does it modify the workspace structure documented above?
3. Should a new command be listed?
4. Does context/ need new files to capture this?

If yes to any, update the relevant sections. This file must always reflect the current state of the workspace so future sessions have accurate context.

---

## Session Workflow

1. **Start**: Run `/prime` to load context
2. **Work**: Use commands or direct Claude with tasks
3. **Install modules**: Use `/install` to add new AIOS capabilities
4. **Plan changes**: Use `/create-plan` before significant additions
5. **Execute**: Use `/implement` to execute plans
6. **Share**: Use `/share` to package systems for team, clients, or community
7. **Maintain**: Claude updates CLAUDE.md and context/ as the workspace evolves

---

## Notes

- Keep context minimal but sufficient — avoid bloat
- Plans live in `plans/` with dated filenames for history
- Outputs are organized by type/purpose in `outputs/`
- Reference materials go in `reference/` for reuse
- API keys go in `.env` — never commit this file
