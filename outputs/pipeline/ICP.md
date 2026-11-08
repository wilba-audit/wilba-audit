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
   **A BARE COPYRIGHT YEAR COUNTS ONLY IF IT IS AT LEAST THREE YEARS OLD. Added 8 Nov 2026**,
   while applying the ladder below to 23 rows, because "is a copyright year a proxy?" was
   otherwise getting a different answer on every row. A 2023 copyright read in 2026 evidences
   three years of trading and is a usable, if thin, dated artifact. A 2025 or 2026 one evidences
   nothing about age. A copyright *range* that starts years ago ("2019-2026") is better evidence
   than either and always counted.

   **AND MUST-HAVE 4 CAN FAIL ON SUBSTANCE EVEN WITH GOOD EVIDENCE.** Row 720 publishes an award
   run for 2025 and 2026, which genuinely dates trading to 2024 or earlier - real evidence, better
   than most of the batch. It still fails, because two to three years is not "enough trading time
   to have accumulated roughly 300+ lapsed patients", which is what this must-have is actually
   for. The ladder tells you whether you KNOW the age; the must-have asks whether the age is
   ENOUGH. Both have to pass.

   **THE EVIDENCE LADDER, set 5 Nov 2026, because "established" was being read three different
   ways in one file.** A sweep where only 2 of 19 clinics published a founding date needed a rule
   rather than a judgement, so: **a dated or quantified artifact on the clinic's own site
   satisfies must-have 4** (a stated founding year, a review count, a copyright range starting
   years ago, "serving X since Y"); **a practitioner's career length alone keeps the row at B**,
   because that person's twenty years are not this clinic's lapsed list; **no proxy of any kind
   parks it at C.** That ladder is what separates a grade A from a grade B on otherwise identical
   rows, and it was set by the worker who could not reproduce the 4 Nov claim that must-have 4 is
   not binding in affluent Ontario.
5. **A published email address, read off their own page.** Never constructed, never
   inferred. Record the URL and the date it was read. A Cloudflare-obfuscated address that
   renders as `[email protected]` counts as not seen — **that has not changed and will not.**
   What changed on 2 Nov 2026 is what happens next: such a clinic is **not unreachable and must
   not be dropped.** The real address is in the page as a hex token that a browser decodes for a
   human reader, so these go on the browser-visit list in
   `outputs/pipeline/browser-visit-list.md`, and an address Jess reads in her own browser is seen.
   We do not decode the token ourselves, by choice rather than inability — a clinic running
   obfuscation has acted to stop automated collection, and must-haves 6 and 7 both rest on an
   address being conspicuously published. The reasoning, and the decision that is Jess's to make,
   are in that file.
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
   - **A company NAME with no number is still a pass. Clarified 4 Nov 2026**, because a
     worker nearly spent a register call confirming what a footer had already answered.
     The must-have asks for "Ltd", "Limited" **or** a company number — any one of the
     three. "Aesthetics By Dr Katherine Limited, Registered in England & Wales" is a pass
     on its own.
   - **Ask the company question in the SAME extraction as the address.** Four of
     twenty-one UK rows on 4 Nov answered must-have 8 off their own page in the fetch that
     got the address — the same one-in-four rate the 1 Nov worker measured, independently
     reproduced. It costs nothing and on 4 Nov it produced the run's best row.
   - **The register is to Britain what the privacy policy is to America.** On 4 Nov the
     homepage or footer gave the address on 20 of the 22 UK sites that published one at
     all, and the one policy fetch spent returned a mailbox already in hand plus no company
     number, no ICO number and no named controller. **What Britain withholds is legal
     identity, not the address.** 23 of that worker's 58 fetches went to the register and
     resolved must-have 8 for ten rows. PECR removed about half the market, not nearly all
     of it: 27 businesses researched, 7 sendable.
   - **A London service address on a provincial clinic's name match is a near-miss until
     something ties them together.** Two of the four near-miss traps that fired on 4 Nov
     were registered at mass-registration addresses — 71-75 Shelton Street, Covent Garden,
     and 1 Quality Court, Chancery Lane. A single-nurse clinic in Salisbury does not
     register its company in Covent Garden. The strongest passes are the reverse: a
     registered office **byte-identical** to the clinic's published street address.
   - **The near-miss trap fired four times in one run on 4 Nov, three of them EXACT name
     matches** — an active or dissolved company with the clinic's exact trading name, in
     another town. Each would have read as a pass. Check the registered-office town every
     time.

