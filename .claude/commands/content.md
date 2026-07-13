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

### Step 6 — Deliver the brief
Assemble everything into a dated file: `outputs/content/YYYY-MM-DD-daily-brief.md` containing:
- Today's angle + why it wins
- The full copy (hook, script, caption, hashtags)
- The visuals (rendered + ids + credits spent)
- The one CTA
- A 1-line "how to shoot this" note (setting, wardrobe, framing per the Brand Bible)

Then give Jess a 3-line summary in chat: what to record, what's attached, and the single next action.

## Notes
- Keep the whole run tight — this should feel like magic, not a meeting.
- Everything checks against `outputs/brand/brand-positioning.md`. If anything smells off-brand, fix it before delivering.
- Credits are real money — be efficient, but this is the highest-ROI spend WILBA has.
