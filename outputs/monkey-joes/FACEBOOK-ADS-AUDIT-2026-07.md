# Monkey Joe's — Facebook / Instagram (Meta) Ads Audit

**Prepared by:** WILBA · **Date:** 2026-07-14 · **Period:** pilot to date ("Spring 2026" campaigns)
**Accounts:** Pointe Orlando (POL) · Winter Park (WP)

---

## 1. Snapshot

| Campaign | Status | Spend | Impr. | Reach | Clicks | LP views | Leads | Cost/lead |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| MJ WP — Spring 2026 | active | $662.90 | 81,480 | 49,434 | 3,627 | 1,814 | 204 | **$3.25** |
| MJ PO — Spring 2026 | active | $350.66 | 59,691 | 33,990 | 2,337 | 1,292 | 94 | $3.73 |
| MJ - POL Spring 2026 | inactive | $57.21 | 8,501 | 7,098 | 338 | 207 | 0 | — |
| **Total** | | **$1,070.77** | 149,672 | ~90,522 | 6,302 | 3,313 | 298 | **~$3.59** |

Campaigns are optimised for **landing-page views** (3,313), with **leads** (298) as the secondary result.

---

## 2. Findings

1. **Meta leads are cheap — ~$3.25–$3.73 each.** That's roughly **8× cheaper per action** than a Google search
   conversion ($26–$32). Different events, but the top-of-funnel efficiency is strong.
2. **Winter Park outperforms again** — more reach, more leads, lower cost-per-lead — consistent with the Google
   picture: **WP is the higher-efficiency market; POL is pricier.**
3. **Retargeting is barely switched on.** Per the pilot calls it had only ~4 days of runtime at the last
   check-in. Retargeting the warm audiences (site visitors, the email/SMS list, past redeemers) is the single
   biggest untapped lever — and the natural engine for the parties push.
4. **A dead campaign is muddying reporting.** "MJ - POL Spring 2026" (inactive, $57, 0 leads) should be archived.
5. **Reach is real** — ~90k people reached, 149k impressions — so brand presence is building (Michael's wife
   noted the uptick in FB activity; 5-star reviews rose over the same period).

---

## 3. The parties play (this is where FB earns its keep)

Parties don't work on Google search ($25–40 CPC), but they're ideal for **Meta retargeting**:
- Build audiences from **site visitors + the email/SMS list + past redeemers**, and run the **$25-off `BDAY25`**
  offer to them. Warm, high-intent, ~$3–4/lead.
- Add a **post-visit "book a party" nudge** and lookalikes off the redeemer list.
- The AI voice agent has already fielded **~25 inbound calls tagged "party"** — warm demand is already there.

---

## 4. Recommendations

- **Scale retargeting** across both locations (highest-ROI audience).
- **Weight prospecting to WP** (cheaper leads); keep POL retargeting on.
- **Mirror the Google insight:** lead with **50%-off creative** — the proven winner — for walk-in campaigns.
- **Archive** the dead POL campaign.
- **Launch the `BDAY25` party retargeting** this week (pending Aluvii `BDAY25` confirmation).

---

## 5. Raise with William / setup
- **Meta API tokens as GitHub secrets** (`META_ACCESS_TOKEN`, `META_AD_ACCOUNT_POL/WP`) — so live FB spend/leads
  flow into the weekly report automatically (currently reporting is from CSV exports only).
- Confirm the **Pixel + Conversions API** are firing on the booking/redemption pages so retargeting audiences
  and purchase events are complete.
- Any **Meta ad credits** on the accounts? (Google gave $1,000; worth checking Meta.)
