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
