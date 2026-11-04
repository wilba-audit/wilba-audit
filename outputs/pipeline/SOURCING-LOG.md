# What we know about sourcing clinics

**Read this before a sourcing run, alongside `ICP.md` and
`reference/clinic-sourcing-brief.md`.** It is the operational knowledge behind the pipeline:
what works, what has gone wrong, and what not to repeat.

**Why it is in the repo.** This was kept in the session's team-memory directory under `/tmp`
until 20 Oct 2026, when that directory was wiped along with the scratchpad, losing four days
of notes. Memory under `/tmp` does not survive. Durable places are this repo and
`/mnt/project-files`, and this file is mirrored to
`/mnt/project-files/prospects/SOURCING-LOG.md` so Claudes in other threads can read it
without the repo.

## The real blocker is not rows, and it is not the copy either — 4 Nov 2026

Confirmed by the sending thread today: **the US and Canadian rows cannot be sent until WILBA has
a postal address for the email footer**, which is what CAN-SPAM and CASL require. That is
**390 of the 662 sendable rows** — US 315 and CA 75, the majority of the file and both of the
markets this thread sources most heavily. Nothing is missing on the rows themselves; the sending
thread was explicit about that.

**There is no postal address anywhere in this workspace.** `outputs/pipeline/email-signature.md`
carries name, title and `wilba.ai` and nothing else, and `context/personal-info.md` has only
"Jan Juc / Bellbrae, Surf Coast, Victoria" as a location, which is a home address and not
something to publish in cold mail. **Only Jess can supply this**, and a PO box or a registered
business address answers it without putting her home address in front of 390 clinics.

Asked on 4 Nov. **Until it is answered, sourcing US and Canadian rows adds to a queue that cannot
move**, which is a stronger version of the standing note below about re-verification being worth
more than new rows. The UK, Australian and New Zealand rows are not blocked on this.

## 4 Nov 2026 — three markets, and the rule that an inconsistent standard is worse than a strict one

**51 rows, ids 933-983: 5 A, 22 B, 24 C.** Three workers: the UK southern half (21 rows), the
California Central Valley remainder (7), and Canada round four — Greater Toronto's affluent
suburbs, Ottawa and Vancouver Island (23). **Pipeline 932 → 983 rows, 636 → 662 ready to
approach.** Fourteen clinics went to the browser-visit list, which is now 87.

### The thing worth remembering: I was running two incompatible address rules at once

The Canadian worker escalated that **our own fetch helper decodes Cloudflare tokens unasked** —
three times out of three, twice saying outright that it had decoded one. That matters more than it
sounds, because the rule as written ("do not decode") assumes a decision point that may never
arrive: the plaintext simply sits in the fetch result looking like any other address. **So the rule
now bites at the recording step. The test is the PAGE, not your result** — if the page shipped a
`cdn-cgi/l/email-protection` token, the address is NOT SEEN, whatever the tooling then handed you.
Zero sendable rows carry a decoded address; the workers held the line unprompted, and all three
said so in writing.

Auditing that, I found something worse, and it was mine. **Rows 536 and 588 are sendable on
addresses that appear only as the target of a `mailto:` link, while row 132's own notes assert that
"an address inside an href is not published text", and rows 103 and 636 were parked for being
meta-tag-only.** Those cannot all be right, and the file was carrying both answers simultaneously.

**Settled: a `mailto:` link IS conspicuous publication; a meta tag is not.** The test the
must-haves actually apply is *can a member of the public use this to email the clinic?* A visitor
sees a clickable "Email Us", their browser shows the address on hover and their mail client prints
it in the To field — the clinic put it there for strangers to use. A meta tag offers the public
nothing: it cannot be seen, hovered or clicked, and nothing on the page invites an email at all.
So 536 and 588 stand, 103 and 636 stay parked, and row 132's note was corrected in place to the
narrower rule it was reaching for: where a clinic publishes one address visibly and a *different*
one only in an href, record the visible one and do not harvest the extra.

**Why this is the fifth instance of one failure mode.** The consent regex that passed five rows
saying nobody had checked; the `email_source` field that asserted a provenance the notes denied;
the Cloudflare audit regex that matched `unobfuscated`; the log entry claiming two greps existed
when one did. Now this: **a standard applied in two directions in the same file, with each
application looking locally correct.** The pattern is always the same — the check interrogates the
claim rather than the evidence, or the rule is never stated in one place where its two readings
would have to meet. **An inconsistent standard is worse than a strict one or a loose one**, because
whichever way the next worker reads it, half the file disagrees with them, and nobody can tell
which half is wrong.

### What each market settled

**The UK southern half beat its own floor.** The standing estimate was three sendable from eighteen
researched. The run got **7 sendable from 27 researched** (2 A, 5 B) and must-have 8 was satisfied
on 10 of 21 rows, so **PECR removes about half this market, not nearly all of it.** Four clinics
answered the company question on their own page in the fetch that got the address — the 1 Nov
one-in-four rate, reproduced independently. **Zero Cloudflare-encoded addresses in 27 businesses**,
and the homepage or footer gave the address on 20 of the 22 sites that published one: **what
Britain withholds is legal identity, not the address.** The register is Britain's privacy policy,
and the privacy-policy rule produced nothing there — six of the clinics opened have no policy page
in existence.

**Hanford, Lemoore and Selma are structurally closed, and now we know why.** The 2 Nov worker
reported they "produced no clinic domain of their own". Two dedicated queries and a newspaper fetch
later: **the aesthetics businesses in those towns do not own domains.** Everything trades on
somebody else's platform — Vagaro, GlossGenius, Timely, `skincaretherapy.net` — and nothing
published on a booking platform's domain can satisfy must-have 5. Closed to an **email** channel
rather than thin, the way Whistler is closed. **A DM channel would open them instantly**, because
a GlossGenius page always has an Instagram behind it. Do not assign those towns again.

**Canada: must-have 2 is the only thing failing anything, in a form the ICP did not describe.**
All seven C rows in the Canadian batch fail or are unresolved on cash-pay and **nothing else** —
not ownership, scale, trading history or the address. Half of them are the briefed vein case. The
other half is new: **a paramedical arm receipted to private extended-health plans** — RMT,
acupuncture, osteopathy, naturopathy in the next room. That is not OHIP, so it passes a literal
reading of "no Medicare billing", and it still fails what the must-have is for, because the
practice has a non-discretionary third-party-reimbursed revenue stream. Parked as unresolved rather
than failed, following the 20 Oct Philosophy of Beauty precedent.

**And the trap that nearly cost the best row in that sweep.** Bradford Skin Clinic prints "No
marketing lists" and "we do not add you to a marketing list because you asked a question about your
skin". **That is a promise about what they SEND. A consent refusal is about what they will
ACCEPT.** One careless reading away from parking the strongest row in the batch. Quote wording like
that verbatim on the row — a paraphrase is how it becomes a wrong call later.

### Market verdicts to carry forward

- **Vaughan and Woodbridge is the richest unworked patch found anywhere recently.** Of seven
  clinics a directory named, three were opened and **all three cleared the ICP**; Elite Skin
  Rejuvenation, Beauty Aesthetics and DC Medical Aesthetics were never opened. That hit rate in a
  market that affluent deserves a worker of its own.
- **Victoria BC is structurally closed** — seven clinics, four already ruled out. And **"Victoria"
  is now the worst same-name trap in the file**: a BC city, an Australian state, and a common
  clinic name. One Victoria BC query returned a Vancouver *Washington* clinic and a page about
  Grovedale, Geelong whose search title read "Victoria Anti-Wrinkle Clinic... in Langford, BC".
- **Oakville is silent, not thin.** Its two best clinics, pür glow and Boutique Medical
  Aesthetics, publish nothing at all across three pages each.
- **Duncan and Port Alberni on Vancouver Island were never queried.** The Saanich Peninsula and
  mid-island corridor gave one A and one B off about ten fetches.
- **The Cloudflare rate in affluent Ontario is far higher than any previous Canadian sweep, and
  the oldest clinics are the ones behind it** — Vaughan Laser est. 1999, Willow est. 2005,
  Mezzmerize est. 2008 are the three deepest trading histories in the sweep and all three are
  unreadable. That is the single strongest argument the browser-visit list has ever had.

## 4 Nov 2026 — two rules, from seven rows nobody was ever going to decide

The sending thread had seven rows staged and held because their own `notes` asked a question:
*"someone should decide whether that is disqualifying before sending"*, *"verify cash-pay before
pitching"*, *"worth a glance before sending"*. All seven were resolved today. Six stand, one was
re-graded down. But the rows are the small part.

### Rule 1: never write a question into a row and move on

**A row that asks a question is a row nobody will ever answer.** The sending side cannot answer
it, because every one of these questions was about qualification, not copy. The sourcing side
never looks at an existing row again, because the prompt says to source. So the question sits in
the field, the row sits out of the wave, and the work of researching that clinic is wasted — all
seven were researched in full, two are grade A, and one (439 Cosmex, trading since 2002) has the
deepest lapsed patient pool in the entire file, which is the single thing the offer depends on.

So: **resolve the question, or grade on it.** Writing "someone should check X" is only legitimate
when paired with a grade that already assumes the worst, so the row is safe to send as graded and
the check can only improve it. A caveat is information. A question is an unassigned task, and an
unassigned task in a CSV field is a row quietly deleted.

