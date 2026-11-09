# Clinics we set aside only because a script could not read their address

**Built 2 November 2026, refreshed the same evening with that day's four sweeps, by collecting every such clinic out of `near-misses.md`, which had them
scattered across sixteen separate market write-ups where nobody was ever going to work through
them.** Every clinic here already cleared the ICP on fit. The single thing standing between it
and the pipeline is that the address did not survive an automated fetch. None of them has been
contacted, and none is in the sendable list.

There are **110** of them: 53 whose address is on the page but encoded, 56 whose site refuses
automated reading or will not render, and one special case (row 352) described at the end.
**Ten more were added on 8 November**, in their own section at the end, along with one clinic that
is a browser job for a different reason — its address is readable, but it is already advertising a
prize draw to "current, past, or prospective clients", which is a person's job and not a script's.
**14 were added on 4 November and 14 more on 5 November**, each in their own section at the end.
One further entry, added 5 November, is **not a clinic at all but a name source** — a local
paper's readers'-choice list that refuses automated reading — and it is listed separately because
opening it yields names rather than an address.
**16 were added on 3 November from the re-read of the staged sending wave, and every one of
those was queued to receive WILBA's first cold email.** They are listed in their own section at
the end of this file rather than merged into the tables above, because they are a different kind
of entry: not clinics we never reached, but clinics we had already verified and staged. **The two groups need different things, and that distinction is the
whole point of this file.**

---

## Group A — the site refuses automated reading (26 clinics)

These return `robots_disallowed`. There is nothing hidden and nothing to decode: the page is
ordinary, the site simply declines to serve robots. **Opening one in a browser shows whatever is
there, exactly as any customer sees it.** Our own brief has said for two weeks that these are
often the best clinic in their town, because a clinic careful enough to configure robots.txt is
usually a clinic that has been trading a while.

One page-open each. If an address is published, the clinic becomes a normal row.

