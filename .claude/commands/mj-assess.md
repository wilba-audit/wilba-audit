# /mj-assess — Monkey Joe's Campaign Assessment

> End-to-end assessment of the pilot: joins ad spend (Google + Facebook) to the GHL code
> funnel (generated → delivered → redeemed) and channel attribution, then produces findings +
> recommendations. Use it to answer "is this working, and what should we do next?"

## When Jess runs this
`/mj-assess` = "assess the whole campaign and tell me what the data says." Produces a findings
summary she can act on or turn into a report/proposal.

## Procedure

1. **Refresh GHL live.** Trigger the `mj-audit` workflow (`mcp__github__actions_run_trigger`,
   run_workflow, `mj-audit.yml`, ref `main`), wait ~3 min, read
   `outputs/monkey-joes/reporting/ghl-audit.md`. Numbers move — always pull fresh.
2. **Pull ad data.** From the platform exports (Google billing + campaign reports, Facebook export)
   or, once tokens are set as secrets, from `fetch_consolidated_reporting.py`. Google spend/credits
   come from the **billing statements** (the campaign "Cost" is gross; credits are separate).
3. **Build the funnel:** spend → codes generated (`promo-issued`) → delivered (`voucher-delivered`)
   → redeemed (unique redemption tags) → by channel (GHL attribution: google/facebook/other).
4. **Compute efficiency by channel:** cost per lead and **cost per redemption** for Facebook vs
   Google. This is the key number — it's what says which channel to back.
5. **Assess against the goal** (weekday walk-ins + parties): what's working, what's not, what's
   untapped.

## What to report (findings)
- Total spend (gross, credits, net) by platform + location
- Code funnel: generated / delivered / redeemed + redemption rate
- **Redemptions by channel** and **cost per redemption by channel** (the headline)
- Best offer (50%-off vs BOGO), best location (POL vs WP)
- Gaps: Google conversion tracking (form bug), 66 untagged redemptions (pre-attribution), parties
  not yet advertised, Meta/Google API tokens not wired
- 3–5 prioritised recommendations

## Guardrails
- **GHL numbers are live and grow** — always date-stamp the assessment ("as of <date>").
- Treat **Google "conversions" as directional** (known form bug); trust **GHL redemptions** as the
  real outcome.
- State the data source for every figure (billing vs campaign report vs GHL).

## After running
Offer to turn the findings into: the branded pilot report, the weekly scorecard, or a proposal
(e.g. `/mj-fb-proposal`).