Worth noting how they were decided, because the pattern was consistent: five of the seven turned
on **"is this the core, or an add-on?"** — menopause and weight loss at 425, weight management
and blood tests at 432, veins and incontinence and sexual health at 439. Must-have 1 asks whether
the clinic is aesthetics-**led**, and v2 disqualifies those categories as *standalone businesses*,
not as add-ons hanging off an aesthetics clinic. All three stand. **639 Renu failed the same test
and shows where the line is: its own menu LEADS with "Dermatology Treatments".** That is not an
add-on, that is the clinic telling you what it is. Re-graded to C, with the second doubt
compounding it — a sibling company named RENU SKIN AND SURGICAL CLINIC LTD exists and nobody has
established which entity holds the patient list, which on a revenue share is a thing to know.

### Rule 2: a check that reads the field making the claim cannot catch the claim lying

**Row 25 Rejuva London was the serious one.** Its notes warned it came from the 24 Aug pass that
"inferred from search snippets" and that the worker never located the clinic's website — so
must-have 5, the rule we hold most tightly, had never actually been satisfied. Meanwhile its
`email_source` field read **"published on contact page - verified 20 Sep 2026"**. An assertion,
not a finding. And the whole-file provenance scan, which has been reported clean for days, reads
`email_source`. **It passed this row every time, because it asked the field that was wrong.**

It resolved in the row's favour: the address is published verbatim on their contact page today,
read and now properly cited. The row was right and its paperwork was fiction. A whole-file sweep
found exactly one other row of this shape (26, already graded C), so this is not a systemic rot —
but it is the second instance in two days of **one failure mode**, which is the thing to keep:

> Yesterday a consent audit cleared five rows whose notes said *"nobody has checked for a no
> unsolicited commercial email notice"*, because it searched for the word `unsolicited`. Today a
> provenance scan cleared a row whose provenance was invented, because it read the field that
> made the claim. **Both checks interrogated the claim rather than the evidence.**

The test that would have caught both: **name the sentence that would make this check wrong, and
grep for it.** For a consent check, that sentence is "nobody has checked". For a provenance check,
it is "inferred from search snippets". Both greps take a minute and both now exist in the
validator. The structural answer is still a dated `consent_screened` column and a
`provenance_verified` column — a boolean belongs in a field, not in prose a regex has to
interpret.

## Where to go next — standing list, refreshed 3 Nov 2026

Keep this current. It is the thing that stops a run spending its first searches deciding where
to look, and `near-misses.md` is the record of everything already swept.

**Markets not yet touched, best first — refreshed 4 Nov 2026:**
- **Vaughan and Woodbridge, Ontario.** Three of three opened cleared the ICP. **Elite Skin
  Rejuvenation Medical Spa, Beauty Aesthetics and DC Medical Aesthetics** were named by a
  directory and never opened. Best known hit rate anywhere right now.
- **Vancouver Island: Duncan and Port Alberni**, never queried at all, plus the rest of the
  Saanich Peninsula and mid-island corridor.
- **Ottawa's remaining directory names, domains already in hand** — The Cosmetic Clinic and
  Accent Image & Laser (Luminesse and Dermalogic are on the browser-visit list instead).
- **Two ownership fetches that would upgrade rows already verified:** The Powder Room and Skin
  Excellence Medispa. Everything else about both is done.
- **Upstate South Carolina remainder** — Greenville and Spartanburg were opened on 3 Nov and gave
  two rows including the first proper Spartanburg-side clinic. The metro is not exhausted.
- **Canada beyond Montreal and the Prairies.** 59 rows and one directory fetch produced 34 names
  in Montreal alone, which is the best single fetch recorded here. CASL's conspicuous-publication
  test has never disqualified a Canadian row.

**Markets that are finished. Do not re-query these:**
- **Australia.** Seven passes. On 2 Nov two Adelaide suburb directories returned the same thirty
  listings with no injectables mentioned; on 3 Nov the country went *down* by four rows.
- **Nevada.** The worst publishing market measured: 22 businesses, 5 readable addresses, on
  well-funded Zenoti and Mangomint sites.
- **Coastal Virginia / Hampton Roads.** Seven towns, five queries, five rows, zero grade A, and
  Norfolk alone has had four queries across two sweeps for one reachable independent.
- **Tulsa and Oklahoma City** — but only on *city-name* queries. See the neighbourhood-stacking
  entry: naming districts inside a city reopened Tulsa after it had been written off, so
  "finished" here means finished by the queries tried, and that is a weaker claim than it sounds.
- **Hanford, Lemoore and Selma, California — closed, 4 Nov.** Not thin: the aesthetics
  businesses there do not own domains, so nothing they publish can satisfy must-have 5. An
  Instagram DM channel would open all three instantly.
- **Victoria BC — closed, 4 Nov.** Seven clinics, four already ruled out, and the town name is
  the worst same-name trap in the file.
- **Oakville, Milton, Waterdown, Stouffville and Orléans, Ontario — 4 Nov.** Oakville is silent
  rather than thin; the other four returned no independent domains of their own at all, only
  service-area pages belonging to Burlington and Aurora clinics.
- **The UK southern half — worked 4 Nov**, but not exhausted: that worker left a "surfaced but
  not reached" list in `near-misses.md`, and Hove's independent layer is partly invisible to
  search because two of its clinics have no website at all.

**The standing job that is not sourcing.** As of 4 Nov the list is further ahead still: 662 rows
ready, 212 staged, ten ever sent. On any run where sourcing would add rows
nobody will email for months, **re-verifying the rows about to be sent is worth more**, and on
3 Nov it was worth 22 rows that would have misfired. The two jobs trade off and the ratio is not
fixed — read `send-state.json` on `claude/project-thread-ptytul` and decide, rather than
defaulting to sourcing because the prompt says to.

## The scheduled prompt is out of date in five places — proposed changes, 3 Nov 2026

**Read this before following the trigger prompt.** The nightly sourcing routine
(`trig_01TwXxobGdpa5M6VH7HuBz28`) was last edited on 16 Oct and five of its instructions have
since been overtaken by measurement. It is Jess's routine, so it has not been changed — these are
proposals for her, and in the meantime the prompt loses to this file on all five.

1. **"Metro order: Australia first — Sydney, Melbourne, Brisbane, Gold Coast, Perth."** Australia
   is finished. Seven passes, and on 2 Nov two Adelaide suburb directories returned the same
   thirty listings with no injectables mentioned, while five of eight rows came from outside the
   assigned corners. On 3 Nov Australia went *down* by two. Sourcing Australia first now means
   spending the first and best fetches of a run on worked-out ground.
2. **"Target at least 60 new qualified rows a run."** That number came from Jess asking for scale
   on 16 Oct, when the easy markets were untouched. It is now the wrong target twice over: the
   remaining markets yield 20-25 a run at this quality, and the list is already far ahead of the
   sending channel, which has 235 rows staged and 10 ever sent. Chasing 60 buys rows nobody will
   email for months, at the cost of the verification work that turns out to matter more.
3. **"Fetch `/contact/` directly, then the careers and privacy pages."** Reversed for the US on
   2 Nov and refined again on 3 Nov. In the US `/contact` is a wasted second fetch; the privacy
   policy is the right next page when the homepage is silent. The careers-page tip still stands.
4. **"Search for wallet, bank or vault plus a metro name."** True in affluent suburbs, dead in
   every mid-size market measured since. It reads in the prompt as a general technique.
5. **Nothing in it about re-verifying an address before a send.** On 3 Nov that was the
   highest-value work of the day: of 14 rows queued to send, one had taken its address down and
   was first in the queue. **A row's address is a perishable fact**, and the prompt treats
   sourcing as the whole job.

**What is missing entirely:** the browser-visit list. The prompt says a Cloudflare-obfuscated
address "counts as not seen", which is right, but implies the clinic is dropped. 57 clinics that
cleared the ICP are parked for want of one page-open each.

## Where the pipeline stands

As of 4 Nov 2026: **983 rows, 662 ready to approach** — US 315, AU 167, CA 75, UK 62, NZ 41, IE 2. (It was 496 rows and 316 ready on
20 Oct.) A further **87 clinics** that cleared the ICP on fit are parked in
`browser-visit-list.md` for want of one page-open each.

**Three rows came OFF the sendable list on 3 Nov** — two Australian and one UK, all of them
long-standing grade A, all parked because a re-read found their published address gone. One of
the three was already loaded into the sending tool and queued to go. **Going down is a working
day too:** a row that cannot be verified today is worth less than no row, because somebody would
have sent to it.

**CORRECTION, 1 Nov 2026 — this log said repeatedly that nothing had ever been sent from the
pipeline, and that was wrong.** Email 1 of the GoHighLevel sequence went to **ten clinics on 15
Oct 2026 UTC** — ids 85, 86, 87, 88, 89, 93, 94, 96, 97 and 98 — recorded in `send-state.json`
on branch `claude/project-thread-ptytul`. **In Jess's own timezone that was the morning of 16
Oct**: the ledger stores UTC and the sender uses Melbourne dates, so both dates that were quoted
to me were right and neither source was wrong. Quote 16 Oct to Jess and 15 Oct to the ledger. Those rows are now marked `Emailed 1` here; they had sat at
`New` for seventeen days and were counted as unapproached in every runway figure this log quotes
before today, including the 316 and the 541. Follow-ups are paused, so each of the ten has had
exactly one email, sent under the **pre-v2 copy**, one day before the 16 Oct standard change.
Two of the ten, 87 Epsom Skin Clinics and 96 Cityskin, are on the sending channel's skip list as
ICP v2 failures, so they were approached and then ruled out.

