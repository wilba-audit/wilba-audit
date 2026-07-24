---
name: social-session-capture
description: >
  "Log in via Playwright" the responsible way — for reviewing a client's own
  content when native exports aren't enough. The ACCOUNT OWNER logs in themselves
  in a visible browser (they enter the password + 2FA); the session is saved
  locally and used to capture THEIR OWN pages (recent activity, analytics) as
  screenshots + text for the audit. No stored passwords, human-in-the-loop, data
  stays local. Use only on accounts you own or have explicit permission for.
---

# Social Session Capture (human-in-the-loop)

Some reviews need the actual posts, and native exports (see `social-analytics-ingest`)
don't cover everything. This skill gets that content **without the thing that gets
accounts banned** — an unattended bot that stores a password and auto-logs-in.

## The safety model (read before using)
Automated login + scraping of LinkedIn/Instagram/etc. **violates their terms and
can get the account restricted or permanently banned.** For a client (e.g. a
doctor whose reputation lives on LinkedIn) that is a serious, hard-to-reverse
harm. So this skill is deliberately built to minimise that risk:

- **The human logs in, not the bot.** A visible browser opens; the owner types
  their own password and does 2FA. No credentials are stored or handled by code.
- **Headed by default.** A person watches the session.
- **Owner's own pages only**, at a gentle, human-like pace (throttled, limited scroll).
- **Local + private.** The session file lives in `.auth/` and is **gitignored**;
  captures stay on the machine.
- **Consent gate.** The capture step refuses to run unless the config states you
  own or have explicit permission for the accounts.

**Prefer `social-analytics-ingest` (owner's native exports) first** — it's lower
risk still. Use this skill only when you additionally need the live post content
and you have the owner present and consenting.

## Requirements
- A **normal machine with open networking** (won't run in the egress-blocked Claude
  web sandbox). `npm i playwright` first.

## Use
1. **Save a login session** (opens a window; the owner logs in; press Enter):
   `node scripts/capture.mjs login linkedin`
2. **Capture their own pages** (config lists the owner's URLs + a consent line):
   `node scripts/capture.mjs capture config.json`
   → full-page screenshots + extracted text in `outputs/<slug>/captures/`.
3. Hand the `.png` + `.txt` to `social-media-audit` → run the manual-review /
   post-STYLE teardown on real content.

See `scripts/SETUP.md` for a copy-paste walkthrough and a sample config.

## What this skill will NOT do
- Store or type passwords; run unattended/headless credential logins; mass-scrape;
  touch accounts without a consent statement. Those are the patterns that get
  clients banned — out of scope by design.
