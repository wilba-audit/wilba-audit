# Plan: The Weekend Content Sprint — 30 Posts Produced & Scheduled

**Created:** 2026-09-18
**Status:** Implemented
**Request:** Spend the weekend batch-producing ~30 Instagram posts (scripts + assets), using Artlist to automate as much as possible, with minimal filming — and decide whether a dedicated social command is needed.

---

## Overview

### What This Plan Accomplishes

Turns a weekend into **30 finished, scheduled posts** by batch-producing them from the scripts that already exist, with a format mix that needs Jess on camera only **once** (one 6–8 clip filming session). Artlist does the heavy production (voiceovers + b-roll) for the faceless posts, Claude generates covers and writes every caption, and a new `/content-batch` command runs the whole thing in bulk. The 30 get **scheduled out over ~4–6 weeks**, not all posted at once.

### Why This Matters

Outreach is quiet on weekends, so this is the highest-leverage use of the time: build a content buffer that runs your credibility engine for a month while you focus weekdays on outreach. It removes the daily "what do I post" friction and means your grid is never empty when a prospect checks you out. Content is the 20% that makes the 80% (outreach) convert.

---

## Current State

### Relevant Existing Structure

- **Scripts already written:** `outputs/content/30-post-authority-bank.md` (30 posts across pillars, carousel-led, reels flagged with Artlist shot lists), `outputs/content/scripts/builder-reels-batch-1.md` + `-batch-2.md` (16 reel scripts), `outputs/content/batch-film-kit-session-1.md`, `outputs/content/reels/` (finished examples).
- **Engine + agents:** `trend-scout`, `hook-writer`, `visual-producer` (wired to **Artlist + Higgsfield**), `repurposer`.
- **Commands:** `/content`, `/content-week`, `/make-reel`, `/make-carousel`, `/thumbnail`, `/repurpose`, `/skill-drop`.
- **Social system:** `outputs/social/social-engine.md` (the script → film → polish → post pipeline, just built).
- **Brand voice:** `outputs/brand/brand-positioning.md`, `outputs/brand/social-media-intelligence.md` (pillars, segments, hooks, 30-day calendar), `outputs/brand/30-day-instagram-calendar.md`.
- **Visual tracking:** `outputs/content/visual-log.md`.

### Gaps or Problems Being Addressed

1. **No batch producer.** Scripts exist but nothing turns 30 of them into finished, ready-to-post assets in one run.
2. **Filming is the bottleneck.** No format plan that minimises time on camera (30 filmed pieces in a weekend is unrealistic; ~6–8 batched clips is not).
3. **Artlist isn't operationalised for volume.** Its voiceover + b-roll automation isn't documented as a repeatable faceless-reel recipe.
4. **No weekend run-sheet or scheduler workflow.** No 2-day schedule, no "how to schedule 30 posts across a month" step.
5. **Niche drift.** The banks are angled at the old hospitality/AIOS-builder positioning; a slice needs re-angling to the current build-in-public / appointment-business (med spa/reactivation) story.

---

## Proposed Changes

### Summary of Changes