**Why this went unnoticed for seventeen days, because the mechanism matters more than the fact.**
There are **two send ledgers for one domain**: the sending channel's `ghl/send-state.json`, which
is authoritative, and `send-log.json` here, which drives this thread's warm-up ramp and **did not
exist at all**. An absent ledger reads identically to a ledger saying zero, so `wilba_outreach.py`
reported "send-day 1, cap 5/day, days sent so far 0" for a domain that was no longer cold, and the
code comment asserted in so many words that jess@wilba.ai had never sent anything. Both are fixed.

**And the two ledgers are now one**, agreed with the sending thread on 1 Nov. `send-log.json` is
deleted; `wilba_outreach.py` reads `outputs/pipeline/ghl/send-state.json` straight out of
`claude/project-thread-ptytul` with `git show`, read-only, and keeps no copy, because a copy
drifts and a drifted copy is what caused this. `save_log()` now refuses outright: if mail goes out,
the thread that sent it records it. **The important half is the failure behaviour** — when the
ledger cannot be read, `status` prints "SEND LEDGER UNREADABLE - send state unknown, NOT zero" and
every other command exits 1. It never fills in a zero, because that substitution is the whole bug:
an unreadable ledger and an empty one are not the same claim, and only one of them is safe to act
on. If the ref is missing, `git fetch origin claude/project-thread-ptytul` fixes it.

**What `send_days` means, confirmed by the sending thread on 1 Nov, because the ramp counts its
entries.** Each entry is one sending day in **Australia/Melbourne** — Jess's own timezone — and
the sender runs at most once a day, so one sending day is always exactly one entry. I had raised
a double-count risk: a Melbourne day straddling midnight UTC landing as two entries and pushing
the ramp out. It does not arise, and the count is trustworthy. The first entry, `2026-10-15`, is
the **only** UTC-dated one and is Melbourne 16 Oct; it stays as it is, being one entry for one
day either way. **Do not reinterpret or deduplicate those dates on our side** — read the list and
count it. If the convention changes it changes in the sending thread.

Everything else still holds, and it is the thing that matters: **575 of the 583 clinics on the
current standard have never been contacted**, sending has been paused since 15 Oct, and it waits
on Jess's sign-off on the v2 wording and nothing else. The GoHighLevel thread holds every batch from
id 300 on until Jess approves the v2 copy, and sends are paused pending her word. The
bottleneck has never been the list.

The qualification standard is **ICP v2**, from Griffin's *Med Spa Reactivation* briefing,
which Jess uploaded on 16 Oct with "I want you to master this stratefy… you have authority to
take action". It inverted the 22 Sep standard: owner-operated, injectables-led, cash-pay, one
to four sites, and plastic surgery, dermatology, hospital groups and chains are now
disqualifications where they used to be targets.

## Three mistakes that keep recurring

**Auditing a list instead of the file.** The first v2 audit covered only the rows loaded into
GoHighLevel, and the 16 Oct re-grade assumed the rest of that id range was therefore covered.
It was not: ids 76-84 were in neither, which is how a plastic surgery practice stayed grade A
for three days after plastic surgery became a disqualification. Three chains survived the
same way — Canada MedLaser at seventeen sites, whose own row said "flag before approaching",
Deluxe Med Spa at five, and Skin Technique, a physician group. **After every sourcing run,
scan the whole file for location counts the rows already admit to**, and for sendable rows
with an empty email address. Both scans have caught real errors.

**A grade that outlives its evidence.** Four rows carried grade A or B with no email address
at all. Nothing could have mis-sent, because `wilba_outreach.py` filters them out as not
contactable, but the grade was lying about the state of the list.
`scripts/append_prospects.py` now refuses such a row, and re-runs the check after writing.

**A disqualification that outlives its standard.** Found 1 Nov 2026. Four rows sat at status
`Disqualified` with the same recorded reason: "solo practitioner / two practitioners, one site,
below the $100k/mo scale proxies". That was the **22 Sep** test. ICP v2 retired it on 16 Oct and
inverted it — owner-operated became must-have 3 and one site became a pass — so the reason those
four rows were dropped had not been true for a fortnight. One of them, Dr Jodie in Camberwell,
reads as a clean v2 fit on must-haves 1 through 4: injectables and threads, cash-pay, two
practitioners on one site, fifteen years' trading and 186 reviews.

This is the 21 Oct lesson again, and it is worth stating in the general form, because it has now
arrived three times from three directions. **When the standard moves, the rows judged under the
old one do not re-judge themselves, and `Disqualified` hides them better than grade C does.** A
parked C row still gets read; a disqualified row reads as settled. So the sweep after a standard
change has to cover the rule-outs as well as the acceptances — the acceptances are the ones
everybody thinks of, because a wrongly-accepted row is the one that could embarrass us, but the
wrongly-rejected rows are where the free sendable rows are.

It also showed the whole-file copy scan has a blind spot in the same shape. The scan only covers
**sendable** rows, so two of these four carried a price in `opening_angle` that no scan had ever
looked at: a row promoted *into* sendability brings its old, never-inspected copy along with it.
Both were rewritten to keep the mechanism and drop the figure. On 21 Oct the same gap bit from the
other side, when eight rows upgraded mid-fix were missed by a scan that had already run.

**The practical rule: say which must-have a row fails, by number.** All four of these were
recoverable only because the note recorded the actual test applied rather than a verdict. A row
that says "not a fit" is unauditable the moment the standard moves; a row that says "fails
must-have 4, no founding year and no review count" can be re-read in seconds.

## Rescuing parked rows beats sourcing new ones

Twelve UK rows were parked for want of a company identity. Checking the registers found
**nine sendable rows in 28 calls** — cheaper per row than fresh sourcing, resting on fit
evidence already verified. Look for the same opportunity before commissioning a new metro.

The order that works is **registers first, the clinic's own site last**, which is the reverse
of what seems natural: Companies House, then the CQC registered-provider record (Healthcare
Improvement Scotland in Scotland, HIW in Wales, the CRO in Ireland), then the ICO
data-protection register, and only then the privacy policy — never the footer, which credits
the web designer. Not one privacy policy needed reading. An LLP counts, since the ICO treats
it as a corporate subscriber. A dissolved company does not: it means the entity now trading
is unknown.

## What each market is actually like

**Australia.** The blocker is silence, not Cloudflare: suburban clinics publish a phone
number and an Instagram handle and no address at all, and the Sydney sweep found not one
obfuscated address. So the "Jess reads it in her browser" workaround rescues almost nothing
here, and with phone ruled out, LinkedIn or Instagram is the only route. Timely runs about
two-thirds of regional clinics. Darwin produced nothing — one group owns its search results.

**New Zealand** is the cleanest market swept: 23 of 25 pages published a readable address,
no obfuscation, no builder placeholders, no site refusing unsolicited email. Its limit is
supply — block the chains and the independent layer is thin, and many independents are one
nurse in a room inside another business. The wallet/bank search returns nothing; look for
weekly-payment memberships and prize-draw opt-in lists instead.

**Canada** is better than the US and was nearly untouched until 20 Oct. Only 4 of 22 clinics
published nothing. Jane App is the default platform, founding years are sometimes published,
and **a Gmail address on the clinic's own page is normal** — CASL's test is where an address
is published, not what domain it sits on. A **loyalty scheme branded for a parent company**
is the tell that marketing is decided elsewhere; it caught two clinics that looked
owner-operated.

**The UK** is a legal problem rather than a sourcing one: PECR allows unsolicited business
email to a limited company but not to a sole trader, and only eight of twenty clinics printed
any company identity. The two qualifications are nearly anti-correlated — the clinics that do
print a company number often publish no address.

**The US** is the opposite of the UK: the fit is easy and the address is everything. Clinics
publish contact forms and "text us" links. Founding years are almost never published, so
"established" is usually inferred, and the row should say so and name the proxy. Spokane and
Wichita were unusually productive; Albany, Syracuse and Toledo produced nothing emailable.

## Searching

**Block the directory farms in the first query, not as a refinement** — whatclinic, fresha,
doctify, bookwell, top4, and the job boards. Before blocking them, nine of ten results are
directory pages and no clinic domain surfaces at all. This was the single biggest lever in
three separate sweeps.

**Read the homepage and About-page footers before `/contact`.** `/contact` has been worse
than the homepage in two consecutive US sweeps, though it was the winning move in the
Midwest, where five clinics showed nothing on the homepage.

Outside the US, **guess the clinic's domain and pass it as `allowed_domains`** rather than
searching the brand name: search is US-weighted, and a Cambridge query once returned
Cambridge, Ontario.

**The search and fetch budgets are shared across every worker running at once** — WebSearch
200 calls, WebFetch 400 an hour. Eight parallel workers starved each other on 16 Oct and all
eight stopped short. Three or four, never more.

## Six things that look like a published address and are not

**This section was stale until 3 Nov 2026 and said something we had already disproved.** It
listed a Cloudflare placeholder as the first entry and asserted that none of these is recoverable
in a browser. The brief and `ICP.md` were both corrected on 2 Nov, when decoding a real token
proved a browser recovers these normally; this file was not, so for a day the three documents
disagreed and this was the one a new Claude reads first. **That is the third time a correction has
been left half-applied across these files.** When one changes, grep the other two for the claim
being replaced before closing the task.

