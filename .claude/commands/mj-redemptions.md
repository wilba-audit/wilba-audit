# /mj-redemptions — Monkey Joe's Promo Code Redemption Tracking

> The pilot lives or dies on **provable redemptions** — that's what proves marketing drove real
> visits, and it's what corporate is buying. This command reconciles the codes and reports
> redemptions by type and channel.

## ⚠️ How redemptions ACTUALLY work (confirmed from call transcripts)
Do not assume redemptions are GHL tags. The real pipeline:
1. Codes are **generated in GHL / Stripe**, delivered by **email + SMS**.
2. They're **redeemed in-store on William's external web verification page** (staff type the code;
   the page records used-status + date + staff initials).
3. **Party codes (`BDAY25`) are redeemed in Aluvii** — which has **no API**, so party attribution
   is a **manual export/count**.
4. **Redemption data therefore lives in William's backend + Aluvii — NOT in GHL by default.**

So the first job every run: **get the redemption numbers from the right place.**
- Ask William whether his verification backend **writes a redeemed flag back into GHL** (a tag/
  field). If yes → we can pull it via the GHL API. If no → we need a **weekly CSV export from
  William** and a **`BDAY25` count from Aluvii**.
- The pilot hit a **GHL form-tracking bug** that falsely showed **0 redemptions**. Never report zero
  without confirming the source is actually reporting.

## The live codes (see `outputs/monkey-joes/promo-codes.md` for full detail)
- `WELCOME` — $25 opt-in voucher (email→SMS opt-in)
- `BOGO/…` — Wacky Wednesday BOGO admission
- `50% off` — half-price admission (best Google performer)
- `FJP/…` — Frequent Jumper Card (10 jumps; not for parties/groups)
- `BDAY25` — $25 off a party (redeemed in **Aluvii** only)

The March `WACKY-*` / `COMEBACK` scheme is **dead** — don't report on it.

## How to pull the numbers
1. **If William tags redeemed back to GHL:** run `python3 scripts/fetch_consolidated_reporting.py
   --days 30` and read `outputs/monkey-joes/reporting/consolidated.json`. First **verify the actual
   tag/field names** with William and update `redeemed_tags` / `redeemed_by_channel` in
   `fetch_ghl()` to match — the current `redeemed-{loc}-g|f|e|d` guesses may not exist.
2. **If not:** request the **verification-page export** from William + the **Aluvii `BDAY25`** count,
   and build the report from those.
3. Note: this session's network policy may **block GHL** — if so, run via GitHub Actions or work
   from William's export (see `/mj-ghl` credential note).

## Report to Jess (plain English)
Per location: redemptions by code type (today / 7d / 30d), channel split (Google / FB / Email /
Direct), and redemptions ÷ ad spend = **cost per redeemed customer**. One-line read on what's
working. Always state the **data source** for the redemption figure.

## What I need from Jess if blocked
1. Does William's system **write redeemed back to GHL**, or do we get a **CSV export**?
2. The exact **live code strings** per location.
3. Is **`BDAY25`** live + redeemable in Aluvii, and who pulls that count?

## After running
If you corrected the tracking tags or code list, note it and make sure `/mj-report` and the weekly
scorecard now reflect the real redemption source.
