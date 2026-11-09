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

   **TWO ADDITIONS TO THE LADDER, 8 Nov 2026, both from the Chicago sweep and both of which
   nearly cost real rows.** First, **a wall of individually dated client reviews IS a quantified
   dated artifact** — it is the clinic's own page evidencing a span of trading, and it nearly parked
   two accepted rows whose only dating was reviews running 2023 to 2025. Second, and the other way,
   **a bare star rating with no count is NOT a quantified artifact**: "rated 5.0" evidences nothing
   about how many patients or how long, where "based on 137 reviews" evidences both. Say which one
   the page actually shows.

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

**A TECHNIQUE THAT HALF WORKS, AND THE RULE THAT MAKES IT SAFE: QUOTE THE PHRASE, THEN READ THE
MATCH COUNT BEFORE YOU READ THE RESULTS. Measured 9 Nov 2026 on three searches.** Quoting a company
name on the public search sometimes forces a phrase match and sometimes silently falls back to
OR-ing the words, and **the match count is the only tell**:

- `"Imogen's Aesthetics"` returned **1** — the phrase search engaged, and the one hit matched a
  company number already known from another route, so the technique is sound when it engages.
- `"Elm Skin"` returned **0**, where the same words unquoted returned 10,000. A fallback would have
  returned ten thousand again, so the zero is real: no company of that name exists.
- `"UK Cosmetic Clinic"` returned **9,016**, and not one result on the first page contained the
  phrase. The search ignored the quotes entirely.

**So: a count of zero or a handful means the phrase search did what you asked and you may trust it.
A count in the thousands means it fell back and you have learned NOTHING — do not read those
results, and do not spend a second call paging through them.** This is the same failure family as
the officer search's 10,000 matches, and the count is the signal in both.

**THREE MORE COMPANIES HOUSE FAULTS, found 8 Nov 2026, and two of them cost rows.**
**A `registeredOfficeAddress` town search gives the REGISTERED OFFICE town, not the trading town** —
it mis-located two of five named leads in one run, including one clinic that turned out to be in
Rugby rather than Leamington. **Never record a trading town from the register.** **The OFFICER
search is unusable: do not spend a call on it.** Ten thousand matches on both attempts, because it
does not AND the terms and does not expose the appointments URL; it cost that run two otherwise
sendable rows. **And the street-name fault has a new worst measurement:** a Stamford street search
returned five of nine companies in Ashton-under-Lyne. Add **Stamford and Cheltenham** to the
street-name town list beside Crown Passages.

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
**THE FOUR-INDICATION THRESHOLD IS UNDER REVIEW BUT NOT CHANGED, 8 Nov 2026.** Two workers in two
markets independently said the same thing on the same day: it feels loose at three. One Seattle
clinic sits at hyperhidrosis plus alopecia plus lipomas and reads closer to a fail; one Chicago
clinic at migraines plus excessive sweating plus TMJ. **Both applied the number as written and said
so, which is exactly right** — a threshold that each worker re-tunes is not a threshold. It stays
at four until a row passes on three and then turns out to be insurance-billed; that is the evidence
that would move it, and the two instances above are now on the record so the third is recognisable.
Note what saved the Chicago row on the merits rather than the count: the page described no treatment
for any of the three and listed the neuromodulator only as "Cosmetic".

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

**THE RULE PAID FOR ITSELF WITHIN A DAY, AND THE REASON IT DID IS WORTH MORE THAN THE RULE.
Measured 9 Nov 2026, Westchester and Fairfield County.** The label test fired **five times in one
sweep and cleared the clinic all five times** — five clinics whose copy carried "dermatology", none
of which was a dermatology practice on the evidence. A rule that fires five times and reverses the
default five times is not a tie-breaker; it is correcting a systematic misread.

**Why, and this is the part that generalises: in an affluent suburb "dermatology" is a HIRING
CREDENTIAL, not a business model.** A cash-pay injectables clinic in Scarsdale or New Canaan
advertises that a board-certified dermatologist oversees its injectors, because that is what its
patients are buying. The word is on the page to describe **who works there**, not what the
business bills for. The old reading inverted exactly the clinics whose credentialing was
strongest — and those are the clinics most likely to be worth writing to.

