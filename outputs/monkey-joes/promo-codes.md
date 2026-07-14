# Monkey Joe's — Promo Codes (REALITY, as of July 2026)

> **This replaces the March 2026 Aluvii plan.** The original version of this file listed
> `WACKY-POL`, `WACKY-WP`, `WELCOME`, `COMEBACK` as Aluvii codes. That was the pre-migration plan.
> The pilot moved to **GoHighLevel (GHL)** for code generation + delivery, with **in-store
> redemption via William's external verification page**, and **party attribution via Aluvii**.
> The codes below are what the call transcripts (Apr–Jun 2026) actually describe. Confirm any
> gaps with William before relying on them for reporting.

---

## How codes actually work now

1. **Generated** in GHL (opt-in form or product purchase) — or via Stripe for paid products.
2. **Delivered** to the customer by **email + SMS**.
3. **Redeemed in-store** by front-desk staff typing the code into **William's external web
   verification page** (hosted HTML, saved as a browser favourite). The page returns: valid →
   deliver; not found; or already-used (with the date claimed). Staff enter their name/initials
   (trust-based; no staff logins yet). **Codes must be typed EXACTLY** or the page errors.
4. **Code prefix indicates the offer type** (e.g. `BOGO/`, `FJP/`).
5. **Redemption data lives on that verification page's backend (William / N8N), NOT as a GHL tag.**
   → This is the key correction. Any "codes redeemed" report needs an **export from William's
   system**, plus **Aluvii** for party codes. Do not assume a GHL `redeemed-*` tag exists unless
   William confirms he writes one back.

---

## The live codes

### `WELCOME` — $25 opt-in voucher
- **Offer:** free entry up to $25 value.
- **Trigger:** email → opt in for texts → give phone → receive voucher by email + SMS.
- **Channel:** email blasts to the ~20k list (goal: capture phone numbers for SMS).
- **Status:** live; ~249 SMS opt-ins recorded at last check-in.

### `BOGO/…` — Buy-one-get-one admission ("Wacky Wednesday" / "Bogo Wednesdays")
- **Offer:** BOGO child admission. Long-standing MJ staple.
- **Prefix:** `BOGO/`.
- **Channel:** Google Ads + Facebook retargeting (weekday walk-ins).
- **Note:** on **Google**, 50%-off outperforms BOGO at both locations (see ads audit). The call
  note "BOGO better at WP" refers to a different context (FB/in-store).

### `50% off` — Half-price admission
- **Offer:** 50% off child admission.
- **Channel:** Google Ads + Facebook. **Best Google performer at both locations.**

### `FJP/…` — Frequent Jumper Card (10 jumps)
- **Offer:** 10-jump punch card. ~**$12/jump at POL** (cheaper at WP). Prefix `FJP/`.
- **Rules (from Michael, verbatim intent):** not tied to one child (siblings/cousins OK); **not
  valid for organisations, groups, or birthday parties** (groups >10 → "contact us"); **only ONE
  FJ card used at a time**; punches not tracked (lose the card → gone); **stackable with ONE other
  offer — the Wednesday BOGO only**; usable at **both** locations.
- **Expiry:** open question — Michael leans to a **30-day auto-expiry** on marketing voucher codes;
  Nicole prefers no expiry (summer planning). The physical FJ card itself has no expiry.
- **Channel:** NOT paid ads — promoted via bi-weekly email/SMS + post-visit upsell sequence.

### `BDAY25` — $25 off a birthday party
- **Offer:** $25 off a party booking.
- **Redemption:** **in Aluvii only** (Aluvii has no API) → this is the **only** way to attribute
  party sales. Must be communicated in party marketing and set up in Aluvii.
- **Channel:** birthday drip/radar, birthday landing page, post-visit upsell.
- **Status:** flagged in calls as needing proper setup (was initially missed).

---

## Other promos referenced
- **Toddler Thursday** · **Wacky Wednesday BOGO** (the stack partner for FJ cards).
- **Google review request** (email/SMS on redemption/exit) → then FJ upsell → then birthday upsell.
- **Grip socks** — not included, purchasable (MJ cost ~$1.60/pair).

---

## Channel → code map (for attribution)

| Channel | Codes | Notes |
|---|---|---|
| Google Ads | `50% off`, `BOGO/` | 50%-off is the efficiency winner |
| Facebook (prospecting + retargeting) | `50% off`, `BOGO/`, `WELCOME` | retargeting = biggest lever |
| Email/SMS to list | `WELCOME`, `FJP/`, `BDAY25` | FJ + parties are NOT paid-ad offers |
| Birthday funnel | `BDAY25` | Aluvii redemption = party attribution |

---

## Open items to confirm with William / Michael
1. Does William's verification backend write a **redeemed flag back into GHL** (tag/field), or must
   we get a **CSV export** from him each week? (Determines how `/mj-redemptions` and the reports pull data.)
2. Exact **live code strings** per location (is it `BOGO/POL-xxxx`, `50OFF/…`, etc.?).
3. **`BDAY25`** — confirmed set up and redeemable in Aluvii?
4. **30-day expiry** decision (Michael vs Nicole).

*Version 2.0 — July 2026. Supersedes the March Aluvii plan.*
