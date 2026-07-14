# /mj-ads — Monkey Joe's Google & Facebook Ads Status & Controls

> Michael pays the ad spend; Jess runs the ads. Meta (Facebook/Instagram) is **live now**.
> Google Ads reporting is built but likely pending API approval. This command pulls an on-demand
> status and, for Meta, lets you make changes safely.

## When Jess runs this
`/mj-ads` = "where are the ads at — spend, results, what's working?" Report both platforms,
both locations. If she asks to change something (pause a loser, bump a budget), do it through the
Meta management script with guardrails.

## Platforms & scripts
- **Meta (live):** reporting via `scripts/fetch_consolidated_reporting.py`; write control via
  `scripts/mj_meta_manage.py` (list / pause / enable / set budget). Needs `META_ACCESS_TOKEN`
  (scopes `ads_read` + `ads_management`), `META_AD_ACCOUNT_POL`, `META_AD_ACCOUNT_WP`.
- **Google Ads (reporting only, likely not wired yet):** in `fetch_consolidated_reporting.py`.
  Needs `GOOGLE_ADS_DEVELOPER_TOKEN` (must be **approved** by Google — slow), OAuth client +
  refresh token, and `GOOGLE_ADS_CUSTOMER_ID_POL/WP`. If these aren't set, report Google as
  "pending API access" rather than failing.

## Status check (default)
1. **Verify Meta access:** `python3 scripts/mj_meta_manage.py verify` — confirms the token sees
   both ad accounts.
2. **List campaigns + spend:** `python3 scripts/mj_meta_manage.py list --loc POL` and `--loc WP`
   — status, daily budget, last-7d spend per campaign.
3. **Consolidated pull:** `python3 scripts/fetch_consolidated_reporting.py --days 30` — writes
   `outputs/monkey-joes/reporting/consolidated.json` with Meta + Google + GHL joined by
   utm_campaign / promo-code channel prefix. Google silently skips if not configured.
4. **Report per location:** spend, impressions, clicks, leads, purchases (Meta pixel), blended
   cost-per-lead and cost-per-redeemed-customer (`blended_30d`). Name the best and worst ad.
5. **Google:** if not wired, state clearly what's needed to activate (dev-token approval status).

## Controls (Meta — ask before any change)
- **Pause a campaign:** `mj_meta_manage.py pause --loc POL --campaign <id> --execute`
- **Enable:** `... enable ... --execute`
- **Set an ad set's daily budget:** `mj_meta_manage.py budget --loc WP --adset <id> --daily 25 --execute`
  — hard guardrail refuses anything over **$60/day** unless `--max` is raised and Jess confirms.
- Every mutation is dry-run (no `--execute`) first; show the before/after and get a "yes".

## Reading the results for Jess (non-technical)
Translate to plain outcomes: *"Pointe Orlando spent $410 last week and drove 22 offer redemptions
— about $19 each. Winter Park's 'Weekday BOGO' ad is the winner; the 'Generic Fun' ad is burning
money, recommend pausing it."* Tie spend back to **redemptions** (via `/mj-redemptions`) whenever
possible — that's the number Michael cares about.

## What I need from Jess if blocked
- Meta: confirm `META_ACCESS_TOKEN` + both `META_AD_ACCOUNT_*` IDs are set as secrets/in `.env`.
- Google: is the developer token approved yet? If not, that's the gate — nothing to report until
  it clears. Confirm whether we even have Google Ads accounts for both locations yet.
- Monthly ad budget per location (so overspend/underspend can be flagged).

## After running
The Monday **weekly scorecard** (`scripts/mj_weekly_scorecard.py`) emails Jess a summary and
flags any platform that isn't wired. If you activate Google or change budgets, note it so the
scorecard narrative stays accurate.