**So the operational line: in a wealthy market, treat the word "dermatology" as evidence ABOUT
STAFF until an insurance line, a surgical menu or a named diagnostic service says otherwise.**
Read the treatment menu and the billing language; the noun on its own tells you nothing about
either. Fifth market this shape has been caught in, and the first where it was the dominant
error rather than an edge case.

**The same mechanical problem has moved to MOLES AND LESIONS, and it is settled here on the vein
precedent, 5 Nov 2026.** The vein narrowing worked and rescued four British clinics in one sweep,
and then the identical ambiguity turned up one line down the menu. So, the same shape:
**CORRECTED 8 Nov 2026 — SCREENING FAILS, BUT NOT ON MUST-HAVE 2, AND THE TEST IS WHO READS THE
IMAGES.** Three workers in three runs raised the same objection to the clause below and each one
correctly applied it as written rather than reinterpreting it mid-run, which is why the sentence is
mine to write. They were right. The clause failed mole screening on must-have 2 and gave the reason
as *"diagnostic work on the insurance and NHS referral pathway"* — but **that is not a billing
argument, and the 4 Nov narrowing made must-have 2 a billing test.** Map My Mole is a private,
cash-pay UK service: on must-have 2's actual wording it passes. The real objection to screening is
clinical risk and a disease caseload, which is the reasoning behind the DERMATOLOGY
disqualification, so that is where it belongs.

**So the test is whether the clinic takes on the skin-cancer clinical risk itself, and the question
that settles it is who reads the images.** A **white-label teledermatology service the clinic merely
HOSTS** — the patient pays, photographs go to a third party's dermatologist, the clinic provides the
room and takes a booking — leaves the clinic a venue rather than a diagnostician: **it passes**, and
the row then stands on its own injectables-led evidence. **Screening the clinic OWNS fails** on
must-have 1 and the dermatology disqualification: its own dermatoscopy read by its own clinician, or
mole checks with a named consultant dermatologist in the practice. One white-label line bolted onto
an injectables clinic no more makes it a dermatology practice than one blemish-removal line makes it
a surgical one — which is the same "substance, not the word" rule as everything else settled today.

**This is NOT the blanket teledermatology exemption that was proposed**, and the difference matters:
row 1101 keeps failing, because its mole checks are done *with a consultant dermatologist*, which is
the clinic owning the screening. Row 1098 converts to B. Row 1038's must-have 2 now passes and it
stays C anyway, on must-have 8.

**mole or lesion SCREENING fails must-have 2** — "Map My Mole", mole mapping, dermatoscopy, any
check for disease — because it is diagnostic work on the insurance and NHS referral pathway, and
it leans on the dermatology disqualification besides. **Anything the clinic itself calls "minor
surgery" fails — AND THE CONVERSE, ADDED 8 Nov 2026: avoiding the phrase does not rescue a
genuinely surgical procedure.** Both halves of this were found on the same day from opposite
directions, which is why the rule is now stated as substance rather than vocabulary. A Peterborough
clinic lists "Laser Minor Surgery for Blemishes": it uses the words and PASSES, because it names a
cosmetic indication and laser blemish work is cash-pay. A Franklin clinic lists "Cyst & Lipoma
Removal" and "Surgical Scar Revision" under a heading it calls *Dermatology* and never says "minor
surgery": it avoids the words and FAILS, because excision with closure is surgery whatever the
heading says. **Fail cyst and lipoma excision and surgical scar revision regardless of the label;
pass cosmetic blemish and benign-lesion removal regardless of the label.** The word is not the
test, and a row parked or passed on the word alone has not been screened. But **cosmetic removal of a benign blemish passes** — liquid-nitrogen cryo or
electrocautery for warts, skin tags and seborrhoeic keratoses is cash-pay cosmetic work
everywhere we sell. **Screening is about finding disease; removal is about appearance.**