**How to search Companies House, because the obvious way does not work.** The plain name
search ranks results **alphabetically rather than by relevance** — "facial perfection"
returned 1,745 matches with the clinic nowhere in the first twenty. Use the **advanced
search** with `companyNameIncludes` plus `registeredOfficeAddress` plus
`companyStatus=active`, and run it **once per town rather than once per clinic**: it returns
every candidate entity in that town with its incorporation date, which answers must-have 8
and must-have 4 together for a whole market in a single fetch. Do not try SIC codes without
a name filter — that returned 108 paginated results and bought nothing.

**A company that is NOT CURRENTLY ACTIVE does not satisfy must-have 8 — and "dissolved" was too
narrow a word. Corrected 5 Nov 2026**, when the near-miss trap fired for the fifth time in two
days on a company **in liquidation**, which is neither active nor dissolved and would have read as
a pass to anyone matching on the two words this file used. Read it as **"dissolved, in
liquidation, or otherwise not currently active"**, and pass `companyStatus=active` on the search
rather than filtering by eye.

**A second mass-registration address, found 5 Nov 2026: Adamson House, Towers Business Park,
Didsbury M20 2YY** — 127 companies across seven pages. It belongs beside 71-75 Shelton Street,
which has now fired three times in two days. **And the truncation fault has a street-level
variant:** a `registeredOfficeAddress` search on a retail parade or a business park paginates at
20 of dozens — Crown Passages, Hale returned 60 across three pages, and the target company was
thirteenth by luck rather than by ranking. A street-level search is never complete at one page.

**FOURTH FAULT, found 4 Nov 2026: `registeredOfficeAddress` matches STREET names, not just
towns.** Searching it for "Salisbury" returned six companies in Slough, Pudsey and Hounslow,
all of them on a road called Salisbury something. This is worse than noise, because the
20-result truncation means those six push the actual local companies off the page — so the
fault produces a false *negative*, and a false negative here reads as "no company identity
exists", which parks a sendable row. Narrowing with `companyNameIncludes=cosmetic` did not
help: it returned one company, in Hounslow. **A town that is also a common street name
(Salisbury, Richmond, Windsor, York) cannot be screened by registered-office search alone.**
Use the clinic's own page for the company identity first, and treat an empty register result
in such a town as unresolved rather than negative.

**Also 4 Nov: a London mass-registration address is a near-miss trap of its own.** 71-75
Shelton Street WC2H is a formation-agent address used by tens of thousands of companies, and
it fired twice in one sweep. A registered office there tells you nothing about where the
business is, so it can neither confirm nor exclude a match.

Two further faults, both found the hard way on 29 Oct and both capable of producing a
confident wrong answer:

- **`companyNameIncludes` matches whole words, not substrings.** Searching `aesthetic` misses
  every company named "AESTHETICS". Six calls were nearly wasted before the plural was tried.
  Search both forms, or search the distinctive part of the clinic's name instead.
- **It truncates at 20 results.** Bolton returned 77 matches, Colchester 38, Wigan 32 — so a
  clinic can be paginated off the first page and read as having no company at all. One was
  invisible exactly that way. **A no-match in a town that returned 20-of-many is unresolved,
  not absent**, and the second call that settles it is a targeted search on the clinic's own
  name. Only a no-match in a town whose full result set you actually saw means no company.
- **The near-miss match is the dangerous one** — added 1 Nov 2026, and the worker who found it
  rates it above truncation, because truncation makes you miss a company while this one hands you
  the wrong company and reads like a pass. "ELIXIR MEDICAL AESTHETICS" returned two companies of
  that **exact** name, both registered in Scotland, against a clinic trading in Loughborough. A
  name match on its own therefore proves nothing: **always pair `companyNameIncludes` with
  `registeredOfficeAddress` for the clinic's own town**, and where the registered office sits in
  another country, treat it as a different business until something ties the two together.

