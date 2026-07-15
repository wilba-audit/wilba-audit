# Monkey Joe's — Google Ads Audit

**Prepared by:** WILBA · **Date:** 2026-07-14 · **Period:** pilot to date (live ~Apr 27 → Jul 14, ~11 weeks)
**Accounts:** Pointe Orlando (POL) · Winter Park (WP) · **Spend paid by Michael direct to Google**

---

## 1. Snapshot

| | Spend | Impr. | Clicks | CTR | CPC | Conv. | Cost/conv. |
|---|---:|---:|---:|---:|---:|---:|---:|
| **Pointe Orlando** | $1,632.26 | 26,016 | 1,406 | 5.40% | $1.16 | 51.0 | $32.01 |
| **Winter Park** | $1,317.99 | 53,187 | 2,900 | 5.45% | $0.45 | 51.0 | $25.84 |
| **Total (gross)** | **$2,950.25** | 79,203 | 4,306 | ~5.4% | $0.69 | 102 | ~$28.9 |

**Ad credits:** Google issued **$500 per account ($1,000 total)** → **net spend ~$1,950**.

---

## 2. Campaign detail

| Location | Campaign | Bid strategy | Daily budget | Spend | Clicks | CPC | Conv. | Cost/conv. | Opt. score |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|
| POL | 50% Off | Max conversions | **$7** | $871.75 | 791 | $1.10 | 30.67 | **$28.43** | 66 |
| POL | BOGO | Max conversions | **$10** | $760.51 | 615 | $1.24 | 20.33 | $37.40 | 77 |
| WP | 50% Off | Max clicks | **$10** | $803.63 | 2,152 | $0.37 | 38.17 | **$21.06** | 91 |
| WP | BOGO | Max clicks | **$7** | $514.36 | 748 | $0.69 | 12.83 | $40.08 | 80 |

**Reach over time (POL impressions):** Apr 3,123 · May 10,541 · Jun 7,895 · Jul 4,457 (to 13th). Delivery is
**choppy** — 62 of 88 days had impressions — so learning and traffic are start-stop.

---

## 3. Findings

1. **50%-off beats BOGO at both locations.** WP: $21.06 vs $40.08/conv. POL: $28.43 vs $37.40/conv. The
   half-price offer is the efficiency winner everywhere on search.
2. **POL's budget is allocated backwards.** Its winner (50%-off) is capped at **$7/day** while the weaker BOGO
   gets **$10/day**. Flipping this is free extra conversions.
3. **Winter Park is the efficient, under-fed account.** CPC $0.45 vs POL's $1.16, and both WP campaigns are
   "Eligible (Limited) — limited by budget." It's leaving cheap volume on the table.
4. **Conversion tracking is unreliable.** Both accounts show *exactly* 51.00 conversions, and a GHL form-tracking
   bug under-fired the event. Treat Google "conversions" as directional until the event is verified firing.
   (GHL's own lead/redemption counts are the trustworthy figures — see the GHL audit.)
5. **Delivery continuity is weak.** Smoothing to steady daily spend will help both the algorithm and walk-in flow.
6. **Parties correctly excluded from search.** "Birthday parties Orlando" is $25–40 CPC — too expensive; parties
   belong on retargeting/owned channels (see the FB audit).

---

## 4. Recommendations

- **Immediate:** flip POL budget to 50%-off (make it the $10, BOGO the $7 or lower).
- **Scale:** raise WP's total budget — it's efficient and budget-limited; push 50%-off first.
- **Fix measurement:** confirm the GHL conversion event fires before trusting cost-per-conversion.
- **Smooth delivery** to continuous daily spend.
- **Keep BOGO live but secondary** — it still converts, just less efficiently.

---

## 5. Raise with William
- Is the GHL/website conversion event now firing correctly (the form bug)? Until it is, Google can't optimise well.
- Confirm whether the $500×2 Google credits are fully applied / any remaining.
- Google Ads API access (dev token) — needed to pull live spend/CPA into the weekly report automatically.
