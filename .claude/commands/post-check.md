# /post-check [draft] — Brand + Virality Gut-Check Before You Post

> Paste a caption, script, or drop a video. Get a fast on-brand + will-it-perform check before you hit publish.

## Instructions

**Input:** `$ARGUMENTS` — pasted copy, a path to a draft, or a reference to a video asset id.

### If it's copy (caption/script):
Check it against `outputs/brand/brand-positioning.md`:
- Does it start with the point? (Rule 1)
- One idea? Numbers used? "You" not "business owners"? Contractions?
- **Banned phrases** (Section 4f) — flag any, suggest the fix
- Is there exactly one clear CTA at the end?
- Does it sound like Jess (Section 4 voice) or like a press release?

Return a **verdict: SHIP / TWEAK / REWORK**, the specific fixes if any, and a cleaned-up version.

### If it's a video:
Launch the **visual-producer** agent to run Higgsfield's **virality_predictor**. Report predicted performance, hook strength, retention risk, and the single highest-impact fix. Verdict: SHIP / TWEAK / REWORK.

Keep it fast and honest — this is the final gate before Jess's face is on the internet. Flatter nothing; protect the brand.
