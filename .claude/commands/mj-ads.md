# /mj-ads — Monkey Joe's Google & Facebook Ads Status, Audit & Controls

> Michael pays the ad spend ($1,500/mo total, ~$750/store, paid directly to Google); Jess runs the
> ads. Meta is live. This command pulls status, runs the audit, and safely controls Meta.
> Full written audit: `outputs/monkey-joes/ADS-AUDIT-2026-07.md`.

## When Jess runs this
`/mj-ads` = "where are the ads at — spend, results, what to change?" Report both platforms, both
locations. If she asks to change something, do it through the Meta script with guardrails.

## Key findings baked in (from the pilot audit — refresh with live/CSV data)
- **50%-off beats BOGO on Google at BOTH locations** (WP $21 vs $40/conv; POL $28 vs $37). The call
  note "BOGO better at WP" was about FB/in-store, not Google search.
- **POL budget is backwards** — its winner (50% off) is capped below its weaker campaign (BOGO). Flip it.
- **WP is cheaper & budget-limited** (CPC ~$0.45 vs POL ~$1.16) → best place to add budget.
- **Meta leads are cheap (~$3.25–$3.73)**; **retargeting is the underused lever.**
- **Conversion tracking is suspect** (both Google accounts show exactly 51 conv; a GHL form bug
  under-fired the event) — verify before trusting cost/conv.
- **Parties stay OFF paid search** (party keywords $25–$40 CPC) — drive via the birthday strategy.

## Data sources
- **Meta (live):** reporting via `fetch_consolidated_reporting.py`; write control via
  `mj_meta_manage.py` (needs `META_ACCESS_TOKEN` + `META_AD_ACCOUNT_POL/WP`).
- **Google Ads:** reporting in `fetch_consolidated_reporting.py` (needs approved dev token + OAuth).
- **⚠️ Network policy:** this session may **block** the Facebook/Google/GHL APIs (egress 403). If so,
  work from the **exported CSVs** in the client archive, or run via GitHub Actions. Don't route
  around the policy.

## Status check (default)
1. `python3 scripts/mj_meta_manage.py verify` — token sees both ad accounts.
2. `mj_meta_manage.py list --loc POL` / `--loc WP` — status, budget, last-7d spend per campaign.
3. `fetch_consolidated_reporting.py --days 30` — joined Meta + Google + GHL (Google skips if unwired).
4. Report per location: spend, clicks, leads/conv, cost-per-result, best & worst ad — tied back to
   **redemptions** (`/mj-redemptions`) wherever possible, since that's Michael's real KPI.

## Controls (Meta — dry-run → confirm → execute)
- Pause: `mj_meta_manage.py pause --loc POL --campaign <id> --execute`
- Enable: `... enable ... --execute`
- Budget: `mj_meta_manage.py budget --loc WP --adset <id> --daily 25 --execute` (hard $60/day guardrail)
- **Recommended first moves:** POL Google flip to 50%-off; raise WP budget; scale Meta retargeting;
  archive the dead "MJ - POL Spring 2026" campaign.

## Reading results for Jess (non-technical)
Translate to outcomes + dollars: *"WP spent $660 and drove 204 leads at $3.25 each — the efficient
account; POL is pricier. On Google, 50%-off is beating BOGO everywhere, but POL's budget is on the
wrong one — flip it."* Always connect spend → redemptions where the data allows.

## What I need from Jess if blocked
- Meta: confirm `META_ACCESS_TOKEN` + both `META_AD_ACCOUNT_*` are available.
- Google: is the dev token approved? Do both locations have Google Ads accounts?
- Confirmed monthly budget per location (to flag over/under-spend).
- Whether to work **live via API** (needs network-policy change) or **from CSV exports**.
