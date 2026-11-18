---
name: gta6-clip-repurposer
description: >-
  Clip Producer for the GTA 6 codes channel. Use whenever turning a long-form
  YouTube video, transcript, recording or test session into YouTube Shorts,
  Instagram Reels or TikTok clips, including picking clip moments, writing
  hooks, on-screen text, captions, per-platform titles/descriptions, hashtags,
  CTAs, or planning A/B hook tests. Trigger on "clips", "shorts", "reels",
  "tiktok", "repurpose", "cut this down".
---

# GTA 6 Clip Repurposer

Each clip should stand alone as **one claim, one verdict, one payoff**. It
should transform the long-form (a new hook, a tighter edit, on-screen context),
not reupload a slice. Low-value duplicates underperform and risk
platform demonetisation.

## Rules (and why)
- **The verdict comes in the first 2 seconds.** People decide almost instantly.
  "This GTA 6 cheat is FAKE" beats a slow build.
- **Status matches the ledger.** Carry the ledger id and current status into every clip spec. Never cut a moment so that an Unverified claim looks confirmed.
- **No graphic violence in the first ~7 s** (YouTube ad rule, reported Sep 2026). Flag it if unavoidable.
- **Use native, clean files per platform.** Don't reuse TikTok-watermarked exports on Reels or Shorts.
- **Keep text inside safe zones.** Avoid the bottom ~20% and right edge, where UI covers it.

## Per-clip spec
```
CLIP <n>: <hook line>
Source: EP<n> <in>–<out> (<duration>)   Ledger: <id> = <status>
First frame: <non-violent visual>   First 2s VO/text: ...
Structure: hook → proof (input + result) → verdict badge → CTA
On-screen text (≤6 words per card): ...
Captions: burned-in, high contrast
YouTube Shorts title (≤60 chars): ...      Related video: EP<n>
Reels caption (hook line first, 3–5 tags): ...
TikTok caption (searchable keywords, 3–5 tags): ...
CTA: "Full test + live status: <site>/<anchor>"
Test variable (if in an experiment): hook A vs B / first frame / length
Violence-in-first-7s flag: yes/no
```

Pick 3–5 clips per episode. Rank them by how strong the standalone payoff is, and
include at least one evergreen clip (how-to or scam-awareness).
