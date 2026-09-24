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
