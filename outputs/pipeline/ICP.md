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

   **The travelling-nurse case holds at a much larger scale than it was written for —
   tested 12 Nov 2026 on row 78.** Medicine of Cosmetics runs **three fixed Adelaide
   clinics and advertises "30+ Mobile Locations"** across two states, and styles itself
   "ADELAIDE LUXURY COSMETIC GROUP" in its own header. A worker flagged it as exactly the
   scale this screen exists to catch and left the call upstream, which was right. **The
   ruling, which is the existing rule rather than a new one: a mobile or outreach venue is
   not a SITE.** Count fixed premises with their own staff. The thirty-plus are "approved
   mobile locations" the clinic travels to, with booking and records running through the
   three clinics, so there is one lapsed list and it belongs to the founder, Registered
   Nurse Hayley Batson. Three sites, so this passes with one to spare. **What a big mobile
   footprint does change is the COPY, not the grade** — an opener written for a one-room
   practice reads wrong to a business serving two states, so the mobile network belongs in
   `scale_signals` where whoever writes the email will see it.

   **And the newest converse, found in coastal Orange County on 11 Nov: a tenancy running
   the other way.** An independent injector books through
   `alumamedicalaesthetics.myaestheticrecord.com` and her footer reads "Powered by Aluma",
   so her diary and her list sit inside **another business's** practice-management tenant.
   The room-renting case qualifies because one person still decides marketing AND owns the
   list; this one fails, because she decides her marketing and does not own the list. **So
   the question behind this must-have is not how many addresses there are but whether the
   person we would be writing to can sell us the list we would be reactivating.** A
   `<someone-else>.<platform>.com` booking subdomain is a must-have 3 question, not just a
   platform detection.
   **A THIRD SPECIES OF THE INVERTED TENANCY, AND IT WEARS AN AUSTRALIAN GENERAL-PRACTICE COSTUME —
   found 18 Nov 2026 in Brisbane's south and west.** The Aluma case fails a clinic whose diary and
   list sit inside another business's practice-management tenant. **Apex Aesthetics books both of its
   sites through `automedsystems.com.au` on its HOST GENERAL PRACTICES' OWN PATHS** — so the booking
   system is not merely a third party's platform, it is a third party's *instance of* that platform,
   belonging to the practices whose rooms it uses. The lapsed list is in the GPs' software. **Fails
   must-have 3.**

   **The discriminator, now tested three clinics against one on a single night: whose tenant holds
   the diary.** Three clinics in that sweep worked out of host rooms; **two passed and one failed,
   and the only difference was the tenant.** A clinic renting a room and running its own Timely,
   Fresha or Dapple account passes — it owns the list. A clinic whose booking link resolves into the
   host's own system fails, however independent its branding. **So check where the Book button
   actually resolves to before counting a room-renter as a buyer** — and note that in Australia the
   host is often a general practice, which makes this a must-have 2 question at the same time.

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
**"DEPARTMENT OF VETERANS' AFFAIRS" IS THE WRONG GREP, AND "HEALTH CARE CARD" IS A NEW TELL —
correcting my own 12 Nov rule on 15 Nov 2026, three days after writing it.** A Melbourne clinic's
privacy policy says only **"Veterans"**, inside the phrase *"(Health Care Card, Veterans, Private
Health fund etc)"*. The long form would have missed it. **Health Care Card is the better find of the
two: it is a Commonwealth concession card, and no cash-pay cosmetic clinic has any reason to record
one.** So the Australian must-have 2 vocabulary is **Medicare, Medicare rebate, bulk billing,
MyMedicare, HICAPS, Veterans (in any form), Department of Veterans' Affairs, DVA, Health Care Card,
concession card, health fund, private health insurer and claiming** — and HICAPS, the word the first
version of this rule was built on, now stands at **0 of 61 clinics across four metros.**

**THE UNITED STATES HAS ITS OWN VERSION OF THIS SCREEN AND IT IS THE HIPAA NOTICE OF PRIVACY
PRACTICES — found 17 Nov 2026, with a discriminator precise enough to be worth the fetch, and one
caution of mine attached.** The Australian lesson is that the billing admission hides in the legal
document rather than on the menu. The American equivalent is the NPP, and two clinics from the same
template family split on **one sentence**:
- **La Vie MD's NPP says: *"we will submit protected health information about you to your insurance
  company in order to receive payment."*** Graded **C on must-have 2** — despite must-haves 3 and 4
  both passing and despite the founder-owner being exactly our buyer.
- **Angell Medical Spa's NPP does NOT say it.** Its only payer sentence is the **statutory self-pay
  restriction right** — the patient's right to stop a disclosure when they pay out of pocket — and it
  never mentions submitting anything to an insurer. **Passed, and its 16 Nov must-have 2 flag is
  closed.**
**So the test inside the document is: does the clinic say it SUBMITS to a payer, or only that a
patient MAY RESTRICT a disclosure if they self-pay?** The first is a third party deciding whether
treatment is paid for, which is what must-have 2 exists to exclude. The second is a statutory right
that every covered entity must recite and that a pure cash-pay practice recites too. **One sentence
apart, opposite answers.**

**MY CAUTION, WHICH THE NEXT TWO OR THREE US RUNS SHOULD SETTLE: payment language in an NPP is
substantially boilerplate, because the notice's job is to enumerate HIPAA's permitted disclosures and
"Payment" is one of them.** A template will often carry the submission sentence whether or not the
practice bills anyone. **What makes the rule worth keeping anyway is the Angell case: within one
template family, some practices delete that sentence and some keep it, so keeping it carries some
information.** But the rule is on probation, and the test is cheap and self-executing: **read the NPP
on the next several US clinics and count how many carry the submission sentence. If it is nearly all
of them, the sentence is uninformative and this screen dies** — and a row parked on it should then be
re-read rather than inherited. **Record the count whenever you read one.** The worker that found this
graded La Vie C rather than clearing a must-have on the argument that a clinic's own legal notice does
not mean what it says, and wrote the evidence both ways into the row; that was the right call under
uncertainty, and it is cheap to reverse if the count comes back near-universal.

**THE LESSON IS NOT ABOUT AUSTRALIA. A SCREEN WRITTEN FROM ONE OBSERVED PHRASE WILL MISS THE SAME
SCHEME UNDER ANY OTHER PHRASING.** Twice in one week an Australian billing instruction of mine was
too specific — first HICAPS, then the long form of the department's name. **Screen for the SCHEME and
list several of its names**, and when writing a screen off a single page, ask what else the same fact
could be called.

**THE AUSTRALIAN POLICY SCREEN HAS A PRECONDITION THAT FAILS OFTEN, AND IT MUST BE REPORTED AS ONE
OF THREE OUTCOMES RATHER THAN TWO — measured 15 Nov 2026.** The 12 Nov rule says to read the privacy
policy for "Medicare rebates" and "Department of Veterans' Affairs" on any Australian clinic about to
be graded B or A. **Three of five accepted Sydney clinics have no privacy policy at all**, which
reproduces the same finding from the 18 Oct Sydney sweep. So the screen returns **clean, dirty, or
absent**, and "absent" is not "clean" — it means the strongest single check available in Australia
could not be run on that row, and the row should say so. Where a policy did exist it paid twice in
one night: one clinic's policy **was where its address was published.**

**AND THE REPLACEMENT SCREEN FOR A POLICY-LESS AUSTRALIAN SITE: A SCHEME NAME IN THE NAVIGATION.**
Northbridge Medical Practice carries **"MyMedicare"** as a nav item — the Commonwealth patient
registration scheme — which settles must-have 2 against it for zero policy fetches, and is the first
Australian row decided that way. Add it to the Australian billing vocabulary alongside "Medicare
rebates", "Department of Veterans' Affairs", "bulk billing" and HICAPS: **MyMedicare on the menu is
the reimbursed arm announcing itself.**

**A QUERY FINDING THAT COST SEVEN OF TEN RESULT SLOTS: IN AUSTRALIA THE WORD "COSMETIC" PULLS
DENTISTS.** On the upper north shore, "cosmetic <towns>" returned cosmetic dentistry for seven of ten
slots. **Use "injectables" as the modifier in Australian queries**, not "cosmetic" — which also sits
alongside the standing Australian finding that a high-street *medical* address is usually a general
practice. The country's search vocabulary is owned by two other professions.

**AND THE GENERAL FORM OF THAT RULE, WHICH IS NOT ABOUT AUSTRALIA AT ALL: AN ABSENT NAV CATEGORY IS
NOT AN ABSENT SERVICE — found 16 Nov 2026 in the US Midwest.** Cool Blue Image's navigation shows no
injectables anywhere; **one fetch of the site found them.** No advertising rule forces that — it is
simply how small clinic sites get built, with a short nav and the detail a page deeper. So the
Australian TGA finding is the strong case of a weaker rule that holds everywhere: **a menu is evidence
of what a clinic chose to put in its menu.** Where must-have 1 turns on a service being absent, spend
one more fetch before recording the absence, and say which pages you read. The mirror image is already
in this file as the two-edge rule — **a service page with a URL is selling, a sentence in a bio is
mentioning** — and this is its third edge: **nothing in the nav is not nothing on the site.**

**IN AUSTRALIA THE ABSENCE OF A NAMED INJECTABLE IS NOT EVIDENCE OF ANYTHING, AND READING IT AS
EVIDENCE HAS QUIETLY COST ROWS — found 15 Nov 2026 on row 1224.** Byron Eve's Cosmetic Services page
names exactly two services, "Cosmetic Consultations" and "Cosmetic Tattoo", and then says in its own
words that **prescription treatments are not named or priced online and are discussed privately at
consultation.** That is the TGA-mandated way an Australian clinic sells prescription injectables, not
an empty menu — a clinic two suburbs away publishes a post titled *"Updated Terms for Cosmetic
Services for TGA Regulations"* for the same reason, and the same rules are why **our own copy** may
not name these medicines. We have been applying the rule to ourselves and forgetting it applies to
them.

**SO IN AUSTRALIA MUST-HAVE 1 IS READ OFF THE PRESCRIBER, THE CONSULTATION COPY AND THE BALANCE OF
THE MENU — never off whether an injectable is named.** The test separated two skin-led clinics on one
night. **Byron Eve** names a Division 1 Registered Nurse in its footer with her registration number,
runs a dedicated `/cosmetic-injectables-clinic-brisbane/` landing page, and hedges in TGA language —
so it does sell injectables, and it fails only on the balance of what it predominantly sells, which
is a different and weaker finding. **The Skin Fairy** (Perth, two sites, founded January 2015,
Timely, gift vouchers — a grade-A shape on every other must-have) names no nurse, no doctor and no
prescriber at all, bills its practitioners as "Dermal Therapist", and uses the word "prescribe" only
about at-home skincare. That one genuinely has no injectable line. **Look for the prescriber, not the
drug.** A clinic with no prescriber named anywhere cannot be selling prescription medicines; a clinic
with one and a TGA-shaped hedge almost certainly is.

**AND A FREE DATING ARTIFACT THAT ARRIVES WITH THE AUSTRALIAN POLICY FETCH YOU ARE ALREADY SPENDING
— added 15 Nov 2026.** A privacy policy that declares itself **"current from 28th August 2018"**
attests the business existed in August 2018. That is a dated artifact on the ladder's plainest
reading, and because the must-have 2 screen already sends you to the policy on every Australian
clinic about to be graded B or A, **the dating comes free on every clinic we screen.** It settled row
1222 alongside a dated post archive.

**BOTH RUNGS WERE TESTED TWICE ON 17 NOV 2026, BY TWO WORKERS WHO DID NOT KNOW OF EACH OTHER, AND
THEY RETURNED OPPOSITE VERDICTS. THE DISAGREEMENT RESOLVES CLEANLY AND IT SPLITS THE TWO RUNGS APART
— ONE OF THEM WORKS AND THE OTHER IS NEARLY WORTHLESS. READ BOTH HALVES.**

**THE SUMMARY, UP FRONT, BECAUSE THE DETAIL BELOW WAS WRITTEN IN TWO SITTINGS AND THE FIRST SITTING
WAS WRONG:**
- **THE POST-ARCHIVE RUNG WORKS.** Worker two fired it twice and both firings were decisive, both
  producing a **grade A** (Ageless MD Solutions, oldest post 9 Jul 2018, a floor of 8.4 years;
  Mindful Med Spa, 28 May 2019, 7.5 years). **Keep it and spend its fetch FIRST.**
- **THE POLICY-DATE RUNG IS NEARLY WORTHLESS AS A FLOOR.** Across both workers it fired nine times
  and was decisive once. Worker two's six floors: 22 months, 18 months, 22 months, 6 weeks, 8
  months, and one good one. Worker one's three: all 2024, all inside or below row 720's failing
  band. **Do not park or clear a row on a policy date, and do not spend a fetch on one for dating
  alone** — fetch the policy for the must-have 2 screen, which is what it is actually good for, and
  take any date on it as a bonus.
- **WHY THE TWO WORKERS DISAGREED ABOUT THE POST-ARCHIVE RUNG: ONE GUESSED `/blog` AND THE OTHER
  ENUMERATED THE FOOTER.** Worker one guessed paths and 4 of its 7 blog fetches returned zero bytes.
  Worker two read the header and footer href sets first, and **both of its archives were behind
  unexpected nav labels — "Videos & Articles" and "Resources".** Neither was at `/blog`. **So the
  rung's measured failure in the first cohort was a measurement of path guessing, not of the rung**,
  and the method fix at the bottom of this section is not a refinement, it is the whole thing.

**WHAT FOLLOWS IS THE FIRST SITTING'S WRITE-UP, KEPT BECAUSE ITS REASONING ABOUT THE POLICY RUNG AND
ABOUT MY OWN OVER-GENERALISATION STILL HOLDS.** Where it says "both rungs returned nothing", read
"the policy rung returned nothing and the archive rung was never reached".

**THE FIRST COHORT: 21 ROWS, 0 CLEARS FROM EITHER RUNG.
I BUILT A BACKLOG ON THESE TWO RUNGS AND THAT COHORT DID NOT PAY.**

On 15 Nov I wrote these two rungs up and inferred from them that 22 pipeline rows parked solely on
must-have 4 were cheap recoveries. One of the 21 worked rows cleared, **and it cleared on the
ladder's ORIGINAL rung one — a stated founding year — found by accident on a page requested as a
policy.** Neither new rung produced a single clear. The measurements:
- **Rung 2, the policy's self-declared date.** Attempted on 19 rows. **A policy document loaded on
  6 (32%)**; of those 6, **3 carried a usable date (50%)**; of those 3, **0 cleared**. Every one
  landed in 2024 — floors of 2.0 to 2.9 years, inside or below row 720's failing band.
- **Rung 1, the archive's oldest date.** Attempted on 7 rows. **A blog loaded on 3**; none reached
  back before 2024. **0 clears.**

**THE THREE REASONS, AND EACH ONE IS A CORRECTION TO SOMETHING I WROTE RATHER THAN A SURPRISE ABOUT
CLINICS.**

**1. "The dating comes free on every clinic we screen" is true in AUSTRALIA and I generalised it off
the end of its own sentence.** Re-read the paragraph above: it earns "free" from the fact that *the
Australian must-have 2 screen has already located the policy*. Outside Australia nothing has located
it, so the fetch is a guess at a URL — and **20 of the worker's 30 fetches returned a hard client
error with zero bytes retrieved**: `/privacy-policy` missed 11 of 19, `/privacy` 4 of 4, `/blog` 4 of
7. Not even a 404 page's footer came back. **The rung is not free anywhere the policy's location is
unknown, and that is everywhere except an Australian row mid-screen.** This is the fourth time in a
week that a claim of mine, true of the procedure that produced it, was restated as a fact about the
world — after "the site publishes no address", "Australian sites do not obfuscate" and "Australia is
finished". **The tell is the same every time: a sentence that names its own scope and a next sentence
that drops it.**

