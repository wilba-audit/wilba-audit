# Who we target, and how we qualify them

Current as of the Jess/Griffin call, 22 Sep 2026. This file is the qualification
standard for every new prospect. If a prospect does not clear "Must have", it does
not go in the pipeline.

## The offer we are selling

Reactivate the clinic's **existing dormant CRM leads** and convert them into booked
procedures. Paid as a **revenue share on procedures booked from those leads**, with
nothing upfront. We integrate with the CRM they already run — no migration.

Why it sells: the clinic's objection is risk. Fear of AI, fear of disruption, fear
of paying for something that might not work. Revenue share removes all three. They
are not buying software, they are getting paid-for-performance on a list they have
already paid to build and are currently not touching.

> **Unconfirmed:** the revenue-share percentage. The call landed on roughly 10% of
> procedures booked from reactivated leads. Do not state a number in any email until
> Jess confirms it. Draft as "a share of what it books, nothing upfront".

## Must have

1. **Med spa, aesthetic clinic, or plastic / cosmetic surgery practice.** Not
   general practice, not menopause or hormone clinics, not functional medicine.
2. **Evidence of scale consistent with $100k+/month.** We cannot read revenue off a
   website, so we qualify on observable proxies. Two or more of:
   - three or more practitioners, or a named surgeon plus support staff
   - more than one location
   - a surgical or high-ticket menu (breast, rhinoplasty, facelift, body
     contouring, thread lifts) or injectables priced per area with a full menu
   - memberships, package pricing, or financing offered
   - an active paid-ads presence, or a booking system implying real volume
3. **A CRM or booking system we can name.** Visible in the booking flow or the
   page source. Close, HubSpot, GoHighLevel, Cliniko, Pabau, Zenoti, Boulevard,
   Aesthetic Record, Nextech, PatientNow, Mindbody, Timely, HotDoc, SimpleClinic.
   No identifiable system means no integration story, so grade it C.
4. **A published email address, read off their own page.** Never constructed.

## Strong signals — grade A

- A named owner-surgeon or owner-injector whose name is on the door
- A CRM we have integrated with before, or one with a documented API
- Evidence of a lead list sitting idle: a long-running lead magnet, a "join our
  waitlist", years of Instagram follower growth, a consultation-request form that
  predates their current booking system
- Consultation fees that are redeemable, or free consults — means a pile of people
  who consulted and never booked
- Memberships or loyalty schemes — a list that lapses

## Disqualify

- Franchise or corporate chains where a head office controls marketing
- Single-operator studios with no support staff
- Anything where the only contact route is a form or phone (no email = no outreach)
- Practices whose domain redirects to another company

## What we record

Every prospect gets `crm_detected`, `scale_signals` and `dormant_lead_signal` filled
from their own site. Those three are what the opening line is built from. An opening
line that could be sent to any clinic is not an opening line.
