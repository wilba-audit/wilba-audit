# Monkey Joe's — Pilot Results Report

**From:** Jess / WILBA · **Date:** 2026-07-14 · **For:** William (Lanyu) → corporate review
**Locations:** Pointe Orlando (POL) · Winter Park (WP)

---

## Executive summary

- **Total ad spend to date: $4,021** (Google $2,950 · Facebook $1,071).
- **Google:** ~51 conversions per location at **$25.84 (WP)** / **$32.01 (POL)** cost-per-conversion.
  50%-off beats BOGO at both locations; **POL's budget is on the weaker campaign** — quick fix.
- **Facebook:** **298 leads** and **3,313 landing-page views** at ~**$3.25–$3.73 / lead** — roughly
  8× cheaper per action than Google search. Retargeting is barely switched on = biggest upside.
- **Live GHL (pulled today):** opted-in audience **258** (POL 112 · WP 146); **166 new offer-leads
  in the last 30 days**; **18 redemptions tracked** in GHL. POL is surging (57 new leads in 7 days).
- **The gap for the corporate story:** provable **in-store redemptions** and **booked parties**.
  GHL shows 18 tracked redemptions and 0 parties; the full, dated numbers live in William's
  verification backend + Aluvii and are the last piece needed (see §5).

---

## 1. Data sources & confidence (so every number is backable)

| Data | Source | Confidence |
|---|---|---|
| Google/Facebook spend, clicks, conv, CPL | Platform CSV exports (all-time) | **High** (exact) |
| Ad spend/CPA split by month/week | — not in the exports (no date column) | **Pending** dated re-export |
| GHL audience, tags, leads-by-window, custom fields | Live API pull, 2026-07-14 03:43 UTC | **High** (live) |
| In-store redemptions (by code, dated) | William's verification backend | **Pending** from William |
| Party bookings (`BDAY25`) | Aluvii (no API) | **Pending** manual count |

---

## 2. Ad performance to date

### Google Ads (Search) — all-time / pilot

| Location | Campaign | Daily budget | Spend | Clicks | CPC | Conv. | Cost/conv. |
|---|---|---:|---:|---:|---:|---:|---:|
| POL | 50% Off — Pointe Orlando | $7 | $871.75 | 791 | $1.10 | 30.67 | **$28.43** |
| POL | BOGO — Pointe Orlando | $10 | $760.51 | 615 | $1.24 | 20.33 | $37.40 |
| WP | 50% Off — Winter Park | $10 | $803.63 | 2,152 | $0.37 | 38.17 | **$21.06** |
| WP | BOGO — Winter Park | $7 | $514.36 | 748 | $0.69 | 12.83 | $40.08 |
| **POL total** | | | **$1,632.26** | 1,406 | $1.16 | 51.00 | $32.01 |
| **WP total** | | | **$1,317.99** | 2,900 | $0.45 | 51.00 | $25.84 |

*Note: both accounts report exactly 51.00 conversions — an unlikely coincidence, and a known GHL
form-tracking bug under-fired the conversion event. Treat Google "conversions" as directional. They
are **not** the same as GHL leads (§3), which aggregate every channel.*

### Facebook / Instagram — all-time / pilot

| Campaign | Status | Spend | Impr. | Reach | Clicks | LP views | Leads | Cost/lead |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| MJ WP — Spring 2026 | active | $662.90 | 81,480 | 49,434 | 3,627 | 1,814 | 204 | $3.25 |
| MJ PO — Spring 2026 | active | $350.66 | 59,691 | 33,990 | 2,337 | 1,292 | 94 | $3.73 |
| MJ - POL Spring 2026 | inactive | $57.21 | 8,501 | 7,098 | 338 | 207 | 0 | — |
| **Total** | | **$1,070.77** | 149,672 | ~90,522 | 6,302 | 3,313 | 298 | ~$3.59 |

*FB campaigns were optimised for landing-page views (3,313) with leads (298) as a secondary result.
Archive the dead "MJ - POL Spring 2026" line so it stops muddying reporting.*

### Totals
**Ad spend $4,021.02** — Google $2,950.25 · Facebook $1,070.77.

### What to change (priority)
1. **POL Google:** shift budget to 50%-off (its winner is capped at $7 while the weaker BOGO gets $10).
2. **WP Google:** raise budget — it's the efficient account ($0.45 CPC) and flagged "limited by budget".
3. **Facebook:** scale retargeting (warm audiences); weight prospecting to WP; archive the dead campaign.
4. **Verify the GHL conversion event fires** before trusting Google cost-per-conversion.

---

## 3. Live GHL account data (both sub-accounts, pulled 2026-07-14)

Both accounts connected successfully.

