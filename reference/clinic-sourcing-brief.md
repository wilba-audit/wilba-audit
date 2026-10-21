# Brief for a clinic sourcing worker

Hand this file's path to every sourcing worker. **It lives in the repo on purpose.** It used
to live in the session scratchpad, which was wiped between runs on 20 Oct 2026 — three
workers that day ran with no brief at all, and one of them rebuilt the standard from
`outputs/pipeline/ICP.md` and the existing rows rather than stopping, which worked but was
luck rather than design.

Pair it with the qualification standard itself in `outputs/pipeline/ICP.md`, which changes
more often than this file and wins wherever the two disagree.

## What we are selling, so the openers make sense

WILBA works a clinic's **lapsed patients** — people who came once or twice and never
rebooked — over a few weeks of two-way SMS conversation, booking them back into the clinic's
own calendar, inside whatever system the clinic already runs. Paid as 10% of what it books,
nothing upfront. Workers do not write the email. They find and verify clinics.

## Must-haves, all of them

1. **Injectables or aesthetics-led.** Treatments wear off on a three-to-four month cycle,
   which is what makes a lapsed list worth recalling.
2. **Cash-pay.** No insurance or Medicare billing. Skin-cancer checks, vein work, urgent
   care and anything bulk-billed are a fail.
3. **Owner-operated, one to four sites.** Count them. Five or more means a head office
   decides marketing. But count **decision-makers, not addresses**: SEO suburb pages, one
   travelling nurse listing every town, and an injector renting a room inside a host salon
   all read as many sites and are still one buyer.
4. **Established**, with enough trading history for roughly 300+ lapsed patients.
5. **A published email address, read off their own site.**

Plus the regional screen for wherever the clinic is — see `ICP.md`, which carries the
Australian and New Zealand no-unsolicited-notice screen, the Canadian CASL conspicuous-
publication screen, and the UK and Irish company-identity screen.

## The absolute rule on addresses

**Never construct, guess or infer an email address.** Only ever record one seen verbatim in
fetched page content, and put the URL and the date in `email_source`. `info@<their-domain>`
that you did not actually read on a page is a fabrication even when it is probably right.

Four things look like a published address and are not. None is recoverable by opening the
page in a browser, so none goes in the pipeline:

- a Cloudflare-obfuscated address rendering as `[email protected]`
- a website-builder placeholder the owner never replaced (`filler@godaddy.com`, `contact@wix.com`)
- an address shipped inside a directory site's QR code image — directory data, not published data
- an address served in a page's Open Graph meta tags while the visible one is obfuscated

A clinic with no readable address is a near-miss, with the reason recorded, never a pipeline
row with a made-up address.

## Grading

**A** — owner-injector or owner-doctor named, a nameable practice system (Pabau, Fresha,
Zenoti, Cliniko, Timely, Boulevard, Aesthetic Record, GoHighLevel, Mindbody, Kitomba,
Dapple, RepeatMD), busy with real reviews, **and** a visible dormant-list signal: a
membership, a loyalty scheme, banked credit, gift vouchers, redeemable or free consults, a
waitlist, a lead magnet. **B** — clears every must-have, thinner on the above. **C** — close
but fails one must-have; still report it, marked C, with the reason. We park rather than drop,
because the standard may widen again and re-finding a clinic costs more than keeping it.

## Searching, in the order that actually works

1. **Pass `blocked_domains` for the directory farms first** — whatclinic, fresha, doctify,
   bookwell, top4, and the job boards. Before blocking them, nine of ten results are
   directory pages and no clinic domain surfaces at all. This is the single biggest lever.
   **Block these known groups in the same list**, all resolved and all disqualified, so
   nobody spends the fetches again: `voscollection.com` and `medspapartnersinc.com` (Vos
   Collection, the May 2026 rebrand of MedSpa Partners Inc — PE-backed, acquisitive, 35+
   clinics across the US and Canada, with a cross-clinic loyalty programme that already
   owns the recall channel we sell); `artisanclinics.com` (Artisan Aesthetic Clinics, a
   14-location Australian chain whose suburbs — Balmain, Bulimba, Maroochydore, Cairns,
   Toowoomba, Mosman, Robina, Gungahlin — overlap our AU targets almost exactly, so it
   surfaces constantly); and `craftedaesthetics` (six staffed Montana locations plus a
   training arm).

   **A parent-group loyalty link in the footer is the tell**, and it is the only one either
   of the Vos clinics gave. A loyalty programme branded for a company other than the clinic
   means marketing is decided above the clinic. Chase it every time you see one.
   Overlapping suburbs are not the same tell: Artisan runs its own branded clinics at those
   addresses, so our rows there are independents in the same market, not group members.
2. **Stack four or five suburb or town names into one query** with "membership", "nurse" and
   "contact", rather than one city at a time.
3. **Guess the clinic's likely domain and pass it as `allowed_domains`** with a generic query
   ("contact us email locations membership"). Search is US-weighted, so a brand-name search
   outside the US returns overseas spam — a Cambridge query once returned Cambridge, Ontario.
4. **Read the homepage and About-page footers before `/contact`.** `/contact` has been worse
   than the homepage in two consecutive US sweeps.
5. The **"wallet" / "bank" / "vault" plus a metro name** search works in the US, where it was
   learned, but it works indirectly: the phrase returns vendor marketing blogs that outrank
   every clinic. Its value is recognising a bank once you are on a clinic's own site. It
   returns nothing useful in Australia or New Zealand, where weekly-payment memberships and
   prize-draw opt-in lists are the equivalent signal.

WebFetch refuses a URL that has not appeared in a WebSearch result, so search before you
fetch. `curl` is blocked.

## The shared budget

WebSearch (200 calls) and WebFetch (400/hour) are **shared across every worker running at
once**, not per worker. On 16 Oct eight parallel workers starved each other and all eight
stopped short with candidates unverified. Three or four at a time, never more. If you are
running low, stop finding new candidates and finish verifying the ones you have.

## Output

A JSON array, one object per accepted clinic, with exactly these keys:

```
country, city, segment, clinic_name, lead_doctor, website, contact_email, phone,
contact_route, email_source, services, price_point, opening_angle, fit_flag, notes,
icp_fit, crm_detected, scale_signals, dormant_lead_signal
```

- `icp_fit` holds **the bare grade letter and nothing else**; `fit_flag` holds a short prose
  label. Two workers once had these the other way round, which would have made every row
  invisible to the drafting script.
- `price_point` — **leave empty**. We are not allowed to use prices in copy.
- `opening_angle` — one specific verified fact about *this* practice that an opening line can
  be built from: who owns it, how long it has traded, what scheme it runs, how many sites.
  **No prescription-medicine or treatment-category name** (no Botox, Dysport, filler,
  anti-wrinkle injections, "tox") and **no price, percentage or discount**, including the
  clinic's own published prices quoted back at it.
- `notes` — your own caveats, uncertainty, and the regional screen findings. Where you
  inferred "established" rather than reading a founding year, say so and name the proxy.
  Do not smooth any of this over: whoever writes the email reads this field.

Also write a near-misses file: clinics that clear the ICP but publish no readable address,
each with why email cannot reach them — **no address published at all** versus
**Cloudflare-hidden**, which need different handling, since Jess can read a hidden one in her
own browser in seconds. End it with a short paragraph on what the market taught you.

Then report back in under 300 words: how many rows, how many A, the file paths, what you ran
out of, and anything that surprised you.