**BUT TRY TO NAME THE INDICATION BEFORE FALLING BACK ON ITS ABSENCE — THE MODALITY AND THE
PRACTITIONER'S LICENCE USUALLY DO IT. Added 8 Nov 2026 by the Nashville sweep, which is a better
rule than the one below it because it rests on positive evidence rather than on silence.** *An
external aesthetic vascular laser in an aesthetician's hands is cosmetic; "endovascular laser
therapy" is venous disease.* That run had one of each and they resolved in opposite directions.
Read the device name and read who holds it.

**And the cheapest move of all comes first: a site-limited search often resolves a bare vein name
from the RESULT TITLES, with no fetch at all.** One such search took a Nashville row from C to B
for zero fetches, because the clinic's own page titles said "spider veins" where its menu had said
only "veins".

**WHERE NO INDICATION IS NAMED ANYWHERE, THE ABSENCE OF DISEASE LANGUAGE IS ITSELF THE
EVIDENCE. Settled 8 Nov 2026, and it closes the vein question.** The 4 Nov rule left a bare service
name "unresolved", which was right while the test was the name — but the 4 Nov narrowing also moved
the test to the BILLING MODEL, and once that is the test, a whole site with no disease and no
billing language is not an absence of evidence, it is evidence. So: **a vein line sitting inside a
cosmetic laser or device menu passes must-have 2 when varicose veins, venous insufficiency,
phlebology and vein disease appear NOWHERE on the site, and neither does insurance, Medicare or
bulk-billing language.** Read the whole site before concluding it, not the menu.

Three people reached this independently before it was written down, which is why it is a rule and
not a judgement: the worker who parked row 802 on 1 Nov said in the row itself *"my own reading is
softer than the grade — it is laser-only, sits among cosmetic laser services, and the site mentions
no Medicare or bulk billing anywhere — but the brief lists vein work as a fail and I am not going
to soften a must-have on my own reading."* **That was exactly right of them and exactly the wrong
outcome**: softening a must-have is this thread's job, not a worker's, and the row then sat at C for
a week because nobody did it. A Chicago worker proposed the same rule on 8 Nov from a laser menu of
its own, and the five rows re-read here point the same way.

**PROMINENCE IS NOT AND NEVER WAS THE TEST.** Two rows (847, 871) were parked on an invented line
where a vein CATEGORY fails and a vein line item buried in an injectables menu passes, with row 847
grading itself C against row 831's A on exactly that. A category heading is a navigation choice. The
billing model is the test.

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
failure and say which kind. **A NAMED INSURANCE SCHEME ON THE TREATMENT MENU IS THE
CHEAPEST MUST-HAVE 2 FAILURE THERE IS — added 9 Nov 2026.** One Long Island clinic prints
"Medical Massage/**NYSHIP**" — the New York State Health Insurance Program — on its own service
list. That is must-have 2 decided for **zero policy fetches**, off the page you were already
reading. So when scanning a menu for must-have 1, read it for scheme acronyms too: a named
public or group scheme beside a service line is a reimbursed revenue stream admitting itself. **Must-have 2 was the only must-have that failed anything in that
market** — every one of the seven C rows, nothing else.

**Seven things that look like a published address and are not.** A website-builder
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
mailbox. It is the most tempting of the seven, because the domain is right and the mailbox is
probably live. **Must-haves 5, 6 and 7 rest on conspicuous publication, and a string a visitor
cannot see was not published to people** — the same answer we gave Cloudflare obfuscation on
2 Nov, for the same reason. Park the row with must-have 5 named, keep the address in it so the
call is reversible, and do not send.

None of the seven may be recorded as a published address. The first four are not recoverable by
opening the page in a browser; the sixth is not a recovery problem at all, but a question about
whether the clinic published anything.