**2. Rung 2 may be measuring the WEBSITE's age, not the BUSINESS's — a hypothesis worth testing
rather than a finding, offered at n=3 and with one piece of direct corroboration.** All three dates
found landed in 2024, which is suspiciously tight for three unrelated clinics. And row 422's policy
reads **"Effective Date: [Insert Date]"** — an unfilled template placeholder, which is direct
evidence that these policies are bought compliance packs rather than documents the business wrote.
**If a policy date tracks when the clinic bought its template, rung 2 is a weak floor BY
CONSTRUCTION**: it would reliably under-state the age of exactly the old, established clinics the
must-have is trying to find. **Test: find a clinic independently known to be old — a stated founding
year or a long review history — and read its policy date. If the policy is years younger than the
business, demote this rung.** Until then treat a policy date as a floor that may be far too low, and
never park a row on it.

**3. Rung 1 is structurally broken at one fetch, and the break is in the rung's own wording.** It
asks for the archive's **oldest** date; one fetch of `/blog` returns the **newest** page. Row 676 is
the proof — its oldest visible date is May 2026 with everything older behind an "Older Posts" link.
**So the rung works in a single fetch only on sites whose entire archive fits one page, which are
precisely the young sites where it pays least.** Stated as a rule: **a blog's first page is a CEILING
on nothing and a FLOOR only if you can see that there is no pagination.** Check for the pagination
control before recording an oldest date, and if there is one, either spend the fetch to reach the end
or record the rung as unreached rather than empty.

**THE METHOD FIX, IF THIS JOB IS REPEATED: stop guessing paths.** One fetch of the homepage for the
footer's real policy and blog hrefs, then one targeted fetch. That is about **two fetches per row
rather than 1.5**, and it converts the 67% hard-error rate into near zero. The worker's own verdict is
the right one: **the rungs were not what failed, the path guessing was** — but even with perfect paths
the measured clear rate on this cohort would have been low, because the dates that did load were too
young. **The seam is not 22 cheap recoveries. It is a thin seam that needs better aim.**

**THE SECOND COHORT, AND THE TWO THINGS IT ADDS BEYOND SPLITTING THE RUNGS.**

**1. A POLICY DATE IS UNRELIABLE IN BOTH DIRECTIONS, WHICH IS A STRONGER CONCLUSION THAN EITHER
WORKER REACHED ALONE — AND IT RETIRES MY "BOUGHT TEMPLATE" HYPOTHESIS BY SUBSUMING IT.** Two
mechanisms are now evidenced and they push opposite ways:
- **Policies get REWRITTEN, so the date drifts toward today and reads as a floor far younger than
  the business.** That is worker two's explanation and it fits every one of its five bad floors
  (6 weeks to 22 months). It is the dominant failure.
- **Policies are also INHERITED BOILERPLATE, so the date can PREDATE the business entirely.** The
  proof is sharp: **La Vie MD's HIPAA notice declares itself "Effective August 1, 2005" — twelve
  years before the company was founded in 2017**, refuted by the clinic's own founding statement.
  **A date that predates the business is not a floor at all**, and the ladder as written would have
  read it as a 21-year one.
**So a policy date can be years too young OR years too old, and nothing on the page tells you
which.** Treat it as corroboration for a date you already have, never as the load-bearing evidence.
(My 15 Nov hypothesis that the date tracks when the template was bought is the second mechanism and
is now evidenced; the test I proposed for it is no longer needed, because the La Vie case is that
test and it came back positive.)

**2. A NEW RUNG, AND IT IS A GOOD ONE: A REVIEW THAT CARRIES THE REVIEWER'S OWN "CUSTOMER SINCE"
YEAR.** East Town Salon & MedSpa publishes eleven reviews each stamped with a **"Customer since"**
year, running **2006 to 2019** — a floor of about twenty years, **drawn from the clinic's own booking
records rather than from its marketing copy**, which makes it better evidence than a "since" sentence
a clinic wrote about itself. **Where a review widget stamps tenure, read the oldest stamp.** It
bounds from below, and it simultaneously evidences the one thing must-have 4 actually cares about —
that a long patient history exists — rather than merely that a business is old.

**3. THE MIDDLE RUNG DID THE QUIET WORK, AND IT DID IT BY BEING ON A PAGE NOBODY HAD OPENED.** Ahern
Aesthetics and Alpine Aesthetics were both parked with "no proxy of any kind", which is the C
condition — and both publish a practitioner's career length ("Over a 20-year career", "more than ten
years") on an About or Team page the previous pass never read. **Two more grade-B releases, and two
more firings of the page-coverage rule on must-have 4 rather than must-have 5.**

**THE METHOD, RESTATED AS THE RULE RATHER THAN AS A FIX, BECAUSE IT IS NOW THE DIFFERENCE BETWEEN THE
RUNG WORKING AND NOT WORKING: ENUMERATE THE HEADER AND FOOTER HREFS BEFORE FETCHING ANY SECONDARY
PAGE. NEVER GUESS A PATH.** One homepage fetch buys the real policy, archive and reviews URLs; then
spend one targeted fetch each, archive first. That is about two fetches a row instead of 1.5, and it
is the entire margin between 0 clears and two grade As. **Expect the archive NOT to be at `/blog`** —
neither of the two that paid was, and the labels were "Videos & Articles" and "Resources".

**AND THE PAGE-COVERAGE RULE FIRED FOR THE SIXTH TIME IN FOUR NIGHTS, IN ITS SHARPEST FORM YET.** Row
700's notes recorded two absences — *"the header reads 'EST' with no year"* and *"no review count is
published"* — and both are false of the clinic: its own page carries **"EST · 2018"**, *"Since 2018"*,
**"8yrs"** and **"90+ 5-star reviews"**. Both were true of the pages the 28 Oct worker read
(`/memberships/` and the homepage header). **What makes this the sharpest instance: the row had
written its own recovery condition — "worth recovering if a founding year ever surfaces" — and the
founding year was already there, one page over, on the day the condition was written.** A row that
names what would release it, and is released by the thing it already had, is the whole rule in one
line.

**A DATED POST ARCHIVE IS A RUNG-ONE ARTIFACT, AND WHAT COUNTS IS ITS OLDEST DATE RATHER THAN ITS
EXISTENCE — three instances in one batch, 15 Nov 2026.** Eleventh Heaven's journal runs 18 September
2017 to 2026 and settles a parked row at nine years; The Aesthetic Company's reaches back only to
June 2024, which is a floor of about 2.4 years and fails the substance half on row 720's precedent;
Aesthetics By Boss's is 2026-only and evidences nothing. A blog is not an artifact. **Its oldest
date is.**

**AND THE REFINEMENT THAT MATTERS MOST HERE: A DATE CAN BOUND TRADING FROM BELOW OR FROM ABOVE, AND
THE TWO HAVE OPPOSITE CONSEQUENCES.** Everything the ladder lists bounds from **below** — an oldest
post, a review count, a "since", a copyright range all prove the business is *at least* so old, and
that is what satisfies must-have 4. But a founding statement bounds from **above**: 704 Aesthetics'
only year is *"moved to Charlotte in 2021 and co-founded"*, which caps the clinic's age at about
five years rather than establishing a floor under it. **A ceiling satisfies must-have 4 only if the
ceiling itself clears the substance test**, and it *refutes* must-have 4 outright when the ceiling
falls inside row 720's failing band of two to three years. Say which direction the date you found
bounds in, because the ladder as written reads as though every date were a floor.

**AND ITS SIBLING, WHICH IS THE SAME QUESTION ASKED OF THE SUBJECT RATHER THAN THE DIRECTION: WHOSE
BUSINESS IS THIS NUMBER ABOUT? Three independent instances in one night, 17 Nov 2026, across three
different must-haves — which is what promotes it from a coincidence to a rule.**
- **Must-have 4.** **Jewell Medical Spa**'s only trading-life sentence is *"establish one of the top
  medical spas in Naples in just three short years"* — **about the owner's FIRST spa**, which he
  left; this clinic is *"his second medical spa"*. Three nights carried as the best name in the file,
  settled as a C.
- **Must-have 3.** **Ahern Aesthetics** is one site in Park City, and its page says its founder
  *"grew the franchise to over 10 locations"* — **her CV, not this clinic's footprint.** Our own
  site-count audit flagged the row on that sentence; the row had already flagged it as a trap for
  whoever writes the email, and was right.
- **Neither must-have, but the same shape: our own records.** A grep of the pipeline for "Ahern" and
  "Alpine" returned one hit each, and both hits were **inside another row's prose** — a note naming
  them as leads to work — which would have read as "already held" and skipped two grade B rows.
**So the ladder's rungs all need a subject as well as a direction.** An owner's previous venture, an
owner's career length, an owner's residency, a franchise they used to run, and a sibling brand all
produce confident, specific, verifiable numbers that are **true of something other than the business
we would be writing to**. The clinic is not lying; we are reading a CV as a balance sheet.
**The practical test is one question asked of every figure before it is used: is this number about
THIS premises, THIS trading entity, THIS patient list?** A founding year that belongs to a prior
business bounds nothing. A site count that belongs to a former employer disqualifies nobody. And the
expensive direction is not the one that over-states a clinic — it is the one that **writes to a
stranger's achievements**, because an opener congratulating an owner on ten locations she no longer
has is worse than no opener at all.

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
   **AN "ABSENT" MUST-HAVE 5 VERDICT IS A CLAIM ABOUT THE PAGES YOU READ, NOT ABOUT THE CLINIC —
   and it was wrong twice in the same direction on 15 Nov 2026.** Two clinics this file recorded as
   publishing no email address of any kind, explicitly *"not obfuscated - simply absent"*, both
   publish one, and neither needed a browser. **Parlour Dala's** is plain visible text under the
   label "Email:" on the very contact page the file had marked absent. **Dr Cosmetist's** is the
   sharper case: its contact page carries `info@drcosmetist.com` three times and **only inside meta
   tags** — which is the sixth look-alike below and correctly not a publication — while its about
   page and its privacy policy both carry the identical string as plain visible body text, which is.
   **One clinic failing and passing must-have 5 on different pages of its own site.** Had the worker
   stopped at the contact page the row would have been parked on must-have 5 and the park would have
   been wrong; the instruction to spend the policy fetch is what caught it. **So where a row or a
   near-miss says "no address published", it must say WHICH PAGES WERE READ** — "the contact page
   publishes nothing" and "the site publishes nothing" are different claims, and the second one is
   expensive to get wrong. This is the same shape as the row 149 `robots_disallowed` finding arriving
   through page coverage instead of permissions.
   **IT FIRED THREE MORE TIMES ON 16 NOV 2026, AND THE THIRD ONE BREAKS A MARKET-WIDE CLAIM. The
   rule has outgrown must-have 5: it is about every ABSENT finding, and about claims at every scale.**
   - **Third instance, same must-have, and it was MY OWN claim.** The 15 Nov standing list records
     of **Flawless Rejuvenation** (Toorak) that it "publishes no address anywhere, and no browser
     recovers that". Its **privacy policy** publishes `reception@flawlessrejuvenation.com.au` in
     plain text with a matching mailto. It is now row 1264 and **the only grade A of the Melbourne
     pass**. I wrote the "say which pages you read" rule the same night I published that claim about
     a clinic whose policy I had not read. Writing a rule down does not apply it to the sentence in
     the next paragraph.
   - **Fourth instance, and it is NOT must-have 5 — which is how we know the rule generalises.**
     **Panacea Skin Clinics** (row 1281) was recorded as naming "NO owner, founder or director
     anywhere", and that absence was given as one of two reasons the row is not a grade A. The
     homepage and the privacy policy do not name an owner. The **About page says "Panacea was
     founded by Dr. Kippen"**. So the missing grade-A leg was never missing; the pages holding it
     were never opened. **Four firings, three different findings (must-have 5 ×3, the owner-name
     leg ×1): the rule is not about addresses. ANY "absent" verdict — no owner, no review count, no
     founding year, no loyalty scheme, no billing language — is a claim about pages, and must name
     them.** The three-outcome policy screen already works this way; this is the same move applied
     to every field.
   - **Fifth instance, and it is the expensive one: A MARKET-WIDE CLAIM WAS A CLAIM ABOUT PAGE
     COVERAGE.** This file asserted, on **five independent reproductions**, that **Australian clinic
     sites do not obfuscate** — that Australia's problem is silence, not masking, and that a browser
     list is therefore worth less in AU than in the US. On 16 Nov **Cronulla Cosmetic**'s privacy
     policy shipped a `/cdn-cgi/l/email-protection#` token and rendered `[email protected]`. The
     helper volunteered the decode and the worker declined it, correctly. **The token was on the
     POLICY. Both of that clinic's contact pages publish nothing.** Five sweeps looked for
     obfuscation where obfuscation is usually found — contact pages — and the thing survived one
     page over. **A claim reproduced five times is still only a claim about the procedure that
     reproduced it.** What is *not* overturned: Australia's dominant failure is still silence, 6 of
     13 published a mailbox in this sweep. What IS overturned is "a browser recovers nothing in
     Australia" — it recovers this. (Cronulla Cosmetic is disqualified anyway, on must-have 2: its
     policy says "to Medicare, insurance companies in relation to claims." The finding stands
     independently of the row.)
     **CORRECTED AGAIN ON 17 NOV 2026, AND MY EXPLANATION IS THE PART THAT WAS WRONG.** Three more
     Australian Cloudflare clinics turned up in one night — **Face Fit** (Southport, Gold Coast),
     **Appearance Clinic Australia** and **SkinMetics** (Melbourne) — taking the count to **four in
     two nights**, so the claim is reversed rather than merely falsified. But look where Face Fit's
     token was: **on its CONTACT page** — the obvious page, the page all five earlier sweeps were
     already reading. **So "the earlier sweeps were looking at the wrong pages" does not survive.**
     The procedure was fine. **The rate is simply low: roughly 2 in 75 clinics across six Australian
     metros, against about a third in some US markets.**
     **THE EPISTEMIC LESSON IS THE DURABLE PART AND IT IS SHARPER THAN THE ONE I DREW: A LOW RATE AND
     A BLIND SPOT LOOK IDENTICAL AT n=5.** Five sweeps finding no obfuscation is the *expected*
     outcome of a 3% rate. I read that run of zeroes first as a property of the market, and then,
     when it broke, as a flaw in our procedure — **two different stories, both of them attempts to
     explain away a number that was simply small.** Before concluding a market *never* does
     something, ask what n you would need to see it once at a plausible low rate: at 3%, five sweeps
     of fifteen clinics is close to a coin-flip. **The right response to a run of zeroes is a
     confidence interval, not a property.**
   **THE COMMON SHAPE, STATED ONCE because it is this project's most-repeated failure and it now has
   an instance at every scale — one field, one row, one market:** a negative finding is evidence
   about the procedure that produced it, never about the world. The fix is never "look harder"; it is
   to **state the procedure alongside the finding**, so the next reader can see what it could not
   have seen. "The contact page publishes nothing" is checkable and survives. "The site publishes
   nothing" is a guess wearing a finding's clothes.

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

**AND THE RULE HAS A MIRROR IMAGE THAT COST US TWO ROWS' WORTH OF FALSE HOPE — 9 Nov 2026.**
"A label is not a finding" says a row parked on a bare noun is unscreened rather than failed. The
mirror is: **a row whose PARKED REASON has been checked and dismissed is also unscreened — it is
not thereby passed.** On 8 Nov a batch note declared of nine "single-operator" rows that "no
must-have has been shown to fail". That was wrong on two of them, and wrong the same way both
times: **the note audited the parked reason and never read the menu.** Row 201 turned out to carry
a full surgical menu — rhinoplasty, facelift, breast augmentation, tummy tuck, liposuction — with
two FRCSC plastic surgeons and "2,500+ rhinoplasties", and is now disqualified on must-have 1. Row
202's recorded website was a different business altogether.

