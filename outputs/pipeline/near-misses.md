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
