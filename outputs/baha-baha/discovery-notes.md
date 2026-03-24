# Baha Baha Villas — Discovery Call Notes

**Date:** 2026-03-23
**Participants:** Jess Morrell (WILBA), Sean (owner — Baha Baha Villas)
**Meeting recording:** https://app.fireflies.ai/view/Jess-Sean-AI-setup::01KMCH6K2GHZNAK5YAJ4AVJK35
**Purpose:** Scope AI Receptionist + Daily Briefing Agent for Baha Baha Villas

---

## Property Overview

**Baha Baha Villas** — surf and accommodation property in West Sumbawa, Indonesia.
Owner: Sean
Primary market: International surf travellers + package guests

---

## Tech Stack (Confirmed)

| System | Tool | Notes |
|--------|------|-------|
| Website | Squarespace | Public-facing site |
| Property Management System (PMS) | Booking Layer | Primary bookings system |
| Channel Manager | Channex | Connects Booking Layer to OTAs (Booking.com, Agoda, etc.) |
| Manual bookings | Instagram, WhatsApp, walk-ins | Not auto-captured in Booking Layer |
| Email | Gmail | All comms run through Gmail |
| Cloud storage / docs | Google Drive | Shared team documents |
| Accounting | Jurnal.co.id | Indonesian accounting software |
| Point of Sale (POS) | Mockapos | In-property purchases, F&B |
| Surf vendor | World Surfaris | Key external surf package partner |
| Flight reference | Travelova | Guests book flights here (reference for arrival times) |
| Booking email address | bookings@[bahavillas] | Incoming booking / inquiry email |

---

## Booking Sources

1. **Booking Layer** — primary PMS; receives bookings from:
   - Direct website (Squarespace → Booking Layer widget)
   - OTAs via Channex channel manager (Booking.com, Agoda, etc.)
2. **World Surfaris** — external surf package vendor; sends their own bookings separately
3. **Manual / off-system:**
   - Instagram DMs
   - WhatsApp
   - Walk-ins

**Gap identified:** Manual bookings and World Surfaris packages are NOT automatically in Booking Layer. This is the fragmentation problem to solve.

---

## Key Observations from Call

- Team currently has to check multiple systems every morning to understand who's arriving/leaving
- World Surfaris sends surf package bookings in their own format (likely email or PDF confirmation)
- WhatsApp is heavily used — both for guest comms and potentially manual booking intake
- Gmail is the central email hub — good news for Phase 2 (email responder)
- Channex as channel manager means OTA bookings DO flow into Booking Layer automatically
- Mockapos handles in-property sales (drinks, food, extras) — future data source for revenue reporting

---

## Open Items (To Clarify Next)

- [ ] What are the exact room/villa names and types?
- [ ] What packages exist? (Accommodation only, surf included, meals included, combos?)
- [ ] Transfer types — airport pickup? Surf spot transfers? How are these tracked currently?
- [ ] What format does World Surfaris send bookings in? (Email, PDF, portal, spreadsheet?)
- [ ] How many bookings per month approximately? Peak vs. low season?
- [ ] What languages do most guests speak?
- [ ] Who needs to receive the daily brief — Sean only, or the whole team?
- [ ] What time should the morning brief arrive?
- [ ] Does Booking Layer have API access enabled on their account?
- [ ] Are special requests / dietary needs tracked anywhere currently?
- [ ] What does a typical WhatsApp inquiry look like — availability, pricing, logistics?

---

## System Requirements (Derived)

### Must Have (MVP)
- Daily morning brief pulling from Booking Layer (check-ins, check-outs, current guests, transfers)
- Flag for World Surfaris bookings (manual input or email parse — TBD)
- Delivered to Gmail inbox(es) at a set time each morning
- Multi-language email responder for Gmail (detect language → respond in kind)

### Nice to Have (Phase 2+)
- WhatsApp integration (respond to DMs automatically)
- Mockapos data in daily brief (revenue snapshot)
- World Surfaris email parser (auto-pull bookings from their confirmation emails)
- Post-stay follow-up automation (review requests, rebooking offers)
- Instagram DM auto-response for common inquiries

---

## Next Steps

1. Send Sean a follow-up with open items list (above)
2. Get Booking Layer API credentials from Sean
3. Get a sample World Surfaris booking confirmation email (to design parser)
4. Confirm room types and package names for data model
5. Confirm recipient email addresses for daily brief
6. Confirm preferred morning brief delivery time (WITA timezone)

---

_Notes compiled by WILBA / Jess Morrell from discovery call 2026-03-23_
