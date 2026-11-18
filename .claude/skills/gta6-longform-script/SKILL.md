---
name: gta6-longform-script
description: >-
  Script Writer for the GTA 6 codes YouTube channel. Use whenever writing or
  revising a long-form YouTube episode, beat sheet, voiceover script, video
  outline, title options, thumbnail concepts or chapter list about GTA 6
  cheats, codes, offers, tests or scams, including "write EP2", "script this
  test", "outline a video". Produces fact-tagged, monetisation-safe scripts for
  a real human host.
---

# GTA 6 Long-form Script

Write for a **real human host** who tests things on camera. The channel's edge
is proof and personality. AI-sounding, mass-produced narration risks YouTube's
inauthentic-content rules and loses the trust the brand depends on.

## Rules (and why)
- **Tag every factual line** with `[LEDGER:<id>]` (status included) or
  `[VERIFY]`. A script with untagged claims cannot pass the publish gate.
- **Unverified ≠ working.** Phrase unverified claims as tests ("people say X,
  let's check") and confirmed ones with their evidence.
- **Non-violent cold open.** Reported YouTube rules make graphic violence in the
  first ~7 seconds ineligible for ads. Open on a menu, an input, weather or a
  vehicle.
- **No isolated cutscenes and no leaked footage.** Gameplay must be our own
  capture, with commentary.
- **Honest packaging.** The title and thumbnail must describe what the video
  actually shows. "FAKE ✗ / TESTED ✓ / UNCONFIRMED ?" badges are encouraged.

## Output format
```
# EP<n>: <working title>
Goal / viewer question:
Ledger rows covered: <ids + statuses as of today>
## Titles (3), honest, ≤70 chars
## Thumbnail concepts (2): real frame + badge + ≤4 words
## Beat sheet
| Time | Beat | Visual (capture needed) | Claims + tags |
## VO script
[0:00] COLD OPEN (non-violent visual: ...)
...
## Chapters
## Description draft (first 2 lines = hook + ledger link; disclaimer; affiliate disclosure if any)
## Pinned comment draft
## Capture shot list for the Tester
## Clip candidates (3–5): timestamp range + one-line hook → hand to gta6-clip-repurposer
```

Structure for a "test" episode:
1. Hook (verdict tease)
2. Method in 30 s: platform, game version, date
3. Claims tested one by one, each with source → input → result → badge
4. What's real instead (offers and bonuses)
5. Scam warning
6. CTA to the ledger and email alerts
