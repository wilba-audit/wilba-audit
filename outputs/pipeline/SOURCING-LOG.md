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

## Where the pipeline stands

As of 20 Oct 2026: **496 rows, 316 ready to approach** — US 138, AU 106, UK 34, NZ 21, CA 16,
IE 2. **Nothing has ever been sent from it.** The GoHighLevel thread holds every batch from
id 300 on until Jess approves the v2 copy, and sends are paused pending her word. The
bottleneck has never been the list.

The qualification standard is **ICP v2**, from Griffin's *Med Spa Reactivation* briefing,
which Jess uploaded on 16 Oct with "I want you to master this stratefy… you have authority to
take action". It inverted the 22 Sep standard: owner-operated, injectables-led, cash-pay, one
to four sites, and plastic surgery, dermatology, hospital groups and chains are now
disqualifications where they used to be targets.

## Two mistakes that keep recurring

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

## Four things that look like a published address and are not

A Cloudflare placeholder rendering as `[email protected]`. A website-builder default the
owner never replaced (`filler@godaddy.com`, `contact@wix.com`). An address shipped inside a
directory site's QR code image. An address served in a page's Open Graph meta tags while the
visible one is obfuscated. None is recoverable by opening the page in a browser, and none goes
in the pipeline. Obfuscation is not always Cloudflare, either: one Canadian site hand-rolled
`aesthevaclinic[@]gmail.com`.

Related: a dead clinic domain does not always 404. `19westaesthetics.com` now serves an
unrelated AI companion app.

## Scripting traps

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
