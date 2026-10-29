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

   **Count decision-makers, not addresses.** Three structures look like five-plus sites
   and are not: SEO suburb pages (one Melbourne clinic claims 18 locations against a
   single address), one travelling nurse who lists every town she visits, and injectors
   renting a room inside a host salon. In all three, one person still decides marketing,
   so they qualify. Conversely a three-site group run by a marketing manager does not.

   **And the inverse: the practitioner collective.** One address hosting several
   independent injectors, each with her own brand and her own booking account, is
   *several* decision-makers at one address — the mirror image of the room-renting case.
   The founder may control only a fraction of the lapsed list, so what we would be
   selling is not hers to sell. That fails this must-have. The tell is a team page where
   each practitioner has a separate business name, a separate booking link or a separate
   email address. Found at a Hamilton clinic on 21 Oct 2026.
4. **Established.** A real review history, and enough trading time to have accumulated
   roughly 300+ lapsed patients. A brand-new clinic has no list.
5. **A published email address, read off their own page.** Never constructed, never
   inferred. Record the URL and the date it was read. A Cloudflare-obfuscated address that
   renders as `[email protected]` counts as not seen.
6. **For AU and NZ, also:** no "no unsolicited commercial email" notice anywhere on the
   site, and the address must be published on the clinic's own site (not a directory).
   Record both findings in `notes`.
7. **For Canada, also: conspicuous publication.** Canada's CASL needs consent, and consent
   is *implied* where the clinic has conspicuously published the address on its own site
   with no statement refusing unsolicited commercial messages, and our message is relevant
   to their business. That is the basis we rely on, so a Canadian row records three things
   in `notes`: the page the address was published on, that the site carries no such
   refusal, and that the privacy policy was checked for one (or could not be read).
8. **For the UK and Ireland, also: a company identity.** UK anti-spam rules (PECR) let us
   email a corporate subscriber — a limited company — without prior consent, but not a
   sole trader or a partnership. Look for "Ltd", "Limited" or a company number in the
   footer, on the contact page, or in the privacy policy, which is where it usually hides
   because UK footers name the web designer instead. No company identity anywhere means
   grade C with "sole trader not verified" in `notes`.

**How to search Companies House, because the obvious way does not work.** The plain name
search ranks results **alphabetically rather than by relevance** — "facial perfection"
returned 1,745 matches with the clinic nowhere in the first twenty. Use the **advanced
search** with `companyNameIncludes` plus `registeredOfficeAddress` plus
`companyStatus=active`, and run it **once per town rather than once per clinic**: it returns
every candidate entity in that town with its incorporation date, which answers must-have 8
and must-have 4 together for a whole market in a single fetch. Do not try SIC codes without
a name filter — that returned 108 paginated results and bought nothing.

Two faults in that search, both found the hard way on 29 Oct and both capable of producing a
confident wrong answer:

- **`companyNameIncludes` matches whole words, not substrings.** Searching `aesthetic` misses
  every company named "AESTHETICS". Six calls were nearly wasted before the plural was tried.
  Search both forms, or search the distinctive part of the clinic's name instead.
- **It truncates at 20 results.** Bolton returned 77 matches, Colchester 38, Wigan 32 — so a
  clinic can be paginated off the first page and read as having no company at all. One was
  invisible exactly that way. **A no-match in a town that returned 20-of-many is unresolved,
  not absent**, and the second call that settles it is a targeted search on the clinic's own
  name. Only a no-match in a town whose full result set you actually saw means no company.

Where Companies House genuinely comes up empty on a clinic worth having, the **CQC
registered-provider record** names the legal entity outright and is still the untried route —
no worker has needed it yet, and three good clinics are waiting on it. A **dissolved-company
answer is itself a finding**: one clinic publishes two first-name mailboxes, reads as a
partnership, and every company of its name is dissolved. That is a sole-trader-or-partnership
answer, not an unresolved one.

**Where to find a UK or Irish company identity, in order.** Go to the registers first and
the clinic's own site last — that is the reverse of what seems natural, and it is what the
20 Oct run established: twelve clinics were resolved in 28 calls without reading a single
privacy policy. **Companies House** first, searching the clinic name and the owner's name.
Then the clinic's **CQC registered-provider record**, which names the legal entity and its
address outright and settles clinics whose own site says nothing; in Scotland it is
**Healthcare Improvement Scotland**, in Wales **HIW**, and in Ireland the **CRO**. The
**ICO data-protection register** also names entities and resolved one clinic. Only then the
clinic's own **privacy policy** — never the footer, which credits the web designer. An LLP counts: the ICO treats it as a corporate
subscriber. A dissolved company does not — it means the entity now trading is unknown.

**Four things that look like a published address and are not.** A website-builder
placeholder the owner never replaced (`filler@godaddy.com`, `contact@wix.com`). An address
shipped inside a directory site's QR code image, which is directory data rather than
something the clinic published. An address served in a page's Open Graph meta tags
while the visible one is obfuscated. And **the owner's own typo** — one AU clinic's terms
page printed a mailbox at `.com.ay`, a domain that does not exist. None of the four may be
recorded, and none is recoverable by opening the page in a browser.

**Tidiness predicts nothing, in either direction.** The company screen is a question about
legal form, and it does not correlate with how organised a site looks. The only clinic in one
sweep printing its own company number had placeholder links; the most polished site in that
sweep — three priced membership programmes, a named nurse — had no company behind it at all.
Do not skip a clinic because it looks too corporate, or chase one because it looks scrappy.

**Two more things that are not a published company identity or address.** A company number
or name appearing inside a **Fresha booking URL slug** proves the entity exists but is not a
publication by the clinic, so it does not satisfy must-have 8 on its own. And an email
address printed as **visible link text but wired to a `tel:` placeholder** — the text was
genuinely published and read verbatim, so it is recordable, but record the caveat: whoever
built the page never tested the link, which is a hint the mailbox may be unattended.

**A mismatched domain is not a typo, and must not be "corrected".** Where a clinic
publishes an address on a domain other than its website — `info@sccclinic.com.au` on a site
at `sccosmeticclinic.com.au` — record it exactly as the page prints it. Editing it to match
the website is fabrication even when the guess would probably work. Seventeen of the 76 rows
added on 21 Oct carried some form of mismatch, so this is common rather than exceptional.
Flag it in `notes` so a bounce is read as a bounce and not as disinterest.

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

**Read the privacy policy before giving up on a clinic.** Homepage, then the About-page
footer, then `/contact`, **then the privacy policy** — which is where one Moncton clinic
published the only address it publishes anywhere, and it would otherwise have been filed
unreachable. Outside the AU/NZ, Canadian and UK screens this costs an extra fetch; inside
them the consent screen already takes you to that page, so it is nearly free.

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
