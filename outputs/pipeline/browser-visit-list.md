# Clinics we set aside only because a script could not read their address

**Built 2 November 2026, refreshed the same evening with that day's four sweeps, by collecting every such clinic out of `near-misses.md`, which had them
scattered across sixteen separate market write-ups where nobody was ever going to work through
them.** Every clinic here already cleared the ICP on fit. The single thing standing between it
and the pipeline is that the address did not survive an automated fetch. None of them has been
contacted, and none is in the sendable list.

There are **55** of them: 29 whose address is on the page but encoded, and 26 whose site refuses
automated reading altogether. **The two groups need different things, and that distinction is the
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

## Group B — the address is on the page, encoded (29 clinics)

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
