# Monkey Joe's — Google & Facebook Ads Audit (Pilot to date)

**Prepared by:** WILBA · **Date:** 2026-07-14 · **Source:** exported campaign reports (all-time / pilot window ~Apr–Jul 2026)
**Locations:** Pointe Orlando (POL) · Winter Park (WP)

> Data comes from the four exported CSVs in the client archive (Google "Campaign report"
> exports for each account + the Meta "Charles Carter Campaigns" export + an impressions
> time-series). Where the exports and the call transcripts disagree, that's called out.

---

## 1. Headline numbers

| Platform | Location | Spend | Impressions | Clicks | CTR | Conv./Leads | Cost / result |
|---|---|---:|---:|---:|---:|---:|---:|
| Google | POL | $1,632.26 | 26,016 | 1,406 | 5.40% | 51.0 conv | $32.01 |
| Google | WP | $1,317.99 | 53,187 | 2,900 | 5.45% | 51.0 conv | $25.84 |
| Meta | POL (active) | $350.66 | 59,691 | 2,337 | — | 94 leads | $3.73 / lead |
| Meta | WP (active) | $662.90 | 81,480 | 3,627 | — | 204 leads | $3.25 / lead |
| Meta | POL (old, inactive) | $57.21 | 8,501 | 338 | — | 207 LPV | $0.28 / LPV |

**Totals:** ~**$4,021 ad spend** across the pilot (Google ~$2,950 · Meta ~$1,071).
Google ~**102 conversions**; Meta ~**298 leads** + 3,313 landing-page views.

---

## 2. Google Ads — findings

**Campaign-level (all-time):**

| Account | Campaign | Daily budget | Spend | Clicks | CPC | Conv. | Cost/conv. |
|---|---|---:|---:|---:|---:|---:|---:|
| WP | 50% Off — Winter Park | $10 | $803.63 | 2,152 | $0.37 | 38.17 | **$21.06** |
| WP | BOGO — Winter Park | $7 | $514.36 | 748 | $0.69 | 12.83 | $40.08 |
| POL | 50% Off — Pointe Orlando | $7 | $871.75 | 791 | $1.10 | 30.67 | **$28.43** |
| POL | BOGO — Pointe Orlando | $10 | $760.51 | 615 | $1.24 | 20.33 | $37.40 |

**What the data says:**
1. **50%-off wins at BOTH locations.** It beats BOGO on cost-per-conversion everywhere —
   WP: $21.06 vs $40.08 (nearly 2×); POL: $28.43 vs $37.40. *This contradicts the call note
   "BOGO better at Winter Park"* — which was likely about Facebook or in-store, not Google
   search. On Google, 50%-off is the clear efficiency leader.
2. **POL budget is allocated backwards.** POL's winner (50% Off) is capped at **$7/day** while
   its weaker campaign (BOGO) gets **$10/day**. Flip it. Estimated effect: more conversions for
   the same spend.
3. **WP is far cheaper than POL.** WP CPC averages **$0.45** vs POL's **$1.16** — POL is the more
   competitive/touristy market. WP delivered ~2× the clicks for ~20% less money.
4. **WP is "Limited by budget"** (both campaigns flagged Eligible-Limited). It's leaving cheap
   volume on the table — the strongest place to add budget.
5. **Conversion tracking is suspect.** Both accounts report *exactly* 51.00 conversions — an
   unlikely coincidence, and the calls documented a **GHL form-tracking bug** that under-fired the
   conversion event. Treat Google "conversions" as directional, not gospel, until the form event
   is verified firing.

**Recommended Google moves (in priority order):**
- **POL:** shift budget from BOGO → 50% Off (make 50% Off the $10, BOGO the $7 or lower).
- **WP:** raise total budget — it's the efficient, budget-limited account. Push 50% Off first.
- Verify the GHL conversion event is firing before trusting cost/conv.
- Keep BOGO live but secondary; it still converts, just less efficiently.
- Do **not** run paid search for birthday parties — party keywords are **$25–$40 CPC** (per
  Michael); parties should come from email/SMS/retargeting/partnerships (see the strategy doc).

