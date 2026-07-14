# Monkey Joe's — Birthday Party Acquisition Strategy

**Prepared by:** WILBA · **Date:** 2026-07-14
**Goal:** More birthday-party bookings at Pointe Orlando (POL) + Winter Park (WP) — the highest-margin product.

> Grounded in the pilot call transcripts (Apr–Jun 2026) + the ads audit. **Anything marked
> `[CONFIRM]` is a genuine unknown I will not assume** — most importantly the party **package names
> and prices**, which do not appear in any source document.

---

## 1. The core constraint (read this first)

**Parties book ONLY through Aluvii, and Aluvii has no API.** That single fact shapes everything:
- We **cannot** auto-track party bookings from a pixel or GHL. The **only** attribution is the
  **`BDAY25` code redeemed in Aluvii** (a manual export/count).
- Party keywords on Google cost **$25–$40 per click** — far too expensive. **Parties do not go on
  paid search.**
- So party growth is a **warm-audience + relationship** play, not a cold-paid-ads play.

**Implication:** every party tactic below drives to one of two actions — (a) **book in Aluvii using
`BDAY25`**, or (b) **submit the birthday lead form** → front-of-house calls and takes a **~$50
deposit** over the phone.

---

## 2. The five acquisition channels (priority order)

### 1) Birthday Radar — reminders before the child's actual birthday (highest intent)
- Triggers off each child's birthday in the waiver data. Michael's stated cadence: **SMS + email at
  ~180, 60, and 30 days before** the birthday. *(Our current `mj_birthday_radar.py` uses 90/60/30 —
  reconcile to Michael's 180/60/30, or agree a blended 180/90/60/30.)*
- **POL only today** — WP's waiver export has **no birthday data**. Fix: (a) William chases the WP
  export from corporate/Aluvii, (b) capture birthday on every WP waiver going forward.
- Copy angle (from Michael): *"We hear there's a birthday coming up — all you need to do is bring
  the cake, give us a call."* Warm, low-friction, phone-forward.

### 2) Post-visit upsell sequence (turn walk-ins into parties)
- After a walk-in / code redemption: **Google review request → Frequent-Jumper upsell → birthday
  upsell.** Parents who just had a great visit are the warmest party prospects.
- Delivered by email + SMS; cap ~**2 SMS + 2 emails/week** across all sequences (agreed limit).

### 3) Bi-weekly email/SMS to the ~20k list
- Rotating Tue/Thu themes: Frequent Jumper cards / birthdays / offers.
- Birthday email → the **birthday landing page** (native form, not GHL) → **N8N** emails
  front-of-house a "birthday party inquiry" → front-of-house **calls + takes ~$50 deposit**.
- Form asks: **preferred location, child's age (not name), preferred date.**

### 4) Facebook retargeting (cheap, warm)
- Meta leads cost only **~$3.25–$3.73** (see audit). Retarget site visitors + the email lists + FB
  custom audiences with **party creative**. This is the one place paid $ makes sense for parties —
  because it's *warm*, not cold search.

### 5) Local partnerships + organic (Nicole-led)
- Michael's list to build with Nicole: **custom-cake shops (Publix is #1; a past Carvel
  ice-cream-cake deal), pediatricians, pediatric dentists, orthodontists.** Cross-promote parties.
- Organic posting in **local Facebook groups** ("Florida mums") — manual (Meta API won't automate
  group posts); coordinate with Nicole/Michael's wife who already monitor FB.

---

## 3. Offer & messaging

- **Party offer:** `BDAY25` — **$25 off** a party. Must be live + redeemable in Aluvii and named in
  every party touchpoint.
- **Packages (verified from monkeyjoes.com, July 2026):** all include a 2-hr private party suite, a
  dedicated party pro, unlimited play, online invites, themed plates/napkins, a gift for the
  birthday child, a Monkey Joe visit, and pizza + drinks.
  - **Jungle Experience** — from **$314** (8 kids) · $374 (16) · $414 (24) · +$19/extra child
  - **Island Excursion** — from **$394** (8) · $464 (16) · $524 (24) · +$22/extra · +ice cream + $5 game card/child
  - **Extreme Safari** — top tier (~$500 range) · +$26/extra · +$10 arcade card + ice cream + goodie bag/child
  - *Confirm any POL vs WP variance and whether these exact figures hold per location (the calls
    noted WP is cheaper on admission/frequent-jumper — party packages are usually corporate-standard).*
  - **✅ Fixed:** the scripts' old "$234 / $194" figures were wrong and have been corrected to the
    real published price ($314, up to 8 kids); the invented "weekday $194" touchpoint was replaced
    with an inclusions-focused message (no fabricated number).
- **Winning message themes** (Michael's past winners + review mining):
  - *"Active kids = happy hearts ❤️"* (his best-ever performer)
  - *"Get the kids off the screen"*
  - **Air-conditioned, indoor, clean, safe, great staff** — strong for the **hot, rainy Florida
    summer** (indoor-play demand peaks).
  - **Zero-stress for the parent:** "you bring the cake, we do the rest."

---

## 4. Reconcile the two birthday automations (do before scaling)

There are **two** birthday systems that can collide:
1. **William's GHL-native birthday automation** (from the waiver DB) — Jess confirmed a GHL workflow
   exists.
2. **Our Python drip** (`mj_birthday_sequence.py`, 180-day, daily GitHub Action) + **radar**
   (`mj_birthday_radar.py`, weekly).

**Risk:** both messaging the same parents = double-sends. **Action:** decide the single source of
truth (recommend William's GHL-native one for the birthday *reminder* automation, since it's tied
to the waiver DB), and repurpose our scripts for what GHL isn't doing (e.g. the post-visit upsell
sequence). Do not run both against the same contacts.

---

## 5. Measuring party growth (what goes in the report)

Because Aluvii has no API, the party scoreboard is semi-manual:
- **`BDAY25` redemptions in Aluvii** (weekly manual count) = booked parties attributable to us.
- **Birthday leads captured** (form submissions → front-of-house).
- **Deposits taken** (front-of-house confirms).
- **Radar/drip reach** (how many birthday reminders sent, from GHL).
- Compare booked parties to **the same month last year** (Michael's "did it move the needle" test).

---

## 6. 30-day action plan

**Week 1 — foundations & safety**
- Confirm party **packages/prices** with Nicole → fix/remove the `$234/$194` copy in the scripts.
- Confirm `BDAY25` is live in Aluvii.
- Reconcile the two birthday automations (pick one source of truth).

**Week 2 — turn on the warm channels**
- Launch the post-visit upsell sequence (review → FJ → birthday).
- Ship the birthday landing page + native form + N8N → front-of-house call flow.

**Week 3 — retarget & remind**
- Stand up FB retargeting with party creative (warm audiences).
- Confirm/adjust Radar cadence (180/60/30) and get WP birthday data flowing.

**Week 4 — partnerships & measure**
- Nicole compiles the partner list (Publix/Carvel/pediatric practices) → outreach.
- First party scoreboard in the weekly report (BDAY25 redemptions + leads + deposits).

---

## Open questions (I need these — will not assume)
1. **Party package names + prices** (and the `$234/$194` in the scripts — real or remove?).
2. **Deposit amount** (calls said ~$50 — confirm).
3. **Radar cadence** — 180/60/30 (Michael) vs 90/60/30 (current script)?
4. **Which birthday automation is the source of truth** — William's GHL workflow or our drip?
5. **WP birthday data** — has the export been obtained yet?