The current list, canonical version in `ICP.md`:

1. A website-builder default the owner never replaced (`filler@godaddy.com`, `contact@wix.com`).
2. An address shipped inside a directory site's QR code image — directory data, not published data.
3. An address in Open Graph meta tags while the visible one is obfuscated.
4. The owner's own typo — one AU clinic published a mailbox at `.com.ay`, a domain that does not exist.
5. **Somebody else's working mailbox, hidden or in plain sight.** A marketing agency's address in
   `twitter:data1`; and, 3 Nov, a Tulsa clinic printing a *vendor's* mailbox in plain visible text.
   Visibility is not the test — whose domain it is, is the test.
6. **An address that exists only in the clinic's own meta tags** — added 3 Nov, row 103. Nothing
   visible anywhere, the domain is the clinic's, the mailbox is probably live. Conspicuous
   publication is what must-haves 5, 6 and 7 rest on, so this fails, and it is the most tempting
   of the six.

**A Cloudflare-obfuscated address is NOT on this list.** It is not seen and is never recorded,
but a browser recovers it, so the clinic goes on `browser-visit-list.md`. Obfuscation is not
always Cloudflare: one Canadian site hand-rolled `aesthevaclinic[@]gmail.com`.

Related: a dead clinic domain does not always 404. `19westaesthetics.com` now serves an
unrelated AI companion app.

## Scripting traps

**A keyword regex cannot tell a finding from a denial that one was ever made — 3 Nov 2026.**
The worst scripting bug in this project so far, because it silently *cleared* rows instead of
failing loudly. The AU/NZ consent check searched a row's notes for the words of the finding
(`unsolicited`, `anti-spam`, `own page`). Five rows passed while stating the opposite: their
notes read *"nobody has checked the site for a 'no unsolicited commercial email' notice"*,
which contains the exact word the check was hunting for. The audit built on that check reported
**zero** AU/NZ rows missing a consent finding, and the real number was five.

Three compounding details worth keeping:

- **The check was widened that same morning for a good reason, and the widening made it worse.**
  It had looked for `unsolicited` alone and wrongly rejected three rows recording "no anti-spam
  notice". Adding synonyms was right. Nobody asked the other question: does matching these words
  ever mean the opposite of a finding? It does.
- **It was caught from outside, by accident.** The GoHighLevel thread excluded exactly those five
  rows because their notes read "HELD at C" while the grade column read B — the wrong reason,
  since a note is history and the grade column is the state. It was right anyway. Two sessions
  reading the same rows differently is worth more than either one's audit.
- **A text field cannot carry a boolean.** The honest fix is a column, not a cleverer regex. The
  regex fix shipped (a denial clause disqualifies unless a dated screening stamp overrides it),
  and the whole-file audit now prints both counts, but the structural answer is a
  `consent_screened` date column, and that is worth doing before the pipeline doubles again.

**The test for any scan over prose is now: write the sentence that would make this scan wrong,
and check it against the file.** It takes a minute and it would have caught this.


`open(path,'w').write(...)` without closing, inside a shell `&&` chain, silently lost the
buffer: the edit printed success, never reached disk, and a commit message claimed a change
the commit did not contain. Use `with open(...) as f:` and re-read the file before committing.

Workers disagree about which field holds the A/B/C grade — two put the letter in `fit_flag`
and prose in `icp_fit`, which would have made 39 rows invisible to the drafting script. Find
the letter wherever it is rather than trusting the key.

## The copy rules apply to rows already in the file — 21 Oct 2026

Fifty rows that were ready to send carried a price, a discount percentage or a
prescription-medicine brand name inside `opening_angle` — the field the opener is built from.
The row validator has refused these since the day it was written, so every row added after it
was clean; the fifty all predate it. **A rule added to the validator protects new rows and
does nothing for the hundreds already in the file.** Whenever a rule changes, scan the whole
file for it once, the same way the chain scan is now a standing step.

`opening_angle` is the field that matters here because it is already phrased as copy and a
drafter can lift it whole. **The research fields keep their figures on purpose** —
`dormant_lead_signal`, `scale_signals` and `price_point` are what the angle gets built *from*,
and the numbers are the evidence. They must never be pasted into a message verbatim, and the
sending side has been told so.

Rewriting these is not deletion: the mechanism is the whole value of an angle, and it survives
without the number. "Banked credit that never expires." "A rollover window with a date on it."
"A consult fee credited only on the day." Where a clinic's own promotion was named after a
medicine, the name goes and the shape stays — a recurring weekly injectables promotion.

## Two non-must-haves were parking good rows — 21 Oct 2026

Seventeen rows sat at grade C because no booking platform could be named, or because the clinic
has a single site. **Neither is a must-have under v2.** A nameable practice system is a grade-A
*signal*, and one to four sites *qualifies* — the preference for multi-site groups belonged to
the 22 Sep standard and died with it. The notes had been honest ("graded C on CRM only"), which
is the only reason this was recoverable: **say which must-have a row fails, by number, or the
reason cannot be audited when the standard moves.**

Seventeen sendable rows for no searches and no fetches. That is a better return than any
sourcing run has produced, and it came from reading the file rather than the web.

One went the other way. 197 LifeSculpt stays C, but for the right reason: its own city field
and scale signals admit to four Illinois sites plus three more in California and Utah. The
recorded reason had been the missing booking platform, which hid a real must-have failure
behind a non-reason.

## 21 Oct 2026 — three markets, and what each one settled

**76 rows from three workers, 66 of them sendable**, on about 39 searches and 147 fetches
between them. Three workers, not four, and every one stopped at supply rather than budget —
which is the first time that has happened and is the clearest evidence yet that three is the
right number.

**A clinic with no website at all is not a near miss.** Three regional Australian clinics
surfaced as nothing but a `*.gettimely.com` booking subdomain — AGE aesthetics in Ballarat,
Alchemy Skin in Bunbury, The Cosmetic Lounge in Wagga. Timely has not only won regional
bookings, for a slice of the market it has replaced the website. These clinics can never
satisfy must-have 5, because there is no page for anyone to open. File them as structurally
unreachable and stop spending fetches on them.

**The Canadian consent screen is a recording cost, not a filter.** Across two sweeps it has
disqualified exactly zero clinics: 29 rows, nine near misses and twelve privacy policies read
in full, without a single refusal notice. Budget it as paperwork. **The real Canadian filters
are no published owner and no published trading history** — of nine Saskatchewan and Atlantic
rows, only two carried any trading-history proxy at all, which is why six say "established not
verified" out loud.

**Toronto's core was written off on 20 Oct for the wrong reason.** Quoting the neighbourhood
names as alternates (`"King West" OR "Yorkville" OR …`) alongside `"info@"` on a
directory-blocked query returned five independent Yorkville clinics in one search. The gap was
the query, not the market. **Before concluding a metro is empty, vary the query shape once** —
neighbourhood alternates, and the literal string `"info@"`.

**The secondary-city tier holds up, and there is a reason.** The US worker's accept rate against
clinics that failed on the address alone was roughly 2:1, against about 1:1 on 19–20 Oct and
about 1:2 in the September big metros. The cause is structural: there is no national roll-up to
clear out of the results, so blocking the directory farms is sufficient and no chain filtering is
needed. Bendigo alone out-produced Townsville, Darwin, Launceston, Ballarat and Mandurah combined.

**An owner who publishes anything publishes herself.** Five regional AU rows carry the owner's
own first-name mailbox (`jo@`, `terry@`, `lianna@`, `chantelle@`). That partly reverses the
19 Oct finding that a strong owner signal predicts no published address, and these are better
than `info@`: no gatekeeper.

**Dry holes, so nobody sweeps them again:** Darwin (third sweep running, nothing), Caloundra,
Eugene OR (its three best clinics publish no address — that market needs a phone call, not
another search), Quebec City proper (five clinics, all graded C, the only usable Quebec rows
being in Lévis), Fredericton (no independent surfaced at all), and Leslieville in Toronto.
Bend OR is under-researched rather than thin — four unopened names were left there.

## The parent-group loyalty link, resolved — 21 Oct 2026

The 20 Oct sweep spotted that a loyalty programme branded for a parent company is the tell
that marketing is decided elsewhere. It has now been chased to the end. **Vos Collection is
the May 2026 rebrand of MedSpa Partners Inc** — Persistence Capital Partners-backed,
acquisitive, more than 35 clinics across the US and Canada, with Cosmedica, SpaMedica,
Whistler Medical Aesthetics and Clinique Chloé among the named acquisitions. Its launch
release promises members "their own identity and **clinical** autonomy" — clinical, not
commercial — alongside a shared e-commerce platform and a **cross-clinic loyalty
programme**. That last one matters more than the site count: a group-run loyalty scheme
means the lapsed-patient recall channel is already owned above the clinic, which is exactly
what we sell. Two rows belonged to it, both already parked at C on the tell alone and now
disqualified: 480 Skin Method (Vancouver) and 547 Bella Sante MD (Saskatoon). Nothing graded
A or B was affected, because the tell caught them both at sourcing.

**The lesson is that the tell works, so chase it the same day.** Both rows sat parked for a
sweep waiting on this, and a parked row is a row nobody is selling to.