---

## 3. Meta (Facebook / Instagram) — findings

| Campaign | Status | Spend | Impr. | Reach | Clicks | LPV | Leads | Cost/lead |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| MJ WP — Spring 2026 | active | $662.90 | 81,480 | 49,434 | 3,627 | 1,814 | 204 | $3.25 |
| MJ PO — Spring 2026 | active | $350.66 | 59,691 | 33,990 | 2,337 | 1,292 | 94 | $3.73 |
| MJ - POL Spring 2026 | inactive | $57.21 | 8,501 | 7,098 | 338 | 207 | — | ($0.28/LPV) |

**What the data says:**
1. **Meta leads are cheap** — ~$3.25–$3.73 each, roughly **8–10× cheaper per action** than Google's
   cost-per-conversion. Different event definitions (Meta "lead"/opt-in vs Google conversion), but
   the top-of-funnel efficiency is strong.
2. **WP outperforms again** — more reach, more leads, lower cost-per-lead. Consistent with Google:
   **WP is the higher-efficiency market; POL is pricier.**
3. **Retargeting is barely tapped.** Per the calls, retargeting (email lists + site visitors + FB
   custom audiences) is the lever Jess expects to "move the needle," and it had only ~4 days of
   runtime at the last check-in. This is the biggest near-term upside on Meta.
4. **Clean-up:** the old **"MJ - POL Spring 2026" (inactive)** campaign is a leftover — archive it
   so reporting isn't muddied by a dead line item.

**Recommended Meta moves:**
- **Scale retargeting** across both locations (warm audiences convert cheapest).
- Weight prospecting budget toward **WP** (cheaper leads) while keeping POL retargeting on.
- Mirror the Google insight: test **50%-off creative** prominently — it's the proven winner.
- Archive the dead POL campaign.

---

## 4. Delivery continuity (time-series)

The impressions time-series (Apr 17 – Jul 13) shows **choppy delivery** — clusters of active days
separated by strings of zero-impression days. Whatever the cause (budget exhaustion, manual
on/off, scheduling), **continuous delivery beats stop-start** for both algorithms' learning and for
steady walk-in traffic. Recommend smoothing to consistent daily delivery.

---

## 5. The number that actually matters — and why it's missing

Michael's real KPI is **provable in-store redemptions / walk-ins**, not platform conversions. Right
now that number is unreliable because:
- Redemptions are recorded on **William's external verification page**, not in the ad platforms.
- **Party** attribution depends on **`BDAY25` redeemed in Aluvii** (no API → manual).
- A **GHL form-tracking bug** meant ~0 provable in-store redemptions at the last documented check.

**So the funnel we can prove today is:** ad spend → clicks → GHL codes generated (109 at last
count) → opt-ins (249 SMS) → **[redemption data lives in William's system / Aluvii]** → walk-in.
Closing that last gap (getting redemption exports from William + BDAY25 counts from Aluvii into the
weekly report) is the single highest-value reporting fix. It's what turns this audit into a
revenue story for the corporate pitch.

---

## 6. Priority action list

1. **POL Google:** flip budget to 50%-off (its winner). *(quick, high impact)*
2. **WP Google:** raise budget — efficient and budget-limited.
3. **Meta:** scale retargeting both locations; weight prospecting to WP; archive dead POL campaign.
4. **Verify** the GHL conversion/redemption event fires (unblocks trustworthy cost-per-result).
5. **Wire redemption data** (William's verification export + Aluvii BDAY25) into the weekly report.
6. **Smooth delivery** to continuous daily spend.
7. **Keep parties out of paid search**; drive them via the birthday strategy doc.

*Numbers here are from the exported reports and will be refreshed live once the account APIs are
reachable (see `/mj-ads`). Figures are pilot-to-date, USD.*