**So "parked on nothing" and "qualified" are different claims, and only the second needs the menu
read.** Both halves of this are the same error: **deciding a must-have from metadata about the row
rather than from the clinic's own page.** A retired rule tells you the old reason is void; it tells
you nothing about whether a current rule fails.

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

**AND ON 10 Nov 2026 THE TEST FAILED A CLINIC FOR THE FIRST TIME IN THIS SERIES, WHICH IS THE BEST
THING THAT COULD HAVE HAPPENED TO IT.** After clearing the clinic five times out of five in
Westchester and twice more in the recovery pass, the label test was starting to look like a rule
that only ever says yes — and a test that always returns the same answer is not a test. In Chevy
Chase it failed one: a self-described "board-certified dermatology practice" with three physicians
and **"Skin Cancer" listed as a treated concern**. **That is the rule working, not breaking.** The
rule never said "dermatology does not disqualify"; it said *read the menu*, and here the menu
disqualified the clinic. The mirror fired in the same market and cleared a clinic whose medical
director's title reads "Surgeon" with no surgical line anywhere on the site.
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

**THAT LIST WAS BADLY WORDED AND IT COST A GRADE-A ROW A FALSE ACCUSATION — corrected 10 Nov 2026,
and the wording was mine.** Putting "varicose veins" in the same list as "venous insufficiency",
"phlebology" and "vein disease" implies the WORD "varicose" is disease language. It is not, and a
careful worker reading the list as written reported a grade-A row as failing must-have 2 because
its sclerotherapy copy says "varicose and spider veins". A direct fetch upheld the row: its actual
wording is *"Say goodbye to unsightly varicose and spider veins"* and *"Reduce the APPEARANCE of
spider and varicose veins"*, it names no medical vein condition anywhere, and it bills nothing.

**So the list is split, because the two halves do different work:**

- **"Varicose" and "spider" are APPEARANCE words and are neutral.** A varicose vein is a visible
  thing a patient dislikes the look of, and treating that look is what a med spa does. The word
  alone resolves nothing — read what the sentence around it is promising. *"Reduce the appearance
  of varicose veins"* is cosmetic; *"Varicose Vein Treatment"* under a **VEIN CENTER** heading
  beside *"Vein Disease Treatments"* is not.
- **"Vein disease", "venous insufficiency", "phlebology", "duplex scanning", "reflux" and a named
  vein clinic or centre are DISEASE language, and any one of them fails must-have 2.** These
  describe managing a condition rather than improving an appearance.

**A THIRD RUNG, FOUND 11 NOV, AND IT INVERTS THE TEST: DISEASE LANGUAGE USED TO REFER A PATIENT
OUT IS EVIDENCE THE ROW PASSES.** Row 178 (PhillyMedClub) was reported as failing must-have 1 on
copy reading *"visible leg veins are frequently a surface sign of venous disease"* and *"needs a
duplex ultrasound and a vein specialist before anyone treats the appearance"*, plus referrals to a
plastic surgeon and to *"the oculoplastic service at Penn"*. **Every quote was accurate and the
conclusion was backwards.** A direct fetch shows all of them sitting inside a block the clinic
headed **"Sometimes the right treatment isn't one we offer"** — its own referral-out policy, which
also declines liquid rhinoplasty and PRP into hips, and which names Wills Eye Institute and Penn as
where to go instead.

**A referral-out block necessarily contains the vocabulary of every business the clinic is NOT.**
That is what the block is for. So the word list cannot be run over a page as a flat grep; it
screens for **what the clinic SELLS**. Before failing a row on disease language, read whether the
sentence is selling the treatment or declining it:

- **Selling it fails.** Row 130 (The R Clinic, struck 11 Nov) lists "Venous Ulcer", "Venous Eczema"
  and "DVT" as conditions it treats, sells "Endovenous Thermal Ablation" and "Ultrasound Guided
  Sclerotherapy", employs a sonographer to map leg veins, and publishes a dedicated `vein@` mailbox.
- **Declining it passes, and passes well.** Row 178 tells the reader to see a vein specialist.

**The two pages share most of their vocabulary and are opposite businesses.** And the honest
reading of row 178 is better than neutral: a clinic that publishes what it will not treat is
unusually straight with patients, which is a good prospect rather than a borderline one.

**The same rung applies to "dermatology", which is where two of the 11 Nov claims went wrong.**
Rows 89 (Skin to Love) and 110 (MediZen) were both reported as dermatology-positioned on the
strength of a "Dermatology" nav item. Both sell private consultations for lumps, bumps, warts,
moles and cysts as **one line on an injectables-led menu**, neither bills a practitioner as a
dermatologist, and 89's own title tag reads "Non Surgical Skin Treatments" while 110's meta
description reads "doctor-led, CQC-registered aesthetic clinic". **A service line is not a
positioning.** Contrast row 107 (Lumiere, struck 11 Nov), whose own welcome sentence reads
*"a Dermatologist and Plastic Surgeon-led clinic"* and whose menu sells Blepharoplasty, Breast
Enlargement and VASER Liposuction: there the clinic says what it is, in its own words, and sells the
thing. **The test for must-have 1 is the clinic's own self-description plus what is on the menu, not
the presence of a word in the nav.**

**AND THE SERVICE-LINE RULE GOT ITS OTHER EDGE THE VERY NEXT DAY, BY PRODUCING AN UNDER-CALL —
12 NOV 2026.** The rule above was written from one direction: two rows had been wrongly reported as
dermatology-positioned on the strength of one nav item, so the rule says a service line is not a
positioning. A re-verification worker applied it correctly to row 100 (The Skin Clinicians,
Brisbane) and cleared the row. **A direct fetch disqualified it.** What is there is not a nav item:
a top-level nav category **"MEDICAL"** whose own service pages are `/medical/skin-checks/` and
`/medical/mole-removal/`; a homepage section headed **"Dermatology and Skin Cancer"** listing *"Skin
cancer screenings and treatments"* and *"Surgical excisions"*; a hero heading reading *"Aesthetic
Treatments, Mole Checks & more"*; a medical practitioner holding *"the Certificate of Skin Cancer
Medicine and the Certificate of Dermatoscopy"* who *"excises suspicious lesions and moles, treats
skin cancers"*; and a principal clinician credentialed MNP(Neurology and Dermatology). The clinic
calls itself *"a trusted medical clinic"* and *"Medically led"*.

**AND THE AUSTRALIAN FORM OF THIS FAILURE HAS A NAME NOW, FROM THREE INDEPENDENT SIGHTINGS IN ONE
NIGHT: IN AUSTRALIA THE REIMBURSED ARM ARRIVES AS A SKIN-CANCER CLINIC BOLTED ON, NOT AS AN
ACRONYM.** The US tell was a "Primary Care" heading beside "if not covered by insurance"; the
Canadian tell was private extended health; Australia's is skin checks, mole mapping and lesion
excision sitting next to the injectables. Three sightings on 12 Nov, in two metros, by two workers
who never spoke:

- **Row 100 (The Skin Clinicians, Brisbane) — disqualified on it.** A "MEDICAL" nav category whose
  service pages are skin checks and mole removal, a homepage section headed "Dermatology and Skin
  Cancer" listing surgical excisions, a practitioner holding the Certificate of Skin Cancer
  Medicine and the Certificate of Dermatoscopy.
- **Youth Lab (Perth) — blocked.** Five sites AND a separately branded "Shade Skin Cancer Medicine"
  sibling.
- **Ultimate Aesthetics (Perth) — still our best Perth prospect**, with "skin cancer excisions"
  named in a staff bio and nothing else pointing that way.

**Why this matters more in Australia than the American version does in America: skin checks are
routinely Medicare-rebated here, so a skin-cancer line is a live must-have 2 risk as well as a
must-have 1 question** — even when, as in all three cases tonight, the page names no Medicare at
all. **But the three outcomes differ, and the difference is the rule above, not the words.** A
separately branded sibling clinic and a named clinical division with its own service pages are
businesses; a sentence in one practitioner's biography is a credential. **So read where the
skin-cancer work lives: on the menu and in the nav, or in a bio.** Ultimate Aesthetics stays a
prospect precisely because it is the latter.

**So the rule has two edges and needs both stated, because each one alone produces an error:**

- **A WORD is not a positioning.** "Dermatology" in the nav, or in a founder's bio describing her
  own past experience, with no dermatologist on staff and an injectables-led menu — rows 89, 110
  and 25 all cleared on this.
- **A NAMED CLINICAL DIVISION is.** Its own nav category, its own service pages, a credentialed
  practitioner, and procedures it performs — row 100 fails on this, as do rows 107 and 83, whose
  surgery is on the menu rather than in a bio.

**The test that distinguishes them in one question: is the clinic SELLING this as a line of
business, or mentioning it?** A service page with a URL is selling. A sentence in a bio is
mentioning. **And note what did NOT decide row 100: must-have 2 is clean there** — *"No referral is
required for these services"*, no Medicare, no HICAPS. It fails on what kind of business it is, not
on how it is paid, which is the distinction must-have 1 exists to make.

**FOURTH EDGE, 16 Nov 2026, and it is the cleanest instance the rule has: THE SURGERY IS REAL, IT IS
PERFORMED, AND THE ROW STILL PASSES — because it is performed somewhere else.** **Panacea Skin
Clinics** (row 1281) describes itself in its own words as *"Led by Dr John Kippen, Specialist Plastic
& Reconstructive Surgeon"*, which is this file's own named disqualification, and its About page
contains the sentence *"breast, abdominal and facial surgery where medically indicated"*. The
sourcing worker, who had not read that page, cleared the row on the Chevy Chase precedent and wrote
that there is *"NO surgical procedure named anywhere - no breast work"*. **That claim was false and
the verdict was right**, and the gap between those two facts is the rule:
- The sentence sits in **Dr Kippen's biography**, describing the practice he runs at Sydney
  Adventist Hospital, Macquarie University Hospital and Pittwater Day Surgery.
- It is **not a bookable service, has no service page, no price, no nav entry, and is not at either
  Panacea address**. Panacea's whole menu is skin and *"Wrinkle & Volumising Treatments"*, injected
  by two Registered Nurses.
- **Had that sentence hyperlinked to a procedure page, the row would be disqualified.** It does not.
**So the discriminator is not whether surgery is NAMED, nor whether it is PERFORMED, nor even
whether the owner performs it — it is whether THIS BUSINESS SELLS IT.** A surgeon's non-surgical
clinic is a med spa whose medical director happens to operate elsewhere; that is a different animal
from a surgical practice with a skin room attached, and the thing that tells them apart is the menu,
every time.
**The process lesson, which matters more than the row: a worker's VERDICT and a worker's EVIDENCE
can come apart, and checking the verdict is not checking the evidence.** The decision survived the
fetch; one of the four sentences supporting it did not. Had the next reader relied on *"no surgical
procedure named anywhere"* for a different clinic sharing that shape, the inherited sentence would
have done the damage, not the grade. **When a row names the one check that would overturn it, spend
the fetch — and read what it says about the row's REASONING, not just its answer.** That fetch also
recovered the owner's name this row was marked as lacking, so one fetch corrected a false supporting
claim, closed a grade-A gap, and confirmed the verdict.

**Worth holding onto about the process rather than the rule: the under-call and the two over-calls
came from the same sentence being written from one direction.** A rule derived from errors in one
direction will produce errors in the other until somebody hits them. So when a rule is written off
a correction, ask what the opposite mistake looks like and write that edge too, before a worker
finds it for you.

**The same row pair settled it in one day, which is why it is written as a rule.** Row 179 passes
on cosmetic framing with no condition named; **row 177 was disqualified the same hour** for running
a "VEIN CENTER" with "Varicose Vein Treatment" and "Vein Disease Treatments" as named services —
and separately for surgical liposuction and FUE transplantation. **One of those rows says
"varicose" and passes; the other says "varicose" and fails. The word was never the test.**

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
CHEAPEST MUST-HAVE 2 FAILURE THERE IS — added 9 Nov 2026.**

**AND IN AUSTRALIA THE PHRASE TO LOOK FOR IS "HICAPS" OR "ALL HEALTH FUNDS" — added 10 Nov 2026,
and it is the cheapest must-have 2 failure in that market.** One Hobart clinic says in its own
words: *"We work with ALL health funds and have Hicaps available for on the spot claims"*. HICAPS
is the Australian on-the-spot private-health claiming terminal, so naming it is a clinic telling
you directly that a third party reimburses part of its revenue.

**BUT HICAPS WAS THE WRONG THING TO TELL WORKERS TO LOOK FOR, MEASURED 12 NOV 2026, AND THAT
INSTRUCTION WAS IN ALL THREE AUSTRALIAN BRIEFS THAT NIGHT.** A Brisbane sweep of 19 clinics found
**zero** printing HICAPS anywhere; a Perth sweep of 11 found zero; a Sydney sweep of 15 found zero.
**Forty-five Australian clinics, not one HICAPS.** The Hobart row above is real and the word still
fails a clinic on sight — it is simply rare, so an instruction built around it finds nothing.

**THE AUSTRALIAN TELL IS "MEDICARE REBATES" AND "DEPARTMENT OF VETERANS' AFFAIRS", AND IT LIVES IN
THE PRIVACY POLICY RATHER THAN ON THE MENU.** Brisbane's policy fetches flipped 2 of 5 clinics that
had looked clean:

- **Vara Aesthetics:** *"We cannot provide Medicare rebates or access to Veterans affairs
  entitlements without properly identifying you."*
- **Skinthetics:** *"Medicare number (where available) for identification and claiming purposes"*,
  *"health fund details"*, and disclosure to *"your health fund, Medicare, or the Department of
  Veterans' Affairs"*.

**Neither says anything about billing on its public pages.** Sydney produced a third the same night:
**drJ Clinics**, whose homepage carries zero insurance language and whose policy reads *"To
Medicare, the Department of Veterans' Affairs, or private health insurers, in connection with
billing."* **That row would have shipped as a sendable B.**

**So this is the Montgomery County finding in an Australian accent, and it is now the strongest
single-fetch screen we have: a market that does not advertise its billing still has to name the
scheme in its policy, because the policy is a legal document and the menu is marketing.** The
corollary for a brief: in Australia the privacy policy is not the last resort for an address, it is
a must-have 2 screen worth running on any clinic you are about to grade B — three sendable rows in
one night were caught by it and none by a menu. **Zero policy fetches, decided off
the page you were already reading.** This is the same ruling as NYSHIP on an American menu and as
the Canadian private-extended-health failure, in the third market — so read it as the general
shape: **a named claiming system, scheme or terminal beside a service line is a reimbursed revenue
stream admitting itself.** Watch for it especially on AU dental, physiotherapy and podiatry arms,
which almost all say it.

**AND THE OPPOSITE WARNING, ADDED 10 Nov 2026 BECAUSE IT WILL KEEP READING LIKE A FAILURE AND IS
NOT ONE: HSA AND FSA ACCEPTANCE IS NOT A MUST-HAVE 2 FAILURE.** A Health Savings or Flexible
Spending Account is **the patient's own money**, set aside pre-tax and spent at their discretion.
A clinic accepting it has no third-party payer and no non-discretionary revenue stream — it is
cash-pay with a tax wrapper. Two Montgomery County clinics advertise it and both pass. The word
"insurance" does not appear and must not be inferred.

**The test that separates these cleanly: does a third party decide whether the treatment is paid
for?** HICAPS, NYSHIP, a named health fund, Medicare, "we bill your insurer" — yes, so must-have 2
fails. HSA, FSA, CareCredit, Afterpay, a payment plan — no, the patient decides and merely pays
differently, so it passes.