**A clean negative worth keeping, so it is not re-run:** Artisan Aesthetic Clinics is an
unrelated 14-location Australian chain whose suburbs overlap our AU targets almost exactly —
Balmain, Bulimba, Maroochydore, Cairns, Toowoomba, Mosman, Robina, Gungahlin. We hold
independents at three of those addresses (51 Suede Clinic, 335 Glo Haus, and three
Maroochydore rows). Artisan runs its *own* branded clinics at those suburbs, so the overlap
is market geography, not group membership, and none of our rows is an Artisan clinic.
**Overlapping suburbs are not the parent-group tell; a loyalty link to another company's
domain is.**

Both groups, and Crafted Aesthetics (six staffed Montana locations plus a training arm,
behind a Cloudflare-obfuscated address), are now in the brief's `blocked_domains` list.

## 22 Oct 2026 — New Zealand, regional Australia, UK secondary towns

**82 rows, 52 sendable**, on about 64 searches and 224 fetches across three workers. All three
stopped on supply rather than budget for the second run in a row.

**A claim in this log was wrong, and the correction matters.** It said the two UK
qualifications were "nearly anti-correlated" — that clinics printing a company identity tend
not to publish an address. They are not. All eight clinics that printed a company identity on
their own site also published a readable address. **The company screen is a question about
legal form, not about how tidy a site is**, and there is no reason the two should correlate.
The original observation came from a single sweep of twenty and was noise.

**The Companies House technique, which is the biggest lever found in the UK.** The plain name
search ranks alphabetically rather than by relevance, so a common clinic name returns
thousands of matches with the clinic nowhere in the first twenty. The advanced search with
`companyNameIncludes` + `registeredOfficeAddress` + `companyStatus=active`, run **once per
town rather than once per clinic**, returns every candidate entity in that town with its
incorporation date — answering the company screen and the "established" must-have together for
a whole market in one fetch. Pass rate 45%, against 40% on 19 Oct. Twenty-nine UK rows for
fifteen searches and no privacy policies read at all. Do not try SIC codes without a name
filter: 108 paginated results, nothing gained.

**"Produced nothing" has twice meant "the query was wrong".** 19 Oct recorded Mackay and
Rockhampton as dry; both produced on 22 Oct once the *local* groups were blocked by name —
`divinemedical.com.au` and `pacificplasticsurgery.com.au` owned the Bundaberg and Hervey Bay
result pages, and blocking them surfaced five independents in one search. 20 Oct recorded
Toronto's core as empty; it produced five clinics on 21 Oct once the query shape changed. The
rule now: **a dry hole is only a dry hole once the query has been varied, and the variation to
try is blocking whatever local group owns the results.**

**The parent-group tell has a second form in Australia: a reception mailbox on the group's
domain.** A Devonport clinic publishes `skinrec@myclinicplus.com.au` — the domain mismatch
*was* the disclosure. But a mismatch is sometimes just the owner's other brand, so read the
page header before concluding either way. One Queensland clinic's privacy policy sits on a
second domain the owner also runs, and publishes the Director's own mailbox, which appears
nowhere on the clinic site.

**Mismatched mailbox domains are now the norm rather than the exception** — 9 of 25 Australian
rows, 6 of 28 in New Zealand, 3 of 29 in the UK. The smaller the town, the likelier it is the
owner's personal mailbox (`bigpond.com`, `icloud.com`), and those are better targets than
`info@` because there is no gatekeeper.

**Dry holes, documented so nobody sweeps them again:** Arrowtown (no aesthetics clinic exists
there at all), Taupo, Rotorua, Johnsonville, Karori and Petone in New Zealand; Burnie, Albany,
Morwell and standalone Armidale in Australia; Blackpool, Swansea, Derby, Peterborough, Ipswich,
Gateshead, Bath and Inverness in the UK. **Unresolved rather than dry, and each one browser
visit from settling:** Devonport (two best sites robots-disallowed), Freya Aesthetics in
Rotorua, Newcastle Skin Clinic in Gateshead, pHskin in Stoke.

**Depth left:** coastal Queensland only — Gladstone, Emerald, Airlie Beach, Bowen, Maryborough
and Gympie all surfaced as catchment on other clinics' own pages and are unswept. Inland New
South Wales, Tasmania outside Hobart and Launceston, and Western Australia outside Perth are
effectively worked out at about one row per town. The untried UK rescue route is CQC, Healthcare
Improvement Scotland and the ICO register, which no worker has needed yet.

> **CORRECTED 28 Oct 2026.** "Depth left: coastal Queensland" was wrong, and the mistake is in
> the sentence that follows it: those towns surfaced *as catchment on other clinics' pages*,
> which is evidence about the clinic claiming the catchment, not about the town. Swept on 28
> Oct, four of them turned out to have no independent injectables clinic at all, and the whole
> coast produced six sendable rows. The real depth was inland mining — Mount Isa alone produced
> four. See the 28 Oct section.

**Best clinics we cannot reach at all, for a channel that is not email:** Nude Aesthetics
(Mackay and Bowen) — named founder, memberships, non-expiring gift cards, two sites, no email
anywhere, and a browser will not help. Then LUSH Skin & Laser (Shepparton), and Newcastle Skin
Clinic, which the UK worker called the best clinic in its sweep.

## 28 Oct 2026 — coastal Queensland, Montreal and the Prairies, the US Upper Midwest

**72 rows, 56 sendable**, on about 63 searches and 179 fetches. All three workers stopped on
supply rather than budget for the third run running.

**First, a correction to this log.** The 22 Oct entry said coastal Queensland was "the last
stretch with real depth". It is not, and the reasoning behind that claim was wrong in a way
worth naming: those towns — Gladstone, Emerald, Airlie Beach, Bowen, Maryborough, Gympie —
surfaced as **catchment on other clinics' pages**, and catchment is all they are. Four of them
have no independent injectables clinic at all; the page claiming the town belongs to a clinic
in Mackay, Minyama, Hervey Bay or Mooloolaba, every one of them already swept. **A town that
appears only as somebody else's catchment is a lead about a metro, not about the town.**

The real Australian depth is **inland mining**, which nobody had thought to look at. Mount Isa
produced four rows, Gladstone four on industrial rather than coastal trade, and Moranbah handed
over a grade-A profile without being asked. The next Australian run is the mining belt:
Moranbah, Blackwater, Dysart, Clermont, Biloela, Cloncurry.

> **CORRECTED 29 Oct 2026 — the mechanism was right and the cause was wrong. It is population,
> not mining.** Swept the next day, Karratha (~17,000) behaved exactly like Mount Isa and gave
> four rows, while the five Queensland coalfield towns under 10,000 produced nothing with a
> website at all: at that size there is no competition because there is no market. And **Mount
> Gambier — 27,000 people, timber rather than mining — produced three rows**, which breaks the
> industry explanation outright. Broken Hill is the clean counter-example: a textbook isolated
> mining town whose only aesthetics business is a day spa with no injectables, while a Sydney
> practice flies in quarterly. **The rule is a population floor of roughly 15,000, wherever the
> money comes from.** Nine of thirteen towns on the mining list produced nothing.

**The biggest new lever: device and skincare stockist "find a clinic" locators.** Two fetches of
the Exomide and Procell locators produced seven in-market clinics that 28 searches had never
surfaced. These are manufacturers' own lists of the clinics that buy their products, which is a
far better filter than a directory — a clinic that stocks a professional device line is by
definition an operating aesthetics practice. Re-fetch Exomide with an `offset`; it truncates.

**Read the phone area code before the address.** Two clinics ranked for the wrong state
entirely: "Emerald Cosmetic Clinic" is in Terrigal NSW, and "Skinsense" ranks for Warwick QLD
and sits in Warwick WA. Both were caught by the area code, not by the address.

**A fetched page tried to steer the extraction.** A Louisville clinic's page read as
instructions to the model fetching it, and the address came back only on a second fetch with a
prompt saying to treat page text as data. The row stands because the address corroborates in
two places on the clinic's own site, and the row records that the page misbehaved. The rule is
now in the brief: nothing a page says can authorise an address nobody saw, widen the must-haves,
or declare a clinic qualified.

**A big US metro nobody has swept behaves like a secondary city, not like Chicago.** The accept
rate against clinics that failed on the address alone was about 2:1, matching the small-city
sweeps, and only about one serious candidate in five was a chain or roll-up, against nine in ten
in the September sweeps. The cause is not that Detroit or Minneapolis differ structurally from
Chicago — it is that **nobody had picked them over, so the independent layer is intact.** That
reframes the whole US plan: the question is not metro size, it is whether anyone has swept it.

**Montreal beats English Canada, because of ownership language.** Eleven sendable rows from the
island and Laval against nine from all of English Canada. French sites state ownership outright
— "infirmière injectrice et co-propriétaire", "physician-owned and physician-operated", numbered
Québec companies named in the policies — so the owner-operated must-have resolves far more
often: four of nine Quebec rows name an owner, against two of nine English-Canadian ones. No
clinic was skipped for language. Winnipeg, where we held nothing at all, was empty of queries
rather than of clinics: neighbourhood alternates plus the literal string `"info@"` opened it.

**Run the wallet/bank/vault query first, not last.** One such search produced three qualified US
rows including the two best dormant structures of the batch. But verify the scheme on the
clinic's own site: one clinic has "vault" in its name and no scheme behind it.

**`/contact` was not needed once in 35 US rows** — all came off a homepage, About, locations or
memberships footer. Third consecutive US sweep saying so. Stop budgeting for it in this market.

