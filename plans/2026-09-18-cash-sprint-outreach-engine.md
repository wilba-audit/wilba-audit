# Plan: The 14-Day Cash Sprint — A Bulletproof Discovery-Call Engine

**Created:** 2026-09-18
**Status:** Draft
**Request:** A clear, bulletproof outreach plan to get clients and book as many discovery calls as possible — money is urgent.

---

## Overview

### What This Plan Accomplishes

Builds a single, dead-simple daily outreach engine whose only goal is **booked discovery calls in the next 14 days**. It locks one offer, three target lanes (warm network first), a ready-to-send message bank, a booking mechanism, and a discovery-call script — all driven by one command (`/sprint`) so Jess's daily job shrinks to "send the batch, log the replies, take the calls."

### Why This Matters

Jess needs cash urgently and the pipeline is at **0 booked calls**. Everything strategic is already decided; the missing thing is *volume of conversations*. This plan removes every point of friction and hesitation between Jess and a booked call, and gives her a number to hit every day. Discovery calls are the leading indicator of revenue — this engine manufactures them on purpose.

---

## Current State

### Relevant Existing Structure

- `.claude/commands/outreach.md` — `/outreach`, writes 10–12 daily messages (hospitality-angled).
- `.claude/commands/pipeline.md` + `outputs/wilba-pipeline.md` — the deal board (currently empty).
- `.claude/commands/mentor.md` — Monday `/mentor` sets 3 weekly targets.
- `.claude/agents/outreach-writer.md` — writes messages in Jess's voice, per segment.
- `outputs/wilba-outreach-sop.md` — the current daily routine (10 touches, hospitality, audit-led).
- `outputs/wilba-prospect-list.md`, `outputs/wilba-bali-prospects.md`, `outputs/outreach-batch-1.md` — existing lists/first batch (hospitality/Bali).
- `outputs/wilba-outreach-pack.md`, `outputs/wilba-10k-60day-sprint.md`, `outputs/wilba-money-first-plan.md` — prior positioning + sprint thinking.
- `outputs/competitor-daniel-odoi.md` — the "sell the map, not the build" messaging angle.
- `.claude/skills/marketing-comms-counsel/` — compliance skill (matters for AU Spam Act + any health-clinic niche).

### Gaps or Problems Being Addressed

1. **No warm lane.** Existing outreach is hospitality-cold. The fastest calls come from people who already know Jess — there's no system for that.
2. **Daily number is too low for urgency.** 10 touches/day won't move fast enough when money is urgent.
3. **Offer isn't locked as a risk-reversal.** No single, repeatable Grand Slam offer + booking CTA + price. Hesitation kills sends.
4. **No booking mechanism named.** "Book a call" with no link = friction and lost momentum.
5. **No discovery-call script.** Calls get booked then fumbled; no Ottley/Hormozi structure.
6. **Tracking is deal-stage, not activity-based.** For a sprint, Jess needs a daily *activity* scoreboard (touches → replies → calls booked), because activity is the only thing she controls.
7. **Scatter risk.** Jess has said repeatedly she gets overwhelmed and has "too many pies." The system must reduce to ONE daily ritual.

---

## Proposed Changes

### Summary of Changes

- Create a self-contained **`outputs/cash-sprint/`** folder = the sprint command center.
- Lock **one Grand Slam offer** with a risk-reversal, a price, and a single qualifying question.
- Define **three target lanes**, warm-first, with sourcing instructions and qualifying criteria.
- Build a **message bank**: first-touch + 3 follow-ups + objection handling, per lane, per channel (DM/email).
- Write a **discovery-call script** (Ottley: sell the meeting/audit not the build; Hormozi: price then pause).
- Create an **activity scoreboard** (daily touches/replies/calls) and align `wilba-pipeline.md`.
- Add a **`/sprint` command** that runs the whole day in one shot (targets → written messages → follow-ups due → booking-ready → log).
- Produce a **Day-1 ready-to-send batch** so Jess starts today.
- Update `CLAUDE.md` to document the sprint + command.

