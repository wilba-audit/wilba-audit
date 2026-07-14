# Monkey Joe's — Pilot Results Report (for William)

**From:** Jess / WILBA · **Date:** 2026-07-14
**Purpose:** Compile marketing results for Michael's corporate presentation, and pull together the
full funnel (ad spend → codes → redemptions). Michael wants to show parties beating last year;
we're launching a party push now (see end).

---

## 1. Ad performance — pilot to date (from platform exports)

### Google Ads (Search)

| Location | Campaign | Daily budget | Spend | Clicks | CPC | Conv. | Cost/conv. |
|---|---|---:|---:|---:|---:|---:|---:|
| POL | 50% Off — Pointe Orlando | $7 | $871.75 | 791 | $1.10 | 30.67 | **$28.43** |
| POL | BOGO — Pointe Orlando | $10 | $760.51 | 615 | $1.24 | 20.33 | $37.40 |
| WP | 50% Off — Winter Park | $10 | $803.63 | 2,152 | $0.37 | 38.17 | **$21.06** |
| WP | BOGO — Winter Park | $7 | $514.36 | 748 | $0.69 | 12.83 | $40.08 |
| **POL total** | | | **$1,632.26** | 1,406 | $1.16 | 51.0 | $32.01 |
| **WP total** | | | **$1,317.99** | 2,900 | $0.45 | 51.0 | $25.84 |

### Facebook / Instagram

| Campaign | Status | Spend | Impr. | Reach | Clicks | LPV | Leads | CPL |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| MJ WP — Spring 2026 | active | $662.90 | 81,480 | 49,434 | 3,627 | 1,814 | 204 | $3.25 |
| MJ PO — Spring 2026 | active | $350.66 | 59,691 | 33,990 | 2,337 | 1,292 | 94 | $3.73 |
| MJ - POL Spring 2026 | inactive | $57.21 | 8,501 | 7,098 | 338 | 207 | 0 | — |
| **FB total** | | **$1,070.77** | 149,672 | ~90,522 | 6,302 | 3,313 | 298 | ~$3.59 |

### Totals
- **Total ad spend (pilot): $4,021.02** — Google $2,950.25 · Facebook $1,070.77
- **Google:** 102 conversions @ ~$28.9 blended cost/conv
- **Facebook:** 298 leads + 3,313 landing-page views @ ~$3.59/lead

### Read on the data
- **50%-off outperforms BOGO on Google at both locations** — but **POL's budget is on the wrong
  campaign** (winner 50%-off capped at $7, weaker BOGO at $10). Recommend flipping.
- **WP is the efficient account** (CPC $0.45 vs POL $1.16) and is **budget-limited** → room to scale.
- **FB leads are ~8× cheaper per action than Google** — retargeting is the underused lever.

---

## 2. What I need from you (William) to complete Michael's report

The ad numbers above are only half the funnel. The number Michael needs for corporate is
**provable in-store redemptions + parties booked** — and that data lives in your systems. Please send:

1. **Code redemptions** (from the verification-page backend): **codes generated vs redeemed
   in-store**, split **by code type** (`WELCOME`, `BOGO/`, `50% off`, `FJP/`) and **by location**,
   for **last 30 days** and **last 7 days**.
2. **`BDAY25` party redemptions in Aluvii** (our only party attribution) — **last 30d + last 7d**,
   and total booked parties if you can pull it.
3. **Confirmation the GHL form-tracking / conversion bug is fixed** — it was showing **0
   redemptions** earlier; I need to know redemptions are firing before I trust cost-per-redemption.
4. **Any GHL-native metrics** you already have: new opt-ins / SMS list growth, and whether the
   birthday automation is sending (so we don't double up with the drip).

---

## 3. By period (month 1 / month 2 / last week)

**Honesty note on the source data:** the Google and Facebook exports are **"All time" aggregates —
no date column**, so **spend and CPA cannot be split by month or week from them.** The only dated
file is a daily **impressions** series, and it's **Pointe Orlando's Google account only**
(its 26,016 total matches the POL Google report). So the by-period view below is **POL Google
impressions**; the spend/CPA-by-period cells need a dated re-export (see the ask below).

**Ads live from ~Apr 27, 2026** (kickoff was March; ramp took a few weeks).

| Period | POL Google impressions | Spend | Conv. | CPA |
|---|---:|---:|---:|---:|
| Month 1 (Apr 27–May 26) | 11,234 | _pending dated export_ | _pending_ | _pending_ |
| Month 2 (May 27–Jun 25) | 8,468 | _pending_ | _pending_ | _pending_ |
| Month 3 (Jun 26–Jul 13, partial) | 6,314 | _pending_ | _pending_ | _pending_ |
| Last 7 days (Jul 7–13) | 2,224 | _pending_ | _pending_ | _pending_ |

*Read: POL Google reach peaked in Month 1 and has tapered — partly the partial current month, partly
choppy delivery (62 of 88 days had impressions). Worth checking budget pacing.*

**To fill the spend / conv / CPA columns** (2 min each in the platform UIs): re-export **Google Ads**
and **Meta** with the date range set to each window — or run the live pull
(`fetch_consolidated_reporting.py` already computes today / 7d / 30d / MTD). Drop those in and this
table becomes exact for both locations and both platforms.

---

## 4. Parties push — so we're aligned

Original pilot goal was **weekday walk-ins**, so we haven't advertised parties. Michael now needs
parties to beat last year for the corporate deck. Plan (launching this week):
- **$25-off (`BDAY25`) as a Facebook/IG retargeting campaign** to the warm audience — Google party
  keywords are $25–40 CPC, so paid search is out; retargeting warm users at ~$3–4/lead is the play.
- **Birthday reminders + post-visit party upsell** on owned email/SMS.
- Everything drives to the booking + `BDAY25` so parties are trackable.
- **Ask:** please confirm `BDAY25` is live and redeemable in Aluvii before we launch.

---

## 5. The corporate story (once your data lands)

**Spend → audience → redemptions → parties.** We have the top of that funnel (spend, ~102 Google
conversions, ~298 FB leads, opt-ins). Your redemption + `BDAY25` numbers close it into an ROI story:
*"$X spend drove Y in-store redemptions and Z parties vs last year."* That's the slide Michael needs.