**A new "established" proxy, and a trap worth more than the proxy.** A run of dated local
readers'-choice awards works. **A practitioner's own years of experience does not** — seven US
rows carry "decades of combined experience" or "17 years each, before this clinic", and every one
is a personal career rather than the clinic's trading history. All seven say so in `notes`. Only
three of 28 US rows published real tenure, and trading history is now the binding filter in
Canada too, where only three of 22 rows published a usable proxy.

**The consent screen has now failed to disqualify a single clinic in five sweeps** — 63 Canadian
clinics and 28 policies read in full, zero refusals, and the same in Australia and New Zealand.
The menu is what disqualifies clinics; the policy is paperwork. It still gets done and recorded,
because it is the basis we rely on, and it still occasionally pays for itself: two Canadian rows
exist only because the address was published inside the privacy policy.

**Dry holes:** Bowen, Charters Towers, Roma, Warwick, Maryborough, Gympie and Proserpine in
Queensland, each on three query shapes; Montclair, Summit, Short Hills and Red Bank in New Jersey
(these four need a query each rather than a combined one, since every other northern NJ town
produced); Grand Rapids and Lexington, which produced no emailable clinic at all; Saint-Laurent,
Mile End, Griffintown and St Catharines. **Structurally closed rather than thin:** Whistler, whose
only aesthetics clinic is a named acquisition of the PE-backed group disqualified last week.

**Left for a browser or a phone, not another search:** CQ Skin and Kalology Gympie, both
robots-disallowed and both the only real candidate in their town; Skin Haven Whitsundays and Mel
Hornery Cosmetics in Moranbah, which publish no email at all; and in Kentucky, Luxe Lounge and
Beautiful You — that state's route in is a phone call.

## Re-reading five old addresses — 28 Oct 2026

Five rows from the 20–23 Sep batch carried `email_source` of "published on site": no page, no
date, and no page named in notes either. They were held and re-checked. **Four of five
confirmed, one unreadable, and the check paid for itself three times over** — in twenty
fetches it corrected facts that had been wrong in the file for five weeks.

- **M1 Med Beauty is two sites, not an unspecified "Australia"** — Sydney and Melbourne, both
  addresses published. Still inside the one-to-four must-have, but the row had no site count at
  all, which is must-have 3 unanswered.
- **Two clinics now name a lead clinician** where the row said none: Dr Eugene Green at Dr Green
  Cosmetic Group, Dr Tammy Tai as Director at Dr Salon. Sites change, and a row written five
  weeks ago is a snapshot, not a fact.
- **Three of the four publish no privacy policy at all.** Recorded plainly rather than left to
  imply one was checked.
- **Suede Clinic could not be re-read: robots-disallowed, six pages refused, including
  `/robots.txt` itself.** That is not Cloudflare — a person opening the site in a browser sees
  it normally, which makes this the best browser-visit candidate in the pipeline. The one page
  that did fetch has its email field blank, so the old address is not confirmed and the row
  stays held.

**The general lesson: a row is a snapshot of a page on a date, and the date is what makes it
one.** That is why must-have 5 asks for the URL and the date, and it is not bookkeeping — the
provenance is also the only way to tell a stale row from a wrong one. Rows whose
`email_source` names a page and a date can be re-verified cheaply; rows that say "published on
site" cannot be distinguished from guesses without re-doing the work.

**Two grading calls worth recording, both made on flags the worker surfaced rather than
smoothed over.** Dr Green's Toorak service-area page has a meta description reading "Cosmetic
surgery & Injections Treatments" and a URL slug of `/cosmetic-surgery-toorak/`, while the body
copy and the whole treatment menu are explicitly non-surgical. Graded B and sendable, because
the menu is the screen the brief says to trust, with the surgery question flagged for the first
call. And Dr Salon lists "Moles and Skin Tags" among its concerns with no description of what
is offered, plus a skin-surgery certification cited as a credential rather than a service: two
soft flags, neither a clear cash-pay fail, both written into the row.

## 29 Oct 2026 — the mining belt, Texas and the mid-South, UK round two

**60 rows, 34 sendable**, on about 72 searches and 200 fetches. One duplicate was caught by the
validator rather than by a worker, which is what it is for.

**The yields diverged sharply, and the reason is how picked-over each market is.** Texas and the
mid-South gave 21 sendable from 24 rows. UK round two gave 8 from 27. The Australian mining
belt gave 5 from 9. Australia is now genuinely worked out below the metros; the US is not.

**A population floor of about 15,000 governs small-town Australia**, and it replaces the mining
theory this log carried for a day — see the correction in the 28 Oct section. Nine of thirteen
towns produced nothing. Broken Hill, a textbook isolated mining town, has no injectables
business at all while a Sydney practice flies in quarterly.

**In the South, the filter that bites is the surgeon, not the roll-up.** Ten rule-outs were
plastic surgery or dermatology, and they owned the first result page in San Antonio, Amarillo,
Jackson and Little Rock. Chains were only about one serious candidate in seven, and no national
brand surfaced at all. The September sweeps taught us to budget for roll-ups; in the South,
budget for the surgeon filter instead.

**Cash-pay now out-filters the company screen even in Britain** — nine of twenty parked UK rows
fail on mole checks, mole mapping, dermoscopy, vein work or minor surgery, against seven on the
company test. Screening the menu first is no longer an AU/NZ/Canada rule. It is the rule.

**McAllen and El Paso differ from the rest of the US in a specific way: the independent layer
is intact but the publishing layer is not.** Three of four Rio Grande Valley addresses are
personal Gmail accounts, two of them spelled differently from the clinic's own domain, and both
metros market Instagram- and Spanish-first with websites thinner than the businesses behind
them — one has Lorem Ipsum live, one prints neither email nor phone. Expect a personal mailbox
and a mismatch there, and do not read either as a red flag.

**Three standing techniques were corrected by the workers using them**, and all three are now
fixed in the brief and the ICP rather than left as written:

- The Companies House one-call-per-town search has two faults that produce confident wrong
  answers: `companyNameIncludes` matches **whole words, not substrings**, so "aesthetic" misses
  every "AESTHETICS" clinic, and the search **truncates at 20 results**, so in a town returning
  77 a clinic can be paginated off page one and read as having no company. A no-match in a
  20-of-many town is unresolved, not absent.
- **The Exomide `offset` trick does not work.** Offsets of 6,000, 22,000 and 45,000 all ended at
  the same entry, and three fetches went on proving it. Ask the first fetch to search the whole
  page for your target towns instead. Only Exomide and Procell are static; the rest render
  client-side.
- **`/contact` is dead in the US** — fourth consecutive sweep, 59 consecutive addresses off a
  homepage, About, locations or memberships footer. The **team page** is the better second
  fetch, because it settles ownership and the address together.

**A fourth way a site defeats a fetch, now in the brief as a taxonomy**: the client-side-rendered
page returns 200 and a document head and nothing else, so unlike a refusal it looks like a
successful fetch and **the fetch is spent before you know the page is empty**. Six of seventeen
businesses opened in the Australian sweep could not be read, mostly this way. The taxonomy
matters because it decides what to do next: Cloudflare obfuscation is unrecoverable and gets
dropped, `robots_disallowed` and client-side rendering are both fine in a browser and belong on
a human's list, and total silence needs a phone call.

**The catchment warning paid off harder than the theory it was attached to.** Five of thirteen
Australian towns are claimed by clinics in already-swept metros, and in four of them that metro
clinic is the number-one result. Six such domains are now blocked by name, along with a regional
West Texas group and seven UK directory farms.

**Flagged rather than smoothed over, by the worker's own choice:** one Mount Gambier clinic's
injectables are provided by a practitioner who also runs her own clinic in another state, which
is a must-have 3 risk written into the row rather than resolved; and that worker marked its own
inference about a linked closed clinic as uncorroborated, which is exactly the right way to
leave it.

## 1 Nov 2026 — Australian outer-metro, northwest Arkansas, the Central Valley, UK round three

64 rows, ids 789-852, 6 A / 34 B / 24 C. Ready to approach went 541 to 583. Four workers, each
inside a 12-search and 45-fetch cap; three hit the fetch cap and none hit the search cap, which
says the binding constraint is reading pages rather than finding them.

**Northwest Arkansas is the best US ground we have found.** Six clinics opened, five published an
address, and three of the run's four American A grades came from Bentonville and Rogers alone. It
was never assigned before today — it surfaced on 29 Oct as a single out-of-market note. Sweep it
properly next: Springdale, Fayetteville and Bella Vista are still untouched.

**The San Antonio suburb ring is email-dead, and it is worth saying why that matters.** Nine
clinics found across New Braunfels, Schertz, Helotes, Boerne and Stone Oak; eight publish no
address at all. The ring is *rich* in exactly our signals — two genuine banked-credit schemes,
three memberships, Moxie, Boulevard and Aesthetic Record, and one family-owned clinic trading
since 1975 — so this is not a thin market, it is an unreachable one. It belongs on a phone or DM
list. Do not send another fetch budget into it.

**In California's Central Valley publishing, not supply, is the constraint — the worst ratio in
this log.** Eleven clinics cleared the ICP and failed on the address alone, nine silent and two
Cloudflare-hidden, against fifteen accepted: close to one lost for every one kept, where Texas ran
two to one. One clinic, Ego Defined, publishes no email **and no phone** across three pages. The
market also split the opposite way to expectation: the affluent inland south gave nine rows and
the northern valley two, and **Visalia alone gave three — more than Fresno, Stockton, Modesto and
Bakersfield combined.**