### New Files to Create

| File Path | Purpose |
| --- | --- |
| `outputs/cash-sprint/README.md` | The one-page command center: the number, the offer, the lanes, the booking link, the daily ritual, the weekly rhythm. |
| `outputs/cash-sprint/offer.md` | The single Grand Slam offer — positioning, risk reversal, setup fee + model, the qualifying question, what's promised vs delivered by Griffin. |
| `outputs/cash-sprint/target-lanes.md` | The 3 lanes (Warm Network, Primary Cold Niche, Hospitality warm-secondary) with how to source names, qualifying criteria, and where to find them. |
| `outputs/cash-sprint/message-bank.md` | Ready-to-send copy: first touch + follow-ups #2/#3/#4 + objection responses, per lane, per channel — all in Jess's voice, AU Spam-Act compliant. |
| `outputs/cash-sprint/discovery-call-script.md` | The 15-minute discovery-call framework: open, discovery questions, outcome framing, price + 8-second pause, next step. |
| `outputs/cash-sprint/scoreboard.md` | Daily activity tracker (date · touches · replies · calls booked · calls held · closes · cash) with a running 14-day total and targets. |
| `outputs/cash-sprint/day-1-batch.md` | A first, fully-written send list Jess can fire today (warm names + 1 cold-niche batch), so momentum starts immediately. |
| `.claude/commands/sprint.md` | `/sprint` — the daily driver that orchestrates targets + messages + follow-ups + booking readiness + logging in one command. |

### Files to Modify

