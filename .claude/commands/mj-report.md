# /mj-report — Monkey Joe's Weekly & Monthly Reports

> Michael wants a clean, **on-brand** (Monkey Joe's colors), simple-first-impression report backed
> by data — for himself and to pitch corporate (Jack & Daryl at Big Game Brands). This command
> builds both the **weekly ops report** and the **monthly corporate report**.

## When Jess runs this
- `/mj-report weekly` → the internal ops scorecard (what's working this week).
- `/mj-report monthly` → the corporate-facing report (due ~the 5th of each month).
- Bare `/mj-report` → ask which, default to weekly.

## Where the data comes from (and the one gap)
- **Ad performance:** `scripts/fetch_consolidated_reporting.py` (Google + Meta once APIs reachable)
  or the exported CSVs if APIs are blocked by network policy. See `outputs/monkey-joes/ADS-AUDIT-2026-07.md`.
- **GHL:** opt-ins, codes generated, audience growth, birthday reach — via the GHL API (`/mj-ghl`).
- **⚠️ Redemptions (the money metric):** NOT in GHL by default. Codes are redeemed on **William's
  external verification page**, and **party sales via `BDAY25` in Aluvii** (no API). Until William
  writes a redeemed flag back into GHL, **you must request a redemption export from William** and a
  **BDAY25 count from Aluvii**. Never report redemptions as zero without stating the source/caveat —
  the pilot hit a GHL form-tracking bug that falsely showed zero.

## Weekly ops report — include
- New opt-ins (SMS/email) this week, per location
- Codes generated vs **redeemed** (with source caveat), by code type (`WELCOME` / `BOGO/` / `50% off` / `FJP/` / `BDAY25`)
- Ad spend + cost-per-result, top & bottom ad, any budget moves made
- Birthday: leads captured, reminders sent, `BDAY25` party redemptions
- 1–3 actions taken + 1–3 recommended
- Delivered by Resend (see `scripts/mj_weekly_scorecard.py`, already scheduled Mondays)

## Monthly corporate report — include (on-brand, decision-maker ready)
- **Executive line:** did it move the needle vs the **same month last year** (Michael's key test)
- Audience growth (new opt-ins, SMS list built)
- **Provable sales:** codes redeemed in-store + parties booked (`BDAY25`), with $ where possible
- Cost per acquisition / cost per redeemed customer (blended across Google + Meta)
- Offer performance by location (50%-off vs BOGO; POL vs WP)
- Reviews gained (5-star Google reviews — a documented pilot win)
- Birthday-party pipeline (leads → deposits → booked)
- Clear next-phase recommendation (scale to 9 locations narrative)
- **Branding:** Monkey Joe's colors, clean layout, simple first page then the data. Build as a
  self-contained HTML report (can publish as an Artifact for a shareable link).

## Guardrails
- **Back up every number** with its source (Michael/corporate will ask). If a number is estimated
  or from a caveated source, say so.
- Don't invent redemption or party figures — pull from William's export + Aluvii, or mark pending.
- Money-metric honesty over vanity metrics: impressions are nice, **redeemed codes + booked
  parties** are what corporate is buying.

## What I need from Jess if blocked
- William's **redemption export** (or confirmation he tags redeemed contacts back in GHL).
- **Aluvii `BDAY25`** party-redemption count for the period.
- **Last-year comparison** figures for store sales/traffic (from Michael) if we're to show "moved
  the needle."
