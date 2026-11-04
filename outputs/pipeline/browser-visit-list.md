# Clinics we set aside only because a script could not read their address

**Built 2 November 2026, refreshed the same evening with that day's four sweeps, by collecting every such clinic out of `near-misses.md`, which had them
scattered across sixteen separate market write-ups where nobody was ever going to work through
them.** Every clinic here already cleared the ICP on fit. The single thing standing between it
and the pipeline is that the address did not survive an automated fetch. None of them has been
contacted, and none is in the sendable list.

There are **73** of them: 34 whose address is on the page but encoded, 38 whose site refuses
automated reading or will not render, and one special case (row 352) described at the end.
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
