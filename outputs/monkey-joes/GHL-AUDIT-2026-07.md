# Monkey Joe's — GoHighLevel (GHL) Account Audit

**Prepared by:** WILBA · **Date:** 2026-07-14 · **Source:** live API pull, both sub-accounts (authoritative tag counts)
**Accounts:** Pointe Orlando (POL, `xlzFHtujfHhegk3xc9q2`) · Winter Park (WP, `yaRfypmZfcGDtpGEz3Gz`)

---

## 1. Account size & the opt-in funnel

| Stage | POL | WP | Total |
|---|---:|---:|---:|
| Contacts in the database | ~13,208 | ~37,052 | ~50,260 |
| Vouchers issued (`promo-issued`) | 158 | 236 | 394 |
| Opt-in pending | 107 | 146 | 253 |
| **Opted-in (`voucher-delivered`)** | **112** | **146** | **258** |
| New offer-leads · last 30 days | 74 | 92 | 166 |
| New offer-leads · last 7 days | **57** | 18 | 75 |

**Read:** the marketing DB is large (~50k), but the **opted-in, contactable audience is ~258**. POL is surging —
57 of its 74 last-30-day leads landed in the past week. For paid party retargeting, use the **full list +
site-visitor pixel**, not just the 258.

---

## 2. Redemptions — the provable-visits number

**92 unique redemptions tracked in GHL** (resolved by unioning every redemption tag, so nothing is double-counted
or dropped):

| Code | POL | WP | Total |
|---|---:|---:|---:|
| Welcome ($25 voucher) | 7 | 40 | **47** |
| Half-price | 5 | 20 | **25** |
| BOGO | 2 | 0 | **2** |
| Promo (generic `promo-redeemed`) | 12 | 6 | **18** |
| **Unique redeemers** | **26** | **66** | **92** |

**Read:** **Winter Park drives redemptions (66 vs 26)**, led by the **$25 Welcome voucher (47 total)**. BOGO barely
redeems (2) — consistent with the ads picture. The generic `promo-redeemed` tag (18) is a *separate* earlier set,
not overlapping the by-code tags.

**Gap:** GHL stores the redeemed *tag* but **not a redemption date**, so we can't yet trend redemptions by week —
adding a timestamp on redemption would fix this.

---

## 3. Campaigns that have shipped (from cohort tags)

| Campaign | POL | WP | Total |
|---|---:|---:|---:|
| 4th-of-July "STARS" email (~Jun 30) | 111 | 142 | **253** |
| May nudge — SMS | 101 | 126 | 227 |
| May nudge — Email | 54 | 38 | 92 |
| Reactivation sequence (`reactivate-wk1-*`, daily batches) | ~2,500 | ~2,500 | ~5,000 |

Plus a `weekly-list` (POL 99 · WP 226) for recurring sends. **Note:** the SMS leg of the 4th-of-July blast has no
send tag — either it didn't fire or wasn't tagged; worth confirming.

---

## 4. Birthday funnel & automations

- **Birthday cohort enrolled 6 Jul** (`bday-start-2026-07-06`): POL 112 · WP 145 — essentially the whole opted-in
  audience. `birthday-{loc}-lead`: POL 110 · WP 145. **Parties booked (GHL): 0.**
- **Child-birthday field differs by location:** POL stores a full **Date** (`4dW6Ni9njQByJweCW8ip`); WP stores only
  a **Month** (`U1HiMixVAZ9ZQ1ItLROl`, numerical). The birthday radar can only key off one field, and WP's
  month-only data can't anchor a precise reminder — needs aligning.
- **AI voice agent is live and working:** ~**25 inbound calls** handled (POL 12 · WP 13), all tagged `topic-party`
  — real party demand landing on the phone. 2 `birthday-inquiry` at POL.

---

## 5. Data hygiene notes

- **Unsubscribes:** the standard `unsubscribed` tag is 0, but **SMS opt-outs are tracked** under `sms-unsub` /
  `unsubscribed-sms` (POL 3 · WP 7 = 10) plus `no-sms-consent`. Worth standardising so suppression is watertight.
- **Test tags present** (`claude-final-test`, `claude-test-contact`) — harmless, clean up when convenient.
- **Two naming conventions per redemption** (`x-redeemed` and `redeemed-x`) — fine, but pick one to avoid confusion.

---

## 6. Raise with William tonight
1. **Redemption tracking:** can redemptions carry a **date/timestamp** (to trend weekly), and is `promo-redeemed`
   (18) genuinely separate from the by-code tags (74) → so 92 is the right total?
2. **Party attribution:** confirm **`BDAY25` is live in Aluvii** and agree who pulls the Aluvii booking count
   (the one number outside GHL).
3. **Birthday automation:** reconcile our drip/radar with your GHL-native birthday workflow (double-send risk), and
   fix WP's month-only birthday field.
4. **Secrets:** add Meta + Google API tokens so live ad data joins GHL in the weekly report.
5. **Workflows:** the birthday-drip / radar / scorecard GitHub workflows are currently **disabled** — decide what
   we switch back on and when.

---

*Live pull 2026-07-14. Refreshable any time via the `mj-audit` workflow.*
