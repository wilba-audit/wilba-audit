# /content — Your Daily Content Engine

> The flagship. One command, and today's content is done.
> Rundown AI → WILBA angles → a ready-to-shoot reel → the visuals made → all in your brand voice.

## What this does

This runs the whole morning loop end to end so Jess never faces a blank page. It orchestrates the content agents in order and hands back a finished daily content brief.

## Instructions

Run these steps in order. Explain each step in one plain-English line as you go (Jess is non-technical and likes to see what's happening).

### Step 1 — Scout today's angles
Launch the **trend-scout** agent. It reads today's The Rundown AI email from Gmail and returns 2-3 WILBA angles ranked best-first, with the #1 pick of the day.

If there's no fresh Rundown email, say so and offer to pull an angle from the 30-day calendar in `outputs/brand/social-media-intelligence.md` instead.

### Step 2 — Confirm the pick (fast)
Show Jess the ranked angles in a short, skimmable list. Recommend the #1 pick and ask a single quick question: **"Shoot the #1, or pick another?"** Default to #1 if she says go. Don't over-ask — she's the director, keep it to one beat.

### Step 3 — Write it
Launch the **hook-writer** agent on the chosen angle. Get back the full package for the recommended format (reel script + 3 hook options + on-screen text + caption + hashtags, or carousel/YouTube as fits).

### Step 4 — Make the visuals
Launch the **visual-producer** agent to generate the matching asset(s) in Higgsfield — a thumbnail for YouTube, cover + slides for a carousel, or b-roll/faceless video for a reel. Preflight credits and generate 1-2 options for the hero asset.

### Step 5 — (Optional) Virality gut-check
If a hero video was made, have visual-producer run the virality predictor and report shoot/skip + one fix.

### Step 6 — Deliver the brief (phone-film-ready)
Assemble everything into a dated file: `outputs/content/YYYY-MM-DD-daily-brief.md` — built so Jess can film it on her phone in 10 minutes:
- Today's angle + why it wins
- **3 hook options** (pick one on camera)
- **A 20–30s script** (what to say)
- **A shot list** — exactly what to film, in order (talking-head lines + any screen-record)
- **The b-roll + cover** made in Artlist/Higgsfield (rendered + ids + credits)
- **The caption + hashtags + the one CTA**

Then give Jess a 3-line summary in chat: what to record, what's attached, the single next action. See `outputs/social/social-engine.md` for the full film → polish → post flow.

## Notes
- **Script source:** default is `trend-scout` on The Rundown. When Griffin's Loveable app (Rundown → scripts) is live, Jess pastes that script in and this command starts at Step 3 (visuals).
- Default angle = **build-in-public / AI authority** (builds credibility for all outreach); angle at med-spa owners when it fits.
- Keep the run tight — this should feel like magic, not a meeting.
- Everything checks against `outputs/brand/brand-positioning.md`. If anything smells off-brand, fix it before delivering.
- Credits are real money — be efficient, but this is the highest-ROI spend WILBA has.
