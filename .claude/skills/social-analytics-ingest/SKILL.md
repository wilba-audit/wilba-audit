---
name: social-analytics-ingest
description: >
  Ingest the analytics and content an account OWNER exports themselves from each
  platform (LinkedIn CSV, Meta "Download Your Information" for Instagram/Facebook,
  TikTok/YouTube exports) plus screenshots of posts — and turn them into a
  structured, grounded input for the social-media-audit skill. Use this whenever
  live scraping is blocked or off-limits (locked-down environments, or to stay
  compliant): the client exports their own data, we parse it. Also runs the
  screenshot-based post-STYLE teardown.
---

# Social Analytics Ingest

The compliant, works-anywhere way to ground an audit in real data. It does **not**
scrape and does **not** log into anyone's account — the account owner exports
their own data (their legal right on every platform), and this skill parses it.

## When to use
- The environment can't reach social hosts (egress-blocked sandbox), OR
- You want to stay strictly within platform terms (no scraping/automated login), OR
- You have screenshots/exports from the client and need them turned into findings.

## Why this exists (the honest constraint)
Public scraping (`social-data-collector`) needs open networking and can still hit
login walls. Logging in via automation to pull someone's feed violates platform
terms and risks their account. The reliable path is the owner's own export — which
is exactly how Dr Schoeman's LinkedIn data came in and got fully grounded.

## Two modes

### Mode A — Parse owner exports (numbers)
1. Ask the client for the right export per platform — see
   `references/export-guides.md` (plain-English, per platform).
2. Drop the files in a folder and run:
   `node scripts/parse_exports.mjs <folder> --out outputs/<slug>/ingested-summary.md`
3. The parser handles LinkedIn "Profile Growth" CSVs today (detects multiple
   profiles, ignores duplicate exports, flags dormant pages), summarises generic
   CSVs, and points at Meta "Download Your Information" JSON for IG/FB (parsed per
   client as Meta's structure varies).
4. Feed `ingested-summary.md` to `social-media-audit`.

### Mode B — Screenshot post-STYLE teardown (content)
When you have screenshots (or pasted text) of real posts, run the forensic
teardown in `social-media-audit/references/manual-review-protocol.md`. Grade each
post on: hook (first 2s / first line), tone (patient vs. peer), captions, pacing,
visual identity, CTA, personality — then **rewrite the hook + caption** so the
client sees the before/after. Vision-capable: paste the screenshots directly.

## Rules
- Never invent a metric. Blanks stay blank; duplicates are flagged, not summed.
- If two profiles appear, surface the fragmentation — don't silently merge them.
- Tag every figure `[REAL]` (from an export/screenshot) vs `[CONFIRM]` (still needed).

## Companion skills
- `social-media-audit` — consumes this skill's output to produce the audit.
- `social-data-collector` — the public-scraping alternative (needs open network).