| Clinic | Site | Market it came from |
| --- | --- | --- |
| Azure Aesthetics | `azureaesthetics.com.au` | AU — Australia, second pass — 18 Oct 2026, under ICP  |
| Bespoke Clinic | `bespokeclinic.com.au` | AU — Near misses — Australian outer-metro suburbs (1  |
| Beyond Beauty Injectables | `beyondbeautyinjectables.org` | AU — Coastal and inland Queensland near-misses and ru |
| Skin Social | `cosmetichqbydanielleryan.com.au` | AU — Australia, second pass — 18 Oct 2026, under ICP  |
| CQ Skin | `cqskin.com.au` | AU — Coastal and inland Queensland near-misses and ru |
| (name not captured) | `defineclinic.com.au` | AU — Australia, second pass — 18 Oct 2026, under ICP  |
| (name not captured) | `deviceconsulting.com.au` | AU — Near misses — Australia's last unswept corners,  |
| Face Against Time | `faceagainsttime.com` | AU — Regional Australia, third pass — near misses and |
| (name not captured) | `illuminateaesthetics.com.au` | AU — Australia, second pass — 18 Oct 2026, under ICP  |
| Kalology Skin Care | `kalology.com.au` | AU — Coastal and inland Queensland near-misses and ru |
| From the About page: | `karrathacosmeticinjectables.com` | AU — Australian mining and industrial belt — near mis |
| (name not captured) | `limestonelaserclinic.com.au` | AU — Australian mining and industrial belt — near mis |
| (name not captured) | `nursevickiaesthetics.com.au` | AU — Australia, second pass — 18 Oct 2026, under ICP  |
| (name not captured) | `soaesthetica.com.au` | AU — Australia, second pass — 18 Oct 2026, under ICP  |
| Tasmanian Skin Clinic, Devonport | `tasmanianskinclinic.com.au` | AU — Regional Australia, third pass — near misses and |
| The Skin Stylist | `theskinstylist.com.au` | AU — Australian mining and industrial belt — near mis |
| Clear Skin Clinic (Suffolk) | `clearskinsuffolk.co.uk` | UK — UK near-misses and rule-outs — round three — 1 N |
| Dr Sknn | `drsknn.com` | UK — UK near-misses and rule-outs — round three — 1 N |
| Milan Skin Clinic — Reading | `milanskinclinic.com` | UK — UK near-misses and rule-outs — 29 October 2026 |
| (name not captured) | `radiantaestheticsclinic.co.uk` | UK — UK near-misses and rule-outs — 22 October 2026 |
| Reverie Wellness & Aesthetics Clinic — Portsmouth | `reverieclinic.co.uk` | UK — UK near-misses and rule-outs — 29 October 2026 |
| Skin Sister Aesthetics — Hampshire (Basingstoke query) | `skinsister.co.uk` | UK — UK near-misses and rule-outs — 29 October 2026 |
| Art of Injections | `artofinjections.com` | US — US under-covered metros — near misses and rule-o |
| Skin By Liv Aesthetics | `skinbylivaesthetics.com` | US — US under-covered metros — near misses and rule-o |
| Botastic Aesthetics & Wellness LLC | `txmedicalaesthetics.com` | US — US under-swept Texas, Memphis, Little Rock and J |
| You Wellness | `youwellness.net` | US — Near misses — northwest Arkansas, San Antonio su |

## Group B — the address is on the page, encoded (31 clinics)

These render as `[email protected]`. **Our brief was wrong about these, and I corrected it today.**
It said a browser does not recover them and they should be dropped. Both halves are false.
Cloudflare email protection ships the real address in the page as a hex token and a script
decodes it when a person loads the page — hiding it from scrapers while showing it to humans is
the entire design. So a browser shows these normally, and we have been throwing away clinics
that were never unreachable.

I verified it rather than assuming: W Medical Aesthetics in Adelaide, long recorded here as
unreachable, carries the token `472e2921...` on its homepage, which decodes to a plain `info@`
address on its own domain.

**That raises a question I am not deciding on my own — see the note at the bottom.** For now these
are listed exactly like Group A: one page-open each.

| Clinic | Site | Market it came from |
| --- | --- | --- |
| (name not captured) | `academyfaceandbody.com.au` | AU — Australia, second pass — 18 Oct 2026, under ICP  |
| (name not captured) | `aesthetiquemedical.com.au` | AU — Australia, second pass — 18 Oct 2026, under ICP  |
| (name not captured) | `ascension.com.au` | AU — Australia, second pass — 18 Oct 2026, under ICP  |
| (name not captured) | `cancosmed.com` | AU — Australia, second pass — 18 Oct 2026, under ICP  |
| meta tags | `salclinic.co.uk` | AU — New Zealand, regional Australia, the UK outside  |
| (name not captured) | `skindeepcc.com.au` | AU — Coastal and inland Queensland near-misses and ru |
| Site: | `skindermaesthetics.com` | AU — Australian mining and industrial belt — near mis |
| (name not captured) | `skintosoulclinic.com.au` | AU — Australia, second pass — 18 Oct 2026, under ICP  |
| (name not captured) | `skosmetics.com.au` | AU — Australia, second pass — 18 Oct 2026, under ICP  |
| (name not captured) | `yourserenity.com.au` | AU — Coastal and inland Queensland near-misses and ru |
| (name not captured) | `gmail.com` | CA — Canada and the US secondary metros — 20 Oct 2026 |
| Mouna MédiSpa | `janeapp.com` | CA — Canada round 3 — near misses and rule-outs — 28  |
| `[email protected]` | `medicalspabuffalo.com` | CA — Canada and the US secondary metros — 20 Oct 2026 |
| Modern Skin Medispa | `modernskin.ca` | CA — Canada round 2 — near misses and rule-outs — 21  |
| PSA MedSpa (Pearl Skin Aesthetics) — Huntsville, AL | `psamedspa.com` | CA — Canada and the US secondary metros — 20 Oct 2026 |
| nothing for a browser to decode | `dgaesthetics.uk` | UK — UK near-misses and rule-outs — round three — 1 N |
| Site: | `newcastleskinclinic.co.uk` | UK — UK near-misses and rule-outs — 22 October 2026 |
| An "Email Us" link with no address printed | `theluxeskinclinic.co.uk` | UK — UK near-misses and rule-outs — 29 October 2026 |
| Chic la Vie Med Spa — Las Vegas (Sahara Ave, Summerlin side), NV | `chiclavie.com` | US — Nevada + California-gap near-misses and rule-out |
| Dahlia by WHA | `dahliabywha.com` | US — Near misses — northwest Arkansas, San Antonio su |
| gmail | `dvashaesthetics.com` | US — US under-swept Texas, Memphis, Little Rock and J |
| Face & Beyond Aesthetic Lounge — Turlock, CA | `faceandbeyondaestheticlounge.com` | US — California Central Valley and inland south — nea |
| Two fetches spent | `firmmedicalspa.com` | US — Northwest Arkansas, then eastern Oklahoma — near |
| Franco Aesthetics — Norman, OK | `francoaesthetics.com` | US — Northwest Arkansas, then eastern Oklahoma — near |
| Natausha Spears, RN, BS | `injectableaesthetics.com` | US — Northwest Arkansas, then eastern Oklahoma — near |
| Zenoti | `luxefactorlv.com` | US — Nevada + California-gap near-misses and rule-out |
| (name not captured) | `mbsmedspa.com` | US — Near misses — northwest Arkansas, San Antonio su |
| Modesto Aesthetics & Laser — Modesto, CA | `modestoaestheticsandlaser.com` | US — California Central Valley and inland south — nea |
| Antidote Aesthetics | `treatment-builder.com` | US — Near-misses — coastal Virginia, the Carolinas, G |

---

## The decision I am not making unilaterally

Group B can be decoded in about four lines of code, from page content we already fetch. Doing
that would turn 29 clinics into pipeline rows this afternoon, with no browser work and no
guessing — the decode is exact, not inferred, and it returns the address the clinic itself put
on the page.

**I am not doing it, and I would advise against it, for a reason that is not procedural.** A
clinic running email obfuscation has taken a deliberate step to stop automated collection of
that address. Decoding it is precisely the thing they acted to prevent. That matters beyond
etiquette, because the consent regimes we screen every row against turn on how the address was
published: the Australian Spam Act and Canada's CASL both rest on an address being
*conspicuously published*, and an address deliberately withheld from automated readers is a weak
basis for unsolicited mail at best. A human opening the page the clinic renders for humans is a
different act from a script stripping the protection off it.

So my recommendation is the boring one: **work Group B by browser like Group A, and leave the
decoder unwritten.** It costs Jess a few minutes per clinic and keeps the consent story clean.
If she would rather we decode, that is her call to make and it is easy to implement — but it
should be a decision taken on purpose, not a shortcut a worker takes because it is available.

## Working through this list

Open the site, look for an address on the homepage footer, the About page or the contact page,
and send it back however is easiest. Anything that comes back gets the same treatment as a
sourced row: recorded verbatim with the page it was read on and the date, the consent screen for
its country, and a grade. **An address read in a browser is "seen" for our purposes** — the rule
that has never moved is that nobody constructs or guesses one.

A clinic that turns out to publish nothing at all stays in `near-misses.md` as it is, and the
only route left to it is a phone call or a direct message.


---

## Added 3 November 2026 — a clinic that moved onto this list

**Bramis Facial Rejuvenation Clinics** · `bramis.com.au` · AU, Melbourne · pipeline row **104**

This one is different from every other entry, and worth a paragraph. Bramis was not set aside
because a fetch failed. It was a **grade-A row with its address read off `bramis.com.au/contact/`
on 24 September** and it sat in the sendable list for six weeks. Re-reading it today, during the
AU consent screen, the contact page now ships two `/cdn-cgi/l/email-protection` links and the
address is gone from the fetched content. The clinic installed email obfuscation *after* we read
it.

That sequence is the strongest version of the argument in Group B above for not decoding. We are
not looking at a site that has always been obfuscated and guessing at intent — we watched this
clinic take the address down. Decoding the token would hand us back exactly the thing they just
stopped publishing. The row is parked at C with must-have 5 named, the address is kept in it, and
**if Jess opens the page in a browser and sees an address, row 104 goes straight back to A.**

Dr Mela is billed as a twice-voted top-100 injector worldwide, so this is a clinic worth the
browser tab.


## Also added 3 November 2026 — the one that was queued to send

**Luxe Skin** · `luxeskin.co.uk` · UK, Glasgow · pipeline row **116**

Same shape as Bramis above and more urgent, because this row was **already loaded into the
sending tool and queued for the first live run**. Its address was read on 24 September; the site
now renders it as `[[email protected]]` in both the visit section and the footer. Obfuscation
installed some time in the last six weeks.

This is the row that justifies re-verifying an address before a send rather than after one. Had
the run gone out on the September list, the first email of WILBA's first live campaign would have
gone to an address that is no longer publicly readable.

One page-open returns it. No company identity is published either (trading as "Luxe Skin
Aesthetic Clinic by Dr Q", no Ltd suffix, no number), so if the browser gives up an address, the
UK company check still has to be run before it can send.


---

# Added 3 November 2026 — from the re-read of the staged sending wave

All 206 October-dated rows staged in the sending tool were re-read before the first live send,
one page each with a second fetch where the first was silent. 176 confirmed, 7 had simply moved
their address to another page, 2 had changed it. **These 16 could not be sent to**, and all 16
were in the queue.

## Encoded since we read them (3) — the clinic installed obfuscation after verification

| Row | Clinic | Site | Note |
| --- | --- | --- | --- |
| 382 | Wellington Cosmetic Clinic | `wellingtoncosmeticclinic.co.nz` | All three email links now Cloudflare tokens |
| 412 | Enrich Aesthetics | `enrichaesthetics.com.au` | Address was read 19 Oct — obfuscated within the fortnight |
| 636 | Aesthetics Central Clinic | `aestheticscentral.co.uk` | See below — the most instructive of the three |

**Row 636 is worth reading twice.** Both visible slots on its contact page are Cloudflare-
protected, but the plain address is still in the page *inside the meta description*. Anything
that merely searched the raw page for the recorded address would have called this a clean
confirm and sent to it. It is the sixth address look-alike recorded in `ICP.md` the same day,
found independently from the opposite direction: **a meta-tag address behind an obfuscated
visible one is not conspicuous publication.** None of the three was decoded.

## Site would not serve or would not render (12)

A person opening these sees the page normally. Ten refused robots; two render client-side and
served no text.

| Row | Clinic | Site | Failure |
| --- | --- | --- | --- |
| 310 | The Louve Skin Clinic | `thelouveskinclinic.com.au` | robots |
| 347 | Art of Aesthetics | `artofaesthetics.com.au` | renders partially; its `/contact` client-errors |
| 366 | Skinave Co | `skinaveco.com.au` | robots |
| 386 | Clinic 23 | `clinic23.co.nz` | robots |
| 421 | The Cosmetic Club | `thecosmeticclub.com.au` | robots |
| 429 | The Aesthetics Table | `theaestheticstable.co.uk` | renders empty on three fetches |
| 433 | Blend Skin & Aesthetics | `blendskinandaesthetics.co.uk` | robots |
| 503 | Iylah Aesthetics | `iylahaesthetics.com.au` | robots |
| 587 | Shoal Aesthetics | `shoalaesthetics.com.au` | robots |
| 610 | Naked Face Clinic | `nakedface.co.nz` | robots |
| 632 | HDM Aesthetics | `hdmaesthetics.co.uk` | robots |
| 730 | Aesthetik Skin & Body | `aesthetikskin.com.au` | robots |

**These rows keep their grade.** Nothing was learned about them in either direction, which is
the whole distinction: an unreadable site is not a dead address. They were recommended for a
hold on the first send only because an unverifiable address on a domain with no sending
reputation is a risk not worth taking, not because anything is wrong with the clinic.

## One special case (1)

**Row 352, Finesse Cosmetic Therapies** · `finessecosmetics.com.au`. Its address is absent from
the homepage and the About page, both of which render fine with no obfuscation — so on the
evidence it has been taken down. But the site's own `/contact-us/` returned a server error, so
two pages were read and the third could not be. **One browser look settles whether this is a
withdrawn address or just a broken page**, which is why it is here rather than written off.

## Not on this list, because a browser will not help

Four rows failed in ways a person cannot fix by opening a tab, and are phone or DM prospects:
**660 Face Works** and **350 The GOSS** (site-side errors with no content at all, on every path
including `thegoss.au`'s redirect), and **308 U Skin Clinics** and **742 SO Aesthetics**, whose
pages render perfectly and simply no longer publish an address anywhere.


---

# Could a headless browser do this instead of Jess? Tested 4 November 2026. No.

This question will occur to every future run, because the sourcing session has a real
Chromium and Playwright installed. It was tested properly rather than assumed, and the answer
is no — for two separate reasons, and the second one is the one that actually closes it.

## First, most of this list should not be opened by a robot even if it could be

The three groups are not equivalent and a browser is not the right tool for two of them:

- **Renders client-side (2 rows).** A browser is exactly the right tool. No directive is being
  disregarded and no obfuscation defeated; the rendered page is what any visitor sees. This is
  the one legitimate case.
- **robots_disallowed (38 rows).** `robots.txt` is a directive addressed to automated agents,
  and a headless browser driven by this session **is an automated agent**. Driving one at a page
  the site asks robots not to read is circumvention, not cleverness. Not done, and not to be
  done without Jess deciding it.
- **Cloudflare-encoded (34 rows).** A real browser recovers these, because the page's own
  JavaScript decodes the token — that is the entire design. But that is also precisely the
  automated collection the clinic installed it to prevent. It is the same question answered on
  2 Nov about decoding the token arithmetically, and automating a browser instead does not change
  the answer, only the mechanism. Not done.

So on the rules we already hold, a browser could legitimately clear **2 of 73**.

## Second, this container cannot reach these sites at all

It could not even clear those 2. Chromium launched fine, and both navigations failed with
`ERR_TUNNEL_CONNECTION_FAILED`. The container's outbound HTTPS goes through an agent proxy,
which answered **403 to CONNECT** for both clinic hosts — a policy denial, logged in the proxy's
own status as `connect_rejected`.

That is worth understanding precisely, because it explains something otherwise confusing:
**`WebFetch` works on clinic sites and a browser in this container does not.** They do not use
the same path out. `WebFetch` is fetched for us; the browser uses this container's network,
which is restricted by the environment's network policy. This project has **no cloud environment
selected**, so it runs on a built-in one whose network settings cannot be changed from here.

**Conclusion: this list needs a person with an ordinary browser, and that has not changed.**
If Jess ever wants the two render-failure rows done automatically, it needs a cloud environment
with broader network access, which is a setting in the Add cloud environment dialog under
[Project settings](#project-settings/environment) — not something this session can arrange.
And even then it would be 2 rows of 73, because the other 71 are a question about what we are
willing to do, not about what we are able to do.


---

# Added 4 November 2026 — from the UK southern half, the Central Valley remainder and Canada round four

Fourteen clinics, all of which cleared the ICP on profile and none of which could be read. **The
Canadian encoded group is the most valuable thing on this whole page**, because the three deepest
trading histories found in that sweep are all in it — and a deep trading history is the lapsed
patient list the offer is built on.

## Encoded address — a browser shows it, a fetch cannot (7)

| Clinic | Site | Market | What makes it worth the tab |
| --- | --- | --- | --- |
| **Vaughan Laser & Anti-Aging Medical Clinic** | `vaughanlaser.com` (Woodbridge, Vaughan ON) | CA round 4 | **"Established in 1999" — 27 years, the deepest history in the sweep.** One site, real review history. Open questions to settle in the same visit: the menu carries laser vein therapy and nail fungus (must-have 2), nobody is named as owner, and the page's own "over 24 years" / "past 25 years" claims disagree with the 1999 date |
| **Mezzmerize Medical Aesthetics** | `mezzmerize.ca` (Burlington ON) | CA round 4 | Cathy Mezzalira RN founded it in **2008 — 18 years, stated**; a mother-and-daughter practice with two injectors. Settle one thing first: the Medical Director is a board-certified plastic surgeon who separately founded Appleby Plastic Surgery. Surgeon-*owned* is a disqualification, surgeon-*supervised* is not |
| **Willow Medical Aesthetics** | `willowmedicalaesthetics.ca` (Courtenay + Campbell River BC) | CA round 4 | Dr Liezl Sullivan MD, **practising aesthetic medicine since 2005 — 21 years**, three doctors, two sites. The policy was read in full: **no refusal notice, and both street addresses in plain text.** Only the mailbox is hidden |
| **Kiss Me Med Spa** | `medspakissme.com` (Fresno CA) | Central Valley | Karen RN, **operating partner since 2013** and an aesthetic nurse since 1997. Named senior partner, laser nurse, derm tech, two vacancies. **Memberships AND banked account credit**, which is exactly the dormant structure the offer acts on. Must-haves 1-4 clear; 5 is one tab away. The surname renders as lower-case "tesi" — confirm it before using it |
| **Ottawa Medical Spa & Aesthetics** | `ottawamedicalspa.ca` (Kanata ON) | CA round 4 | MDware booking, gift certificates, promotions page. Policy read in full, no refusal notice. Caveats: day-spa hybrid, two conflicting postal codes printed, no owner named |
| **Mana's Med Spa** | `manasmedspa.ca` (Aurora ON) | CA round 4 | Injectables plus a broad skin and laser menu, free consultations, one site. **Resolve the menu before spending the tab:** electrolysis, lash and brow, teeth whitening, tooth gems and acupuncture alongside the injectables, so it is a beauty-spa hybrid with the extended-health question attached |
| **Sculpt Medispa** | `sculptmedispa.ca` (Unionville / Markham ON) | CA round 4 | **DO NOT SPEND A TAB YET.** Michelle Mag-iba RN is a Galderma Canada clinical trainer with her own training programme, which is a strong second list — but the page says Sculpt "encompasses surgical and non-surgical cosmetic procedures" and her listed skills include hormone replacement therapy. Either fails. Two Unionville addresses are printed, so the site count is unresolved too |

## Site refuses automated reading (4)

A person opening these sees an ordinary page. Nothing is hidden and nothing is encoded.

| Clinic | Site | Market | Why it is worth the tab |
| --- | --- | --- | --- |
| **mAesthetics** | `maesthetics.co.uk` (Salisbury, Wiltshire) | UK south | Surfaced twice on two different Salisbury queries, ranking above everything else in the town, described as "Nurse Led Aesthetics and Skincare". **On ranking alone, likely the strongest independent in Salisbury.** Completely unassessed — unqualified, not disqualified. Check the domain: there is an unrelated `maesthetics.com.au` and an `hdmaesthetics.co.uk` in Hull already in the pipeline |
| **FOŶ Aesthetics & Skin Clinic** | `foyaesthetics.co.uk` (Brighton & Hove) | UK south | One of only **two** clinics with their own domain that the Hove queries surfaced at all. Hove's independent layer is thin enough that one unread clinic is a material fraction of it |
| **Reborn Aesthetics** | `rebornaesthetics.ca` (Orléans, Ottawa ON) | CA round 4 | A direct hit on an "Orléans nurse injector" query, and **Orléans produced nothing else at all.** Nothing retrieved: no email, owner, menu, platform or address. Could be a free row or a rule-out |
| **Dermalogic** | `dermalogic.ca` (Greenbank Road, Ottawa ON) | CA round 4 | One of the nine clinics the Ottawa directory index names, which is weak evidence of being established and independent. Unassessed |

## Will not render for a fetch (2)

These return HTTP 200 and a document head with no body. The fetch is spent before you know the
page is empty.

| Clinic | Site | Market | Note |
| --- | --- | --- | --- |
| **Uplift Medical Aesthetics** | `upliftmedicalaesthetics.ca` (Nanaimo area BC) | CA round 4 | Metadata and one stray line only. **Not the same business as Uplift Aesthetics, Winnipeg**, which is already a grade-A row from 28 Oct — similar name, different province |
| **Burlington Skin Clinic** | `burlingtonskinclinic.com` (Burlington ON) | CA round 4 | No body content whatsoever |

## A sixth failure mode, and its first entry (1)

| Clinic | Site | Market | Note |
| --- | --- | --- | --- |
| **Luminesse Laser & Skin Clinic** | `luminesselaser.ca` (Centrepointe, Ottawa ON) | CA round 4 | **HTTP 200, a complete page, and the entire content was "Please wait while your request is being verified".** A challenge interstitial: not obfuscation, not robots, not client-side rendering, not a site error. **A person's browser clears this in about a second**, which makes it one of the cheapest tabs on this page |

## Not added, and why — so the next worker does not re-file them

- **`alle.com/discover/l-visalia-california`**, the Allē provider locator, renders client-side. It
  is **a page, not a clinic**, and it is the single highest-value page in that market for a human
  with a browser: by definition it is the list of clinics buying one manufacturer's line in a
  named town. The brief's client-side list has been updated.
- **`d3medspa.com`**, **`amandahydeskin.com`**, **`dripfact.com`** (Central Valley) and **Nurse
  Rachel** / **Lumina MD `/contact`** (BC) all return site-side errors or bare metadata with no
  town even establishable. A browser is no more likely to help than a fetch.
- **Pamela Fletcher Aesthetics** (Sussex) — site-side error, and no phone number either, so there
  is no route to it at all until the site comes back.
- **Revive Medical Aesthetics** (Visalia) and **Aesthetic Club / `aestheticclubcorp.com`**
  (Clovis/Fresno) are robots-refused and were already logged on 2 Nov. The 2 Nov worker asked for
  Aesthetic Club to be settled before the next Central Valley run; **the 4 Nov worker could not
  settle it either**, because it refuses the fetch and nothing else about it surfaced in sixteen
  queries. **It needs a browser tab, not another sourcing run** — that is twice now.

## What the UK contributed to this list: nothing, and that is the finding

**Zero encoded addresses in 27 British businesses opened.** The 1 Nov UK round found two in
eighteen. The browser-visit workaround rescued nothing in that market, because **the thing Britain
withholds is not the address — it is the company identity** that must-have 8 needs. A tab does not
fix that; a register search does.


---

# Added 5 November 2026 — from Utah, Phoenix, York Region and the UK northern half

Fourteen clinics and one name source. **The pattern across four markets in one day is the thing
worth reading here**: the obfuscation rate is not a property of the trade, it is a property of the
market. Affluent Ontario and Utah hide addresses; **Phoenix hid none at all in 46 businesses**,
and Britain hid two, the same low rate every British sweep has found.

## Encoded address — a browser shows it, a fetch cannot (7)

| Clinic | Site | Market | What makes it worth the tab |
| --- | --- | --- | --- |
| **Urban Injections** | `urbaninjections.com` (Syracuse, Davis County UT) | Utah | **The strongest parked profile in Utah.** Stacie Colby RN BSN is published as Owner, with a named medical director and four more staff; "8+ Years"; self-describes as locally owned; Jane App booking. **Two priced memberships that both include monthly credits**, a new-client welcome credit, gift cards and a consultation credit — banked credit is the single best dormant signal we look for |
| **Nuance Aesthetics + Wellness** | `nuanceaesthetics.com` (9th and 9th, Salt Lake City) | Utah | **"Since its inception in July of 2015" — eleven years, verified.** Dr Rhudy is Owner and Medical Director with Jill Miller as Co-Owner. **"The Nuance+ Membership — a monthly fee banked toward any service"**, plus a second membership tier, a VIP page and an SMS opt-in. The token sits on the privacy policy and the homepage publishes nothing. One oddity for a human's eye: the SMS consent text names "Abundant Salon", which matches nothing else on the site |
| **Spruce Aesthetics + Infusion Bar** | `sprucespa.com` (Holladay UT) | Utah | A grade-A profile on everything except the address: Lauren Lightfield NP as Co-Founder and CEO, Dr Robert Sawyer MD as Co-Founder and CMO, six more named staff including two nurse injectors, Zenoti booking, memberships, refer-a-friend, gift cards and payment plans. Rebranded from Olympus Health and Performance |
| **Elite Skin Rejuvenation Medical Spa** | `eliteskinrejuvenation.ca` (Vaughan/Woodbridge ON) | York Region | One of the three clinics a directory named and nobody had opened; two of the three went straight into the pipeline and this is the third. One site, broad cash-pay menu, and the "Rosacea & Veins" line is IPL and laser — the cosmetic case, not venous disease, so must-have 2 is not a problem here. The token is in both the header and the footer, and there is no mailto and no privacy policy |
| **ENRICHED Med Spa** | `enrichedmedspa.com` (Woodbridge + East Gwillimbury ON) | York Region | Two sites, a full injectables and device menu, Vivier and ZO retail, and page metadata carrying a 2017 publish date as a trading proxy. Four fetches across two pages produced no plaintext. **Its loyalty mechanism is Brilliant Distinctions, a manufacturer's programme — not a parent-group tell**, and the brief now says so. Its own two postal codes for the Woodbridge address disagree |
| **Aesthetics by Sarah Williams** | `aestheticsbysarahwilliams.com` (Jesmond, Newcastle + Holmfirth) | UK north | **Chase this one first of the two British ones.** Sarah Williams, Advanced Nurse Practitioner and Independent Prescriber, named and NMC registered, "25+ Years Nursing Experience". Two rooms rented inside host clinics, which is the one-decision-maker pattern, so must-have 3 passes. ThermaVein on the menu is cosmetic thread-vein work and does **not** fail must-have 2 — do not park this one on veins |
| **Jesmond Aesthetics** | `jesmondaesthetics.co.uk` (Newcastle) | UK north | **Low priority despite being cheap.** No practitioner named, no founding year, no company identity, no review count, a five-item menu, and the page ships unrendered template placeholders (`{{related_areas}}`). It reads like a part-built template site. **Jesmond is now worked out** — four near-miss entries across two sweeps, zero sendable rows |

**The helper's behaviour on these was inconsistent, which is the whole argument for the recording-step rule.** On Urban Injections it volunteered the decoded address and named the token it came from; on Nuance it volunteered the decode **and stated the XOR key it had used**; on Spruce, on both Ontario clinics and on both British ones it reported the token and stopped. Every worker refused every offer and said so in writing. **If the rule had been "do not decode", the two volunteered plaintexts would have arrived without any decision being made at all.**

## Site refuses automated reading (4)

| Clinic | Site | Market | Why it is worth the tab |
| --- | --- | --- | --- |
| **Beauty Spell Injectables & Skincare** | `beautyspellaz.com` (Surprise AZ) | Phoenix | **The only independent Surprise clinic the sweep surfaced that was not ruled out on profile**, and the only browser-visit entry Phoenix produced at all |
| **SQ Medi Spa** | `sqmedispa.ca` (Main Street Unionville, Markham ON) | York Region | Named by the Unionville Main Street business directory, which is the kind of index that has been reliable. Completely unverified — no menu, address, ownership or site count was retrieved |
| **Dr Melanie Aesthetics** | `drmelanieaesthetics.com` (Southport, Merseyside) | UK north | A doctor-named Southport clinic; nothing is known beyond the search title. Two minutes in a browser |
| **Liv Aesthetics** | `liv-aesthetics.com` (South Jordan UT) | Utah | A narrow case: the **homepage read fine and published no address**, so the privacy policy was the one route left, and it is the policy that refuses the fetch |

## Will not render for a fetch (2)

| Clinic | Site | Market | Note |
| --- | --- | --- | --- |
| **Halo Aesthetic Clinic** | `haloaestheticclinic.com` (Richmond Hill ON) | York Region | A React shell: title, tags and "You need to enable JavaScript to run this app". Its meta description is the only content on the page. **Do not spend a fetch on its policy or terms pages — they will be the same shell** |
| **LM Clinical** | `lmclinical.co.uk` (Leamington Spa) | UK north | Metadata and a "Skip to main content" link. All that is readable is nurse-led, Royal Leamington Spa, and a four-item menu. **Leamington Spa was the richest town in that market**, which is what makes this worth two minutes |

## A seventh thing that looks published and is not (1)

| Clinic | Site | Market | Note |
| --- | --- | --- | --- |
| **Balanced Body** | `balancedbodyutah.com` (Kaysville UT) | Utah | Three named co-founders — Mindy Wade APRN, Cindy Kelfer RN and Clint Kelfer. Their footer prints what is plainly an address **split across a line break**: `info@balanced` on one line and `bodyhealthcare.com` on the next, and that is a **different domain from the website**. Recording it would mean doing two forbidden things at once: joining two visible fragments into a string the page never renders as one, and then accepting a domain the site does not use. **A human reading the footer sees one address**, which is exactly why this belongs here rather than in the bin |

## Not a clinic — a name source that refuses the fetch (1)

**City Weekly, "Best of Utah: Body & Mind"** — `robots_disallowed`. Not a prospect and it cost a
fetch to discover. It is the one human-written local readers'-choice list that surfaced anywhere in
Utah, organised by category, and **it is probably the single highest-yield page in that market**.
Opening it hands over names, not an address, so it is a different kind of errand from everything
above: whoever reads it should write the names down rather than look for a mailbox.

## What four markets in one day settled about this list

- **Phoenix produced exactly one entry in 46 businesses**, and that one was a robots refusal. Not a
  single page in the metro shipped an email-protection token. Recorded as a measured absence rather
  than an omission, because the contrast is the finding.
- **Utah produced four**, including the two best profiles of the day, and its clinics hide addresses
  the way affluent Ontario does.
- **Britain produced two**, the same low rate as every previous British sweep. What Britain
  withholds is company identity, and a browser tab does not fix that.
- **No market produced a challenge interstitial.** The sixth failure mode, found on 4 Nov, has one
  instance and has not reproduced in four markets since.

---

## Added 8 November 2026 — Chicago's affluent suburbs, Seattle's eastside, the Nashville ring

**Nine clinics, and one deliberate exclusion worth reading before the table.** A seventh
fetch-failure mode was found twice on 8 November — a privacy policy that nominates an email route
and then omits the address, as in *"please email them to ."* — and it does **NOT** belong on this
page, because no browser recovers a sentence the site never wrote. Those two went to
`near-misses.md` instead. This page is only for addresses that exist and that a script could not
read.

| Clinic | Domain | Market | Why a browser fixes it |
| --- | --- | --- | --- |
| **Dermatique Laser and Skin** | `dermatique.com` (Geneva IL, 407 S Third St Suite 240) | Chicago, 8 Nov | **The highest-value tab on this whole page, and the worker said so unprompted.** Cloudflare: the privacy policy renders `[email protected]` and the page carries two `cdn-cgi/l/email-protection` tokens, so NOT SEEN. **The best dormant-list structure found in that market and the only enterprise system in it** — Zenoti throughout (booking, patient portal and gift cards all resolve to `dermatique.zenoti.com`), a Skin Membership, a "Bloom Loyalty Rewards" programme, an "Insider" programme with early access, Zenoti gift cards and Allergan Data Labs financing. Postal address and phone (630-262-2515) are readable. Note the helper offered no decode this time, so nothing was offered and nothing refused. Must-have 3 is unresolved: no owner named, and "full-time physicians, Nurse Practitioners, Aestheticians, and Laser Technicians" is a bigger staff than one decision-maker implies — worth settling in the same visit |
| **Kucumber Skin Lounge** | `kucumberskinlounge.com` (Bellevue WA) | Seattle, 8 Nov | Cloudflare. **A would-be grade A: 380+ reviews and trading since 2010**, so must-have 4 is already evidenced twice over. One tab from being one of the strongest US rows in the file. Note its `areas-served/<town>` page set is blocked from sourcing queries, which is a separate matter from reading its address |
| **RejuvenationMD** | `rejuvenationmdaesthetics.com` / `rejuvenationmdmedspa.com` (Seattle eastside) | Seattle, 8 Nov | Cloudflare — **and the one where the rule was tested and held**: the fetch helper volunteered the decoded plaintext unasked and the worker discarded it, as recorded in the file. The address exists on the page and a person reading it in a browser is the only route we will take to it |
| **Skin Essentials Med Spa** | `skinessentialstn.com` (Brentwood TN) | Nashville, 8 Nov | Cloudflare-encoded; the helper offered no decode and none was attempted. Reached only via the Downtown Franklin association listing, which was the best fetch of that run |
| **Nolo MedSpa** | `nolomedspa.com` (Nolensville TN) | Nashville, 8 Nov | Robots-refused. Runs **Jane App** and is **owner-CRNA**, so it clears on platform and on must-have 3 before anyone opens it. The close-out search proved the domain is live, which is the one thing that search is actually good for |
| **La BeauTe Medical Spa & Laser Hair Removal** | `labeautemedspa.com` (Lake Forest IL) | Chicago, 8 Nov | Client-side render. Two fetches, homepage and contact page, both returned nothing but front matter and a single `meta-viewport` tag, so the ICP could not even be screened. **One of only two Lake Forest independents found** |
| **Blue Seas Med Spa** | `blueseasmedspa.com` (Naperville + Glen Ellyn IL) | Chicago, 8 Nov | Partial render rather than silence: one fetch returned a truncated fragment of an Allē rewards blog post and none of the nine items asked for. The Allē tie is a MANUFACTURER programme, so per the 5 Nov clarification it is a grade-A signal and not a parent-group tell. Two towns, both in market. Unresolved rather than screened |
| **Eastside Aesthetics and Wellness** | `eastsideaestheticsandwellness.com` (Seattle eastside) | Seattle, 8 Nov | Client-side render |
| **HC Med Spa** | `hcmedspa.com` (Seattle eastside) | Seattle, 8 Nov | Client-side render. **Its town is also unresolved**, so the visit should settle which eastside town it is actually in — the town-in-the-postal-address rule caught a sibling case the same day, where a `/bothell-washington` URL belonged to a Bellevue clinic |

| **Pure Perfection Clinic** | Wrexham, Wales | UK, 8 Nov | Cloudflare-encoded; decode not offered and not taken. **Must-haves 4 and 8 are already answered before anyone opens it** — established 2008, Ltd with company number 10719135, and 60 published reviews, which is the quantified review count British clinics almost never print. The worker stated its entry grade so nobody re-argues it on arrival: **C on must-have 2 unresolved**, for a bare "sclerotherapy" with no indication named. Under the rule settled the same day, read the modality and the practitioner's licence first, and the site-limited search on its own page titles before any fetch |

**One clinic that is a browser job for a different reason — not an unreadable address.**
**Skintegrity MedSpa** (`skintegritymedspa.com`, Kirkland / Bellevue / Redmond) publishes enough to
be read, and the Seattle worker's judgement was that it "needs Jess with a browser, not another
sourcing pass": **it already runs a prize draw open to "current, past, or prospective clients"**,
which is a clinic advertising for exactly the cohort our offer works. No further fetch will improve
on that; a person looking at it will.

**And a market-level note that belongs here rather than in the pipeline: Kirkland WA is SILENT,
not unworked.** Four clinics found, zero published emails. It is a browser market, not a sourcing
market, and it has now been established at cost so nobody re-queries it.

| **SeeBeyond Beauty** | `seebeyondbeauty.com` (Scarsdale NY + Greenwich CT, 2 sites) | Westchester/Fairfield, 9 Nov | Cloudflare — the policy renders the literal `[email protected]` **twice**, each linking a `cdn-cgi/l/email-protection` token, in a sentence that reads "Contact See Beyond Beauty at [address] or 914-635-4609 to exercise these rights". Not seen, not recorded. Strong on fit before anyone opens it: Dr Joon Lee, "20+ Years", "Over 10,000 patients", three priced membership tiers. **Free CRM detection off the same fetch: the policy names LeadConnector, so this is a GoHighLevel clinic** — worth knowing before the call. **Settle one thing in the same visit:** the menu carries a heading "Facelift" and says "View All 22 Services" while showing 20. If that is a surgical facelift the plastic-surgery disqualification bites; nothing else on the page is surgical |
| **Luxe Level Aesthetics** | `luxelevelaesthetics.com` (Darien CT) | Westchester/Fairfield, 9 Nov | Cloudflare — renders the literal `[email protected]` beside the word "Email" in Contact Us. Not seen, not recorded. **Second gap to close in the same visit: must-have 4 is unevidenced** — the only date on the site is a "© 2025" copyright, which under the three-year convention proves nothing |
| **Applied Aesthetic** | Garden City NY | Long Island, 9 Nov | Cloudflare on **both the homepage and the privacy policy**, which is why no route reached it. **The best row Long Island has, and it is not close**: 301+ published reviews, a "Beauty Bank" banked-credit membership — the dormant-credit mechanism the offer is built for — and a named FNP owner. Everything but the address is already answered |
| **The Skin Clinic** | Huntington NY | Long Island, 9 Nov | **CleanTalk encoding**, the eighth fetch-failure mode and the first instance of it: the page renders `th****@gm***.com` and says outright the address is protected, and the masked domain behind the `mailto:` differs from the masked domain in the text. Same answer as Cloudflare for the same reason — the page did not ship the characters |
| **Rejuv Aesthetix** | Long Island NY | Long Island, 9 Nov | Client-side render, site-wide. Nothing was screenable, so this is unresolved rather than qualified — the visit decides whether it is in the market at all |