And, added 9 Nov 2026 from Westchester, a **seventh: a gmail published only inside an `sms:`
href.** The page's "text us" button carries `sms:+1...&body=...` and the clinic's gmail appears
inside that href's query string, so the string IS in the visible page's markup and a fetch reports
it as found. **But a visitor cannot email from it.** Clicking the button opens a text message, not
a mail composer, and nothing on the rendered page invites anyone to write to that mailbox. That
makes it functionally identical to the meta-tag case: the address exists in the HTML and was not
published *to people*. Same answer, same reason — park on must-have 5, keep the address in the row
so the call is reversible, do not send. **The general form, worth more than the instance: ask what
a visitor could DO with the string, not whether the string is in the page.** A grep over markup
cannot tell these apart, which is why must-have 5 is a reading task and not a search task.

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
member of the seven-item look-alike list below is really one of those two questions.

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
  Consent, Aesthetidocs** (the last three added 4 Nov 2026), **MyAestheticsPro, Moxie,
  Optimantra** (added 8 Nov 2026, each seen twice or more; clinics running them were being marked
  down for "no named system"), Setmore, Acuity, Vagaro, GlossGenius, Dapple, MyPatientNow,
  Mangomint
  - **Collums and PowerDiary added 8 Nov 2026** from the British sweep, which also confirmed
    Aesthetic Nurse Software as the commonest UK independent platform for a third time.
  - **Meevo and Symplast added 9 Nov 2026** from Long Island, each seen with a real tenant ID
    rather than a logo. **Meevo is the stronger evidence of the two by some distance**: it serves
    the diary, gift cards AND memberships from one tenant, so seeing it is seeing a queryable
    patient list and a dormant-credit mechanism in one observation. Seen twice there.
    **`elyonhq.com` (Elyon) is NOT on the list and should not be treated as a named system yet** —
    seen once, nothing known about what it does. Record the string in `notes`, do not grade on it,
    and if a second sweep meets it, that is the point to decide.
  - **PODIUM IS DELIBERATELY NOT ON THIS LIST, decided 8 Nov 2026** on the Seattle worker's
    reasoning, which is right: it is a messaging-and-reviews product with booking bolted on, so it
    is materially weaker evidence that a queryable patient list exists. Seeing Podium is not seeing
    a practice system.
  - **AND THERE IS NO SINGLE US PLATFORM — correcting my own 5 Nov claim.** I wrote that "Aesthetic
    Record is the dominant US platform" on two independent measurements, Phoenix 10 and Utah 7.
    Nashville is a clean counter-example: Vagaro three, Aesthetic Record two, Zenoti two, Boulevard
    two, Podium two and six singletons, with no dominant platform at all. Seattle's eastside had
    Aesthetic Record at five and was the standard there. **So platform concentration is a
    PER-MARKET fact, not a US fact**, and a pitch should not assume the platform before the row
    names it.
  - **GRADE A MAY BE STRUCTURALLY UNREACHABLE IN BRITAIN, and that is a fact about our grade rather
than about British clinics. Recorded 5 Nov 2026.** A UK sweep returned **7 sendable rows and not
one grade A**, and the worker's account of why is precise: it kept finding clinics with any three
of grade A's four requirements and never all four, because **Britain's owner-injectors publish
the practitioner and the platform freely and almost never publish a loyalty or membership
scheme.** The 4 Nov UK sweep found two A rows out of 21, so this is not absolute — but the
banked-credit signal that makes a Mountain West clinic an easy A is close to absent here.

**THE DIAGNOSIS IS CORRECTED, 8 Nov 2026, and it is a better one.** The 5 Nov account said
Britain's A-count is suppressed because its owner-injectors almost never publish a loyalty or
membership scheme. A third British sweep returned 9 sendable and 0 A and found something different:
**six of its sixteen rows carried a real dormant scheme, and the missing requirement in every
near-A case was a PUBLISHED REVIEW COUNT — only 3 of 23 British businesses published one.** So it
is not the dormant signal that is absent in Britain, it is the quantified review history. **British
clinics are busy and well reviewed and simply do not print the number**, which is a publishing habit
rather than a business fact, and it collides with must-have 4's evidence ladder. Do not read a
British zero-A run as a weak market, and do not pad a row to A to fix it.

**AND THAT CORRECTION IS ITSELF CORRECTED, 9 Nov 2026 — ONE DAY LATER, BY AN AMERICAN
MEASUREMENT. IT IS NOT A BRITISH PUBLISHING HABIT. IT IS A MARKET-TYPE EFFECT.** Yesterday's
sentence above blamed a national habit, which was the natural reading when every measurement came
from Britain. A Westchester / Fairfield County sweep — rich American suburbs, nothing British about
them — found the identical pattern independently: **only 3 of 28 clinics published a dated artifact
about the business at all**, and must-have 4 on *evidence* was what failed the rest. Two
measurements in two countries with one shape between them is a market-type effect, not a
nationality.

