---
name: social-data-collector
description: >
  Collect the maximum PUBLIC data available for a person or brand's social
  accounts (Instagram, YouTube, TikTok, LinkedIn, X) so a social media audit is
  built on real numbers, not guesses. Use before/with the `social-media-audit`
  skill when you need actual profile stats and recent-post metadata. Runs a
  Node + Playwright collector script; requires OPEN outbound network to the
  social hosts (won't run inside a sandbox whose egress policy blocks them).
---

# Social Data Collector

Turns handles into real, structured data for an audit. Its whole job is to
**never make a number up** — it reports exactly what each platform exposes
publicly, and honestly marks anything blocked or login-walled.

## When to use
- A prospect/client audit needs real metrics and you have their handles.
- Pair it with `social-media-audit`: collect first, then audit the output.

## Hard requirement: network egress
The script must reach `instagram.com`, `youtube.com`, `tiktok.com`,
`linkedin.com`. **It will not work inside a locked-down agent/CI sandbox whose
egress policy blocks those hosts** (symptom: `403 CONNECT policy denial` /
`ERR_TUNNEL_CONNECTION_FAILED`). Run it where networking is open:
1. On a normal machine (Jess's Mac, the developer's laptop), or
2. In a WILBA cloud environment created with an open/permissive network policy
   (see code.claude.com/docs — the network policy is chosen per environment).

If you're in a blocked sandbox, don't fake it: tell the user, and either have
them run the collector locally or supply the data another way (see the
`social-media-audit` manual-review protocol).

## What it collects (public, no login)
- **YouTube** (no browser needed — public RSS): channel, subscriber text,
  last ~15 videos with **real public view counts**, titles, dates. This is the
  richest honest signal available without analytics access.
- **Instagram**: followers / following / posts (from og:description + embedded
  JSON), bio, title.
- **TikTok**: profile stats + recent video metadata where exposed.
- **LinkedIn**: public name + headline only (engagement needs login — flagged).
- **X**: profile meta where exposed.

## How to run
1. Install once: `npm i playwright` (Chromium auto-detected; set `CHROMIUM_PATH`
   to override). YouTube works even without Playwright.
2. Write a `config.json` (see `scripts/collect_social.mjs` header for the shape).
3. `node scripts/collect_social.mjs config.json`
4. Outputs `collected-data.json` + `collected-data.md` in the config's `outDir`.
5. Feed `collected-data.md` to `social-media-audit`.

See `scripts/SETUP.md` for a copy-paste, non-technical walkthrough.

## Honesty rules
- Blocked host → record the block, continue, do not substitute a guess.
- A hidden count stays blank (`[hidden]`), it does not become an estimate.
- The audit built on this data cites which numbers are real vs. still needed.