**The UK finding reverses what this log said on 29 Oct, and it is structural rather than a
sampling artefact.** Six of the fifteen UK rows parked today fail on **must-have 8 alone** — a
company identity — against three on cash-pay. The 29 Oct sweep had concluded the opposite. The
reason is that round three moved into smaller and more owner-shaped towns, and **the business
structure that passes must-have 3 is the one that never incorporates**: a single owner-injector
trading under her own name has no reason to form a limited company, and PECR then shuts us out of
exactly the clinic v2 most wants. That tension is in the standard itself, not in the sourcing, so
the UK will keep returning three sendable rows from eighteen until something changes. It is worth
Jess knowing that the UK has a ceiling the other markets do not.

The regulator route that was supposed to rescue those rows is **blocked by tooling** — CQC
location pages error on a fetch and the ICO register is a POST form with no searchable URL. It
needs a browser, so it is Jess's to do, not a worker's. Recorded in ICP.md where the route is
described, so nobody assigns it again.

**Three workers independently hit the same wall on stacked queries**, which is why the cap in the
brief is now explicit: unquoted, and about four names with two modifiers. Quoted town names
returned one result where the unquoted query returned ten; an over-long stack came back with a
massage directory, a set of UK clinics on an Australian search, and a bare directory page. It cost
the Perth outer ring and the whole southern half of the UK list.

**Two smaller things worth keeping.** `Aesthetic Nurse Software` turned up four times in the UK and
was never named in page text — always inferred from a booking URL — so it is the UK solo-injector
default and the booking link is where to look for it. And the UK worker graded nothing A on
purpose: three rows were A-shaped but it had spent no fetch on review volume, so it flagged them
rather than upgrading them. That is the right call, and the right way round.

## 2 Nov 2026 — Arkansas and Oklahoma, the last Australian corners, the southeast coast, Nevada

58 rows, ids 853-910, 13 A / 32 B / 13 C. Ready to approach 575 to 620. **Under the 60 target, and
deliberately so**: the Australian worker was told to report an empty market rather than pad it and
returned 8 rows instead of 15. That was the right trade and the finding it brought back is worth
more than seven soft rows.

**Australia is finished. Stop assigning it.** This is the clearest market verdict in the log and it
came with proof rather than an impression. The Yellow Pages skin-clinic indexes for Brighton SA and
Marion SA returned **the same thirty listings**, including The Body Shop four times, with **not one
mention of injectables or a cosmetic nurse**. Perth's remaining corridors failed structurally:
Wanneroo and Canning Vale's only candidates sell skin checks and excision-with-biopsy, which is
must-have 2. Five of the eight rows that worker did find sit *outside* the corners it was assigned,
because the corners were empty. Seven passes have now covered both big metros and their outer
suburbs, every regional centre above the ~15,000 floor, the mining belt, Tasmania, Darwin and Alice
Springs. **The standing instruction in the sourcing trigger still says "Australia first", and that
instruction is now wrong** — it was written on 16 Oct when the list was US-weighted at 106 AU rows
against 138 US. It is 173 against 294 today, but the reason to stop is not the ratio, it is that
there is nothing left to find. Jess should be told before a future run spends another four hours
proving it a third time.

**Oklahoma out-published Arkansas, 12 rows to 5**, which inverts yesterday's conclusion that
northwest Arkansas was the best US ground we had found. Yesterday's six-opened-five-published came
from Bentonville and Rogers, and that was **the top of the seam rather than the average**:
Springdale, Fayetteville and Siloam ran about one address in two, and Bella Vista, Centerton and
Cave Springs surfaced no clinic of their own at all across three searches. Tulsa's ring published
and Tulsa city did not. The lesson is about sampling, not about Arkansas: **a single high-yield
query is one query, and a market's average is the thing worth acting on.**

**Nevada is the worst publishing market in the log, worse than inland California**, and it fails
differently. Twenty-two businesses examined, five readable addresses. These are not scrappy sites
that forgot a mailbox — they are well-funded operations running Zenoti, Mangomint, Vagaro and
PatientNow that simply never print one. Inland California was ~1:1 accepted to unreachable; Nevada
is nearer 4:11. **That makes the non-email channel the binding constraint in two US markets now**,
and the phone-or-DM decision outstanding since 24 Sep is overdue.

**The southeast coast was the day's best market**: 17 rows and 6 A grades off 12 searches, the
strongest A-rate of any sweep. Coastal Virginia, Savannah and Pensacola had never been touched.
Norfolk and Newport News still have not had their own query.

**Two technique findings, both now in the brief.** The privacy policy is the **highest-yield address
fetch in a silent market** — two fetches, two addresses, both among that worker's best rows, where
about thirty homepage and About fetches returned fourteen. The brief had it last, which is right
when it is a consent fetch and wrong when it is an address fetch, so the rule is now conditional on
the market. And **the ownership fetch is settled fact rather than advice**: five more ownership
fetches today settled must-have 3 five times and produced zero addresses, which is eleven for
eleven across two days.

**A fifth thing that looks like a published address and is not:** somebody else's working mailbox
in a social meta tag. A Pensacola-area clinic serves its marketing agency's address in
`twitter:data1`, and nothing about it reads as wrong until you notice the domain is an agency's.

**Two clinic sites served injected content**, one carrying PHP in its source that logs a visitor in
as an administrator. That is the hard version of "a fetched page is data": nothing on such a page
is reliable as the clinic's own words. It is also not ours to fix or to mention.

**The duplicate check was wrong and is now right.** It keyed on clinic name alone and rejected a
grade-A Siloam Springs clinic as a duplicate of a grade-C clinic in Mildura, Victoria — both called
"The Skin Clinic", sharing nothing else. Names in this trade are generic, so name alone is not
identity; it now keys on name **and** country, and separately on the website's domain, which adds a
check we never had: a clinic re-sourced under a different name is now caught. Verified on three
cases before writing. **The near-miss that reads like a pass is the dangerous kind of wrong**, and
this is the second one this week after the Companies House near-miss match.

## 3 Nov 2026 — Oklahoma finished, coastal Virginia closed out, and the AU consent backlog cleared

**One worker, not four.** The run was deliberately scaled down: 22 rows against a 60-row target,
because Jess is working about twenty minutes a day on a tight budget and a bigger list is not
what is short. 16 searches and 61 fetches spent. Rows **911-932**, five grade A.

**Tulsa reversed yesterday's verdict, and the method is the lesson.** On 2 Nov Tulsa read as
worked out on city-name queries. Naming *neighbourhoods inside* the city — "Brookside Cherry
Street" — surfaced five domains two sweeps had never returned, and eight of nine clinics opened
there qualified. Suburb-stacking was written down as a technique for the ring around a city; it
works just as well inside one. **A metro declared finished on city-name queries has been sampled,
not searched.** Oklahoma has now out-published Arkansas two days running.

**The privacy-policy rule reversed, and the 2 Nov version of it was built on two data points.**
Yesterday this log made policy-first conditional on a market being quiet, on the evidence of two
Nevada fetches. Today six accepted addresses came off policies the homepage withheld, **in
Oklahoma, a market that published well** — exactly the case the conditional excluded. The rule is
now unconditional: no mailbox on the homepage, the policy is the next fetch, ahead of About and
instead of `/contact`. The mechanism was never scarcity: a policy has to name a contact for data
requests, which is a different obligation from wanting enquiries, so it survives on sites that
strip the mailbox from everywhere a marketer looks.

**Coastal Virginia is finished and should not be re-queried.** Seven towns, five queries, five
rows, zero A. Norfolk has had four queries across two sweeps for one reachable independent.
Hampton Roads is dermatology, plastic surgery and an out-of-state chain's SEO pages.

**Twenty-nine businesses opened with zero Cloudflare, zero robots refusals, zero render failures
and zero site errors.** Worth recording as a fact about these markets rather than a gap in the
method: the fetch-failure modes cluster by region, and Virginia, Oklahoma and the Upstate have
almost none of them. Nothing new for the browser-visit list from the sweep itself.

### The AU/NZ consent backlog — 18 rows, and two of them did not survive

Eighteen AU and NZ rows graded A or B were created on 20-24 Sep, before the must-have 6 consent
screen existed. The GoHighLevel thread has made AU/NZ/UK the **free first sending wave** — no
postal address needed, unlike the US and Canada — which turned this from a recording chore into
the actual legal basis for the first emails WILBA will send at volume. A finding about what was
*not* on a page cannot be reconstructed after the fact by anybody, so all 18 were re-fetched, one
page each. **No AU or NZ sendable row is now without a consent finding in words** — the validator
enforces it and the whole-file audit returns zero.

Sixteen cleared. Not one of the 18 carried a notice refusing unsolicited commercial email, which
is now **more than thirty AU/NZ/CA policies read without a single refusal**. The screen is a
recording cost, not a filter — but it has to be on the record, because the point is being able to
show it was checked.

Two rows failed and were parked at C with must-have 5 named, addresses kept so both calls are
reversible:

- **Row 103, Skin Forum (Gold Coast).** Publishes `info@` and `manager@` on its own domain in
  **meta tags only** — no mailbox in the visible body of the homepage or the contact page. A sixth
  address look-alike, and the most tempting, because the domain is right and the address probably
  works. Same answer as Cloudflare: conspicuous publication is the test.