Where Companies House genuinely comes up empty on a clinic worth having, the **CQC
registered-provider record** names the legal entity outright. **Tried on 1 Nov 2026 and blocked
by tooling, not by budget: CQC location pages return a client error to a fetch, and the ICO
register is a POST form with no searchable URL.** So this route is not something to assign a
worker again — it needs a person with a browser. The three clinics that have been waiting on it
since 29 Oct are waiting on Jess, not on a sourcing run, and they should be carried on the
browser-visit list rather than re-queued. A **dissolved-company
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

**A THIRD must-have 2 failure kind, found 5 Nov 2026, and in York Region it was commoner than
the other two combined: a named therapeutic-injection line.** Migraine, hyperhidrosis, TMJ,
alopecia — reimbursed through private extended-health DRUG plans rather than through a provincial
plan. Found on 6 of 19 businesses in one sweep. It is a spectrum rather than a line, so the worker
set a threshold and applied it to all thirteen of its rows, and **the threshold is adopted here so
that the next worker argues with a number instead of re-inventing one**: **four or more
reimbursable indications under a named medical heading parks the row at C on must-have 2; one to
three incidental lines pass, with the caveat recorded in `notes`.**

**A LABEL IS NOT A FINDING, AND DERMATOLOGY IS THE WORD IT KEEPS HAPPENING TO. Ruled 8 Nov
2026**, the third outing for this shape after the vein rule and the mole rule. The Disqualify list
below says "plastic surgery or dermatology practices", and it gives the reason in four words:
*insurance billing, heavier privacy rules*. **That is what is disqualified — a practice that bills
insurance and carries a disease caseload, not a clinic whose copy uses the word.** So a row parked
on the bare label, with no insurance billing seen, no surgical menu and no diagnostic line named,
is **UNRESOLVED, NOT FAILED**, and it holds at C until the treatment menu is read rather than being
written off. Row 469 was downgraded B to C on 20 Oct because its meta description said "cosmetic
dermatology", and went back to B on 8 Nov with the evidence against the label already in its own
note: nothing surgical, nothing insurance-billed, injectables listed first and largest. The same
test applies in reverse — row 27 fails honestly on nine consultant surgeons across three sites with
a surgical menu, which is substance and not a word.

**The general rule behind all three: extract the substance, not the word.** Whenever a row is
parked on a single noun — "dermatology", "veins", "moles", "surgery", "chain", "consent-risk" —
the question to ask is what was actually *seen*, and if the answer is nothing, the must-have is
unscreened rather than failed.

**The same mechanical problem has moved to MOLES AND LESIONS, and it is settled here on the vein
precedent, 5 Nov 2026.** The vein narrowing worked and rescued four British clinics in one sweep,
and then the identical ambiguity turned up one line down the menu. So, the same shape:
**mole or lesion SCREENING fails must-have 2** — "Map My Mole", mole mapping, dermatoscopy, any
check for disease — because it is diagnostic work on the insurance and NHS referral pathway, and
it leans on the dermatology disqualification besides. **Anything the clinic itself calls "minor
surgery" fails.** But **cosmetic removal of a benign blemish passes** — liquid-nitrogen cryo or
electrocautery for warts, skin tags and seborrhoeic keratoses is cash-pay cosmetic work
everywhere we sell. **Screening is about finding disease; removal is about appearance.**

**And on vein work specifically: extract the INDICATION, not the service name.** The 4 Nov rule
made a bare, undescribed service name "unresolved rather than failed", and that is still right —
but "unresolved" is only for a bare name. Where the clinic names the indication the rule resolves
in one direction or the other: **"Spider Vein Removal (Sclerotherapy)" passes** (cosmetic,
cash-pay), **"spider veins and varicose veins" fails** (varicose veins are venous disease). Two
rows would have been needlessly parked on 5 Nov by stopping at the service name.

**Must-have 2 has a second failure mode in Canada, found 4 Nov 2026: private
extended-health billing.** The briefed case is public funding — Medicare, OHIP, the NHS. But in
Canada the thing that actually failed seven rows in one sweep was a clinic running an
RMT / acupuncture / naturopathy arm **receipted to private extended-health plans**. That is not
OHIP, so it passes a literal reading of "no Medicare billing", and it still fails what must-have
2 is for: the practice has a non-discretionary, third-party-reimbursed revenue stream, so its
patient list is not a list of people spending their own money by choice. Park it as a must-have 2
failure and say which kind. **Must-have 2 was the only must-have that failed anything in that
market** — every one of the seven C rows, nothing else.

