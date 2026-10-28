# Near misses — good clinics we cannot email

Clinics that clear the ICP on profile but publish **no machine-readable email
address**. They are recorded here so nobody spends another hour re-researching
them, and so Jess can decide whether any are worth a phone call.

**Never construct an address for any clinic on this list.** Several of them
obfuscate their email with Cloudflare, which means the address *is* on the page
and readable in a normal browser — it just cannot be read by a fetch. If Jess
opens the page herself she can read it off and we will add them to the pipeline.

## Found 23 Sep 2026 (London / South East sweep)

| Clinic | Why it qualifies | Why we can't email |
|---|---|---|
| EF MEDISPA | Three London sites (Kensington, Chelsea, St John's Wood), complimentary consultations, "EF Loyalty Points", own booking portal | No email published anywhere on the site. Phone 0207 361 1000 |
| CJA Aesthetics | Six sites (Southampton, Winchester, Portsmouth + 3), Semble booking, two membership tiers, Dr Chris Airey & Dr Lauren Airey | Cloudflare-obfuscated on every page. Phone 023 8033 2429 |
| Cosmedics Skin Clinics | Four sites including Harley Street and Putney | Cloudflare-obfuscated |
| The Cosmetic Skin Clinic | Harley Street + Stoke Poges | Cloudflare-obfuscated |
| Melior Clinics | Sevenoaks, Harley Street, Huntingdon; vouchers, £25 refer-a-friend, free consults, three named doctors | No published email, no identifiable booking platform |
| Centre for Surgery | Baker Street, Chrysalis 0% finance, CQC "Good" | No published email, no booking platform |
| Illuminate Skin Clinics | Dr Sophie Shotter, Kings Hill, Kent | Contact page returns 401 to a fetch |

**Cloudflare obfuscation is the single biggest blocker on this list.** Four of
the seven are otherwise strong. If Jess wants them, the fastest route is her
opening the contact page in her own browser and pasting the address back.

## Found 24 Sep 2026 (Australia sweep — Sydney, Melbourne, Brisbane, Gold Coast, Perth)

| Clinic | Why it qualifies | Why we can't email |
|---|---|---|
| **Contour Clinics** (Sydney + Brisbane) | The single largest prospect found anywhere: eight doctor-led clinics, ~50 practitioners including 20 cosmetic doctors, Zenoti, a Rewards program at every location, a $75 deposit on every booking, Afterpay/ZipPay/Elevant | Cloudflare-obfuscated. Form and phone only (1300 233 803) |
| Absolute Cosmetic (Perth) | 12 WA clinics, Nookal booking, gift vouchers, Dr Glenn Murray medical director — and they already advertise a 24/7 "AI receptionist", so they are pre-sold on the category | Cloudflare-obfuscated / form only |
| Artisan Aesthetic Clinics (NSW/ACT/QLD) | 11 clinics, gift cards, loyalty program, refer-a-friend | No plain-text email |
| Victorian Laser & Skin Clinic (Melbourne) | Five clinics, Kitomba booking, vouchers, Afterpay and Zip, free consultations | No plain-text email |
| LLC Cosmetic (QLD) | Four clinics, Timely booking, free consultation, "save up to 50% on eligible first-visit offers" | No plain-text email |
| Jade Cosmetic & Wellness (Brisbane + Cairns) | Two clinics, Dapple CRM, $100 consultation redeemable against any treatment, gift vouchers | No plain-text email |
| Southern Cosmetics (Melbourne) | Sandringham and Highett, Dapple CRM, "Southern Circle" loyalty program, gift cards | No plain-text email |

**Contour Clinics is worth a phone call on its own.** Eight clinics and fifty
practitioners on one Zenoti instance, with a deposit on every booking, is the
best-fit prospect in the entire pipeline — it just cannot be emailed.

## Ruled out in Australia, don't revisit

- **Franchise or corporate chains:** Cosmetique (23 clinics, head-office
  marketing), Australian Skin Clinics, SILK Laser
- **Same group as an existing pipeline row:** CDC Clinics Armadale (publishes
  info@csdclinics.com.au — the CSD Clinics group, already listed)
- **Single operators:** Dr Terrence Scamp, DC Aesthetics
- **No identifiable booking system:** Dr Tass Cosmetic & Skin Clinics (three
  Melbourne clinics and a Signature Club membership, but bookings are taken by
  phone), Cosmetic Connection (Toorak + St Leonards, gift cards on Square)
- **Failed on scale, CRM or email:** Enrich Clinic, ICCM, The Layt Clinic,
  Gold Coast Plastic Surgery, Skin Project Clinics, Studio Aesthetica, MA360,
  The Manor Clinic

## Ruled out in the UK, don't revisit

- **Single operators, no support staff:** Sussex Aesthetics (Crawley),
  Aesthetic Klinik (Brighton), Dr Liesel Holler (Bromley)
- **Beauty-led rather than medical:** No.6 Clinic (Tunbridge Wells)
- **Corporate chains — head office controls marketing:** sk:n, Thérapie,
  The Harley Medical Group, Air Aesthetics

## Found 24 Sep 2026 (UK regional sweep — Manchester, Birmingham, Leeds, Bristol, Glasgow, Edinburgh)

| Clinic | Why it qualifies | Why we can't email |
|---|---|---|
| **Quinn Clinics** (Bristol) | Eight-plus named staff including an oculoplastic surgeon, Zenoti, and four separate dormant pools — a named membership, a referral scheme, payment plans and gift vouchers | No email anywhere on the site. Phone 0117 924 4592, or the enquiry form |
| Elanic (Glasgow) | Eleven named surgeons across three Bath Street addresses, financing eligibility checker, gift cards, free consultations | No email on the homepage or either contact page; on-site form only |
| CLNQ / Reza Nassab (Manchester + Knutsford) | Two clinics, Chrysalis Finance, and a "CLNQ Privé" annual subscription membership | No email published and no booking system visible |

Quinn Clinics is the strongest of these — the membership, referral scheme,
payment plans and vouchers all point at exactly the list we want to work.

### A judgement call worth knowing about

**The Goddess Clinic (Edinburgh)** has the best dormant signal of anything found
in this sweep — a "Goddess Glow Club" tiered subscription at £75/£125/£170 a
month, gift cards, and free 45-minute consultations — plus a real booking system
and a published email. It was excluded only because a single practitioner (Nurse
Dawn, the founder) is named anywhere on the site, and our rule drops
single-operator clinics. If Jess wants to relax that rule, this one goes
straight in.

## Ruled out in the UK regions, don't revisit

- **Corporate and hospital chains:** Spire, Nuffield Health, sk:n, Thérapie,
  Transform, The Private Clinic, Signature Clinic, Nu Cosmetic, Este Medical Group
- **Single operators:** Essence Medical (Dr Kieren Bong, Glasgow), Craig Hobson
  Aesthetics (Bristol), Skin & Joints / Vee Spandoni (Bristol), Skins Clinic
  (Manchester)

## One caveat on every "no CRM" verdict in this file

Sourcing agents identify the booking system from where the "Book now" link
points, because raw page source is not readable from this environment. A clinic
recorded as having no identifiable system may still run one behind a contact
form — it just isn't linked publicly. That is why the four C-graded rows in the
pipeline (Manchester Private Hospital, UK Aesthetic, Victoria House Clinic,
Yorkshire Skin Centre) are worth emailing anyway: the first discovery question
answers it.

## Found 24 Sep 2026 (Ireland, New Zealand, regional Australia)

| Clinic | Why it qualifies | Why we can't email |
|---|---|---|
| **The Skin Care Clinic** (Hobart) | The best dormant signal found in Tasmania: a full points loyalty scheme — a point per dollar, £5 off per 100 points, 300 points for a referral and 300 for a testimonial — plus Timely, gift e-certificates, Afterpay and Zippay, six named staff including a doctor in cosmetic medicine since 2004 | No email on any reachable page, and no phone published either. Their `/contact/` page could not be fetched at all |
| River Medical (Dublin, Cork, Belfast) | Three clinics across two jurisdictions, Phorest on two instances, BAAPS/BAPRAS/RQIA accredited surgical practice | Cloudflare-obfuscated everywhere |
| Palm Clinic (Auckland) | Skin and vein clinic, Dr Sam Dunn, NZ Society of Cosmetic Medicine accredited, gift vouchers, Q Mastercard interest-free plans | Cloudflare-obfuscated |
| Vamp Cosmetic Clinic (Newcastle) | Zenoti, a named loyalty programme with its own terms page, gift cards, treatment packages, complimentary consultations, open six days | No email on the homepage or contact page — form only |
| Laser Skin & Vein Clinic (Adelaide) | Two clinics, treatment vouchers through their own shop, direct booking with no referral | Cloudflare-obfuscated |
| Ponsonby Cosmetic Medical Clinic (Auckland) | Medical-led appearance medicine, gift voucher collection, a dedicated treatment financing page | No email and no phone published |
| Accent on Skin (Wellington) | CANNZ-accredited, own booking portal | Cloudflare-obfuscated, and only two practitioners named so it would likely fail scale anyway |

**The Skin Care Clinic in Hobart and River Medical are the two worth Jess opening
herself.** The Hobart one converts straight to grade A if its contact page can be
read — that loyalty scheme, with points for referrals and testimonials, is exactly
the database the offer is built for.

## Ruled out in Ireland, NZ and regional Australia

- **Chains:** Skin Institute (NZ), The Cosmetic Clinic (NZ), Transform Clinic (NZ),
  My Cosmetic Clinic (Newcastle), Concept Cosmetic Medicine (Newcastle), and the
  SILK / Australian Skin Clinics / Cosmetique branches in these cities
- **Single operators:** Newcastle Cosmetic Doctor, Coastal Skin & Laser (Tewantin),
  Dr Sarah Sparks and Hobart Facial Aesthetics (Hobart), Sapphire Appearance
  Medicine (Auckland)
- **Wrong offer shape, not wrong size:** Fitzgerald Plastic Surgery (Dublin) has a
  published email but states "We do not offer payment plans", charges consultation
  fees in advance and non-redeemable, and runs no complimentary consults. There is
  no dormant pool to reactivate — the model is built to filter people out before
  they book. A useful reminder that scale alone does not make a prospect.

## Found 24 Sep 2026 (United States — South and West)

The US is the worst region yet for this. Roughly **two strong clinics were blocked
for every one that made the pipeline**, and about sixty in total. Listing the ones
worth the effort rather than all of them.

### Worth a browser visit or a phone call, best first

| Clinic | Where | Why it matters |
|---|---|---|
| **Aesthetic Center for Plastic Surgery** | Houston ×3 | 13 surgeons, three sites, memberships on RepeatMD at $149/$199/$299 a month, all six-month commitments |
| **Cienega Medical** | West Hollywood, Santa Monica, Calabasas | Three LA sites, ~12 clinicians including a board-certified dermatologist medical director |
| **La Jolla Cosmetic Surgery Centre** | La Jolla | Seven surgeons, free consults on all primary procedures, Model Rewards plus Allē, and four separate financing partners |
| **Westlake Dermatology** | 22 sites across Texas | The largest footprint found anywhere in any sweep |
| **North Texas Plastic Surgery** | DFW ×7 | Seven surgeons, seven locations, nine aesthetic providers |
| **Advanced Aesthetics** | Las Vegas ×3, Dallas, La Jolla | Five sites on PatientNow, $99/month membership on a six-month commitment |
| **La Jolla Cosmetic Medical Spa** | Five San Diego-area sites | Double board-certified facial plastic surgeon, GLAMfam VIP loyalty club |
| **AdmireMD Skin + Wellness** | Scottsdale ×2 | Zenoti, three memberships including a "Bank Your Beauty" credit-banking tier |
| **La Belle Vie Med Spa** | Tukwila, WA | Six practitioners including two MDs, Zenoti, three tiers at $99/$175/$275 |
| **Skintegrity MedSpa** | Kirkland, Bellevue, Redmond | Runs a monthly prize draw explicitly open to "current, past, or prospective clients" — they are already trying to do this by hand |
| **Spa Sydell** | Atlanta ×3 | Zenoti, eight membership tiers |
| **Truffles Aesthetics** | Atlanta metro ×5 | Boulevard, Diamond Club membership |
| **Fresh Start Aesthetics** | Scottsdale ×2 + Phoenix | Mindbody, four tiers from $149 to $399 a month on twelve-month commitments |

Another twenty or so are recorded in the sourcing reports but not worth listing
until the ones above are exhausted.

### Two findings that change how we should work this

**1. Surgical practices do not publish email addresses. Med spas do.** Every large
surgical group found across all six southern metros — ACPS, North Texas, Dallas
Plastic Surgery Institute, Miami Plastic Surgery, Basu, Memorial — routes
everything through a form. If the offer is meant to land on plastic surgeons
specifically, email-only outreach will keep hitting this wall, and phone or
LinkedIn needs a decision before the next US batch.

**2. Which CRM Griffin integrates with first is now an evidence-based choice.**
Across the US sweeps: **Zenoti** appeared most often overall, **Aesthetic Record**
appeared on the most dormant-lead-rich accounts (every AR clinic found ran a
membership or a banked-credit scheme), and **PatientNow / RepeatMD** covered the
larger surgical groups. In the UK and Australia the picture was completely
different — Pabau, Timely and Phorest. One integration will not cover both sides
of the Atlantic.

### Excluded, don't revisit

- **US chains and franchises:** Beverly Hills Rejuvenation Center, SkinSpirit,
  It's A Secret Med Spa, dermani MEDSPA, Elase, VIO, Skin Spa New York, Juvly,
  Skin Pharm, Smiley Aesthetics, Mia Aesthetics, Novuskin, OrangeTwist,
  Hand & Stone, milk + honey
- **Hospital and university systems:** Vanderbilt Health, UTHealth, Wellstar
- **Portrait Care** is a directory, not a clinic

### Judgement calls, same shape as The Goddess Clinic

**Skin 101 Houston** (OptiMantra, three membership categories, $350 and $179 paid
consults) and **The MedSpa of DFW** (Aesthetic Record, real membership) both have
published emails and real systems, and are excluded only by the single-site rule.
If Jess wants Houston volume, Skin 101 is the one to relax it for.

## Found 24 Sep 2026 (United States — Northeast)

### Worth a browser visit or a phone call, best first

| Clinic | Where | Why it matters |
|---|---|---|
| **Greenwich Medical Spa** | 8 sites across CT, NY and NJ | The single best prospect found in the entire Northeast. Zenoti *and* GoHighLevel, a $99/month VIP membership with loyalty points and anniversary credits, plus a $199/month HRT programme. One browser tab away from being emailable |
| **SkinMD** | 10 Massachusetts sites | The biggest Boston-area practice found. RepeatMD rewards, gift cards, CareCredit and Cherry |
| **East Coast Advanced Plastic Surgery** | NYC + 5 NJ sites | 10 surgeons and 8 PA-Cs across six locations — the largest practice in the region |
| **Ethos Aesthetics + Wellness** | 7 NJ sites | Owner-operated, not a chain. Two founders plus four NPs, and a VIP membership with bankable "Ethos Bucks" |
| **Trifecta Med Spa** | 4 NY sites | Allergan Top 100 Injector, Zenoti, 0% APR plans |
| **Metro Laser MedSpa** | 3 Philadelphia-area sites | Boulevard, memberships from $39 to $249 a month across two ladders |
| **Tribeca MedSpa / AYA Skin** | 2 NYC sites | Board-certified plastic surgeon, Zenoti, an "AYA Beauty Bank" loyalty scheme |
| **SkinHealth Centers**, **PURE Cosmetic**, **Demma Aesthetics**, **Clareo**, **Boston Medical Aesthetics** | Boston metro | All four have the profile and a real platform. None publishes an email |

**Boston is a hole in the map.** Every strong Boston clinic found publishes no
readable email, so the city contributed nothing to the pipeline. A focused
Massachusetts pass would likely clear SkinMD, Demma, SkinHealth Centers and PURE
Cosmetic — they need an address found, not qualifying.

### Two more things the Northeast pass established

**Boulevard is the dominant platform in the Northeast** — five of the fifteen
qualified rows run on it, with Zenoti on two more and Aesthetic Record on three.
Combined with the West Coast picture, that makes Boulevard and Zenoti the two
integrations that would unlock the most US ground.

**RepeatMD is worth watching.** It is a dormant-rewards database by design, and it
turned up on both a qualified row (Newtown MediSpa) and a near-miss (SkinMD). Any
clinic running it is, by definition, already tracking exactly the credit we would
be reactivating.

### Rejected on dormant signal rather than contactability

A useful category, because it is the one kind of clinic to stop researching:
**Plastic Surgery Group New Jersey** publishes a perfectly good address but runs no
membership, loyalty, gift-card or financing scheme at all. Boston Center for
Plastic Surgery, Longwood, NYBG Plastic Surgery and about a dozen other surgical
groups are the same. Scale without a scheme is not a prospect for this offer —
there is nothing dormant to reactivate.

### Three grade-C fallbacks with real published emails

If a batch ever needs topping up: **Aesthé By MD** (3 CT/NJ sites),
**Manhattan Medspa** (annual memberships at $1,999 and $2,299) and
**Skinly Aesthetics** (Skinly Club plus two lenders). All three fail only on
naming a booking platform, which the first discovery question answers.

---

## Midwest — Chicago, Milwaukee, Indianapolis, Detroit, Columbus, Cleveland (16 Oct 2026)

Fourteen rows went into the pipeline from this sweep. These cleared the ICP on profile
and failed only on contactability.

**Worth Jess opening in her own browser, best first:**

| Clinic | Where | Why it matters | Blocker |
|---|---|---|---|
| **Ageless Indy** | Indianapolis NW, Greenwood, Fishers IN | The best dormant structure in the whole sweep. Zenoti, three sites, founder Shelley Clayton FNP-BC. "Forever Flawless" at $149/mo is a prepaid credit account — credits do not expire while active, and after cancellation remaining credit stays usable for 90 days. Plus Platinum $249, Gold $149, Zenoti gift cards, financing | No email and no phone anywhere on the site; /contact/ errors |
| **Illume Cosmetic Surgery & MedSpa** | 6 Wisconsin sites | The largest practice in any of the six metros — six locations, nine named surgeons. Allē and Aspire rewards, patient financing, MedSpa seasonal specials | No email; /contact/ errors. Phone (414) 439-3000 |
| **SHarper Surgery & Med Spa** | Indianapolis, Fishers, Avon IN + a surgical centre | Dr Stanley Harper and Dr Jaime Harper. "SHarper Skin Society" $225/mo with $100 toward tox after four months of active membership — banked credit with a clock on it | Cloudflare-obfuscated on every page |
| **Quintessa Aesthetic Center** | 5 Wisconsin sites | Three named doctors, per-location phone lines, a gift-card shop | No email anywhere on the site |
| **SkinergyMD** | Birmingham, Troy, Grosse Pointe MI | Exactly the three target Detroit suburbs. RepeatMD rewards, Prospyr gift cards, CareCredit *and* Cherry, a $200-off first-visit offer | Cloudflare-obfuscated |
| **Ashpole Plastic Surgery** | Itasca, IL | $150/mo buys $175 of MedSpa credit and the credit rolls over for up to three months on a six-month minimum — textbook expiring banked credit | Cloudflare-obfuscated |
| **Modern Aesthetics of Michigan** | metro Detroit | Vagaro confirmed. A "Membership Savings Bank" at $99/mo where "all of your monthly payments are banked for you to use on your treatments" | No email, no phone and no address published at all |
| **Wellness Center Cleveland** | North Olmsted, OH | Silver/Gold/Platinum $99/$149/$199 on a six-month minimum, and "any accrual funds must be used within 12 months, otherwise will expire" — expiring banked credit stated outright | No email. Single site, so scale is thin too |
| **Radiant Divine Medical Spa** | Avon, Brecksville, Medina OH | Three locations with their own lines, RepeatMD, Giftfly gift cards, financing | No email |
| **Radiant Skin Indy** | Zionsville + Danville IN | PatientNow confirmed, six named staff under owner Kayla Trammel BSN RN, a membership, Square gift cards, Cherry | No email |
| **Grace + Beauty Medical Spa** | Westlake, OH | Five named staff, a documented membership with member injectable pricing and a birthday treatment, package discounts, gift cards, financing | No email; booking is an on-page popup |
| **KÜR Modern Medical Aesthetics** | Cleveland, OH | KÜR Rewards on RepeatMD, Square Appointments, Square gift cards, Cherry 0% | No email — social only |
| **SKN BAR Rx** | Milwaukee / Shorewood / Pewaukee WI | Zenoti confirmed, "Elevated Monthly Memberships", Zenoti gift cards, four named providers | No email; /contact/ errors |
| **Wise Aesthetics** | Carmel, IN | Aesthetic Care Plans, a W/A Rewards programme, gift cards, Cherry split payments, and a $50 account credit to both sides of every referral | No email |

**Ruled out, don't revisit.** Rejected on dormant signal despite real scale: Giancarlo
Zuliani MD (Bloomfield Hills), Illuum Cosmetic Surgery (Novi), Ponsky Facial Plastic
Surgery (Beachwood, Symplast), Donaldson Plastic Surgery (Columbus, three surgeons),
**Moxie Medispa** (Menomonee Falls — publishes a perfectly good address and books on Jane,
but runs no scheme at all), Between the Lines Aesthetics (Birmingham MI), Spa 43 (three
Michigan sites, four DOs and eleven estheticians, but no scheme and a shared
`dermsites4.com` booking instance under a "DOCS" group, i.e. a roll-up). Also out:
Skin House (Birmingham MI) and Cleveland Plastic Surgery Institute, both of which fail
the dormant test as well as the email test.

Chains and networks out: **Medspa of Cleveland** and **Medspa of Indianapolis** are
white-labelled sites on the MedspaCircle network (Cleveland's "Book Now" resolves to
`go.medspacircle.com/clinics/medspa-of-newyork/`) with a $19.95/month network
membership — not independent clinics. Cleveland Clinic and OSU Wexner are hospital systems.

Single operators out: Glo Aesthetics (Carmel IN — has a "Glo Bank" holding gift-card
value all year, but one operator), Reflection Theory, Revive Medical Aesthetics,
Cool Blue Image, East Town Salon & MedSpa, Mind & Body Aesthetic Center, Renova Aesthetics.

**What this region taught us.** The Midwest publishes emails far more readily than the
Northeast or the South — fourteen of roughly forty serious candidates, against about one
in three elsewhere. The reliable move was fetching `/contact/` directly rather than the
homepage: RELUXE, BB Aesthetic, PURE, Boss Gal and Jiva all showed nothing on the
homepage and a plain address on `/contact/`. **Make that the default second call.**
Milwaukee and Detroit are the holes, for opposite reasons: Milwaukee's scale sits in two
practices that publish nothing, so a phone call would unlock it; Detroit's two practices
with real size run no scheme at all, so nothing would.

## Mid-Atlantic — DC, Northern Virginia, Maryland, Richmond (16 Oct 2026)

Eighteen rows went into the pipeline. Of the near-misses, these are the ones worth a
browser tab — several are better prospects than rows that did qualify:

| Clinic | Where | Why it matters | Blocker |
|---|---|---|---|
| **Life Med Institute** | 6 sites across MD, DE and PA | The largest footprint in the sweep. AestheticsPro confirmed, a free rewards programme, gift cards, financing | No email on the homepage; the contact page was never reached before the budget ran out — **re-check this one first** |
| **The District Injector** | McLean, VA | Symplast confirmed, and a membership that banks units: $139/mo = 10 banked units, $249/mo = 20. Banked units are the ideal dormant asset | No email anywhere, no mailto |
| **Javan Wellness** | Dupont Circle, U Street DC + Ballston | Three sites and eleven named clinical staff — the biggest independent in DC | No email, and every Book button is an on-page anchor so even the platform is hidden |
| **Vitalify MedSpa** | Dupont Circle, DC | Zenoti *and* Practice Better, a "Vitalify Vault" loyalty programme, a botox membership, a $100 refer-a-friend credit | Cloudflare-obfuscated — one browser tab from qualifying |
| **Purity Spa Med** | Arlington, VA | Meevo confirmed, Silver $110 and Gold $200 memberships, a points loyalty programme, an eGift portal, treat-now-pay-later | Cloudflare-obfuscated |
| **Aesthetic Artistry Laser Centers** | North Bethesda, Annapolis + Arlington | Three locations, Zenoti confirmed, an "AALC Membership Club" with priority booking across all three | No email on the homepage, contact page or HIPAA notice |
| **Georgetown Allure** | Washington DC | Zenoti confirmed, memberships at $150/$280/$400, gift cards, financing, a corporate wellness programme | No email (their reviews link also points at `localhost` — the site is half-built) |
| **Elegance Aesthetics** | Roland Park, Baltimore | Mangomint confirmed, Mangomint gift cards, Cherry *and* CareCredit on practice links | Cloudflare-obfuscated |
| **Butterfly Medical Spa** | Rockville, MD | Zenoti confirmed, online gift cards | Cloudflare-obfuscated on every page |
| **Synergy Face + Body** | Richmond + Midlothian VA | A "FAB Beauty Vault" membership under a named plastic surgeon, multi-site. On profile the strongest Richmond prospect found | Pages returned a fetch error three times — likely bot-blocking, so this needs a browser |
| **Belcara Health** | Baltimore | Plastic surgery, dermatology and wellness in one, a "BH Blue" loyalty programme, an Allē programme, a community loyalty scheme | No email on any page reached |
| **Somenek + Pittman MD** | West End DC + NYC | Two board-certified plastic surgeons plus a PA-C, an "S+P MedSpa Club" at $250/$350/$450, Square e-gift cards, NextPatient booking | No email on the homepage, contact page or privacy policy |
| **NoBe Aesthetics** | North Bethesda, MD | Jane App, a $185/mo Tox Membership, two named NPs | No email |
| **Posh Med Spa & Wellness** | Old Town Alexandria | AestheticsPro confirmed, CoolSculpting and filler packages | No email, nobody named |
| **Maple & Magnolia Aesthetics** | Richmond, VA | **Publishes an address** and has three named practitioners, a membership section and payment plans — only the CRM is unresolved. One fetch from qualifying | Budget ran out mid-verification |

**Two judgement calls in the same shape as the others.** **Artifex Aesthetics**
(Alexandria) publishes an address and has the best banked-credit term found anywhere:
"The Study" at $125/mo gives $125/mo in treatment credits with a **12-month rollover**.
Excluded only because one person is named on the site. **The Aesthetic Era** (Richmond)
publishes an address, runs on Prospyr and has both memberships and gift cards; again one
named practitioner.

**Ruled out, don't revisit.** Real scale or a published email but nothing dormant:
**FMW Med Spa** (Towson — publishes an address, board-certified NPs, no scheme at all),
**DWH Med Spa** (Richmond — publishes an address and runs AestheticsPro, but no scheme),
Metropolitan ENT medical aesthetics, WeDo Aesthetics. Chains and institutions out:
**Medspa of Baltimore** (another MedspaCircle white-label, its location field a literal
`xxxx` placeholder), OVME, SkinSpirit Annapolis, Evexia, dermani, Massage Envy,
Anne Arundel Dermatology (PE-backed), University of Maryland Facial Plastic Surgery.
**Modern Med VA** redirects to another company — an ICP disqualifier. Single operators out:
Muse Medical Spa, Clear Aesthetics & Wellness.

**What this region taught us.** Aesthetic Record dominates the mid-Atlantic and dominates
the dormant-credit end of it: seven of the eighteen qualified rows run on it, and six of
those seven run a membership or a banked-credit wallet. And **"wallet", "bank" and "vault"
are the words to search for** — eight of these clinics name their membership credit
explicitly, and searching those three words plus a metro name was far more productive
than searching "med spa" plus a city. Every clinic found that way had a dollar balance
attached to named patients.

## Florida outside South Florida (16 Oct 2026)

Twenty-one rows went into the pipeline. The near-misses here are unusually strong:

| Clinic | Where | Why it matters | Blocker |
|---|---|---|---|
| **Beverly Hills Wellness Center & Med Spa** | West Palm Beach | **The single best phone-call target in Florida.** Aesthetic Record confirmed, memberships at $99 Beauty Bank / $199 Starlet Glow / $399 Couture Rejuvenation, and unused Beauty Bank funds sit in a "Wellness Wallet" that **expires on cancellation**. Dr Dahabra named | Publishes no email anywhere — there is no contact page at all, only phone and address |
| **Sarasota Premier Aesthetics** | Lakewood Ranch + Sarasota | Zenoti confirmed. "VIP Beauty Bank" at $145/$295 where "every dollar you contribute monthly is banked in your account" | Cloudflare-obfuscated — one browser tab from qualifying |
| **Skin Lab Winter Park Village** | Winter Park | Dr Jeffrey Hartog DMD MD overseeing two APRNs, Boulevard, and four dormant pools: a Rewards programme, a BeautyBANK, gift cards and payment plans | No email — footer has a signup field only |
| **Sweet Spot MediSpa** | Fort Myers + Punta Gorda | PatientNow, a Boulevard client portal **and** a GoHighLevel form. Gold $99 / Platinum $199 with a "Stash or Cash" option — "stash your fee and use it towards future services" | No email on the homepage, memberships page or contact page |
| **Elite Medical Spa of Lakewood Ranch** | Bradenton | Four named providers including a board-certified plastic surgeon medical director, Boulevard. "Elite Beauty Bank" $149/mo on a 12-month term, and on cancellation unused services, balance and credits are **forfeited after 12 months** | No email |
| **Modern Aesthetic Centers (MAC Florida)** | 3 Jacksonville-area sites | Twenty-six named staff — including a **"Lead Conversion Specialist"**, so they already employ someone to work the lead list. Zenoti, a membership section. The strongest Jacksonville profile found | No email on the about page |
| **Azul Cosmetic Surgery & Medical Spa** | 6 southwest Florida sites + 2 surgery centres | Four named surgeons. The largest footprint found in Florida. A membership programme and CareCredit | No email on the offices or contact page — form only |
| **Polished Beauty MedSpa** | Winter Park | Moxie. "Beauty Bank" $150/mo and "Polished Elite" $250/mo, monthly contribution fully banked, $1,800–$3,000 banked annually on a 12-month commitment, expiry terms given only at enrolment | Cloudflare-obfuscated |
| **The Garden Medical Spa** | 4 sites, Pinellas to North Palm Beach | Plastic-surgeon medical director, VIP Memberships, gift cards, Cherry | Cloudflare-obfuscated, and no platform named either |
| **Bijoux Med Spa** | Orlando | Podium. "Each month, your membership payment goes into your BIJOUX BANK" — $149/$199/$249 on a 12-month commitment. Kyla Hargraves PA-C | No email |
| **Perizia Aesthetics** | Jupiter | Dr Fred Silvestri plus two APRNs, AestheticsPro, and Cherry, CareCredit **and** Alphaeon | Cloudflare-obfuscated |
| **Ponte Vedra Plastic Surgery** | 5 north Florida sites | Six doctors, eight APPs and six skin-health specialists — the largest practice in north Florida | No email, and no scheme either, so it fails the dormant test too |
| **Bowtique Med Spa** | Sarasota + Lakewood Ranch | Seven named providers including two MD medical directors, Zenoti | No email; payment plans only, no membership |
| **Inside Out Med Spa** | 2 Naples sites | Mangomint, memberships at $59/$99/$149 | No email — contact is a JotForm |
| **Nouveau Health & Wellness** | Palm Beach Gardens | Zenoti, three named providers, an "Exclusive Membership Program" | No email |
| **Von & Co Aesthetics** | Naples | White-labelled Zenoti, "The Club" member pricing, a $100 referral credit, Affirm, a 15%-off first-visit funnel | No email |
| **BlueWater Wellness & Med Spa** | Ponte Vedra | Podium, six providers including three NPs, a $35/mo membership with a free first month, CareCredit | No email |
| **Jewell Medical Spa** | Naples | **Publishes an address**, runs Aesthetic Record, has a membership ladder from $99/mo and CareCredit. Excluded only because the site describes the owner as "sole proprietor" — relax that rule and it goes straight in | Single-operator rule |

**Ruled out, don't revisit.** Chains and franchises: **Look Lab** (eight sites across four
states with a corporate office and an 833 number — the best membership on paper, with
credit that "rolls over and never expires", but head office runs it), **Couture Med Spa**
(seven sites, multi-state), **Facial Mania Med Spa** (a franchising LLC with a
franchise-opportunities arm), **CARE Esthetics Jupiter** (100+ locations),
**Windermere Medical Spa** (has joined AYA Skin, a multi-state network, and all booking
now resolves there). Real scale but nothing dormant: **Hass Plastic Surgery** (the only
"loyalty" named is Allē and Aspire, which belong to Allergan and Galderma, not the
practice — so there is no list of theirs to work), **Truglo**, **Kent V. Hasen MD**,
**Arsenault Aesthetics**, **Plastic Surgery of Palm Beach / MedSpaZen** (an unusually rich
scheme, but the only address on the page belongs to their web agency),
Southwest Florida Med Spa. Wrong vertical: **The Spa Orlando** has the cleanest dormant
signal seen anywhere ("your service rolls over automatically and never expires") and
publishes an address, but it is a day spa with no injectables.

**What this region taught us.** "Beauty Bank" is a product category, not a brand — nine
separate Florida clinics use that exact phrase or near-identical wording, and several
state in writing that the balance expires or is forfeited on cancellation. That is the
sharpest version of this offer's premise found anywhere in the pipeline, and a
Florida-specific opening line could be built on the phrase itself. Zenoti and Boulevard
together cover sixteen of around forty identifiable platforms here, and three clinics run
**GoHighLevel forms alongside** their booking platform — the easiest integration Griffin has.

## Massachusetts and New England (16 Oct 2026)

Fourteen rows went into the pipeline. **The five named Boston clinics are now resolved**
and three of them can be struck off permanently:

- **SkinMD** — confirmed publishes no email anywhere. Nine pages checked including two
  separate privacy pages, the terms, careers and the Shopify store. Phone only:
  (844) 754-6631 for all ten sites. It also exposes no booking platform, so it would have
  graded C regardless. Rewards run on RepeatMD. **Stop researching.**
- **Demma Aesthetics** — dead name. The domain now 302-redirects to RN Esthetics, so it is
  disqualified under the redirect rule. **Drop permanently.** But the successor is the
  strongest near-miss in New England (below).
- **SkinHealth Centers** — qualified, now row 243. The address was on the employment page.
- **PURE Cosmetic Center** — Cloudflare-obfuscated on the membership terms page, so not
  seen. Worth a browser tab: Nextech confirmed, and the VIPure membership runs Bronze $49
  / Silver $199 / Gold $399 on a 12-month commitment with a 3-month cancellation penalty,
  where the Bronze **$150 quarterly credit expires each quarter and cannot accrue** while
  reward points never expire.
- **Boston Medical Aesthetics** — confirmed publishes no email anywhere; the full sitemap
  was checked. Vagaro confirmed, three stacked manufacturer schemes (Allē, ASPIRE,
  Xperience+), and a $50 charge for a missed consultation, which implies a consultation
  pipeline worth reactivating. Phone (617) 973-9700. **Stop researching.**

Other near-misses worth a browser tab:

| Clinic | Where | Why it matters | Blocker |
|---|---|---|---|
| **RN Esthetics** (successor to Demma) | Boston/Brighton, Salem, Lynnfield, Newburyport MA | **The best dormant signal in New England.** They sell prepaid annual cards — Navy $2,295, Teal $1,895, Black $550, Teen Teal $500 — all on 365-day terms, plus a $550 hydration membership. **26+ named providers** including eight nurse practitioners, four sites | No third-party platform exposed and no email on locations, team, terms or privacy |
| **Bella Santé** | Boston Newbury St, Lexington, Wellesley | Three locations on one call centre. Meevo confirmed. **"Bella Points"** — up to 500 points redeemable per visit for $25, **expiring six months after they are earned**, redeemable at all three sites. A loyalty ledger on a six-month clock | No email on contact, loyalty or careers pages |
| **AW Plastic Surgery** | Portsmouth, NH | PatientNow confirmed. Two memberships — AW VIP $175/mo and AW VIP Wellness $350/mo, the latter mandating in-office labs and three follow-ups a year. Shopify gift cards, financing. Membership enrolment is by phone | No email |
| **MD Esthetics** | Harwich MA, Windham NH HQ, 3 Virginia sites | Zenoti **and AesthetixCRM, a GoHighLevel white-label — so Griffin's GHL work transfers directly.** Four membership tiers $109–$379/mo with credits redeemable only at the purchasing location, gift cards, financing, a $100/$100 refer-a-friend | No email. Flag: multi-state with a separate HQ — check it isn't becoming a franchise |
| **Cape Cod Surgical Arts & MediSpa** | Falmouth, MA | Double board-certified surgeon plus two RNs, Square booking and gift cards. **Nearly emailable** — the visible text is Cloudflare-obfuscated | One browser tab converts this to a grade-B prospect |
| **Dr Frank Fechner / Facial Plastic Surgery** | Worcester + Concord, MA | Two MDs, two locations, CareCredit, and a "Beauty Bucks" promotional week | No email. Flag: the careers link suggests an APDerm affiliation — verify it isn't head-office-controlled |
| **Seacoast Rejuvenation Center** | Newington, NH | Four separate dormant pools: a three-tier membership each including a birthday gift card of $50/$75/$100, a standalone rewards page, gift certificates and financing | No email. Single site |
| **Modern Med Spa NH** | Hooksett + Plymouth, NH | Jane App confirmed, two locations, memberships, packages, payment plans, Jane gift cards | Cloudflare-obfuscated |
| **BIO Medspa** | Providence RI + Fall River MA | Two locations in two states on one Boulevard instance, gift cards, special financing | No email, and nobody named |
| **Thrive Med Spa** | Portsmouth, NH | Two named naturopathic doctors, a membership page, Boulevard gift cards | No email. Segment flag: naturopathic-led rather than medical-aesthetic |
| **Penobscot Medical Aesthetics** | Hampden (Bangor), ME | Three named staff, a membership page, Square gift cards, AdvanceCare financing with 6–14 month interest-free periods | No email, no platform |

**Ruled out, don't revisit.** Rejected on dormant signal: Sean Doherty MD, Boston Plastic
Surgery Specialists, Longwood Plastic Surgery (confirming the earlier verdict),
**Pretti Aesthetic** (Cape Cod — publishes a good address but runs no scheme at all,
the Fitzgerald lesson again), Newton Beauty, Level Up Med Spa. Single operators:
Bel Viso Medical Spa, **Sorgente MedSpa** (gift certificates that expire in three months
is a decent signal, but the med spa is a side-line of an OB/GYN practice — wrong segment).
Chains: VIO Med Spa, Hand & Stone. **LuxDerm Med Spa** disallows fetching in robots.txt
and was never assessed.

**What this region taught us.** Zenoti was on eight of the twenty-four practices profiled,
far ahead of everything else — **for Massachusetts and northern New England, Zenoti is the
single integration that unlocks the most ground**, which agrees with the West Coast finding
and cuts against Boulevard being the Northeast default. And the biggest blocker here is not
Cloudflare (only three clinics) but practices that **publish no address at all** (eleven of
twenty-four). The two addresses found in unexpected places came off a **careers page** and a
**privacy-policy block on an about page** — both pages a normal contact-page sweep skips.
Make those two page types standard checks.

## The constraint that capped all four sweeps

All four agents hit the same wall and reported it independently: **WebSearch (200 calls) and
WebFetch (400/hour) are shared across the whole turn, not per agent.** Running eight sourcing
agents at once starves all eight — each of these four stopped two to sixteen rows short of
its target with candidates already queued and unverified. **Run three or four at a time, in
sequence, not eight in parallel.** Each report ends with a named queue of already-surfaced,
immediately-fetchable URLs, so a follow-up run costs no search budget to restart.

## Northern California and Oregon (16 Oct 2026)

Thirteen rows went into the pipeline. **One finding changes how this region gets worked:
not a single Cloudflare-obfuscated address in the entire sweep.** Every near-miss below is
form-only — the address is not on the site at all, so opening these in a browser will not
reveal one. These need a phone call or LinkedIn, which is a different conclusion from the
UK and Australia sweeps.

| Clinic | Where | Why it matters | Blocker |
|---|---|---|---|
| **Destination Aesthetics** | El Dorado Hills, Elk Grove, Folsom, Napa, Roseville, Sacramento (6 sites) | **The biggest prospect in this sweep.** 35 team members including a 20-strong injector team (16 RNs, 3 NPs, a PA-C), a named MD medical director, Zenoti with per-location service paths, and a **"DA Beauty Bank" VIP membership**. They also rent out beauty suites | No address on contact, per-location contact or team pages; the Beauty Bank page is robots-disallowed |
| **Berman Skin Institute** | 10 sites across the Bay Area and Sacramento Valley | The largest footprint in NorCal. **RepeatMD** for gift cards, a HubSpot form, a Nextech patient portal, NextPatient provider booking, CareCredit and Allē payment plans, monthly specials, an online store. They are already pre-sold on the category | No address on the Walnut Creek or appointment pages |
| **Skin by Lovely** | Portland, Lake Oswego, Bend, Camas WA, Santa Monica (5 sites) | **22 named practitioners** — 14 injection specialists plus 5 estheticians and a training manager. White-labelled Zenoti. Memberships, refer-a-friend, financing. A Portland Thorns sponsor and a Business Journal fastest-growing company | No address on the contact page or homepage |
| **Hayes Valley Medical & Esthetics** | SF Gough St, SF Cow Hollow, Larkspur (3 sites) | **The only Marin presence found anywhere.** 15 named staff including an MD medical director and a Director of Nursing, an enormous device menu, and **four separate dormant pools** — rewards, referrals, a VIP specials signup and gift cards | No address on either page checked |
| **Illuminate Plastic Surgery** | San Jose ×2, Palo Alto, Morgan Hill (4 sites) | 3 plastic surgeons plus 12 named med-spa providers including two Master Injectors and a Nurse Educator — 15 clinicians, the largest count in the South Bay. PatientNow. $75 consultation fees, so consults are a paid, tracked product | No address on schedule or contact pages |
| **Fresh Faces Rx** | Portland + Lake Oswego | 15 named staff including three doctors and three RN injectors. Mindbody. A **"FFRX Skin Club" with a $99 enrolment fee** and tiered benefits plus bonus treatments | No address on homepage or new-patient page |
| **Thrive Aesthetic & Wellness** | Tigard / Portland | **The best dormant stack in Oregon — six schemes:** VIP memberships, HRT memberships, an app-based rewards programme advertising a $50 reward for downloading the app, gift cards, payment plans and bridal packages. PatientNow | No address on homepage or appointment-request page |
| **Refine Anti-Aging Medicine and Aesthetics** | Oakland | Prospyr Med CRM. Memberships, packages, gift cards, Cherry financing — and a **"Specials Redeem" page, which is a literal unredeemed-credit ledger** | No address on homepage or contact page |
| **Nubo Spa** | Berkeley | 10 named staff including a board-certified plastic surgeon owner and a founder-CEO. Boulevard. A membership, gift cards, financing, and a **free consultation with a hard deadline** — a dated lead magnet | No address on the homepage |

**Best three to phone:** Destination Aesthetics (6 sites, 35 staff, Zenoti, a named Beauty
Bank), Berman Skin Institute (10 sites, already running RepeatMD *and* HubSpot) and
Hayes Valley (3 sites, 15 staff, four dormant schemes, the only Marin foothold).

**Ruled out, don't revisit.** Chains: NakedMD (40+ locations), LaserAway, Restore Hyper
Wellness (269 locations), SkinSpirit, Ideal Image. Health systems: Sutter, Kaiser, El Camino,
The Oregon Clinic, UCSF. Scale but no dormant scheme: **Angell Medical Spa** (Sacramento —
publishes two perfectly good addresses and runs Boulevard, but has no membership, loyalty,
gift cards or financing, and new clients go through a *Google Form*), Movassaghi Plastic
Surgery, Centre for Plastic Surgery, Roseville Facial Plastic Surgery, Bohley, Hetal
Fichadia, Reza Najafian, Dr Lee Daniel. **That last cluster confirms the earlier finding:
Oregon plastic surgeons are a dead end for this offer.** Single operators: Osho Aesthetics,
La Vie MD, True You, Seven:Thirty. Wrong segment: the entire Santa Rosa and Sonoma listing
is day spas, so the North Bay produced nothing; San Jose single-provider medical
dermatology; Sacramento weight and metabolic clinics.

**One lead left unverified, worth a single search next run:** **Korman Plastic Surgery &
Wunderbar MedSpa** — four sites (San Jose, Mountain View, Los Altos, Carmel-by-the-Sea) on
PatientNow, with a directory-listed address that was never confirmed on their own page.

**Technique worth keeping.** `WebSearch` with `allowed_domains: ["<clinic-domain>"]` and a
generic query like "contact us email locations membership" reliably surfaces a clinic's own
contact, team and membership URLs, which can then be fetched. Plain brand searches return
almost nothing but directory spam. `threebestrated.com/med-spa-in-<city>-<state>` is the
most efficient single source found — one fetch returns three clinics with website, email,
phone, locations, practitioners, memberships and pricing — but it only exists for the larger
metros, and the address must still be confirmed on the clinic's own page afterwards.
`withorbital.com/data/med-spa/<city>/largest/` gives a ranked multi-location list per metro
and is how four of the best near-misses above were found, though it gives no websites.

**Platform picture.** NorCal and Oregon are **Boulevard-dominant** — Boulevard on five of
the ten qualified rows, Zenoti on four, and **PatientNow on every large multi-site group**.
Boulevard plus PatientNow would unlock this region. And **VIDA Aesthetic Medicine is already
on GoHighLevel**, the platform WILBA already runs — worth checking whether more Oregon
clinics are, because if so Oregon is the cheapest market in the pipeline.

## The Carolinas and east Tennessee (16 Oct 2026)

Ten rows went into the pipeline, covering **Charleston, Raleigh-Durham, Charlotte and
Greensboro only**. Five target metros got no coverage at all because the search budget died
before a single clinic domain could be surfaced for them: **Wilmington NC, Greenville SC,
Columbia SC, Knoxville TN and Chattanooga TN.** Again, no Cloudflare obfuscation anywhere —
every blocked clinic here is form-only, so a browser visit will not help.

| Clinic | Where | Why it matters | Blocker |
|---|---|---|---|
| **BodyLase Med Spa** | Raleigh, Cary, Chapel Hill/Durham, Clayton NC | **The single strongest Carolinas prospect found.** Four locations, Meevo booking with Liine lead capture, and **four separate dormant pools** — a VIP membership, BodyLase Rewards, Allē Rewards, gift cards and financing. Inc. 5000 listed, a top-50 Allergan provider | No address on the homepage or the book-consultation page, which doubles as the contact page |
| **Charleston Medical Spa** | James Island, Charleston SC | Prospyr Med booking, a **"Beauty Bank Membership"** with monthly savings on treatments, services and products, plus a GLP-1 membership, gift cards and payment plans. The best dormant framing in the Carolinas | No address on homepage or contact page |
| **Cool Renewal Spa** | Charlotte + Mooresville NC | Two locations, PatientNow, and memberships, gift cards, payment plans and CareCredit each on its own page, behind a CoolSculpting and CO2 high-ticket menu | No address on homepage or contact page |
| **Infinity Med Spa & Wellness** | SouthPark, Charlotte NC | Zenoti, a VIP membership with two named tiers, Allē payment plans plus PatientFi plus CareCredit, six-plus named staff | No address on homepage or contact page |
| **Blossum Aesthetics** | Raleigh NC | Aesthetic Record, **Luxe members $150/mo or $1,500/yr and Elite $250/mo or $2,500/yr**, gift cards, and 0% financing with approvals up to $50,000 and no hard credit check | No address and **no contact page at all** — a phone link is the only route |
| **Glow Aesthetics NC** | Greensboro NC | Aesthetic Record, a memberships page and a payment-plans page | Their main contact page was never reachable — **this one may well convert on a single fetch next run** |
| **M.D. Laser Studio** | Mooresville, Cornelius, Huntersville NC | Three locations, MDware booking, 450+ reviews | No address — Google Forms and phone links only, and nobody named |

**Ruled out, don't revisit.** Scale without a dormant scheme: **Piedmont Plastic Surgery &
Dermatology** (10 NC sites, 25 MDs — the biggest practice in the Carolinas and exactly the
wrong offer shape), **Beck Aesthetic Surgery** (and note `surface-medspa.com` redirects to
their domain, itself a disqualifier), **The MedSpa Raleigh** (publishes an address but
booking is a homepage anchor, so grade C, with payment plans as the only scheme).
Single-site or single-operator, several with perfectly good published addresses — they fail
on size, so do not re-source them: 704 Aesthetics, Aesthetica Med Spa, Charlotte Medical
Aesthetics, Mirama, The Skin Atelier, Prestige Medical Spa, NuDerma Health, Ella Ora,
Ageless Remedies, Voci MedSpa, Evolve Medical Associates, Femme Medspa (*"this is a TEXTING
line only"*), Cameo Facial Aesthetics, Med Spa CLT, Infinite Allure, Nu Body Solutions,
Radiant Medical Aesthetics. Chains: Elase, VIO, SkinSpirit, Skin Pharm, **Smiley Aesthetics**
(14 Knoxville-area sites), Ideal Image, **Genesis Lifestyle Medicine** (22 TN sites),
Allure Medical, **Skin Clique** (15 SC sites, a nurse-network model), The Aesthetics Lounge
& Spa (self-describes as a chain).

**Named leads for the five uncovered metros** — directory-level only, nothing verified, no
addresses, no CRMs, and none of them elsewhere in this file or the pipeline. This is the
shortest path for whoever picks the region up next:

- **East Tennessee, highest priority and genuinely promising:** Southern Surgical Arts,
  Chattanooga (16 locations, 1,808 reviews — the largest east-TN operator in the data);
  Meridiem Dermspa, Knoxville (10); Gallaher Plastic Surgery & Spa MD, Knoxville (9);
  Plastic Surgery Group, Chattanooga (9).
- **South Carolina:** The Essential Face, Columbia (4); JAG Medical Spa, Summerville (4);
  Germain Dermatology, Summerville (13 — check whether it is a chain); Body By Design
  Charleston (3); Solcara Health, Mt Pleasant (3); Back To 30, Greenville; Lux, Bluffton.
- **North Carolina, surfaced but never reached:** Revive Aesthetics and Wellness, Monroe (6);
  Luminous Medical Aesthetics, Stanley (4); White Diamond Medical Clinic & Spa, Charlotte (3);
  New Life Aesthetics, Raleigh (4); La Miel Aesthetics, Raleigh (3); Synergy Face + Body,
  Charlotte and Raleigh; Urban Medspa, Hydrate Medical, Carolina Facial Plastic.
  **Wilmington produced nothing at all — not one name.**

**Platform picture.** Aesthetic Record dominates the Carolinas: five of the ten qualified
rows run it, and it appears on half the ruled-out list too, with PatientNow on three and
Boulevard on two. That is a sharper signal than the Northeast's Boulevard lead — **if
Griffin builds one US integration, Aesthetic Record unlocks the most Carolinas ground.**

## The US Mountain West (16 Oct 2026)

Twenty-two rows went into the pipeline: Denver and Boulder carried the batch with nine,
and **Reno, Boise and Santa Fe each produced exactly one qualified clinic** — genuinely
thin, not under-researched. In each of those three the strongest local prospect was
unreachable, which is why they are thin.

**The two Jess can convert herself — Cloudflare-hidden, so the address is on the page in a
real browser:**

| Clinic | Where | Why it matters |
|---|---|---|
| **Om Wellness and Aesthetics** | Boise, ID | The best Boise prospect found. Zenoti, and a membership where **"100% of your monthly membership payments goes toward future treatments"**, with members-only VIP sales and events and Zenoti gift cards. One browser tab from qualifying |
| **Royal Medical Health** | Albuquerque, NM | A named medical team, memberships, a concierge-medicine fee model, three live monthly specials, and a newsletter lead magnet offering **15% off a next visit** |

**Qualify on profile but publish no address at all — a browser will not help these,
strongest first:**

1. **RESTOR Medical Spa** — Denver ×4 plus Boulder, with two more opening (6 addresses).
   Dr Flora Waples. **"TrueYou" membership described as "a beauty savings account"** with
   monthly instalments, plus RESTOR Rewards and Founding Memberships. Two live lead
   magnets: a **"CLAIM MY $75"** new-guest popup that expires a week after signup, and a
   "join the insider list" waitlist for the two unopened locations. Scheduling on Decoda
   Health. **The single best prospect in Colorado — it needs an address found, not
   qualifying.**
2. **Utah Facial Plastics** — Draper, Layton, Heber City plus a Park City med spa.
   Double board-certified facial plastic surgeon, VIP memberships, a rewards programme and
   refer-a-friend. **Runs GoHighLevel** — Jess and Griffin's own stack, so integration
   would be near-zero friction. **The highest-value name in the whole sweep.**
3. **The Center for Cosmetic Surgery / Rejuvenate MedSpa** — Golden, Denver ×2, Colorado
   Springs and a Denver SkinLab. **The largest practice found in Colorado:** six plastic
   surgeons plus 13 named med spa providers across seven addresses. Nextech, GiftUp gift
   cards, a newsletter. Covers Denver *and* Colorado Springs in one deal.
4. **Vyla Aesthetics** — Park City and Millcreek SLC. Eight named staff including two
   co-owner FNPs. **"Vyla Beauty Bank" at $199/month** on a six-month commitment,
   Aesthetic Record, a $50 late-cancel fee. The best Park City prospect by a wide margin.
5. **AlluraDerm MD Med Spa** — Albuquerque. **The best dormant-credit scheme found
   anywhere in this sweep:** the "A-List" at $149/month, three-month minimum, where each
   payment "becomes credit you can apply to any service or product", unused credit "rolls
   over without penalties and does not expire while the membership is active", and after
   cancellation "you have 60 days to use remaining credit before it expires". Zenoti, plus
   a birthday gift card, two annual guest passes, Cherry and CareCredit.
6. **Sandia Skin + Face** — Albuquerque. An FNP-C owner plus a facial cosmetic surgeon
   co-owner and three more staff. A **"Beauty Bank Membership"** with a monthly treatment
   balance. PatientFi and Cherry. Nextech.
7. **Stay Flawless** — Albuquerque ×2. A membership benefits page, a **"Flawless Rewards
   Program"**, financing and gift cards. Running **both PatientNow and a GoHighLevel form
   subdomain**.
8. **Ageless Aesthetics** — Santa Fe. **Zenoti plus Liine lead-capture forms**, so they
   already pay for lead software. Facial and wellness memberships, both manufacturer
   rewards programmes, two lenders, walk-in Wednesdays, thirteen staff named. **By profile
   the best Santa Fe prospect; Viva Skin got the pipeline slot only because it publishes
   an address.**
9. **Timeless Aesthetics** — Colorado Springs. Boulevard, a "Timeless Member" membership,
   treatment packages, 0% financing over up to 24 months, Square e-gift cards.
10. **Beautiful Skin** — Denver and Boulder. **Two booking platforms** — Zenoti for Denver
    and Booksy for Boulder — with a "Beauty Bank" membership *and* a separate TrueTox
    membership.
11. **Treasure Valley Aesthetics & Wellness** — Boise and Caldwell. **Pabau**, a DNP owner
    and medical director, and a redeemable-consult lead magnet.
12. **Raval Facial Aesthetics** — Denver Cherry Creek. Nextech, and three membership
    ladders at $50, $75 and $100 a month.
13. **Juicy Face Med Spa** — Denver Cherry Creek. The richest dormant stack on any
    unreachable site — a VIP club, a VIP access signup, a newsletter page, an offers page,
    payment plans and gift cards — and it **publishes neither an email nor a phone number**.
14. Also: **Monumental Med Spa** (Palmer Lake, Zenoti), **The Firm Medspa** (Lone Tree,
    a $50-off first-visit form), **BB Medical Esthetics** (Boise and Meridian, Vagaro,
    a VIP signup through Podium).

**Ruled out, don't revisit.** Verified email but nothing dormant to reactivate — the
category to stop researching: **Spa 35** (Boise — has both the address and Zenoti, but no
membership, loyalty or lead magnet; the only scheme is that financing "may" be available),
**Santa Fe Skin Institute**, **Ageless Aesthetics Med Spa** (Cherry Creek — its injector
is top-1% nationally by Allergan's count, and there is still no scheme of any kind),
**Skinsanity**, **Alpine Aesthetics**, **Ahern Aesthetics** (Park City — the site
advertises "Personalized, **no memberships**"), **Mindful MedSpa**, **Ageless MD
Solutions**, and **Revenge MD** (Reno, Las Vegas and Henderson — eleven named staff,
three locations, four lenders under "BOOK NOW. PAY LATER.", and no membership or loyalty
scheme at all, so the financing applications are the only pool and not one the ICP
recognises). Scale but no scheme and no address: Janiga MDs, Renovation Medical Spa,
Bonaldi Aesthetics, Dr Eric Cerrati, Santa Fe Medical Aesthetics, Venus Medi Spa.
Chains and multi-state groups: **Aurora Medical Spa** (nine sites across three states
behind one Austin-area number), **RenewMD** (eight sites across three states behind an 800
number, despite an excellent $50 referral "Beauty Bank"), Face to Face Spa, SkinSpirit,
Ideal Image, OVME, 4Ever Young. **Belén Aesthetics** (Denver) returns ROBOTS_DISALLOWED to
any fetch and cannot be judged either way without a human opening it.

**What this region taught us.** The **"beauty bank" is the Mountain West's signature
scheme** — eleven separate clinics run a named banked-credit membership, several of them
stating in writing when the balance expires, and they are already tracking that liability
in Zenoti or Aesthetic Record. A regionally specific opener could be built on the phrase
itself. **Vagaro matters here in a way it did not in earlier US sweeps** — five clinics,
and it is the dominant platform among smaller Mountain West med spas, behind Zenoti's
eight. And **two more clinics already run GoHighLevel** — Utah Facial Plastics and Stay
Flawless — which brings the pipeline's GHL count to four and makes them the cheapest
integrations available; both are blocked purely on a readable address.

---

## The standard changed under all of this — 16 Oct 2026

Everything above was swept under the 22 Sep ICP, which *wanted* scale: multi-site groups,
plastic surgery, "$100k+/month" proxies. On 16 Oct Jess uploaded Griffin's *Med Spa
Reactivation* briefing and told us to master it, and the standard inverted. v2 wants
**owner-operated, injectables-led, cash-pay, one to four sites**; plastic surgery,
dermatology, hospital-attached groups and anything with five or more locations are now
disqualified outright.

So read the sweeps above with that reversal in mind:

- The clinics ruled out above for having **no published email** are still ruled out. That
  finding does not expire — it is about the website, not the standard.
- The clinics the sweeps above *kept* are a different matter. 49 pipeline rows were
  re-graded to C on 16 Oct for failing v2, most of them for being surgical practices or
  five-site-plus groups. The notes on each row say which rule it failed.
- A market this file records as "swept" was swept for the **old** profile. Looking for
  single-site owner-operated clinics there may well turn up rows the old pass skipped as
  too small — "single-operator studios with no support staff" was a disqualification under
  22 Sep and is close to the ideal under v2. Boutique one-site clinics passed over in the
  Midwest, mid-Atlantic and Mountain West sweeps are worth a second look.
- **Australia is now the priority market** and barely appears above. Sydney, Melbourne,
  Brisbane, Gold Coast and Perth are where the next sweeps belong.

The other v2 change that affects sourcing: an opener may not name a product or a price.
Several US rows above carry membership and tier prices in their opening angle. Those
openers need rewriting before they send, and future rows should quote a fact about the
practice — who owns it, how long it has traded, what scheme it runs — rather than its menu.

---

# Australia, second pass — 18 Oct 2026, under ICP v2

The 24 Sep Australian sweep looked for scale and ruled out "single operators with no
support staff". v2 wants exactly those clinics, so this pass went back over the same five
metros plus Tasmania and Canberra, staying out of the CBDs and the multi-site groups.
It added 82 pipeline rows (ids 300-381) and the clinics below are the ones it could not
email.

**Two findings that change how to work this market.**

The first is that **Australia's problem is not Cloudflare, it is silence.** Suburban
clinics here publish a phone number and an Instagram handle and no email at all. Sydney
produced not one obfuscated address in the whole sweep. So the "Jess reads it in her own
browser" workaround, which rescued clinics in the UK and the US Northeast, rescues almost
nothing here — most of these need a call or a DM, and Jess has ruled out calling. That
makes the LinkedIn and Instagram route the only one left for them.

The second is that **builder placeholders are a trap.** Several Melbourne clinics publish
`filler@godaddy.com` or `contact@wix.com` — a template default the owner never replaced.
Those are not addresses, they are furniture, and they are not recoverable in a browser
either. Likewise, directory sites ship real-looking addresses inside QR code images; the
Perth sweep flagged three rows that would have been fabrications had it trusted them.

**What worked, for the next pass.** Blocking the directory farms (whatclinic, fresha,
doctify, bookwell, top4) was the single biggest lever in three of the four sweeps — plain
brand-name searches returned overseas medical-tourism spam. Stacking four or five suburb
names into one query with "membership", "nurse" and "contact" roughly doubled the useful
hits. Guessing a `.com.au` domain and passing it as `allowed_domains` beat searching for
the clinic by name, because search is US-weighted. And Fresha's city landing pages are the
cheapest test of whether a clinic is established, since they show the name, the suburb and
the review count together.

**What this pass could not reach:** Toowoomba, Cairns, Darwin, and most of the Sunshine
Coast, where about a third of the qualifying clinics are robots-disallowed. Nine unscreened
Sydney candidates and two Canberra contact pages are listed in the sections below for
whoever picks this up next.


## Sydney (suburban) near-misses — 18 Oct 2026

Clinics that clear the ICP but that I could not put in the pipeline, almost all for the same
reason: **no readable email address anywhere on their own site.** Notably, **not one** Sydney
clinic in this sweep used a Cloudflare-obfuscated address — the pattern here is simply
"phone number and Instagram, no email at all", so there is nothing Jess can unmask in her own
browser. These need a phone call or a DM, not an email.

## Qualifies on ICP, publishes NO email address at all

| Clinic | Where | Why it qualifies | Evidence gap |
|---|---|---|---|
| **Hills Aesthetics** | Castle Hill (Suite 1, 269-271 Old Northern Rd) | "Hills Aesthetics was then founded in 2021" — stated outright, so 5 years of trading; one site; Danielle (RN, 13+ years, surname Hunt only in page metadata); Timely; gift vouchers sold through Timely | Homepage lists only phone 0430 871 926 + socials. `/contact/` returned a server error on two attempts, so an address may exist there — worth one retry later. Best near-miss of the batch. |
| **Lived In Aesthetic** | Northern beaches | Founder and Clinic Director "Sarah", RN; Timely (bookings.gettimely.com) | No email on homepage; footer lists "Privacy Policy" as text with no link; `/contact` 500-errored twice. |
| **Facetime Skin and Body** | Crows Nest (Shop 58/78-80 Alexander St) | One site; "specialist clinician" with 18+ years; injectables on the menu; runs on **Konnect** (bookings.konnect.software); "Skin Gym Programs" packages page = a real dormant signal | No email anywhere on the homepage, including footer. No practitioner named either. |
| **Marah** | Chatswood | Founder & Clinical Director **Marina Hu** named; "15+ Years in Practice"; one clinic; Fresha | No email anywhere including footer — phone and address only. Injectables prescribed by an unnamed AHPRA practitioner, administered by the nursing team. |
| **Rejuve Cosmetix** | Sydney (suburb not stated) | Founder **Linda**, RN, 14+ years; Timely | No email; and the phone is contradictory — page text says 0478 008 228 while the tel: link goes to 0406 789 188. Also no address published, so I could not confirm the suburb. |
| **Cosmetic Nurse Sarah** (cosmeticinjectablessydney.com.au) | "2 locations across Sydney NSW" | Nurse since 2010; two sites; Timely | No email; no suburbs named at all, which makes it hard to even place. |
| **Northern Beaches Cosmetic** | Belrose | Led by **Dr Sam Qin**; one site; 2017 copyright | No email. ALSO a likely must-have fail: the menu includes "Skin Checks" and "Skin Moles Removal", which usually means Medicare billing — check before ever working it. |

## Qualifies, publishes an email — but one I do not trust

| Clinic | Where | Issue |
|---|---|---|
| **Cosmetic HQ by Danielle Ryan** | Corrimal, Wollongong / Illawarra | Good ICP fit — AHPRA-registered cosmetic nurse **Danielle Ryan** named as founder, 10+ years, one site at 1/55 Railway Street, Timely. But the only address published on cosmetichqbydanielleryan.com.au is **info@malexinjectables.com** — a different business's domain. Either a shared/sister brand or an unedited template leftover. I would not send to it without Jess eyeballing the site herself. Worth a phone follow-up; the clinic itself is the best Illawarra candidate I found. |
| **Skin Social** | Sydney (memberships page) | Sells memberships, which is exactly our dormant signal, but the site is **robots-disallowed** to WebFetch, so I could verify nothing — not the suburb, not the owner, not an address. Needs a human to open it. |

## Ruled out on the must-haves (do not re-source)

- **Dee Why Skin Cancer and Cosmetic Clinic** — skin cancer work, Medicare. Fail on cash-pay.
- **Rejuv Australia**, **Babyface**, **My Cosmetic Clinic**, **Laser Clear Clinic** (East Gosford /
  Terrigal / Cooks Hill) — multi-site networks or chains; Laser Clear is borderline on three sites
  but reads as a laser chain rather than an owner-injector clinic.
- **Dr Van Park**, **Refine Clinic**, **Cosmos Clinic** — surgical / plastic-surgery-led.
- **Privée**, **Contour Clinics**, **Concept Cosmetic Medicine** — already on the ruled-out list.
- **MD Cosmedical Solutions**, **Bespoke Cosmetics Institute**, **DrCosmetist**, **The Beauty
  Collective**, **Beauty and Laser Clinic**, **Ozderm / Medical Cosmetic Clinic**, **Face to Face by
  Marjan** — not reached before budget ran down; unscreened rather than rejected. Pick these up first
  on the next Sydney pass.

## What this market taught me

Suburban Sydney is full of exactly the clinic the new standard wants — one site, one named
owner-injector, Timely or Phorest underneath — but it is the **worst market so far for published
email**. Roughly half the qualifying clinics publish no address at all; the northern beaches and
lower north shore were the worst for it. The useful substitute signal was the **booking subdomain**:
searching for `gettimely.com` and reading `bookings.<brand>.gettimely.com` links off homepages both
identified the practice system and proved the clinic was single-site, because multi-site groups route
through `book.gettimely.com/Booking/Location/<id>` with a location picker instead. Shopify-built
clinics (Manly, The Clinic Bondi, Sisä) were the most reliable for a readable address, because
Shopify forces a `/policies/privacy-policy` page that almost always restates the contact address —
and those policies consistently described the clinic's *own* opt-out email marketing, i.e. the
opposite of a no-unsolicited-email notice. I found **no** clinic in Sydney carrying such a notice.
Constructed `/privacy-policy/` paths 404 on the smaller WordPress and Squarespace clinics, which is
itself a finding: most of these businesses have no privacy policy at all.

## Melbourne near-misses — inner & middle suburbs, Geelong, Ballarat
Swept 18 Oct 2026 under ICP v2. These clinics clear the ICP on fit but publish **no readable
email address**, so under the absolute rule on email addresses they are not sendable from here.
Two different problems, which need two different fixes.

---

## Group 1 — Cloudflare-obfuscated address (Jess can read these in her own browser)

### Dermaluxe Beauty — Geelong West / Geelong / Colac, VIC
- **Site:** https://dermaluxebeauty.com.au/
- **Why it qualifies:** Three Victorian sites (138 Shannon Ave Geelong West; a day-spa suite at
  Oaks Vue Geelong; a monthly room in Colac) — inside the four-site cap. Runs **memberships**,
  **gift vouchers** and a **payment plan**: three separate pools of named people with unspent
  intent. Two practice systems side by side — **Phorest** (`dermaluxebeauty.phorest.me`) for the
  main book and a **separate Timely instance specifically for injectables**
  (`bookings.gettimely.com/dermaluxeinjectables/book`), which is both a nameable system and
  evidence injectables are a distinct, deliberate revenue line.
- **Email status:** **Cloudflare-hidden.** The contact section and the footer both render the
  literal placeholder `[email protected]`. Per the brief that counts as NOT SEEN and I have not
  recorded it. **Jess can almost certainly read it by opening the page in a normal browser** —
  worth sixty seconds, because on fit this is one of the better prospects in the whole batch.
- **Caveats:** No owner or founder named anywhere ("Meet the Team" links to an empty page). No
  founding date. No specific injectable treatment named in body copy — injectables are inferred
  from the Timely URL and the Facebook handle. The Colac site opens one Monday a month, so it is a
  room, not a clinic.

### Appearance Clinic Australia — Aberfeldie / Essendon, VIC
- **Site:** https://appearanceclinicaustralia.com.au/
- **Why it qualifies:** Says it has operated **"Since 1995"** with "30+ Years of Experience" —
  the deepest lapsed pool I found outside Nitai and Beauty on Rose. **Dr Diana Phan** named as
  leading the team. Runs **Aesthetic Record** (My Aesthetic Record booking), which is on the
  brief's own list of nameable practice systems. One real clinic (301 Buckley St, Aberfeldie;
  the FAQ says Essendon).
- **Email status:** **Obfuscated.** The only email on the page is a scrambled "Email Us" link.
  It decodes to a plausible `info@` address, but that is a decode, not text shown on the page, so
  I have recorded nothing. **Jess can read this one in a browser.**
- **Caveats, and they matter:** the site advertises **18 "locations"** — Brunswick, Carlton,
  Docklands, Essendon, Fitzroy, Footscray, Hawthorn, Kensington, Maribyrnong, Moonee Ponds, North
  Melbourne, Parkville, Richmond, South Yarra, Southbank, St Kilda, Williamstown, Yaraville —
  against **one street address**. These are SEO suburb pages, not sites, but anyone reading
  quickly will score this as a 5+ fail. Injectables are one of many treatments, not the stated
  focus. Dr Phan is called team lead, never owner.

---

## Group 2 — No email address published at all (a form or phone only)

### Take Off Skin & Body — North Melbourne, VIC
- **Site:** https://takeoffskinandbody.com.au/
- **Why it qualifies:** Strong dormant-list infrastructure — a real **three-month membership
  program** (four named tiers, each requiring a consultation and prepaid treatment courses, with
  a "must be completed within 3 months" expiry that *manufactures* lapsed patients), plus **gift
  vouchers**, both running on **Square**. "Nurse Shelley" is the public face.
- **Email status:** **None published.** I fetched the contact page and the memberships page; there
  is no email address and no `mailto:` link in body or footer on either. Phone, street address and
  a contact form only. Not recoverable by opening a browser — the address genuinely is not there.
- **Caveats:** Site copyright reads 2020, so trading length is unverified. Owner not named.
  Memberships are facial/skin courses, so the list may skew skin rather than injectables.

### Medical Aesthetic — South Melbourne, VIC
- **Site:** https://medicalaesthetic.com.au/
- **Why it qualifies:** **Established 1984 — "over 40 years."** Nothing else in this sweep comes
  close; a four-decade patient database is the single largest lapsed pool I saw. Runs **The Good
  Skin Club**, a genuine tiered weekly-fee membership (three levels), on **Timely**. Zena Dammous
  named as leading first consultations with "over 12 years of experience in aesthetic care."
- **Email status:** **None published.** Phone numbers, booking links and a **Podium** enquiry form
  (`forms.podium.com`) — no email address anywhere on the homepage. A Podium form usually means
  inbound is deliberately routed to SMS, which is ironic given our offer is SMS-based, and is
  itself an argument for a phone-first approach rather than email.
- **Caveats:** Injectables are offered but are **not** the focus — the clinic positions itself as a
  laser-hair-removal and cosmetic-skin pioneer, with injectables sitting inside an "Age Management"
  category. No owner named.

### In Depth Cosmetics — Albert Park, VIC
- **Site:** https://indepthcosmetics.com.au/
- **Why it qualifies:** Single Albert Park site, explicitly **"specialises in advanced cosmetic
  injectables"**, run by **"Nurse Julie"**, a Registered Nurse Cosmetic Injector with "over 20
  years of nursing experience" including more than five years working with plastic surgeons.
  Books on **Timely**. Clean owner-operator shape.
- **Email status:** **None published.** The only address on the page is `filler@godaddy.com`,
  which is a GoDaddy website-builder placeholder in the "Signed in as" account menu, not a clinic
  address. I did not record it. Nothing a browser would recover.
- **Caveats:** No founding date, so trading length unverified. No membership, loyalty or voucher
  scheme — the only promotion is a dated HIFU special. Appointment-only, likely single-operator.

### Skin Society Co — Belmont, Geelong, VIC
- **Site:** https://skinsocietyco.com.au/
- **Why it qualifies:** **Founder Aubrey**, an internationally registered nurse with over ten
  years' nursing experience, one site at 159 High St Belmont. Injectables are headline services.
  Books on **Fresha**. Sells **gift vouchers from $100 to $750, "Valid for 12 months"** — dated
  banked credit against named buyers is close to a perfect dormant-list signal — plus a
  first-time-client offer feeding an enquirer list.
- **Email status:** **Not found.** No email on the homepage, and `/contact-us/` returned a fetch
  error so I could not check it. This one is **unresolved rather than confirmed absent** — an
  address may well sit on the contact page. Worth one retry; on fit it would be a solid B, maybe
  an A given the named founder plus Fresha plus dated vouchers.

### Enhanceme Lab — Ballarat Central, VIC
- **Site:** https://www.enhancemelab.com/
- **Why it borderline qualifies:** Single Ballarat Central site, a registered nurse and skin
  therapist on staff, a gift card on sale.
- **Email status:** **None published.** The only address is `contact@wix.com`, a Wix template
  placeholder. Not recorded.
- **Why it would probably fail anyway:** the footer reads **"© 2035"** and the newsletter block is
  unstyled — the site is a barely-edited Wix template, which points to a very new business, and the
  only injectables reference on the whole page is a "Post Injectables Aftercare" link. Listed for
  completeness, not as a recommendation.

---

## Also looked at and dropped outright (not near-misses)

- **CDC Clinics** (`cdc-clinics.com.au`) resolves to **CSD Clinics**, Armadale — already on the
  do-not-source list, and it offers **skin cancer checks**, which is a Medicare/cash-pay fail.
  Runs Zenoti, for what it's worth.
- **Cityskin Brighton**, **Victorian Laser & Skin**, **MySkin Clinics** — previously ruled out or
  multi-site chains.
- **Melbourne Cosmetic Centre** (`melbournecosmeticcentre.com`) is an injectables **training
  provider**, not a treating clinic.
- **drsaber.com.au** is one practice spraying near-identical suburb landing pages across Melbourne
  (Fitzroy, CBD, North/East/South Melbourne); it reads as an SEO shell rather than local clinics.
- **Beingwell Melbourne** — multi-specialty wellness group.
- **dvinesmiles.com.au** — a dental practice selling injectables on the side.

---

## What this market taught me

Melbourne's inner and middle ring is exactly the opposite of the CBD sweep, and the constraint
flipped with it. In the CBD the problem was scale — everything was a group with a head office. Out
here almost nothing fails on site count; the single-site owner-injector is the *default* shape. The
binding constraint became **the email address**, and specifically **small-operator web hygiene**.
Clinics run by one nurse with a Wix, Squarespace or GoDaddy template routinely publish a phone
number and a form and no address at all, or leave a builder placeholder (`filler@godaddy.com`,
`contact@wix.com`) sitting where a real address should be. Four of my seven near-misses are that
exact failure, and none of those four are recoverable in a browser — the address is simply not
there. Only two were Cloudflare-hidden and therefore worth Jess's sixty seconds. If this metro
is swept again, the yield-limiting step is not finding clinics, it is that **roughly a fifth of
good-fit owner-operated clinics are unreachable by email by construction** — and a few, like
Medical Aesthetic with its Podium SMS form, have deliberately chosen not to be reachable that way.

Two further patterns worth carrying forward:

**The "wallet/bank" search technique did not work here and something better replaced it.** Searching
"beauty bank Melbourne" and "skin wallet Melbourne" returned nothing but WhatClinic and Fresha
directory spam. What worked was **stacking four or five suburb names into one query** alongside
"membership", "nurse" and "contact" — four such searches produced every single row in this batch.
Blocking `whatclinic.com`, `fresha.com`, `doctify.com` and `bookwell.com.au` roughly doubled the
useful hits per search. Fetching `/contact/` blind was right about 70% of the time; when it errored,
the plain homepage almost always carried the address anyway, so a failed `/contact/` is worth one
homepage retry rather than abandonment.

**Site counting is now the subtlest trap, not the obvious one.** Three different structures all
*look* like 5+ sites and are not: SEO suburb pages masquerading as locations (Appearance Clinic
claims 18 against one address; Dr Saber does the same), one travelling nurse running clinic days
across towns (PEP Me Up's six, Bianca Stewart's four), and injectors renting rooms inside host
beauty salons (Beneath The Skin's five, Dermaluxe's Colac room, Loving Glow inside Devine
Aesthetics). The brief's rule — 5+ means a head office decides marketing — is about *who decides*,
and in all three of those structures one person still decides. I parked PEP Me Up and Beneath The
Skin as C rather than dropping them for precisely that reason, and I'd suggest the rule be
restated as decision-makers rather than addresses. Two genuine disqualifies did show up and are
cleanly parked: EST Clinic (plastic surgeon on the team) and True Aesthetics (two of three sites
inside private hospitals).

## Queensland near-misses — 18 Oct 2026

Clinics that clear (or very nearly clear) the ICP but publish no email address I could read.
Two different handling routes: **Cloudflare-hidden** (Jess can read these in her own browser in
about ten seconds each) vs **no address published / site unreadable to a fetcher**.

## Cloudflare-hidden address — Jess can read these herself

1. **Ascension Cosmetic Medicine** — New Farm, Brisbane. https://ascension.com.au/
   Single site ("our New Farm clinic"), doctor-led (Dr Scott Allison named), cash-pay, very broad
   device and cosmetic-medicine menu, **Zenoti** (ascension.zenoti.com) as the practice system,
   gift cards sold through the shop. Strong A-grade candidate on every test except the address.
   Three email links on the contact area, **all rendered as the Cloudflare `[email protected]`
   placeholder** — not recorded. Also note three different 1300 numbers on one page.
2. **S Kosmetics** — Parkwood, Gold Coast. https://www.skosmetics.com.au/contact_us.php
   One site, ~574 reviews on Fresha, Fresha booking, gift vouchers, InMode device suite plus
   regenerative injectables. Address shows as `[email protected]` (Cloudflare); the underlying
   link decodes but that is not a *seen* address, so it is not recorded. Caveat for Jess: the
   page's own meta description calls the business "Cosmetic and Plastic Surgery", which may
   disqualify it on the surgery rule — check before sending.

## No readable address — site blocks fetching or publishes a form only

3. **Aesthetic Nurse Aimee** — Noosaville / Coolum Beach, Sunshine Coast. aestheticnurseaimee.com.au
   Founder named and verified in press: Aimee Browne, senior registered cosmetic nurse specialist,
   founder/director, written up in Noosa Today in September 2022 (so 4+ years trading). Exactly the
   owner-operator profile. **Site returns robots-disallowed on every page**, so nothing could be read
   off it — needs a human browser.
4. **sō Aesthetica** — Mooloolaba (La Balsa building), Sunshine Coast. https://soaesthetica.com.au/
   Injectables-only clinic, RN Dionne Hayes named ("Your Registered Nurse", 20+ years), one site.
   Homepage shows **no email and no phone**; the /contact page is robots-disallowed.
5. **Illuminate Aesthetics Co** — Warana, Sunshine Coast. illuminateaesthetics.com.au
   Named in three separate Style Magazines Sunshine Coast injectables round-ups, has its own
   contact page. **Whole domain robots-disallowed** — nothing readable.
6. **Azure Aesthetics** — Maroochydore, Sunshine Coast. azureaesthetics.com.au — robots-disallowed.
7. **Imani Skin Clinic** — Maroochydore, Sunshine Coast. imaniskinclinic.com.au — robots-disallowed.
   ~152 reviews on Fresha, so a real trading history.
8. **Define Clinic** — Milton, Brisbane. defineclinic.com.au
   Doctor-led (Dr Joshua Mullins), Timely (defineclinics.gettimely.com), named in the Style
   Magazines Brisbane injectables list. **Robots-disallowed** — no address readable.
9. **Nurse Vicki Aesthetics** — Mermaid Beach, Gold Coast. nursevickiaesthetics.com.au
   Owner-named brand, injectables-only pages, on Fresha's Gold Coast list. **Robots-disallowed.**
10. **Skin to Soul Clinic** — Mermaid Waters, Gold Coast (plus a Melbourne site, so 2 locations).
    https://skintosoulclinic.com.au/contact/ — Timely, full injectables and thread-lift menu.
    Contact page publishes **a form and a phone number only; no email address at all**. Not a
    Cloudflare case — there is nothing to read, so this one needs a phone or form approach.
11. **Beautiqué / miscellaneous Fresha-listed Gold Coast clinics** (Snatched Clinic, Clarity Cosmetic
    Laser, Mimi Lane Cosmetic, Image Aesthetics Burleigh, Stevie J. Aesthetics, Gold Coast Cosmetic
    Medicine): all appear on Fresha's Gold Coast aesthetics directory with real review counts but
    I ran out of budget before finding and verifying their own domains. Worth a second pass.

## Ruled out on the ICP, not on the address (noted so nobody re-sources them)

- **The Rejuv Lab** (Buderim, Noosa, Bundall, North Lakes, Springwood + 2 NSW) — **7 locations**,
  head-office marketing, contact form only. Fails the 1-4 site rule outright.
- **AuzSkin Aesthetic & Dr Umed Cosmetics** — 4 sites across Australia, New Zealand and Dubai, and
  it runs **skin cancer services** alongside cosmetics (HotDoc for skin checks, Kitomba for
  cosmetics). Fails scale and cash-pay. Its `info@auzskin.com.au` exists only behind a footer icon,
  not as visible text, so it would not have been recordable anyway.
- **Laser Skin Specialist** (Bundall) — publishes info@laserskinspecialist.com.au openly and runs
  Phorest, but the menu has **no injectables**: laser/skin only.
- **Skin Enhance** (Bulimba, 638 Fresha reviews) — no injectables, and no email on the site.
- **LÚME HAUS Aesthetics** (Wavell Heights) — publishes lumehausaestheticsau@gmail.com and names
  founder Katharina Libicher, but it is brows/lashes/body sculpting, not injectables.
- **Earth & Skin** (Mudgeeraba) — day spa. **Chantal Louise Skin Therapy**, **Hawthorne Skin &
  Beauty**, **Aceso Aesthetics** (Hawthorne) — skin/brow/cosmetic-tattoo led, not injectables.
- **Cosmetic Injectables Australia** (East Brisbane) — redirects to **cosmeticnursesaustralia.com.au**
  with Brisbane, Gold Coast and Darwin locations; the domain-redirect-to-another-company rule plus an
  unresolved site count parked it. Could be re-checked if the standard widens.

## What this market taught me

Queensland's owner-operated aesthetics layer is deep and almost entirely nurse-owned — the pattern
is a single suite in a shopping plaza or a shared studio building, one or two registered nurses, a
Timely or Fresha diary, and a gift-voucher page. Timely dominates Brisbane and the Gold Coast;
Fresha dominates the review-rich clinics (it is also the best *discovery* tool I found, because its
city landing pages list clinic name, suburb and review count together, which is the cheapest
"established?" test available). Dapple appeared once, Zenoti once, Kitomba once, Phorest once.

The real constraint here was not ICP scarcity, it was **readability**. Roughly a third of the
qualifying Sunshine Coast and Gold Coast clinics sit behind robots-disallowed walls or Cloudflare
email obfuscation, and Wix/Squarespace builds increasingly publish a form instead of an address.
The Sunshine Coast was by far the worst (five of my seven best candidates there were unreadable),
which is why my accepted rows skew Brisbane and Gold Coast. Search was also actively hostile: the
engine is US-weighted, so brand searches returned Florida med spas, and the technique that actually
worked was `WebSearch` with a **guessed .com.au domain in `allowed_domains`** plus a generic
"contact us email" query — that confirmed the domain and handed me the contact URL in one call.
Local magazine listicles (Style Magazines Brisbane/Gold Coast/Sunshine Coast) were the best
candidate generator and often named the owner-injector where the clinic's own site did not.

One recurring trap worth flagging to whoever writes the email: several of these clinics are
mid-rebrand (Hamilton Skin Clinic → Soluxe Skin House, Fresh Face Australia → Amayra, SCinjectables
→ Aesthetics on Point). That is great news for the offer — a rebrand strands an old patient list —
but it also means displayed addresses and underlying mailto links sometimes disagree. Always send to
the address as published, and expect some bounces.

## Near misses — Perth / Adelaide / Tasmania / Canberra sweep, 18 Oct 2026

Clinics that look like the ICP but could not go in the pipeline because no email address
was readable off their own site. The two categories need different handling: a
**Cloudflare-hidden** address Jess can read herself in a browser in ten seconds; a
**no address at all** clinic needs a phone call or a contact form instead.

---

## Cloudflare-hidden address — Jess can read these in her own browser

### Academy Face & Body — Suite 1a, Arcadia Chambers, 1 Roydhouse Street, Subiaco WA
- **Why it looked right:** long-established Subiaco clinic, named lead practitioner (Dr Jason Oates), single address published, phone and fax both listed. Contact page carries no "no unsolicited commercial email" notice.
- **Email status:** **Cloudflare-obfuscated.** The contact page at https://academyfaceandbody.com.au/contact/ renders the address as `[email protected]`. Not recorded, per the absolute rule.
- **Warning before Jess spends time on it:** Dr Jason Oates works in facial surgery, and the clinic brands as "Face & Body". If it is a cosmetic-surgery practice it is disqualified outright regardless of the email, so check the treatment menu before unmasking the address.

### Aesthetique Medical — Shop 2, 246 Unley Road, Unley SA
- **Why it looked right:** two named co-founders (Noleen, Registered Nurse; Dr Veronica, Cosmetic Doctor) plus a senior dermal therapist, one site, Zenoti in place (aesthetiquemed.zenoti.com), a real linked privacy policy, and a broad device menu (Morpheus8, EMFACE, Lumecca, EMSELLA).
- **Email status:** **Cloudflare-obfuscated.** The footer of https://aesthetiquemedical.com.au/about-us/ renders as `[[email protected]]`.
- **But it probably fails anyway:** the about page calls it "Adelaide's Newest Boutique Clinic", and the only tenure figures given are staff experience (Noleen 5 years). A clinic marketing itself as the newest in town does not have 300+ lapsed patients. Unmasking the address is cheap, but this is a park-for-later, not a send.

---

## No readable address anywhere — needs a phone call or a form

### Canberra Cosmetic Medicine Centre (cancosmed.com) — 1/14 Hannah Place, Deakin ACT
- **Why it looked right:** the best "established" evidence I found in Canberra — the clinic claims it has treated **over 20,000 clients in nearly 25 years**, which is exactly the lapsed-list profile the offer needs. Injectables, IPL, peels and medical management of acne, rosacea and pigmentation. One site. "Dr Gibson" credited with introducing the category to Canberra.
- **Email status:** **none obtainable.** cancosmed.com returns ROBOTS_DISALLOWED to any fetch, so I could not read a single page of it, and the Top4 listing's contact record has an empty email field. This is a crawler block, not Cloudflare obfuscation — Jess opening the site in a browser would see whatever address is there.
- **Caveat:** sclerotherapy and "medical management" of skin conditions on the menu raise a Medicare question that needs answering before pitching. Phone is (02) 6282 8587.

### The Skyn Lounge — Bruce, Canberra
- **Why it looked right:** gift vouchers available in clinic, a 75-minute new-client skin assessment as an entry point, injectables delivered by a named staff member (Hayley), and **two** nameable practice systems in evidence — Phorest for appointments and a second Shortcuts Software booking link. Reviews name three staff, so it is busy.
- **Email status:** **no address on the homepage.** There is a contact page at https://www.theskynlounge.com.au/contact that I did not fetch (shared fetch budget). Worth one fetch next run — this is the most likely of the near-misses to convert.
- **Caveat:** no founding year, no owner named, and the menu is skin-, laser- and beauty-led with injectables as one line. Name collision warning: this is **not** the already-ruled-out "SKYN" brand.

### Platinum By April — Canberra
- **Why it looked right:** founder named and fronting the brand ("Nurse April", head aesthetics nurse), **six named practitioners** including four registered nurses, Timely in place, and a "Cosmetic Aesthetics" category on the menu. A six-practitioner single-site clinic has a real lapsed list.
- **Email status:** **no address on the our-story page.** A contact page exists at https://www.platinumbyapril.com.au/contact-us-1, unfetched (budget). Second-best conversion candidate.
- **Caveat:** no founding year, no location count, no privacy policy, and the Cosmetic Aesthetics category lists no treatments, so injectables-led is inferred from the nurses' titles.

### Siren Cosmetic Clinic — Perth
- **Why it looked right:** surfaced on an owner-operated, cosmetic-nurse-led search for the Mount Lawley / Leederville / Fremantle / South Perth corridor.
- **Email status:** **unknown.** https://www.sirencosmeticclinic.com.au/ returned a client error on fetch, so nothing was verified — not even the suburb. Retry next run before writing it off.

### The Aesthetic Laser Centre — Battery Point, Hobart
- **Why it looked right:** the only Hobart clinic listed in the Battery Point professional strip, i.e. the right postcode for cash-pay aesthetics.
- **Email status:** **no own website found.** The only presence that surfaced was a Facebook page. Directory-only businesses are not worth a send.

---

## What this market taught me

**Generic searches are useless here and brand searches are worse.** Every "cosmetic
injectables <suburb>" query returned the same wall of WhatClinic, Top4, Fresha, Seek and
bsale listings, and searching a clinic by its own name was the single worst-performing
move of the run — it returned medical-tourism spam and overseas clinics with similar
names. The thing that actually broke the market open was `blocked_domains` with the
directory farms listed out: the same query that had returned nine directories returned
nine real clinic domains. That is a bigger lever than any query wording, and it should be
the default on every future AU sweep.

**The directories were still worth one pass, but only for names.** WhatClinic state-level
pages gave me a clean roster of clinic names per market at one fetch each, and Top4
business pages then gave me the clinic's own domain. But Top4 ships an email inside a QR
code contact block, and that is a directory address, not a published one — three of my
rows (Future You, Heart Aesthetics, Victoria's) had their address appear in a Top4 QR
first, and I re-read every one off the clinic's own page before recording it. Anyone
working faster than that would have recorded directory data as site data.

**The new standard fits this half of the country better than the old one.** Perth and
Adelaide are full of exactly what the ICP now wants: a named registered nurse, one room,
Timely or Zenoti behind it. The catch is that the same smallness destroys must-have 4 —
roughly a third of what I looked at published no founding year at all, and several
operate out of a room inside someone else's business (Eterna inside Vera Beauty,
Attentive inside FaceHub, Lite Nurse inside the Midnight Hotel). "Established" is the
must-have I had to infer most often, and it is the one most likely to be wrong.

**Tasmania and Canberra punch above their size on list depth.** The three strongest
lapsed-list cases in the whole run came from the smallest markets — Inya in O'Connor
trading since 2009 with a stated last-minute waiting list, Sanctum running Dapple CRM
across three sites on 30+ years, and the one I could not reach, cancosmed.com, claiming
20,000 clients over 25 years. Small-city clinics stay put for decades, which is precisely
what accumulates a dormant list. Chasing those two Canberra contact pages and finding a
way into cancosmed.com is worth more than another twenty Perth searches.

**One practical warning for whoever writes the email:** four of these clinics publish a
mailbox that is not a clean branded one — two gmails (Lite Nurse, and Attentive's hidden
mailto), an ISP mailbox at tpg.com.au (Attentive's visible one), and one address on a
*different domain* from the website it was printed on (The Clinique Aesthetics, whose site
is theclinique.com.au but whose published address is @thecliniqueaesthetics.com.au).
Expect bounces there, and read the `notes` field before sending — the fallback addresses
are recorded in it.

---

# New Zealand, regional Australia, the UK outside the big cities, and the US interior — 19 Oct 2026

Four sweeps, 81 pipeline rows (ids 382-462), 60 of them sendable. The markets were picked
because no earlier sweep had touched them: New Zealand held only three rows in the whole
pipeline, regional Australia none, and the UK and US sweeps in September had stayed in the
large metros.

**New Zealand is the cleanest market we have swept.** Twenty-three of twenty-five pages
fetched published a readable address, with **no Cloudflare obfuscation and no builder
placeholders at all**, and not one site carried a no-unsolicited-email notice. The limit in
New Zealand is not reachability, it is supply: block the chains and the independent layer is
thin. The "wallet / bank / vault" search returns nothing there — what works instead is
**weekly-payment memberships and prize-draw opt-in lists**. Many NZ independents are one
nurse in a room inside another business, or a home clinic that visits a second town monthly,
which is why several are parked: the 300-plus lapsed-patient bar cannot be verified.

**The UK is a legal problem, not a sourcing problem.** UK anti-spam rules let us email a
limited company without prior consent but not a sole trader, and that single screen decided
the whole sweep: sixteen clinics had a readable address and a clean fit, and only eight
printed any company identity. **UK footers name the web designer, not the entity** — the
"Ltd" hides in the privacy policy, and one extra fetch of that page flipped a clinic from
parked to sendable. Worse, the two qualifications are close to anti-correlated: the clinics
that do print a company number often publish no address at all. So **twelve of the parked UK
rows are one Companies House lookup away from being sendable**, which is the cheapest
conversion available anywhere in this file.

**In the US interior the fit is easy and the address is everything.** Clinics there publish
contact forms and "text us" links rather than addresses, which killed the best lead of the
sweep outright. Founding years are almost never published, so "established" was inferred
rather than verified on most rows, and each of those rows says so.

**A third fabrication trap, new this run.** One UK clinic serves a real-looking address in
its Open Graph meta tags while the address visible on the page is obfuscated. A meta tag is
not a published address and was not recorded. That joins the builder placeholders
(`filler@godaddy.com`, `contact@wix.com`) and the addresses shipped inside directory QR
images. Also worth knowing: the Australian "beauty bank" search does not transfer to Britain
— a Cambridge query returned Cambridge, Ontario.

**Market-specific notes.** Timely runs roughly two-thirds of regional Australian clinics,
and three of them had two booking systems live at once, which is a half-finished migration
and a genuine opening angle. Darwin produced nothing because a single group owns its search
results. Cairns over-produced. Queenstown produced nothing.


## New Zealand — near misses (19 Oct 2026)

Clinics that clear the ICP but could not go in the pipeline, plus the NZ clinics I checked
and ruled out for a substantive reason. Sourced 19 Oct 2026.

---

## 1. Clears the ICP, publishes NO readable email address

### Marnie Aesthetics — Queenstown
- **Site:** https://marnieaesthetics.co.nz/
- **Why it qualifies:** founder-led, nurse-run appearance medicine clinic at 4A Sandford
  Terrace, Lower Shotover, Queenstown. Founder is "Marnie", described as an advanced
  aesthetics practitioner and registered nurse. Repeat-cycle injectables menu plus skin
  rejuvenation and iS Clinical retail. Single site. Cash-pay. This is the clinic I most
  wanted for Queenstown coverage, and Queenstown is the one target city in my brief that
  ended up with no accepted row.
- **Address problem:** **no email published at all** — and no phone either. The site exposes
  only a street address and its own internal booking page. This is NOT a Cloudflare-hidden
  address, so there is nothing for Jess to read in her own browser; it genuinely is not on
  the page I fetched. If she wants this one, the route is the on-site booking/contact form,
  or an Instagram DM, not email.
- **Also missing:** surname, founding year, any membership or voucher scheme.

### The Face Place — Auckland (partial; it IS in the pipeline, flagged here for handling)
- **Site:** https://www.thefaceplace.co.nz/
- This one is accepted as an **A** row, but it belongs on this list too because it publishes
  **no generic inbox** — only four personal staff mailboxes (`queza@`, `marilou@`, `bryony@`,
  `jess@`). Dr Jenni Irvine, the named Owner & Medical Director, has no published address.
  I put the Clinical Team Leader in the row. **`/contact` would not fetch** (client error),
  so there may well be a generic `info@` or `hello@` there that I could not see. Worth Jess
  opening that page herself before the email goes out — it is a two-site Zenoti clinic with
  an owner-doctor, so it is the best NZ target in the batch and worth getting the route right.

---

## 2. Checked and ruled out for a substantive reason

- **Koru Skin Clinic (Cashmere, Christchurch)** — in the JSON as a **C**, not a near-miss,
  because it does publish `info@koruskin.co.nz`. Fails the cash-pay screen: skin cancer
  screening, mole checks and minor surgery sit alongside the appearance medicine.
- **Orewa Cosmetic Medical (Auckland)** — in the JSON as a **C**. Dr James Crighton publishes
  `james@` directly, but he is a GP as well as a cosmetic doctor and is based at the Hibiscus
  Coast Medical Centre, so the surrounding practice is not cleanly cash-pay.
- **Dunedin Skin and Surgery Clinic** — surgery practice, disqualified on the face of it;
  not fetched.
- **Skin Centre (Tauranga)** — appearance medicine sits inside what is primarily a
  dermatology/skin-cancer centre; disqualified on category, not fetched.
- **Caci (Mt Maunganui and nationwide)** — national franchise network, far beyond four sites.
- **The Skin Clinics** — multi-site nurse-injector group; head office decides marketing.
- **Face Doctors / Promedical (Auckland)** — not fetched; both read as larger multi-practitioner
  Auckland groups and I ran out of budget before I could count their sites. Worth a look on a
  later run if more Auckland rows are needed, with site-counting as the first question.
- Already excluded by the brief and confirmed as such in search results: Skin Institute
  (national, and skin cancer plus veins), The Cosmetic Clinic (national chain), Transform
  Clinic, Palm Clinic, Ponsonby Cosmetic Medical Clinic, Accent on Skin, Sapphire Appearance
  Medicine. Already in the pipeline: Bloom Clinic (Wellington), Clinic 1 (Auckland),
  Clinic4O2 (Takanini).

---

## What this market taught me

New Zealand is small enough that the usual sourcing trick — search a metro, skim ten clinics —
collapses fast: the first page of results for any NZ city is dominated by the four or five
national chains the brief already rules out (Skin Institute, The Cosmetic Clinic, Transform,
Caci), and once you block those the independent layer underneath is genuinely thin. The
vocabulary swap mattered more here than anywhere: "appearance medicine" is the trade term and
searching it, rather than "med spa", is what surfaced the owner-operated clinics. The
"wallet / bank / vault" trick from the brief returned nothing at all in NZ — zero NZ results,
just a US clinic — so banked patient credit does not seem to be a thing the NZ trade markets.
What NZ independents run instead is **weekly-payment memberships** (Wellington Cosmetic Clinic,
Cashmore, Aesthetic Avenue, The Treatment Clinic, Blossom) and **prize-draw opt-in lists**
with names like "Glow Club", which do the same job for us.

Two structural quirks changed how I graded. First, a large share of NZ independents are a
single nurse working out of a **room inside someone else's business** — a beauty salon, a
wellness cafe — or out of a **private home clinic**, often with a second town visited monthly.
Charris, Timeless, Refine Nurse and Andrea Harris all have this shape. It makes "count the
locations" ambiguous and it makes the 300+ lapsed-patient bar genuinely unverifiable, which is
why five rows came back C rather than B. Second, almost nobody publishes a founding year:
I could verify trading history outright for only three clinics (Clinique Élan 2013, Silk 2022,
Wellington Cosmetic Clinic's 2024 ownership change), so "established" is inferred from menu
depth and practitioner tenure on most rows and I have said so in every `notes` field.

On the upside, the email position is much better than I expected: **23 of the 25 clinics I
fetched published a readable address in page text**, and I hit **zero Cloudflare obfuscation
and zero website-builder placeholders** across the whole run. The NZ pattern is a plain
`info@` or `admin@` in the footer, or the owner's own first name at the domain — which is the
best possible route for this offer. Three clinics publish a personal Gmail rather than a domain
mailbox, which I recorded (they were read verbatim and plainly in use) but flagged as a signal
of how small the back office is. **No NZ site in this batch carried a "no unsolicited
commercial email" notice**, so the Unsolicited Electronic Messages Act screen passed on every
row. The real gap left is geographic, not legal: Queenstown has no row because the one good
clinic there publishes no address, and Auckland is under-covered relative to its size —
I got CBD, Takapuna, Parnell, Albany, Orewa and Conifer Grove, but nothing in Ponsonby,
Remuera, Newmarket, Mount Eden or Howick that was not already ruled out.

## Regional & coastal Australia — near-misses (19 Oct 2026)

Clinics that clear the ICP on substance but publish no email address I could read verbatim.
Split into two groups, because they need different handling.

---

## Group 1 — Cloudflare-obfuscated address (Jess can read these in her own browser)

These clinics **do** publish an address. It renders as `[email protected]` to a fetcher
because of Cloudflare email protection, but it decodes and displays normally in a real
browser. Each of these is one browser visit away from being a sendable row.

### Nouvelle Cosmetics — Newcastle NSW (+ visiting room in Cessnock)
- **Site:** https://nouvellecosmetics.com.au/
- **Why it qualifies:** Jane O'Brien is named as "owner and primary Registered Nurse".
  Trading "since 2016" — the clearest ten-year history of anything I found in the Hunter.
  Timely as the practice system. Gift vouchers sold online. Level 4/6 Bolton St, Newcastle,
  plus a visiting location at 139 Vincent St, Cessnock (so one fixed site, one visiting).
- **Email status:** Cloudflare-hidden. The visible text is `[email protected]`; the link
  target decodes to an `info@` address on their own domain, but it is **not shown in plain
  text anywhere**, so I did not record it. This is the single highest-value near-miss in
  the batch — owner named, decade of trading, nameable system, vouchers. Worth Jess's two
  minutes.
- **Consent note for when it is read:** no "no unsolicited commercial email" notice on the
  contact page. There is a marketing opt-in checkbox ("I want to receive news and special
  offers"), which is a subscriber opt-in, not a refusal notice.

### Dose of Envy — Toowoomba & Dalby QLD
- **Site:** https://doseofenvy.com.au/
- **Why it qualifies:** "Alison Platt RN, Owner & Lead Cosmetic Nurse" — titled owner, which
  is rarer than it should be. Two sites (30c Duggan Street, Toowoomba; 56G Patrick Street,
  Dalby), so within the cap. Timely for bookings and vouchers. A team of unnamed
  "highly skilled Cosmetic Nurses" implies a real book.
- **Email status:** Cloudflare-hidden, and **two of them** — one per clinic, both rendering
  as `[email protected]`, both linking to `/cdn-cgi/l/email-protection`. Also worth knowing:
  the site publishes **no phone number at all**, so email is the only route in. Reading the
  two addresses in a browser would make this a strong B, possibly an A.
- **Consent note:** no "no unsolicited commercial email" notice found.

### Naturaliste Skin Clinic — Bunbury, Busselton & Dunsborough WA
- **Site:** https://www.naturalisteskinclinic.com.au/
- **Why it qualifies:** three South West WA sites, within the cap, plus unspecified
  "Visiting Clinics". Claims to have been "the first clinic to introduce cosmetic injectable
  services in the South West", which is a real trading-history signal. A **Memberships** page
  in the nav, gift vouchers, and a referral scheme that hands out treatment credit —
  "BOOK A SKIN CONSULT WITH A FRIEND & RECEIVE $50 TREATMENT CREDIT EACH". Banked credit with
  names attached is exactly the dormant-list signal the brief asks for.
- **Email status:** Cloudflare-hidden — one per clinic, all rendering `[email protected]`.
  Phones are published for all three sites.
- **Caveat if Jess pursues it:** nobody is named as owner or practitioner anywhere (only
  "Kylie" and "Jacquie" in social captions, no roles), so the buyer is unidentified. Three
  sites with no named owner is the profile that sometimes turns out to have a manager
  running marketing.
- **Consent note:** no "no unsolicited commercial email" notice; newsletter block says only
  "Sign up with your email address to receive our newsletters."

### Minnamurra Medispa — Minnamurra NSW (Illawarra: Kiama / Shellharbour / Jamberoo)
- **Site:** https://minnamurramedispa.com.au/
- **Why it qualifies:** "Our Registered Nurse Kathleen" at 144 Charles Avenue, Minnamurra,
  serving Kiama Downs, Shellharbour and Jamberoo. **Cliniko** as the practice system, which
  is a named, exportable system. Gift vouchers offered.
- **Email status:** Cloudflare-hidden — shown as `[email protected]` in the body text and
  behind a "Send Email" button under "Contact Kathleen".
- **Caveat:** Kathleen is named but not titled owner, no surname, and the clinic says she
  works with "Fresh Team Doctors", which hints at an external prescriber arrangement rather
  than a solo-owned book. Trading length not published.
- **Consent note:** no "no unsolicited commercial email" notice found.

---

## Group 2 — no email address published at all

These publish a phone number, an Instagram handle, or a contact form, and nothing else.
There is nothing for Jess to read in a browser either. Per the brief, no address was
constructed for any of them.

### The Injectables Queen — Erina & Charlestown NSW (Central Coast / Newcastle)
- **Site:** https://www.theinjectablesqueen.com/
- **Why it qualifies — and this one hurts:** the best dormant-list signal I saw all day.
  A paid annual membership, stated in their own words: **"Become a VIP Member for just $99
  annually"**, with a phone number given specifically "To Join" (0249431043). **Phorest** as
  the practice system. Gift cards sold through Phorest. Telisa is named as "Founder, Director
  and Head Queen" — a titled owner-founder. Two rooms (Erina, Charlestown), footer reads
  ©2020 so roughly six years trading.
- **Email status:** **none published.** No address, no mailto, not even an obfuscated one.
  Phone and booking links only. A paid membership list with no email route to the owner is
  the most frustrating combination in this batch.

### Skin Shore — West Wallsend NSW (Newcastle & Hunter Valley)
- **Site:** https://www.skinshore.com/
- **Why it qualifies:** two named owners, which is unusual — **"EBONNY: Senior Nurse Injector
  / Clinic Owner"** and **"CANDICE: Clinic Co-Ordinator / Owner / Laser Technician"**, with the
  site inviting people to "Come in and meet the sisters behind Skin Shore." Sister-owned,
  single site (68B Carrington Street, West Wallsend), Timely, gift vouchers. Explicitly says
  it uses "prescription-only medicines where clinically appropriate", so genuinely
  injectables-led. No skin cancer or Medicare service.
- **Email status:** **none published.** A contact form with an "Email (Required)" field for
  the visitor, but no clinic address, and not obfuscated either. Phone (02) 4967 5634 only.

### The Marr Clinic — Lennox Head NSW (Northern Rivers)
- **Site:** https://themarrclinic.com.au/
- **Why it qualifies:** a **"Rewards Points Program"** with its own terms page — banked points
  are a named dormant list. Timely. Dr May Marr named, with "the last 27 years" in skin.
  Single site at 42 Ballina Street, Lennox Head. No skin cancer or Medicare service listed.
- **Email status:** **none published.** Two conflicting phone numbers instead
  ((02) 6687 5202 in the header, (02) 6610 9707 in the footer).
- **Secondary caveat:** the practice reads closer to medical/dermatologic skin than
  injectables-led — the menu leads with lasers, peels, cryotherapy and intralesional steroid
  injection, with injectables mentioned only in "Our Approach". Even with an email it would
  have needed a judgement call.

### The Luxe Clinic — Warrnambool VIC
- **Site:** https://www.theluxeclinicwarrnambool.com/ (reached via a 302 from
  luxecosmeticinjectablesclinic.com)
- **Why it qualifies:** **"Owned and operated by Registered Nurse Lani"** — stated outright.
  Single site at 222 Timor Street, Warrnambool. Timely. "Gift Vouchers Available in Clinic".
  Footer ©2020, so roughly six years.
- **Email status:** **none published.** The site's own instruction is "Dm us on instagram" —
  exactly the phone-plus-Instagram-no-email pattern the task warned about. Call/text
  0421 272 452 or Instagram, nothing else.

### The Louve Skin Clinic — Geelong VIC
- **Site:** https://thelouveskinclinic.com.au/
- **Why it qualifies:** "owned by renowned Cosmetic Nurse Elly Seymour" — named owner — and a
  membership-shaped scheme called **"The Louve Society"** plus Gift Vouchers in the nav.
- **Email status:** **none published**, and no phone number either. Built on GoDaddy Website
  Builder with no contact details on the home page at all.
- **Note:** Geelong is already represented in the pipeline (Geelong Veins Skin & Laser, Lush
  Aesthetics Geelong), so this is a lower priority to chase.

### Skin Society Co — Belmont, Geelong VIC
- **Site:** https://skinsocietyco.com.au/
- **Why it qualifies:** "I'm Aubrey, the founder of Skin Society Co." Fresha as the practice
  system. Gift vouchers with real terms published ("Valid for 12 months, no refunds or
  returns on Gift Vouchers") plus a first-client offer, so there is a redeemable-credit list.
- **Email status:** **none published** — not obfuscated, simply absent. Phone 0421 124 145 only.

### The Cosmetic Studio Noosa — Noosaville QLD (Sunshine Coast)
- **Site:** https://thecosmeticstudionoosa.com.au/
- **Why it qualifies:** the best-verified trading history of any near-miss — **"Since 2014"**
  and **"Over 12 Years In Business"** in their own words. Timely, gift vouchers, Zip Pay
  buy-now-pay-later (so financed treatment courses). James Denton, Nurse Practitioner, named
  under a Medical Director model. No skin cancer, no Medicare.
- **Email status:** **none published.** Phone (07) 5447 4227 only. Twelve years of patient
  records and no email route to the owner.

### Bare Aesthetic — Sunshine Coast / Noosa QLD
- **Site:** https://bare-aesthetic.com/
- **Status: unreachable, not merely email-less.** The fetch returned metadata only — title,
  description and build tags, no rendered body. Nothing could be verified: no contact details,
  no owner, no locations, no policies. Logged here per the task's instruction not to fight
  the Sunshine Coast blockers. Services visible in the meta description are injectables-led
  and plausibly in-ICP, so it may be worth a browser look if the Sunshine Coast is revisited.

---

## Disqualified outright (not near-misses — recording so nobody re-sources them)

- **North Coast Medispa** (Ballina & Lismore NSW) — has "our on-site Dermatologist" and offers
  Photo Dynamic Therapy for "superficial types of skin cancer or pre-cancerous lesions", with
  skin cancer management through collaborative clinics including North Coast Dermatology.
  Dermatology-attached and not cash-pay-only. Also published no email.
- **Aesthetics by Tarah** (Toowoomba QLD) — https://www.aestheticsbytarah.com/ returns
  "This Account has been suspended." The only address on it is the hosting provider's
  `webmaster@` link, which is furniture, not a clinic address. Business may be gone.
- **Absolute Cosmetic** (Mandurah, Bunbury, Geraldton and more) — multi-site WA group, head
  office decides marketing. Over the cap.
- **Cosmetic Nurses Australia / Cosmetic Injectables Australia** (Brisbane & Darwin) — group
  structure across two brand domains with a central contact and booking funnel; reads as a
  head-office operation, not an owner-operator. This is also why **Darwin produced nothing**:
  the searchable Darwin aesthetic market is dominated by this group.
- **Queensland Plastic Surgery** (Townsville) — plastic surgery. **Cairns Dental Group** —
  dental. **The Cosmetic Lounge** (Wollongong page) — Sydney chain. **Artisan Clinics**
  (Toowoomba) — already on the ruled-out list.

---

## What this market taught me

Regional Australia delivers on the structural promise: nearly everything here is single-site
and owner-run, and I hit the owner-operator test far more often than a metro sweep would. The
problem is not qualification, it is **reachability**, and it fails in a very specific way.

The pattern is a town-sized business run from a phone. Three of the four best clinics I found
— a paid $99 VIP membership (The Injectables Queen), a sister-owned practice with two titled
owners (Skin Shore), a nurse-owner who states "Owned and operated by" outright (The Luxe
Clinic Warrnambool) — publish no email at all. Two of them tell you to DM Instagram instead.
These are not oversights; the owner genuinely runs the business through DMs and a mobile, and
the better the owner-operator signal, the likelier that is. The ICP and the email requirement
pull in opposite directions out here.

Cloudflare was the second tax, and it is the cheaper one to fix: four clinics (Nouvelle,
Dose of Envy, Naturaliste, Minnamurra) publish a real address that only a browser can read.
Nouvelle Cosmetics especially — named owner, trading since 2016, Timely, vouchers — is a
finished row waiting on one browser visit. I would hand those four to Jess before sourcing
anything new.

Three incidental things worth carrying forward. **Timely has effectively won regional
Australia** — it is the system on roughly two-thirds of these sites, so a lapsed-list export
story can be told once and reused. **Two live booking systems on one site** (Adorned, Laserclear,
Aesthetic Studio Bendigo) turned up repeatedly and is a tell for a half-finished migration,
which means lapsed names sitting unworked in the old system — a genuinely good opening. And
**Cairns massively over-indexes**: five of my accepted rows are Far North Queensland, which is
real market structure (an isolated city with no chain presence) but means the batch is
geographically lumpy, and two of those clinics share one building on Upward Street.

On the Sunshine Coast, the task's warning held exactly. One search returned almost nothing but
directory farms and `wheree.com` listing pages, and of the two real clinic sites it surfaced,
one was unreadable. I stopped after one query rather than burn fetches, as instructed. Darwin,
Townsville, Mackay and Rockhampton produced nothing usable at all — Darwin because one group
owns the search results, the others because search is US-weighted and simply did not return
local independents.

## UK near-misses — cities the September sweeps missed
Sweep run 19 Oct 2026. ICP v2 (owner-operated single-site injectables).

These clinics clear the ICP but publish **no email address I could read verbatim**, so none of
them went into `uk.json`. They split into two groups that need different handling.

---

## Group 1 — Cloudflare-obfuscated address (Jess can read these in her own browser)

The address is there, on the clinic's own page, but it renders as `[email protected]`.
Opening the page in a normal browser with JavaScript on will show it.

### CJA Aesthetics — Southampton, Winchester, Portsmouth
`https://www.cja-aesthetics.co.uk/` · 023 8033 2429
**The single best near-miss in this market — chase this one first.**
Why it qualifies: footer names the operating company as **"Run My Clinics Ltd trading as CJA
Aesthetics"**, so the sole-trader screen is already passed. Led by a named owner-doctor pair,
**Dr Chris Airey and Dr Lauren Airey**. Three sites (Southampton, Winchester, Portsmouth) — inside
the one-to-four band. And the dormant-list signal is the most explicit I saw anywhere in the UK:
two named membership tiers (**Standard Club** and **Premier Club**) with four LED facials a year,
product discounts and **a birthday voucher** — the clinic is already holding its members' birthdays
and unredeemed annual allowances. Gift cards sold on site too.
One flag before anyone writes to them: the group also runs **Arc TRT** (testosterone replacement,
on a separate domain), and TRT is on the brief's disqualify list. It is a sibling brand rather than
this clinic's menu, but it should be a conscious decision, not an oversight.
Status: **Cloudflare-hidden, not absent.**

### Harrogate Aesthetics — Harrogate, North Yorkshire
`https://harrogateaesthetics.co.uk/` · 01423 567567 · 12 Princes Square, Harrogate HG1 1LX
Why it qualifies: single clinic in the centre of Harrogate, "award winning medically led clinic",
full injectables and energy-device menu, separate men's and women's treatment pages.
Status: **Cloudflare-hidden, not absent.**
Two oddities worth knowing before Jess reads the address: the footer prints **two different company
numbers**, one of which is the literal placeholder `12345678` and the other `06184603`, and neither
is accompanied by a "Ltd" or "Limited" name. So even once the email is readable, the sole-trader
screen is unresolved — the real company number needs confirming. No owner is named on the site
either (only "Sharon" and "Anthea" in testimonials), and no membership or voucher scheme is
published. On current evidence it would come in as a C even with the address.

### Sheffield Aesthetics & Laser Clinic (SAL Clinic) — Sheffield
`https://salclinic.co.uk/` · 0114 327 5855 · 742 Ecclesall Road, Sheffield S11 8TB
The visible email link is obfuscated. An address does appear in the page's **meta tags**
(`meta-business:contact_data:email`), which is machine metadata rather than a published address, so
I have deliberately **not** recorded it — it is the same class of problem as a directory-supplied
address. Treat the email as unread.
Why it half-qualifies only: the site is a UENI template, names no owner ("our team of highly skilled
doctors"), states no trading length, and the navigation links to an **Islamabad clinic**, which makes
the one-to-four site count unverifiable. Lower priority than the two above.

---

## Group 2 — no address published anywhere I fetched

These need a phone call or a contact form, not a browser trick.

### Dr Fiona Steedman — Jesmond / Newcastle upon Tyne
`https://www.drfionasteedman.co.uk/` · 0191 260 5222 · St Nicholas Chambers, Amen Corner, NE1 1PE
The most frustrating miss of the sweep. The footer reads **"(c) 2026 by Dr Fiona Steedman Ltd."**
with **company registration number 12660943** — the cleanest corporate-subscriber verification I
found in any UK city, on a named owner-doctor, single-site, pure-injectables clinic (anti-wrinkle,
fillers, Mesotox, Profhilo, polynucleotides, skin boosters, SkinPen, PCA peels). It ticks four of the
five must-haves outright and still cannot be sent to, because there is **no email address on the
site at all**. Phone or the contact form only.

### CKS Aesthetics — Nottingham
`https://cksaesthetics.co.uk/` · 07950 633649
Footer reads **"(c) 2026 CKS Aesthetics Limited"** — sole-trader screen passed. Treatments delivered
by named nurses **Chantal Seera and Katie Haines**; "7+ years" of specialist experience; offers a free
anti-wrinkle or skin consultation. No email on the page and **no street address either**, so even the
site count is unverifiable. Worth a call.

### Winchester Medical Aesthetics — Winchester, Hampshire
`https://wmedicalaesthetics.co.uk/`
Founded by an "award-winning Aesthetic Nurse Specialist" named only as **Carolina**, on Winchester's
High Street. Runs **two named membership schemes — "The Founder Skin Club" and "The Anti-Wrinkles
Club"** — which is a textbook dormant-list signal. But the site publishes **no email, no phone and no
full street address**, and no company identity. Contact form only. Strong ICP, zero contactability.

### City Aesthetics Clinic — Newcastle upon Tyne
`https://www.cityaestheticsclinic.co.uk/` · 0191 260 38 62 · 5 Saville Place, NE1 8DQ
Single first-floor city-centre clinic, injectables-led, a "Prices, Special Offers & Vouchers" page in
the nav. No email, no company identity, no named owner (only "Book with Jane Gillies" in a menu
link). Also sells prescription weight loss, which dilutes the list.

### Novellus Aesthetics — Jesmond, Newcastle upon Tyne
`https://novellusaesthetics.co.uk/contact/` · 0191 695 0450 · 1 Benton Terrace, Jesmond, NE2 1QU
Single Jesmond clinic offering "complimentary, no obligation consultations" — a real dormant signal.
I fetched the contact page itself and the only "Email" on it is a form field label. No company
identity. One thing to check before any outreach: the copyright line reads **"(c) 2026 novellus
training"**, which suggests the main business may be a **training academy** rather than a patient
clinic — training businesses sell to practitioners, not to lapsed patients.

### LA Clinic UK — Burwell (Cambridge) and Helpston (Peterborough)
`https://www.laclinicuk.com/` · 01638 505982
Nurse-led, two sites, described as "an established aesthetic clinic". The email is behind a
JavaScript anti-spam wrapper that renders only as *"This email address is being protected from
spambots"* — so there is nothing to read even in a browser without interaction. No company identity,
no owner named beyond "Lily" in reviews.

### Skin Lab Cambridge — Cambridge
`https://skinlabcambridge.co.uk/`
Owner named outright — **"Amy, Skin Specialist / Owner"** — with nurse **Natalya** doing the
injectables, in one room at Chesterton Mill. Offers a free virtual consultation and runs named club
events ("Skin Lab Summer Club", "Skin Lab x Freckled Club"). Squarespace site with **no email, no
company identity** — two mobile numbers only. Also quite young: Natalya has specialised in
aesthetics since 2023.

### Skin&Spirit — Clowne / Chesterfield, Derbyshire
`https://skinandspirit.co.uk/` · 01246 570170
Footer reads **"Skin&Spirit Limited"** — screen passed — and it sells gift vouchers through its own
shop. But **no email on the page**, and the menu is extremely wide (hair services, nails, ear
piercing, counselling, hormone treatments, weight loss) so the patient list would be heavily diluted.
Chesterfield also sits outside the brief's named cities. Low priority.

---

## Also seen and deliberately not accepted

Recorded so nobody re-sources them:

- **The Cardiff Clinic** (Cardiff) — medical director is a **Consultant Plastic Surgeon**, and the
  menu includes breast and body surgery plus **skin cancer assessment and melanoma treatment**.
  Disqualified on two counts. Publishes `info@thecardiffclinic.co.uk`, so it would otherwise have
  passed the email test — do not let that tempt anyone.
- **The A Clinic** (Nottingham/London/Manchester/Birmingham, possibly Cannock) — **four to five
  sites** and the owner is a surgeon ("Owner and Surgeon at Liposhape", Vaser liposuction).
  Disqualified.
- **Dr Nancy** (Cardiff, London, Cowbridge, Bristol, Tetbury, plus Jammu and Lucknow in India) —
  **seven locations**. Head office decides marketing. Disqualified.
- **Muse Medical Clinic** (Harrogate) — `musemedicalclinic.co.uk/harrogate` **302-redirects to
  `whealthclinic.co.uk`**. The brief disqualifies anything whose domain redirects to another company.
- **Marlborough Clinic** (Belfast) — it is a **dental** practice (implants, aligners, endodontics)
  with dermatology attached, not an aesthetics clinic.
- **Mediaesthetics / Rebecca Rollett** (Leeds) — plastic surgery practice, and Leeds was already
  swept in September.
- **Cambridge Skin and Wellness** — looked ideal (Jane App, named doctor-and-nurse-practitioner
  partnership, gift cards) and is in **Cambridge, Ontario, Canada**. Out of market. The search
  engine's US weighting put it top of a UK query.
- **Beauty Within Medi Spa** (Cowbridge, Vale of Glamorgan) — publishes
  `info@beautywithinspa.co.uk` and has been trading since 1987, but the team page lists
  chiropractic, acupuncture, podiatry, ophthalmology and GP services alongside the aesthetics. That
  reads as a multi-specialty group, which the brief disqualifies. Park it; if the standard widens to
  allow host-practitioner spas it is a good one.
- **The One Clinic** (Leicester) — publishes `enquiries@the-oneclinic.co.uk` and has a Membership
  page, but its Medical Director is a **Consultant Plastic Surgeon** and the footer carries no
  company identity. Two strikes.
- **Cardiff Cosmetic Clinic** (Cardiff) — publishes `enquiries@cardiffcosmeticclinic.com`, Dr Raj
  Aggarwal, "Since 2010", one site, refundable consultation deposit. Held back because the menu
  lists **blepharoplasty and brow lift** and the footer carries no company identity. If someone
  confirms those are the non-surgical Plexr versions, this becomes a usable C.
- **Simply Be Beautiful** (Lisburn Road, Belfast) — publishes `simplybebeautiful@hotmail.com`, lead
  nurse Lisa Sloan, self-describes as a "busy very busy established Clinic". Held back on a hotmail
  address plus no company identity plus no published street address.
- **Skin Appeal Clinic** (Liverpool) — publishes `aestheticsliverpool@gmail.com`, nurse "Cornelius"
  with 27 years' experience, one site on Walton Hall Avenue. Held back: gmail address, no company
  identity, and the owner's surname is never given.
- **Aspire Aesthetics** (Aberdeen) — publishes `info@aspireaesthetics.co.uk` and sells a **"Client
  Prepayment Card"**, which is literally banked patient credit and exactly the signal the brief's
  wallet/bank/vault technique is hunting for. Held back because the site publishes **no address, no
  phone, no owner and no location count** — four of the five must-haves are unverifiable from it.
  Worth a second look by someone with more fetch budget.
- **JTMedical** (Liverpool) — publishes `infojtmedical@gmail.com`; "Ltd" appears only in the page
  title. No owner named, no address, no location count. Too thin.
- **Nikki Butler Skin Specialist** (Alton, Hampshire) — publishes two readable addresses, but the
  menu is skin-and-scar work with no injectables, and Alton is outside the brief's cities.

---

## What this market taught me

**The sole-trader screen is the whole game in the UK, and it is brutal.** Of the clinics I verified,
**sixteen had a readable email and a perfect ICP fit, and only eight of those printed any company
identity**. The pattern is consistent and worth exploiting: a UK aesthetics clinic's homepage footer
almost never names the entity — it names the web designer. The company identity, when it exists,
hides in the **privacy policy** (Dr Bonny → "B.Aesthetic Ltd."), in a **"T/A" line** (The Clinic
Norwich → "Joolia Gilvey Ltd T/A The Clinic"), or in a **finance-broker disclosure**. For the next UK
run: budget one extra fetch of `/privacy-policy/` per candidate before grading, because that single
fetch is what separates a sendable B from a parked C. It flipped Dr Bonny from C to B in one call.
Conversely, the footer that *does* carry a company number often belongs to a clinic with **no email
at all** (Dr Fiona Steedman Ltd, CKS Aesthetics Limited, Skin&Spirit Limited) — the two
qualifications seem almost anti-correlated, as if the tidier operators route everything through a
form.

**The inversion of the standard is real and it changes who the good leads are.** The best rows in
this batch are not the polished multi-site groups September was chasing; they are HGface, where the
doctor writes *"the clinic is just me and I am my own receptionist!"*, and Skin Aesthetix, where one
injector covers Aberdeen three days and Elgin on Fridays. Both have the problem the offer solves
written on the page.

**Three technique notes.** (1) `WebSearch` is heavily US-weighted even with UK cities stacked — a
Cambridge query returned a clinic in Cambridge, *Ontario*, and a "beauty bank" query returned ten US
med spas and not one British clinic, so the wallet/bank/vault trick from the AU run **does not
transfer to the UK**. (2) What did work was stacking city names with the literal string `"Ltd"` plus
"membership" — that is how Innersense, HGface, The Aesthetics Hub and CKS surfaced, and it
pre-filters for the screen. (3) Fetching the **memberships page instead of the homepage** was the
highest-yield single call: it carries the email, the owners' names and the scheme in one go.

**One new fabrication trap, beyond the two in the brief.** `salclinic.co.uk` serves a real-looking
address inside its **Open Graph / business meta tags** while the visible mailto is obfuscated. That is
machine metadata, not a published address, and recording it would be the same error as reading one
off a directory. I did not record it. Also watch for **mismatched domains**: Blend prints
`@blendskinandaesthetics.co.uk` in the header and `@blendskinandbeauty.co.uk` in the footer mailto,
The Skin Firm publishes `info@theskinfirm.NET` from a `.co.uk` site, and Leicester Medispa publishes
`info@leicestermedispa.UK` from a `.co.uk` site. All three are what the page says. The instinct to
"tidy" them into matching the website domain would fabricate an address.

## US interior metros — near misses (19 Oct 2026)

Clinics below clear the inverted ICP (injectables-led, cash-pay, owner-operated, one to four
sites, established) but **publish no email address I could read verbatim**. Each entry says
whether there is **no address at all** or a **Cloudflare / JS-obfuscated** one — Jess can open
the obfuscated ones in her own browser and read them; the others need a phone call or a form.

Market: Kansas City, St Louis, Minneapolis–St Paul, Omaha, Des Moines, Madison, Pittsburgh,
Louisville, Memphis, New Orleans, Oklahoma City, Tucson.

---

## No published address at all (form and phone only)

### 1. Metropolitan Skin Clinic — Edina, MN (Minneapolis metro)
https://metropolitanskinclinic.com/ · contact page: /contact-us/
**The best lead I had to drop.** **Suzanne St. James is listed in plain text as
"Injector/Co-Owner"** — a named owner-injector, which is exactly the buyer. Runs on **Zenoti**
(metropolitanskin.zenoti.com webstore). Single Edina site, "15+ years of experience". Deep
injectables and laser menu (BBL, Halo, Moxi, SkinPen with PRP). Has "Treat Now, Pay Later" and
a "Programs" page.
**Why dropped:** I fetched both the homepage and /contact-us/. Neither carries an email — only
a form with an "Email*" field. Nothing obfuscated, just absent. Would be an A row on a phone
call.

### 2. Scout Aesthetics — Louisville, KY
https://www.scoutaesthetics.com/ · contact page: /contact
Lead injector **Jennifer Fick, DNP**, FNP with advanced and master's injector training. Single
Herr Lane site. Two named memberships (The Scout, The Glow Getter) and — the detail that makes
it valuable — the site says **membership dollars are "retained as an account credit"** for
future treatments. That is a named list of people holding unspent balances.
**Why dropped:** homepage and /contact both carry only the phone number (502) 576-7710 and a
form. No address, obfuscated or otherwise.

### 3. Metro Medspa — St Louis, MO
https://www.metromedspa.com/ · memberships: /memberships/ · contact: /contact/
Seven membership tiers, and the injectable and "Skinjectable" tiers explicitly **bank the
membership fee into a "Beauty Bank"**. Runs on **MyPatientNow** (book.mypatientnow.com).
Member perks extend to 14 partner businesses across St Louis, so this is an embedded local
operator, not a new arrival.
**Why dropped:** fetched both /memberships/ and /contact/. The contact page publishes no street
address and no email — only a city and ZIP (63128). Phone and text only. Location count never
stated either, which is a second thing to check.

### 4. A Beautiful You Medical Spa — Memphis, TN
https://www.abeautifulyoumedicalspa.com/aesthetics-center-in-memphis/
**The longest tenure I found in Memphis.** JL and Lorrie Fisk bought the Memphis (and Little
Rock) Sona MedSpa locations in **2005** and rebranded 11 years later; the page says 20 years of
operation. Medical director Dr Kenneth Thompson; Megan Stewart, board-certified FNP and
aesthetic NP. Memberships and financing are linked.
**Why dropped:** no email anywhere on the About page, footer included. Also needs a location
count check — they bought a Little Rock site in 2005 and image captions mention Collierville and
Germantown, so this may be a multi-site group.

### 5. a.dore Med Spa — Elkhorn, NE (Omaha metro)
https://www.adoremedspaomaha.com/
Publishes the **"a.dore SAPPHIRE Beauty Bank"**, a monthly membership — a textbook banked-credit
dormant list, found exactly by the wallet/bank/vault search. Single Elkhorn site. Kristen Hammes,
APRN, named in a photo caption.
**Why dropped:** fetched /injectables-omaha and /contact. Neither carries an email; the contact
page is remarkably bare (no address, no owner, no year).

### 6. Skin Artisans — Edina / Minnetonka / Woodbury, MN (Minneapolis metro)
https://skinartisans.com/
Three sites, so inside the one-to-four rule. Runs on **NextPatient**. Named CANS-certified
injection specialist (Jennifer Jeansson RN, CANS). "Rewards Programs", financing and a monthly
newsletter.
**Why dropped:** no email in the page content. Also no owner named, and the menu carries BIOTE
hormone therapy and diVa vaginal laser, which pushes it toward the functional-medicine edge.

### 7. Euphoria Health & Med Spa — Elkhorn, NE (Omaha metro)
https://euphoria.health/
HydraFacial memberships at a published monthly rate, gift cards, payment plans. Single site.
Phone 402-957-6363. Booking runs on MyAestheticsPro.
**Why dropped:** no email; the only "Email" on the page is a form label and a newsletter prompt.
Owner not named either.

### 8. Ageless Skin Co — Omaha, NE
https://www.agelessskinco.com/
Runs on **Boulevard** (dashboard.boulevard.io). Claims "8+ Years Experience", so established.
Injectors Liz and Melissa named in reviews, one called a nurse injector.
**Why dropped:** no email at all, and no membership or loyalty scheme — packages and financing
only. Thinner than the rest of this list even if an address turns up.

### 9. Telos Medical Aesthetics — Metairie, LA (New Orleans metro)
https://telosmedicalaesthetics.com/
Single Athania Parkway site, device-led aesthetics menu (AgeJET, Denza RF, ADVATx, AlloraPro).
**Why dropped:** no email, no owner named, no membership, no founding year — nothing to build an
opening line on even with an address. Lowest priority on this list. Peptides, medical weight loss
and hyperbaric therapy also push it toward the functional-wellness disqualify.

---

## Obfuscated address (Jess can read this one in a browser)

### 10. Great Skin KC — Kansas City, MO
https://greatskinkc.com/contact/
The contact page renders its address as **`in**@*********kc.com`** — masked, so by the brief's
rule **NOT SEEN** and not recorded. Readable in a browser.
**But do not chase it:** it **disqualifies on two counts anyway** — **four locations** (Ward
Parkway KC MO, Liberty MO, Lenexa KS, Overland Park KS, with a head-office shape), and the
service menu includes **plastic surgery** (blepharoplasty, facelifts, tummy tuck) plus hormone
therapy, menopause and sexual wellness. Logged here only so nobody re-finds it and thinks the
masked address is the only problem.

---

## What this market taught me

The wallet/bank/vault search is genuinely the right first move in the US — it is how I found
Divine Radiance's "Divine Beauty Bank" in Kansas City, L3's "Beauty Bank" in Oklahoma City,
Beauty Lounge's in Tucson, a.dore's "SAPPHIRE Beauty Bank" in Omaha and Metro Medspa's in St
Louis. Every one of those holds named patient credit. But it is a **thin** vein in the interior:
it returned one or two results per metro and then dried up, where a plain metro-plus-membership
search returned ten. Past Tucson and Kansas City I got more mileage from stacking suburb names
(Leawood, Overland Park, Elkhorn, Middleton, Metairie, Cordova) with "membership" and "nurse
injector", exactly as the 18 Oct Australian note suggested.

Two things are structurally different from the AU and UK runs. First, **email publication is the
binding constraint, not the ICP**. Nearly every clinic I opened was owner-operated, single-site,
cash-pay and injectables-led — the inverted standard is easy to meet here. What US med spas do
not do is publish an address: they publish a form, a phone number and a text-us link, because
booking is the only funnel they care about. Half my drops were on email alone, and the single
best lead in the whole sweep (Metropolitan Skin Clinic, with a named Injector/Co-Owner on Zenoti)
died on exactly that. Fetching /contact/ was often *worse* than the homepage — the footer is
where US addresses live, when they live anywhere.

Second, **founding dates are almost never published**. Fourteen of my eighteen rows have no year
opened; "established" had to be inferred from footer copyright, a membership ladder, a device
stack or a stray testimonial. Only Skin Medics ("Trusted Since 2002") and A Beautiful You (bought
2005) actually say. KSD Aesthetics and The Beauty Haven are the two accepted rows I would check
for review history before sending, because both could be two years old.

Third trap worth recording: **gmail addresses are the norm, not a red flag.** Five accepted rows
publish a gmail or a first-party gmail-style address in the footer (L3, Reveal, The Aesthetic
Place, Spa MD, Face KC) and one site publishes *both* a branded address as visible text and a
gmail as the mailto target (Aesthetically Pleasing). I recorded the visible text in that case.
I also hit the metadata-author trap the brief warns about in a new form: l3aesthetics.com carries
`hibbtd@gmail.com` in its page metadata as the "Written by" author — that is the web designer,
not the clinic, and I did not record it. And confidentbeautymedspa.com publishes
`info@confidentbmedicalspa.com`, a *different* domain from the site it sits on — real, read
verbatim, but it tells you the owner has moved domains at least once. That clinic is in Pikeville,
not Louisville, so it fell outside the market and is not in the JSON.

Finally, the four-site ceiling bit once. OWN Aesthetics in West Des Moines looks like a single
clinic until you read the navigation, which carries three location pages (Des Moines, West Des
Moines, Waukee). It is still inside the rule, but it is the row to re-count. Great Skin KC was
the only outright five-plus-shaped group I hit, and it disqualified on plastic surgery too.

---

# Canada and the US secondary metros — 20 Oct 2026

Thirty-four rows (ids 463-496), 31 of them sendable, plus nine British clinics rescued out
of this file's own parked list by checking the registers instead of their websites.

**Canada is a better market than the US for this, and nobody had looked.** The whole list
held four Canadian clinics before today, two of which were disqualified the same morning.
Only 4 of 22 Canadian clinics examined published nothing, against roughly half in the US.
**Jane App is the default platform** — 12 of 22 — and founding years are sometimes actually
published, which they almost never are in the US. **A Gmail address on the clinic's own page
is normal in Canada**: five of the sixteen accepted rows are Gmail, which satisfies CASL's
conspicuous-publication test, because the test is where an address is published, not what
domain it sits on.

Canada also produced a new tell worth reusing: **a loyalty scheme branded for a parent
company** is how you spot a clinic whose marketing is decided elsewhere. It caught two
clinics that otherwise looked owner-operated. And obfuscation is not always Cloudflare — one
site hand-rolled `aesthevaclinic[@]gmail.com`, which is still an address we have not seen.

**In the US secondary metros the fit is easy and the address is everything**, same as the
interior sweep. Of roughly 35 clinics opened, nearly all passed on profile; thirteen publish
no address at all and two are Cloudflare-masked. **Spokane and Wichita were unusually
productive** — five rows between them — so the Pacific Northwest and the Plains are the best
next ground. **Albany, Syracuse and Toledo produced nothing emailable at all**, and
Birmingham and Bakersfield one thin clinic each; the route into those is Jess opening three
pages in her own browser, not more searching.

**Two search findings that should change how the next sweep starts.** Passing
`blocked_domains` for the directory farms was the single biggest lever in both sweeps —
before blocking them, nine of ten results were directory pages and no clinic domain surfaced
at all, so do it first rather than as a refinement. And `/contact` was again *worse* than the
homepage: every accepted US address came off a homepage or About-page footer.

**One domain has changed hands.** `19westaesthetics.com` in Dayton now serves an unrelated
AI companion app. Worth remembering that a dead clinic domain does not always 404; sometimes
it answers as something else entirely.


## US secondary metros — near misses (20 Oct 2026)

Market swept: **Buffalo and Rochester NY, Albany NY, Syracuse NY, Harrisburg and Allentown PA,
Toledo and Dayton OH, Lexington KY, Knoxville and Chattanooga TN, Birmingham and Huntsville AL,
Tulsa and Wichita, Fresno and Bakersfield CA, Spokane WA.** Every metro listed as already covered
was avoided; where a search dragged in an out-of-market clinic it is recorded below so nobody
re-finds it.

Clinics here clear the v2 ICP on profile (injectables-led, cash-pay, owner-operated, one to four
sites) but **publish no email address I could read verbatim**, or publish one and fail a different
must-have. Each entry says which. **Never construct an address for any clinic on this list.**

> **Note on the brief.** `BRIEF.md` was not present at the path given
> (`.../scratchpad/au-sweep/BRIEF.md` — the whole `au-sweep` directory was missing), so I worked to
> `outputs/pipeline/ICP.md` v2 (16 Oct 2026) as the qualification standard, the no-constructed-address
> rule from it and `.claude/skills/outreach-daily/SKILL.md`, and the 27-column row shape of the
> 19 Oct US rows in `outputs/pipeline/clinic-pipeline.csv`. `email_source` is dated 20 Oct 2026.
> Anything the brief said beyond those sources was not available to me.

---

## Group 1 — Obfuscated address (Jess can read these in her own browser)

### Medical Spa Buffalo — Orchard Park / Amherst / Depew, NY
https://medicalspabuffalo.com/ · team: /meet-the-team/
The footer address renders as **`[email protected]`** — a Cloudflare artifact, so by the rule it is
**NOT SEEN** and not recorded. It is readable in a normal browser.
**Why it is worth the browser trip:** **Matthew Bailen, DHSc, MSN, RN, is named in plain text as
co-owner**, with Dr Jay Park, MD, a DMS PA-C and a second PA on the team. Four site listings across
three towns (Orchard Park, Amherst, and two suites in Depew — injectables/laser and esthetician
split across the same Terrace Blvd address), so it is inside the one-to-four rule on
decision-makers. Booking runs on **MedspaCircle** (go.medspacircle.com) and the footer calls itself
a "MedspaCircle.com Network" site. Dormant pools: a monthly membership page, a **weekly giveaway
entered by joining the newsletter** (a named opt-in list), a free-consultation offer and an e-gift
card store.
**Caveat before sending:** count the Depew suites properly — if they are two separate businesses
rather than one split site, the structure needs re-reading.

### PSA MedSpa (Pearl Skin Aesthetics) — Huntsville, AL
https://psamedspa.com/
Cloudflare-obfuscated in the header, the contact section and the footer — all three render
`[email protected]` and the links are `/cdn-cgi/l/email-protection#...` paths. **NOT SEEN.**
Single Church Street NW site. Booking on **Meevo**. Memberships page and gift-cards page both
linked, plus a complimentary consultation attached to a prepaid treatment offer. No owner named
anywhere, and no founding year. Would be a B on a browser read, not an A, because the buyer is
unidentified.

---

## Group 2 — No address published anywhere I fetched

### 1. Victoria Aesthetics — Clifton Park, NY (Albany metro)
https://www.victoriaaesthetics.com/
**The best lead I had to drop, and the only Albany-area prospect worth anything.**
**Victoria Gondar, NP** is named as the practitioner and the practice is her personal brand. One
Clifton Park site (Albany and Saratoga are service-area keywords only). Booking on **Aesthetic
Record**. The dormant signals are unusually good: a **Patient Rewards page**, e-gift cards, free
consultations, CareCredit, and a past promotion giving **tenure-based discounts scaled by how many
years you have been a patient** — which means the clinic already segments its list by recency.
An Instagram post says "celebrating FIVE years in business", so roughly five years trading.
**Why dropped:** no email in the page content, obfuscated or otherwise. Form and phone only.

### 2. Luxe Lounge Medspa — Lexington, KY
https://www.luxeloungemedspa.com/ · contact: /contact/ · the prize page: /about/luxe-beauty-bank/
**The best banked-credit signal in the sweep that I could not email.** The navigation carries a
page called **"Luxe Beauty Bank"** — found exactly by the wallet/bank/vault search. Two
owner-injectors are named: **Jenny Ash, RN** (owner, certified master injector) and **Alyssa
Fleming, FNP-C** (owner and medical director); the meta description names a third owner, Grace
Mullins, MSN. One Chevy Chase site. **Aesthetic Record** booking, Square gift cards, financing.
The site states **"5.0 stars from 521+ Reviews"**, the firmest established proxy of anything here.
**Why dropped:** I fetched the homepage AND /contact/. Neither carries an email — the contact page
publishes the address and phone only. Nothing obfuscated, just absent.
**If Jess opens one page from this file, make it this one.**

### 3. Odara Medical Spa — Spokane, WA
https://www.odaramedicalspa.com/about
**Founded in 2018 by Jaime Crocker, MSN, ARNP, FNP-C** — the site says so outright, which makes it
one of the only clinics in the sweep with a **published founding year and a named owner-injector**
at once. One N Lincoln Street site. "Odara Memberships" in the navigation, plus payment plans.
**Why dropped:** no email on the About page. Booking is an on-page anchor, so no practice system
could be identified either. Converts straight to an A row if the address can be read.
**Minor note:** a staff bio (Brittany Martin) mentions practising in facial plastic surgery — that
is her history, not the clinic's menu.

### 4. Old City Med Spa — Knoxville, TN
https://oldcitymedspa.com/about/
One W Summit Hill Drive site. **Katelyn Wetherington, FNP**, is an AANP board-certified Advanced
Nurse Injector; supervising physician **Dr Mark Davenport, MD, with 35 years in East Tennessee** —
the strongest tenure evidence in Knoxville after KnoxGlow. Dormant pools: a membership programme
the site says discounts up to half of regular prices, gift cards, and a free consultation. Shop
runs on **Mindbody**.
**Why dropped:** no email anywhere on the About page, footer included. No owner named either.

### 5. Flawless Aesthetics Med Spa — Chattanooga, TN
https://www.flawlesschattanooga.com/ · provider: /lindsay-bright
**Lindsay Bright, FNP-C**, founder, with two more providers and an esthetician. One Airpark Drive
site. Booking on **Boulevard**. A new-patient offer plus a complimentary consultation with skin
analysis, and payment plans.
**Why dropped:** no email on the homepage, and **`/contact` returned a fetch error**, so one page
is genuinely unchecked. This is the one in this group most likely to be a false negative — worth
a browser look at the contact page before writing it off.

### 6. Lavender Medi Spa — Chattanooga, TN
https://lavendermedispa.com/about/
**Sharlotte Manley, FNP-C**, founder and nurse injector, under the medical direction of Dr Sujay
Kumar. One Mackey Branch Drive site. **Aesthetic Record** booking, a **Rewards page** in the
footer, gift cards sold online, and a free consultation.
**Why dropped:** no email on the About page. No founding year and no review count either, so
"established" would have had to be inferred even with an address.

### 7. Glow Spa Buffalo — Williamsville, NY
https://glowspabuffalo.com/injectable-services/
**Jessica Hafezi, DNP, FNP-BC**, ANCC board-certified, is the injectables specialist. One Harris
Hill Road site. **Aesthetic Record** booking, Cherry financing, and both a Membership page and a
Gift Cards page in the navigation.
**Why dropped:** no email in the page content. No owner named — Hafezi is described as the
specialist, not the principal — so it would have been a B anyway.

### 8. Smart Skin Med Spa — Homewood and Hoover, AL, plus Franklin, TN
https://smartskinmedspa.com/
Three sites, so inside the one-to-four rule. **Three named membership tiers (Silver, Teal and
Diamond)** differing by monthly services included, plus gift cards and payment plans. Booking runs
on **Revique** (admin.revique.io) with a treatment-builder virtual consult tool.
**Why dropped:** no email at all, and **no owner or practitioner is named anywhere** — with three
sites and no identifiable buyer, this is the shape the standard warns about (a group run by a
marketing manager rather than an owner). Hormone replacement and vaginal rejuvenation also sit on
the menu.

### 9. Society Wellness and Skin Spa — Vestavia Hills, AL (Birmingham metro)
https://societywellnessandskinspa.com/
One Montgomery Hwy site. Booking on **PatientNow**. Dormant pools are real: "loyalty rewards",
"VIP membership programs", and complimentary consultations for all new clients.
**Why dropped:** no email, **no owner or practitioner named** (only "licensed medical
professionals"), and the tenure claims contradict each other on the same page — "25 Years",
"10+ Years Service" and "25+ Years". Its FAQ also notes some medical weight-loss programmes **may
qualify for insurance**, which is the cash-pay must-have wobbling.

### 10. MD Aesthetics — Bixby, OK (Tulsa metro)
https://mdaestheticstulsa.com/about/
**Two named owners**, which is unusual and useful: **Karma Hefner, MBA**, nurse and Master
Aesthetic Instructor, founder, and **Nicole Atkinson, RN, BSN**, Master Nurse Injector, co-owner.
One Bixby site (the site says "the heart of Tulsa"; the address is Bixby). Booking on **Vagaro**.
Hefner also runs a training academy.
**Why dropped:** no email on the About page. **No membership, loyalty or gift-card scheme either**,
so the dormant signal was thin even before the address problem.

### 11. Blush Aesthetics — Perrysburg, OH (Toledo metro) and Columbus, OH
https://blushnwo.com/
Family-owned, **Erin Hennessey** named as founder. Runs on **Zenoti** (cpp.zenoti.com, with its own
Zenoti-built app), memberships for weight management and skin, and Zenoti gift cards.
**Why dropped:** no email, no mailto, nothing obfuscated — only Instagram handles. **Also partly
out of market:** one of its two sites is in **Columbus, which is already covered**, and no
credential is published for the founder.

### 12. Herrington Aesthetics — Huntsville, AL
https://www.herringtonaesthetics.com/
**Dr F. Stephen Herrington, MD**, Family Medicine and Aesthetics, University of Alabama trained,
former chair of Huntsville Hospital's Family Practice department, nearly four decades caring for
Huntsville families.
**Why dropped, twice over:** no email in the portion of the page I could fetch (**the page was
truncated before the footer, so the footer is genuinely unchecked**), and more importantly he is
**MDVIP-affiliated** — a concierge primary-care membership on top of a family-medicine practice,
which puts insurance billing and a much heavier privacy regime in the room. Probably a
disqualification on profile, not just contactability. Do not spend more time here.

### 13. Lovely You Aesthetics — Rochester, NY
https://lovelyyouaesthetics.co/
**Nothing readable at all.** The fetched page is a title, a logo and the practice name — no
services, no team, no address, no contact. A JavaScript-only build. Logged so nobody re-fetches it
expecting content.

---

## Group 3 — Publishes an email, but parked at grade C (did NOT go in the JSON)

These five publish a verbatim address and are recorded so nothing is re-researched, but each fails
a must-have or has a dormant signal too thin to open on. Per the ICP they are parked, not dropped —
the standard may widen.

### ONYX Aesthetics and Wellness — Bakersfield, CA · `info@onyxaw.com`
https://www.onyxaw.com/ — read verbatim as visible text in the Contact section, 20 Oct 2026.
Physician-owned and operated, **Richard H. Rawson, DO, FAAFP**, one Brimhall Road site, staff
averaging ~30 years in aesthetics. **Parked because:** there is **no membership, loyalty, gift-card
or banked-credit scheme of any kind** (Cherry financing only), **no booking or practice-management
system identifiable**, and no founding year — so there is no dormant list to name and nothing
specific to open on. Telehealth, hormone replacement and weight loss also pull it toward the
functional-wellness edge. **This was the only emailable Bakersfield prospect I found**, so if the
dormant-signal bar ever drops, promote this one first.

### Il Mulino Aesthetics — Williamsville, NY (Buffalo metro) · `aesthetics@weareilmulino.com`
https://www.ilmulinoaesthetics.com/ — read verbatim as visible text twice (general-enquiries
section and footer), 20 Oct 2026.
One Main Street site, booking on **Boulevard** (joinblvd.com), and it runs an injector
certification academy. **Parked because:** **no owner is named** (care is "under the medical
direction of Dr Jafar Siddiqui, MD, FAAPMR, DABPM" — a physical-medicine and rehabilitation
specialist, not an aesthetics owner), and there is **no membership, loyalty or gift-card
programme** — only undescribed "Packages" and payment plans. Nothing to recall and nobody
identified to recall it to.

### Replete Aesthetics + Wellness — Allentown, PA · `info@repleteaesthetics.com`
https://repleteaesthetics.com/ — read verbatim as **visible footer text**, 20 Oct 2026.
**Dr Cecilia Bermudez, DNP, CRNP**, one W Tilghman Street site, **Aesthetic Record** booking,
"5+ years of experiences". **Parked because:** **no membership, loyalty, rewards or gift-card
scheme at all**, and the menu leads with IV therapy, hormones and weight loss rather than
injectables — functional wellness with an aesthetics line attached.
**Worth recording separately:** the visible footer text says `info@repleteaesthetics.com` but the
**mailto target behind it is a different address on a different domain**
(`replete.wellness@gmail.com`). Both were seen verbatim; following the 19 Oct precedent I recorded
the visible one. A mismatch like that usually means the branded inbox is unmonitored.

### Azia Medical Spa — Birmingham, AL · `theaziaexperience@gmail.com`
https://aziamedispa.com/ — read verbatim as visible text in the Contact Us section, 20 Oct 2026.
One Narrows Pkwy site, footer copyright 2021. **Parked because:** **no owner or practitioner is
named anywhere**, **no booking or practice-management system is identifiable**, and there is **no
membership, loyalty or gift-card programme** — payment plans and a nutraceuticals shop only.
Hormone replacement, massage and spray tanning dilute the injectables focus. **This was the only
emailable Birmingham prospect I found.**

### Dr Buffalo Medspa & Surgery — Clarence, NY (Buffalo metro) · `info@doctorbuffalo.com`
https://doctorbuffalo.com/ — read verbatim, 20 Oct 2026.
Genuinely good dormant signals — a membership programme, SalonVision gift cards, and booking on
**PatientNow** (na02.patientnow.com) — and a single Clarence site.
**Parked because the profile is wrong:** the founder, **Dr Armen Kirakosyan, is a triple
board-certified urogynecologist**, the trading name includes **"Surgery"**, and **cosmetic
gynecology** is on the menu. That is a surgical, multi-specialty practice with a specialty that
normally bills insurance — the opposite of the cash-pay, injectables-led, owner-injector profile.
Do not promote this one without asking the insurance question first.

---

## Disqualified outright — do not re-source

**Plastic surgery or dermatology attached (a v2 disqualification):**
- **Spa One** — Albany, NY. Publishes `general@spaonemedspa.com`, so it is contactable, but it
  trades as **"Spa One at The Plastic Surgery Group"** with a team of board-certified plastic
  surgeons. Out on profile, not on contactability.
- **Q the Medical Spa** — Rochester and Victor, NY. Owner and medical director **Vito C. Quatela,
  MD, FACS**, a facial plastic surgeon; the spa is the non-surgical arm of the Quatela Center for
  Plastic Surgery. Also publishes no email. Its membership is the most interesting one I saw —
  a 12-month scheme that **credits the shortfall to the patient** if they do not save at least the
  membership cost — but the practice is out.
- **Revitalize Aesthetics** (Theresa Setter, NP Family Health PLLC) — Fayetteville, NY (Syracuse
  metro). Trades as **Revitalize Dermatology & Aesthetics**, offers skin-condition diagnosis and
  full skin cancer screening, runs **Klara and EMA** (a clinical EMR), and posts a notice that it
  stopped participating with insurance companies directly from 1 July 2024 — i.e. it billed
  insurance until recently. Out on dermatology and billing history.
- **ADA Aesthetics** — Perrysburg and Toledo (Sylvania), OH. Explicitly "the Medi-Spa division of
  **Dermatology Associates Inc**", working under that practice's physicians. Also no email.
- **Bella Via Medical Spa** — Toledo, OH. Aesthetic specialists supervised by **board-certified
  plastic surgeons** ("Reconstructive and Aesthetic Surgeons"), three named MDs. Also no email
  (the "Email Us" control links to a form). **Worth recording for the pattern, though:** it
  publishes the richest banked-credit scheme found anywhere in this sweep — a tiered units club
  that **banks unused monthly units**, grants bonus units on the member's one-year anniversary, and
  layers the manufacturer's points programme with an **online wallet** on top. That is precisely
  the dormant structure the offer is built for; it is just attached to the wrong kind of practice.
- **Haus of Beauty Medical & Aesthetics** — Homewood, AL (Birmingham metro). Publishes
  `hausofbeautybhm@gmail.com` and has strong memberships, but the medical menu includes
  **dermatology appointments, skin cancer screening, urgent care and house calls** under an
  emergency-medicine physician. Multi-specialty medical, not a cash-pay med spa.

**Chains, franchises, groups and head-office marketing (5+ sites or a franchise model):**
VIO Med Spa (franchise, Toledo among others) · Monroe MedSpa (Buffalo, Rochester and Syracuse
sub-sites off one brand) · Rejuvn8 (multi-metro plus its own academy) · Smiley Aesthetics
(Chattanooga, Knoxville and beyond) · Curate MedAesthetics · Face Forward Aesthetics ·
**Princeton Medspa Partners** (Huntsville — PE-backed roll-up, recruiting through a jobs board) ·
Infinity Med-I-Spa / med-i-spa.com (locations page) · Mobo Med Spa (Sylvania) · Jiva Med Spa
(Dayton and Cincinnati) · Chapter Aesthetic Studio · Skin Aesthetics Med Spa (Harrisburg location
page) · Orr Salon & Med Spa and Hobbs Salon + Med Spa (salon-led, Tulsa).

**Domain no longer belongs to the clinic:**
- **19 West Aesthetics** — Dayton, OH. `19westaesthetics.com` now serves an **unrelated AI
  companion app**, not a med spa. Disqualified under "practices whose domain redirects to another
  company". Logged so nobody fetches it again.

**Out of market (surfaced on an in-market search — do not count these as coverage):**
- **Inject Wellness** — **Montrose, CO**, not Rochester NY, despite ranking for a Rochester query.
  It publishes `info@injectwellness.com` and is otherwise a clean fit (**Jana Faragher, FNP-C, DNP,
  Owner and Clinician**, single site, **Aesthetic Record**, memberships linked). Colorado is
  already-covered ground, so it is not in the JSON — but it is a real prospect if the market ever
  reopens.
- **A Beautiful You / New River MedSpa (Huntsville, *Tennessee*)** — a different Huntsville from
  the Alabama one; ignored.

---

## What this market taught me

**The 19 Oct finding held exactly: email publication is the binding constraint, not fit.** Of the
~35 clinics I opened, almost every one was owner-operated, single-site, cash-pay and
injectables-led — the inverted v2 standard is easy to meet in US secondary metros. What killed
prospects was publication: **13 otherwise-good clinics publish no address at all** and two more
hide it behind Cloudflare. US med spas publish a form, a phone number and a "text us" link because
booking is the only funnel they care about.

**The footer is the whole game, and /contact is still usually worse than the homepage.** Every
single accepted row's address came from a footer or a contact block on the **homepage** or an
**About** page. The two clinics where I fetched a dedicated `/contact/` page as well (Luxe Lounge,
and Flawless Chattanooga before it errored) gave me *less* than their homepages. Fetch the homepage
and the About page; only fetch /contact as a last resort.

**The wallet/bank/vault search works, but it works indirectly.** Searching the phrase plus a metro
name returned mostly **vendor marketing blogs** (RepeatMD, PatientNow, Mangomint, Prospyr all
publish "how to build a beauty bank membership" content that outranks every clinic). The phrase
still earned its place, though — it is how I found **CC Aesthetics' "CC Beauty Bank"** in Lexington
(accepted, grade A, and the best dormant signal in the batch), **Luxe Lounge's "Luxe Beauty Bank"**
(dropped on email), **The LAB's unit-banking membership** in Spokane (accepted) and **Bella Via's
units club** in Toledo (disqualified). Lead with it, but expect to find the clinics via a
*different* route and then recognise the bank when you land on the site.

**What actually generated candidates: blocking the directories.** The single biggest efficiency
gain this sweep was passing `blocked_domains` for the aggregators — practicefinder.newpatientsinc.com,
lantern.llc, fresha.com, portraitcare.com, vagaro.com, threebestrated.com, medspascout.com,
thecliniccompass.com, poyst.com, buoyhealth.com, whelth.com — plus the job boards (careerplug,
rippling, ziprecruiter, glassdoor) and the business-for-sale sites (bizquest, pitchbook). Before
blocking, 9 of 10 results were directory or recruitment pages and no clinic domain surfaced at all.
After, nearly every result was a clinic's own site. **Do this first on the next US sweep.**

**Founding years are almost never published — confirmed again, and worse than last time.** Only
**two** of my 16 accepted rows state tenure: KnoxGlow ("owned the practice since 2006") and Chief
Aesthetics ("founded 2018"). For the other 14 I said so plainly in `notes` rather than asserting
"established", and used whatever proxy existed: a stated review count (Crafted Beauty 680+,
Refyned 500+, Luxe Lounge 521+ among the near-misses), a footer copyright year (Nouveau 2020,
SkinWell 2024), a membership ladder, or a device stack. **Four accepted rows should have their
review history eyeballed before sending** — Just Refreshed (a one-room salon suite with no tenure
evidence at all), SkinWell + Co. (copyright 2024, so possibly two years old), Jeuje Aesthetics and
Zula Modern Medspa. Those are the ones most likely to have no lapsed list worth recalling.

**gmail is normal here, again.** Two accepted rows publish a gmail (Just Refreshed, Zula) and two
parked rows do (Azia, Haus of Beauty). Not a red flag in this market. But **check the mailto behind
the visible text** — Replete Aesthetics publishes a branded address as visible footer text with a
*different gmail on a different domain* as the actual mailto target, the same trap the 19 Oct sweep
hit at Aesthetically Pleasing. Recording the visible text is the right call; the mismatch is worth
noting because it suggests the branded inbox is unread.

**The four-site ceiling bit in a new way: "locations" that are rooms.** Medical Spa Buffalo lists
four addresses across three towns, but two of them are **separate suites at the same Terrace Blvd
address** split by service type (injectables/laser vs esthetician) — one site presented as two.
Conversely Smart Skin's three sites come with **no named owner at all**, which is the structure the
standard actually warns about. Count decision-makers, not addresses, exactly as the ICP says — and
read suite numbers, not just town names.

**Three metros produced nothing emailable.** **Albany** (Victoria Aesthetics has no address; Spa One
is plastic surgery), **Syracuse** (Revitalize is dermatology; everything else was a Monroe MedSpa
sub-site) and **Toledo** (Blush no address and half out of market; Bella Via plastic surgery; ADA
dermatology). **Birmingham and Bakersfield yielded exactly one emailable clinic each**, and both
were thin enough to park at C. If the next sweep needs those five metros, the route in is Jess
opening Victoria Aesthetics, Luxe Lounge and Flawless Chattanooga in a browser rather than more
searching — I exhausted the search angles that return clinic domains in them.

**Spokane and Wichita were the opposite — unusually productive.** Spokane alone gave three accepted
rows (The LAB, SkinWell, Crafted Beauty) plus a fourth that only failed on the address (Odara, which
publishes both a founding year and a named owner-injector). Wichita gave two. Both are mid-size
metros with a dense independent injector scene and no national roll-up presence yet, which is
exactly the profile this offer wants. **Worth going deeper in the Pacific Northwest and the
Plains on the next sweep** — Boise, Billings, Sioux Falls, Fargo, Lincoln, Springfield MO.

## Canada sweep — near misses and rule-outs

Swept 20 Oct 2026. Metros covered: Toronto and the GTA (Markham, Oakville,
Mississauga, Kleinburg, North York), Montreal, Ottawa (incl. Manotick),
Vancouver, Calgary, Edmonton, Winnipeg, Halifax (incl. Sydney NS), Victoria,
Kelowna.

**16 accepted rows and 2 parked C rows went to `canada.json`.** Everything below
is either unemailable or fails a must-have.

**Never construct an address for any clinic on this list.**

---

## What this sweep taught us about Canada

1. **Jane App is the default.** Twelve of the clinics looked at book through
   `*.janeapp.com`. In Australia the giveaway platforms were Pabau, Timely and
   Dapple; in Canada, assume Jane first. It is a nameable CRM, so it is worth
   checking the booking link on every Canadian row — it is nearly free grade-A
   evidence.

2. **Email publication is much better than in the US, and Gmail is normal.**
   Only four of twenty-two clinics examined published nothing at all. But five
   of the sixteen accepted rows publish a **Gmail address** on their own site,
   which in the US sweep was rare. A Gmail address published on the clinic's own
   page still satisfies conspicuous publication — it is where it is published
   that matters, not the domain.

3. **Founding years ARE sometimes published here**, unlike the US. Four clinics
   stated one outright (Aurora 2007, Dermis 2006, Distinct 2020, True Clinic
   2021). Where it is absent, say so — the copyright range is the usual proxy and
   must not be dressed up as a founding date.

4. **Quebec needs French search terms**, as briefed. "Médecine esthétique" and
   "clinique médico-esthétique" surface a different set of clinics from the
   English queries, and Quebec sites name the owner more readily — Versa MD
   labels its owner "Propriétaire" outright, which no English-Canadian site in
   this sweep did.

5. **Watch for the group/parent-company tell.** Two otherwise-good clinics turned
   out to sit under something larger, and the tell was a **loyalty programme
   branded for a parent company** rather than for the clinic. Check whose name is
   on the rewards scheme.

6. **Obfuscation is the main blocker, and it is not always Cloudflare.** One site
   hand-rolled it as `aesthevaclinic[@]gmail.com`. Same outcome under the
   standard — not machine-readable, so not seen.

---

## Cannot email — no address published at all

| Clinic | City | Why it qualifies | Why we can't email |
|---|---|---|---|
| **True Clinic** | Halifax + Sydney, NS | The best-fit unemailable clinic found in Canada. Two sites, **both owner-medical-director-injectors named** (Will blanD NP, Chris Browner NP) plus two named RN injectors, **founded summer 2021** (stated), purely injectable-led menu, Jane App, Square gift cards | No email address, no `mailto:`, no privacy policy — nothing. Booking and gift cards only |
| **Vitality MediSpa** | Halifax, Bedford + Halifax North, NS | Three sites, Dr Renier Van Aardt (described as having pioneered the first medispa in Nova Scotia), Aundrea Trevors NP as Lead Nurse Injector, a **Rewards page**, Ernex gift cards, Meevo booking, Affirm plans | No email anywhere. Also carries **cosmetic surgery as a separate service line**, which would need resolving even if an address appeared |
| **New Skin YYC** | Calgary, AB | Founder named (Melanie Rodrigues, Medical Aesthetic Director), four named cosmetic nurse injectors, **Memberships page** and Jane App gift cards, Jane App booking | No email address. Also publishes no street address — "steps away from Britannia Village" and a Maps link only |
| **Skinfidelity** | Mississauga + Kleinburg, ON | Founder named (Shelby Hall, Master Nurse Injector), two sites, injectables-led, Jane App, referral programme, Shopify store | No email — the only "Email" on the site is a contact-form field label |

**True Clinic is worth a phone call on its own.** Two named owner-injectors, a
stated founding year and a clean injectables-only menu is the profile the
standard is built around; it simply publishes no way to write to them.

## Cannot email — address present but obfuscated

Per the standard, an obfuscated address **counts as not seen** and must not be
recorded. All three are readable in a normal browser, so if Jess opens the page
herself she can read the address off and these become pipeline rows.

| Clinic | City | Why it qualifies | The obfuscation |
|---|---|---|---|
| **Juvea Aesthetics** | Calgary, AB | Owner named (Hanan Atwi, RN, described as first in her field to specialise in advanced neuromodulator injections), **VIP membership with a monthly treatment credit**, Jane App, Aerolase, Beautifi financing | Cloudflare — renders as `[email protected]` in both header and footer. **Also unresolved: the location count.** One Calgary address is visible, a `geo.placename` meta tag carries a second Calgary address, and Edmonton clinics are referenced with no address. Resolve the count before it goes anywhere |
| **Beauty Diamond Medical & Aesthetics** | Edmonton, Sherwood Park + St Albert, AB | Owner named (Lola Olorunfemi, PhD, MSN, Dermatology Nurse Practitioner, "owner and lead practitioner"), three sites, Jane App, **RepeatMD membership app** | Cloudflare — renders as `[email protected]`. **Would likely fail the standard anyway:** the medical menu carries HRT, medical weight loss, dermatology and urotechnology beside the aesthetics, which is the heavier-privacy profile the standard disqualifies |
| **Aestheva Medical Aesthetics** | Victoria, BC | Dr Helen Ross named, one Fort Street address, injectables-and-aesthetics menu, Jane App, a limited company ("Aestheva Medical Aesthetics Limited") | **Hand-rolled** obfuscation: published as `aesthevaclinic[@]gmail.com`, so not machine-readable. Minor caveat: hormone health sits on the menu |

## Ruled out on the standard — don't revisit

- **Clinique Praxis Esthétique** (QC) — **five clinics** (Blainville, Terrebonne,
  Montreal Downtown, La Prairie, Laval). Five or more means head office decides
  marketing. It does publish `esthetique@cliniquepraxis.ca`, so it would
  otherwise have been contactable — the scale rule is what rules it out.
- **Dermapure** — national chain with a Yorkville location among many. Head office.
- **DermaEnvy** — multi-location Atlantic Canada chain. Head office.
- **3D Lifestyle** — franchise network (separate Calgary and national sites).
- **Vic Park / vicpark.com** — multi-clinic group (Toronto Bay Street, Montréal-Est
  and others).
- **Clinique Esthétique Montréal Le 200** — plastic surgeon (Richard Lapointe).
  Surgery practice.
- **Clinic 805** — "Cosmetic Surgery & Medical Aesthetics". Surgery practice.
- **Lakeshore Vein & Aesthetics Clinic** — vein practice; the insurance-billing
  and heavier-privacy profile the standard disqualifies.
- **Clinique M (mrockland.com)** — dermatology-led ("clinique dermo et médecine
  esthétique"). Dermatology practice.

## Ruled out as duplicate decision-makers

- **nursejacklyn.com** (Nurse Jacklyn, GTA) — this is **Jacklyn Sudetic, RN**,
  the named founder of **Distinct Medical Aesthetics** (Oakville), which is in
  `canada.json`. Same buyer, same patient list, two brands. Deliberately not
  added. Do not let it in as a second row.

## Not pursued — thin on the lapsed-list test

Single-operator personal-brand sites with no support staff and no published
trading history. They may publish an address, but a solo injector a year or two
in is unlikely to hold the roughly 300+ lapsed patients the standard asks for.
Worth revisiting only if the standard widens.

- **The Beautox Nurse** (Toronto/GTA), **Aundrea Trevors** (Halifax — and she is
  already the Lead Nurse Injector at Vitality MediSpa above, so she would be a
  duplicate decision-maker too), **Face Sculptor** (GTA), **Michele MacLean MD**
  (Halifax), **Organic Glow Medical Aesthetics**, **Kelowna Hills**, **Medliv**
  (Kelowna), **Victoria Skin Care Centre** (Victoria).

## Parked at grade C — in `canada.json`, not for sending

Recorded per the standard rather than dropped. Both fail one must-have that
could not be resolved from the page, and **both need that question answered
before they are ever sent anything**.

- **Philosophy of Beauty** (Toronto/North York) — RN founder named, one address,
  Kangaroo Rewards loyalty programme and gift cards, so a strong dormant signal.
  But the menu carries **private primary care, chronic disease management,
  vaccinations, psychotherapy and pain management** beside the injectables.
  Cash-pay is unestablished (in Ontario this is exactly the profile that might
  bill the provincial plan) and the scope reads multi-specialty. Ask the
  discovery question; if it comes back clean this is a B.
- **Skin Method** (Vancouver) — named naturopathic-doctor founder, one address,
  Jane App, injectables-led. But the footer links **"Join Vos Loyalty", described
  as a parent-company programme**, so whether the founder or a group decides
  marketing is unresolved. Resolve the Vos relationship first.

---

## Still untouched in Canada

Worth a later sweep: **Quebec City**, **Laval and the Montreal North Shore**
(Praxis is there but ruled out on scale), **Hamilton and Burlington**,
**London and Kitchener-Waterloo** (note Skin Vitality already holds 14 Ontario
sites and is ruled out), **Regina and Saskatoon**, **St John's**,
**Moncton and Fredericton**, **Whistler and Kamloops**, and **Toronto proper** —
the downtown and midtown core was barely scratched here, because the English
queries kept returning chains and directories. The accepted Toronto-area rows
are all suburban (Markham, Oakville, North York), so the city core is the single
biggest gap left.

# 21 October 2026 — regional Australia, Canada and the US Northwest

# Regional Australia — near-misses and rule-outs (21 Oct 2026)

Markets swept: Toowoomba, Cairns, Townsville, Darwin, the Sunshine Coast outside
Maroochydore (Noosa, Caloundra, Buderim, Mooloolaba), Bendigo and Ballarat, Launceston,
Bunbury and Mandurah, Wagga Wagga and Dubbo.

Everything below clears some of the ICP on substance but is **not** in `au-21oct.json`.
Grouped by what is actually missing, because the groups need different handling.

---

## Group 1 — Cloudflare-obfuscated address (Jess can read these in her own browser in seconds)

### NQ Aesthetics — Pimlico, Townsville QLD
- **Site:** https://www.nqaesthetics.com.au/
- **Why it qualifies:** **"Founded in 2017"** read verbatim — nine years' trading, one of the
  few verified founding years in the whole sweep. Single site at 115 Kings Rd, Pimlico.
  Practitioner named as Petra (a MirrorMirror link gives "Petra Lee Mackin"). **Timely**
  (bookings.gettimely.com/nqinjectables), gift vouchers sold through Timely.
- **Email status:** **Cloudflare-hidden.** Renders as `[email protected]`. Nothing else
  published but the mobile, 0419 353 390.
- **Consent note for when it is read:** no "no unsolicited commercial email" notice and no
  anti-spam statement on the homepage. Privacy policy not read — none was linked.
- **Minor caveat:** lists "Skin Tag/Thread Vein Removal", which is cosmetic thread-vein work
  rather than Medicare vein medicine; nothing mentions Medicare or bulk billing.
- **This is the best unreachable clinic in the batch.** Verified founding year + Timely +
  vouchers + one site + a named practitioner is a finished grade-A row waiting on one browser
  visit. Townsville otherwise produced almost nothing.

### Suppelle Cosmetic Clinic + Skin Care — Pimlico, Townsville QLD
- **Site:** https://www.suppelle.com.au/
- **Why it qualifies:** a medical cosmetic clinic on one site (Shop 3 Fulham House, 12-16
  Fulham Road, Pimlico), with a landline *and* a published after-hours mobile — a clinic that
  answers. Has a Gift Vouchers page in its About menu.
- **Email status:** **Cloudflare-hidden**, rendering as `[email protected]`. Phone
  (07) 4725 4340, plus 0412 378 144 after hours.
- **Consent note:** no unsolicited-email notice on the homepage. Privacy policy not read.
- **Caveat:** nobody is named as owner or practitioner, no founding year, no booking platform
  (an on-site reCAPTCHA'd "Request A Booking" form). Thinner than NQ Aesthetics; if Jess only
  opens one Townsville tab, open NQ.

---

## Group 2 — No address published at all (the dominant failure mode out here)

### Luxe Skin Aesthetica — Bendigo VIC
- **Site:** https://luxeskinaesthetica.com.au/
- **Why it qualifies:** states it is "registered nurse-led", runs **Timely**, and sells gift
  vouchers through it.
- **Email status:** **none published** — not obfuscated, simply absent. And **no phone number
  either**, which makes Timely the only way in at all.
- **Consent note:** no unsolicited-email notice. Privacy policy not read.
- **Caveat:** no practitioner named, no street address, no founding year. Thin even if reachable.

### Bare Facial Aesthetics (Bare Injectables) — Wendouree, Ballarat VIC
- **Site:** https://www.barefacialaesthetics.com/about
- **Why it qualifies:** **"Monique, Founder & Director"** and a Registered Nurse — a titled
  owner, which is the signal we most want. **Founded in 2021**, read verbatim.
- **Email status:** **none published**, and no phone number either. Booking runs on their own
  /bookings page. Site is built on Wix.
- **Consent note:** no unsolicited-email notice. Privacy policy not read.
- **Worth knowing:** Monique is also named as **Co-Owner of Contour Co** — a second business.
  That makes her a two-business owner rather than a multi-site group, so she still passes the
  decision-maker test, but someone should establish what Contour Co is before approaching.

### The Beau Clinic — Bunbury WA
- **Site:** https://thebeauclinic.com/about-us-1
- **Why it qualifies:** **"est. 2015"** and "now here in Bunbury (since 2023)" — eleven years
  of trading history, originally in the UK, relocated. "Nurse Jen", a UK and Australian
  Registered Nurse, is "the face behind the brand", with 13 years' nursing and 11 in aesthetics.
  Every treatment includes a full consultation.
- **Email status:** **none published** on the About page. Phone +61 456 748 284 only. A
  `thebeauclinic.gettimely.com` booking page surfaced in search, so **Timely** is behind it.
- **Consent note:** no unsolicited-email notice. Privacy policy not read.
- **Caveat:** the Australian trading history is only three years; the eleven years is mostly UK,
  so the lapsed list may be smaller than the "est. 2015" suggests.

### Skin + Body Co — Bunbury WA
- **Site:** https://www.skinandbodyco.com.au/about
- **Why it qualifies:** **"the owner of Skin + Body Co for the past five years"** — Bronaugh,
  first name only, stating her own tenure. **Timely**. A nurse on staff (Gioia) holds a Graduate
  Diploma in Cosmetic Nursing and Injectables.
- **Email status:** **none published** on the About page, and no phone either.
- **Consent note:** no unsolicited-email notice. Privacy policy not read.
- **Caveat:** facial aesthetic work is not explicitly listed as a service — the page says
  "advanced skin, cosmetic, and aesthetic treatments" and the injectables qualification sits on
  a staff bio. It may fail must-have 1 as well as the address test.

### Ageless Health Clinics NT — Parap, Darwin NT
- **Site:** https://agelesshealth.com.au/
- **Why it qualifies:** the only independent Darwin clinic of any size the sweep surfaced. One
  address (114/12 Salonika Street, The Avenue, Parap NT 0820), a landline, and it calls itself
  "Darwin's first and leading health clinic".
- **Email status:** **none published.** A newsletter subscribe field only. Phone (08) 8942 1177.
- **Consent note:** no unsolicited-email notice. Privacy policy not read.
- **Caveat, and it is a real one:** this is a broad health-and-wellness clinic, not an
  aesthetics-led one. Nobody is named as owner, there is no booking platform (the "Book Now"
  button is an on-page anchor), and no founding year. Even with an address this would be a
  thin B at best.

### Nurse Laura (at Coastal Skin & Laser Noosa) — Tewantin QLD
- **Site:** https://nurselaura.com.au/
- **Why it nearly qualifies:** Registered Nurse Laura Craddock, named, working alongside
  Dr Andrew Spall at 4/84 Poinciana Avenue, Tewantin.
- **Email status:** **none published**, and no phone either. Booking runs on her own
  /book-now page.
- **Why it is a rule-out as much as a near-miss:** the host clinic, **Coastal Skin & Laser
  (Tewantin)**, is already on the "ruled out — single operators" list from the 24 Sep sweep, so
  this is the same decision-maker reached from a different domain. Also: Laura's bio lists skin
  cancer nursing interests, dermoscopy and benign lesion removal, which puts the cash-pay
  must-have in doubt.

### SAINT Medical Aesthetics — Toowoomba QLD
- **Site:** https://saintma.com/
- **Status: unreachable, not merely email-less.** The fetch returned only metadata — title,
  description ("Toowoomba's trusted clinic for neuromodulators, biostimulation, and hair
  restoration") and build info. No body text, no contact details, no phone, no address. A
  JavaScript app that this environment cannot read.
- **Handling:** this one is worth Jess opening, because the metadata says it is a real
  Toowoomba clinic and we learned nothing else about it. Same shape as Bare Aesthetic
  (Sunshine Coast) from the 19 Oct run.

### Aesthetica By Andy — Darwin NT
- **Site:** https://www.aestheticabyandy.com.au/
- **Status: unreachable, same way.** Metadata only — "Dawin Nurse Andy Non surgical Cosmetic
  Treatments" (their typo), a service list (anti-ageing consultations, skin rejuvenation,
  Laser IPL SHR, skincare) and nothing else. No address, no phone, no body text.
- **Handling:** the only owner-operator-shaped Darwin result in the sweep. One browser visit
  would settle whether Darwin has anything at all.

### Salt Esthetique — Townsville QLD
- **Site:** https://saltesthetique.com.au/
- **Why it qualifies, and this one hurts:** **"Salt Esthetique® is proudly owned and operated
  by Registered Nurse Alexandria Read"** — stated outright, with her AHPRA number
  (NMW0001919640) published. **Timely** (bookings.gettimely.com/saltesthetique/bb/book). A
  "Join Our Skin Community" list with "early access to selected offers and events" — an opt-in
  list they are already building by hand.
- **Email status:** **none published on the homepage**, and no phone either. I tried
  `/contact` and the fetch errored, so there may be an address one page deeper that I could
  not reach.
- **Consent note:** no refusal of unsolicited email. The signup block says "We respect your
  privacy. Unsubscribe at any time", which is an opt-out for *their* list, not a refusal of
  inbound mail. Privacy policy not read.
- **Handling: open this one.** A titled nurse-owner with a published AHPRA number, Timely and
  an opt-in community list is a grade-A profile. The only thing missing is one page I could
  not fetch.

---

## Group 3 — Published an address but ruled out on the standard (not in the JSON)

- **Chrysalis Medispa (Aitkenvale, Townsville)** — publishes `enquiries@chrysalismedispa.com.au`
  plainly on the homepage and on its treatment page, so it is perfectly reachable. **Ruled out:
  the site says it is "a division of Queensland Plastic Surgery" and its facial team is
  "overseen by Plastic & Reconstructive surgeon Dr Mark Vucak."** Plastic-surgery-attached, and
  Queensland Plastic Surgery (Townsville) is already on the 19 Oct disqualified list. Same
  decision-maker, reached from a new domain. **Do not re-source.**
- **Allure Cosmetic Clinic (8 Margaret Street East, Toowoomba)** — publishes
  `enquiries@drmagnusson.com.au` on its contact page. **Ruled out: the lead practitioner is
  A/Prof Mark Magnusson, a plastic surgeon**, and the contact mailbox is on his surgical
  practice's domain. Plastic surgery is a v2 disqualification.
- **Tamar Skin Clinic (Invermay, Launceston)** — publishes `reception@tamarskinclinic.com.au`.
  **Ruled out on cash-pay: offers "Full body skin checks for assessment, diagnosis, and
  management of skin cancers."** Its doctors are GPs with dermatology and skin-cancer-medicine
  training. Fails must-have 2 outright.
- **Vita Medical / Vita Medical and Skin Clinic (Pinjarra Rd, Mandurah)** — publishes
  `info@vitamedical.au`. **Ruled out: a GP practice.** "Owned by General Practitioners working
  at the practice", six named doctors, a "Skin Cancer Medicine" service, a GP Skin Cancer
  Specialist, **MyMedicare registration**, HotDoc booking and a fax number. Medicare billing on
  the record.
- **Brylie Jayne Injectables (Bendigo)** — `bryliejayneinjectables.com.au` **302-redirects to
  `theaestheticstudiobendigo.com.au`**, which is already pipeline row 419. Same decision-maker,
  second domain. Worth noting as a pattern: a nurse's personal brand domain pointing at the
  clinic she now runs.
- **Cosmetic RN (Braddon ACT)** and **Bellevue Clinic (Albury/Griffith NSW)** — both surfaced
  on a Wagga-area query and both are outside the assigned markets. Cosmetic RN publishes
  `hi@cosmeticrn.com.au` (Imogen Battaglia RN, Timely) and Bellevue publishes no address but
  runs a **6-month skin membership** on **Halaxy**. **Neither was sourced; recording them so a
  Canberra or Albury run can pick them up cheaply.**
- **Nurse Kate Clinics (Young, Griffith, Dubbo, Mudgee NSW)** — a travelling-nurse round
  covering four towns, which per the ICP is one buyer and would qualify. **Not verified: the
  fetch of `nkclinics.com.au` failed with a client error and I did not retry.** Worth one
  fetch on a later run.
- **Skinovation Cosmetic Clinic** and **Skin Repair** (Townsville), **Launceston Skin Clinic**,
  **Launceston Skin Cancer Clinic**, **Esk Family Health Care**, **Mandurah Skin Cancer /
  Mandurah Wrinkle and Skin Care Centre**, **Darwin Dermatology**, **Riverina Skin Specialists**
  (Wagga), **Toowoomba Skin Cancer Clinic**, **Sunlife Skin Cancer Care** and **Cairns Skin
  Cancer & Cosmetic Clinic / Skin Alert Cairns** — all skin-cancer or dermatology practices
  (several under the `skincancercentres.com.au` umbrella). Medicare-billed. **Do not re-source.**
- **NPS Darwin** — plastic, reconstructive and cosmetic surgery. **Queensland Plastic Surgery**
  (Townsville) — already ruled out. **Oral Facial & Implant Centre** (Toowoomba) — dental and
  facial surgery; it is the *landlord* of accepted row Iylah Aesthetics, not a prospect.
- **SILK Laser**, **Australian Skin Clinics**, **Cosmetique**, **Skin Societe**, **Med
  Aesthetics / Rejuv Lab**, **Clinica Lase**, **The Cosmetic Lounge**, **Absolute Cosmetic** —
  chains or head-office groups, already on the ruled-out list. They dominated the Mandurah,
  Bunbury, Palmerston and Ballarat result pages.
- **Central Wagga Medical** and **Trinity Medical Centre** (Wagga) — general practices.
- **Aglo** (`aglo.com.au`) — surfaced on the Sunshine Coast query with one page per tiny
  locality (Calico Creek, Theebine, Woorim). This is the **SEO suburb-page pattern** the ICP
  warns about — many URLs, probably one buyer — but no single clinic address or identity
  surfaced, so there was nothing to verify. Flagging it rather than sourcing it.
- **Defined Cosmetic Aesthetics** (`definedcosmeticaes.wixsite.com`) and **Nova Injectables**
  (`louisew-9.wixsite.com/nova-injectables`) — both on unbranded `wixsite.com` subdomains with
  no custom domain, which in three sweeps has correlated with a business too new or too small
  to have a lapsed list. Not fetched.
- **AGE aesthetics (Ballarat & Torquay)**, **Alchemy Skin & Aesthetics (Bunbury)** and
  **The Cosmetic Lounge (Wagga)** — surfaced only as **`gettimely.com` booking subdomains with
  no own website at all**. There is no clinic page to read an address off, so they fail must-have
  5 by construction. See the market note below, because this is a distinctively Australian failure.
- **Revival Skin Clinic (Mandurah)** — exists only as a `company.site` Square storefront.
  **Gobeauty.au listing for "The Conscious Nurse" (Toowoomba)** — directory page; no own site
  surfaced, and a directory address would not be admissible anyway.

---

## What this market taught me

**The 19 Oct run's headline finding holds, but the mechanism has shifted.** That run concluded
regional Australia fails on reachability, with silence the main tax and Cloudflare the second.
This sweep found the same ratio — 22 accepted against 12 near-missed — but the single biggest
blocker was neither. It was **clinics that have no website at all, only a Timely booking
subdomain**. AGE aesthetics, Alchemy Skin & Aesthetics and The Cosmetic Lounge each surfaced as
nothing but `*.gettimely.com`. Timely has not just won regional Australia's bookings, it has
replaced the website for a slice of the market, and those clinics can never satisfy must-have 5
no matter who opens the page, because there is no page. They are not near-misses; they are
structurally unreachable by email, and the sourcing log should say so.

**Cloudflare behaved geographically, which I did not expect.** Both obfuscated addresses in the
sweep are in Townsville, and both are on Fulham Road / Kings Road in Pimlico, a few hundred
metres apart. Four of the 19 Oct run's Cloudflare clinics clustered similarly. This reads like a
shared local web developer rather than a national pattern, which means Cloudflare is worth
predicting per town, not per country — and it means a town that returns one hidden address will
probably return a second.

**The owner-operator-versus-reachability tension from 19 Oct partly resolved.** That run found
the better the owner signal, the likelier the clinic publishes nothing. This sweep found the
opposite often enough to matter: five accepted rows publish the **owner's own first-name
mailbox** — `jo@`, `terry@`, `lianna@`, `chantelle@`, `sculptedbysuzette@`. That is a better
outcome than a generic `info@`, because the email lands in the decision-maker's inbox with no
gatekeeper. The pattern seems to be that an owner who publishes anything publishes herself.

**Bendigo is the surprise of the sweep and Townsville is the disappointment.** Bendigo produced
four accepted rows from one search — Skinworkx, Bendigo Skin Clinic, CosMedic Solutions and
LUME — all single-site, all with a readable address, three with a titled owner-director, and on
three different systems (Timely, Kitomba, own storefront). A town of 100,000 out-produced
Townsville, Darwin, Launceston, Ballarat and Mandurah combined. Townsville, by contrast, has
four real independent clinics and I could email **one** of them, graded C: two are
Cloudflare-hidden, one is a plastic surgery division, and the one readable clinic has three
skin-cancer-qualified doctors. **Darwin produced nothing again** — the 19 Oct run blamed one
group owning the search results; this run blocked that group's two domains by name and still
found only a wellness clinic with no address and a nurse's site that would not render. Three
sweeps now say Darwin is not a market, it is a single operator plus noise.

**Two consent-screen notes for the AU must-have.** First, **not one of the 22 clinics carried a
"no unsolicited commercial email" notice anywhere I read** — the screen has never once failed in
this market, and I now think the real risk is not a refusal notice but mistaking an opt-out
promise for one. Three clinics print "unsubscribe at any time" or "opt out at any time" against
their *own* newsletter signup; GLO Collective and Salt Esthetique both do. That is an offer to
their subscribers, not a refusal of our mail, and I have recorded it in the notes so nobody
re-reads it as a block later. Second, and less comfortably: **I could only read one privacy
policy in the whole sweep.** Chloe Regan's (clean — its only spam wording is a prohibited-uses
clause barring visitors from scraping the site) and Cosmedic Lab's combined terms page (clean).
Every other guessed `/privacy-policy` path errored, and a domain-scoped search for them returned
treatment pages. Regional Australian clinic sites mostly do not have one. So for 20 of 22 rows
the consent screen rests on the pages I actually fetched, which every row's `notes` states
plainly rather than implying a policy was checked.

**One trap worth repeating in the log.** Cosmedic Lab's own terms page prints
`bianca@cosmediclab.com.ay` for refund requests — `.com.ay`, a typo for a domain that does not
exist. It looks exactly like a published address and is not one. Add it to the "four things that
look like a published address and are not" list as a fifth: **an owner's typo.** The usable
address was on the contact page. Similarly, Sunshine Coast Cosmetic Clinic publishes
`info@sccclinic.com.au` on a site at `sccosmeticclinic.com.au` — a mismatch that looks like an
error and is what the page says, so it went in uncorrected. Correcting it to match the website
would have been a fabrication under the absolute rule, even though it would probably have worked.

# Canada round 2 — near misses and rule-outs — 21 Oct 2026

Markets swept: **Toronto proper** (downtown/Fort York, Yorkville, King West, Leslieville —
North York deliberately excluded, already covered), **Hamilton and Burlington ON** (incl.
Binbrook, Ancaster, Dundas, Grimsby), **London ON**, **Kitchener-Waterloo ON** (incl.
Cambridge, Guelph, Paris), **Quebec City QC** (incl. Sainte-Foy, Beauport, Lebourgneuf,
Lévis), **Regina and Saskatoon SK**, **Atlantic Canada beyond Halifax** (Moncton,
Fredericton, Saint John/Quispamsis, St John's NL).

**23 sendable rows (4 A, 19 B) and 6 parked C rows went to `canada-21oct.json`.**
Everything below is either unemailable or fails a must-have.

**Never construct an address for any clinic on this list.**

---

## Cannot email — no address published at all

| Clinic | City | Why it qualifies | Why we can't email |
|---|---|---|---|
| **Clinique Ekinoxe** | Québec City (Beauport + Lebourgneuf; Sainte-Foy and L'Ancienne-Lorette landing pages) | **The best unemailable fit found in this run, and the only deep-history clinic in Québec City.** States **"DEPUIS 1988"** — thirty-seven years of trading, by far the deepest lapsed list seen in either Canadian sweep. **Ackroo gift cards with a balance-lookup page** (banked credit a lapsed patient is literally holding), goRendezvous booking, a Cyberimpact newsletter list, staff of "10 esthéticiennes, une infirmière et un médecin", registered at the Québec enterprise registrar as a single **entreprise individuelle** so one person decides marketing | `/nous-joindre/` is a **contact form only** — no address, no `mailto:`. The **only** address published anywhere is `emilie_beaulieu@hotmail.com`, on `/mentions-legales/`, named there as the **privacy officer / data-deletion contact**. See the note below before using it |
| **Beaudee Clinic** | Toronto (Leslieville / Queen St E) | Genuinely in the Leslieville core, which was the gap this run was sent to fill. Injectables-led menu, a **Memberships page**, Mangomint booking, Dr Eriney Hanna as medical director overseeing a named nurse injector (Delena), new-client intro offer | **No email, no `mailto:`, no street address and no privacy policy** — the page gives only the neighbourhood. Booking links and Instagram are the whole contact surface |
| **Forever Beauty Injectables** | Hamilton, ON (1160 Upper Paradise Rd) | **"Serving Hamilton and surrounding areas since 2019"** — a stated six-year trading history, which is rare. Injectables-led, Fresha booking, services supervised by qualified medical professionals | **No email address anywhere and no `mailto:` link.** Also only a first name for the injector ("Alyssa"), no surname and no credential |
| **Beauté Santé Anne Bélanger** | Québec City (Beauport) | Médico-esthétique menu including injections, a **carte-cadeau product category**, samples and a gift in every order | **No email and no street address** — only a phone number and a Google Maps short link. Shopify site; "Nous joindre" page not reachable without more spend |

### Read this before using the Ekinoxe address

`emilie_beaulieu@hotmail.com` **is** conspicuously published on the clinic's own site with
no refusal notice, so it technically satisfies CASL's publication test, and Emilie Beaulieu
is very likely the owner given the business is a registered sole proprietorship. **But** it
is published for a single declared purpose — privacy and deletion requests — and CASL's
conspicuous-publication basis also requires the message be *relevant to the recipient's
business role, functions or duties*. A reactivation pitch to a declared privacy-officer
mailbox is a weaker fit than a pitch to a general business address, and it is a personal
Hotmail rather than a clinic address. **Deliberately not made a row.** Given Ekinoxe is the
strongest Québec City prospect by a distance, the better route is one phone call to
418-661-8278 asking for the owner's email, which also confirms who the buyer is.

## Cannot email — address present but could not be read

Per the standard these count as **not seen**. The first is recoverable by Jess opening the
page in her own browser; the second two are rows already in `canada-21oct.json` whose CASL
screen is incomplete and which need a browser check before sending.

| Clinic / page | City | What happened |
|---|---|---|
| **Modern Skin Medispa** (`modernskin.ca`) | New Brunswick | **Not obfuscation — the site refuses automated fetching entirely** (`ROBOTS_DISALLOWED`, 21 Oct 2026). Nothing at all could be read: no email, no address, no owner, no platform. It surfaced second in the New Brunswick search, so it is probably a real independent. **Jess can open it in her browser and it may be a free row** |
| **Artista Medical Aesthetics** — privacy policy | Hamilton, ON | **Row accepted (grade B); CASL screen incomplete.** The address `injectorclaudia@gmail.com` is published three times on the About page, and no refusal notice appears there. But a "Privacy POLICY" link sits in the footer whose URL the page does not expose, and `artistamedicalaesthetics.ca/privacy-policy/` returned a client error. **Open the footer link before sending** |
| **Lucia Medspa** — privacy policy | Saskatoon, SK | **Row accepted (grade B); CASL screen incomplete.** The policy exists at `luciamedspa.com/policies/privacy-policy` but the fetch was refused by the site's robots rules. Also note this row's address is published as a `mailto:` target behind an "Email Us" link rather than as visible text — un-obfuscated and machine-readable, but a step weaker than a displayed address |

## Ruled out on the standard — don't revisit

- **Monaco Spa / Monaco MedSpa** (Ancaster, Burlington, Mississauga, Dundas, **Waterloo**, plus a Miami affiliate) — its own page says **"five locations in the GTA"**. Five or more means head office. It does publish `info@monacospa.ca` and runs a points loyalty programme, a Skin Club and a Laser Club, so it would otherwise have been very contactable — **scale is what rules it out**, same as Clinique Praxis in the 20 Oct sweep. TimeTap booking.
- **Cambridge Skin and Wellness** (Cambridge, ON) — **fails two must-haves at once.** Dermatology-led: Dr David Arnott's medical skin consultations **require a referral from a doctor or nurse practitioner**, and the clinic offers **OHIP-covered consultations** for non-cosmetic skin concerns. Publishes `info@cambridgeskinandwellness.com`, Jane App, Beautifi — irrelevant given the fail.
- **Clinique Médico-Esthétique de Québec** (3165 chemin St-Louis, Québec City) — menu carries **"Consultation en dermatologie"** and **"Chirurgie dermatologique"** plus labiaplasty, and a plural "Nos cliniques" page. Dermatology and surgery. Publishes `info@cliniquemedicoesthetiquequebec.com`, Pomelo Health booking.
- **AA Medical Aesthetics** (1142 Wilson St W, Ancaster, ON) — **not injectables-led**: the menu is lashes, brows, permanent makeup, waxing, laser hair removal, body contouring and a training academy, with no injectables at all. The Fresha booking slug reads "elva-beauty-ancaster-medical-aestheticians-inc" — a beauty business using the words "medical aesthetics". Publishes `info@aamedicalaesthetics.ca`.
- **Bella Sante MD** (Saskatoon) — **parked at C in `canada-21oct.json`** rather than ruled out, because the owner-doctor evidence is strong. Two problems: a **"Join Vos Loyalty" link to `voscollection.com/loyalty`**, a parent-group loyalty programme, and dermatology in its metadata and acne/rosacea on its menu. See the Vos note below.
- **Bense SurgiSpa** (St John's, NL) — "SurgiSpa", an aesthetic treatment centre attached to a surgical practice. **Not opened** — ruled out on name and search description, so treat as unverified.
- **Landells Clinic** (St John's, NL) — **not opened.** Search description reads as an established dermatology practice ("The Landells Team"). Unverified; if Atlantic Canada is swept again, confirm rather than assume.
- **Innovaderm Esthétique** (Québec) — **not opened.** The name points to the Innovaderm dermatology research group. Unverified, same caveat.
- **DermaEnvy (St John's NL)** — already ruled out as a multi-location Atlantic chain in the 20 Oct sweep; it surfaced again and was blocked from later searches.

## Out of scope for this run — but free rows for whoever covers North York

Both surfaced from Toronto-core queries, both are **in North York**, which this run was told
to skip because it was already covered — **but neither is in the pipeline.** Each publishes
a readable address and clears the must-haves on the evidence read on 21 Oct 2026. Somebody
should pick them up; the verification is already done.

> **CORRECTED 21 Oct 2026, same day.** Both were taken into the pipeline, and re-reading the
> evidence changed one of the two grades. "Clears the must-haves" was right for Touch of
> Beauty (now id 574, grade B) and **wrong for The Injection Lounge** (now id 573, grade C):
> a 2024 copyright, no founding year and no review history is roughly two years of trading,
> which will not support the 300+ lapsed patients must-have 4 asks for — the same reason NZ
> row 399 is a C. It also runs no membership, loyalty, gift-card or banked-credit scheme at
> all. Its one real asset is the photo-triage inbox its service pages invite people into.
> Touch of Beauty carries a domain mismatch of its own: the address is on `touchtoronto.ca`
> while the site is `touchofbeauty.love`, the host facility's domain, so check for a bounce.
> The lesson is narrow and worth keeping: **"publishes an address" and "clears the
> must-haves" are two findings, and a near-miss note that runs them together will be read as
> a free row.**

- **The Injection Lounge**, 621 Sheppard Ave E (Bayview Village), North York — `info@theinjectionlounge.com` read as plain text on the homepage. **Jessica Walker, RPN, founder and head nurse injector**, named outright. Jane App (`injectionlounge.janeapp.com`). No refusal notice; no privacy policy on the site. No founding year, copyright 2024. Minor caveat: a lipotropic injection is described as promoting weight loss.
- **Touch of Beauty / Touch Toronto**, 63 Provost Drive, North York (inside Touch Health & Fitness) — `kali@touchtoronto.ca` read as plain text in the contact and accessibility sections. **Kali Tocco, RPN**, practising under Susie Jezerinac, NP. Jane App (`touchtoronto.janeapp.com`), do Finance financing. No refusal notice; no privacy policy. Copyright 2021. Caveat: an injector inside a host gym — the room-rental pattern, so still one buyer, but a small list.

## Not pursued — thin on the lapsed-list test, or out of budget

Single-operator personal-brand sites with no support staff and no published trading history,
on the same reasoning as the 20 Oct list:

- **Aesthetic Nurse Marta** (Toronto), **Nurse Injector Melissa** (Hamilton), **YourSkinRN**, **Freeze Fill Glow**, **Royal Medical Spa Guelph**, **Aesthetics By SAM** (Kitchener-Waterloo — a content/SEO site), **Nurse Kim** (St John's), **Dr Andrea Hickey Medical Aesthetics** (St John's), **Amy NP** and **Clinique Energii** (New Brunswick), **SKN Med Spa** and **InjectYXE** (Saskatoon), **Tabitha Ann Medical Aesthetics**, **ProSkin Regina**, **Lamella**, **Nude Cosmetic Injection Studio** (Saskatchewan), **Clinique Pro-Derme**, **Clinique Viva**, **Clinique Foglia** (Québec).
- **The Beautox Nurse** (Toronto/GTA) was already on the 20 Oct not-pursued list and surfaced again.
- **ArtMed** (Kitchener) — not opened; presents as a larger regenerative-health group rather than an owner-operated injectables clinic. Unverified.
- **Medicart Québec**, **Dermapure Québec–Ste-Foy**, **Vic Park Québec–Sainte-Foy** — all national chains already ruled out in the 20 Oct sweep, re-confirmed as present in Québec City. **Québec City's visible search layer is unusually chain-heavy**, which is the main reason it produced so little (see below).

---

## A group to chase across the whole pipeline: Vos Collection

**Bella Sante MD (Saskatoon) carries a "Join Vos Loyalty" link to `voscollection.com/loyalty`
— the same parent-group loyalty tell that parked Skin Method (Vancouver) at C on 20 Oct.**
Two clinics on opposite sides of the country now sit under one group that nothing in our
list names. That is no longer a coincidence, it is a roll-up we are blind to. **Worth a
single pass over the whole pipeline looking for Vos-branded loyalty links**, and worth
opening `voscollection.com` once to see how many Canadian clinics it holds — if it is a
five-plus group, every one of its clinics is a disqualification and some may already be
graded A or B in the file.

---

## What this sweep taught us about Canada, round 2

1. **The privacy policy is where Canadian clinics park the email address, and nobody was
   looking there.** **Sparkle Lifestyle & MediSpa** in Moncton publishes *no* address on its
   homepage — it would have gone straight into this file as unemailable under the old
   routine — and publishes `info@sparklelifestyle.ca` **twice, in sections 8 and 12 of its
   privacy policy**. Est. 2012, Zenoti, a named injecting medical director: the single best
   Atlantic prospect of the run, rescued by one extra fetch. The existing guidance is
   "homepage and About footer before `/contact`" — **add "then the privacy policy" to it.**
   The CASL screen already forces us onto that page; read it for an address while we are
   there. This is nearly free and it converted a near miss into a row.

2. **Yorkville is the densest independent injector scene found in Canada so far, and it was
   sitting behind one bad query.** The 20 Oct sweep concluded "the English queries kept
   returning chains and directories" and gave up on the Toronto core. Adding
   `"King West" OR "Queen West" OR "Yorkville" OR "Leslieville"` **as quoted alternates
   plus `"info@"`** to a directory-blocked query returned five independent Yorkville clinics
   in one search — MedVSpa (founded 2012), Magy, VBeauty, Kati Face, Labelle Cosmetic — four
   of which became rows. **Two of them share one building**, 182 Davenport Rd: VBeauty in
   the main suite and Kati Face in Suite 250. Separate businesses, separate rows, not one
   clinic with two listings — but check the address before assuming a duplicate. Toronto
   proper went from "the single biggest gap left" to the run's most productive market.

3. **Québec City is the weakest Canadian market swept, and the reason is structural.** Two
   French-language searches, eight clinics opened, and **not one sendable row inside the city
   itself** — three C rows and two near misses. The visible layer is chains (Dermapure,
   Medicart, Vic Park all hold Sainte-Foy addresses), and the independents behind them split
   two ways: physician practices with a surgical line (La Clinique SE does liposculpture;
   Clinique Médico-Esthétique de Québec does dermatological surgery and labiaplasty) or
   esthetics-first clinics that publish no address (Ekinoxe, Beauté Santé). The two rows
   that did come out — Annie Lapointe and Beauté Médic — are both in **Lévis**, across the
   river. The 20 Oct finding that "Quebec sites name the owner more readily" **did not
   hold here**: not one Québec City site used "propriétaire" or "fondatrice", and three
   named nobody at all.

4. **Saskatchewan and Atlantic Canada are the opposite — easy fit, easy address, no history.**
   Nine rows between them and only one failure on scope. Every Saskatchewan clinic opened
   published a readable address, four of five on **Gmail**, which confirms the 20 Oct
   finding. But **nothing publishes a founding year**: of nine rows across SK and Atlantic,
   only Sparkle (2012) and MedAesthetic NL (a 2017 copyright) carry any trading-history
   proxy at all. The "established" must-have is the binding constraint in these markets, not
   the address — the reverse of the US.

5. **A stale copyright year is a trading-history proxy, and worth looking for.** **Medcare
   Aesthetics** carries *two* copyright notices on one page, `© 2019` and
   `Copyright © 2026` — the 2019 line is a leftover nobody cleaned up, which makes 2019 a
   reasonable guess at when the site went up. **MedAesthetic NL** does the same with a lone
   `©2017`. Where no founding year is published, check for a second, older copyright string
   before writing "established not verified".

6. **Two sites published a broken contact mechanism beside a working address.** Visage
   Medical Aesthetics (Regina) displays `visagemedicalregina@gmail.com` as text while its
   `mailto:` link points at the placeholder `email@here.com`. The Aesthetics Boutique
   (Binbrook) displays `contact@theaestheticsboutique.ca` while the `mailto:` behind it
   targets `Ashlynn@...`. **Modern You** (Burlington) does the same: displays
   `info@modernyou.ca`, links `modernyoumedical@gmail.com`. **Record the displayed address
   and note the mismatch** — the displayed one is what was conspicuously published, and the
   mismatch is itself a sign of a loosely maintained site, which tends to correlate with an
   unworked patient list.

7. **No site in this entire sweep carried a notice refusing unsolicited commercial email.**
   Twenty-nine rows and nine near misses, with twelve privacy policies read in full: not one
   refusal. **The CASL screen has now failed to disqualify a single Canadian clinic across
   two sweeps.** It still has to be run and recorded, but it should be budgeted as a
   recording cost, not a filter — and it is cheap to combine with reading the policy for an
   address (finding 1). The real Canadian filters are **no published owner** and **no
   published trading history**.

8. **One structure to watch that is not in the standard yet: the practitioner collective.**
   **The Narra Clinic** (Hamilton) looks like a four-or-five-location Ontario clinic and is
   actually one Hamilton address hosting several independent injectors who each run their own
   brand and their own Jane App account (Phases Aesthetics publishes its own separate
   address; "Aesthetic Medic" has its own). The standard already covers "an injector renting
   a room inside a host salon" as one buyer — this is the inverse: **a host clinic whose
   patient list is split across several buyers.** The founder is a real decision-maker but may
   only control a fraction of the lapsed list. Ask whose patient list it is before quoting
   anything off list size.

# US Pacific Northwest, Mountain West, Plains and Upper Midwest — near misses and rule-outs, 21 Oct 2026

Markets swept: Tacoma and Olympia WA · Bend and Eugene OR · Billings and Bozeman MT ·
Sioux Falls SD · Fargo ND · Omaha and Lincoln NE · Des Moines and Cedar Rapids IA ·
Madison and Green Bay WI. 25 rows went into `us-21oct.json` (8 A, 16 B, 1 parked C).

Clinics already recorded in `near-misses.md` for these metros were NOT re-sourced:
a.dore Med Spa, Euphoria Health & Med Spa and Ageless Skin Co (all Omaha, 19 Oct) and
Odara Aesthetics (Spokane, 20 Oct). Clinics already in the pipeline were skipped:
ANEU, BLUR and KSD (Madison), OWN Aesthetics (West Des Moines), Harmony Med Spa (Omaha).

---

## Group 1 — Address present but obfuscated (Jess can read these in her own browser in seconds)

Only two in fifteen metros, which matches the standing US finding: obfuscation is rare here and
silence is the norm.

### Central Wellness — 1420 S 24th St W, Billings, MT
Renders as `[email protected]`. The strongest Billings prospect found and better on
profile than either Billings row that qualified. **Zenoti** confirmed
(`centralwellness.zenoti.com`), a membership programme banner-lined "MEMBERS GET MORE" with a
Memberships page and a Membership Discounts page, Allē and PatientFi financing, a
"Request A Consult" form, and a separate BHRT patient login. Single Billings site. Nobody is
named on the site, and the footer gives only "© Central Wellness 2026", so tenure is unknown.
**One browser tab from qualifying.**

### Laura Trapp Aesthetics — 4018 N 144th St, Suite 112 & 113, Omaha, NE
Renders as `[email protected]`; the mailto target is encoded. Owner-injector named
outright — **Laura Trapp, APRN, NP-C, "owner and injector"**, a Creighton nurse practitioner
since 2011 — plus Kelly Turgeon, BSN, nurse injector. Aesthetic Record booking. Single Omaha
site, footer copyright 2023-2026, eight Google reviews displayed and no total. No membership
or loyalty scheme found, so the dormant pool is the recall cycle only. Worth Jess's thirty
seconds because the owner's name and tenure are both already verified.

---

## Group 2 — No email address published anywhere I fetched (a browser will NOT help these)

Eleven clinics. Each clears or very nearly clears the ICP and publishes a form, a phone number
or a text-us link instead of an address. These need a phone call, LinkedIn or Instagram.

**Best three to work by another channel, in order:**

### 1. Juniper Face & Figure — 155 Mill Town Loop, Bozeman, MT
The strongest near-miss in the whole sweep. **Boulevard** (`dashboard.boulevard.io`),
**"Over 390 - 5.0 STAR Reviews on Google in the Last Year!"** — the only clinic in fifteen
metros publishing a reviews-per-year figure, so tenure and volume are both settled — and three
separate dormant schemes: a **Lifetime Loyalty Program** (buy a device package at full value,
keep a member rate on that package for life), an **Injectable Reward Program**, and a
**Refer-A-Friend credit both ways**. Lead injector named (Brett Ashley McMillan), plus a
medical director, an NP and a licensed nurse who are not named. Cherry payment plans.
Contact forms with Phone and Email fields and no address of its own anywhere.

### 2. Fargo Wellness District — 435 32nd Ave E, Suite B, West Fargo, ND
The best dormant structure found in the Dakotas, and it is unreachable. **Aesthetic memberships
whose monthly payments go into an aesthetic account for future services** — banked credit stated
outright — plus a separate injectables club, gift cards, a free phone consultation, and a free
add-on for first-time facial clients. **MyPatientNow** booking. Seven named clinicians under
Spencer Berry, MD, Medical Director & Master Injector, with a business manager named too.
"Over 10,000 Patients Treated" and medical weight loss "since 2011". No email, no mailto.
**Count the decision-maker carefully before approaching: an MD medical director plus six
NP/DNP/PA providers is large for an owner-operated buyer, though it is one address.**

### 3. Bare Body Shop — 10811 Prairie Brook Road, Omaha, NE
Owner, medical director and clinician are one person and she is named:
**Rachel Breitkreutz, DNP, APRN, FNP-C, "Nurse Practitioner, Owner, Medical Director"**, with
her full education published. Runs **Aesthetic Record** for the patient portal *and*
**RepeatMD** for gift cards and a VIP Shop (`barebodyshop.repeatmd.app`) — RepeatMD is a
dormant-rewards ledger by design, which earlier sweeps named the single best signal available.
Also an Ageless.ai results simulator. "New offers coming soon!" is the only special. No email
anywhere; the Book An Appointment button goes to the contact form. Exactly the profile the
offer wants, blocked purely on publication.

**The remaining eight:**

### Revive Clinic and Spa — 1850 SW Plaza Shops Lane, Suite A, Ankeny, IA (Des Moines metro)
Founder named: **Stefanie Gatica, DNP, FNP-C**, "founder and expert injector", with four more
named providers. **MyPatientNow** booking. A VIP Program page, a Gift Cards page and a Payment
Plans page, though none publishes terms. **"Over 130 Reviews" at 4.9 on Google.** Phone and
text numbers and contact forms only — no email in header, footer or contact block. Would have
been a grade A row on an address.

### Rejuvenate (Rejuvenate Wellness Center) — Olympia, WA
Owner named: **Stacy McIntyre, CRNA**, master's-prepared nurse anaesthetist, who "opened
Rejuvenate"; a named BSN nurse injector and a licensed medical esthetician under her. But the
site publishes **no email, no visible phone number and no street address at all** — only Call
Now and Book An Appointment buttons — no platform named, no scheme, no reviews and no founding
date. The least contactable clinic in the sweep.

### Ritual Med Boutique — 3915 Reserve Way, Suite 100, Cedar Rapids, IA
**Zenoti** confirmed (`ritualmed.zenoti.com`) and **100 Google reviews at 5 stars**, with a
full device stack (BBL HERO, HALO, Sofwave, Contour TRL) that a new clinic would not own. But
nobody is named anywhere, the only scheme is "exclusive deals" at a holiday open house, and
there is no email. Tenure proxy is good; everything else needs a call.

### Wagner Aesthetic Studio — 320 N Wisconsin St, De Pere, WI (Green Bay metro)
**Dr Lynn Wagner** named, and the site states it is "a division of LKW Health, LLC" — a rare
published legal entity for a US clinic. One named aesthetic nurse injector and two
aestheticians. Books on **Fresha**, with a Rewards & Savings page and Fresha gift cards. No
email, no founding year, no review total. The second Green Bay clinic found and the better of
the two on clinical depth.

### Absolute Laser MD — 3467 Hilyard St, Eugene, OR
The best banked-credit scheme in the Pacific Northwest and no way to email it. The
**"Absolute Beauty Club"** banks a fixed monthly sum into the member's account toward products
or services on a three-month commitment, then cancellable at will — stated in those terms on
the page. Claims **over 10,000 clients served**. Full device stack (Sofwave, Morpheus8,
Triniti, VISIA). Nobody named except a blog author; phone, address and a social handle only.

### Alora Wellness Spa — 895-C Country Club Rd, Suite 150, Eugene, OR
**"5.0 STAR rating on Google with 300+ reviews!"** — the strongest tenure proxy in Eugene —
**MyPatientNow** booking, monthly memberships, gift cards, new-patient offers, and Cherry plus
CareCredit. Nobody named, no founding year, and no email in header, footer or contact block.

### Jewell Aesthetic Med Spa — Eugene, OR
Owner named: **Hillary Jewell**, board-certified nurse practitioner and nurse injector, who
owns the practice; two long-tenured staff (16 and 28 years). No email anywhere. **Also check
the attachment before anyone works this one:** the page describes Hillary's 20 years serving
*Dr Mark Jewell Plastic Surgery* patients and a colleague's 28 years with Dr Jewell, so the
med spa may sit alongside a plastic surgery practice, which ICP v2 disqualifies. Tenure is not
the problem here; the structure might be.

### Catalyst Med Spa — Gig Harbor, WA
Surfaced on the Tacoma query with a dedicated Gig Harbor location page; never fetched before I
stopped at target. Unresolved rather than ruled out — one fetch for the next run.

---

## Ruled out on the standard — do not re-source

- **Madison Medispa / Madison Vein & Laser** — 114 E Main Street, Suite 115, Waunakee, WI.
  **Disqualified twice over:** the page states the office "works with insurance companies for
  medically necessary vein care patients" and handles insurance coding and billing, which fails
  cash-pay outright, and vein work is itself named as a fail in the brief. Medical director
  **Boyd Erdman, MD**, is a diplomate of the American Board of Venous and Lymphatic Medicine.
  Its address is also Cloudflare-obfuscated. 132 Google reviews at 4.9, MyAestheticsPro booking
  — all irrelevant given the billing. Logged so nobody fetches it again.
- **Billings Dermatology** (Billings, MT) — dermatology practice with a med spa arm. Out on
  profile.
- **Revive Skin Health + Wellness** (Eugene, Florence and Roseburg, OR) — trades as
  "Dermatology & Med Spa", three towns, Jane App, a published memberships page. Out on
  dermatology, and the three-town footprint would need counting too.
- **Dr Andrews Plastic Surgery** (Iowa City and Cedar Rapids) — plastic surgery with a med spa
  arm. Out on profile.
- **Chapter Aesthetic Studio**, Coralville IA — national chain, already on earlier rule-out
  lists.
- **AVIVA Infusions** (Howard and De Pere, WI) — IV infusion brand with per-suburb location
  pages rather than an injectables-led clinic. Wrong segment.
- **Northwest Medical Specialties** (Tacoma, WA) — a multi-site medical oncology/specialty
  group that ranked on a med-spa query. Not a med spa.
- **Omni Centers** (Lacey, WA), **Studio Esthetics** (Olympia), **Tumwater Chiropractic**,
  **Olympia Dental**, **Hair Success Salons' medi-spa** (Fargo), **Beauty Bar Inc** and the
  other "beauty bank" hits — all either wrong segment or out of market. The
  wallet/bank/vault search returned almost nothing in-market this time (see below).

## Surfaced but never opened — the cheapest start for the next run

No search budget is needed to restart on these; they are all fetchable URLs or exact names.

- **Tacoma/Olympia WA:** Catalyst Med Spa (Gig Harbor location page), NW Medical Arts,
  Aesthetic Centre (Tacoma page).
- **Bend OR:** EsthetixMD (`/contact-us/` already surfaced), AH Medicine, Elite Medispa Bend,
  Bodi Sculpting Specialists, Renew Esthetics / Renewed You (Redmond).
- **Sioux Falls SD / Fargo ND:** Lazaderm (`/contact` surfaced — check whether it is
  dermatology before spending a fetch), Total Skin ND (same caution), Image Medi-Spa's
  Fargo-Moorhead second location if there is one.
- **Omaha/Lincoln NE:** Omaha Med Spa (`omahamedspa.com` — reads as a physician weight-loss
  practice with "The OWL Diet" and testosterone, so check the profile first).
- **Des Moines / Cedar Rapids IA:** Coachlight Med Spa (a "Coachlight office Des Moines" page
  implies a multi-office group — count sites first), 360 Med Spas, Nova MedSpa, The Rec Center
  (Iowa City/Coralville).
- **Madison / Green Bay WI:** AestheticA Skin Health Center (Appleton — count sites),
  Allure Skin Health, Indiglo Med Spa (Green Bay), Elite Aesthetics Spa, Genesis by Janelle,
  REN Rejuvenation Bar (Green Bay — its contact page surfaced directly).
- **Montana, unresolved and worth one fetch:** **Crafted Aesthetics & Wellness** lists
  Missoula, Butte, Helena, Billings, Kalispell and Bozeman in its own page title. That is
  either one travelling nurse practitioner (one buyer, and it qualifies) or a six-site group
  (disqualified). It is the single highest-leverage unresolved question in Montana and one
  fetch settles it.

---

## What this market taught me

**This tier of city holds up, and the reason is specific.** Fifteen metros of this size yielded
25 rows against 13 clinics that failed on the address alone — roughly a two-to-one accept rate,
where the 19 and 20 Oct sweeps of comparable metros ran closer to one-to-one and the big-metro
sweeps in September ran one-to-two. The mechanism is not that these cities publish more
willingly; it is that there is **no national roll-up presence to clear out of the search results
first**. Blocking the directory farms in the first query was enough — I never had to block a
single chain, because outside Chapter Aesthetic Studio in Coralville there were none. In Denver,
Boston or Charlotte, half a sweep goes on identifying and excluding LaserAway, SkinSpirit,
Ideal Image and the PE roll-ups. Here the first page of results is clinic domains.

**The published-address problem is real but milder here than the log suggests.** Thirteen of the
38 clinics I opened published nothing, which is bad, but 24 published a readable address on the
first page I fetched. And the footer finding held exactly: **every single accepted address came
off a homepage, an About page or a team page.** I fetched a dedicated `/contact` only twice.
One of those two (Refined Aesthetics, Sioux Falls) was the page that produced the address and
the homepage would not have — worth recording as a counter-example, because the standing advice
is now two sweeps old and may be slightly over-stated for the Plains.

**Cloudflare obfuscation has almost vanished from this part of the country.** Two in fifteen
metros, against six in the mid-Atlantic. So the "Jess reads it in her browser" rescue is worth
almost nothing here — the blocked clinics are blocked by silence, which needs a phone call or
LinkedIn, exactly as the Northern California and Oregon sweep concluded.

**Founding years: confirmed again, and the proxies are getting better.** Only four of 25 rows
publish tenure — LISSÈ ("since 2013"), Onyx (2020), Refresh ("since 2018"), Injector Boutique
(2022) — plus Radiance, which publishes both its founding year and the year the current owner
bought out her co-founder, the single most usable opener in the batch. For the other twenty I
said so in `notes` and named the proxy. **Published Google review counts were the best proxy
available and this region publishes them unusually often:** 627 (Innovative Aesthetics), 316
(Aesthetic Collectives), 306+ plus a patients-served total (Gig Harbor Medical Spa), 200+
(Simply Bliss), 88 (Élan). **Six rows have no tenure evidence of any kind and are flagged in
`notes` for a review-history check before sending:** Puget Beach, Magic Mirror, Refined
Aesthetics, HD Medical, Elevate and Kalen & Co. Three of those six are rooms inside salons or
salon suites, which is the shape that correlates with being young.

**The wallet/bank/vault search finally failed outright.** One query across five of these metros
returned ten results and not one was in-market — Beauty Bar Inc, The Clinique, Rejuve, Everbody,
Joslin, Elite Medical Spa LWR, all elsewhere. The phrase still earned its keep the indirect way
the log describes: I recognised **Kalen & Co.'s "Beauty Wallet credits"** in Cedar Rapids,
**ClubHD's banked member account** in Lincoln, **Absolute Laser MD's "Absolute Beauty Club"** in
Eugene and **Fargo Wellness District's aesthetic account** once I was already on their sites.
In metros this size, spend the query on suburb-stacking instead and recognise the bank when you
land.

**Two structural traps worth adding to the file.** First, a **domain mismatch between the site
and the published address** hit four of 25 rows this sweep — Maintenance Bar (.net vs .com),
Infinity (infinity-ma.com vs infinitymedicalaesthetics.com), Refresh (refreshmedspa.net vs
refreshlincoln.com) and Elevate (elevaterecoveryspa.com vs elevateomaha.com). All four were
read verbatim and all four are recorded, but that is a sixth of the batch where the branded
inbox may be unwatched. It was a curiosity in the 20 Oct sweep; at this rate it is a pattern,
and it is worth a line in the opener's deliverability check. Second, **the quarterly satellite**:
Simply Bliss lists Omaha plus Wauneta and Kearney, which reads as three sites and is one
decision-maker visiting twice a quarter — the travelling-nurse structure the ICP names, found in
a new form. Élan's three sites across two states are genuine and still inside the ceiling;
Fargo Wellness District's seven named providers at one address are the opposite risk, a single
address that may be too big to have an owner-buyer in the room.

**Metros that produced nothing.** Only one: **Eugene, OR** yielded a single thin row (Arbora)
out of four clinics opened, and the three that failed are the three best — Absolute Laser MD,
Alora and Jewell all publish no address, and Jewell may be plastic-surgery-attached anyway.
Eugene needs a phone, not another search. **Green Bay** came close to the same fate: two
clinics found, one emailable. **Bend** gave one row and has four unopened names left, so it is
under-researched rather than thin. Everywhere else — Tacoma, Olympia, Billings, Bozeman, Sioux
Falls, Fargo, Omaha, Lincoln, Des Moines, Cedar Rapids, Madison — produced at least one row and
most produced two or three.


# 22 October 2026 — New Zealand, regional Australia and UK secondary towns

# New Zealand — regional and Wellington-region sweep, near misses and rule-outs — 22 October 2026

Markets swept: Queenstown and Arrowtown, Palmerston North, Rotorua, Taupo, Nelson, New Plymouth,
Invercargill, Whanganui, Gisborne, Blenheim, Timaru, and the Wellington region beyond Te Aro and
Lower Hutt (Petone, Porirua, Kapiti Coast, Johnsonville, Karori). Auckland, Christchurch, Hamilton,
Tauranga, Napier/Hastings, Whangarei, Wanaka and Dunedin were deliberately NOT re-swept.

Accepted rows live in `nz-22oct.json` (28 rows: 1 A, 20 B, 7 C). This file holds everything that did
not make it, and why.

---

## 1. Clears the ICP but publishes NO email address at all

These cannot be rescued by Jess opening the page in her own browser. The address genuinely is not
there.

### Bare Beauty Aesthetics — Taupo
- **Site:** https://www.barebeautyaesthetics.co.nz/
- **Why it qualifies:** a cosmetic and skin aesthetics clinic "operating in the heart of Taupo",
  running on **Timely** and with a **Memberships** page in its own navigation — the dormant-list
  signal we look for. Open five days plus every second Saturday, so it is a real operating clinic,
  not a side hustle.
- **Address problem:** **no email and no phone anywhere.** I fetched both the homepage and
  `/contact` — neither publishes an email, a phone number or even a street address. No privacy
  policy is published or linked, so there was no third page to try. This is NOT obfuscation; there
  is nothing on the page to decode.
- **Also missing:** owner's name, founding year, the actual treatment list, and the membership terms.
  The Facebook and Instagram links in the footer point at squarespace.com rather than at the
  clinic's own profiles, which suggests a template that was never finished.
- **Route if Jess wants it:** the on-site booking link or an Instagram DM. Not email.
- **This is why Taupo produced no row.**

### Freya Aesthetics — Rotorua
- **Site:** https://www.freyaaesthetics.co.nz/
- **Why it qualifies:** "Freya", a New Zealand Registered Nurse with **over 17 years' experience**
  and described as a Registered Cosmetic Nurse, running cosmetic injectables, dermal fillers and
  advanced skin therapy in Rotorua. Solo, cash-pay, no skin cancer or vein work on the menu. On
  substance this was the best Rotorua candidate of the three I found.
- **Address problem:** **no email and no phone on the homepage**, and
  `/contact-freya-aesthetics/` **could not be fetched at all** — it returned a client error on two
  separate attempts, minutes apart. So I cannot say whether an address is published there or not.
  No privacy policy is linked anywhere, so there was no alternative page.
- **Worth Jess opening herself.** This is the one clinic in the sweep where a working browser might
  simply produce the address, because the page exists and I could not reach it. If the contact page
  carries a mailbox, Freya is a clean B and Rotorua gets a sendable row.
- Note: no street address, no surname and no founding year are published either.

### Nelson Appearance Medicine — Nelson
- **Site:** http://nelsonappearancemedicine.co.nz/
- **Why it matters:** this is the brand that Nelson Skin Clinic's own "Cosmetic Injectables" menu
  item links out to, so it is probably where the Nelson injectable patient list actually sits.
- **Address problem:** **the site is robots-disallowed.** Both the homepage and `/contact-us/`
  refused the fetch outright — nothing of either page was retrieved. This is not obfuscation and not
  an absent address; it is a site we are not permitted to read with these tools.
- **Worth Jess opening herself**, and it is the cheapest unlock in this file: reading one page would
  both produce a possible Nelson row and resolve whether Nelson Skin Clinic (parked at C in the
  JSON) owns its injectable list or not. Two outcomes for one page view.

### Athena Clinic — Rotorua and Tauranga
- **Site:** https://www.athenaclinic.co.nz/
- **Why it matters:** it is the top organic result for Rotorua appearance medicine and spans Rotorua
  plus Tauranga, so it is a two-site independent on the face of it.
- **Address problem:** **could not be fetched** — client error on two separate attempts. Nothing is
  known about its address, owner or site count beyond the search snippet.
- **Worth one browser look** before the next Bay of Plenty sweep. Tauranga is already well covered,
  so the value here is the Rotorua half.

---

## 2. Address present but NOT readable — Jess can read these in her own browser in seconds

### Simply Skin Appearance Medicine — Timaru
- **Site:** https://www.simplyskintimaru.co.nz/about-us.html
- **Why it qualifies on substance:** **Debbie Gough, "Owner / Registered Nurse", with over 30 years
  in the aesthetic medical profession** — the longest verified practitioner tenure found in this
  entire sweep. Single clinic at 25 The Royal Arcade, Timaru. Runs on **Fresha**. Free consultations.
  A packages page.
- **Address problem:** **Cloudflare-obfuscated.** The visible text renders as `[email protected]`
  behind a `/cdn-cgi/l/email-protection` link, which the standard counts as NOT SEEN, so it could
  not be recorded. Jess can read it in a browser in seconds.
- **But read this before sending:** even with the address in hand this is a **grade C, not a B** —
  the menu carries **microsclerotherapy** (vein work) and Cryopen mole and skin tag removal, which
  fails the cash-pay must-have as the brief writes it. Recording it here rather than in the JSON
  because the address could not be read at all; if the standard ever widens on cosmetic vein work,
  Debbie Gough is the most experienced operator we have found in South Canterbury.
- No privacy policy is published; the footer links a "Consumer Mandatories" page instead.

### Skin Matters — Taupo
- **Site:** https://skinmatters.co.nz/
- **Why it half-qualifies:** 166 Tamamutu Street, Taupo, offering medical facials, peels, LED, IPL
  and laser, collagen induction therapy and "appearance medicine (cosmetic medicine)". Has both a
  landline and a mobile published, so a real established business.
- **Address problem:** **Cloudflare-obfuscated** — renders as `[email protected]` with the same
  `/cdn-cgi/l/email-protection` signature. Jess can read it in a browser.
- **But verify before sending:** the page never names injectables or says who performs the
  appearance medicine, no owner is named, and no founding year is given. If the appearance medicine
  turns out to be therapist-delivered skin work rather than nurse-delivered injectables, it fails
  must-have 1. The website was "created in 2016", which is a site-age proxy only.
- **Taupo's two clinics are one unreadable address and one absent one**, which is the whole story of
  that town.

### Sophie Hunter Aesthetics — Napier (out of my market, recorded for completeness)
- **Site:** https://www.sophiehunter.co.nz/
- Registered Nurse, 20+ years nursing, boutique cosmetic medicine clinic at 19 Mahia Street,
  Ahuriri, Napier. Runs on **Timely**. Clean injectables-only menu.
- **Cloudflare-obfuscated** address. Also **Napier is already-covered ground** (The Skin Suite is in
  the pipeline), so this is a free row for whoever revisits Hawke's Bay, not for me.

---

## 3. Ruled out on the must-haves — do not re-source

### Fails cash-pay (must-have 2) — the dominant New Zealand failure mode
- **Clinic Eleven** (Suite 11, Coastlands Shopping Mall, 220 Rimu Road, Kapiti Coast) — Dr Brent
  Krivan, fellowships with the Australasian College of Aesthetic Medicine and the NZ Society of
  Cosmetic Medicine, so a genuinely credentialled aesthetic doctor. But the menu **lists skin cancer
  checks and skin cancer medicine**, and **new patients are accepted by GP referral only** — which
  is about as far from cash-pay self-referral as a clinic can get. Publishes no email either.
  **Double fail. This is why the Kapiti Coast has no B row.**
- **Korrene Robinson Skincare** (192 Fitzherbert Ave, Palmerston North) — a deep salon offering with
  **AGLOW skin subscriptions**, facial memberships and gift vouchers, and a Registered Nurse on site
  for injectables, all on **Timely**. Excellent dormant signals. But it lists **"Red Vein Removal"
  by electrology**, which is vein work, and publishes **no email address** on the homepage.
  Salon-led rather than aesthetics-led as well. **Double fail.**
- **Invercargill Skin Centre** (81a Don Street plus a second room at Arena HealthCare, Invercargill)
  — publishes `info@invercargillskincentre.co.nz` in plain text, so reachable, but it is a **skin
  cancer diagnosis and treatment plus acne clinic** run by "Dr Sophie". Two sites and "plans to
  expand". No injectables on the menu at all, so it **fails must-have 1 as well as must-have 2.**
- **Vein and Skin Clinic** (New Plymouth, Paraparaumu, Upper Hutt, Invercargill, Wanaka and more) —
  vein practice by name, multi-site. Surfaced in four separate queries across four towns; block it.
- **Skin Synergy** (New Plymouth) — "Skin Cancer and Cosmetic Medicine" in its own page title.
- **Nelson Skin Doctors** and **Bezar Skin Specialist** (Blenheim) — dermatology / skin-doctor
  practices.
- **Skin Centre** (Tauranga) — already ruled out on 19 Oct; confirmed again.

### Fails must-have 1 (not injectables or aesthetics-led)
- **Miss Kat D** (Bay City Studio, Rongotai, plus Upper Hutt, Masterton and Otaki) — publishes
  `Katdyhrberg@gmail.com` in plain text and covers *exactly* the Wellington suburbs in my brief
  (Johnsonville, Karori, Petone, Porirua, Kapiti). 25 years in the industry, four locations, gift
  vouchers. But the entire menu is **cosmetic tattooing** — microblading, combo brows, lip blush,
  eyeliner, colour refresh. No injectables, so no three-to-four month repeat cycle and nothing the
  offer can recall. A frustrating near-match on geography and a clean fail on substance.
- **Kylie's Beauty Clinic** (1271 Pukuatua Street, Rotorua) — publishes
  `kyliesbeautyclinic@xtra.co.nz` in plain text and runs on Timely, but it is beauty therapists
  only, with no nurse and no injectables named anywhere.
- **Cosmetic Nurse Injectors** (cosmeticnurseinjectors.co.nz) — a **nurse directory**, not a clinic.
  It surfaced in three separate town queries; add it to the blocked list.
- **Sunekos "Find a Clinic"**, **OBSERV "Find Clinics"**, **rohe.nz**, **explore{town}.co.nz**,
  **exploretaupo / exploretimaru / exploreblenheim / explorenelson / exploreinvercargill**,
  **businessme.co.nz**, **infobel**, **findhealthclinics**, **southlandapp**, **whatsoninvers**,
  **myweddingguide**, **ruli.com**, **zoominfo** and **rocketreach** — all directory or
  supplier-locator farms. The explore*.co.nz network in particular is a New Zealand-specific
  "3 Best X in Y" farm that occupies two or three slots in almost every town query. **Block the
  whole `explore*.co.nz` family in the first query next time**; it was the single biggest noise
  source in this sweep.

### Fails owner-operated / site count, or is a known chain
- **The Cosmetic Clinic**, **Transform Clinic**, **Caci**, **Skin Institute**, **Laser Clinics New
  Zealand**, **The Skin Clinics** — all national networks, all already in the brief or confirmed
  again here. Between them they held the top two or three results for Invercargill, Rotorua,
  Porirua, Palmerston North and Timaru before blocking.
- **Tristram Clinic** (Hamilton) and **Pulse Health** — multi-specialty groups; the buyer is not in
  the room.
- **ENT Central / "Cosmetic Central"** (Palmerston North) — appearance medicine bolted onto an **ENT
  surgical practice**. Hospital-attached specialty group; disqualified on category, not fetched.
- **The Lab Clinic** (3/3 Akoranga Drive, Northcote, Auckland) — publishes `info@thelabnz.com` in
  plain text, has a memberships page, a big device menu and a "Dr. Dixon", but it is **Auckland**,
  which is out of scope for this sweep, and it carries National Trainer / Training Centre branding
  that suggests a larger operation. **A free row for whoever next sweeps the North Shore** — the
  address is already verified as readable, read 2026-10-22.
- **Belle Aesthetics** (Unit E, 37 Woodside Ave, Northcote, Auckland) — Camille, RN and founder,
  inside a holistic medical and wellness building, on Fresha, with a memberships menu item.
  **Auckland, out of scope**, and it publishes **no email**. Also worth knowing: the site advertises
  **a clinic room for rent**, which is the host-business pattern in reverse.
- **New Aspect** (Mount Maunganui) — already-covered market.

### Fails "established" / home clinic — the caution in my brief, confirmed
- **Aesthetic Creations** (65 Sneyd Street, Kaiapoi — out of my market, Canterbury) — publishes
  `info@aestheticcreations.co.nz` in plain text, owner "Sarah" a registered nurse of **over 15
  years**, running on Timely. But its own meta description calls it a **"home based salon"**, which
  is exactly the structure that cannot support the 300-plus lapsed patients must-have 4 asks for.
  Out of market anyway, but recorded because it is the clearest example of the pattern in this
  sweep and because the address is verified readable if anyone sweeps North Canterbury.

### GP and medical centres surfaced and not pursued
Queenstown Medical Centre, The Village Medical Centre and The Doctors Whakatipu (Queenstown),
Arrowtown Medical Centre, Ranolf Medical Centre (Rotorua), Awapuni Medical (Palmerston North), Gore
Medical Centre. All general practice — bulk-funded, insurance-adjacent, and the wrong buyer.

---

## 4. Towns that produced nothing, and why

| Town | Result | Reason |
|---|---|---|
| **Arrowtown** | nothing | **There is no aesthetics clinic in Arrowtown.** Every query returned Arrowtown Medical Centre and nothing else. The whole Wakatipu aesthetics supply sits in Queenstown and Frankton, 20 minutes away — three clinics, all now rowed or near-missed. Arrowtown should come off the target list, not be re-swept. |
| **Taupo** | nothing | Exactly two clinics exist. One publishes no address at all (Bare Beauty), the other's is Cloudflare-hidden and its injectable status is unconfirmed (Skin Matters). |
| **Rotorua** | no sendable row | Three clinics readable or part-readable, and **two of the three fail cash-pay on vein work** (On Point Aesthetics, The Appearance Clinic — both parked at C in the JSON with addresses verified). The one clean fit, Freya Aesthetics, has an unreachable contact page. |
| **Kapiti Coast** | no B row | Clinic Eleven fails on skin cancer plus GP-referral-only; Allure Skin & Laser is parked at C as salon-led with a second injector trading under her own mailbox. |
| **Johnsonville / Karori / Petone** | nothing of their own | No clinic is based in any of the three. They appear only as *areas served* by clinics based elsewhere — Miss Kat D (cosmetic tattooing, fails must-have 1) and Naked Face (rowed, based in Paremata). The Wellington region's aesthetics supply is concentrated in Te Aro, the Hutt and Porirua. |

---

## What this sweep taught me about New Zealand

**The email position is as clean as the 19 October sweep found, and the reason is now clearer.** Of
31 clinic sites I fetched, **25 published a readable address in page content** and only **two** were
Cloudflare-obfuscated (Simply Skin Timaru, Skin Matters Taupo) — plus one Napier clinic out of
scope. **No website-builder placeholders, no QR-code addresses, no Open Graph tricks, and not one
site in New Zealand refused unsolicited commercial email.** I read privacy policies on twelve
clinics specifically to check, and the closest thing to a refusal anywhere was Perfectly You
Aesthetics' "We will not send promotional materials without your consent" — which is their own
*outbound* practice toward patients, not a refusal to receive, and I have flagged it in that row
rather than failing it. **The Unsolicited Electronic Messages Act screen passed on every single
clinic in two consecutive New Zealand sweeps.** I think we can now treat it as a formality here and
spend the fetch elsewhere — with one exception, below.

**But the constraint has moved, and it is no longer supply.** The 19 October note said the limit in
New Zealand was supply: block the chains and the layer underneath is thin. That is only half true in
the regions. There is plenty of supply — I found 31 fetchable independents across twelve towns — but
**the binding constraint out here is the cash-pay screen, not reachability and not scarcity.** Seven
of my 28 rows are parked at C, and **five of the seven fail on cash-pay**: vein work at both Rotorua
clinics and at Simply Skin Timaru, vein work plus salon-led structure at Korrene, and skin cancer
plus minor surgery plus Southern Cross insurance claiming at Skin Medic. Add Clinic Eleven and
Invercargill Skin Centre, ruled out entirely. **In small New Zealand towns there is not enough
population to support a pure injectables clinic, so the clinic bolts on whatever else the town
needs — spider veins, mole checks, skin cancer work, or a full beauty and hair offering.** The
bigger the town, the cleaner the menu: New Plymouth, Whitby, Blenheim and Timaru gave clean
injectables-only clinics; Rotorua, Levin and Kapiti did not. **Screen the treatment menu before
spending a fetch on the privacy policy** — that inverts the order my brief gave me, and it is the
single change I would make to the New Zealand procedure.

**Three structural findings worth carrying forward.**

1. **`/contact` beat the homepage twice, against the brief's US-derived rule.** NueAesthetics
   (Timaru) and Aesthetics by Michelle May (Blenheim) both publish **nothing** on the homepage —
   no email, no phone, in Michelle May's case not even a street address — and both publish a clean
   plain-text mailbox on `/contact`. Following homepage-first strictly would have filed two good
   rows as near misses. In New Zealand, fetch the homepage for the *story* and `/contact` for the
   *address*.
2. **The privacy policy earns its fetch for a second reason here.** At Luminous Skin the policy was
   the only page that printed the address as readable text rather than hiding it behind a mailto
   label; at Skindeep Clinic it disclosed the legal entity ("CHA Ltd") that appears nowhere else on
   the site. So the Moncton lesson holds in New Zealand too — just not for the no-refusal check,
   which is a formality.
3. **Mismatched mailbox domains are the norm, not the exception, and they come in two distinct
   flavours.** Six of my rows carry one. The benign kind is a **personal Gmail or Xtra address on a
   .co.nz site** (Paige Gray, Aria Beauty, Miss Kat D, Kylie's) — a signal of a one-person back
   office, not a problem. The one to watch is the **mailto that disagrees with the displayed text**:
   Skin Glow displays `hello@skinglow.co.nz` while the link targets a Gmail, and Perfectly You
   displays `whanganui@` while the link targets `Wellington@` and the privacy policy prints a third
   address at Outlook. **A bounce on any of those six is a routing problem, not disinterest** — I
   recorded each exactly as printed and never corrected it, and said so in every row.

**One parent-group check, resolved, and worth recording as the method working.** The Beauty Lounge
Queenstown publishes its mailbox on `bodysanctum.co.nz` — a different company's domain, which is
precisely the footprint the brief tells us to chase. I fetched Body Sanctum's own locations page: it
is a **two-site Queenstown day-spa group**, which clears the 1-to-4 must-have, with no third-party
loyalty brand in the footer. So this is **not** the acquisitive-group pattern that caught the two Vos
clinics in Canada. It cost one fetch to resolve and it turned a suspicious row into a usable one
with a redeemable monthly membership — the strongest banked-credit signal found in New Zealand to
date. Worth noting for the log: **the 19 October finding that "wallet / bank / vault" returns nothing
in New Zealand still holds, but the equivalent signal is now clearly identifiable** — named
membership subscriptions (Lumé Skin Club, Estetica's plans, Juve's skin-health memberships, Bare
Beauty's, the Skin Journey Membership) and **Aglow**, a third-party membership programme that turned
up independently at a Timaru clinic and a Palmerston North salon. **Aglow is a regional product, not
a parent-group loyalty link** — do not chase it as one, which I nearly did.

**Finally, "established" remains the weakest field in New Zealand and I have not smoothed it over.**
Only **four** of 28 rows have a founding year read verbatim off the page: Ivy Clinic (2018), Allure
Appearance Medicine (2016), CosMedic Clinic (2017) and Aria Beauty (past its fifth anniversary,
undated). Every other row says in its `notes` that "established" is **inferred** and names the proxy
— practitioner tenure, menu depth, a landline, a site copyright year, or a satellite clinic day.
Practitioner tenure is the most common and the most misleading: a nurse with 17 years' experience may
have opened her own clinic last year. The one row where this is a genuine soft spot is **Lumé Clinica**,
whose owner started injecting in 2021, so the 300-plus lapsed bar is plausible but unproven — it says
so in the row.

# Regional Australia, third pass — near misses and rule-outs (22 October 2026)

**Markets swept:** Rockhampton (and Yeppoon), Mackay, Bundaberg and Hervey Bay QLD; Shepparton,
Mildura, Warrnambool and the Latrobe Valley (Traralgon, Sale, Morwell) VIC; Tamworth, Orange,
Bathurst and Armidale NSW; Devonport and Burnie TAS; Albany, Busselton and Kalgoorlie WA;
Alice Springs NT.

**Spend:** about 27 searches and 82 fetches. Accepted rows are in `au-22oct.json` — 25 rows,
2 graded A, 16 B, 7 parked at C with the failing must-have named by number.

Everything below clears some of the ICP on substance but is **not** in the JSON. Grouped by
what is actually missing, because the groups need different handling.

---

## Group 1 — Cloudflare-obfuscated address (Jess can read these in her own browser in seconds)

Only one in the whole sweep, which is itself the finding.

### Gippsland Cosmetic Laser Clinic — Warragul VIC
- **Site:** https://gippslandlaser.com.au/
- **Why it qualifies:** one site at 22a Williams Square, Warragul VIC 3820, with all
  consultations and treatments performed by Registered Nurses. A landline that is answered,
  (03) 5622 1579, and its own BigCommerce retail store.
- **Email status:** **Cloudflare-hidden**, rendering as `[email protected]`. Nothing else
  published.
- **Consent note for when it is read:** no "no unsolicited commercial email" notice on the
  homepage. No privacy policy is linked, so none was read.
- **Caveat:** Warragul is *outside* the assigned Latrobe Valley towns (Traralgon, Sale,
  Morwell) and nobody is named as owner or practitioner. Even unmasked it would be a thin B.
  Recording it so the fetch is not spent again.

---

## Group 2 — No email address published at all (a browser will NOT help these)

This was again the dominant failure mode, and three of these are the best clinics the sweep
found anywhere.

### 1. Nude Aesthetics — Mackay CBD and Bowen QLD
- **Site:** https://nudeaesthetics.com.au/ (contact page also fetched:
  https://nudeaesthetics.com.au/contact-us/)
- **Why it qualifies, and this one hurts the most:** **"Amy Kinlyside, Founder"** named
  outright. Two sites inside the cap — 23 Wellington Street, Mackay QLD 4740 and 34A William
  Street, Bowen QLD 4805. **Memberships stated in the FAQ** ("Yes, we have memberships,
  Afterpay and Zip Pay options available") and **gift cards with no expiry date**, which is
  banked credit with names attached — exactly the dormant-list signal the brief asks for.
- **Email status:** **none published**, on the homepage or the contact page. Phones only —
  0437 235 303 and 0499 189 879 (general enquiries).
- **Consent note:** no refusal of unsolicited email; a newsletter sign-up only.
- **Caveat:** a plastic and reconstructive surgeon (Dr Drew Cronin) consults at the clinic
  monthly. He is a visiting practitioner, not the owner, so this is not a
  plastic-surgery-attached practice — but confirm before approaching.
- **Handling: the best unreachable clinic in the batch.** Named founder + memberships +
  non-expiring gift cards + two sites is a finished grade-A row waiting on a phone call or a
  DM. A browser will not rescue it, because there is no address to unmask.

### 2. LUSH Skin & Laser Clinic — Shepparton VIC
- **Site:** https://lushskinandlaserclinic.com.au/ (policies page also fetched:
  https://lushskinandlaserclinic.com.au/clinic-policies/)
- **Why it qualifies:** **Caterina Armstrong, Clinic Director**, named with a title, plus
  Dr Niki Talic as cosmetic doctor. "More than two decades" of director experience. One site
  at 66 Skene St, Shepparton VIC 3630. **Phorest** as the practice system.
- **The dormant signal is the strongest in the sweep and is on the policies page:**
  **"LUSH Loyalty Cards"**, with rewards redeemable on full-priced in-clinic services, *and* a
  Gift Voucher Policy — "Gift Vouchers are non-refundable and must be used within 3 years of
  purchase." A three-year redemption window with names against it is a dated recall list.
- **Email status:** **none published** — not obfuscated, simply absent from the homepage, the
  footer and the clinic-policies page. Phone (03) 5832 7604 only.
- **Consent note:** no refusal of unsolicited email on either page. No privacy policy exists —
  the "Clinic Policies" page is the closest thing and it is operational, not privacy.
- **Handling:** worth a DM or a call. A loyalty scheme plus a three-year voucher window plus a
  titled director plus Phorest is a grade-A profile with one thing missing.

### 3. Embrace Cosmetic Clinic — Bundaberg North QLD
- **Site:** https://www.embracecosmeticclinic.com/
- **Why it qualifies:** **"8+ Years as a Bundaberg go-to"** — a real tenure claim. One site at
  51/53 Perry Street, Bundaberg North QLD 4670. The treating practitioner is a registered
  cosmetic nurse with a Graduate Diploma in Cosmetic Nursing (AACDS Perth and Gray Clay
  Aesthetics, Gold Coast). By appointment only.
- **Email status:** **none published.** Phone 0429 182 123 only, plus a contact page form.
- **Consent note:** no refusal of unsolicited email. No privacy policy published.
- **Caveat:** nobody is named, and a "mole check" is performed before diathermy lesion removal
  "after GP clearance" — cash-pay-looking, but it puts a GP in the loop.

### 4. Kàllos Aesthetics by Nurse Kellie — Urangan, Hervey Bay QLD
- **Site:** https://www.kallosaesthetics.com.au/
- **Why it qualifies:** **"Nurse Kellie"** named with her AHPRA number published
  (NMW0002270223) and her qualifications listed. One address, Shop 3, 9 Buccaneer Drive,
  Urangan QLD 4655, with Maryborough listed as a serviced town. Booking on Square.
- **Email status:** **none published.** A contact form with name/email/phone/message fields,
  and — a new one for this file — **the envelope icon links to an Emojipedia page**, not a
  mailbox. Phone 07 2103 3359.
- **Consent note:** no refusal of unsolicited email. No privacy policy published.
- **Caveat:** no founding year and no voucher or membership scheme.

### 5. RR Rejuvenate (RR Rejuvenate Skin and Laser Clinic) — Bairnsdale VIC, serving Sale
- **Site:** https://rejuvenate.clinic/contact/
- **Why it qualifies:** **Rachael Rodriguez, Registered Senior Nurse Clinician**, named. One
  site at Suite 13 / 80 Main St, Riviera Plaza, Bairnsdale VIC 3875, by appointment only,
  explicitly serving Sale and Gippsland. **Timely.** A free consultation bookable online.
- **Email status:** **none published** anywhere on the contact page. Phone 0438 722 477 only.
- **Consent note:** no refusal of unsolicited email. No privacy policy and no about page are
  linked at all.
- **Caveat:** Bairnsdale is outside the assigned towns; it reaches Sale as a catchment, and
  Sale already produced an accepted row (HALO Skin Aesthetics).

### 6. Youthful Cosmetic Clinic — Hervey Bay QLD
- **Site:** https://www.youthfulbylisa.com/services-pricing
- **Why it qualifies:** "Nurse Lisa" — **Lisa Zipf**, Cosmetic Nurse, though her name and the
  town both appear only in image alt text. **Dapple CRM**
  (youthfulcosmeticclinic.dapplecrm.com) — the second Dapple clinic in Queensland this sweep,
  after accepted row Ariden Aesthetics in Rockhampton.
- **Email status:** **none published**, and **no phone number either**, so Dapple is the only
  way in at all.
- **Consent note:** no refusal of unsolicited email. No privacy policy published.
- **Caveat:** pigmentation treatment requires "a prior skin check from your doctor", which
  keeps cash-pay clean but shows a GP referral habit.

### 7. Hervey Bay Skin — Urraween, Hervey Bay QLD
- **Site:** https://www.herveybayskin.com.au/cosmetic-injectables/
- **Why it nearly qualifies:** one site at Suite 9 / 1-17 Hershel Court, Urraween QLD 4655.
  Doctor-led, with "Dr Benjamin" named in the footer's About links — first name only.
- **Email status:** **none published.** Phone (07) 4124 6333 only.
- **Consent note:** no refusal of unsolicited email. No privacy policy published.
- **Caveat:** no surname, no title, no founding year, no booking platform, no scheme. Thin
  even if reachable, and Hervey Bay already produced two rows.

### 8. Beautè on the Mall — Alice Springs NT
- **Site:** https://www.beauteonthemall.com.au/
- **Why it qualifies, and it is the best trading history in the sweep:** **"Beautè in the Mall
  was established in early 2000"** — read verbatim, so twenty-six years. **Proprietor Theresa
  Coccetti** named with a title. One address, Suite 14 (upstairs), Cummings Plaza, Todd Mall.
  A Gift Vouchers page.
- **Email status:** **none published.** Phone (08) 8953 6888 only, with a salon.com.au booking
  link.
- **Consent note:** no refusal of unsolicited email. No privacy policy published.
- **Caveat, and it is a real one:** injectables appear only in the **meta description** ("dermal
  fillers… micro-injections to treat facial lines") and are absent from the visible services
  menu, which reads as a beauty salon. Must-have 1 is doubtful. Even so, a 26-year-old
  owner-operated business in a town with nothing else is worth one DM.

### 9. Dr Wod Cosmetic Clinic — Shepparton VIC (plus Mulwala NSW, Cobram and Windsor VIC)
- **Site:** https://drwod.com.au/ (contact page also fetched: https://drwod.com.au/pages/contact)
- **Why it nearly qualifies:** Dr Wod Al Khateeb named. **Timely** on a Shopify site, with gift
  vouchers sold. Main clinic at 43-45 Benalla Rd, Shepparton VIC 3630.
- **Email status:** **none published** on the homepage or the contact page — only a form. Four
  phone numbers are published, one per location.
- **Consent note:** no refusal of unsolicited email. No privacy policy is linked; the only
  policy link is Terms of service, which is the Shopify default.
- **Also a probable must-have 3 problem:** four addresses, two of them rooms inside host
  businesses whose own names are published (S&H Hub in Mulwala, "Blissful Beauty By Majella" in
  Cobram) with separate appointment contacts named for each — Heidi Taylor and Mejellla Almond.
  That reads closer to a host-salon arrangement than to one buyer.

---

## Group 3 — Structurally unreachable (stop spending fetches on these)

**No website at all, only a Timely booking subdomain.** The 21 Oct sweep established that
these can never satisfy must-have 5 because there is no page for anyone to open. Four more,
which brings the running total across two sweeps to seven:

- **Injector Diaries** — `injectordiaries.gettimely.com` (Shepparton query)
- **KJ Aesthetics** — `kjaesthetics3.gettimely.com` (Mildura)
- **Cosmetic Nurse Claire** — `cosmeticnurseclaire.gettimely.com` (Mildura)
- **Lilly Cosmetic & Beauty Pty Ltd** — `lillycosmeticclinic.gettimely.com` (Mildura and
  Tamworth queries both)
- **Injxu Face + Skin** — `injxucosmetics.gettimely.com` (Tamworth and Bathurst queries)
- **ME Aesthetics** — `meaesthetics.gettimely.com` (Devonport)
- **The Cosmetic Lounge** — `thecosmeticlounge2.gettimely.com` — surfaced on the Tamworth,
  Orange *and* Bathurst queries. Already on the 21 Oct list from the Wagga sweep; it keeps
  reappearing because it has no site to rank instead.

**Site exists but will not render to a fetch (robots-disallowed or client error).** A browser
visit would settle each of these in seconds; this environment cannot:

- **Face Against Time** (`faceagainsttime.com`) — **robots_disallowed**. Surfaced on *three*
  separate north-west Tasmania queries as the top result, so it is the most prominent
  Devonport/Burnie-area injectables site and we know nothing about it. **Open this one if any.**
- **Tasmanian Skin Clinic, Devonport** (`tasmanianskinclinic.com.au`) — **robots_disallowed**.
  The only other named Devonport aesthetics clinic.
- **Cosmetic Injectables by Nurse Judee** (`nursejudee.com.au`) — **robots_disallowed**, on two
  attempts via two different paths. Ranked first on both Tamworth/Armidale queries.
- **Albany Skin Clinic, Albany WA** (`albanyskinclinic.com`) — the homepage and the
  `/aesthetic-services/` page both returned **client errors**; only `/contact-us/` rendered, and
  it publishes **no email** and lists **skin cancer checks** as a service, so it probably fails
  must-have 2 anyway. See the Albany note below.
- **Soft Touch Aesthetics privacy policy** (`softtouchaesthetics.com.au/privacy-policy/`) —
  **client error**. The clinic itself is an accepted row; its consent screen rests on the
  homepage alone, which the row's notes say plainly.

---

## Group 4 — Published a readable address but ruled out on the standard (not in the JSON)

These are reachable. They are rule-outs on substance, recorded so nobody sources them again.

- **Divine Medical & Cosmetic Skin Centres** (Maryborough, Hervey Bay, Bundaberg QLD) —
  https://divinemedical.com.au/about-us/. **Ruled out on must-haves 2 and 3, hard.** A
  **mixed-billing general practice**: Medicare Online, bulk billing for under-16s, concession
  and veteran card holders, a Skin Cancer Clinic section, TYRO terminals, and **more than
  thirty named doctors** across three sites plus allied health. Dr Sam Osedimilehin established
  it; the footer also names "La Divino Cosmetic & Skin Clinics". It publishes no email anyway.
  **The single biggest consumer of Bundaberg and Hervey Bay result pages — block
  `divinemedical.com.au` in the first query next time.**
- **Divine Laser + Cosmetic by Dr Sam** (`divinelaser.com.au`, Hervey Bay) — same Dr Sam,
  second domain, same decision-maker. Not fetched. Do not re-source.
- **Absolute Health & Skin Clinic** (Norman Gardens, Rockhampton) —
  https://www.absolutehealthandskin.com.au/. Publishes `admin@absolutehealthandskin.com.au`
  plainly, so it is perfectly reachable. **Ruled out on must-have 2:** a **general practice**
  with thirteen named GPs, comprehensive skin cancer checks and treatment, published Medicare
  rebate amounts, and bulk billing for over-65 pension card holders. It also carries an
  instruction worth noting as a near-relative of the consent screen but *not* one: "Under no
  circumstances should patients seek medical advice or communicate any health matters… via
  email to our Practice Manager." That restricts clinical email from patients; it is **not** a
  refusal of unsolicited commercial email. Do not misread it as one.
- **Pacific Plastic Surgery** (Bundaberg, Mackay, Rockhampton QLD) —
  `pacificplasticsurgery.com.au`. **Plastic surgery**, a v2 disqualification, and it ranked
  first on the opening Queensland query. Block it.
- **Kaleidoscope Cosmetic & Skin Cancer Clinic** (Bundaberg) — skin cancer in the name.
  **My Skin Centre Busselton**, **Mildura Skin Cancer Clinic** (`milduraskin.com.au`),
  **Bathurst GP skin cancer clinic**, **MoleMap Mildura** — all skin-cancer practices,
  Medicare-billed. Fail must-have 2. Do not re-source.
- **Northway Plaza Medical and Skincare** (Bundaberg), **Family First Medical Centre** (Madsen
  Rd), **Shepparton Skin Clinic** (listed on healthdirect as a *skin-check general practice*),
  **Sunshine Medical Centre Busselton**, **Valley Road Medical Centre TAS**, **Burnie GP Super
  Clinic**, **Bath Street Family Medical Centre** and **Mall Medical Centre** (Alice Springs),
  **Central Clinic Alice Springs**, **Central Wagga-style GP practices** generally — general
  practices. Fail must-have 2.
- **My Skin Plus** (166 Steele St, Devonport TAS) — https://www.myskinplus.com.au/. Publishes
  `skinrec@myclinicplus.com.au` — **a mismatched domain** that is itself the tell: the header
  logos link out to other clinic websites and the mailbox sits on the **myclinicplus.com.au**
  parent domain. **Ruled out on must-haves 2 and 3:** a "Skin Check" service, **HotDoc**
  booking, and a parent-group mailbox means marketing is decided above the clinic. This is the
  parent-group tell in its Australian form — not a loyalty link, but a **shared reception
  mailbox on the group's domain**. Worth adding to the tell list.
- **Bathurst Cosmedical & Skin Clinic** (189 Bentinck St, Bathurst NSW) —
  https://bathurstcosmedical.com.au/about-us/. **Ruled out on must-have 2:** the principal is
  Dr Akber Alamyar (MBBS UNSW, FRACGP, FACRRM) and the page lists treatment of **melanoma,
  squamous cell carcinoma and basal cell carcinoma**. Open Tue/Wed 10-4 and Thu 2-4. Publishes
  no email either. **This was Bathurst's only other independent.**
- **Eyra Medical and Skin Clinic** (Moree, Armidale, Tamworth, Sydney, Gold Coast) —
  https://www.eyramedical.com.au/. **Ruled out on must-have 3: five locations**, nobody named
  as owner or practitioner, no street addresses, copyright range 2007-2023, bookings by phone
  only. Publishes no email. Do not re-source.
- **City Medical & Skin Clinic, Burnie TAS** (`cmct.com.au/skin-clinic`, footer: City Medical
  Practice, MOSL Pty Ltd) — **ruled out on must-have 1:** a Burnie general practice, cosmetic
  injectables not mentioned at all. No email published.
- **MedAesthetics Australia** — https://www.medaesthetics.com.au/about/our-story/. Founded by
  **Dr Ehsan Jadoon in Alice Springs in 2009** and expanded to WA in 2010, so it shows up on
  every Alice Springs query. **Ruled out on must-have 3: seven WA clinic locations** (Subiaco
  ×2, Applecross, Butler, Duncraig, Hillarys, Rockingham) with sixteen named cosmetic nurses
  and dermal clinicians. **It no longer has an Alice Springs presence at all.** Publishes no
  email. Block `medaesthetics.com.au` on NT queries.
- **Enhanced Aesthetics** (`enhanced-aesthetics.com.au`, WA) — the only address on the site is
  **`filler@godaddy.com`**, an unreplaced GoDaddy Website Builder placeholder. **That is
  furniture, not a published address**, and it is not recoverable in a browser. The site also
  names no town, no street address and no phone, and the copyright reads 2023. "Melinda" leads
  it; bookings run on Appointlet. Fourth builder-placeholder sighting in this pipeline.
- **Skingoodies Tamworth** — surfaced only as a `findhealthclinics.org` directory page. A
  directory address would not be admissible under must-have 6 even if one were shown.
- **Revive, Skin Correction and Laser Clinic** also appears as `revivenailsbeauty.gettimely.com`
  — the same Alice Springs operator we accepted at grade C from her own site. One
  decision-maker, two surfaces. Do not double-source.

---

## Group 5 — Qualified clinics found outside the assigned markets (free rows, already checked)

Surfaced on my queries, out of my towns. **Two of the five are already in `clinic-pipeline.csv`,
so I checked before writing any of them up** — that check cost nothing and saved three rows of
duplicate work. Whoever revisits these metros can have the rest cheaply:

- **Bloom Aesthetic Clinic** — 11 Percy St, Bellerive, **Hobart TAS**.
  `info@bloomaestheticclinic.com.au` read on https://bloomaestheticclinic.com.au/ on
  2026-10-22. **Sarah Munnings, registered nurse and founder** (AHPRA NMW0002354734). Timely,
  gift vouchers, one site. Privacy policy exists at /privacy, unread. **Not in the pipeline —
  a free Hobart row.**
- **Deluxe Aesthetic Clinic** — 12A Winston Street, Maidstone **VIC 3012 (Melbourne)**.
  `info@deluxeinjectables.com.au` read on https://www.deluxeinjectables.com.au/ on 2026-10-22.
  "Cosmetic Nurse Jennifer", RN. By appointment only, no founding year, no booking platform
  named. **Not in the pipeline — a free Melbourne row, thin.**
- **Aesthetica Cosmetic Clinic** — 52 Toorak Rd, South Yarra **VIC 3141**.
  `hello@aestheticacosmetic.com.au` read on https://aestheticacosmetic.com.au/ on 2026-10-22.
  Injectables named outright, "Packages & Plans" in the nav. Nobody named as owner. **Not in
  the pipeline — a free Melbourne row.**
- **Fusion Aesthetics** — 139 Spencer Street, South Bunbury **WA**. `hello@fusionaesthetics.com.au`,
  "Gina, Owner | Clinical Nurse", Timely, gift vouchers, and a weekly-payment **"Treatment
  Wallet"** on PayLeadr — the AU equivalent of the US wallet/bank signal, found at last.
  **ALREADY PIPELINE ROW 501.** Do not re-add. Worth knowing the 21 Oct Bunbury sweep filed
  Bunbury as near-dry while this was already in the file.
- **Suzie Bannon Aesthetic Nurse** — two **Adelaide** rooms (Glenelg East and Royal Park, both
  inside host businesses). `info@aestheticnursesuzie.com.au`. **ALREADY PIPELINE ROW 371.**
  Note its author byline publishes the web agency's mailbox, `marketing@adelaideseomarketing.com.au`
  — a fifth category of thing that looks like a published clinic address and is not.
- **Amanda Fritz Aesthetics** — Cairns and Trinity Beach QLD, `info@amandafritzaesthetics.com.au`,
  AFA Wellness Plan membership, Timely. **ALREADY PIPELINE ROW 408.**
- **Cosmetic Nurse Vee** (Rouse Hill, Sydney) — Gold Membership and personalised gift vouchers
  on Timely, Ms Veda Avard-Van Blanken named with a Masters of Nursing. **Publishes no email**,
  so a Sydney near-miss rather than a free row.
- **The Injectables Nurse** (440 Victoria Street, North Melbourne) — publishes
  `theinjectablesnurse@gmail.com`. Nurses Lucynda and Laura named, no owner. Out of market;
  recording the address so a Melbourne run does not re-fetch it.
- **The Skin Specialist Nurse** (Stowe Business Park, Buckinghamshire, **UK**) — ranked fourth
  on a *Rockhampton* query. `info@theskinspecialistnurse.com`, and the footer names **The Skin
  Specialist Clinics Ltd**, which satisfies the UK company-identity screen outright. A free UK
  row for whoever sweeps the Midlands. It is also a clean demonstration of the brief's warning
  that search is US- and UK-weighted.

---

## What this market taught me

**Queensland's regional coast is the find, and it reverses the 19 Oct verdict outright.** That
run concluded "Darwin, Townsville, Mackay and Rockhampton produced nothing usable at all".
Rockhampton alone produced **three** rows this time, including a grade A (CQ Aesthetics, a
named nurse-founder with a Pty Ltd and an ABN) plus Ariden Aesthetics in the same suburb and
Nurse Bron up the coast at Yeppoon. Mackay produced its first row ever. Bundaberg produced two
and Hervey Bay two more. **The gap was the query, not the market** — exactly what the 21 Oct
Toronto finding predicted. What changed was stacking four town names into one
directory-blocked query and then, crucially, **blocking the local medical groups by name on the
second pass**: `divinemedical.com.au` and `pacificplasticsurgery.com.au` between them owned the
Bundaberg and Hervey Bay result pages, and blocking those two surfaced five independents in a
single search. That is the Darwin lesson applied to a market where it actually worked.

**The parent-group tell has an Australian form, and it is not a loyalty link.** Canada's tell
was a loyalty programme branded for a parent company. Australia's is **a reception mailbox on
the group's domain**: My Skin Plus in Devonport publishes `skinrec@myclinicplus.com.au` while
trading as myskinplus.com.au, and its header logos link out to sibling clinics. The mismatched
domain *was* the disclosure. Worth chasing every time a regional clinic's mailbox sits on a
domain that is a near-synonym of the clinic name rather than the clinic name itself — because
sometimes it is a group (My Skin Plus) and sometimes it is just the owner's other brand (NKA
Aesthetics' `admin@nursekellyaesthetics.com.au`, Vanish's
`admin@vanishskinandlaserclinic.com.au`). You cannot tell without reading the header.

**Mismatched domains are now the norm, not the exception.** Nine of the twenty-five accepted
rows publish a mailbox on a domain other than their website: three free-mail (gmail ×2, outlook,
icloud ×2, bigpond), two near-synonym domains, two sister brands. None was corrected. The 21 Oct
run put the rate at seventeen of seventy-six; this run is **nine of twenty-five, and higher
still outside the metros**. The smaller the town, the likelier the mailbox is the owner's
personal one — which is the better outcome, because it lands with no gatekeeper. `lflavel1@bigpond.com`
(Mildura) and `coastalcosmeticnw@icloud.com` (north-west Tasmania) are the two best examples:
neither looks like a clinic address and both are the only address the clinic publishes anywhere.

**The consent screen has now failed zero times in four Australian sweeps.** Not one of the
twenty-five accepted clinics, and not one of the sixteen near-misses or rule-outs, carries a
"no unsolicited commercial email" notice. I read **seven privacy policies in full this time**
(CQ Aesthetics, CosMedic Collective, The Dermal Clinic, Cosmetic Skin Lab, ANO Cosmetics,
Glow Aesthetics Gippsland, Respectable Injectables) — up from one in the whole 21 Oct sweep,
because I went looking for them rather than guessing `/privacy-policy` paths. All seven were
clean. **The lesson from last time held exactly: the risk is not a refusal notice, it is
mistaking an opt-out promise for one.** Six clinics print "unsubscribe at any time" or
"withdraw consent for marketing communications at any time" against their *own* list, and CQ
Aesthetics' newsletter block says "No spam. Just the things worth knowing". None of those is a
refusal of inbound mail and every row's notes says so. **I would now budget the AU screen as
paperwork, the way the log already does for Canada, and stop treating it as a filter.**

**Reading the privacy policy paid once, exactly as the Moncton case predicted.** Respectable
Aesthetics' policy — on a *different* domain, respectableinjectables.com.au — publishes
**`matt@respectableinjectables.com.au`**, the Director's own first-name mailbox, which appears
nowhere on the clinic's own site. The site's footer only gives `info@`. So the policy did not
rescue an unreachable clinic this time; it upgraded a reachable one from a generic mailbox to
the decision-maker's inbox. That is a cheaper win than it sounds and it argues for reading the
policy on every row we intend to *send* to, not just on the ones that look unreachable.

**Three towns are genuine dry holes and should not be swept again.** **Burnie** — one GP
practice and nothing else; four queries, zero independents. **Albany WA** — one clinic, which
lists skin cancer checks, publishes no email, and whose own pages return client errors.
**Armidale as a standalone market** — a dedicated query returned nothing but Sydney and Perth
clinics, confirming the search weighting; Armidale is only covered at all because Grace
Aesthetics' travelling round reaches it from Tamworth. **Bathurst is a near-dry hole**: two
clinics exist, one bulk-bills and one treats skin cancers, so the town yields one parked C and
nothing sendable. **Devonport is unresolved rather than dry** — its two best sites (Face Against
Time and Tasmanian Skin Clinic) are both robots-disallowed, so one browser visit would settle
whether Tasmania's north-west has two more rows or none.

**Is regional Australia worked out? Not yet, but the cheap depth is gone.** Coastal Queensland
is the exception and still has room — Gladstone, Emerald, Airlie Beach, Bowen, Maryborough and
Gympie all surfaced as catchment towns on clinics' own pages without being swept, and the
Queensland accept rate this run was the best of any Australian pass. Inland NSW, Tasmania
outside Hobart and Launceston, and the whole of WA outside Perth are close to exhausted: each
yielded one row per town at best, and the limiting factor was supply, not budget — I stopped
with roughly half the search allowance unspent because the same seven clinic names kept
returning. **The next Australian run should be a coastal-Queensland run, not another
all-of-regional sweep**, and it should block `divinemedical.com.au`,
`pacificplasticsurgery.com.au`, `medaesthetics.com.au` and `eyramedical.com.au` in its first
query alongside the directory farms.

# UK near-misses and rule-outs — 22 October 2026

Markets swept: Newcastle upon Tyne and Gateshead, Preston, Blackpool, Stoke-on-Trent, Coventry,
Derby, Hull, Middlesbrough, Swansea, Dundee, Inverness, Bath and Cheltenham, Swindon,
Peterborough, Ipswich, Luton and Milton Keynes. ICP v2, under the UK corporate-subscriber screen
(must-have 8). Rows went to `uk-22oct.json`; everything below either cannot be emailed or was
ruled out on the standard.

Run on roughly 15 searches and 76 fetches.

---

## Group 1 — Address present but obfuscated (Jess can read these in her own browser in seconds)

Only two in the whole sweep, which is a lower obfuscation rate than the 19 Oct UK run.

### Hampton Aesthetics — Hampton Hargate, Peterborough (+ Oakwood and Hampstead, London)
- **Site:** https://www.hamptonaesthetics.com/ · 07542 989469
- **Chase this one first.** The company screen is ALREADY PASSED and it is the only near-miss
  here where that is true: the page states the clinic is **"a trading name of liyan ltd"**, and
  prints VAT registration **497999480**. So the only thing standing between this and a sendable
  row is two minutes in a browser.
- **Why it qualifies:** named owner-doctor **Dr Pri Liyanage**; **founding year published
  outright — "has been serving the Hampton region since 2017"**, which almost nothing in Britain
  does; three sites, inside the one-to-four band; Appointedd as the booking platform; free
  consultations advertised, plus bridal and treatment packages. Injectables-led and cash-pay.
- **Address status: Cloudflare-hidden, not absent.** The visible text is `[email protected]` and
  the link is a `/cdn-cgi/l/email-protection` URL, so there is nothing to record from a fetch,
  but it decodes in a real browser.
- One flag for whoever writes: no company *number* is published, only the "liyan ltd" name and a
  VAT number. The name alone satisfies the ICP screen, but a Companies House check on "Liyan"
  would firm it up and also date the entity.

### Mirabel Clinic — 17 Wood St, Old Town, Swindon
- **Site:** https://www.mirabelclinic.co.uk/ · 01793 321180
- **Why it qualifies:** **Dr Alison Brooks** named as the clinic lead, with **Debbie Sandison** as
  practice manager; **Pabau** as the practice system; single site; "over 20 years of experience"
  and "the past decade" in Swindon's Old Town, which is a solid trading-history proxy; a
  complimentary 15-minute consultation, which is a pile of people who consulted and may never
  have booked.
- **Address status: obfuscated, not absent** — the page carries a "protected email" link only.
- **Unresolved even once the address is read:** no company name or number anywhere on the page,
  so must-have 8 would still need a register call. "Minor Surgery" is also a menu category, which
  needs the cash-pay question.

---

## Group 2 — No email address published anywhere I fetched (a browser will NOT help these)

### Newcastle Skin Clinic — Maingate, Team Valley, Gateshead NE11 0BE
- **Site:** https://www.newcastleskinclinic.co.uk/contact/ · 0191 500 0330 · WhatsApp 07761 987 476
- **The best clinic in this entire sweep, and the reason Gateshead has no row.** It is the only
  Gateshead candidate any query surfaced, and it publishes no address at all — not obfuscated,
  genuinely absent from the contact page I fetched.
- **Why it hurts:** a named monthly membership, **"New Skin Club — your monthly membership to all
  year round skin confidence"**; **gift vouchers** sold through its own skin shop; a
  **complimentary skin assessment** with a named practitioner; **Nurse Luisa Scott** named as the
  award-winning skin expert; and **two practice systems live at once — Zenoti and Pabau** — which
  is the half-finished-migration shape earlier runs flagged as a genuine opening angle. Membership
  plus vouchers plus a free assessment is three separate dormant pools.
- No company identity on the page either, so even with an address it would need a register call.
- Route in: phone, WhatsApp or the Zenoti booking account. Worth a call rather than an email.

### pHskin Cosmetic Clinic — First Floor 1, Victoria Rd, Stoke-on-Trent ST4 2HE
- **Site:** https://www.phskin.co.uk/ · 07791 983895
- **Why it qualifies:** **Pauline Dean, Aesthetic Nurse**, named as the practitioner with "over 10
  years experience"; a clean repeat-cycle injectables and skin menu with nothing non-aesthetic on
  it; **Fresha**; single site; ACE and British Association of Cosmetic Nurses affiliations.
- **No email anywhere** on the page, in text or in a mailto. Phone only.
- **Worth knowing for the screen:** the page publishes an **ICO registration, ZA509847**. That is
  a data-protection registration, not a company registration, and it does NOT satisfy must-have 8
  on its own — but it is a thread to pull, because the ICO data-protection register entry for that
  number will name the registered entity, which is exactly the third lookup in the ICP's order. I
  ran out of budget before following it. This is the only clinic in the sweep that handed me its
  own ICO number.

### Midland Aesthetics Clinic — Coventry
- **Site:** https://www.midlandclinic.co.uk/
- **Why it qualifies:** **Karan Briah** named as founder (MPharm, PGCert, clinical pharmacist
  prescriber); single small private clinic; free remote consultations; repeat-cycle injectables
  and PRP menu; "5+ years specialising".
- **No email and no phone number at all.** The only route is a Calendly booking link
  (calendly.com/midlandclinic). No company identity either. Structurally hard to reach.

### Lumé Med & Co — Dundee
- **Site:** https://www.lumemedco.co.uk/
- **Why it qualifies:** **Jennifer Mullen, registered nurse**, who "founded and led" the clinic —
  a titled owner-nurse, which is rarer than it should be; **Faces Consent** as the booking
  platform; single site; clean injectables and skin-booster menu.
- **No email and no phone.** The page even carries `telephone=no` in its meta tags, which
  suppresses phone detection. A past Instagram post mentions a gift-voucher giveaway, so vouchers
  may exist, but nothing is published. No company identity.

### The Nightingale Wellness Clinic — Ipswich, Suffolk
- **Site:** https://www.nightingalewellnessclinic.co.uk/
- **Why it half-qualifies:** "Amy, Registered Nurse" is the only person named, with no surname;
  clean repeat-cycle menu (injectables, skin boosters, microneedling); single site.
- **No email, no phone, no booking platform, no company identity, no founding year.** Four of the
  five must-haves are unverifiable from the page. Thin.

### Tweak NCL — 45 Halewood Avenue, Newcastle upon Tyne NE3 3RX
- **Site:** https://tweakncl.co.uk/ · 07932 595404 / 07881 023252
- Nurse-led clinic run by two nurses who say "we both continue to work within the amazing NHS";
  Instagram handles imply **Ashleigh** and **Charlotte**; "over 10 years combined nursing
  experience"; free consultations; booking via tweak-ncl.book.app.
- **No email at all**, no company identity, and only a 2025 copyright line. Also worth noting for
  must-have 3: two nurses both still working NHS shifts is closer to a side practice than an
  established book, so the 300+ lapsed-patient bar is doubtful even if the address surfaced.

### Mollie Elise Aesthetics — 16 Pall Mall, Chorley, Lancashire
- **Site:** https://mollieeliseaesthetics.com/about-us/
- Surfaced on a Preston query but the clinic is in **Chorley**, which is outside the brief's towns —
  recorded so nobody re-sources it.
- **Why it would have qualified:** **"Nurse Mollie, Specialist Injector & Owner"** — a titled
  owner-injector; **Nurse Alison** as prescribing nurse; **Fresha**; single site; a finance page.
- **No email and no phone anywhere.** And a near-miss on the screen as well as the address:
  **"Mollie Elise Aesthetics Ltd" appears ONLY inside the Fresha booking URL slugs**
  (`mollie-elise-aesthetics-ltd-l94qy43i`), not in the page text. A platform's URL slug is not a
  published company identity any more than a meta tag is a published address — but it does tell
  you the company exists, so one Companies House call would confirm it. Both qualifications are
  one lookup away; only the address is genuinely unrecoverable.

---

## Group 3 — Could not be fetched at all

### Radiant Aesthetics Clinic — Swindon
- **Site:** https://radiantaestheticsclinic.co.uk/
- The site returns **robots_disallowed**, so nothing of the page was retrieved and nothing about it
  is known — not the address, not the owner, not the entity. It was the top organic result for
  Swindon, so it is probably a real clinic. Needs a browser visit, not another fetch.

---

## Ruled out on the standard — do not re-source

- **LASE Cosmetic** (Newcastle, 0191 389 7090) — publishes a readable address,
  `contact@lasecosmetic.com`, and would otherwise have passed the email test, so do not let that
  tempt anyone: the menu is **surgical** (breast and chest, body and limb, facial rejuvenation
  surgery, plus a "Selfie Surgery" service). Plastic surgery, disqualified outright.
- **My Aesthetics Lounge** (Newcastle Business Park) — resolved on Companies House as **MY
  AESTHETIC LOUNGE LIMITED, 15690945, incorporated 29 April 2024**. The company screen passes, but
  eighteen months of trading cannot hold 300+ lapsed patients. Fails must-have 4. Park it for a
  later year rather than re-sourcing it.
- **Derby Derm** (derbyderm.com) — dermatology practice on the face of it. Category
  disqualification, not fetched.
- **Clinic M Medical** (clinicmmedical.co.uk, Dundee/Inverness) — leads with Dermatology. Category
  disqualification, not fetched.
- **Oracle Aesthetics** — its aesthetics service runs **at The Beverley Hospital**.
  Hospital-attached, so the buyer is not in the room. Disqualified.
- **Mumbles Dental & Cosmetic Suite** and **The Mumbles Clinic** (Swansea) — the first is a dental
  practice with facial aesthetics attached; the second is hair restoration plus facial aesthetics.
  Neither is an aesthetics clinic in our sense. Also **Perfect 32** (Hull) and **Lighthouse Dental
  Practice** (Ipswich) — both dental. Not fetched.
- **Reflect Aesthetics** (Blackpool) — the site's own title now reads
  **"websitenolongerinuse"**. Dead domain, in the same family as `19westaesthetics.com` serving an
  unrelated app. Nothing to source.
- **Therapy House** (Lytham St Annes) and **Forte Beauty Clinic** (Dundee) — beauty-and-laser led
  rather than medical. Not fetched.
- **Peachy Health** (Milton Keynes) — "doctor led lifestyle clinic", which reads as weight
  management and hormone work rather than injectables. Not fetched.
- **Pure Skin Clinic** — went into the JSON as a **C**, not a near-miss, because it does publish
  readable addresses. Flagged there for a mailto that disagrees with the printed address, three
  free-mail addresses, an academy arm and a very wide menu.
- **Apsaras Aesthetic Clinic** (Coventry) and **UK Cosmetic Clinic** (Peterborough) — both in the
  JSON as **C** rows with readable addresses. Both carry **vein work** on the menu, which the ICP
  names as a cash-pay fail; neither should be used until that is resolved.
- Search artefacts from US weighting, recorded so nobody chases them: **Rare Aesthetics, West
  Dundee, Illinois** (returned by a Dundee query) and **jeuneaesthetics.com.au**, an Australian
  site returned by an Ipswich query. Same failure mode as the Cambridge, Ontario clinic on 19 Oct.
- Already ruled out by earlier runs and re-surfaced here: **City Aesthetics Clinic** (Newcastle),
  **Harrogate Aesthetics**, and the Harrogate half of **Pure Skin Clinic**. No fetches spent.

---

## Surfaced but never opened — the cheapest start for the next run

Supply was not the constraint this time; budget was. These came back on queries that produced
accepted rows, and none has had a single fetch spent on it:

- **Newcastle / Gateshead:** LA Beauty and Aesthetics (labeautyandaesthetics.co.uk), 415
  Professional Aesthetics, Dr Matla (drmatla.com — check the site count first, it reads
  multi-city)
- **Preston / Blackpool:** Dr Amro Clinic (dr-amro.com), Lotus Medical Aesthetics, Beautiluxe
  Aesthetics Clinic (resolved on the register as **BEAUTILUXE AESTHETICS CLINIC LTD, 11568155,
  inc 13 Sep 2018**, Bamber Bridge — company screen already passed, website unknown)
- **Stoke-on-Trent:** Dr Msha Clinic (drmshaclinic.com), CS Aesthetics Stoke
- **Coventry / Derby:** Geraldine Malone Aesthetics, Mejorar Clinic, MCS Aesthetics, Lady May
  Aesthetics, Balanced Aesthetics (Wendy Dudley), Med Skin Clinic
- **Hull:** Look Natural Aesthetics (looknaturalaesthetics.co.uk)
- **Swansea:** Gower Skin Aesthetics (gowerskinaesthetics.com — flags "Swansea & London", count
  the sites first)
- **Dundee / Inverness:** Fresh Inc Medispa, Laura Belle Aesthetics, City Aesthetics and Laser
  Clinic, Cairn Medica
- **Milton Keynes:** Shujo Aesthetics, Kimberley Mae Aesthetics (lists MK, Bedford and Hereford —
  count the sites), Nue Skin, The Skin Specialist Nurse
- **Peterborough:** **AND SO BEAUTIFUL SKIN CLINIC & WELLNESS LIMITED, 17445131** — surfaced as a
  register entry with no website found. The company screen is passed before anyone looks at it;
  all that is needed is the trading site and an address.

---

## What this market taught me

**Registers-first held up, and more decisively than the 20 Oct run suggested, but not by the route
the brief describes.** The brief says to search Companies House by clinic name and owner name. The
plain name search (`/search/companies?q=`) is nearly useless for that: it ranks results
**alphabetically, not by relevance**, so "facial perfection" returned 1,745 matches and "gallery
medispa" 4,874, with the actual clinic nowhere in the first twenty either time. What works, and
what I would put in the brief, is the **advanced search with `companyNameIncludes` plus
`registeredOfficeAddress` plus `companyStatus=active`** — a precise, single-page, decisive answer
every time. It gave me firm negatives I could trust (no active company with "aesthetic" in its
name is registered in Inverness **at all**; no active "Flawless" company in Preston; nothing
named "Tallent" in Ipswich) as well as the matches. A negative you can trust is worth as much as
a match, because it converts "I ran out of budget" into "graded C for a stated reason".

**The cheapest version of all is a register sweep per town rather than per clinic.** One call on
`companyNameIncludes=aesthetic&registeredOfficeAddress=<town>&companyStatus=active` returns every
candidate entity in that town with its **incorporation date**, which answers must-have 8 and
must-have 4 together, for a whole market, in one fetch. That is how Newcastle and Preston were
mapped before a single clinic page was opened, and it is how **Beautiluxe** and **And So Beautiful
Skin Clinic** ended up on the next-run list already screened. Do NOT try the same thing with SIC
codes and no name filter — `sicCodes=86220&registeredOfficeAddress=Swindon` returned 108
paginated results across every kind of medical business and was a wasted call.

**The anti-correlation the file warns about did not hold this time, and the reason matters.** Of
the clinics I resolved, **eight printed a company identity on their own site** (The Bespoke Clinic
spelling it out as "a trading name of Brandling Health Ltd | CRN 11963327", Halo Aesthetics,
Harley Skin and Laser, Rosie Morley Clinic, Aesthetics Central, Derma Advanced, Astounding Skin,
HDM Aesthetics) and **every one of those eight also published a readable address**. The 19 Oct
finding was that the two qualifications are nearly anti-correlated; what I saw is that the clinics
that print an entity are simply the better-run ones, and better-run clinics publish a mailbox too.
The anti-correlation showed up instead at the *other* end: the clinics with no entity anywhere —
Townhouse, Dr Kane, Aurielle, Tallent — were not sloppy, they were sole traders or
accountant-registered, and three of them published an address perfectly well. **The screen is a
legal-form question, not a tidiness question**, and I would stop treating a missing company name
as a signal about the clinic.

**Thirteen of twenty-nine rows cleared the screen — a 45% pass rate against the 40% of 19 Oct**,
and the improvement is entirely down to going to the register before the website. Not one privacy
policy was read in this sweep. Not one.

**Obfuscation has almost vanished as the UK failure mode.** Two Cloudflare-hidden addresses in
seventy-six fetches, against a far higher rate in September. The dominant failure is now **no
address at all** — seven clinics, every one of them with a phone number or a booking link instead.
That shifts the rescue work from "Jess opens a browser" to "somebody makes a call", which is a
different and more expensive kind of follow-up, and Newcastle Skin Clinic is the one worth the
call.

**Two new traps, both worth adding to the four we already list.** First, **a company identity
inside a booking-platform URL slug** — Mollie Elise's Fresha slug reads
`mollie-elise-aesthetics-ltd-...` while the page text names no entity. That is the same class of
evidence as an address in a meta tag: it proves the thing exists, it is not a publication, and it
should send you to Companies House rather than into a row. Second, **an address printed as visible
link text whose link is a `tel:` placeholder** — Flawless Aesthetics prints
`info@flawlessaestheticsclinic.co.uk` as visible text but wires it to a `tel:` target of
"0 800 123 1234", an unreplaced template default. The address itself was read verbatim and is
recordable; the broken markup is a caveat, not a disqualification. Distinguishing the two was the
closest judgement call of the run.

**Mismatched domains were as common here as the ICP says.** Four of twenty-nine rows publish an
address on a domain other than their website: Skinfinity (`contact@skinfinity.uk.com` from
`skinfinityuk.com`), AMAR Aesthetics (`info@thesalclinic.com` from `amaraesthetics.co.uk` — the
widest mismatch I have seen, and a possible parent-brand tell worth chasing), and UK Cosmetic
Clinic publishing two addresses on `aol.co.uk`. All recorded exactly as printed. AMAR's is the one
to chase rather than just flag: a sibling brand at another domain is how the parent-group tell
starts.

**One register finding worth generalising: a dissolved company at the clinic's exact address.**
Skinfinity Swansea's address matches SKINFINITY LTD 09681780 character for character — and that
company was dissolved in August 2017 while the clinic has traded on since 2012 and is still
trading. Per the ICP a dissolved company fails the screen because the entity now trading is
unknown, so it is a C. But the *exactness* of the address match is itself evidence: this is not a
clinic that never incorporated, it is one that changed legal form. Of all sixteen C rows, this and
**Tallent Medical** are the two I would spend the next two calls on — Tallent on a national
Companies House search rather than an Ipswich-scoped one, and Skinfinity on the HIW register.

**Dry and thin markets, so nobody sweeps them the same way again.** **Gateshead** produced exactly
one candidate and it publishes no address — the only query that found anything there returned
Newcastle Skin Clinic twice and nothing else, and the town is effectively absorbed into Newcastle's
search results. **Inverness** yielded one clinic in the whole town and no company registered there
at all. **Stoke-on-Trent proper** produced nothing: its one good clinic, pHskin, publishes no
address, and the sendable row credited to that market (Harley Skin and Laser) is actually in
Newcastle-under-Lyme. **Bath** produced one clinic, Townhouse, and it failed the screen. Richer
than expected: **Hull** (three rows from one query, counting Beverley and Hessle), **Dundee**
(two sendable, both resolved on the Scottish register) and **Milton Keynes** (three rows including
the sweep's best, Halo Aesthetics).

**One query-shape note.** Stacking four town names with the literal strings `"Ltd"` and `"info@"`
and blocking the directory farms in the first query worked on the first attempt in every cluster
but one. The exception was **Dundee/Blackpool/Gateshead**, which returned two results in total —
the three towns have nothing in common and the engine found no page matching all of it. Splitting
Dundee out on its own immediately returned six clinics. **Stack towns that are near each other,
not towns that are merely both unswept.**


# 28 October 2026 — coastal Queensland, Montreal and the Prairies, the US Upper Midwest

# Coastal and inland Queensland near-misses and rule-outs — 28 October 2026

Markets swept: **Gladstone, Emerald, Airlie Beach and the Whitsundays (Cannonvale, Proserpine),
Bowen, Maryborough, Gympie, Mount Isa, Charters Towers, Roma and Warwick, Queensland.** ICP v2,
under the Australian no-unsolicited-notice screen (must-have 6). Rows went to `au-28oct.json`;
everything below either cannot be emailed or was ruled out on the standard.

Blocked in the first query and every query after it: the directory farms (whatclinic, fresha,
doctify, bookwell, top4, the job boards), the known groups (`artisanclinics.com`,
`voscollection.com`, `medspapartnersinc.com`, `craftedaesthetics`), the local groups the 22 Oct
sweep named (`divinemedical.com.au`, `divinelaser.com.au`, `pacificplasticsurgery.com.au`,
`medaesthetics.com.au`, `eyramedical.com.au`), the chains (Laser Clinics Australia, Australian
Skin Clinics, SILK, Cosmetique), and — new to the list — the regional skin-cancer networks
(`sundoctors.com.au`, `preventskincancer.com.au`, `theskincancerdoctor.com.au`,
`qldskinchecks.com.au`), plus the government and health-directory domains that otherwise eat
every small-town result page (`health.qld.gov.au`, `healthdirect.gov.au`, `healthshare.com.au`,
`hotdoc.com.au`, `healthengine.com.au`).

---

## Group 1 — Cloudflare-obfuscated address (Jess can read these in her own browser in seconds)

Only two in the whole sweep, both outside the assigned towns, which is itself the finding:
**this region's failure mode is silence and robots.txt, not obfuscation.**

### Your Serenity — Gympie QLD
- **Site:** https://yourserenity.com.au/
- **Email status:** **Cloudflare-hidden**, rendering as `[email protected]`. Nothing else published.
- **Why it is only a footnote:** it fails must-have 1 anyway. The menu is facials, Geneo, IPL,
  LED, massage, spray tan, waxing and nails — **no injectables**. Runs ClientDiary with gift
  vouchers. Not worth the browser visit except to confirm the rule-out.

### Skin Deep Cosmetic Clinic — Paradise Point QLD (Gold Coast, out of market)
- **Site:** https://skindeepcc.com.au/
- **Email status:** **Cloudflare-hidden**, rendering as `[email protected]`.
- **Ruled out regardless:** Paradise Point is Gold Coast, already swept. It books on **HotDoc**
  and names **Skin Alert Paradise Point** as an affiliate and as the booking entity, so it is
  skin-cancer-adjacent and probably Medicare-billing — must-have 2. Its content is also stale
  (a 2021 holiday-closure notice still on the page). **Do not re-source.**

---

## Group 2 — Qualifies or nearly qualifies, publishes NO email address at all (a browser will NOT help)

### 1. Skin Haven Aesthetics Whitsundays — Cannonvale QLD
- **Site:** https://www.skinhavenwhitsundays.com.au/
- **Why it qualifies:** injectables-led and nothing else — wrinkle reduction, facial contouring
  and volume, skin rejuvenation, cosmetic peels, PRP, PRX-PLUS. One site at 3A, 76 Shute Harbour
  Rd, Cannonvale QLD 4802. **Led by Registered Nurse Kristina**, who publishes her **AHPRA
  number (NMW0002233134) and the business ABN (69 670 907 329)** — more identity evidence than
  most accepted rows carry. **Timely.** A **complimentary consultation is compulsory for every
  new client**, which is a consult pool with names attached.
- **Email status:** **none published.** Phone 0408 756 296 only. Not obfuscated — simply absent.
- **Consent note:** no refusal of unsolicited email anywhere on the page. **No privacy policy is
  published, so none was read.**
- **Handling: the best unreachable clinic in this sweep.** Named owner-nurse, AHPRA number, ABN,
  Timely, compulsory free consult, pure injectables menu, in a town that produced one accepted
  row. A DM or a call, not an email. No surname published.

### 2. Mel Hornery Cosmetics — Moranbah QLD (and Mackay)
- **Site:** https://melhornerycosmetics.com.au/
- **Why it qualifies, and this one is a grade-A profile:** **Melanie Ellen Jane Hornery, "Founder
  & Registered Nurse"**, AHPRA NMW0001474572, and — unusually — also published as **Moranbah
  Hospital Director of Nursing**, which is a trust signal and a bandwidth problem at the same
  time. A second RN, **Corina Murdoch** (NMW0001790661), is named. **Timely**, Shopify retail,
  **gift vouchers sold through Timely**. Full device suite (truSculpt/truFlex/truBody, Limelight
  IPL, Laser Genesis, 1NEED Pro, Healite II) plus injectables.
- **Email status:** **none published.** **No phone number either** — the booking link is the only
  way in at all.
- **Consent note:** no refusal of unsolicited email. **No privacy policy published, so none read.**
- **Caveat:** Moranbah is **outside the assigned towns** (inland Bowen Basin, a Mackay catchment).
  Recording it so the find is not lost and the fetch is not spent again.
- **Handling:** DM or the booking form. Named founder + second RN + vouchers + Timely + a device
  suite is a finished A row waiting on a contact route.

### 3. Glow Whitsundays — Proserpine QLD
- **Surfaced on:** a supplier stockist locator, at 4 Anzac Road, Proserpine QLD 4800.
- **Status: no website found at all.** Two domain guesses passed as `allowed_domains`
  (`glowwhitsundays.com.au`, `glowwhitsunday.com.au`) returned nothing indexed, and the brand did
  not surface on any Proserpine or Whitsundays query. It is the **only** aesthetics business of
  any kind that surfaced in Proserpine.
- **Handling:** cannot satisfy must-have 5 from here. Social or phone only.

---

## Group 3 — Structurally unreachable (stop spending fetches on these)

**Site exists but will not render to a fetch (robots-disallowed).** A browser visit would settle
each of these in seconds; this environment cannot. Four more, and note how concentrated they are
in the towns that otherwise produced nothing.

- **CQ Skin** (`cqskin.com.au`) — **robots_disallowed**. Titled "Anti-Wrinkle and Cosmetic
  Injectables Central Queensland" and **ranked first on the Emerald/Central Highlands injectables
  query**, so it is the most prominent injectables site in the Central Highlands and we know
  nothing about it. **Open this one if any.**
- **Kalology Skin Care** (`kalology.com.au`) — **robots_disallowed**. Titled "Kalology Gympie:
  Holistic & Advanced Aesthetic Skin Care" and listed on a device-brand stockist locator as the
  only Gympie entry. **The single best hope for Gympie**, which otherwise produced nothing but
  beauty salons.
- **Beyond Beauty Injectables** (`beyondbeautyinjectables.org`) — **robots_disallowed**. Murgon
  QLD (South Burnett, outside the assigned towns). An injectables-named brand on an unusual `.org`.
- **Brooklyn Brow Aesthetics** (`brooklynbrowaesthetics.com`) — Airlie Beach, listed on a stockist
  locator. **Not indexed at all** — a domain-scoped search returned nothing, so there is no page to
  fetch and no result to fetch from. The name suggests brow work rather than injectables, so it
  probably fails must-have 1 as well.

**No website at all, only a link-aggregator page.** The 21 and 22 Oct sweeps established that a
clinic with no site of its own can never satisfy must-have 5. One more, and it is a new variant
worth naming: not a `*.gettimely.com` subdomain this time but a **Linktree**.

- **Elara Beauty** — Mount Isa. Listed on a stockist locator as `linktr.ee/elarabeauty` and nothing
  else. **A link aggregator is the same dead end as a bare Timely subdomain** — there is no page
  anyone can open to read a published address. File and stop.

One correction to the 22 Oct list, worth recording because it saves a wrong assumption: **Refresh
NQ** surfaced on the Cannonvale query as `refreshnq.gettimely.com`, which looks like the
no-website pattern. It is **not** — `refreshnq.com.au` exists, publishes a readable address, an
ABN and a privacy policy, and is an accepted row. **A Timely subdomain in the results does not
prove there is no site; check the `.com.au` before filing a clinic as structurally unreachable.**

---

## Group 4 — Published a readable address but ruled out on the standard (not in the JSON)

Reachable, and recorded so nobody sources them again. The five parked at C are in the JSON with
their failing must-have numbered; these are harder rule-outs.

- **Jema Clinic** (Maryborough QLD, two sites on Lennox Street) — https://www.jemaclinic.com.au/.
  **Ruled out on must-haves 1 and 2, hard.** A **"7 Day BULK Billed & Mixed Billing Practice"**
  with **seventeen named doctors**, a skin cancer clinic with full-body mole mapping, a mini
  operating theatre, coal-board and rail medicals, and HealthEngine booking. "Cosmetic Therapies"
  appears as one line in a forty-item GP menu. Publishes no email anyway.
- **Maryborough Clinic** (258 Bazaar Street, Maryborough QLD) —
  https://www.maryboroughclinic.com.au/. Publishes `pracman@maryboroughclinic.com.au` plainly, so
  it is perfectly reachable. **Ruled out on must-haves 1 and 2:** a general practice founded
  around 1951 and now under Dr Amadi, with an affiliate skin cancer clinic (**Dermatech**) doing
  PhotoFinder full-body photography, dermoscopy and "simple and complex surgical skin repairs."
  No cosmetic work at all.
- **Warwick Medical Centre and Skin Clinic** (Warwick QLD) — a medical centre running a skin
  clinic with a cosmetic-services page attached. **Must-have 2.** It owns the Warwick result pages.
  **Block `warwickmedicalcentre.com.au` in the first Warwick query next time.**
- **Carbal Medical Services** (55 Wood Street, Warwick QLD) — surfaced on a supplier stockist
  locator. An Aboriginal and Torres Strait Islander community health service, so bulk-billed by
  definition. **Must-have 2.** Not fetched.
- **Gladstone Beauty Clinic** (3/96 Toolooa St, Gladstone Central) —
  https://www.gladstonebeautyclinic.com.au/contact. Publishes `hello@gladstonebeautyclinic.com.au`
  plainly. **Ruled out on must-have 1:** hairdressing, make-up, brows, BB Glow, dermaplaning,
  hydrodermabrasion, skin needling and LED — **no injectables**. Timely, Afterpay, no owner named.
- **Highlands Cosmetics** (Shop 3/1 Egerton Street, Emerald QLD 4720) —
  https://highlandscosmetics.com/. **Ruled out on must-have 1:** cosmetic tattoo, brows, lashes,
  luxury facials and permanent hair removal — no injectables. Publishes **no email** either, only
  a form. Worth one note for whoever reads the Saje Aesthetics row: this site runs the **same
  Shopify theme and the same "Apply for our free membership" line** as Saje. That is a shared web
  designer, **not** a parent group — the loyalty link points nowhere but their own shop, which is
  the tell the brief asks us to chase. Chased, and it is clean.
- **Aria Skin and Beauty** (22 Mary St, Gympie QLD 4570) — https://www.ariaskinandbeauty.com/.
  Publishes `ariaskinandbeauty@gmail.com` plainly and states **"Operating Since 2017"**, which is
  a rarer thing than a published email in this region. **Ruled out on must-have 1:** facials,
  peels, microdermabrasion, IPL, waxing, cosmetic tattoo, lashes, nails, spray tans — no
  injectables. ClientDiary with gift cards. **Re-check if the standard ever widens past
  injectables** — this is the best-documented trading history in Gympie.
- **Aglo Salon and Skin Clinic** (Mooloolaba, Sunshine Coast) —
  https://aglo.com.au/cosmetic-injectables-gympie/. Publishes `info@aglo.com.au`. **Out of
  market, and an SEO suburb page:** the URL says Gympie and the content is a Sunshine Coast
  clinic that lists Maroochydore, Buderim, Kawana, Caloundra and Noosa as its catchment. The
  Sunshine Coast is already swept. Also note its "Cosmetic Injectables" menu link points at
  **`doctormitch.com.au`**, a different domain — possibly a visiting-practitioner arrangement,
  which would raise must-have 3. Phorest, gift cards. **Do not re-source.**
- **The Cosmetic Studio Noosa** — publishes `locations-we-serve/` pages for both **Gympie** and
  **Maryborough**. Pure SEO suburb pages against a Noosa address; the Sunshine Coast is swept.
  **Block `thecosmeticstudionoosa.com.au` in any future Gympie or Maryborough query** — it
  outranks anything actually in those towns.
- **Frank Aesthetics** (Oxenford, Currumbin and Loganholme) — https://www.frankaesthetics.com.au/.
  Publishes `hello@frankaesthetics.com.au`, runs **Dapple CRM**, sells gift cards, names nine
  staff including an **Area Manager**. **Out of market** (Gold Coast and Logan, both swept) and
  **an area manager plus three sites and no named owner reads as managed marketing rather than an
  owner-operator** — must-have 3 in spirit. Ranked first on a "Southern Downs" query, which is
  the search weighting, not geography. **Do not re-source.**
- **Skinsense Beauty Therapy** — https://www.skinsensebeautytherapy.com.au/. A **geography trap
  worth recording**: it ranks for "Warwick 4370" and is at **639 Beach Rd, Warwick — in Western
  Australia**, which the `08` phone number gives away. Publishes `skinsensenelly@bigpond.com` and
  names **Nelly Chard, Proprietor**, a therapist since 1980 with vouchers and a privacy policy —
  exactly the regional-owner profile the log describes, and useless to us twice over: it is in a
  swept metro and it has **no injectables** (must-have 1). Its before-and-afters do show spider
  naevi and cherry angioma removal and skin-tag work.
- **121 Medical Centre Cannonvale**, **Herbert Street Family Medical Clinic** (Bowen),
  **Tannum Sands Family Practice**, **BITS Medical Centre** (Boyne Island), **The Gympie Clinic**,
  **North Blackwater General Practice** (Emerald), **Port Curtis Medical Centre** (Gladstone),
  **Gladstone GP Superclinic**, **Emerald Medical Group** — general practices with cosmetic or
  skin lines attached. All must-have 2. Not fetched beyond what the result pages showed.
- **Whitsunday Skin Cancer Clinic**, **Gympie Skin Cancer Clinic** (SunDoctors),
  **QLD Skin Checks** (Gladstone), **The Skin Cancer Doctor** — skin-cancer networks. Must-have 2.
  They own the small-town result pages; block them by name.
- **Mackay Skin Clinic** — already an accepted pipeline row (578). It publishes
  `locations/skin-clinic-airlie-beach` and `locations/skin-clinic-proserpine` SEO pages, which is
  why it keeps surfacing on Whitsundays queries. **Not a new clinic; do not re-source.**
- **Nude Aesthetics** (Mackay CBD and Bowen) — already on the 22 Oct near-miss list as the best
  unreachable clinic in that sweep. Re-confirmed as **the only aesthetics business in Bowen**.
  Still no email. Blocked in my queries so the fetch was not spent again.
- **Respectable Aesthetics** — already an accepted pipeline row (582), with **Gladstone** among
  its serviced towns. Blocked. **Not a new clinic.**
- **Nurse Jodie Clinic** (Minyama) — already an accepted pipeline row (326), with **Gympie** as a
  serviced town. Blocked. **Not a new clinic.**

---

## What this market taught me

**Coastal Queensland is not the depth the 22 Oct log hoped for, and the reason is specific.**
The log listed Gladstone, Emerald, Airlie Beach, Bowen, Maryborough and Gympie because they
appeared as *catchment* on other clinics' pages — and catchment is exactly what they are. Four of
the ten assigned markets have no independent injectables clinic of their own at all: a clinic in
Mackay, Minyama, Hervey Bay or Mooloolaba publishes a page claiming the town, which is why the
town's name surfaces, and the actual buyer is in the metro that was already swept. **A town that
appears only as somebody else's catchment is a lead about the metro, not a lead about the town.**
That is the single most useful thing to carry into the next regional run, in any country.

**Where the depth actually was: Mount Isa, not the coast.** The three best new rows outside
Gladstone came from Mount Isa and Cloncurry — two outback mining towns 900 km inland that nobody
had assigned. Mount Isa alone produced three accepted rows and a fourth parked at C, against one
for Airlie Beach and zero for Bowen, Proserpine, Maryborough, Gympie, Charters Towers, Roma and
Warwick combined. The mechanism is obvious once you see it: a mining town has money, no
competition and no chain presence, so one nurse can own the whole market and does. **Gladstone
(also industrial) produced four.** If there is another Australian run, it should be the inland
mining belt — Moranbah already handed over a grade-A profile unasked, and Blackwater, Dysart,
Clermont, Biloela and Cloncurry's neighbours were never queried.

**The stockist locator is the best candidate generator found in Australia so far, and it beat
search outright.** Two device and skincare brand "find a clinic" pages — Exomide and Procell —
handed over **seven clinics in the assigned towns in two fetches**, including four (One
Aesthetics, Kalology, Elara Beauty, Brooklyn Brow) and two of the three best unreachables (Glow
Whitsundays, Mel Hornery) that **no search query surfaced at all, across twenty-eight searches**.
It works for the same reason Fresha's city pages work as discovery, only better: a stockist list
is national, organised by town, and lists only clinics that actually buy professional product,
which is itself an "established" filter. Two practical notes. The Exomide list is long enough to
truncate mid-fetch, so **re-fetch it with an `offset`** — the second half held Mel Hornery and
Glow Whitsundays. And it gives names and addresses but usually no URL, so budget one
domain-guessing search per batch of names.

**On the consent screen, the fifth sweep running: it disqualified nobody.** Four privacy policies
read in full this run (Saje, Dermotique, Refresh NQ, Emerald Cosmetic Clinic), eight more clinics
with no policy published at all, and **not one site anywhere refuses unsolicited commercial
email**. The brief's instruction to screen the menu first and leave the policy till last was
right, and it paid: Whitsunday Cosmedics, The Beauty Room, One Aesthetics, Belle Âme, La Bella,
Gladstone Beauty Clinic, Highlands Cosmetics, Aria and Your Serenity were all settled on the menu
without a policy fetch being spent. **The menu is the filter out here, and it failed nine clinics
to the consent screen's zero.** The regional pattern the brief predicted held exactly: in a small
town the aesthetics layer is a beauty salon that added skin devices, not a clinic that added
beauty. Nine of the sixteen businesses I opened have no injectables at all.

**The second filter, and it is specific to towns this size: the skin-cancer GP.** Maryborough and
Warwick produced nothing but general practices with skin-cancer clinics bolted on — Jema (bulk
billing, seventeen doctors, mole mapping), Maryborough Clinic (Dermatech, surgical skin repairs),
Warwick Medical Centre and Skin Clinic, Carbal. In a town of twenty thousand the only business
with the capital for a laser is the GP, and that is an automatic must-have 2 failure. **Add the
skin-cancer networks to the first-query block list** (`sundoctors.com.au`,
`preventskincancer.com.au`, `theskincancerdoctor.com.au`, `qldskinchecks.com.au`) — they own these
result pages the way `divinemedical.com.au` owned Bundaberg's.

**Three dry holes, varied three ways each, and I am confident in them.** **Bowen** — three query
shapes, and the only aesthetics business in town is Nude Aesthetics, already a known unreachable.
Worth knowing why it is hard to search: "Bowen" is swallowed by **Bowen Hills, Brisbane**, so
every query returns a Cosmetique branch. Quote the postcode, 4805. **Charters Towers** — four
queries across three shapes, zero independents, and the town name is itself a street name in
Townsville ("259 Charters Towers Road") which poisons the results. **Roma** — nothing, and the
name is unusable: it returns Italy, Roma Street in Brisbane, and nothing in the Maranoa.
**Maryborough, Gympie, Proserpine and Warwick are near-dry rather than dry**: each has exactly
one genuine candidate and in three of the four cases it is unreadable (Kalology robots-disallowed
in Gympie, Glow Whitsundays with no site in Proserpine) or fails on the menu.

**Two geography traps cost real fetches and both have the same shape: the clinic is named after
somewhere it is not.** **Emerald Cosmetic Clinic** is in **Terrigal NSW** — "Emerald" is the
brand. **Skinsense Beauty Therapy** ranks for Warwick QLD and is in **Warwick, Western
Australia**. Both were caught by the area code, which is the cheapest tell available and should be
the first thing read off any regional Australian contact page: **02 is NSW, 03 is Victoria and
Tasmania, 07 is Queensland, 08 is SA, WA and NT.** Check the area code before the address.

**On mismatched mailbox domains, confirming the 22 Oct finding and sharpening it.** Four of the
eight sendable rows publish a mailbox on a domain other than their website — two on gmail, one on
hotmail, one on a `.info` — and a fifth (`admin@oneaesthetics.info`) is parked. That is half,
against nine of twenty-five on 22 Oct, and it goes the way the log predicted: **the smaller the
town, the likelier the published mailbox is a free-provider one in the owner's own hands.** None
was corrected. One row, Saje Aesthetics, publishes **two** addresses on two different free
providers under two different brand names, the second buried in the privacy policy — which is the
clearest case yet for the standard's instruction to read the policy even after an address is
found.

**One structure worth naming because it is the mirror of the host-salon case and it caught a
clinic.** The Skin Coaches in Mount Isa and Cloncurry is a salon that **imports** injectors: two
independent practitioners, each with her own brand, her own mobile and her own booking account —
Square for one, Timely for the other, Phorest for the salon — flying in on published rotations.
Three diaries at two addresses. The salon runs memberships, a loyalty programme **and** gift
vouchers, the richest dormant signal in the sweep, and none of the injectables list is its to
sell. **It is the practitioner-collective fail at a distance**, and in regional Australia it will
be common, because a town of twenty thousand cannot keep an injector busy full-time. The tell is
the same one the standard already names: a separate business name, a separate booking link or a
separate phone number against each practitioner on the team page.

# Canada round 3 — near misses and rule-outs — 28 Oct 2026

Markets swept: **Montreal proper** (Plateau Mont-Royal, Mile End, Westmount, Griffintown,
Vieux-Montréal, Saint-Laurent, Villeray, Verdun / Île-des-Sœurs, Hochelaga-Maisonneuve,
Sherbrooke Est) · **Laval and the North Shore** (Sainte-Rose, Saint-Elzéar, Fabreville,
Blainville, Sainte-Thérèse, Mercier) · **Winnipeg, Manitoba** (Exchange District, Bridgwater,
Portage Ave, Corydon, Stafford St, East Saint Paul) · **Victoria, BC** (Oak Bay, Fort St,
Helmcken Rd, Shelbourne) · **Kamloops, BC** · **Whistler, BC** · **Barrie, ON** ·
**Niagara, ON** (Niagara Falls, St Catharines, Fonthill) · **Windsor, ON**.

**22 rows went to `ca-28oct.json` — 2 A, 18 B, 2 parked C.** Everything below is either
unemailable or fails a must-have.

Clinics already recorded in `near-misses.md` for these markets were NOT re-sourced:
**Aestheva Medical Aesthetics** (Victoria — hand-rolled `aesthevaclinic[@]gmail.com`) and
**Victoria Skin Care Centre** (Victoria — not pursued, solo operator). Clinics already in the
pipeline were skipped: **Clinique Versa MD** (Outremont / Mile End), the only Montreal row we
held before today.

**Never construct an address for any clinic on this list.**

---

## Cannot email — no address published at all

| Clinic | City | Why it qualifies | Why we can't email |
|---|---|---|---|
| **Spa Lumina** | Barrie, ON (1005-74 Cedar Pointe Dr) | **The best unemailable clinic of the run, and the deepest trading history found anywhere in it.** States "Since our establishment nearly 15 years ago" — about fifteen years of lapsed patients. Runs **VIP Rewards on RepeatMD** (`spalumina.repeatmd.com`), a membership programme and a promotions page. Injectables-led with a full device menu | **Nothing, on three pages.** No address on the homepage, none on `/contact/` (an "Email Us" link that resolves to the contact form, not a mailbox), and none in `/privacy-policy/`. Phone and form only. A browser will not help |
| **Protea Medispa** | Barrie, ON (682 Veterans Dr, Suite #1) | "DR. DA SILVA" named in the About menu, a 2024 Platinum award for medical aesthetics in Barrie, **a stale 2021 footer copyright beside a live site** (trading proxy), VIP and VIP MINI menu items, refer-a-friend | No address on the homepage and none in `/privacy-policy/`, which was read in full. Wix contact form only |
| **413 Medical Aesthetics** | Barrie, ON (494 Veterans Dr #8) | Injectables-led, physician-supervised, an injector-training arm, a 2023 footer copyright | No address anywhere read. **One thing to chase if anyone returns to Barrie:** a form consent line reads "I agree to receive promotional messages from **The Aesthetic Edit, LLC**" — a *different* company's name on the clinic's own opt-in. That is not the Vos loyalty-link tell, but it is a name above the clinic and it should be resolved before this is ever sent anything |
| **ClaraDerma+** | St Catharines, ON (300 Bunting Rd Unit 12) | **Two named leaders** — Olenka Lyle NP (Nurse Practitioner / Medical Director) and Alicia Yap (Founder & Education Director). Jane App. **Complexion Collective Membership**, gift cards, Beautifi financing. A privacy policy with an **effective date of 31 December 2016**, which is a real ten-year trading proxy | No address on the homepage and none in `/site/privacy-policy/`, read in full. Phone `(905) 397-7075` and a subscribe form only. *Caveat even if an address turns up:* women's hormone optimisation, weight loss and stem-cell collection sit on the menu |
| **Nurse Niagara / Nurse Aesthetic & Holistic Clinic** | Niagara Falls, ON (Unit B-1, 4725 Dorchester Rd) | **Mary Reinhart named as founder**, a registered nurse. States the business began as Laser Hair Removal Niagara "over 9 years ago" — a nine-year trading history. Fresha booking and Fresha gift cards | No address on the homepage and none in `/privacy-policy/`, read in full. *Caveat even if one turns up:* the menu carries erectile-dysfunction treatment, Emsella for bladder control and **in-home nursing and care**, which reads part nursing agency and would need the cash-pay question |
| **ESME Esthétique** | Montréal (Villeray — 8344 rue Saint-Denis, suite 2) | Facial injections on the menu, **a points scheme on every purchase** and **gift cards with no expiry date** — two real dormant-list signals. Third-party booking at `esme.datedechoix.com` | No address on the homepage and none on `/contact/`, both read. The footer prints the words "Politique de confidentialité" with **no URL behind them**, so there is no policy page to open. Form and phone `514 825 5471` only |
| **Clinique Révolution du Plateau — homepage** | Montréal (Plateau) | — | Listed here only as a pointer: nothing is published on its homepage or `/our-locations/`. **It became a row anyway** because the doctor's own mailbox sits inside `/privacy-policy/`. See finding 1 below |
| **L'atelier Medical Aesthetics** | Winnipeg (186 Provencher Blvd) | **"Atelier Aesthetics is owned by Joelle Touchette, Nurse Practitioner and Skin Specialist"** — ownership stated outright, which is rare. Jane App (`lateliermedicalaesthetics.janeapp.com`). Injectables-led | No address on the homepage, no privacy policy linked, and **`/contact` returned a client error on 2026-10-28**. One Wix page away from being a row — **Jess can open `ateliermedicalaesthetics.com/contact` in her browser and this is probably a free B** |
| **Mouna MédiSpa** | Montréal (Saint-Laurent) | Unknown — could not be assessed | The homepage returned **nothing but a viewport meta tag and a title**: a client-side-rendered site that serves no text to a fetch. Not obfuscation and not a refusal — simply unreadable. **Jess can read this one in a browser**; Saint-Laurent produced no rows otherwise |

## Cannot email — address present but could not be read

Per the standard these count as **not seen**. Both are readable in a normal browser, so if
Jess opens the page herself they become pipeline rows — but read the rule-out note on each
first, because neither would clear the must-haves as things stand.

| Clinic | City | What happened | Would it qualify anyway? |
|---|---|---|---|
| **Institut Brabant** | Blainville, QC (876 Curé-Labelle, suite 102, plus an appointment-only second address at Ascension) | **Cloudflare** — every address renders as `[email protected]` in both header and footer | **No.** Founder **Nathalie Brabant**, a nurse injector and member of the Ordre des infirmières du Québec since 1989, **founded the institute in 2007** — nineteen years of trading and the best history in the Quebec half of the run. But the menu carries **small varicose veins in the legs** and a **"Minor Surgeries Interventions"** block, which fails the cash-pay must-have on the same reading that ruled out Lakeshore Vein. Gift cards offered. Recorded in full because if the standard ever widens on vein work this is the first clinic to revisit |
| **DermaSpa** | Victoria + Nanaimo, BC (101-1830 Oak Bay Ave; 3531 Uptown Blvd, Victoria; 404-1515 Dufferin Cres, Nanaimo) | **Cloudflare** — renders as `[email protected]` | **No.** Ruled out twice over: the named principal is **Dr Harlow Hollis, a plastic surgeon** of forty years, which is a straight disqualification, and the menu carries spider-vein and leg-vein laser work plus peri/menopause hormone therapy. Three sites across two cities |

## Ruled out on the standard — don't revisit

- **Station L Médi Spa** (1304 Greene Ave, Westmount, Montréal) — **extensive cosmetic surgery**: facial, breast, body-contouring, intimate and hand procedures, plus "Ablation de lésions et grains de beauté mineurs" (minor lesion and mole removal). Surgery practice. Publishes `info@stationl.ca`, so it would otherwise have been contactable — the menu is what rules it out. Webflow site, no platform named, "© 2025 Station L Médi Spa".
- **Reimagine Clinic** (3554 av Coloniale, Montréal) — **fails cash-pay on the menu**: mole removal, skin-tag and wart removal, seborrheic keratoses, plus psoriasis, eczema, onychomycosis and xanthelasma as listed concerns, and "Laser Vascular Lesions" with spider veins. That is the dermatology-and-lesion profile the standard disqualifies. Publishes **two** addresses — `reimagineclinic@gmail.com` and `info@reimagineclinic.ca` — and books on Vagaro, so it was fully contactable. Gift cards.
- **Clinique Rheia** (8000 boul Décarie, suite 310, Montréal) — **fails cash-pay and reads multi-specialty**: Medical Dermatology, a Family Medicine Clinic, Integrative Medicine, Specialized Gynecology, Private Endocrinology & Metabolism, Clinical Psychology and blood work sit beside the aesthetics, and the FAQ says some treatments may be covered depending on the insurance plan. Jane App; Integrative Medicine, Family Medicine and Aesthetics memberships. Same profile as Philosophy of Beauty (North York), but worse — parked that one, rule this one out. No address published either.
- **Sona MD** (#202-755 McGill Rd, Kamloops, BC) — **fails cash-pay on the menu**: the page offers **"Skin Cancer Care and Dermatologic Solutions"**. Skin-cancer work is an outright fail. Also calls Kamloops "our main office", which implies an unresolved site count. Publishes `info@sonamd.ca` and books on **Zenoti**, so it would otherwise have been a strong row — the menu is what rules it out.
- **Clinique Face MD** (Le Sud-Ouest, Montréal) — **facial plastic surgery** practice ("Chirurgie plastique faciale et médecine esthétique"). Not opened beyond the search result; ruled out on the stated specialty.
- **Clinique Médicale Esthétique LABELLE / medlabelle.com** (Laval) — its own page heading reads **"PRIVATE FAMILY MEDICINE"**. Multi-specialty private practice, not an owner-operated aesthetics clinic. Not opened; unverified beyond that heading.
- **Whistler Medical Aesthetics** (Whistler, BC) — **already disqualified**: it is one of the named acquisitions of **Vos Collection**, the May 2026 rebrand of MedSpa Partners Inc (PE-backed, 35+ clinics, cross-clinic loyalty programme). It was the *only* independent-looking aesthetics clinic a Whistler query returned. `whistlermedicalaesthetics.com` was blocked from later searches and should go in the brief's `blocked_domains` list beside `voscollection.com`. **Whistler is a one-clinic town and the one clinic belongs to a group — do not sweep it again.**
- **Vic Park / vicpark.com — Winnipeg Grant** — a Winnipeg location of the multi-clinic group already ruled out on 20 Oct. It surfaced in a Winnipeg neighbourhood query and was blocked. Worth knowing that the group is now in Manitoba.
- **Clinique Praxis Esthétique** (Blainville, Terrebonne, Montréal Downtown, La Prairie, Laval) — five clinics, already ruled out 20 Oct. It still owns the North Shore result pages; blocked by name in the Laval queries, which is what made that market produce.
- **Clinic 805** (Victoria, BC) — already ruled out as "Cosmetic Surgery & Medical Aesthetics" on 20 Oct. It is still the first result for a Victoria aesthetics query; blocked.

## Not pursued — thin on the lapsed-list test, or out of budget

Single-operator personal-brand sites, host-salon rooms, and clinics whose names surfaced but
which were not opened:

- **Dr Anna MD** (#322-1964 Fort St, Victoria, BC) — opened, and closest of this group to a row: "Dr. Anna" is the only name, no surname and no credential, a 2023 footer copyright, phone-only booking, no address published, and the menu carries **sclerotherapy for spider veins** plus treatments for skin tags and nail fungus. Fails on the address and probably on the menu.
- **Lumera Skin Clinique**, **ML Aesthetic Clinic** (an acne-led clinic), **Clinique Main d'Or**, **Le Médispa de Maisonneuve**, **Clinique AG Montréal**, **Clinique Cosmedic**, **Clinique EuroDerm Med Spa**, **Dermamode**, **MEDIX**, **Mediluxe**, **CHIC Medispa**, **La Déesse**, **RITUALES**, **Griffintown Med Spa**, **Centre Esthétique Montréal Vieux-Port**, **Medispa Physimed** (Saint-Laurent), **Injections by Lydia** (Westmount), **Spa Médical Mont-Royal**, **Clinique Grace** (Villeray), **Zoe Medical Aesthetic** (Côte Saint-Luc), **Nuvo Medispa** (LaSalle), **The Aesthetic Clinic / TAC** (Dorval) — all Montréal names harvested from two directory index pages and left unopened on budget. **This is the largest block of pre-identified, unopened Montréal candidates we have ever had**, and it is worth one more worker.
- **Clinique CS**, **Clinic Esthetic MD**, **Dr Bernier** (Laval) — surfaced, unopened.
- **Clinique Nios** (Sainte-Thérèse) and **Humani** (Rosemère / Blainville / Saint-Jérôme) — private *medical* clinics rather than aesthetics; not opened.
- **Simply Radiant Aesthetics** (Winnipeg) — its own search title reads "Medical Spa & **Dermatologist** in Winnipeg". Not opened; treat as a probable dermatology rule-out rather than a confirmed one.
- **Visage Clinical Beauty**, **Inskin MediSPA**, **Advanced Cosmetics Clinic**, **Astro Medical Aesthetic**, **Enhance Medical Aesthetics** (a bare Squarespace preview domain) — Winnipeg, surfaced and unopened. **Winnipeg has depth left.**
- **Injector Daniel**, **AGLS Medical Clinic**, **Advanced Laser Skin Clinic & Tattoo Removal**, **Barrie's Best Medspa** (Barrie) — surfaced from a directory index, unopened.
- **NV Beauty Boutique** (St Catharines) — surfaced only as 2020 and 2021 blog posts, which reads stale; unopened.
- **Dr Marissa Gaucher** (Kelowna, Kamloops and Lake Country) and **Dr Kaleb Falk** (Kamloops) — travelling-injector pages across three towns; one decision-maker each under the standard, but both read as a physician's satellite listing rather than a clinic with a patient list. Unopened.
- **Drgblackburn / Clinique DGB** (Vieux-Montréal + Bromont) — its own homepage title is "**Surgical** & Non-Surgical Medical Aesthetic Clinic". Not opened; probable surgery rule-out, and the directory also files it under Médispa Victoria Park, which is a blocked group.

---

## What this sweep taught us about Canada, round 3

**1. The privacy policy is now the single most productive page in Canada, and that is a
change of routine, not a tip.** Two of today's twenty-two rows exist *only* because of it —
**Clinique Révolution du Plateau**, where the doctor's own mailbox `y.moyal@…` sits inside
`/privacy-policy/` and nothing is published on the homepage or the locations page, and
**Revery Medical Aesthetics** in Windsor, the only emailable clinic found in that city, whose
address is in section 10 of its policy. Add Sparkle (Moncton, 21 Oct) and that is three
rescues in two sweeps. But note the cost honestly: the same page produced **nothing** for Spa
Lumina, Protea, ClaraDerma and Nurse Niagara, each of which was read in full. It is worth one
fetch on every Canadian clinic that publishes nothing elsewhere, and it is still a coin flip.

**2. Montreal is a better market than English Canada, and the thing that makes it better is
ownership language.** Eleven sendable rows from the island and Laval against nine from the
whole of English Canada today, and the French sites say who owns the business in a way the
English ones do not. **DermaMédiBeauté** prints "Infirmière injectrice & **co-propriétaire**"
in two practitioners' own job titles. **Clinique La Clé** says in terms that it is
"physician-owned and physician-operated". **La Clinique DC** publishes its numbered Quebec
company in its policy, and **Clinique CD** publishes "Clinique CD Médico-Esthétique Inc." The
20 Oct finding that "Quebec sites name the owner more readily" **did not hold in Québec City**
on 21 Oct and **does hold on the island of Montreal** — so the finding was right about Quebec
and wrong about which Quebec. Four of nine Montreal/Laval rows name an owner or state
ownership outright; of the nine English-Canadian rows today, two do.

**3. A French-only site cost nothing, and the French words were the whole lever.** Not one
clinic was skipped for language. The query that opened the city was neighbourhood alternates
in French — `"Plateau-Mont-Royal" OR "Mile End" OR "Griffintown" OR "Vieux-Montréal"` with
`clinique médico-esthétique` and `injectrice fondatrice` — which is the Yorkville technique
from 21 Oct translated. `politique de confidentialité` and `nous joindre` are the page names
to look for, and two sites print the words "Politique de confidentialité" with **no URL behind
them**, which is a Quebec-specific dead end worth knowing: there is no page to open, so Jess
cannot rescue it in a browser either.

**4. Two directory index pages produced more candidate names than every search combined, for
two fetches.** `mtlpages.com/med-spas/` gave a by-neighbourhood list and
`thecliniccompass.com/montreal/` gave **34 independent Montreal clinics** with neighbourhoods,
after excluding the chains. Neither publishes clinic domains, so each name still costs a
search to resolve — but the brief's rule is to *block* directory farms in search results, and
that is still right. This is the opposite move: **fetch one directory index deliberately, as a
name source, once per metro.** It is why the "not pursued" list above is so long, and those
names are a worked-out market waiting for a second worker.

**5. Winnipeg was empty of nothing — it was empty of queries.** The city held zero rows this
morning and holds five tonight, four of them sendable, and the one query shape that did it was
`"medical aesthetics" OR "med spa" Winnipeg` with **neighbourhood alternates** (`"St. Vital"
OR "Osborne" OR "Tuxedo" OR "Transcona"`) plus `"info@"`. Every Winnipeg clinic opened
published a readable address except two, and **Uplift Aesthetics is the only grade A found
outside Ontario today**. Winnipeg also behaves like Saskatchewan on history: of five rows only
Enhance (founded 2017, stated) carries a founding year.

**6. The parent-group tell did its job again, and this time it saved a whole town.** Whistler
returned exactly one independent-looking clinic and it is a **named Vos Collection
acquisition**, so Whistler is structurally closed to us — a one-clinic resort town whose one
clinic has its recall channel owned above it. **Vic Park now has a Winnipeg location**, which
is new; the group is spreading west. And a second, weaker form of the tell turned up in
Barrie: **413 Medical Aesthetics** asks consent to receive promotional messages from "**The
Aesthetic Edit, LLC**" — another company's name on the clinic's own opt-in form. That is not a
loyalty link and it may be nothing but a marketing vendor, but it is the same question (whose
list is it?) and it is recorded so whoever reaches that clinic asks.

**7. The real Canadian filter is still trading history, and it is getting worse, not better.**
Of twenty-two rows today, **three** publish any usable trading proxy: Enhance ("Founded in
2017"), La Clinique DC ("More than 5,000 people treated since 2021" — which is a trading start
*and* a rough list size, the single best line found in three Canadian sweeps), and Revive
(fifteen years of the founder's own career, which is not the clinic's). Nineteen rows say
"established not verified" out loud. Two carry **no copyright year at all** —
DermaMédiBeauté's footer reads "© DermaMédiBeauté. Tous droits réservés." with no date, and
Niagara Medical Esthetics has none either — so the stale-copyright proxy from 21 Oct is not
always available. The clinics with the deepest history are, maddeningly, the ones we cannot
email: Institut Brabant (founded 2007, Cloudflare), Spa Lumina (fifteen years, nothing
published), ClaraDerma (a 2016 policy date, nothing published).

**8. The CASL consent screen has now disqualified zero Canadian clinics across three sweeps.**
Thirty-four clinics examined today, **sixteen privacy policies read in full**, and not one
statement anywhere refusing unsolicited commercial email. Combined with the earlier sweeps:
sixty-three clinics, twenty-eight policies, zero refusals. It remains a recording cost and it
must still be written down, but the brief's instruction to do it **last** is correct and the
budget should be spent on the menu first. What *does* vary is whether a policy exists at all:
**eight of today's twenty-two rows publish no privacy policy whatsoever**, which the row
records honestly as "could not be read because none is published". One is worse than absent —
Niagara Medical Esthetics has a footer "Privacy Policy" link whose href is a placeholder `#`,
so there is no page behind it and nobody, in a browser or otherwise, can read it.

**9. A domain mismatch is now the majority case in Canada.** Six of twenty-two rows publish a
mailbox on a domain other than their website — `info@lacliniquedc.com` on `cliniquedc.com`,
`info@cdmedicoesthetique.com` on a `.ca` site, `info@skinsuitewpg.ca` on a `.com` site,
`jessjacob@injectionnurseclinic.com` on `theinjectionnurse.com`, and **both** of the Victoria
clinic's addresses on `BritishColumbiaBotoxClinics` while the site is `victoriabotoxclinic.com`.
None was corrected. The 22 Oct Australian figure was 9 of 25; Canada is now at about the same
rate, so this should be treated as normal and flagged in every row rather than remarked on.

**Dry holes, documented so nobody sweeps them again:** **Whistler** (one clinic, group-owned —
structurally closed, not thin) · **Saint-Laurent** (three clinics surfaced, one unreadable, no
rows) · **Mile End and Griffintown** proper (every name a chain or a page of another borough's
clinic; the Plateau and Old Montreal carried the central-Montreal rows instead) ·
**St Catharines** (ClaraDerma is the market and it publishes nothing).

**Unresolved rather than dry, and each one browser visit from settling:** **L'atelier Medical
Aesthetics** (Winnipeg — ownership stated outright, `/contact` returned a client error) ·
**Mouna MédiSpa** (Montréal Saint-Laurent — a client-rendered page that serves no text) ·
**Distinction MD**'s `mentions légales` page (the one candidate consent page on the site,
returned a client error).

**Depth left, in the order worth working:** the **34 unopened Montréal independents** listed
above, which is a whole second sweep already identified and needs only domain resolution ·
**Winnipeg**, where five of ten candidates were never opened · **Barrie**, where four of seven
directory names were never opened · and **Victoria, BC**, which took five queries to yield one
row and is the hardest market of the nine — its visible layer is a plastic surgeon, a cosmetic
surgery practice and a clinic with hand-rolled obfuscation, all three already ruled out before
today.

# US under-covered metros — near misses and rule-outs, 28 October 2026

Markets swept: Minneapolis–St Paul MN; Detroit and suburbs, Grand Rapids and Ann Arbor MI;
Indianapolis IN; St Louis and Kansas City MO; northern New Jersey (Hoboken, Jersey City,
Montclair, Summit, Short Hills, Morristown, Red Bank, Ridgewood, Paramus); Louisville and
Lexington KY. Chicago, Columbus, Cleveland, Milwaukee, Madison, Omaha, Lincoln, Des Moines,
Cedar Rapids, Nashville and Cincinnati were treated as already covered and not re-swept.

Everything below clears the ICP on profile and fails on the address, or fails the standard for
a stated reason. **28 rows went into `us-28oct.json`** (1 grade A, 27 grade B) plus 7 parked
at C, each naming the must-have it fails by number.

---

## Group 1 — Address present but obfuscated (Jess can read these in her own browser in seconds)

Only two in the whole sweep, which is far fewer than the Australian and UK runs produced.

### Complexion Med Spa — 7423 Orchard Lake Road, West Bloomfield MI 48322
https://www.complexionspa.com/
Chantal Bacall is named as **Founder**. Books on Boulevard (a joinblvd.com widget), sells gift
cards through it, and links a payment-plans page. Deep device and injectable menu — HydraFacial
MD, OxyGeneo, IPL/RESURFX by Lumenis, Emsculpt Neo, eight filler brands — plus a tanning arm.
Clean cash-pay menu: no surgery, no vein work, no hormones, no insurance billing.
**Blocker:** the visible text renders as `[email protected]`. By the rule that is **NOT SEEN**
and nothing was recorded. One browser tab from being a B row.
No founding year, no review count.

### The Refinery Skin Clinic — 13903 Aldrich Ave South, Burnsville MN 55337
https://therefineryskinclinic.com/
**The best Minnesota clinic I could not record.** Three named memberships — Glow Getter
DiamondGlow, Year Round Radiance Skincare, and **Elite Refinement Injectables** — plus Allē
Rewards, gift cards and financing. Books on **EnvisionGo**, texts through Weave, sells skincare
through Brilliant Connections and supplements through Fullscript, which is a more built-out
stack than most rows that did qualify. Serves Burnsville and Lakeville.
**Blocker:** the visible text renders as `[email protected]`. The fetch tool happened to
decode the underlying mailto, but the page itself does not display it, so by the rule it is
**NOT SEEN and I did not record it** — Jess should read it off the page herself.
No founding year, no review count; Google reviews are linked without a total.

---

## Group 2 — No email address published anywhere I fetched (a browser will NOT help these)

### Minnesota

**Remedy Medical Aesthetics & Wellness** — 7767 Elm Creek Blvd, Suite 100, Maple Grove MN
(`remedywellnessclinic.com`). Led by **Kristina Thissen, PA-C** (named, though not stated as
owner). **Boulevard** confirmed, VIP Memberships page, gift cards through blvd.me, a "Join The
List" signup. Menu carries hormone replacement and BHRT pellet therapy alongside the
aesthetics. No email anywhere including the footer; no founding year, no review count.

**Expressions MD** — 15120 Chippendale Avenue, Suite 101, Rosemount MN
(`expressionsmd.com`). **Glenn Detlefsen, M.D.** named. A badge reads "20+ Years of trusted
exprerience" (their typo), which is a real tenure proxy and better than most rows that
qualified. No platform, no scheme beyond CareCredit and Cherry. No email anywhere.

**Sapphire Advanced Aesthetics** — 2 Carlson Parkway Suite 120, Wayzata MN
(`sapphireadvancedaesthetics.com`). **Leslie Smith, D.O.**, named founder, board-certified
surgeon and cosmetic physician. Also **ruled out on the standard**: the menu carries mini tummy
tuck and "any surgery or laser package", plus spider and laser vein treatment and hormone
replacement. Fails must-have 1 and must-have 2. Recorded so nobody re-sources it. No email either.

**The Med Spa Woodbury** — 10035 City Walk Dr, Suites A & B, Woodbury MN
(`themedspawoodbury.com`). "Membership Plans" and "Gift Cards" both in the navigation, a
Woodbury Magazine Best of '25 award. Nobody named at all, BioTE hormone pellets on the menu.
No email anywhere.

**Dr Ann Marshall Aesthetics** — 4420 Valley View Road, Edina MN (`drannaesthetics.com`).
**Boulevard** confirmed for booking, gift cards and referrals; single Edina site; CareCredit in
the footer. Ten testimonials, no total. No email on the homepage — and per our own notes
`/contact` has been worse than the homepage in two consecutive US sweeps, so I did not spend
the second fetch. **Cheapest unresolved lead in Minnesota: one About-page or /contact fetch.**

**Art of Injections** — Minneapolis MN (`artofinjections.com`). **robots_disallowed — could
not be fetched at all.** Structurally unreachable by our tooling; needs a browser.

**Skin By Liv Aesthetics** — Woodbury MN (`skinbylivaesthetics.com`). **robots_disallowed —
could not be fetched at all.** Same handling.

**Aesthetic Repository** — North Loop, Minneapolis MN (`aestheticrepository.com`). Fetch
returned a client error. Unresolved rather than ruled out.

Already on file from 19 Oct and re-confirmed as still the two best unreachable Minnesota
clinics: **Metropolitan Skin Clinic** (Edina, Suzanne St. James named Injector/Co-Owner,
Zenoti) and **Skin Artisans** (Edina/Minnetonka/Woodbury, NextPatient). Neither was re-fetched.

### Michigan

**Studio 4955 Aesthetics** — Grand Rapids MI (`studio4955aesthetics.com`). **Ramin Rahimi, DO,
FAAPMR**, dual-board-certified, plus Heidi Rahimi RN BSN and Ashley Byrnes FNP MSN — three
named clinicians, which is a stronger team page than any Grand Rapids clinic that qualified.
Books on **Aesthetic Record**, runs a membership with service discounts and priority
scheduling, plus seasonal specials and payment plans. "Vascular Reduction" on the menu.
No email anywhere; "Email" appears only as a form field label. **The best Grand Rapids lead
and the one to put in front of Jess first.**

**The Aesthetics Studio** — 47792 Van Dyke Avenue, Shelby Township MI
(`theaestheticsstudiomi.com`). **Founded 2023** — stated outright, which almost never happens
in the US — "locally and woman-owned", team with "over 15 years of industry experience".
**Boulevard** confirmed, gift cards, payment plans, free consultations. Hormone replacement on
the menu. Nobody named. No email anywhere.

**Bella Rosa Med Spa** — West Bloomfield MI (`bellarosamedspa.com`). Free consultations, laser
and injectable menu. Nobody named, no scheme, no tenure evidence, and the menu drifts into
gynaecological and sexual-health procedures. No email anywhere. **Low priority even with an
address** — it is thin on every axis.

### Missouri / Kansas

**Illume Med Spa** — 817 NE Anderson Ln, Lee's Summit MO (`illumemedspa.com`). **Glen Fansler**
named, "an aesthetic injector with more than a decade of experience". Monthly memberships, and
aesthetic consultations are complimentary. Hormone therapy and TRT on the menu. Built on Wix
with no platform named. No email anywhere including the footer. *Note: this is a different
business from Illume Cosmetic Surgery & MedSpa in Wisconsin, already a near-miss from 16 Oct.*

**Karma Beauty and Wellness** — Lee's Summit MO and Overland Park KS
(`karmabeautyandwellness.com`). Also **ruled out on the standard**: it sells **direct primary
care memberships** with unlimited provider visits and has **Pap smears** under sexual wellness,
alongside HRT, thyroid optimisation and peptides. That is a multi-specialty medical practice,
which fails must-have 1. No email either, and nobody named. Recorded so nobody re-sources it.

### Indiana

**317 Aesthetics** — 320 N Meridian St Ste 110, Indianapolis IN (`317aesthetics.com`). Found by
the bank/vault search and it does run a real **"Beauty Bank"** — "$99 each month, your fees
accumulate into a Beauty Bank" (the page also calls it a one-time signup fee with annual
renewal, and does not reconcile the two). **But also ruled out on the standard:** it is "proudly
led by Christopher Jones MD", the banner links out to plastic surgery at
`ChristopherJonesMD.com`, and the Beauty Bank's own benefits include "a free surgical
consultation with Dr. Jones". Fails must-have 1 and must-have 2. No email anywhere either.
Logged so nobody re-finds the Beauty Bank and thinks the missing address is the only problem.

### Kentucky

**Beautiful You Medical Spa** — 3801 Dylan Pl Ste 110, Lexington KY
(`beautifulyoumedspa.com`). Says **"13 Years In Business"** outright — the best published
tenure of any Kentucky clinic I opened, and better than all three Kentucky rows that qualified.
Books on **Booker** (go.booker.com), sells gift certificates through it, runs monthly specials.
Rae Eaves, NP named for peptide consultations. No owner named, no review total. No email
anywhere including the footer. **The Kentucky clinic most worth a phone call.**

**Luxe Lounge Medspa** — 867 E High St, Suite 230, Lexington KY (`luxeloungemedspa.com`).
Already a 20 Oct near-miss; **re-checked today and it still publishes no email address**, so the
earlier verdict stands and nobody should spend the fetch again. Worth noting what it does
publish, because it is the strongest Kentucky profile on file: **Jenny Ash, RN** named as
Aesthetic Injector and Owner and a certified Master Injector, **Alyssa Fleming, FNP-C** named as
Owner, Aesthetic Injector and Medical Director, and **"521+ Reviews" at 5.0** — a published
review count, which is rare here. Aesthetic Record, gift cards. Two named owner-injectors and
521 reviews make this the best unreachable clinic in the sweep.

---

## Ruled out on the standard — do not re-source

**Five or more sites (must-have 3):**

- **Mosaic Luxury Medical Spa** (`themosaicspa.com`) — publishes `info@themosaicspa.com`, so it
  is perfectly contactable, and runs on **Boulevard** with memberships and gift cards. But it
  lists **five locations: Berkley, Troy, West Bloomfield and Clinton Township MI plus Naples,
  Florida**, and claims "over 2500 clients". Five sites across two states is head-office
  marketing. **Out on profile, not on contactability** — this is the roll-up filter the small-town
  sweeps never had to run, and it caught exactly one clinic.
- **Ethos Aesthetics + Wellness** (`myethosspa.com`) — multi-site northern NJ brand with a
  locations page and an expansion press cycle (a Hoboken opening announced separately). Not opened.
- **Evolve Med Spa** (`evolvemedspa.com`) — multi-state chain with per-city location pages. Not opened.
- **Rajeunir Medical Spa** (`rmedspa.com`) — Kansas City, Springfield, Overland Park and Lee's
  Summit off one brand. At or over the ceiling; not opened.
- **Chapter Aesthetic Studio** (`mychapter.com`) — national chain, surfaced on an Eagan MN query.
- **S2G Medical Spa** (`s2gmedspa.com`) and **Front Door Med Spa** (`frontdoormedspa.com`) —
  both surfaced on the Detroit-suburb query with multi-location or "areas we serve" structures.
  Not opened.
- **Urban You Medical Aesthetics & Wellness** (`theurbanyou.com`, Grand Rapids MI) — publishes
  **no email**, so it is a near-miss on contactability too, but the reason to record it is the
  scale question. It has the richest retention stack in the whole sweep — **Insider Access**
  membership, **UY Loyalty Points**, a corporate membership, a referral programme, a first-visit
  credit, treatment packages, Cherry and CareCredit, gift cards and a **Zenoti** booking app —
  and the page never states a location count. **Note the parent-group test came out clean:** the
  only externally-branded scheme is **Jeuveau Rewards hosted by Evolus**, which is the
  manufacturer's own programme and is NOT the parent-group tell. Copyright reads "URBAN YOU,
  LLC". If anyone revisits it, the one thing to establish is the site count.

**Plastic surgery or dermatology attached (must-haves 1 and 2):**

- **Plastic Surgery Arts / The Spa MD** (`plasticsurgeryarts.com`, Rochester Hills MI) — owned the
  Detroit-suburb result page; a plastic surgery practice with a med spa arm.
- **Bengtson Center / Symmetry Med Spa** (`bengtsoncenter.com`, Grand Rapids MI) — plastic surgery.
- **Cosmetic & Plastic Surgery of Ann Arbor** (`cpsaa.com`) — plastic surgery with a med spa team page.
- **Allure Medical** (`alluremedical.com`) — multi-site Michigan cosmetic surgery and wellness group.
- **Avani Derm Spa** (`avanidermspa.com`, St Louis MO) — dermatology-attached on the name; not opened.
- **Vital Skin Dermatology** (`vitalskinderm.com`, Middletown KY) — dermatology.
- **UK HealthCare Aesthetics Center** (`ukhealthcare.uky.edu`) — hospital system, buyer not in the room.
- **Avanti Skin Center of Louisville** (`avantioflouisville.com`) — franchise model.
- **Ageless Center** (`agelesscenter.net`) — Lexington, Louisville and London KY, a weight-loss-led
  three-site group; not opened.
- **Zero Gravity** (`zerogravitynky.com`) — Northern Kentucky, i.e. the Cincinnati metro, which was
  excluded from this sweep as already covered.

**Out of market (surfaced on an in-market search — do NOT count as coverage):**

- **Luxe Lift PLLC** (`luxeliftpllc.com`) — **Danville, ILLINOIS**, not Indiana, despite surfacing on
  an Indiana bank/vault query. Worth recording anyway because the profile is good and Illinois is
  already-covered ground: **Bobbi Fischer, NP** named as lead nurse practitioner, CEO and founder;
  **"Since 2021, we've been providing care"** — a published founding year, which is rare; a **"Beauty
  Bank"** membership whose "balance rolls over month to month", sold through a **ProspyrMed**
  storefront. It publishes **no email**, so it would have been a near-miss regardless.
- **Ageless Aesthetics** — opening a third central-Indiana site in Fishers per a press release.
  Three sites is inside the rule and this was never opened; **a free lead for the next Indiana run.**
- **Grand Beauty Aesthetics** (`grandbeautyaesthetics.com`) — East Lansing MI, outside the assigned
  Michigan markets. Not opened.
- **Downtown Med Spa** (`downtownmedspa.com`, Jersey City NJ) — in market, and **in the pipeline's
  only other NJ metro**, so worth its own note. Founded **2012** (published), founders **Dr Eric
  Reynolds and Marietta Reynolds** named, booking split across **Meevo** and **Vagaro**, powered by
  Tebra, a $50/$50 two-sided referral reward, Meevo e-gift cards, Pay With Cherry. **No email
  anywhere including the footer.** The page also contradicts itself on site count — it lists Jersey
  City and Edgewater as current, then says the founders "opened two additional locations in Brooklyn
  and Edgewater", which would make three. Published tenure and named founders make this the best
  unreachable New Jersey clinic.
- **Attain Med Spa** (`attainmedspa.com`) — Hoboken NJ plus New York NY, and the page says **"three
  locations (and growing)"** with Allenhurst and Charleston also named in the booking block, so the
  real count may already be four or five and is rising. **Lauren Ben-Meir** named as Founder and CEO.
  Memberships at $99 and $199 a month on a six-month minimum with a **monthly service credit**, which
  is a banked-credit scheme. **No email anywhere.** Unresolved on both count and contactability.

---

## What this market taught me

**A big metro nobody has swept behaves like the secondary cities, not like the September big
metros — with one qualification.** The accept rate against clinics that failed on the address
alone was roughly **2:1** (28 accepted, 14 unreachable), which is the secondary-city number from
21 Oct, not the ~1:2 the September big metros returned. But the cause is not that these metros
are structurally different from Chicago or Columbus. It is that **these are the big metros nobody
had picked over**, and the independent layer under the chains is still intact. The chain tax was
real but small: of roughly 55 clinics I seriously considered, **eleven were chains, roll-ups,
franchises or plastic-surgery groups** — about one in five, against essentially zero in the
small-town sweeps. That is a visible cost and it is nowhere near the September experience of
nine in ten results being a group or a directory. **Blocking the directory farms in the first
query remains the single biggest lever; blocking the groups was a second, much smaller one**, and
I only needed to name local groups once (Michigan, where `plasticsurgeryarts.com`,
`alluremedical.com` and `skinergymd.com` owned the Detroit-suburb pages until I blocked them).

**The footer rule held and `/contact` was never needed once.** Every single one of the 35 rows
had its address read off a **homepage, an About page, a locations page or a memberships page
footer**. I did not fetch `/contact` a single time and did not miss anything by it. Two
consecutive sweeps said `/contact` was worse than the homepage in the US; a third now says the
same. **Treat the homepage footer as the whole game and stop budgeting for `/contact` in the US.**

**The bank/wallet/vault search is the highest-yield query in this market and it should be run
FIRST, not last.** I ran it late and it was the single most productive query of the sweep: one
search produced **Artistry Aesthetics** in Forest Lake MN (a Beauty Bank whose funds, in its own
words, "do not expire"), **Üesthetics Indy** in Indianapolis ("your banked dollars roll over and
stay yours — even if you cancel"), **My Beauty Vault** in Elkhart IN, plus 317 Aesthetics and
Luxe Lift as near-misses. Every one held patient credit with names attached. The caveat our notes
already record is confirmed twice over: the phrase also returns **vendor marketing blogs** that
outrank the clinics, and it returns **false positives on the brand name** — My Beauty Vault has a
vault in its name and **no vault scheme behind it at all**. Verify the bank on the clinic's own
site; never trust it from a result title.

**Founding years are almost never published — and the near-substitutes are traps.** Only **three**
of 28 qualified rows state tenure: SimplySkin ("over 19 years"), Icon Anti-Aging ("Est. 2023") and
Synergi, parked at C ("20 YEARS IN BUSINESS"). For the other 25 I said so in `notes` and named the
proxy. **Two proxies worked and one keeps looking like a proxy and is not.** What worked:
a **published review count** (Icon 287, Embolden 63+30) and, newly, **a run of dated local
readers'-choice awards** — Artistry took Best Med Spa in Forest Lake for 2024 and 2025, Renew
MedSpa for Eagan in 2025 and 2026, Northville across 2019–2023. An award run is a dated,
third-party, year-by-year record of trading and it is the best proxy available when no review
total is published. **What does NOT work, and bit repeatedly: a practitioner's own years of
experience.** Seven rows carry a phrase like "decades of combined experience" (MK Aesthetics),
"over 25 years of combined experience" (Refine KC), "17 years each, before Beauty HQ" (Beauty HQ),
"25+ YEARS" (The Wellness at Ridgewood) or a testimonial saying the injector has practised 17
years (Prick'd). **Every one of those is a personal career and says nothing about how long the
clinic has traded** — Beauty HQ's is explicitly "before Beauty HQ". Each of those rows says so in
`notes` and flags that the oldest Google review needs eyeballing before sending.

**Minneapolis–St Paul was the hardest market and needed four query shapes to crack.** A metro-plus-
membership query gave one usable clinic. A neighbourhood-alternates query (Uptown, North Loop,
Grand Avenue, Linden Hills) returned **two results, one of them an assisted-living home** — the
worst query of the sweep. What finally worked was **stacking outer-ring suburb names** (Eagan,
Burnsville, Maple Grove, Stillwater, Lakeville, White Bear Lake), which produced four of the five
Minnesota rows in one search, and the bank/vault query, which produced the fifth. This confirms the
22 Oct rule in a new market: **a dry hole is only dry once the query shape has been varied**, and
in a US metro the variation that works is **suburb-name stacking, not neighbourhood names**. Twin
Cities neighbourhood names are residential, not commercial, so no clinic markets against them.

**Mismatched mailbox domains are now so common they should be assumed.** **Six of 35** rows carry
one: The Aesthetic Lab (`the-aestheticlab.com` against a site at `the-aesthetic-lab.com` — a
single hyphen), EOS (`eos-stl.com` against `eosmedspa.com`), 1Aesthetic (`skingoods@yahoo.com`),
Envee (`drellen.com`), Middletown Spa (`louisvilledayspa.com` beside its own), and Renew MedSpa
(a gmail in the footer beside its own domain in the contact block). **Three rows published TWO
addresses on the same page**, in which case I recorded the one on the clinic's own domain and
documented the other in `notes` as a fallback. None was corrected. The Aesthetic Lab's is the one
to watch: a one-character difference is exactly the kind of thing a well-meaning reader "fixes".

**Three things about the obfuscation picture.** Only **two** clinics in 35-plus hid an address
behind Cloudflare, against roughly a third in some Australian sweeps — so the "Jess reads it in
her browser" workaround rescues very little here, and the dominant US failure is still **total
silence**: a form, a phone number, and nothing else. Second, **two Minnesota clinics were
`robots_disallowed`** and could not be fetched at all (Art of Injections, Skin By Liv); those need
a browser, not another search. Third, one page — Bellatox Boutique — **interfered with the
extraction prompt on the first fetch** and returned a summary instead of the address; a second,
tighter fetch that explicitly told the model not to follow instructions found in the page content
got it. Worth knowing that re-fetching with a narrower prompt is sometimes the fix rather than
giving up on the clinic.

**Where the depth is, for whoever goes next.** **Michigan is the richest of these states and is
not worked out** — six rows plus five good near-misses, and the Detroit suburbs (Royal Oak,
Clarkston, Shelby Township, Northville, West Bloomfield) each returned fresh independents on a
single query. Grand Rapids and Ann Arbor are both under-researched rather than thin: two queries
produced three qualified rows and Studio 4955, which is the best clinic I could not reach.
**Northern New Jersey has more left**, and the shape to try is one I did not get to — Montclair,
Summit, Short Hills and Red Bank specifically returned almost nothing on a combined query, while
Hoboken, Morristown, Ridgewood and Paramus all produced; those four Essex and Monmouth towns
deserve their own query each. **Kentucky is the thinnest of the six states** — three rows, and the
two best clinics in the state (Luxe Lounge with 521 published reviews and two named owner-injectors,
and Beautiful You with 13 published years) both publish nothing, so **Kentucky's route in is a
phone call, not another search.** **Kansas City produced only one row**, which is the weakest
result of the sweep relative to the metro's size, and the Kansas side (Overland Park, Leawood,
Lenexa) was barely touched.