| File Path | Changes |
| --- | --- |
| `outputs/wilba-pipeline.md` | Add a top-of-file **Sprint scoreboard** (14-day activity totals + this-week target) and ensure stages map cleanly to: Outreach sent → Follow-up → Reply → **Call booked** → Call held → Proposal → Won. Make "Call booked" the headline metric. |
| `.claude/commands/outreach.md` | Point it at the new `cash-sprint/message-bank.md` + `target-lanes.md`; raise the sprint-mode daily number; keep it as the "just write today's messages" command (a lighter subset of `/sprint`). |
| `outputs/wilba-outreach-sop.md` | Add a banner at top: "During the Cash Sprint, follow `outputs/cash-sprint/README.md` and run `/sprint`. This SOP is the steady-state version." (Keep it; don't delete.) |
| `CLAUDE.md` | Add a **Cash Sprint (Active)** subsection under the sales engine area documenting the folder, the `/sprint` command, the offer, the daily number, and the booking link. |

### Files to Delete (if any)

None. Everything is additive or superseded-by-reference to preserve history.

---

## Design Decisions

### Key Decisions Made

1. **Warm-first, then one cold niche.** Warm contacts convert to calls fastest with zero cold-start friction (Hormozi's warm-reach-out lane; Ottley's "start warm"). The engine always runs the warm lane, then adds ONE cold niche — not five. This is the antidote to Jess's "too many pies."
2. **Recommended primary cold niche = med spa / cosmetic clinics (AU).** Per Griffin's briefing: it runs on the *proven* AI receptionist/booking + follow-up asset, has a Grand Slam risk-reversal ("pay from what comes back"), produces the missing case study, and is adjacent to the health-clinic compliance world Jess already knows from Schoeman. (Configurable — see Open Questions.)
3. **One offer, one CTA, one link.** Every message ends with the same ask: a short call / free audit, booked via one link. Fewer decisions = more sends = more calls.
4. **Sell the call, not the build (Ottley).** The offer on outreach is the *audit/conversation*, never the system. Removes price friction and dramatically lifts booking rate.
5. **Risk reversal for the close, setup fee for the cash (Hormozi).** "We work a slice of your list / answer your enquiries — you pay from results" makes the yes easy; a modest setup fee brings cash in now instead of waiting on rev-share.
6. **Activity scoreboard, not just a deal board.** In a sprint, Jess controls *touches*, not outcomes. Tracking daily activity keeps her focused on the one input that guarantees results, and protects her from the emotional whiplash of an empty deal board.
7. **One command runs the day.** `/sprint` collapses the routine to a single action to fight overwhelm; `/outreach` remains the lighter "just give me today's messages" option.
8. **AU Spam-Act compliant by design.** Inferred-consent only, functioning unsubscribe on email, opt-outs actioned in 5 business days, no health testimonials — baked into the message bank via the `marketing-comms-counsel` skill.

### Alternatives Considered

- **Cold-only, high-volume scraped lists.** Rejected as the *primary* lane: slower to first call, higher spam risk under the AU Spam Act, and demoralising at zero reputation. Kept as a secondary lane once warm is exhausted.
- **Content/inbound as the engine.** Rejected for *urgent* cash — content compounds slowly. It stays the 20% supporting play, not the sprint engine.
- **Running three niches at once (med spa + hospitality + pest).** Rejected — directly causes the scatter Jess flagged. One cold niche at a time.
- **Upgrading `/outreach` instead of a new `/sprint`.** Rejected as insufficient — the sprint needs targets + follow-ups + booking + logging in one pass; `/outreach` stays as the lighter subset.

### Open Questions (need Jess's input at/ before implementation)

1. **Primary cold niche?** Recommend **med spa / cosmetic clinics (AU)**. Alternatives: hospitality (existing lists), local service businesses, pest control. *(Warm lane runs regardless.)*
2. **Offer price + model?** Proposed default: **modest setup fee (e.g. AUD $1,000–1,500) + rev-share on recovered revenue for 90 days → flat monthly retainer**, OR for fresh-enquiry receptionist a **monthly subscription (e.g. AUD $500–1,000/mo) + setup**. Need Jess to approve the numbers (one number, same for everyone).
3. **Booking link?** Does Jess have a Calendly / Cal.com? The CTA needs one live link. If not, Step 1 sets one up.
4. **Daily touch target?** Recommend **20/day** (≈ 12 warm + 8 cold) given urgency + her 4 hrs/day. Confirm.
5. **What can be delivered in 14 days?** Discovery calls can be booked now; the med-spa/receptionist build is Griffin's (6–8 wks, pro-bono first client). Confirm the near-term sellable: audit + setup fee now, build follows — so outreach promises are honest.

---

## Step-by-Step Tasks

### Step 1: Lock the offer and the booking link

Create `outputs/cash-sprint/offer.md`.

**Actions:**
- Write the single Grand Slam offer: the outcome promised, the risk reversal, the setup fee + model, and the one qualifying question ("Do you bill any insurance/Medicare electronically?" for med spa; adapt per chosen niche).
- State plainly what's delivered now vs by Griffin's build (honesty in the pitch).
- Insert the booking link placeholder `[[BOOKING_LINK]]` and note in README that every message uses it. If Jess has no link, add a 3-line "set up Cal.com in 5 minutes" instruction.
- Run content past the `marketing-comms-counsel` skill for AU compliance (no health testimonials, Spam-Act consent).

**Files affected:** `outputs/cash-sprint/offer.md`

---

### Step 2: Define the target lanes

Create `outputs/cash-sprint/target-lanes.md`.

**Actions:**
- **Lane A — Warm Network (always on):** past clients/colleagues, IHF contacts, Danielle's network, anyone who knows Jess, adjacent-industry acquaintances. Sourcing: phone contacts, Instagram followers/following, LinkedIn, email history. Criterion: knows her name.
- **Lane B — Primary Cold Niche (the chosen one):** med spa / cosmetic clinics AU by default. Sourcing per briefing: Google Maps by metro (Sydney/Melbourne/Brisbane/Gold Coast/Perth), Instagram (injector = the brand), practice-mgmt directories (Pabau/Fresha/Zenoti). Qualifying: cash-pay, injectables-led, owner-operated, 300+ dormant patients, well-reviewed; exclude derm/plastic/chains/brand-new.
- **Lane C — Hospitality (warm-secondary):** the existing `wilba-prospect-list.md` + `wilba-bali-prospects.md`, dipped into when warm runs thin.
- For each lane: how many to add per day, and a mini "spot the leak" note for personalisation.

**Files affected:** `outputs/cash-sprint/target-lanes.md`

---

### Step 3: Build the message bank

Create `outputs/cash-sprint/message-bank.md`.

**Actions:**
- For each lane × channel (DM + email): **first touch**, **follow-up #2 (2–3 days)**, **follow-up #3 (day 6)**, **follow-up #4 / break-up (day 10)**.
- Warm-lane opener leads with the relationship + a specific, generous ask for a quick chat.
- Cold-niche opener leads with *their* leak/opportunity, uses the "sell the map, not the build" framing from `competitor-daniel-odoi.md`, ends with the audit/call CTA + `[[BOOKING_LINK]]`.
- Add an **objection bank**: "how much?", "I already have someone", "not now", "send me info" — each with a one-line response that steers to the call.
- All copy in Jess's voice (no em-dashes, no "unlock/dive in"), AU Spam-Act compliant (unsubscribe line on emails, inferred-consent framing).

**Files affected:** `outputs/cash-sprint/message-bank.md`

---

### Step 4: Write the discovery-call script

Create `outputs/cash-sprint/discovery-call-script.md`.

**Actions:**
- Structure: warm open → permission → 4–5 discovery questions (their bookings/enquiries, busiest times, what's slipping, what a recovered customer is worth, who follows up today) → reflect the leak back in dollars → the offer + price → **8-second silence** → book the next step (build/audit start).
- Include the "don't sell the build, sell the audit/outcome" rule and a one-line pre-call checklist.
- Add a 2-line post-call routine: log outcome in scoreboard + send the recap/proposal.

**Files affected:** `outputs/cash-sprint/discovery-call-script.md`

---

### Step 5: Create the activity scoreboard + align the pipeline

Create `outputs/cash-sprint/scoreboard.md`; modify `outputs/wilba-pipeline.md`.

**Actions:**
- Scoreboard table: one row per day — `Date · Touches · Replies · Calls booked · Calls held · Closes · Cash` — plus a 14-day running total and the targets (e.g., 20 touches/day, 2+ calls booked/week).
- Add the same summary block to the top of `wilba-pipeline.md`, and make **"Call booked"** the headline metric. Confirm stages: Outreach sent → Follow-up → Reply → Call booked → Call held → Proposal → Won.

**Files affected:** `outputs/cash-sprint/scoreboard.md`, `outputs/wilba-pipeline.md`

---

### Step 6: Write the command center README

Create `outputs/cash-sprint/README.md`.

**Actions:**
- One page: **the number** (calls booked target), the offer one-liner, the 3 lanes, the booking link, the daily ritual (run `/sprint` → send → log → take calls), the weekly rhythm (Mon `/mentor`, daily `/sprint`, Fri `/pipeline`), and a 3-line motivation truth for hard days.
- Link out to offer / lanes / message-bank / call-script / scoreboard.

**Files affected:** `outputs/cash-sprint/README.md`

---

### Step 7: Build the `/sprint` command

Create `.claude/commands/sprint.md`.

**Actions:**
- Instructions: (1) read `scoreboard.md` + `wilba-pipeline.md` for follow-ups due; (2) pick today's targets across lanes (warm-first) per `target-lanes.md`; (3) launch `outreach-writer` to write every message from `message-bank.md` patterns; (4) output a single send list marked first-touch vs follow-up, each with the booking link; (5) surface any calls booked and prep the call script; (6) log all sends to the scoreboard + pipeline; (7) end with today's number and one nudge.
- Keep it 15-minutes-to-send fast.
- Update `.claude/commands/outreach.md` to reference the new bank/lanes and note `/sprint` as the full-day driver.

**Files affected:** `.claude/commands/sprint.md`, `.claude/commands/outreach.md`

---

### Step 8: Produce the Day-1 batch

Create `outputs/cash-sprint/day-1-batch.md`.

**Actions:**
- Write a ready-to-send first batch: a warm-lane set (with placeholders for Jess to drop in 8–10 real names) + one fully-written cold-niche set of 5.
- Each message copy-paste ready with the booking link, marked by channel.
- One line: "Send these today, log them, come back with any replies."

**Files affected:** `outputs/cash-sprint/day-1-batch.md`

---

### Step 9: Update CLAUDE.md + validate

Modify `CLAUDE.md`; run validation.

**Actions:**
- Add a **Cash Sprint (Active)** subsection: folder location, `/sprint` command, the offer, the daily number, the booking link, and the "warm-first, one cold niche" rule.
- Add banner to `wilba-outreach-sop.md` pointing to the sprint during the sprint.
- Validate against the checklist below.

**Files affected:** `CLAUDE.md`, `outputs/wilba-outreach-sop.md`

---

## Connections & Dependencies

### Files That Reference This Area

- `.claude/commands/outreach.md`, `pipeline.md`, `mentor.md`, `daily.md` — all touch the outreach loop.
- `.claude/agents/outreach-writer.md` — the engine that writes the messages.
- `outputs/wilba-pipeline.md`, `wilba-outreach-sop.md` — the current tracking + routine.
- `outputs/brand/brand-positioning.md` — voice source for the message bank.

### Updates Needed for Consistency

- `CLAUDE.md` sales-engine section must list `/sprint` and the cash-sprint folder.
- `wilba-outreach-sop.md` gets the "during the sprint, use this" banner.
- `/outreach` and `/pipeline` must read/write the same stages the scoreboard uses.

### Impact on Existing Workflows

- The daily ritual becomes `/sprint` (with `/outreach` as a lighter subset). Monday `/mentor` and Friday `/pipeline` unchanged. The hospitality SOP is preserved as steady-state and referenced, not replaced.

---

## Validation Checklist

- [ ] `outputs/cash-sprint/` exists with all 7 content files + is internally cross-linked.
- [ ] `offer.md` states one offer, one price/model, one qualifying question, and the booking link.
- [ ] `message-bank.md` has first-touch + 3 follow-ups + objections for each lane × channel, in Jess's voice, AU-compliant (unsubscribe + inferred-consent).
- [ ] `discovery-call-script.md` includes the price-then-pause and "sell the call not the build" rules.
- [ ] `scoreboard.md` and `wilba-pipeline.md` share the same stages, with "Call booked" as the headline metric.
- [ ] `/sprint` runs end-to-end: targets → written messages → follow-ups → booking-ready → logged, in ~15 min.
- [ ] `day-1-batch.md` is genuinely ready to send today.
- [ ] `CLAUDE.md` documents the sprint + `/sprint`.
- [ ] All five Open Questions answered (niche, price, booking link, daily number, near-term deliverable).

---

## Success Criteria

1. Jess can run **one command** each morning and have a full day of personalised, ready-to-send outreach in under 15 minutes.
2. Every message ends with the **same booking CTA + link** — zero decisions to make before sending.
3. The system tracks **calls booked** as its headline number, updated daily.
4. Within 14 days of running it daily, the pipeline shows **booked discovery calls** (target: 2+/week, i.e. 4+ in the sprint) — breaking the zero.
5. The whole thing reduces to **one daily ritual**, with no scatter across niches.

---

## Notes

- **Deliverability honesty:** the med-spa/receptionist build is Griffin's and takes weeks; outreach sells the *call/audit* and a setup fee now, with the build following (pro-bono first client for the case study). Keep promises honest.
- **Compliance is a feature, not a tax:** in AU health niches, compliant-by-design is a genuine differentiator — lean on it in the pitch, but get legal sign-off on templates before any campaign.
- **Future extension:** once calls are flowing, add the 20% content-support layer (already built in the Content Engine) and, later, the Skool/community flywheel — but not during the sprint.
- **If warm converts fast:** it's fine to run warm-only for the first few days and add the cold niche once the warm list is worked — warm-first is the point.
