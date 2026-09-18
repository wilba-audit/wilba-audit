# /prospects [city] — Claude builds your pipeline

> Never face an empty list. Point me at a metro and I research ~10 qualified med-spa prospects and append them, ready to message.

## Instructions

Given a metro (`$ARGUMENTS` — e.g. "Brisbane", "Perth", "Sydney"; default rotate through Sydney/Melbourne/Brisbane/Gold Coast/Perth), build the next batch of prospects.

### Step 1 — Research
Use **WebSearch** to find independent, owner-operated cosmetic/injectable clinics in that metro. Good query shapes:
- "boutique cosmetic injectable clinic [city] owner registered nurse independent"
- "[suburb] cosmetic nurse founder clinic aesthetic"
- Best-of / "top injectable clinics [city]" listicles (then filter).

### Step 2 — Qualify against the ICP
**Keep:** cash-pay, injectables/aesthetics-led, owner-operated (nurse/founder), one location or a small handful, established (real review history → a dormant list to work), busy + well-reviewed.
**Drop on sight:** dermatology / plastic surgery, hospital or multi-specialty group, national chains/franchises, brand-new clinics.

### Step 3 — Append (de-duped)
Add ~10 new rows to `outputs/cash-sprint/prospects-medspa.md`, **skipping any already listed**. For each: clinic · owner (mark "verify" if unsure) · city/area · site · Status: New. Keep the default leak/angle (dormant list + slow enquiry response) unless something specific jumps out.

### Step 4 — Hand off
Tell Jess how many were added and from where, and remind her the next `/daily` will pull from them. Offer: "Want me to research another metro?"

## Rules
- Real, verifiable businesses only — no invented names. Mark anything uncertain "verify".
- Owner name + Instagram matters most (the injector is the brand → DM a person).
- Keep it fast: research → filter → append. This is pipeline generation, not a report.