**The shape: the richer and more referral-driven the market, the less its clinics publish about
themselves.** A clinic whose chairs fill on word of mouth in an affluent suburb has no reason to
print a review count, a "serving X since Y", a patient number or a dated milestone. A clinic
competing on visibility in a mid-market metro prints all four, because it must. **So the evidence
ladder reads marketing effort and calls it trading history.**

**The structural consequence, which is uncomfortable and should stay written down: must-have 4's
ladder systematically parks good clinics in exactly the markets this offer most wants.** Affluent,
owner-operated, cash-pay, dormant-list-rich — the ICP's own profile — is the profile least likely
to clear the ladder's evidence bar. Every near-A row lost this way is a clinic we would have been
glad to write to.

**What this does NOT license: inventing evidence, or padding a row to A.** The ladder stays as it
is and the grades stay honest; a C parked on must-have 4 evidence is still a C today.
**What it DOES change is how a run is read and what is worth one more fetch.** A sweep of an
affluent suburb reporting a thin grade mix has probably found good clinics and a stingy market, so
report the market type alongside the mix; and where a row is otherwise strong and the ONLY gap is
a quantified artifact, that is the single highest-yield fetch left on the row, because the trading
history almost certainly exists and simply was never printed on the page you read.
**The open question, for whoever has a day to spend on it rather than a run to finish:
is a ladder that measures marketing effort the right ladder for must-have 4 at all?**

**A FOURTH MEASUREMENT, AND IT IS A DIFFERENT FAILURE WEARING THE SAME CLOTHES. Northern New
Jersey, 9 Nov 2026.** Five of its six C rows fail on must-have 4, so the pattern holds a fourth
time — but **the reason is new and it matters more than the count.** Britain's clinics are busy and
simply do not print the number. New Jersey's **print a BROKEN one**: three sites render
"0 +" or "0 Total Reviews" beside a page of real, individually dated testimonials. The trading
history exists, the clinic tried to publish it, and **a counter widget is misconfigured.**

**So there are now three distinct things the ladder cannot tell apart**, and it fails all three
identically: a clinic with no trading history (the honest C), a clinic with history it never
printed (the affluent-suburb case), and a clinic with history it printed into a broken widget.
Only the first is a reason not to write to someone. **Operationally: a "0" counter sitting beside
visible dated testimonials is NOT zero evidence — read the testimonials and date the oldest, and
the 8 Nov rung that a wall of individually dated reviews IS a quantified artifact already covers
it.** Do not let a broken number beat a readable page.

**And this sharpens the open question below rather than just adding to it.** The ladder is not only
reading marketing effort; it is reading **whether a clinic's website works.** That is further still
from trading history, and it is a worse thing to grade an owner-operated business on.
Flagged, not answered, and not changed unilaterally — it is a scoring change and it would
re-grade the whole file.

**A THIRD MEASUREMENT, THE SAME DAY, FROM A THIRD AFFLUENT SUBURB. Long Island, 9 Nov 2026.**
Six of its seven C rows are C on must-have 4 **alone** — nothing else failed them — and **only 2
of 24 businesses published a founding year.** Britain, Fairfield County, Nassau/Suffolk: three
measurements, three countries-or-coasts, one shape. Must-have 4 on evidence is now the **binding
constraint** in affluent referral-driven markets, ahead of must-have 2 and must-have 5, and that
should be the expectation a worker carries INTO such a market rather than a surprise it reports
out of one.

**And the way that third measurement arrived is itself the finding.** The Long Island worker
reached independently for the retired explanation — it wrote "a publishing habit, not a business
fact", the exact framing corrected a few hours earlier — because **it was commissioned before the
correction existed.** Nobody was careless. This is the 8 Nov lesson arriving from the other
direction: **a rule change reaches the run that makes it and nothing already in flight.** A worker
dispatched in the morning is reasoning from the morning's file however good it is, so its
conclusions have to be read against the brief it actually held, not the file as it now stands —
and a mid-run correction to a live convention is worth messaging to the workers already out, not
just writing down for the next ones.

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
