# /mj-birthday — Monkey Joe's Birthday Party Funnel

> Birthday parties are the highest-margin product. This command reports funnel health, operates the
> controls, and — critically — keeps our automations from colliding with William's GHL-native one.
> Full plan: `outputs/monkey-joes/BIRTHDAY-ACQUISITION-STRATEGY-2026-07.md`.

## ⚠️ Two things to check EVERY run
1. **Price safety.** `scripts/mj_birthday_sequence.py` and `mj_birthday_radar.py` hard-code
   **"Jungle Experience from $234"** and **"weekday from $194."** These figures appear in **NO
   source document** and are **unconfirmed**. If the daily drip is enrolled + live, it is emailing
   customers these prices. **Confirm the real package prices with Jess/Nicole, then fix or remove
   this copy before any more sends.** Do not treat these numbers as correct.
2. **Double-send risk.** There are TWO birthday systems: (a) **William's GHL-native birthday
   automation** (from the waiver DB) and (b) **our Python drip + radar**. If both run against the
   same contacts, parents get duplicate messages. **Confirm the single source of truth** (recommend
   William's GHL workflow for the birthday *reminder*; repurpose our scripts for the post-visit
   upsell) before running any send.

## The moving parts
- **Birthday Drip** — `mj_birthday_sequence.py`, daily via `mj-birthday-drip.yml`. 180-day,
  10-touchpoint nurture from **enrollment date**. Idempotent via `bday-sent-dN`. Exits on
  `birthday-{loc}-booked` / `unsubscribed`.
- **Birthday Radar** — `mj_birthday_radar.py`, weekly via `mj-birthday-radar.yml`. Reminders before
  the child's **actual birthday**. **Michael's stated cadence is 180/60/30 days**; the script
  currently uses **90/60/30** — reconcile.
- **POL only.** WP's waiver export has **no birthday data** yet (William chasing corporate/Aluvii).
  Radar reaching few WP contacts is expected until that's fixed.

## Attribution reality
Parties book **only in Aluvii** (no API). The only party attribution is **`BDAY25` redeemed in
Aluvii** — a manual count. Booking link in scripts: `monkeyjoespo.com/birthday-party` (confirm WP
routing). The agreed lead flow: birthday landing page (native form) → **N8N** emails front-of-house
→ front-of-house **calls + takes ~$50 deposit**. Form asks location, **child's age (not name)**,
preferred date.

## Status check (default)
1. Load creds (same GHL keys as `/mj-ghl`; network policy may block GHL from this session).
2. `python3 scripts/mj_birthday_sequence.py status` → enrolled vs booked per location.
3. `python3 scripts/mj_birthday_radar.py coverage` → how many contacts have a usable child birthday.
4. Confirm `CHILD_BDAY_FIELD_ID` is set (Jess says the field exists — pull its ID via `/mj-ghl`).
5. Dry-run both (`run` without `--execute`) to show who WOULD get messaged — **but reconcile with
   William's GHL workflow first** so you're not about to duplicate it.

## Controls (dry-run → confirm → execute)
- Enroll a cohort: `mj_birthday_sequence.py tag-cohort --loc POL --execute`.
- Mark booked: apply `birthday-{loc}-booked` to stop a sequence.
- Edit copy/timing: update `TOUCHPOINTS` / `WINDOWS`; **fix the unconfirmed prices** and align
  radar to the agreed cadence.

## Missing design doc
`mj_birthday_sequence.py` references `MJ-180Day-Birthday-Sequence-2026-06-22.md`, which isn't in the
repo. Offer to regenerate it from the script's touchpoints once prices are confirmed.

## What I need from Jess if blocked
1. Real party **package names + prices** (and the `$234/$194` — fix or remove).
2. **Which birthday automation is source of truth** — William's GHL workflow or our drip?
3. **Radar cadence** — 180/60/30 or 90/60/30?
4. **WP birthday data** — obtained yet?