**AND IN A GOVERNMENT-PROFESSIONAL MARKET THE TELL IS NOT A SCHEME NAME. Measured 10 Nov 2026 and
it corrected my own expectation.** I briefed a worker to watch Montgomery County and northern
Virginia for FEHB, CareFirst and Medicare, on the reasoning that a federal-employee region would
print plan acronyms. **Zero of 22 clinics printed a scheme name of any kind.** The one must-have 2
failure arrived instead as a **"Primary Care" menu heading plus the words "If not covered by
insurance"**. So in these markets the reimbursed arm is usually **a primary-care or hormone clinic
bolted onto the aesthetics business**, not an acronym in the footer. Read the menu's top-level
categories for a clinical service line; do not go hunting for plan names. One Long Island clinic prints
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

None of the seven may be recorded as a published address. **AND ONE THING THAT IS EXPLICITLY NOT ON
THIS LIST, STATED HERE BECAUSE IT HAS BEEN RE-ARGUED IN EVERY SWEEP SINCE 8 Nov AND TWO WORKERS
HAVE NOW ASKED FOR IT IN WRITING: A CONSUMER MAILBOX PUBLISHED ON THE CLINIC'S OWN SITE IS A VALID
PUBLISHED ADDRESS.** `arabellaboutiquemedspa@gmail.com` printed on `arabella...com` passes
must-have 5 outright. It is the fourth Illinois instance alone, and workers keep stopping to
reason it out from first principles because the answer was implied by the two tests above and
never said.

**Why it passes, from must-have 5's own words — "a published email address read off THEIR OWN
site":** the two questions are *where was it published* (their own domain — yes) and *who receives
mail sent to it* (the owner, who chose a gmail because a lot of small clinics do). A mismatched
mailbox domain is already stated above to be normal and never "corrected". **A gmail is simply the
far end of that rule, not an exception to it.** It is weaker evidence of a marketing operation, so
it may bear on the grade through `crm_detected` and the dormant signals; it has nothing to do with
whether the address is published. **The contrast that matters: the disqualifying cases above are
somebody ELSE'S mailbox (an agency, a vendor) or a GENERIC INDUSTRY DOMAIN — a consumer mailbox
on the clinic's own page is neither.** Record it, note the gmail in `notes`, and do not re-argue
it.

None of the seven may be recorded as a published address. The first four are not recoverable by
opening the page in a browser; the sixth is not a recovery problem at all, but a question about
whether the clinic published anything.

**AND THE SHARPEST ADDRESS FINDING OF THE WEEK IS NOT A LOOK-ALIKE AT ALL — IT IS TWO REAL
ADDRESSES THAT DISAGREE. 12 Nov 2026, THREE INSTANCES IN ONE BRISBANE SWEEP, EACH ONE CHARACTER
APART:**

- **Vara Aesthetics:** `enquire@` and `enquires@` in the privacy policy; `enquiries@` in the footer.
- **Vissi Aesthetics:** **`hell0@` — with a zero** — in the policy; `hello@` in the footer.
- **Skinthetics:** `info@skintheticclinic.com.au` in the policy; `info@skintheticsclinic.com.au` in
  the footer.

**All three footer forms are `mailto:`-wired. All three policy forms are the owner's typo.** A
policy is pasted together once by somebody who is not checking, and nobody ever clicks an address
inside it; a footer address is wired, clicked daily, and fixed the first time a patient complains.
**Recording the policy's version would have produced three silent bounces that read to us as
disinterest, and every row would have looked completely normal** — which is what makes this worse
than a mask. A mask announces itself.

**THE RULE: where a page publishes the same mailbox twice and the two disagree, the disagreement is
the evidence and the FOOTER wins.** This is the other half of "never correct a mailbox" rather than
an exception to it: we are not correcting anything, we are choosing between two things the clinic
published, on the ground that one of them is wired and one is not.

**And the test that generalises, settled on row 694 the same night: a domain mismatch is a typo risk
only when the published appearances disagree with EACH OTHER.** Row 694 publishes
`contact@the-aestheticlab.com` (one hyphen) on a site at `the-aesthetic-lab.com` (two) — flagged by
a typo audit as the most suspicious address in the file, and cleared by one fetch, because the
visible text and the wired `mailto:` href agree exactly and no other address exists. **Visible text
agreeing with its own `mailto:` is the strongest attestation available, whatever the domain looks
like.**

**The audit that produced that row also produced a reassurance worth recording: the defect is NOT
already in our file.** Across all sendable rows, no local part is one edit from a standard form
except five legitimate `booking@` mailboxes, and the domain mismatches are brand and country-TLD
variants recorded verbatim rather than typos. **So this rule is a guard against a future error, not
a cleanup of a past one — which is the cheapest moment to write one down.**

And, added 12 Nov 2026, an **eighth: an unreplaced theme placeholder address on the demo vendor's
own domain.** Row 163's page carries two extra blocks printing `sanfrancisco@message.com` and
`losangeles@message.com` beside Latin filler copy. `message.com` is the theme's demo domain, so
neither address belongs to the clinic and neither block is evidence of two more sites — **it is the
`filler@godaddy.com` case with a city name glued on, which makes it read far more like a real
branch mailbox.** The tell is the same one that caught the demo addresses in a locations slot: a
city that has no business being there. Do not record them and do not count them toward must-have 3.
**And `filler@godaddy.com` itself turned up in the wild on 12 Nov — Sol Skin Clinics prints it as
visible text BESIDE a genuine published gmail.** The keeper is not the placeholder, which is
obvious; it is that a page can carry one valid address and one worthless one at the same time, so
**"I found an address on this page" is not enough — read the domain of EACH address, including when
one of them is obviously fine.**

**A NINTH, 12 NOV 2026, AND IT IS NOT AN ADDRESS BUT IT FAILS THE SAME WAY: A PLACE NAME IN A META
TAG IS NOT A LOCATION.** Three of nineteen Brisbane clinics name a suburb in their meta description
that they are not in — Vissi says "Albion" and is in Nundah, Enhance says "Hawthorne" and is in
East Brisbane, Harmony says "Sunshine Coast" and is in Newstead, three hours away. The mechanism is
that inner Brisbane's suburbs are small and adjacent, so a clinic SEO-targets the better-known
neighbour one street over. **We already had the rule that an ADDRESS in a meta tag is not published;
this is its other half, and it bites on coverage rather than on contact** — a worker querying
exactly the right town gets a clinic in the wrong one, and the row's `city` field then carries a
suburb the clinic does not trade in. **Reading the postal address first catches all of them.**

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

**AND A CONSUMER *ISP* MAILBOX IS THE SAME ANIMAL AS A GMAIL — SETTLED 11 NOV 2026, AND SETTLED BY
THE WORKER RATHER THAN ASKED, WHICH WAS RIGHT.** Skin IQ Medspa publishes `skinIQ@att.net` on its
own page. That is neither of the two disqualifying kinds: it is not somebody else's mailbox, and
`att.net` is not a generic *industry* domain in the `medspas.info` sense — it is a consumer ISP,
which means the clinic's own owner reads it. So it passes must-have 5 on exactly the reasoning that
settled the gmail case: **published conspicuously on the clinic's own site, and received by the
owner.** Record it, and note the weakness in the grade, which is the same weakness a gmail carries
— a consumer mailbox is more likely to be read by one person and less likely to survive a staffing
change than a mailbox on the clinic's domain. **The test that decides all of these cases in one
line: whose inbox does mail to this string land in?** Own domain, gmail and ISP all answer "the
owner's"; a generic industry domain and somebody else's mailbox do not.

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

**AN EIGHTH LOOK-ALIKE, 17 NOV 2026, AND IT IS THE BEST ARGUMENT YET FOR THAT GENERAL FORM: A
MAILBOX ON THE HOSTING PROVIDER'S OWN SERVER HOSTNAME.** Lotus (Brunswick, VIC) publishes an address
whose domain is a **cPanel server hostname** ending `...supercp.com`. **It passes every item on the
seven-item list** — it is not a web designer's address, not a vendor's, not a placeholder, not a
meta-tag-only appearance, not a directory's, and it sits in plain text on the clinic's own page. It
fails only the general form: **that domain is the hosting company's shared infrastructure, not
anything the clinic controls, so who receives mail sent there is genuinely unclear.**
**This is why the general form outranks the list.** The list is seven observed shapes; the shapes
will keep coming (a cPanel hostname today, something else next month), and each new one passes the
previous seven by construction. **Ask the two questions — where was it published, and who receives
mail sent to it — and the list is a worked-examples appendix rather than the test.**
**It is grep-able, which is the practical part:** `supercp.com`, and more generally a mailbox whose
domain looks like server infrastructure — `cpanel`, `srv`, `host`, `box`, a digit-suffixed hostname —
rather than a business. Park such a row on must-have 5 unless a second, controlled address exists.

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

**THE MARKET-TYPE EFFECT WAS TESTED ON A MARKET PREDICTED TO BREAK IT, AND IT BROKE EXACTLY AS
PREDICTED — COASTAL ORANGE COUNTY, 11 NOV 2026.** Every measurement until now came from a quiet,
referral-driven market, which is the kind of agreement that can mean a real effect or can mean
nobody has looked anywhere else. So the coastal Orange County brief carried the opposite
prediction in writing, labelled a hypothesis rather than a finding: a dense, competitive,
marketing-heavy market should publish far MORE about itself. **It did, and the gap is not
marginal: 8 of 19 clinics, 42%, published a dated or quantified artifact about the business,
against Montgomery County 20%, Westchester 11% and Long Island 8%.** Three outright founding
years, two trading spans, four numbered review counts.

**So must-have 4 was not the binding constraint there — must-have 5 was, and that is the useful
half of the result.** Nine of nineteen clinics publish no usable email at all (eight silent, one
Cloudflare-masked). **The constraint moves with the market type and it moves in the opposite
direction**: where clinics compete on visibility they prove their establishment readily and guard
their inbox, and where they fill chairs on word of mouth they print a mailbox and prove nothing.
A run's thin grade mix therefore says which market type it swept, not how good the clinics were —
and the single highest-yield extra fetch differs by market: a quantified artifact in the quiet
suburbs, a privacy policy in the marketing-heavy metro.

**AND THE SAME NIGHT, A SIXTH MARKET BROKE THE OTHER HALF OF THE RULE — NORTH ATLANTA, 11 NOV
2026. THE ABOVE IS NOT WRONG, BUT IT IS NOT THE RULE EITHER.** Buckhead, Alpharetta, Roswell and
Dunwoody are affluent suburbs on any reading — the market type the rule predicts will publish
nothing. **They published the most of anywhere measured: 11 of 19 clinics, 58%, carried a dated or
quantified artifact**, higher even than coastal Orange County. "EST. 2011" with 149 reviews,
"since 2005" with 393+, a named founding month in 2006 with a four-year award run, "since opening
our doors in 2014" with 75 reviews. **So "affluent suburb means must-have 4 binds" is 5 markets of
6, not a law, and the exception is not a borderline case — it is the largest measurement in the
set.**

**WHAT BOTH 11 NOV MARKETS AGREE ON IS BETTER THAN WHAT THE OLD RULE CLAIMED, AND IT CAME FROM A
WORKER RATHER THAN FROM ME: WHAT VARIES BY MARKET IS *WHICH* MUST-HAVE BINDS, NOT HOW STINGY THE
MARKET IS.** In Atlanta 10 of 12 parked rows failed on must-have 5 — nine in total silence, one
masked — while founding years and review counts were printed freely. In coastal Orange County the
same thing happened independently: must-have 4 easy, must-have 5 binding on 9 of 19. Two unlike
markets, measured the same night by workers who never spoke, reaching the same structural finding.
**A clinic publishes what its market makes it publish, and the two things it chooses between are
not "evidence" and "nothing" but evidence and a mailbox.**

**So the operational instruction changes shape. Do not predict the constraint from the market's
wealth. Measure which must-have is binding in the first five or six clinics and spend the rest of
the budget on that one** — a quantified artifact where must-have 4 is binding, a contact page or a
privacy policy where must-have 5 is. Atlanta's own first-page hit rate says the same thing from the
other end: 7 of 18 clinics gave up the address on the first page read, so **in a must-have-5 market
the second page of a clinic you have already found beats a new clinic**, and that is where a run's
last fetches belong.

**A THIRD MEASUREMENT THE SAME WEEK, FROM A MARKET TYPE NOBODY HAD MEASURED: PERTH, 12 NOV 2026 —
36%.** Perth's western suburbs are affluent, referral-driven and in the most geographically
isolated major metro in the world, which is the strongest possible version of the conditions the
old rule says produce silence. **They published a dated or quantified artifact on 4 of 11 clinics,
above Montgomery County's 20% and below coastal Orange County's 42%.** So the sequence now reads
8%, 11%, 20%, 36%, 42%, 58% across six markets, and the two highest are an affluent American
suburb and an isolated Australian one. **The old rule's predictor does not order the data.**

**Perth's binding constraint was must-have 5 again, on 8 of 11** — and in three distinct shapes
worth keeping apart: four live sites publishing no mailbox at all, one Cloudflare mask, three
fetch-blocked domains. **That is the third market in two nights where must-have 5 bound**, which
makes it the question to ask first rather than must-have 4. Perth also measured where the mailbox
actually lives: **homepage 0 of 5, privacy policy 2 of 4, contact page 2 of 3.** Nothing on a
homepage, twice.

**And must-have 2 failed ZERO times in eleven Perth businesses, with four privacy policies read in
full** — no HICAPS, no "all health funds", no Medicare, no bulk billing anywhere. For a market that
a 2 Nov entry had written off, that is the opposite of a structural failure.

**THE PREDICTOR IS RETIRED, 12 NOV 2026. Not qualified, not "a tendency with a counter-example" —
retired.** Sentences above kept weakening it one measurement at a time, which is how a dead rule
survives. **A fourth measurement the same week finished it: Sydney's harbourside and eastern
suburbs, as affluent and referral-driven a market as exists anywhere, published a dated or
quantified artifact on 9 of 15 clinics — 60%, the highest rate in the file.** Founding years of
1999, 2001, 2002, 2004, 2018, 2019 and 2022, "Established over 32 years ago", "Since 2007", and a
count of 380 reviews.

**The six-market sequence, lowest to highest: Long Island 8%, Westchester 11%, Montgomery County
20%, Perth 36%, coastal Orange County 42%, Sydney east 60%.** The old rule predicts that the
affluent referral markets sit at the bottom. **Three of the top four ARE affluent referral markets.**
The predictor does not order the data, and a rule that does not order the data is not a weak rule,
it is the wrong variable.

**What stays is the measurements, which are real and useful, and the instruction they support:
measure which must-have is binding in your first five or six clinics and spend the rest of the
budget on that one.** That instruction has now been tested in four markets and returned three
different answers, which is the point of it: **must-have 5 bound in north Atlanta (10 of 12 parked
rows), coastal Orange County (9 of 19) and Perth (8 of 11); must-have 1 bound in Sydney east (6 of
15), where for the first time in the file it was the ICP's own disqualifications — plastic-surgeon-led
practices, a self-described dermatology clinic, aesthetics clinics with no injectables — rather than
the evidence ladder or a silent contact page that removed the clinics.** Must-have 4 bound in
exactly one of the four, at 1 of 15.

**AND A REFINEMENT WORTH MORE THAN THE INSTRUCTION ITSELF, FROM TWO RUNS ON 17 NOV 2026: "WHICH
MUST-HAVE BINDS" AND "WHICH MUST-HAVE IS COSTING YOU" ARE DIFFERENT QUESTIONS, AND THE SECOND ONE IS
THE USEFUL ONE.** Both runs that night reported must-have 5 as the binding constraint by first-fail
count — Melbourne's inner north and west 5 of 20, the Gold Coast 5 of 22 — and **in both runs the
must-have that actually determined the result was 4**:
- **On the Gold Coast, must-have 4 capped all nine accepted rows.** Four of the nine pass only at the
  ladder's career-length rung; only three carry a stated founding year. **Nine grade B rows, no A.**
