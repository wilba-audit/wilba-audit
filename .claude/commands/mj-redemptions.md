# /mj-redemptions — Monkey Joe's Promo Code Redemption Tracking

> The whole point of the pilot is proving marketing drives paying visits. Redeemed promo codes
> are the proof. Codes now live **in GHL** (not Aluvii anymore). This command reconciles the
> codes, pulls redemption counts, and reports which channel is actually working.

## When Jess runs this
`/mj-redemptions` = "how many codes got redeemed, and where did they come from?" Report by
location and by channel (Google / Facebook / Email / Direct).

## ⚠️ Known gap to check FIRST
There are two conflicting code schemes in the repo history:
- **March plan** (`outputs/monkey-joes/promo-codes.md`): Aluvii codes `WACKY-POL`, `WACKY-WP`,
  `WELCOME`, `COMEBACK`.
- **Live reporting** (`scripts/fetch_consolidated_reporting.py`): GHL tags `redeemed-{loc}`,
  `redeemed-{loc}-g|f|e|d`, and code format `BOGO-PO-G-XXXX`.

Jess confirmed **codes are in GHL**. So the source of truth is GHL. Your first job each run is to
**verify how a redemption actually gets recorded in GHL** — is it a tag applied by a GHL
workflow when a code is used? A custom field? A pipeline stage? Until that's confirmed, redemption
counts may read as **zero even when codes are being used**. If you can't confirm the mechanism,
say so plainly and ask Jess/William: *"When a customer redeems a code, what happens in GHL —
which tag or field gets set?"* That answer is what makes this report trustworthy.

## How to pull the numbers
1. Load creds (see `/mj-ghl` for the credential note — same keys).
2. Run `python3 scripts/fetch_consolidated_reporting.py --days 30` (it writes
   `outputs/monkey-joes/reporting/consolidated.json`). This already counts `redeemed-{loc}` and
   the per-channel `redeemed-{loc}-g|f|e|d` tags across today / 7d / 30d / MTD windows.
3. If the mechanism check above shows redemptions are recorded a **different** way (a field, a
   different tag), adjust the tags in `fetch_consolidated_reporting.py`
   (`redeemed_tags` and `redeemed_by_channel` in `fetch_ghl`) to match reality, then re-run.

## Report to Jess (plain English)
For **each location**:
- Total redemptions: today / last 7 days / last 30 days
- Channel split: how many came from Google vs Facebook vs Email vs Direct
- Redemptions ÷ ad spend = blended cost per redeemed customer (the `blended_30d` block already
  computes `blended_cpa_redeemed`)
- One-line read: "Facebook is delivering redemptions at $X each; Google is quiet — investigate."

## Reconcile the codes (do this when the schemes don't line up)
- Confirm the **actual live code names** with Jess (WACKY-*, BOGO-*, or the real ones).
- Update `outputs/monkey-joes/promo-codes.md` so it reflects the **GHL reality**, not the old
  Aluvii plan. Mark the Aluvii version as superseded rather than deleting the history.
- Make sure each live code maps to exactly one channel tag so attribution stays clean.

## What I need from Jess if blocked
1. The exact redemption mechanism in GHL (tag/field set on redemption).
2. The real, current list of promo codes and which channel each represents.
3. Whether William's GHL workflows already apply the channel-split tags (`-g/-f/-e/-d`) or if
   that split needs to be built.

## After running
If you corrected the tracking tags or the code list, note it, update the promo-codes doc, and
flag whether the weekly scorecard (`/mj-ads` / `mj_weekly_scorecard.py`) now reflects real
redemption data.