| Metric | Pointe Orlando | Winter Park |
|---|---:|---:|
| Opted-in audience — `voucher-delivered` (all-time) | 112 | 146 |
| Unsubscribed | 0 | 0 |
| New offer-leads — last 30 days¹ | 74 | 92 |
| New offer-leads — last 7 days¹ | **57** | 18 |
| Birthday leads tagged | 110 | 145 |
| Parties booked (GHL tag) | 0 | 0 |
| Redemptions tracked — `promo-redeemed` (all-time) | 12 | 6 |
| Child-birthday field type | DATE (full date) | NUMERICAL (month only) |

¹ *"New offer-leads" = contacts tagged from the BOGO / half-price / 50%-off funnels, counted by date
added. This is distinct from the all-time `voucher-delivered` audience above, and from Google's
conversion count.*

**Reading it:**
- **Opted-in audience is ~258, not 20k.** The 20k is the raw waiver DB; ~258 have opted in. Paid
  party retargeting should use the **full list + site-visitor pixel audiences**, not just these 258.
- **POL is surging** — 57 of its 74 last-30-day offer-leads landed in the **last 7 days**.
- **166 new offer-leads in 30 days** across both locations (POL 74 + WP 92).
- **0 unsubscribes** at both — worth confirming the unsubscribe tag is actually wired.

---

## 4. By period (the month/week view)

**GHL new offer-leads — live, exact:**

| Window | POL | WP | Total |
|---|---:|---:|---:|
| Last 7 days | 57 | 18 | 75 |
| Last 30 days | 74 | 92 | 166 |
| Month-to-date (Jul) | 61 | 35 | 96 |

**POL Google impressions by month — from the daily export (impressions only):**

| Period | POL Google impressions |
|---|---:|
| Month 1 (Apr 27–May 26) | 11,234 |
| Month 2 (May 27–Jun 25) | 8,468 |
| Month 3 (Jun 26–Jul 13, partial) | 6,314 |
| Last 7 days (Jul 7–13) | 2,224 |

**Ad spend / conversions / CPA by month:** *not derivable from the current exports* — the Google and
Facebook reports are "all-time" with no date column. To fill this precisely, re-export Google Ads +
Meta with the date range set to **Last 7 days** and each month (2 min each), **or** add the Meta +
Google API tokens as GitHub secrets and the live pull produces these windows automatically (GHL
already does).

---

## 5. The redemption picture — and what only you (William) can close

Redemptions are the number Michael needs, and here's exactly where it stands:

- GHL shows **18 redemptions tracked** via `promo-redeemed` (POL 12 · WP 6). The standard
  `redeemed-{loc}` tag is **empty**.
- All 18 are on contacts **created more than 30 days ago**, so they show **0 in the last-30-day
  window** — GHL is storing the redeemed *tag* but **not a redemption date**, so we can't yet report
  redemptions "this week / this month" from GHL alone.

**To complete Michael's numbers, please send:**
1. **Code redemptions** from the verification backend — generated vs redeemed in-store, **by code**
   (`WELCOME` / `BOGO/` / `50% off` / `FJP/`) and **by location**, for **last 30 days** and **last 7
   days** (with dates, so we can show the trend).
2. **`BDAY25` party redemptions in Aluvii** — last 30d + 7d, and total booked parties.
3. **Which tag/field marks a redemption** (is `promo-redeemed` the complete set of 18?), and can it
   carry a redemption **date** going forward?
4. **Confirm the GHL conversion/form-tracking bug is fixed.**
5. **Birthday automation** — is it live, at what cadence, and POL-only? (So our sends don't double up.)

---

## 6. Parties push — next 7 & 30 days (WILBA scope: lead reactivation / retargeting)

Original focus was weekday walk-ins, so parties haven't been advertised — and "birthday parties
Orlando" is $25–40 CPC on Google, so paid search is out. Plan (launching this week):
- **$25-off (`BDAY25`) as a Facebook/IG retargeting campaign** to warm audiences — the **full email
  list + site-visitor pixel**, not just the ~258 opted-in.
- **Post-visit "book a party" upsell** on owned email/SMS.
- Everything drives to the booking + `BDAY25` so parties are trackable.
- **Gate:** please confirm `BDAY25` is live and redeemable in Aluvii before launch.

---

## 7. The corporate story (once your redemption + party data lands)

**Spend → audience → redemptions → parties.** We now have the top of the funnel verified: **$4,021
spend**, ~298 FB leads, **166 new GHL leads in 30 days**, **258 opted-in**, **18 tracked
redemptions**. Your dated redemption + `BDAY25` numbers turn that into the ROI slide Michael needs:
*"$X spend → Y in-store redemptions → Z parties vs last year."*

*GHL figures: live API pull 2026-07-14. Ad figures: platform exports (pilot-to-date, USD).*
