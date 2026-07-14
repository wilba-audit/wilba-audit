# Monkey Joe's — Pilot Results Report

**From:** Jess / WILBA · **Date:** 2026-07-14 · **For:** William (Lanyu) → corporate review
**Locations:** Pointe Orlando (POL) · Winter Park (WP)
_All GHL figures are live, pulled from both sub-accounts 2026-07-14. Ad figures are platform exports (pilot-to-date, USD)._

---

## Executive summary

- **Ad spend to date: $4,021** (Google $2,950 · Facebook $1,071).
- **Redemptions tracked in GHL: 74** — POL 14 (BOGO 2 · half 5 · welcome 7), **WP 60** (half 20 · welcome 40). WP is doing the heavy lifting, mostly on the Welcome voucher.
- **Opted-in audience: 258** (POL 112 · WP 146), sitting inside a large marketing DB (~13k POL / ~37k WP).
- **Recent campaign activity is strong:** the 4th-of-July "BANANAS/STARS" email reached **253** (POL 111 · WP 142); a May nudge campaign hit 227 SMS + 92 email; a reactivation sequence has worked ~2,500/location.
- **New offer-leads last 30 days: 166** (POL 74 · WP 92); POL is surging (57 in the last 7 days).
- **Parties booked (GHL): 0** — parties haven't been advertised yet; the plan (§6) is a $25-off FB retargeting push. Voice agent has already fielded ~25 inbound calls tagged "party".

---

## 1. Data sources & confidence