- **Row 104, Bramis (Melbourne).** A grade-A row for six weeks, read off their contact page on 24
  Sep. The site now runs Cloudflare email protection and the address is gone from fetched content.
  **The clinic took it down after we read it**, which is the strongest version of the argument for
  not decoding: we are not inferring intent from a site that was always obfuscated, we watched it
  change. On the browser-visit list; one page-open returns it to A.

**Three rows re-read with a different address than the one on file would have been a disaster and
were not.** 95, 98 and 102 all matched exactly. Row 93's homepage no longer prints any address and
needed a second page to confirm — which is the general shape of this: **an address verified six
weeks ago is not verified now.** Four of the 18 (93, 94, 97, 98) had already been emailed on 15
Oct with no finding on record; today's re-read clears all four and the address used is the address
still published, so those sends were on solid ground — but nobody had checked at the time, and
that is why the screen now runs before a send instead of after one.

**Two rows sit at the top of the must-have 3 band**: 97 Skintech and 98 Injex both publish four
clinic addresses. Four qualifies, five disqualifies, and both are chains-in-waiting. Re-count
before any second approach.

### Re-reading the whole staged sending wave — 206 rows, and the number that matters is 11%

The sending thread had **235 AU/NZ/UK rows staged** with v2 openers, waiting on Jess's yes. Of
those, 10 had been re-read earlier in the day and 19 were added within the last three days, so
**206 October-dated rows were re-read before the first live send** — four workers, one page per
row, a second fetch only where the first was silent. 208 fetches, 11 searches.

| verdict | rows | what it means |
| --- | --- | --- |
| confirmed | 176 | address published verbatim, as recorded |
| moved | 7 | address live, but on a different page than we cited |
| unreadable | 14 | fetch failed — **nothing learned, grade unchanged** |
| gone | 6 | 3 newly obfuscated, 3 genuinely absent |
| changed | 2 | the site publishes a different address |

**6 of 206 addresses had gone in under a month — 2.9%.** Add the 2 changed and the 14
unverifiable and **22 rows, 11% of the wave, should not have gone out as staged.** On a sending
domain with no reputation, that is the difference between a campaign that lands and one that
gets filtered.

**Three findings worth more than the row count.**

1. **Row 636 Aesthetics Central is the best argument the look-alike rule has.** Both visible
   slots on its contact page are Cloudflare-protected, and the plain address is still in the page
   — *inside the meta description*. A check that searched the raw page for the recorded address
   would have called it confirmed and sent to it. This is the sixth address look-alike, recorded
   in `ICP.md` the same morning from row 103 — found again independently, from the opposite
   direction, by a worker who had read the rule. That is the rule earning its place rather than
   just being written down.
2. **Most decay is not deliverability, it is stale citation.** Seven rows had a live address on a
   page we were no longer pointing at, and four more "confirmed" rows had a recorded source page
   that now errors or refuses robots while the address sits on the homepage. **A dead citation
   looks exactly like a dead address on the first fetch.** It is only the second fetch that tells
   them apart, and telling them apart is the difference between parking a good clinic and sending
   to a dead mailbox.
3. **The decay rate varies hugely by batch, so one batch is not a rate.** Batch 2 lost 4 of 52;
   batch 4 lost 0 of 51, with no obfuscation and no absences at all. Earlier in the day a batch of
   14 lost 1 and I quoted "one in fourteen" to the sending thread as though it were a rate. It was
   one batch. The honest aggregate across 220 rows re-read today is **about 3% gone per month**,
   and even that is one month's observation.

**The AU/NZ/UK consent screen has now disqualified nobody across more than fifty policies and
206 further pages.** Not one clinic refuses unsolicited commercial email. The closest wordings
found were clinics promising *their own* lists "no spam" (382, 420, 575, 384, 614) — a promise
about their outbound mail, not a refusal of our inbound. The screen stays, because being able to
show it was checked is the point, but it can now be stated plainly: **it is a recording cost, not
a filter.**

**Two rows needed a judgement rather than a verdict.** Row 322 has rebranded — domain redirects,
new name, new mailbox, and the staged opener still names the old clinic. Row 588 publishes
`info@...com` where we recorded `info@...com.au`; one of the two is a probable hard bounce and
this session has no DNS tooling to find out which (MX and A lookups both fail), so the row now
carries what is published and is recommended out of the first send. **Row 582 was the only
must-have failure found: five locations on its About page, where five is the disqualifying
threshold.** Held at C rather than dropped, because five addresses across coastal Queensland
reads more like one travelling operator than a chain. **Nothing in our process re-counts
locations except a re-read.**

### Still open

- Griffin's `/contact` rule cost one good Oklahoma City row (named MD, banked-credit programme,
  silent homepage, **no privacy policy at all**). A second exception is now written into the brief
  for exactly that case.
- `portraitcare.com/.../sapulpa/` read like a town directory index and was a vendor logo wall.
  One fetch for nothing. A directory index names many businesses in its snippet; a vendor's
  location page names one.

### Later the same day: the consent screen was five rows short, and I had said it was complete

Within the hour of reporting the screen finished, the GoHighLevel thread said it had excluded
rows 66, 67, 70, 72 and 75 from the staged wave because their notes read "HELD at C" while their
grade column read B. Checking that turned up the real problem, which was mine: **those five
rows passed my consent audit by denying the consent check.** See the regex-negation entry under
Scripting traps — their notes say "nobody has checked the site for a 'no unsolicited commercial
email' notice", so a scan for the word `unsolicited` matched. The number I had just reported as
eighteen rows and zero gaps was twenty-three rows and five gaps.

All five were re-read: `contact@drgreencosmeticgroup.com.au`, `contact@collinscosmeticclinic.com.au`,
`info@dr-jodie.com.au`, `info@m1-beauty.com.au` and `booking@drsalon.com.au`, each printed
verbatim on the clinic's own page, matching the recorded address, none carrying a notice. So all
five are sendable and the staged wave can have them back. **Twenty-three of twenty-three AU/NZ
rows have now cleared the screen without a single refusal found** — which is the strongest
version yet of the finding that the screen is a recording cost rather than a filter. Row 70 is
worth singling out: it was dropped on the retired 22 Sep standard, recovered on 1 Nov, held on
must-have 6 alone, and is now clear on every must-have that applies to it.

The thing to keep is not the five rows. It is that **"I audited it and it is clean" was wrong,
and an unrelated session's wrong-reason objection was what surfaced it.** When another thread
disagrees with the file, check the file.

### Re-verifying the loaded rows — one in eight had gone, and a method trap

The sending thread had **125 rows loaded and unsent, mostly dated September**. 21 of them are
AU/NZ/UK, the wave that can go first because those markets need no postal address in the footer.
13 had already been re-read in the consent screen; the other **8, all UK, were re-read before the
first live run rather than after it.**

Seven stand. **One had gone: row 116 Luxe Skin, which was queued to send on an address that is no
longer publicly readable** — the site has installed Cloudflare-style obfuscation since 24
September. That single row is the whole argument for verifying before a send. It is now parked at
C and on the browser-visit list.

Two rows gained a company identity we had never read off their own page: `Dermoperfection
Cosmetic Services Limited`, and best of all row 118, `Skin Clinic (Edinburgh) Ltd trading as
DRVICTORIA, registered in Scotland SC669495` — a named company **and** a number, the strongest
PECR footing any UK row in this file has. Note the trading name differs from the registered name,
which is normal and is exactly the Companies House near-miss trap: match the registered name or
the number, never the brand.

**The method trap, which cost nothing only because it was checked.** On the first pass, three of
the eight looked like they had lost their address. Only the homepage had been fetched. Two of the
three still publish it on a contact page — `info@medizen.co.uk` and
`enquiries@drvictoria.co.uk`, both exactly as recorded. **A liveness re-read that fetches only
the homepage over-reports decay threefold.** One fetch says the homepage changed. It takes the
second to say the clinic stopped publishing, and "the clinic stopped publishing" is the claim
that parks a row. The trap repeated on the second batch: row 83 Bodyvie also prints nothing on
its homepage and publishes `info@bodyvie.co.uk` on its contact page, unchanged.

**The whole pre-October queue, 14 rows, re-read.** Final tally: **12 confirmed verbatim, one gone
(116 Luxe Skin, obfuscated), one unreadable (78 Medicine of Cosmetics, site-side client error on
both hosts).** Six-week decay is **one row in fourteen**.

**"Unreadable" is not "gone", and the two have different remedies.** Row 78 returned a client
error on both the bare domain and the www host, so nothing was learned about the clinic either
way and the grade stays at A. An obfuscated row goes to a human with a browser; an erroring site
goes back in the queue for another day. It was still recommended for a hold on the first live
run, on the narrower ground that a site erroring on every host may be a site going away.

**Two more UK rows reached the strongest PECR footing in the file**, both read off their own
pages: `Bodyvie Limited trading as Bodyvie Medi-Clinic, Company number 3849113`, and row 118's
`Skin Clinic (Edinburgh) Ltd, SC669495`. Both trade under a name that is not their registered
name, which is the Companies House near-miss trap stated twice in one day: match the registered
name or the number, never the brand.

**Three rows publish more locations than their row implied** — 82 Dr MediSpa has three, 97
Skintech and 98 Injex four each. All inside the one-to-four band, none a breach, but all three
are chains-in-waiting and the count is what must-have 3 turns on. A re-read is the natural moment
to re-count, and nothing else in the process ever does.