- **In Melbourne's north and west, must-have 4 capped all six**, and is the whole reason there is no
  grade A there either.
**So must-have 5 stops you REACHING a clinic and must-have 4 stops it being GOOD.** A first-fail
tally counts the clinics you lost and says nothing about the ceiling on the ones you kept. **Measure
both: which must-have removes clinics (spend your fetch budget against that one) and which must-have
caps the grade of the ones that survive (that is what decides whether a run can produce an A at
all).** A worker that reports "must-have 5 bound" after producing nine B rows and no A has measured
the less important of the two numbers.

**TWO MORE MARKETS ON 16 NOV 2026, AND THEY TAKE THE TALLY TO SIX MARKETS AND FOUR DIFFERENT
BINDING MUST-HAVES — SO THE INSTRUCTION TO MEASURE IT IS NOW SETTLED, NOT PROVISIONAL.**
- **Sydney's northern beaches and Sutherland Shire: must-have 5 bound, 7 of 13.** Only 6 of 13
  businesses published a mailbox (46%) — **the third reproduction of the Sydney corridor's split**,
  and it reproduced on the towns the 18 Oct sweep predicted would be worst, which is the first time
  a prediction in this file about an Australian market has come true. Must-have 1 co-bound at 4 of
  13, three of those being the ICP's own named disqualifications.
- **Melbourne's inner east, second pass: must-have 4 bound** — and **I PREDICTED THE WRONG LEG IN
  THE BRIEF I WROTE FOR THAT RUN.** On 15 Nov I measured Melbourne's missing grade-A leg as the
  owner's NAME and told the 16 Nov worker so. It was must-have 4. **Which leg goes missing is
  market-specific AND run-specific, and a measurement from last night is not a prediction for
  tonight.** The brief should tell a worker to MEASURE the binding constraint in its first five
  clinics — which this file already says — and should stop naming which one it expects to be.
**~~MELBOURNE'S DATING IS BIMODAL~~ — RETRACTED 17 NOV 2026, THE NIGHT AFTER I WROTE IT, BY A SWEEP
OF THE OTHER HALF OF THE SAME CITY.** Across 19 businesses in Melbourne's inner north and west the
distribution is **three-way, not two**: 3 published a review count, 2 a founding year, **4 published
only a practitioner's career length — the ladder's middle rung, which I had just written off in this
city** — and 10 published nothing. **The west advertises the practitioner's years where Toorak
advertises its review count.** So the middle rung does real work here and the ladder does not
collapse to pass-or-park. **I measured 14 businesses in ONE DISTRICT and wrote it up as a property of
MELBOURNE** — the same move as "Australian sites do not obfuscate" and "Australia is finished", at
the scale of a city this time, and the third instance of it in four days. **One district is not a
city.** What survives is narrower and still worth knowing: inner-east Melbourne's dating was bimodal
in the fourteen businesses measured there.
**A result that does hold across both halves: the two new ladder rungs fired ZERO times in those 19
businesses** — not one site renders a post date, and none of the three policies that exist declares
itself "current from" anything (two say "last updated", a month and a week old, which bounds
nothing). **Budget the policy rung at zero in Melbourne.**

**WHAT THE 16 NOV NOTE CLAIMED, KEPT BECAUSE THE MEASUREMENT ITSELF WAS SOUND AND ONLY ITS SCOPE WAS
WRONG:**
Across 14 inner-east businesses a clinic either published a review COUNT and cleared must-have 4
outright, or published nothing datable at all. **No middle case — no copyright ranges, no "since"
sentences, no dated post archives, in 14 businesses.** Everywhere else the ladder's middle rungs do
real work; here they were empty, so the ladder collapsed to pass-or-park. **Where dating is bimodal
the must-have 4 fetch is cheap** (one page tells you), and where it is graded the fetch is
expensive — worth knowing before budgeting a run.

**AND THE RECOVERY WORK PUT A NUMBER ON SOMETHING THE SWEEPS CANNOT: WHAT MAKES AN OLD RULE-OUT
WORTH RE-TESTING.** Three lists of clinics ruled out under retired rules were re-tested across 15
and 16 Nov, and the hit rates fall cleanly — **41%, 33%, 14%** — with one discriminator: **whether
our own file already recorded a published address.** 14 of 15 recorded addresses were still live
three to four weeks on, so must-have 5 is not what expires. **What binds a recovery is must-have 4**
(7 of 15 on one list, 4 of 14 on another, and the separate 22-row seam found in the CSV the same
night). **So the cheapest recoverable row is one parked on a RULE WE RETIRED while holding an
address we already read** — and the ones parked for want of a date need the two new ladder rungs
spent on them, not a re-source.

**AND THE BRISBANE SWEEP THE SAME NIGHT EXPLAINED WHY EVERY ONE OF THESE MARKETS KEEPS PRODUCING
NEAR-MISSES RATHER THAN GRADE A ROWS, WHICH IS A BETTER QUESTION THAN WHICH MARKET PUBLISHES MOST.**
Nineteen clinics, zero grade A — and **every near-A was missing a DIFFERENT leg**:

- Future Face: named owner-injector, Phorest, real multi-tier memberships — **no email**.
- The Facial Hub: 452 published reviews, a seven-year copyright range — **no injectables**.
- Eleventh Heaven: a CPCA vice-president on staff — **no date of any kind**.
- Bare Beauty: named owner, Dapple, gift vouchers — **no review count**.

**That is the third market where this exact shape recurs, and the worker's reading of it is the
right one: it is not that one leg is scarce in rich markets, it is that the legs are independently
distributed and almost never co-occur.** Four roughly independent conditions at maybe 50-70% each
will co-occur in a small minority of clinics however good the market is, which means **a sweep
producing many strong B rows and no A is the expected outcome, not a sign the market or the worker
underperformed.** Brisbane's own rates show it: a mailbox on the first page read 13 of 19 (68%), a
dated or quantified artifact 10 of 19 (53%), a named practice system 17 of 19 (89%) — **and a
published review count only 4 of 19.**

**The review count is the leg that keeps going missing, now in a third market type** — the same
hole found in Britain and in Westchester. So of the four, that is the one to stop treating as
ordinary evidence and the one a run should not wait for.

**And a better hypothesis to test rather than assume, offered by the Sydney worker and labelled by
it as a recommendation: what predicts a published founding year is the clinic's AGE, not its
market's wealth.** Sydney east's clinics are old — a 1999, a 2001, a 2002, a "32 years" — and an old
business has a number worth printing. That is testable on a young affluent market, and **nobody
should put it in a brief as a prediction until somebody has measured it**, which is the mistake the
retired rule was.

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

**A FOURTH VARIETY, FROM AUSTRALIA, 10 Nov 2026 — AND IT IS THE PLAINEST OF THE FOUR. Some clinics
print NO FOOTER AT ALL.** Two of the six AU/NZ clinics opened that day are small WordPress or
SiteOrigin sites with **no copyright line anywhere**, which the ladder reads as "no trading
history" when what it has actually read is **a theme default.** DC Aesthetics is a
published-mailbox, clean-consent, single-site owner-injector running Timely and offering free
consultations, **parked at C because its theme omits a copyright year.**