**Six things that look like a published address and are not.** A website-builder
placeholder the owner never replaced (`filler@godaddy.com`, `contact@wix.com`). An address
shipped inside a directory site's QR code image, which is directory data rather than
something the clinic published. An address served in a page's Open Graph meta tags
while the visible one is obfuscated. And **the owner's own typo** — one AU clinic's terms
page printed a mailbox at `.com.ay`, a domain that does not exist. And, added 2 Nov 2026 and
widened 3 Nov, a **fifth: somebody else's working mailbox, whether hidden or in plain sight** —
one clinic serves its marketing agency's address in `twitter:data1`, and a Tulsa clinic prints a
vendor's mailbox in plain visible text on its own page. Visibility is not the test; **whose
domain it is** is the test, so read the domain of every address before recording it.

And, added 3 Nov 2026, a **sixth: an address that exists only in the clinic's own meta tags.**
This is distinct from the Open Graph case, where a visible address existed and was merely
obfuscated. Here nothing is visible anywhere: pipeline row 103 serves `info@` and `manager@` on
its own domain in meta tags, while its contact page shows a form and two street addresses and no
mailbox. It is the most tempting of the six, because the domain is right and the mailbox is
probably live. **Must-haves 5, 6 and 7 rest on conspicuous publication, and a string a visitor
cannot see was not published to people** — the same answer we gave Cloudflare obfuscation on
2 Nov, for the same reason. Park the row with must-have 5 named, keep the address in it so the
call is reversible, and do not send.

None of the six may be recorded as a published address. The first four are not recoverable by
opening the page in a browser; the sixth is not a recovery problem at all, but a question about
whether the clinic published anything.

**A GENERIC INDUSTRY DOMAIN IS NOT THE CLINIC'S OWN. Settled 5 Nov 2026, and settled here
rather than asked of Jess, because it is a qualification question and she should never have to
answer one.**

The case: Clara Med Spa's address is published as `clara@medspas.info` — the clinic's name as the
local part on a generic industry domain, found on a page bylined by a third party who gives their
own gmail. The worker read it as a middle case between the clinic's own domain, an identifiable
agency's mailbox and a consumer mailbox, and it is right that the existing test does not reach it.

**The ruling follows from must-have 5's own words: "a published email address read off THEIR OWN
site."** Two questions, and both have to pass:

1. **Where was it published?** On the clinic's own domain, or on somebody else's page? An address
   found only on a third-party page is not the clinic publishing an address. **Clara fails here**,
   which decides it on its own, and the mailbox domain never has to be argued about.
2. **Whose mailbox is it?** A mismatched mailbox domain is normal and is never "corrected" — a
   clinic on `theclinique.com.au` publishing `cosmetic@thecliniqueaesthetics.com.au` is the clinic
   publishing its own mailbox. But `medspas.info` is not a brand variant of Clara: it is a generic
   domain serving an industry, so mail to it reaches whoever operates `medspas.info`, which may or
   may not be the owner we are writing to.

**So: if the clinic's own site publishes the address, record it, and record in `notes` that the
mailbox sits on a generic domain the clinic does not appear to control, because a reply may not
reach the owner.** That is a weaker row, not an invalid one. **If the address exists only on a
third-party page, park it on must-have 5.** Clara is parked.

**The general form, which is the part worth keeping:** the test for must-have 5 is never what the
address looks like. It is *where it was published* and *who receives mail sent to it*. Every
member of the six-item look-alike list below is really one of those two questions.

**A privacy promise about what the clinic SENDS is not a refusal to RECEIVE. Found 4 Nov 2026,
and it nearly cost the best row in a sweep.** Bradford Skin Clinic prints, on its homepage and its
policy, "We use what you send here only to contact you about this. **No marketing lists.**" and
"we do not add you to a marketing list because you asked a question about your skin". That is a
promise about what **they** do with a visitor's form submission. **A consent refusal under CASL or
the AU/NZ rules is about messages the clinic will not ACCEPT; this is about messages the clinic
will not SEND.** Privacy-forward marketing copy is spreading and "no marketing lists" reads like a
refusal to anyone skimming for the word "marketing". **Quote the wording verbatim on the row rather
than paraphrasing it**, because a paraphrase is exactly how this becomes a wrong call six weeks
later. Running total across four Canadian sweeps: past eighty clinics, thirty-odd policies read in
full, **zero actual refusals.**