- Create **`outputs/content/weekend-sprint/`** — run-sheet + the 30-post production plan/tracker + the one-session film shot-list.
- Add a **`/content-batch [N]`** command — produces N finished posts in one run (hook + script/slides + caption + hashtags + shot list) and **queues faceless assets (Artlist voiceover + b-roll) via `visual-producer`**, logging to the tracker.
- Create **`outputs/social/artlist-automation.md`** — exactly what Artlist can/can't automate + the batch faceless-reel recipe + CapCut assembly.
- Refresh/re-angle a slice of the existing 30 scripts to the current positioning and pull them into the sprint plan (reuse, don't rewrite).
- Update `CLAUDE.md` + cross-link `/content-week`.

### New Files to Create

| File Path | Purpose |
| --- | --- |
| `outputs/content/weekend-sprint/README.md` | The weekend run-sheet: the goal (30 produced + scheduled), the format mix, the 2-day schedule, and the scheduling/posting workflow. |
| `outputs/content/weekend-sprint/30-post-plan.md` | The master tracker: 30 rows — #, pillar, format, hook, source script, assets needed, status. Drives the whole weekend. |
| `outputs/content/weekend-sprint/batch-film-shotlist.md` | The ONE filming session: the 6–8 talking-head clips to record back-to-back (hook + lines each) so Jess films once. |
| `outputs/social/artlist-automation.md` | What Artlist automates (voiceover ✅ / b-roll ✅ / images ✅ / auto-post ❌) + the faceless-reel batch recipe + CapCut steps. |
| `.claude/commands/content-batch.md` | `/content-batch [N]` — bulk producer: N finished posts + queued Artlist faceless assets, logged to the tracker. |

### Files to Modify

| File Path | Changes |
| --- | --- |
| `.claude/commands/content-week.md` | Add a note: for a big weekend push use `/content-batch [N]`; keep `/content-week` as the 5–7/week planner. |
| `outputs/social/social-engine.md` | Link the weekend sprint + `artlist-automation.md`; add the "batch 30, schedule out" note. |
| `CLAUDE.md` | Under the Content Engine / Daily OS: add `/content-batch`, the weekend-sprint folder, and the Artlist automation doc. |

### Files to Delete (if any)

None. The existing banks are reused as source material.

---

## Design Decisions

### Key Decisions Made

1. **Produce 30, schedule out — don't post 30 in a weekend.** Posting 30 at once tanks reach and reads as spam. The weekend builds a **buffer**; the 30 drip out ~1–2/day over 4–6 weeks via a scheduler. (Reframes "get 30 up" into the version that actually works.)
2. **Format mix that needs one film session, not thirty.** Target split of 30: ~**10 carousels** (designed, no film), ~**10 faceless reels** (Artlist voiceover + b-roll, no film), ~**5 screen-record reels** (strongest proof, no face needed), ~**5 talking-head reels** (filmed back-to-back in ONE session). Jess is on camera once.
3. **Artlist automates the faceless production; assembly + posting stay manual.** Honest scope: Artlist generates voiceovers, b-roll and images on my command; it cannot auto-post. Jess (or a scheduler) assembles in CapCut and posts. "Automate" = I batch-produce the assets, not hands-off publishing.
4. **Reuse the existing scripts.** The 30-Post Authority Bank + 16 builder-reels already cover this — the weekend is production, not writing. Re-angle only where the old niche shows.
5. **One new command, not a new skill from scratch.** The engine exists; the only missing piece is a **bulk producer** (`/content-batch`). Answer to "do we need a specific social skill?": no — add `/content-batch` and operationalise Artlist.
6. **Default angle = build-in-public / AI authority.** Niche-agnostic, fastest to produce, builds credibility for all outreach; sprinkle posts angled at appointment-business owners (the reactivation story).
7. **Compliance stays on.** If any post touches the med-spa/health side: no prescription-med brand names, no before/afters, no testimonials.

### Alternatives Considered

- **Film all 30.** Rejected — unrealistic in a weekend and unnecessary; faceless + carousel + screen-record cover most formats.
- **Fully automate posting.** Rejected — Artlist can't post; native auto-posting of 30 would look spammy anyway. A scheduler (Meta Business Suite, free) is the right tool.
- **Write 30 fresh scripts.** Rejected — they already exist; rewriting wastes the weekend.
- **A big new "social media skill".** Rejected — over-engineering; `/content-batch` + the existing agents is enough.

### Open Questions (if any)

Defaults applied, none blocking:
1. **Film one 6–8 clip session?** Default yes (the only on-camera time). If Jess wants zero filming, we shift those 5 to faceless/screen-record.
2. **Posting cadence for the 30?** Default: ~1/day (mix reels + carousels) over ~4–6 weeks, scheduled in Meta Business Suite (free). Confirm or adjust.
3. **Artlist credits/connection.** If the Artlist MCP is connected I produce assets directly; if not, the doc gives Jess the exact prompts/scripts to run in the Artlist app herself.

---

## Step-by-Step Tasks

### Step 1: Build the 30-post production plan (the tracker)

Create `outputs/content/weekend-sprint/30-post-plan.md`.

**Actions:**
- Pull the 30 from `30-post-authority-bank.md` + the 16 builder-reels, de-duplicated, and assign each a **format** to hit the mix (10 carousel / 10 faceless reel / 5 screen-record / 5 talking-head).
- Re-angle ~5–8 to the current positioning (build-in-public + the reactivation/enquiry-response story for appointment businesses).
- Table columns: **# · Pillar · Format · Hook · Source script (link) · Assets needed (voiceover? b-roll? cover? film? screen-record?) · Status (Draft → Produced → Scheduled → Posted)**.
- Add a legend + the target mix at the top.

**Files affected:** `outputs/content/weekend-sprint/30-post-plan.md`

---

### Step 2: Write the weekend run-sheet

Create `outputs/content/weekend-sprint/README.md`.

**Actions:**
- State the goal: **30 produced + scheduled** (not 30 posted this weekend).
- The 2-day schedule:
  - **Saturday AM:** run `/content-batch 15` → I produce scripts/captions + queue Artlist voiceovers/b-roll for the faceless set; Jess designs the carousels (Canva template) while assets render.
  - **Saturday PM:** the ONE **batch-film session** (record 5–8 talking-head clips from `batch-film-shotlist.md`) + record 5 screen-captures of the system/skills working.
  - **Sunday AM:** run `/content-batch 15` for the rest; assemble reels in CapCut (drop in Artlist voiceover + b-roll + captions).
  - **Sunday PM:** **schedule all 30** in Meta Business Suite (free), ~1/day, and mark them Scheduled in the tracker.
- Include the scheduling how-to (Meta Business Suite / Later free tier) and the "drip, don't dump" rule.

**Files affected:** `outputs/content/weekend-sprint/README.md`

---

### Step 3: Build the one-session film shot-list

Create `outputs/content/weekend-sprint/batch-film-shotlist.md`.

**Actions:**
- Select the 5–8 posts marked "talking-head" and lay out a single filming session: for each, the **hook** (say to camera) + the 2–4 key lines, in the order to shoot, with wardrobe/setting notes (natural light, coastal, per Brand Bible).
- Add a 5-shot **screen-record list** (what to capture on screen: `/daily` running, a booking/text landing, a skill firing) — the proof shots.
- One line: "Film these back-to-back in ~30–40 min. One outfit, one setting, done."

**Files affected:** `outputs/content/weekend-sprint/batch-film-shotlist.md`

---

### Step 4: Document the Artlist automation

Create `outputs/social/artlist-automation.md`.

**Actions:**
- **What Artlist automates:** `generate_voiceover` (script → narration for faceless reels ✅), `generate_video` (b-roll ✅), `generate_image` (covers/backgrounds ✅ — but text-in-image is unreliable, so text goes on via Canva/CapCut). **What it can't:** auto-post ❌; assembly is CapCut.
- **The faceless-reel recipe (repeatable):** script → Artlist voiceover → Artlist/Higgsfield b-roll to match each line → CapCut assemble + captions → export 9:16.
- **Higgsfield vs Artlist:** Artlist for voiceover + b-roll clips; Higgsfield for covers/thumbnails, avatar, image-to-video, virality check.
- **Batch note:** `/content-batch` calls `visual-producer` to generate the voiceovers + b-roll for all faceless posts in the run; Jess just assembles.
- Fallback if the MCP is down: the exact prompts/scripts to paste into the Artlist app directly.

**Files affected:** `outputs/social/artlist-automation.md`

---

### Step 5: Build the `/content-batch` command

Create `.claude/commands/content-batch.md`.

**Actions:**
- `/content-batch [N]` (default 10): take the next N un-produced rows from `30-post-plan.md` and, for each, output the finished post — 3 hooks, the script or carousel slides, caption, hashtags, one CTA, and the shot/asset list.
- For **faceless** rows: launch `visual-producer` to generate the **Artlist voiceover + b-roll**; for **carousel** rows: generate the cover + note the slide text for Canva; for **talking-head/screen-record** rows: output the shot-list reference (no generation).
- Save each finished post to `outputs/content/weekend-sprint/posts/` (or append to a dated batch file) and update the tracker status → Produced. Log visuals to `visual-log.md` with credits.
- Preflight Artlist/Higgsfield credits; be efficient; report what was produced.

**Files affected:** `.claude/commands/content-batch.md`

---

### Step 6: Cross-link + document

Modify `.claude/commands/content-week.md`, `outputs/social/social-engine.md`, `CLAUDE.md`.

**Actions:**
- `content-week.md`: note `/content-batch [N]` for a big push.
- `social-engine.md`: link the weekend sprint + `artlist-automation.md`; add "batch 30, schedule out over weeks."
- `CLAUDE.md`: add `/content-batch`, the `outputs/content/weekend-sprint/` folder, and `outputs/social/artlist-automation.md` under the content engine.

**Files affected:** `.claude/commands/content-week.md`, `outputs/social/social-engine.md`, `CLAUDE.md`

---

### Step 7: Validate

**Actions:** run the checklist below; confirm the tracker has 30 rows across the target format mix and the run-sheet is executable.

---

## Connections & Dependencies

### Files That Reference This Area

- `.claude/commands/content.md`, `content-week.md`, `make-reel.md`, `make-carousel.md`, `repurpose.md`, `daily.md` (Block 4 content).
- `.claude/agents/visual-producer.md`, `hook-writer.md`, `trend-scout.md`, `repurposer.md`.
- `outputs/social/social-engine.md`, `outputs/content/30-post-authority-bank.md`, `outputs/content/scripts/`, `outputs/brand/brand-positioning.md`.

### Updates Needed for Consistency

- `CLAUDE.md` lists `/content-batch` + the weekend-sprint folder.
- `visual-producer` stays the single Artlist/Higgsfield operator; `visual-log.md` records credits.
- Voice checked against the Brand Bible; AU compliance where health content appears.

### Impact on Existing Workflows

- `/content-batch` is the new bulk producer; `/content` stays the daily single post; `/content-week` the weekly planner. `/daily` Block 4 unaffected. The weekend sprint feeds a scheduled buffer so weekday `/daily` content can pull from the bank instead of producing fresh.

---

## Validation Checklist

- [ ] `outputs/content/weekend-sprint/30-post-plan.md` has 30 rows across the target mix (≈10 carousel / 10 faceless / 5 screen-record / 5 talking-head) with status tracking.
- [ ] `README.md` lays out the 2-day schedule + scheduling workflow + "drip don't dump" rule.
- [ ] `batch-film-shotlist.md` is a single, shoot-once session (5–8 clips) + a 5-shot screen-record list.
- [ ] `outputs/social/artlist-automation.md` documents voiceover/b-roll/image automation, the faceless recipe, and the CapCut steps.
- [ ] `/content-batch [N]` produces N finished posts and queues Artlist faceless assets, updating the tracker.
- [ ] `CLAUDE.md` + `content-week.md` + `social-engine.md` cross-link the new pieces.
- [ ] Reused existing scripts (no wholesale rewriting); re-angled slice reflects current positioning.

---

## Success Criteria

1. By Sunday night, **30 posts are produced and scheduled** (not dumped) across the next ~4–6 weeks.
2. Jess filmed on camera **once** (one 6–8 clip session); the rest are carousel/faceless/screen-record.
3. **Artlist produced the faceless assets** (voiceovers + b-roll) in batch, via `/content-batch`.
4. Running `/content-batch [N]` reliably turns tracker rows into finished, ready-to-schedule posts.
5. The grid is never empty when a prospect checks — a month of credibility runs on autopilot while weekdays stay on outreach.

---

## Notes

- **Realistic reframe:** "30 up this weekend" = 30 *produced + scheduled*, drip-posted over weeks. Posting 30 at once would hurt reach.
- **Loveable app:** when Griffin's Rundown→script app is live, it becomes an additional script source feeding `/content-batch`.
- **Highest-value posts:** the screen-record reels (proof the system works) and the build-in-public talking-heads — front-load these in the schedule.
- **Weekday tie-in:** once the buffer exists, `/daily` Block 4 just pulls the next scheduled post instead of producing fresh — protecting outreach time.
- **Don't over-invest in perfection:** a phone-shot, Artlist-polished reel that ships beats a perfect one that never does.

---

## Implementation Notes

**Implemented:** 2026-09-18

### Summary
- Built `outputs/content/weekend-sprint/`: `30-post-plan.md` (30 rows across the exact mix — 5 talking-head, 5 screen-record, 10 faceless, 10 carousel, with hooks, sources, assets, status), `README.md` (2-day run-sheet + scheduling workflow + "drip don't dump"), `batch-film-shotlist.md` (one 5-clip film session + 5 screen-captures).
- Built `outputs/social/artlist-automation.md` (voiceover/b-roll/image = yes; auto-post = no; the faceless recipe + CapCut steps + MCP-down fallback).
- Built `.claude/commands/content-batch.md` (`/content-batch [N]` bulk producer that generates copy + queues Artlist assets + updates the tracker).
- Cross-linked `/content-week`, `social-engine.md`, and `CLAUDE.md`.

### Deviations from Plan
- None material. `/content-batch` saves finished posts to `outputs/content/weekend-sprint/posts/` (created on first run).

### Issues Encountered
- Artlist/Higgsfield MCP connectivity has been intermittent this session; `content-batch.md` + `artlist-automation.md` include a fallback (produce all copy + hand Jess exact prompts to run in the Artlist app) so the weekend is never blocked.