**So the ladder now has four distinct failures it cannot tell apart:** no trading history (the
honest C), history never printed (the affluent-suburb case), history printed into a broken widget
(New Jersey), and **no publishing furniture in which to print it (a theme default).** Only the
first is a reason not to write to someone. **A SEVENTH VARIETY, 11 NOV 2026, AND IT IS THE ONLY ONE THAT ALSO MIS-COUNTS MUST-HAVE 3: DEMO
DATA SITTING IN THE LOCATIONS SLOT.** `michelmedspa.com` lists four addresses — two real
Californian ones and two in **Minnesota** — which are CMSMasters "bella-beauty" theme demo
content; the nav still links the demo host and a counter reads "3". **A worker counting addresses
reads four sites in two states and either parks the row on must-have 3 or, worse, accepts the
count.** The placeholder rung was written for the social-proof slot ("10 Happy Returning
Clients"); the Orange County worker extended it to the locations slot on its own reading, graded
the row C, and said in the row that it had done so **so the call could be taken back here**. That
was right on both counts and the extension stands: **unreplaced theme demo content is placeholder
copy wherever it sits, and a site still carrying it has not told you its site count any more than
it has told you its trading history.** The tell is a city that has no business being there — and
it is cheap, because demo addresses cluster in whichever state the theme author lives in.

**The practical instruction is the same in all three
non-honest cases: look for the trading history somewhere other than the footer** — an About page,
a practitioner's stated tenure, a wall of dated reviews — before parking a row that clears
everything else.

**A NEW LADDER RUNG, ADOPTED 10 Nov 2026 ON A WORKER'S PROPOSAL, AND IT CUTS AGAINST THE CLINIC
RATHER THAN FOR IT: UNREPLACED TEMPLATE PLACEHOLDER COPY IN THE SOCIAL-PROOF SLOT IS POSITIVE
EVIDENCE OF A RECENT LAUNCH, AND IT BEATS THE CAREER-LENGTH RUNG.** Two Burr Ridge clinics were
otherwise identical on the ladder — career length only, same platform, single site, founder named —
and the only separator was that one still ships builder demo text in two of its three testimonials
("Maybe you want to launch a business"). **A clinic that has not replaced its demo testimonials
does not yet have enough real ones to replace them with**, which is direct evidence against
must-have 4's "established enough to have a lapsed list". So that one is C and the other is B.

**It is the exact converse of New Jersey's broken-counter rung**, and worth holding as a pair: a
broken counter is a site that *had* the evidence and failed to display it, so look past the widget;
unreplaced placeholder copy is a site that *has no* evidence yet, so believe the absence.

**AND A SIXTH THING THE LADDER CANNOT SEE, WHICH IS THE MOST IMPORTANT OF THEM BECAUSE IT MAKES A
GOOD-LOOKING ROW WRONG RATHER THAN UNDERGRADED: AN OWNERSHIP CHANGE RESETS MUST-HAVE 4, AND THE
FOOTER LIES ABOUT IT. Added 10 Nov 2026.** One Main Line clinic advertises "8+ Years on the Main
Line" and a "Since 2018" badge. Its About page says the premises opened in 2018 **as a different
business**, that the current owner **bought it in 2025**, and that she **relaunched in February
2026**. So the trading history on the footer is real and belongs to **somebody else** — nine months
of the current owner's own list, and the inherited list is a cryotherapy lounge's customers.

**Why this one matters more than the other five: must-have 4 exists to establish that a LAPSED
PATIENT LIST exists for this owner to reactivate.** A previous owner's list may not have
transferred, may not have consented, and in any case is not a list of people who had the treatments
this clinic now sells. **A confident B became an honest C on one extra fetch.**

**So: when a footer or badge asserts a trading span, check the About page for an acquisition or
relaunch before relying on it.** The tells are "under new ownership", "newly reopened", "relaunched",
a founder's start date later than the business's, and a premises history described in the third
person. **This is the one case where the ladder's top rung — a stated founding year — is actively
misleading rather than merely absent.**

**It is the exact converse of New Jersey's broken-counter rung**, and worth holding as a pair: a
broken counter is a site that *had* the evidence and failed to display it, so look past the widget;
unreplaced placeholder copy is a site that *has no* evidence yet, so believe the absence. The
practitioner's own career length does not rescue it, because must-have 4 is about the BUSINESS
having a lapsed list, not about the injector's experience.

**AND A FIFTH SHAPE, WHICH IS THE OPPOSITE PROBLEM — THE SELF-CONTRADICTING COUNTER, 10 Nov 2026.**
Where New Jersey's sites print a broken zero, one Montgomery County clinic prints **too many
numbers and they disagree**: "Founded in 2010" beside a "20 Year Of Experience" counter, beside
"25 years combined", beside a "10 Happy Returning Clients" placeholder nobody replaced. **The rule:
prefer the specific typed claim over the widget.** "Founded in 2010" is a sentence somebody wrote;
"20 Year Of Experience" is a theme counter somebody half-configured. A clinic that publishes four
mutually inconsistent durations has still told you it has been trading since 2010, and that is the
one to record — with the disagreement noted on the row rather than tidied away.

**The practical instruction is the same in all three
non-honest cases: look for the trading history somewhere other than the footer** — an About page,
a practitioner's stated tenure, a wall of dated reviews — before parking a row that clears
everything else.

**And this sharpens the open question below rather than just adding to it.** The ladder is not only
reading marketing effort; it is reading **whether a clinic's website works** — and now, whether its
WordPress theme happens to include a footer. That is further still from trading history, and it is
a worse thing to grade an owner-operated business on.
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

**WHERE THE COPY RULES BITE, AND WHERE THEY DO NOT — settled 9 Nov 2026 after a scan that was
overdue.** The validator has checked `opening_angle` for medicine names and prices since it was
written, and has honestly reported zero for days. **It reads one field.** A recovery worker found
`$11-a-unit tox` sitting in `dormant_lead_signal`, and a scan of every column of every row then
found **70 sendable rows with a price in that field and 16 with a medicine name**, plus 286 with a
medicine name in `services`.

**Almost none of that is a breach, and this is the distinction to hold.** The copy rules govern
what we **SEND**. `services`, `notes` and `scale_signals` record what a clinic sells and what it
published — "Injectables/threads/fillers/skin" is a true research note, and rewriting it would
destroy the asset for no gain. **More than that: most of the `dormant_lead_signal` hits are the
clinic's own PROPER NOUNS** — a "Botox Bank", a "Monthly TOX Club", "Bevara Bucks". That is the
programme's actual name, it is the most precise thing we know about the row, and it is exactly what
identifies the scheme on a call. **None of these rows was rewritten and none should be.**

**The real exposure is narrow, and it is at the DRAFTING end rather than the sourcing end.**
`dormant_lead_signal` is the field an opener gets built from, so a drafter reading "a Botox Bank
that adds 5 units" may write "your Botox Bank" into the email — because it is the clinic's own word
and it reads as personal. That is the trap, and it is one step away from a breach rather than being
one. **THE RULE, CORRECTED WITHIN HOURS BY THE DRAFTING CHANNEL, WHICH WAS RIGHT AND HAD THE
MEASUREMENT.** My first version of this said "name the MECHANISM, never the clinic's brand for it",
flatly. That is over-broad and it would have thrown away about thirty personalised openers for no
reason any rule we hold actually gives. The drafting side had already scanned **all 366 staged
subjects and openers against their full text** — not just `opening_angle`, which is the field my
own audit reads — and found **zero medicine words and zero prices**. Their ruling, which stands:

- **A clinic's own programme name is KEPT where the name itself contains no medicine word and no
  price** — "Beauty Bank", "Skin Club", "Bevara Bucks". It is the clinic's published brand, it
  breaks none of the copy rules as written, and **it is the most personal line in the email.**
- **A name that CONTAINS a medicine word gets the mechanism instead** — "Botox Bank", "TOX Club"
  become "your banked treatment credit".
- **A published price never appears**, whatever it is attached to. That a club costs $99 a month is
  useful to us and goes nowhere near an email.

**The general lesson, and it is about which side owns a copy rule.** I was reasoning about copy
from the sourcing side, where the conservative call looks free; the drafting side could see that it
costs the best line in thirty emails. **A rule about what we SEND belongs to whoever sends it, and
should be settled with the staged text in front of you rather than from the row.** My audit reads
one field and theirs reads the whole email, so on this question theirs is the better instrument.

**So the validator now prints both counts as a HANDOVER WARNING, not a rejection** — "a true
record, NOT to be quoted" — and the drafting channel has been told directly, because it is the only
place the mistake could actually ship from.

**AND THE SAME SCAN CAUGHT A SECOND, SHARPER VERSION OF THE PROBLEM THE SAME NIGHT — one I had
just created.** Recovering rows 166 and 298 from C to B immediately put two copy breaches into the
sendable set: 166's opener named a prescription category and a published price, 298's quoted a
discount figure. **Both had been sitting in the file for weeks and neither had ever been reported,
because the copy audit reads SENDABLE rows only.** While a row is parked at C its opener is invisible
to every check we run.

**So every C-to-B recovery is an unaudited promotion**, and recoveries are something this project
does deliberately and in bulk — eight of them that night. **The rule: a row promoted into the
sendable set gets its opener re-read as if it were new, because for every check we own, it is.**
Both were rewritten to keep the mechanism and drop the clinic's own figure, which is the paraphrase
rule above applied to copy that already existed.

**This is the eighth or ninth time the same shape has bitten: a check scoped to where the problem
usually is will not see it where it actually survives.** The whole-file sweep, the parked-row
deferred-decision audit, and now the promotion case are all the same lesson. **When adding a check,
ask what state a row has to be in to escape it.**

**TWO MORE INSTANCES ON 16 NOV 2026, BOTH IN OUR OWN VALIDATOR, AND THE FIRST ONE IS THE MOST
POINTED THIS PROJECT HAS PRODUCED: I MADE THIS EXACT MISTAKE FOUR HOURS AFTER WRITING THE COROLLARY
AGAINST IT.**
1. **The deferral predicate existed in three places and I fixed one.** Earlier that night the
   validator's no-deferred-decisions check fired on a NEGATION — it rejected two rows for saying
   *"no further check is required before sending"*, which is the opposite of a deferral. I added a
   `NEGATED_DEFERRAL` strip and verified it against five cases. It worked. Then the append ran and
   **the whole-file audit reported the same two rows** — because the regex was called in three
   paragraphs and the fix went into one. On 15 Nov I wrote down, about the 11 Nov Carolinas strike,
   that it *"fixed the paragraph it stood in and never asked which other paragraphs said the same
   thing - the fix was scoped to the instance rather than the class."* **Writing the corollary down
   did not stop me doing the thing the corollary describes, the next day, in the next file.**
   **The fix is structural, not attentional:** there is now one `defers()` function and one call
   site per paragraph, because three copies of a predicate is three places for it to be wrong.
   Knowing a lesson and having a structure that enforces it are different states, and only the
   second one survives a tired night.
2. **The price_point audit had been reporting a quarter of the problem for weeks.** It counted
   `sendable` rows and reported 27, which read as a small legacy tail. Counting **every** row gives
   **102** — and the 75 it never showed were parked and off-ICP rows, which is exactly where the
   hazard lasts longest, because a C row is parked rather than dropped and carries all its columns
   into the sendable set when it is re-graded. Widened to all rows; all 102 cleared, each value
   preserved in `notes` so the call is reversible. **An audit scoped to where a problem does the
   most DAMAGE will not show you where it lasts the LONGEST, and those are different places.**
**What generalises past the validator:** every one of these — plus the page-coverage findings under
must-have 5 and the five-times-reproduced Australian obfuscation claim — is one shape. **A procedure
tells you about the region it covers and says nothing about the rest, and the most dangerous
procedures are the ones that have succeeded often enough to stop being questioned.** The counter is
not vigilance. It is to **write the procedure's boundary down next to its result**, so the boundary
is visible to whoever inherits the result.

## Two published addresses that disagree: the wired one wins unless it is the implausible one — 18 Nov 2026

**Two rows resolved the same conflict in opposite directions, three days apart, so the rule needs
stating.** A page can publish a mailbox as visible text and as a `mailto:` href and have the two
disagree.

- **Row 1220 (Vissi Aesthetics) took the WIRED form**, on the reasoning that the `mailto:` is the one
  clicked daily and therefore the one a clinic fixes when mail stops arriving.
- **Row 1331 (Snatched Clinic) took the VISIBLE form**, because there the wired one was the
  implausible one: the visible text reads `goldcoast@snatchedclinicgc.com.au` while the href drops
  the `.au` — and the clinic's own domain **is** `snatchedclinicgc.com.au`, so the wired form points
  at a TLD the business does not have. The mismatch was identical on two pages, so it reads as a
  template defect rather than a one-off paste.

**The rule: prefer the WIRED form, because it is the one maintained — unless it is the one that
cannot be right.** Test it against the clinic's own domain: a wired address on a domain the clinic
demonstrably owns beats visible text; a wired address on a domain that does not exist, or that drops
a component of the real one, loses to visible text. **Record both forms either way**, and where the
conflict is unresolved say so in `notes` rather than silently picking — a bounce reads to us as
disinterest, which is the most expensive possible misreading.

**And the cheap tiebreaker in Australia: the ABN.** Where the footer publishes one, the register says
which domains and trading names belong to the same company, which is what this conflict is really
asking. That is how row 423's identical conflict was settled — see the register section in
`reference/clinic-sourcing-brief.md`.

## A review count on a booking TENANT does not satisfy the ladder — ruled 18 Nov 2026

**The question, put to a worker deliberately and argued rather than asserted:** the ladder says a
dated or quantified artifact **"on the clinic's own site"** satisfies must-have 4, and that a
published review *count* qualifies where a bare star rating does not. Six Gold Coast clinics had
numeric review counts on their **Fresha booking tenants** and no site of their own. Does that count?

**The ruling is NO, and the reasoning is the part to keep.** A tenant's review count is genuinely
good *evidence* of trading — it is generated by real bookings, so in one sense it is better than a
self-written "since 2015" sentence, and that argument was put. But it is **not an attestation by the
clinic**: nobody at the clinic chose to publish it, and the platform can seed, migrate or reset it.
Reading "their own site" loosely enough to include a tenant would also contradict two rulings
already in this file — the Fresha-slug case and the Clara case — both of which turn on a
platform-hosted artifact not being the clinic's own published claim.

**What DOES satisfy it:** the clinic **embedding the count on its own page** (Plasma Therapy, row
1337, publishes "Over 280+" Google reviews on its own homepage, and that is a clean top-rung pass),
or **the tenant stamping tenure rather than volume** — the East Town precedent, where each review
carries the reviewer's own "Customer since" year, is a floor drawn from the clinic's own booking
records and is better evidence than either.

**The practical consequence: a bare "it has 200 reviews on Fresha" is a reason to go and look at the
clinic's own site, not a rung.** And note a second thing that came out of asking: the 18 Oct claim
that "all six have real Fresha review counts" has **no number and no URL recorded under it**, so it
was never evidence in the first place — it was a recollection. A quantified artifact that is not
quoted with its figure is not quantified.

## Which must-have binds is not a property of a city — it is a property of a RING. 17-18 Nov 2026

The 17 Nov refinement separated **which must-have BINDS** (stops you reaching a clinic) from **which
is COSTING you** (stops it being good). One night later the distinction got sharper, and it is now
finer-grained than a metro:

- **Brisbane's inner north and east (12 Nov): must-have 5 binds.** Mailbox on the first page 68%.
- **Brisbane's south and west (18 Nov): must-have 4 binds** — **7 of 27 sole failures** — and
  must-have 5 barely figures, because **18 of 27 published a mailbox on the first page read (67%),
  the highest of any of the six markets measured**, above Sydney's east at 60%.

**Same city, two rings, two different binding constraints, and the middle ring publishes BETTER than
the inner ring.** So "this market's binding must-have is X" cannot be carried from one part of a
metro to another, and a brief that asserts it will mis-aim the run. State the ring, not the city.

Two more market measurements in the same vein, both of which contradict something this file asserts
generally:
- **Adelaide's east: review counts 0 of 20 clinics.** That rung is simply dead there, and seven of
  the twelve rows are Bs carried by bare copyright years. This is the second metro where the
  review-count rung returns nothing.
- **Adelaide's east published a mailbox on the first page read 85% of the time** — far above every
  other Australian market measured. Publication habit continues not to track wealth, distance or
  anything else we can name.

## What four markets did to the Australian policy screen — 18 Nov 2026

The screen (read the privacy policy for the billing vocabulary on any Australian clinic about to be
graded B or A) had a mixed night, and the honest summary is that **its value varies more by market
than any other check we run.** All four findings matter:

**1. Its precondition fails much more often than this file says.** The recorded figure was ~40%
absent. Measured tonight: **Brisbane south/west 63% absent (10 of 16)**, **Adelaide east 57%**. So
"absent" is the *majority* outcome in some markets, not an edge case — and absent is still not clean.

**2. The 12 Nov claim that the billing tell usually hides in the policy did NOT reproduce in
Brisbane.** Of six readable policies, two were dirty — and **two further must-have 2 failures were in
plain sight on marketing pages.** It split 2 in the policy, 2 on the menu. The policy is one place to
look, not the place.

**3. But when it fires it is decisive, and it saved two sends in NSW.** **Thrive Skin Clinic**
(Unanderra) was **grade A on every other leg** — founded 2016, an owner-doctor, Timely, a
members-only shop — and its policy says *"to claim Medicare rebates"*. Same outcome for YOU by Dr
Shauna Watts. Two clinics that would have gone out under WILBA's name, stopped by one fetch each.
**That is the whole argument for keeping the screen despite point 2.**

**4. AND A NEW USE OF THE POLICY FETCH THAT IS NOT ABOUT BILLING VOCABULARY AT ALL — it reveals the
CORPORATE GROUP.** In Adelaide, ACLC's navigation is pure aesthetics, and its privacy policy **names
"Adelaide Skin cancer Centre" as a covered entity under the same policy.** One fetch, decisive — and
decisive on must-haves 1 and 2 together, because a shared legal entity with a skin-cancer practice is
a shared billing model. **So read the policy's list of covered entities, not only its billing words.**
A policy is the one page where a clinic is legally obliged to say who it actually is, which is why it
keeps paying for reasons nobody predicted: it has now produced a published postal address, a founding
date, a billing admission and a corporate parent on different nights.

## Filing: which file a researched clinic belongs in — ruled 18 Nov 2026

**`near-misses.md` is for clinics EMAIL CANNOT REACH. The pipeline at grade C is for clinics we
can reach that fail a must-have. A clinic with a verified published address and one failed
must-have belongs in the pipeline, and five have been written to the wrong file.**

Both the daily skill and the standing sourcing prompt say the same thing in the same words — *"a
clinic that is close but fails one must-have is graded C and parked with a note saying why, not
dropped"* — and the 16 Oct changeover did exactly that, parking 49 rows at C rather than deleting
them. What has drifted since is narrower and easy to miss: a worker that has **read a published
mailbox off a clinic's own page** and then finds must-have 4 unevidenced writes the whole thing
up in `near-misses.md`, because that is the file it was told to write its rule-outs into. The
write-ups are excellent and complete. They are simply in the file nothing reads.

**Why the file matters more than it sounds.** A C row in the pipeline is visible to
`wilba_outreach.py`, is re-read whenever the standard moves, and carries its verified address and
its date forward in a column. An entry in a 24,000-line prose file is none of those things: the
expensive half of sourcing — finding the clinic and reading an address off its own page — has
already been paid for and is then parked somewhere it cannot be found by anything except a grep
somebody has to think to run.

**The five, with what happened to each:**
- **DC Aesthetics** (Ashmore, Gold Coast) — its own write-up says verbatim *"Grade C. Failing
  must-have: must-have 4. Exactly one must-have fails, so this is parked and recoverable, not
  dropped"*, and records `info@dcaesthetics.com.au` read off its contact page on 10 Nov with both
  AU/NZ findings clear. **Appended 18 Nov.**
- **Skinly Aesthetics** (Upper East Side, New York) — `info@skinlyaesthetics.com` read verbatim as
  text and as a `mailto:` on 9 Nov. **Appended 18 Nov.**
- **Filtered Faces Aesthetics**, **LuxLab** and **Aura Medi Clinic** (all Gold Coast) — all three
  publish a mailbox already verified on 17 Nov; handed to a worker on 18 Nov to resolve must-have
  4, and **to be appended either way**, B if it clears and C if it does not.

**The rule, so this does not need rediscovering: the file is chosen by REACHABILITY, the grade is
chosen by the must-haves, and they are two independent questions.** Unreachable goes in
near-misses whatever its grade. Reachable goes in the pipeline whatever its grade. A clinic that
is both reachable and failing may usefully be written up in near-misses *as well*, for the market
knowledge — but the row is what makes it findable, so the row comes first.

**AND THE METHOD NOTE, BECAUSE THE OBVIOUS AUDIT FOR THIS DOES NOT WORK.** Grepping
`near-misses.md` for email addresses to find mis-filed rows returns mostly noise, and the noise is
structural rather than accidental: **the file's whole job is to record the addresses we refused.**
A scan of 1,237 entries returned 100 blocks holding an address absent from the pipeline, and the
bulk of them were Cloudflare `[email protected]` placeholders quoted in order to be declined,
vendor and web-designer mailboxes already on the look-alike list, `mail@example.com` template
leftovers, and addresses a worker named precisely to explain why it would not record them. Enhance
Cosmetics and Wellness was flagged by the scan on the strength of an address its own entry refuses
in bold. **Audit the VERDICT, not the artifact** — and at this n, read the entries.

## A grade A needs a rung on the ladder, and 25 of them do not have one — measured 18 Nov 2026

**33 of 202 grade-A rows carry a note saying must-have 4 is "inferred" or "NOT VERIFIED", and
25 of those name no rung of the evidence ladder anywhere in their notes.** They reached A on
team size, a device fleet, a membership programme, a count of booking locations, a fitted-out
shopfront, or the business "looking busy".

The twenty-five, for whoever works them: **348, 351, 408, 498, 500, 512** (AU) · **535, 540, 690**
(CA) · **548, 558, 563, 567, 861, 862, 863, 886, 887, 897, 985, 986, 987, 988, 989, 793**. Note the
clustering: 985-989 are five consecutive rows from one Utah sweep and 861-863 three from one Nevada
sweep, so this is sweep-level habit rather than scattered carelessness — which means re-reading one
sweep's rows together is cheaper than re-reading twenty-five rows separately.

**This contradicts the ladder in terms.** The 5 Nov ruling above says it "is what separates a
grade A from a grade B on otherwise identical rows": a dated or quantified artifact on the
clinic's own site satisfies must-have 4; a practitioner's career length alone **keeps the row at
B**; no proxy of any kind parks it at C. **The ladder has three rungs and none of them is "the
operation looks busy."** A device fleet is a capital-expenditure signal, not a dated one — it says
somebody spent money, not when.

**The workers were not sloppy and that is the point.** Every one of the 23 says so out loud, and
two say it better than this file does: *"this A is one evidence short and I would rather say so
than upgrade on a feeling"* (Lou Lou Med Spa), and *"I graded A on the strength of the
owner-injector plus system plus scheme stack, which is the strongest in this whole sweep, and I am
naming the gap rather than hiding it"* (Tru Beauty By Trevor). The notes are honest; the grade is
what disagrees with them.

**Why it is worth acting on rather than noting.** `wilba_outreach.py batch` selects **A before B**,
so these rows sit at the **front of the send queue holding the weakest age evidence in the file** —
and must-have 4 is the one must-have whose failure empties the offer, because a clinic with no
lapsed list has nothing for a lapsed-patient campaign to reactivate. Every other must-have failure
sends a good offer to the wrong buyer. This one sends it to a buyer with nothing to sell back.

**Almost all 23 predate the 5 Nov ladder**, which makes this one more instance of the standing job
that is bigger than any market: **a rule change reaches the run that makes it and nothing behind
it.** The ladder was applied forward and never backward.

**NOT DOWNGRADED ON THE STRENGTH OF THE SCAN, deliberately.** The count above is a count of **rows
to read**, not of rows to re-grade — one bad regex in a sample this size is exactly the reason five
claims got retracted on 17 Nov, and this one proved the point within the hour.

**THE FIRST VERSION OF THE SCAN WAS WRONG IN THREE WAYS AND BOTH OF ITS ERRORS CANCELLED, WHICH IS
THE WORST WAY TO BE WRONG.** It reported **23** and named **row 894, The Injectory**, as a known
false positive. Re-measured with the pattern fixed, the figure is **25 and row 894 is not on the
list at all.** What was wrong:
- **It read negation.** "No review count is published" matched its `review count` branch, so three
  rows were credited with the exact artifact their notes say they lack. Tonight's two Adelaide
  grade-A rows both "passed" that way, which is how the defect was caught — the rows are genuinely
  clean (a stated 2018 founding, and a `(c) 2018` read in 2026), so **the audit got the right answer
  for the wrong reason.** This is the same defect that broke the deferral predicate on 16 Nov,
  reproduced hours after the lesson about it was written down.
- **It missed a stated founding year with words in the middle.** *"Established in Adelaide in 2018"*
  — the city sits between "in" and the year — which is the plainest rung-one artifact there is.
- **It assumed the copyright glyph** and the shape of a review badge: `(c) 2018` and
  *"Over 280+' Google reviews"* both slipped past.

Row 894 was never a false positive of the rule; it was a false positive of a broken regex, and the
fix reads its *"Founded Feb 2021"* correctly. **The pattern is now tested in both directions — 18
controls, half of which must NOT match — because a screen tested only against text you expect to
match is untested.** That test lives beside the audit in `scripts/append_prospects.py`.
The audit now runs inside `scripts/append_prospects.py` on every append and **prints the matching
sentence rather than the id alone**, so each one can be judged in a glance instead of a fetch.
Whoever works them re-reads the row and either names the rung it actually has or moves it to B.

## The ladder's middle rung, named at last — and 24 of the 25 grade-A rows went onto it. 19 Nov 2026

The 18 Nov list of 25 grade-A rows resting on no rung of the must-have 4 ladder has been worked, all
25, by reading each row's notes rather than by fetching anything. **22 moved to B, 2 moved to C, and
1 kept its A.** That one, row 408, kept it on the weakest artifact the ladder admits: a site
copyright reading 2022, four years old when read, which clears the three-year floor and was the only
rung the row had.

**What the pass found is that the ladder's middle rung was described too narrowly.** The 5 Nov
version named exactly one kind of middle evidence — *a practitioner's career length* — and said
anything less parks the row at C. Reading 25 rows turned up a fourth kind the ladder never named,
and it was doing most of the work in practice:

- **An operational proxy.** A payment-plan integration on a 52-week term. A stocked retail
  storefront. A branded, named membership programme. A gift-card shop. A twelve- or twenty-person
  named team. A second or third published street address. A roster of manufacturer trainers.
  A fitted-out shopping-centre tenancy.

**Why these are not nothing, and why they are still not enough.** Each one is evidence the clinic is
*past its first setup* — nobody integrates a 52-week payment plan or names a membership tier in
month one. But **none of them says how long**, and must-have 4 is a question about duration. So they
sit exactly where career length sits: **B**. Nothing at all still parks a row at C.

Stated as a rule: **a non-dated, non-quantified operational proxy holds a row at B. It never lifts
one to A, and it never leaves one at C.**

Two independent routes reached that rule the same night, which is some evidence it is real rather
than convenient. The re-grade pass reached it by reading 25 rows; **row 1204's own worker had
reached it alone, weeks earlier**, writing *"I have applied the evidence ladder's MIDDLE rung: a
practitioner-level claim keeps the row at B rather than parking it at C, because 'thousands of
patients' is the thing must-have 4 actually asks about"* — and then explicitly inviting this thread
to overrule it. It was right and has been confirmed in the row.

**What the pass says about grade A itself, which is the more uncomfortable finding.** Several of
those 25 rows said in terms that they were short: *"this A is one evidence short of the standard"*,
*"three legs of four"*, *"I would rather say so than upgrade on a feeling"*. The graders were honest
and the notes were accurate. **The grade still said A, and `batch` takes A before B — so a gap
everybody had documented was putting the weakest age evidence at the front of the send queue
anyway.** The defect was never dishonest grading. It was a grading scheme in which a documented gap
changed the prose and not the sort order. Writing the caveat is not the same as acting on it.

## And the identical defect was sitting in grade B, found by a check built for something else. 19 Nov 2026

The audit that found the grade-A problem was **scoped to grade A**, on the reasoning that grade A is
where a weak row does the most damage. That scoping was this project's most repeated mistake, now
at nineteen instances: **a check scoped to where the problem usually is will not see it where it
survives.**

It surfaced by accident. The **deferral predicate** — a different check, built for a different
purpose — flagged twelve grade-B rows whose notes tell a person to go and date a clinic from its
Google review history. Reading those twelve found **six C rows wearing a B**. Nothing about grade A
had anything to do with finding them, and the grade-A audit could not have found them in principle.

The audit now covers **A and B**. Grade B prints as a count and ids only, with no snippets: there
are hundreds of B rows and a snippet each would bury the grade-A lines, which are the urgent ones.
First measurement: **88 grade-B rows name no rung and have never been ruled on.** That is a backlog,
not a to-do list — the middle rung is wide and plenty of those rows hold B legitimately without
using the ladder's vocabulary. **Read them before moving them.**

**And the widened audit was wrong on its first run, in a way worth keeping.** It immediately flagged
the 22 rows that had just been moved A-to-B on an explicit middle-rung ruling as "candidates for C" —
because their notes *do* say must-have 4 is inferred and the ladder regex *does* find no artifact in
them. Both facts true, conclusion wrong: **a row that has been read and ruled is not a candidate for
anything.** A recorded ladder ruling now suppresses the flag, the same way `QUESTION RESOLVED`
suppresses the deferral flag. That is not the audit being made lenient; it is the audit learning the
difference between a row nobody has looked at and a row somebody looked at and decided.

## The 88-row backlog worked: 79 held, 9 moved to C — and the middle rung turns out to be a principle, not a list. 22 Nov 2026

The 88 grade-B rows that named no rung and had never been ruled on have all been read, with no
fetches spent. **79 hold at B, 9 move to C.** The audit's count of unruled B rows is now **0**.
Pipeline: 925 on-ICP, 917 ready to approach.

**The nine that failed, and the shape they share.** 358, 477, 686, 732, 778, 783, 844, 881, 941.
Every one of them says so in its own notes — *"no trading proxy whatsoever"*, *"Established is
INFERRED and the proxy is absent"*, *"my proxy is the breadth of the build-out, which is weak"*.
Not one needed a judgement call I had to invent; the graders had already written the finding and
the grade had not followed it. That is the same defect the 19 Nov pass found in grade A: **a
documented gap changed the prose and not the sort order.** Two of the nine fail a second must-have
as well — 477 on the inverted tenancy (the Jane App diary sits under another practitioner's
account, so she is the room-renter and owns no list) and 844 on must-have 3 (nobody named anywhere).

### The middle rung is a test, and the 19 Nov list was examples of it

Three rows would not fit the 19 Nov list and all three were obviously right to hold:

- **1020** rests on *"a mature multi-platform device stack (InMode FaceTite/AccuTite, Alma,
  Morpheus8, 3D HIFU, ProCell) which takes years and capital to assemble"*. A device stack is not
  on the list.