**A `mailto:` link IS conspicuous publication. A meta tag is not. Settled 4 Nov 2026,
because the file was carrying both answers at once.**

Three rows turn on this and they were not being treated alike. Rows **536 Lucia Medspa** and
**588 Specialist Facial Aesthetics** are sendable on an address that appears only as the target
of an "Email Us" link, never as visible body text. Meanwhile row **132's own notes** said, of a
second address found the same way, that "an address inside an href is not published text" — and
rows 103 and 636 were parked for being meta-tag-only. Those cannot all be right.

**The ruling, and the reason:** the test for must-haves 5, 6 and 7 is conspicuous publication,
and the question that actually answers is **can a member of the public use this to email the
clinic?**

- A **`mailto:` link is a working, public invitation to email.** A visitor sees a clickable
  "Email Us", their browser shows the address on hover and their mail client prints it in the To
  field. The clinic put it there for strangers to use. **That is published**, and 536 and 588
  stand.
- A **meta tag offers the public nothing.** No visitor can see it, hover it or click it; it
  exists for machines. Nothing on the page invites an email at all. **That is not published**, and
  103 and 636 stay parked.
- A **Cloudflare placeholder is an act against machine collection** specifically. Still not seen,
  still never decoded.

**Row 132's note overstated the rule and is corrected today.** What it was reaching for is
sound and narrower: when a clinic publishes one address visibly and a *different* one only in an
href, record the visible one and do not harvest the extra. That is about not collecting more
than the clinic offered, not about hrefs being invalid.

**Still worth recording on the row when it happens**, as 536 and 588 both do: an address that
was never printed on screen is one step weaker as evidence than one that was, and whoever sends
should know which they have.

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
  Aesthetic Record, GoHighLevel, PatientNow, Mindbody, **Aesthetic Nurse Software, Faces
  Consent, Aesthetidocs** (the last three added 4 Nov 2026), Setmore, Acuity, Vagaro,
  GlossGenius, Dapple, MyPatientNow, Mangomint
  - **GRADE A MAY BE STRUCTURALLY UNREACHABLE IN BRITAIN, and that is a fact about our grade rather
than about British clinics. Recorded 5 Nov 2026.** A UK sweep returned **7 sendable rows and not
one grade A**, and the worker's account of why is precise: it kept finding clinics with any three
of grade A's four requirements and never all four, because **Britain's owner-injectors publish
the practitioner and the platform freely and almost never publish a loyalty or membership
scheme.** The 4 Nov UK sweep found two A rows out of 21, so this is not absolute — but the
banked-credit signal that makes a Mountain West clinic an easy A is close to absent here.

**The consequence to hold onto: a grade is not comparable across markets.** A British B and an
Arizonan B are not the same row, and a run that reports "no grade A" may have found the best
clinics in the country. Judge a market by its sendable count and its trading histories, not by
its grade mix. **Do not pad a British row to A to make a sweep look better**, and do not read a
low A-count there as a bad run.

**Aesthetic Nurse Software is the commonest platform in the UK independent sector** and
    its absence from this list was costing us grade A rows. One sweep of the UK southern half
    found it on **seven** clinics against one each for Timely, Fresha, Cliniko and Pabau. A
    clinic running it was being marked down for having "no named system" when it in fact runs
    the sector-standard one. The tell is a booking link resolving to
    `portal.aestheticnursesoftware.com/book-online/<id>`.
  - The point of this list was never the brand. It is that a named system means **a patient
    list exists in a queryable place**, which is what the offer acts on. So a platform not on
    this list is a prompt to check what it is, not a reason to mark a row down. Vagaro,
    GlossGenius and similar are the exception that proves it: they are real systems, but a
    clinic whose entire web presence is a Vagaro subdomain usually publishes no address of its
    own, which fails must-have 5 for a different reason entirely.
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