| Data | Source | Confidence |
|---|---|---|
| Google / Facebook spend, clicks, conv, CPL | Platform CSV exports (all-time) | **High** (exact) |
| Ad spend/CPA split by month/week | Not in the exports (no date column) | Pending dated re-export |
| GHL audience, redemptions-by-code, campaign sends, DB size | **Live API pull, 2026-07-14** | **High** (GHL's own counts) |
| Redemptions split by week/month | GHL stores the tag, not a redemption date | Pending (needs date on the tag) |
| Party bookings (`BDAY25`, Aluvii) | Aluvii (no API) | Pending manual count |

---

## 2. Ad performance to date

### Google Ads (Search)

| Location | Campaign | Daily budget | Spend | Clicks | CPC | Conv. | Cost/conv. |
|---|---|---:|---:|---:|---:|---:|---:|
| POL | 50% Off | $7 | $871.75 | 791 | $1.10 | 30.67 | **$28.43** |
| POL | BOGO | $10 | $760.51 | 615 | $1.24 | 20.33 | $37.40 |
| WP | 50% Off | $10 | $803.63 | 2,152 | $0.37 | 38.17 | **$21.06** |
| WP | BOGO | $7 | $514.36 | 748 | $0.69 | 12.83 | $40.08 |
| **POL total** | | | **$1,632.26** | 1,406 | $1.16 | 51.00 | $32.01 |
| **WP total** | | | **$1,317.99** | 2,900 | $0.45 | 51.00 | $25.84 |

50%-off beats BOGO at both locations. WP is the efficient, budget-limited account. *(Both accounts show
exactly 51 conversions and a GHL form-bug under-fired the event — treat Google "conversions" as directional;
they are not the same as GHL leads or redemptions.)*

### Facebook / Instagram

| Campaign | Status | Spend | Reach | Clicks | LP views | Leads | Cost/lead |
|---|---|---:|---:|---:|---:|---:|---:|
| MJ WP — Spring 2026 | active | $662.90 | 49,434 | 3,627 | 1,814 | 204 | $3.25 |
| MJ PO — Spring 2026 | active | $350.66 | 33,990 | 2,337 | 1,292 | 94 | $3.73 |
| MJ - POL Spring 2026 | inactive | $57.21 | 7,098 | 338 | 207 | 0 | — |
| **Total** | | **$1,070.77** | ~90,522 | 6,302 | 3,313 | 298 | ~$3.59 |

FB leads are ~8× cheaper per action than Google search. Retargeting is barely switched on = biggest upside.

**Total ad spend: $4,021.02** (Google $2,950.25 · Facebook $1,070.77).

---

## 3. Live GHL account data (both sub-accounts, 2026-07-14)

| Metric | Pointe Orlando | Winter Park |
|---|---:|---:|
| Total contacts in the DB | ~13,208 | ~37,052 |
| Opted-in — `voucher-delivered` | 112 | 146 |
| Vouchers issued → delivered (funnel) | 158 → 112 | 236 → 146 |
| **Redemptions tracked (by code)** | **14** | **60** |
| — BOGO / half / welcome | 2 / 5 / 7 | 0 / 20 / 40 |
| New offer-leads — last 30 days | 74 | 92 |
| New offer-leads — last 7 days | **57** | 18 |
| SMS unsubscribes (`sms-unsub`) | 3 | 7 |
| Birthday cohort enrolled (`bday-start` 6 Jul) | 112 | 145 |
| Parties booked (GHL tag) | 0 | 0 |
| Voice-agent inbound calls (tagged "party") | 12 | 13 |

**Campaign sends (from GHL cohort tags):**
- **4th-of-July "STARS/BANANAS" email (~30 Jun):** POL 111 · WP 142 (**253 total**). SMS leg not tagged/sent.
- **May nudge campaign:** SMS 227 (POL 101 · WP 126) · Email 92 (POL 54 · WP 38).
- **Reactivation sequence** (`reactivate-wk1-*`, 5 daily batches): ~2,500 per location.

**Reading it:**
- **74 redemptions is the real provable-visits number so far**, and it's mostly WP (60) — the Welcome voucher (40) and half-price (20) are the workhorses. POL is lighter (14) and BOGO barely redeems (2).
- **Opted-in audience is ~258**, sitting inside a big DB (~50k combined) — so paid party retargeting should use the **full list + site-visitor pixel**, not just opt-ins.
- **POL is surging** — 57 of its 74 last-30-day offer-leads landed in the last 7 days.

---

## 4. By period (month / week)

**GHL new offer-leads — live, exact:**

| Window | POL | WP | Total |
|---|---:|---:|---:|
| Last 7 days | 57 | 18 | 75 |
| Last 30 days | 74 | 92 | 166 |
| Month-to-date (Jul) | 61 | 35 | 96 |

**POL Google impressions by month (impressions-only export):** Month 1 (Apr 27–May 26) 11,234 · Month 2
(May 27–Jun 25) 8,468 · Month 3 (Jun 26–Jul 13) 6,314 · Last 7 days 2,224.

**Ad spend / CPA by month:** not derivable from the current "all-time" exports — re-export Google + Meta by
date range, or add the Meta/Google API tokens as secrets and the live pull produces these windows (GHL already does).

**Redemptions by week/month:** GHL stores the redeemed *tag* but not a redemption *date*, so the 74 can't yet be
split by week. Adding a date/timestamp on redemption (your side) would let us trend it.

---

## 5. Redemptions — detail & one reconciliation

Redemptions tracked by code (deduping the `x-redeemed` / `redeemed-x` tag pair, which are the same event):

| Code | POL | WP | Total |
|---|---:|---:|---:|
| Welcome ($25 voucher) | 7 | 40 | **47** |
| Half-price | 5 | 20 | **25** |
| BOGO | 2 | 0 | **2** |
| **Total** | **14** | **60** | **74** |

**One thing to confirm:** there's also a separate `promo-redeemed-{loc}` tag (POL 12 · WP 6 = 18). It may be an
earlier/generic redemption tag that overlaps the by-code tags above — can you confirm whether it's additional or
a subset, so we don't double-count? And can redemptions carry a **date** going forward (for the weekly trend)?

---

## 6. Parties push — next 7 & 30 days (WILBA scope: lead reactivation / retargeting)

Parties haven't been advertised (weekday walk-ins were the focus, and "birthday parties Orlando" is $25–40 CPC on
Google). Plan (launching this week): **$25-off (`BDAY25`) as a Facebook/IG retargeting campaign** to the **full
list + site-visitor pixel** (not just the ~258 opt-ins), plus a **post-visit "book a party" upsell** on owned
email/SMS. Everything drives to the booking + `BDAY25` so parties are trackable. Voice agent has already fielded
~25 party-tagged inbound calls — worth making sure those convert.
- **Gate:** please confirm `BDAY25` is live and redeemable in Aluvii before launch.

---

## 7. The corporate story

**Spend → audience → redemptions → parties.** Verified so far: **$4,021 spend**, ~298 FB leads, **166 new GHL
leads in 30 days**, **258 opted-in**, and **74 tracked in-store redemptions** (WP 60 · POL 14). The last piece is
**`BDAY25` party bookings from Aluvii** (your side) — add that and it's a clean ROI slide:
*"$X spend → 74+ redemptions → Z parties vs last year."*