- **791** and **795** rest on *"18+ Years Combined Exp."* and *"more than 70 years collective
  experience"* — a team's career length, not a practitioner's.
- **449** rests on an *"Events & VIP Perks"* app whose platform the page never names: loyalty
  furniture that exists but cannot be identified.

So state the rung as the test it always was: **the middle rung is evidence of ACCUMULATION — capital
or commitments that cannot be assembled in a clinic's first months.** A stocked storefront, a
52-week payment plan, a membership roll, a gift-card float, a named team, a second street address, a
trainer roster, a mailing list, a multi-platform device stack, a career: every one of these is
something that had to be built up. **What is NOT a rung is anything that can be bought in a month** —
and that is the sharp edge the old list was missing. Row 881's proxy was *the breadth of its menu*,
and a wide menu is a purchase order, not an accumulation. That is why 881 moved and 1020 did not.

The rule as it now stands: **an accumulation with no date on it holds a row at B. It never lifts one
to A, and it never leaves one at C. Nothing at all parks it at C.**

### Three rows were already on the TOP rung, in prose the regex cannot parse

The audit prints "names no ladder artifact anywhere". That is true of the **regex**, and I read it as
true of the **row**. Three of the 88 carried a top-rung artifact in prose:

- **588**: *"Almost 4 years of Specialist Facial Aesthetics"* in an on-page caption. That dates the
  practice to about 2022, which is enough. Must-have 4 on that row is **satisfied, not inferred**.
- **839**: *"Voted Best in Health & Wellness - RC Chamber 2025"* — a dated award on their own site.
- **1022**: *"a blog with multiple dated posts under a consistent byline"* — a dated archive.

**So the audit's count is a count of what the regex can see, and the regex reads a narrow dialect.**
It wants `since 2018` or `© 2019` or `47 reviews`. It cannot read "almost four years of" or "the RC
Chamber 2025 award" or "multiple dated posts". Widening it further is the wrong move — the fourth
literal-gap bug on 19 Nov came from widening this very pattern. The right move is the one that
worked here: **the regex nominates, a person reads.**

### 839 is the cleanest statement yet of the artifact/age distinction

Its dated award is a genuine top rung: the clinic's age is now **known**. What is known is that it
existed in 2025 — about a year. So the row has the best kind of evidence and still fails to reach A.

**A top rung does not imply A.** The ladder answers *do you know how old this clinic is*; must-have 4
asks *is that old enough*. Row 1346 (Afterglow) reached A on two dated awards, 2023 and 2025, because
two dates **bracket** three years of trading. One recent date brackets nothing.

### What nearly went wrong, and the method that caught it

With 88 rows to read I first swept them with a keyword regex for the rung vocabulary — membership,
gift card, retail, payment plan, named team, trainer, mailing list. **85 of 88 "hit".** Had I ruled
from that sweep, 85 rows would have been confirmed as B on evidence that mostly did not exist,
because the overwhelming majority of the hits were **negations**: *"No membership, loyalty or voucher
scheme"*, *"None published"*, *"no gift cards, no banked credit"*. Row 421's `membership` hit was the
clinic's own trading name, **The Cosmetic Club**.

This is the disease already recorded in the validator's `DENIAL` comment — *a keyword regex cannot
tell a finding from a denial that one was ever made* — and it bit again on the first new check I
wrote. **The two-line fix is the whole lesson: do not print the match, print the matched span with
fifty characters either side.** Reading 88 short spans took one pass and resolved 66 of them outright;
the 22 the spans could not settle were read in full. A sweep that reports *which rows to read* is
sound. The same sweep reporting *what the rows say* is not.

### A rule change does not reach the rows already decided under the old rule. 22 Nov 2026

**This is a new failure class, separate from the scoping one, and it cost eight rows for eighteen
days.** Looking for parked rows whose reason no longer matches the standard, I searched the 418 C
rows for a parking reason of must-have 2 with vein language beside it. Fifteen came back. Eight of
them were parked against a version of the vein rule that no longer exists:

- **Six were parked on 4 November** — rows 949, 952, 953, 955, 982, 983 — **the same day the vein
  rule was narrowed.** Every one of them says some version of *"the brief names vein work outright
  as a cash-pay fail"*, which is the pre-4-Nov wording. The narrowing was written and the workers
  already running kept the old brief.
- **Two were parked on 22 October** (625, 656), three weeks before the 10 Nov appearance/disease
  split existed.

**Row 949 is the one that stings.** Its own notes say: *"If the standard ever widens on cosmetic
sclerotherapy, this is the first row in this batch to revisit, because everything else about it is a
B or better."* The standard changed that day in exactly the direction the row anticipated. The row
left a forwarding address and nobody came. It is now **B and sendable** — Ontario, two sites, a
monthly-billed Skin Membership, gift cards and a complimentary first-consult.

