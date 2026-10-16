# Who we target, and how we qualify them

**Current standard: v2, 16 Oct 2026.** Source: Griffin's *Med Spa Reactivation* briefing
(Prestique, 2 Sep 2026), which Jess uploaded on 16 Oct and told us to master. The canonical
copy lives at `/mnt/project-files/revenue-engine/ICP.md`; this file is the working copy the
daily outreach skill reads. If the two ever disagree, the revenue-engine file wins and this
one gets fixed.

**This replaces the 22 Sep standard** (multi-site, plastic surgery welcome, "$100k+/month"
proxies) for all new sourcing. Rows already in the pipeline that fail v2 are graded **C**
and parked with a note saying why — not deleted, because the standard may widen again.

## The offer we are selling

Work the clinic's **lapsed patients** — people who came once or twice and never rebooked —
over a multi-week, two-way SMS conversation that books them back into the clinic's own
calendar. Their team changes nothing. We work inside the system they already run.

Paid as **10% of what it books, nothing upfront** (confirmed by Jess 24 Sep 2026). Never
promise a refund — that line was never Griffin's and is not ours to offer. The risk
reversal is simply: if nothing comes back, you owe nothing.

> **The percentage is 10%.** If Jess ever changes it, change it here and in
> `.claude/skills/outreach-daily/SKILL.md` together.

Coming later, pending Jess and Griffin: a modest setup fee plus one percentage for the
first 90 days, then a flat monthly service answering new enquiries within minutes. That
monthly is the real business; reactivation is the way in. Do not pitch it yet.

## Must have

1. **Injectables / aesthetics-led** clinic or med spa. The treatments wear off on a three
   to four month cycle, which is what makes a lapsed list worth recalling.
2. **Cash-pay.** No insurance or Medicare billing. Where it is unclear, the discovery
   question is "Do you bill any insurance or Medicare electronically?" — a yes pulls the
   clinic into a much heavier health-privacy regime.
3. **Owner-operated, one site or a small handful (1 to 4).** The owner or owner-injector
   is the buyer, and they need to be reachable. Five or more sites usually means a head
   office decides marketing.
4. **Established.** A real review history, and enough trading time to have accumulated
   roughly 300+ lapsed patients. A brand-new clinic has no list.
5. **A published email address, read off their own page.** Never constructed, never
   inferred. Record the URL and the date it was read. A Cloudflare-obfuscated address that
   renders as `[email protected]` counts as not seen.
6. **For AU and NZ, also:** no "no unsolicited commercial email" notice anywhere on the
   site, and the address must be published on the clinic's own site (not a directory).
   Record both findings in `notes`.

## Strong signals — grade A

- An owner-injector named on the door or on the clinic's Instagram
- A practice system we can name: Pabau, Fresha, Zenoti, Cliniko, Timely, Boulevard,
  Aesthetic Record, GoHighLevel, PatientNow, Mindbody
- Busy and well reviewed — reactivation amplifies an operation that already works
- Memberships, loyalty schemes or banked credit. A lapsed member is an obvious recall,
  and schemes named "wallet", "bank" or "vault" are a reliable search term
- Redeemable or free consults: a pile of people who consulted and never booked

## Disqualify

- **Plastic surgery or dermatology practices** — insurance billing, heavier privacy rules
- **Hospital-attached or multi-specialty groups** — the buyer is not in the room
- **Chains, franchises, PE-backed or acquisitive groups** — 5+ sites usually means head office
- **Brand-new clinics** — no lapsed list to work
- Anything whose only contact route is a form or phone. No published email means no email
  outreach, so it goes to `near-misses.md` or the LinkedIn sheet, never into the pipeline
  with a guessed address
- Practices whose domain redirects to another company

Note what changed from 22 Sep: plastic surgery, dermatology and multi-site groups were
*targets* under the old standard and are *disqualifications* under this one. Scale is no
longer a virtue — owner-operated is.

## Where to find them, in order

**AU metros first:** Sydney, Melbourne, Brisbane, Gold Coast, Perth. Google Maps by metro,
filtering for independents with real review histories; Instagram for the owner-injector's
name; Pabau, Fresha and Zenoti directories. **US and UK next**, same profile.

`near-misses.md` records the metros already swept and what each one taught us. Read it
before picking a market so the same ground is not covered twice.

## Copy rules — every message, every channel

- **No prescription-medicine brand or category names.** Not Botox, Dysport, filler,
  anti-wrinkle injections, "tox". The TGA bans advertising prescription medicines to
  consumers; keeping our B2B copy clean as well makes it portable and shows we know the rules.
- **No prices and no discounts** in anything public or clinic-facing, especially in AU.
  This includes quoting the clinic's own published prices back at them in an opener.
- **No testimonials or case studies we do not have.** There is no med spa case study yet.
- Third-party benchmarks (for example "15 to 25% reactivate") only ever as a question,
  never as our result.
- Every cold email carries a working unsubscribe and WILBA's business address. Opt-outs
  actioned within 5 business days.

## What we record

Every prospect gets `crm_detected`, `scale_signals` and `dormant_lead_signal` filled from
their own site, and `email_source` saying where the address was read and on what date.
Those are what the opening line is built from. An opening line that could be sent to any
clinic is not an opening line — but it also cannot name a product or a price, so build it
from the clinic's own story: who owns it, how long it has traded, what scheme it runs.