**Row 983 is the bigger prize and is not released yet.** It reasoned *"sclerotherapy is the firm
form of the fail, so a relaxed IPL-only vein rule would not rescue this row"* — but the 4 Nov rule
is not IPL-only; it names **ThermaVein** explicitly, which is this clinic's own wording
(*"ThermaVein thread vein removal"*). With must-have 4 satisfied at the **top** rung (*"Established
by Nikkita Hancock in 2019"*), the owner-injector named and a three-tier membership club, it now
sits at C on must-have 8 alone — unresolved for want of **one Companies House call**. Pair it with
the Harrogate Aesthetics lookup, which is the same single call.

The other five move from *failed* to **unresolved**, which is the difference between a dead row and
a row one fetch from alive.

**Why neither existing check could catch this.** The audit asks whether a row's reason is
*well-formed* — is a must-have named, with its digit adjacent — never whether the reason is *still
true*. A parked row is, by construction, the part of the file nobody reads again. So the standard
drifts forward and 418 C rows stay frozen at the moment each was written.

**THE PROCEDURE, AND IT IS CHEAP: WHEN A RULE CHANGES, GREP THE PARKED ROWS FOR THE OLD RULE'S
VOCABULARY BEFORE DOING ANYTHING ELSE.** The whole of tonight's recovery was one query — parking
reason plus a keyword, with the matched span printed, which is the same two-line method that saved
the ladder pass. The same sweep is now owed to every other rule that has moved since a parked row
was written: the mole screening-versus-removal split, the therapeutic-indication threshold, the
inverted-tenancy species, and the must-have 4 ladder itself. **Each of those narrowings has a
cohort of rows parked under its predecessor, and none of them has been swept.**

### The mole sweep came back almost clean — and the difference between the two rules is the useful part

Having written that procedure, I ran it again on the next narrowing: the 5 Nov mole split
(screening fails, cosmetic removal passes). Fifteen parked rows name moles or lesions in their
must-have 2 reason. **Thirteen were decided correctly**, and two had already been re-decided on
8 Nov. Only one row had been missed:

**Row 762, Evolve Skin Clinic, Bolton.** Every item in its parking reason now passes — Lynton
thread and leg vein laser work is the cosmetic case, "ABR covers MOLE REMOVAL" is removal and not
screening, and the co-located CQC-registered minor skin surgery service is not a must-have 2
question at all, because benign lesion removal is cosmetic and the CQC is a regulator rather than
an insurer. Its must-have 4 is published three times over: **"Est.1999"**, "Established for over
30 years", "30+ years' experience". It stays C on must-have 8 — and only because a Bolton
Companies House search returned 77 results of which 20 were readable, so it is a **pagination gap,
not an absence.**

**So one rule propagated and the other did not, and the reason is worth knowing.** The mole rule
drew a DISTINCTION — screening versus removal — and a distinction is self-applying: a worker
reading "Mole Check" can tell which side it falls on. The vein rule REVERSED A PROHIBITION the
briefs still quoted verbatim ("the brief names vein work outright as a cash-pay fail"), and a
worker holding that sentence has no way to know it has been withdrawn.

**The indication rule propagated too, which makes it two refinements against one withdrawal.** Six
parked rows name a therapeutic indication in their must-have 2 reason (625, 693, 759, 871, 952,
1085) and all six are decided correctly — 1085's *"FIVE reimbursable indications"* against the
four-or-more threshold is exactly the rule being applied as written. Two of them (693, 759) do
quote a vein line that no longer fails, but both have an independent and decisive fail beside it: a
private medical practice carrying blood testing, nerve blocks, vaginismus treatment and pilonidal
abscess management. **Both now carry a note saying the vein point is void and changes nothing**, so
that the next vein sweep does not "recover" them on it. A recovery sweep can be wrong in the
generous direction too.

**A rule that refines a prohibition reaches the rows. A rule that withdraws one does not.** When
the standard withdraws a prohibition, the old sentence has to be hunted down in the brief AND the
parked rows swept the same day — the narrowing's own text already said as much ("applying the old
rule as written cost three UK clinics in a single sweep") and then it happened six more times in
the hours after it was written.

### The tenancy sweep, fourth and last: it propagated best of all

43 sendable rows describe a host tenancy. Reading the span on each, the discriminator added on
11 Nov — **whose tenant holds the diary** — has been applied almost everywhere, and usually in the
row's own words: *"booking runs on her OWN subdomain, not a host's tenant, so she owns the list"*,
*"each holds its own diary"*, *"it is NOT the inverted Aluma tenancy"*. This is what a propagated
rule looks like, and it is the one rule of the four that was written as a **question** rather than
as a prohibition or a distinction. A question travels because a worker has to answer it to finish
the row.

One row looked like the fourth species and is not. **1384 Aesthetics Geelong** describes itself as
the host of two other brands at Shop 2/111 Pakington Street, which is the shape of row 1353's
inverted case — except the host runs **four Div 1 RNs with published AHPRA numbers**, its own gift
vouchers and its own shop. **A host with its own four injectors is a clinic, not a landlord.** The
fourth species needs the host to have no injector of its own.

Two rows had left the diary question open rather than answered (309 Loving Glow, inside Devine
Aesthetics; 617 Juve, with an "in-salon cosmetic nurse"). Both are now decided the way everything
else was decided tonight: the question is one only the clinic can answer, so it is the sanctioned
first-call discovery question with the withdrawal condition stated, not a hold.

**Scoreboard on the four sweeps my own procedure named.** The withdrawal (vein) did not propagate
and cost eight rows. The distinction (mole) propagated, missing one. The threshold (indication)
propagated completely. The question (tenancy) propagated best. **Write a rule change as a question
if you can, as a distinction if you cannot, and never leave it as a withdrawal without going to
find the old sentence yourself.**

### Four UK rows are blocked on one Companies House call each

A by-product of both sweeps, and the cheapest concrete work in the file. Every one of these has
must-have 4 satisfied and sits at C on must-have 8 alone:

- **983 NJH Aesthetics**, Bracebridge Heath, Lincoln — "Established by Nikkita Hancock in 2019",
  owner-injector named, three-tier membership club.
- **762 Evolve Skin Clinic**, Bolton — "Est.1999"; the register search was a pagination gap, so
  try Bolton pages 2 to 4.
- **982 Sci-U Clinic** — no register call was ever spent on it.
- **Harrogate Aesthetics** (in `near-misses.md`, not yet a row) — company number **06184603** is
  already known, so this one is a lookup rather than a search.

That is four rows for roughly four fetches, against a sourcing run that spends forty-five per
market. **It has been item 3 on the standing list for four nights as "Harrogate, cheapest on the
list" and never done, because one row was never worth a worker. Four is.**

### When NOT to suppress a flag — I was one edit from getting this wrong

Having added a suppressor for the ladder check, I went looking for the next audit line printing a
known false positive and found one: *"sendable rows admitting to five or more sites: 2"*, which has
flagged rows 1284 and 1308 on every run for a week. Both are genuine false positives. Row 1284's
"over 10 locations" is its founder's **previous franchise**, stated as such on the row.

I was about to give it the same suppressor, and `append_prospects.py` says in its own comments why
that would be wrong: *"A crude check whose evidence is visible beats a clever check whose verdict
you must trust."* The check prints the matched snippet, so dismissing it costs one second of
reading. The ladder flag was different: it printed 88 bare ids, so dismissing it cost re-reading 88
rows, and a row already ruled on was indistinguishable from a row nobody had opened.

**The principle: suppress a flag only when the flag hides the evidence needed to dismiss it.** An
over-flag that shows its work is not noise, it is a cheap second opinion — and the urge to make an
audit print zero is not the same thing as the audit being right. Nothing changed in the checker.

### A side-effect worth keeping: 11 rows disagreed with themselves

While applying the rulings I found **11 rows already graded C in `icp_fit` whose `priority` column
still read A or B.** `priority` is cosmetic — sendability is computed from `icp_fit` — so nothing
had leaked. But the 19 Nov finding stands: **when a row contradicts itself across two fields,
somebody eventually reads the wrong one.** All 11 corrected, each with a note saying why.

## "Eyeball the Google review history before sending" is not a deferral. 19 Nov 2026

Twelve rows carried some form of that instruction. It reads like diligence and functions as a leak,
because **nobody was ever going to do it**: our tooling cannot fetch Google review dates, and nobody
is going to spend Jess's attention opening twelve Google Business profiles to date clinics she has
not decided to contact. An instruction addressed to nobody is not a deferral — **it is an unresolved
must-have wearing a task's clothes**, and it had been sitting in the send queue for weeks looking
like it was handled.

All twelve were ruled on with what was actually known. Six held at B with the rung named; six moved
to C. Three of the rulings are worth keeping as precedent:

- **A published review COUNT satisfies the ladder; it does not date the clinic.** Row 765 named
  *"the published count of 72 five-star reviews"* and then asked for the review dates on top. The
  count is a quantified artifact and ICP.md lists it as a rung. What the worker wanted was the
  dating, and that is the distinction this file already carries: **the ladder tells you whether you
  KNOW the age; the must-have asks whether the age is ENOUGH.** The count clears the ladder. Nothing
  published settles the dating, and no further check is required before sending.
- **Two street addresses are a rung. Two town names in a meta description are not.** Rows 696 and
  698 came out of the same sweep and resolved differently for exactly that reason — 696 publishes
  two full addresses under one named co-owner (B), 698 has two towns in a meta tag, no explicit
  count, no published addresses, and a homepage its own grader called close to a placeholder (C).
- **An existing marketing list is not a proxy for a lapsed list. It is one.** Row 782's notes said
  *"NO membership or loyalty scheme is published anywhere"* in the same breath as its
  `dormant_lead_signal` field recorded a live SMS list offering *"special discounts and text-only
  deals"*. The field was right and the sentence was wrong. **When a row contradicts itself across
  two fields, the structured field is likelier to be right than the prose** — prose gets written
  once and copied forward, and this is the second time this month that a row's own notes have
  denied something the row's own data recorded.

## The Australian policy screen: how often it is ABSENT is a property of the RING, not a trend. 19 Nov 2026 (corrected the same night)

The rule as written says the Australian must-have 2 screen *lives in the privacy policy*. Measurement
says that is the wrong word — but **the first version of this section, written two hours earlier the
same night, drew the wrong conclusion from the right numbers, and the mistake is instructive enough
to keep.** It listed four markets in date order, saw 57 → 63 → 67 → 85, and called the absent rate
"now the majority case", as though it were rising over time. Then Perth's western and river rings came
in at **19%**, and the trend evaporated.

| Market | Date | Policy absent |
| --- | --- | --- |
| **Perth west / river / coast** | **19 Nov** | **19%** |
| Brisbane south and west | 18 Nov | 57% |
| Adelaide east / Hills | 18 Nov | 63% and 57% |
| Canberra and Queanbeyan | 19 Nov | **67%** |
| Moreton Bay + Sunshine Coast | 19 Nov | **85%** |

**19% and 85% were measured on the same night.** So the absent rate is not a trend and there is no
drift to track: **it is a property of the ring, like the mailbox rate and like which must-have binds.**
Four data points in date order made a story out of a variable that is geographic, and putting a date
column next to a rate was what made the story look real. Do not budget a fetch count for this screen
from the last market you swept; budget it from nothing, and measure it per ring.

**Keep running it in every ring, whatever the last ring measured, and here is the arithmetic that says
so.** In Canberra six policies were
readable, four clean and two dirty — and **the two dirty ones were the two best-looking rows in the
sweep.** Aesthetics & Wellness Collective (two co-founding RNs, four nurses, a membership, gift
vouchers, Timely, two published mailboxes — the only full grade-A dormant stack in the city) collects
a *"Medicare number"* in its policy, and nothing on any marketing page says so. Ren Cosmedical
collects a Medicare number *"for identification and claiming purposes"*, health fund details, and
discloses to the Department of Veterans' Affairs. **Both would have shipped as sendable Bs.** Two
sends saved under WILBA's name for two fetches is the entire argument for a screen whose precondition
fails two-thirds of the time.

Perth adds a third save on the same night, from a ring where the policy was nearly always *present*:
**Dermedica read as a clean grade B until its policy admitted Medicare rebates.** So the screen pays
in a 19%-absent ring and in a 67%-absent ring alike — the absent rate changes how many fetches it
costs, not whether it is worth them.

**But when it is absent, the screen does not vanish — it moves.** Moreton Bay read about twenty
policies, could read three, and **not one came back dirty** — while two clinics failed must-have 2 in
plain sight on their marketing pages: Jevani's *"privately charged… Medicare rebate is not
processed"* and Plaza Central describing itself as *"a general practice clinic"*. So the honest
statement of the rule is:

**The privacy policy is where to look FIRST. It is not where the screen lives. When it is absent or
silent — now the majority case — the billing screen is decided on the treatment and About pages.**

The absences have shapes worth knowing, because each one looks like a fetch failure and is not:
policy links that are `href="#"` placeholders; a page that reads *"Privacy Policy coming soon"*; a
policy outsourced to `termsfeed.com`, i.e. no clinic-side policy to screen at all.

And it pays a third way that has nothing to do with billing: **Platinum Cosmetic Skin Clinic's policy
page was the only page on either of its two domains that publishes an email at all** — the Flawless
Rejuvenation precedent, now with a second instance.

## The fourth species of inverted tenancy, and this one has nobody to sell to. 19 Nov 2026

The three species already recorded all ask the same question of a clinic renting a room: a clinic
inside a GP practice, a clinic booking through a host's own system, a clinic sharing the host's
brand — **whose tenant holds the diary.** Row 1353 (Authentix, Canberra) is the **inverse**, and it
breaks the offer rather than the grade:

**The host business is the one publishing the address and the one we would write to, and its
injectables are delivered by an independent registered nurse who rents the room.** The injectables
list therefore is not the host's to reactivate. There is no lapsed list behind the address. Stated as
a rule: **when the room-renter is the injector and the host is the business publishing the mailbox,
the host does not own the list.**

## Canberra: reading tenancy instead of ruling on it saved eight rows out of nine. 19 Nov 2026

Canberra is built out of professional suites, and **nine of the fifteen accepted rows are rooms inside
somebody else's building** — Erindale Chambers, two Brindabella buildings, the Kingsborough complex, a
suite inside House of Define, a room inside Skin Society, a Thursday room inside a Braddon barber and
spa, a room entered through a hair salon, a room inside a general practice.

**Rule 8's question resolved eight of those nine in the clinic's favour**, because each runs its own
Timely, Phorest or Aesthetic Record tenant and therefore owns the list we would reactivate. **The one
that failed is the one inside the GP practice** — Enrich Medical Aesthetics, publishing the host's own
phone number and naming no booking system of its own.

Two things follow. **An office-park or professional-chambers address is not a tenancy problem at all;
it is just how some cities are built.** And **the Australian general-practice costume is the species
to watch** — it is the one that actually fails. Had tenancy been ruled on by reflex, that sweep would
have lost eight good rows out of fifteen.

## A prediction this file made about Canberra was wrong, and what replaced it is better. 19 Nov 2026

The brief predicted that a Commonwealth city with a large Defence and public-service population would
print Commonwealth schemes, so DVA and Veterans language would be commoner here than elsewhere.
**Across six privacy policies read in full, "Veterans" and "DVA" appeared exactly once.** Nothing
printed a scheme acronym on a marketing page. That reproduces the Montgomery County finding in an
Australian accent for the second time: **the reimbursed arm does not advertise itself by acronym.**

What the government-town effect actually produced is **medical-practice crossover**. Both must-have 2
failures run on general-practice software stacks — Ren Cosmedical names HotDoc, MediRecords, eTP and
My Health Record in its own policy, and its principal holds a RACGP fellowship — and the biggest
rule-out of the run, Her Health & Aesthetics, is a women's-health medical practice with an aesthetics
arm. **In Canberra the reimbursed arm arrives as a doctor's practice with a skin room, not as an
acronym.** Screen the software stack and the principal's fellowships, not the vocabulary.

## 0 of 24: the review count is the grade-A leg that goes missing, and in Canberra it went missing absolutely. 19 Nov 2026

Fifteen accepted rows came out of a city of 460,000 — a higher yield per clinic opened than the recent
Melbourne and Adelaide rings — and **zero grade A.** The reason is not the market and not the rows:
**not one Canberra clinic in the sweep published a review count, 0 of 24.** The four grade-A legs did
not co-occur once.

That is the third market type in which the review count is the leg that fails, and the first where it
was absolute rather than scarce. Two consequences. **A market can be good ground and still yield no
A** — yield per clinic opened and grade distribution are independent, and a run reporting zero A is
not thereby a failed run. And **where a market publishes no counts at all, the award-year rung is
what is left**: row 1346 (Afterglow, Adelaide) is tonight's demonstration, graded A on a dated award
run — *"Voted #4 Best Cosmetic Nurse in South Australia"* in 2023 and again in 2025 — with the 2023
award putting a three-year floor under the business and no review count published anywhere.

## "State the ring, not the city", in its sharpest measured form: 85% against 30%, same metro, eight days apart. 19 Nov 2026

Adelaide's EAST, measured 18 Nov: **a mailbox on the first page read 17 of 20 times, 85%** — recorded
at the time as far above every other Australian market.

Adelaide's NORTH-EAST and coastal west, measured 19 Nov: **eleven aesthetics businesses found and
EIGHT of them have no website at all** — Fresha or Facebook tenants only. Of the nine that do own a
domain, seven published a mailbox, which is a fine rate; **the denominator is the finding.** Roughly
30% against 85%, nine kilometres apart, eight days apart.

**A brief that carried one ring's measurement into the next ring of the same city would mis-aim the
whole run.** Which must-have binds is a property of a ring, not a city — already recorded on 18 Nov,
and this is the sharpest instance yet. Note what the worker said about its own brief: *"mine did not
say either way"*, which is the right thing for a brief to do when nobody has measured the ring.

## Perth's western ring: must-have 1 bound harder than must-have 5, which is new. 19 Nov 2026

Every Australian ring measured until now was limited by **reachability** — must-have 5, the published
mailbox. Perth's western and river suburbs inverted it: **84% published a mailbox**, and what cost the
rows was **must-have 1**. Four of nineteen businesses opened are **dermal-therapist-led with no
prescriber named anywhere.**

That is a real clinic type rather than a documentation gap, and it is the type the TGA/AHPRA rule makes
hardest to read: because no Australian clinic may name an injectable publicly, a dermal-therapy clinic
and an injectables clinic can publish almost identical menus. **The prescriber is the only tell, and
where there is no prescriber there is no injectables list to reactivate.** So in a high-reachability
Australian ring, budget the fetches for the team and About pages rather than for the contact page.

**And the ring finding fired for a third time in one night, in a third city.** Perth west: 84%
published a mailbox. The same city a week earlier (12 Nov, the Cottesloe/Claremont/Nedlands sweep):
3 of 11. Adelaide east 85% against Adelaide north-east ~30%, eight days apart. **Three independent
reproductions, two of them intra-city, of the rule that a mailbox rate is a property of a ring and
never of a city.**

## What we record

Every prospect gets `crm_detected`, `scale_signals` and `dormant_lead_signal` filled from
their own site, and `email_source` saying where the address was read and on what date.
Those are what the opening line is built from. An opening line that could be sent to any
clinic is not an opening line — but it also cannot name a product or a price, so build it
from the clinic's own story: who owns it, how long it has traded, what scheme it runs.
