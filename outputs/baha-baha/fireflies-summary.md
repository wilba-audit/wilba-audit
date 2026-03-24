# Fireflies Meeting Summary — Jess/Sean AI Setup

**Date:** Mar 23 2026, 4:03 PM
**Participants:** Jess Morrell, Sean (Baha Baha), Mashi (team)
**Duration:** ~1 hour (01:01:57)
**Source:** https://app.fireflies.ai/view/Jess-Sean-AI-setup::01KMCH7P74KX2N65FCVFAS0S4M

---

## General Summary

- **Booking System Challenges:** Manual input required for many fields in Booking Layer; automation needed for linked room bookings (e.g. studio + 2-bed combined as a deluxe suite)
- **Agency Relationships:** Channel manager (ChanX) interfaces with key agencies, but most bookings remain manual; communication issues persist
- **AI Automation Plans:** Phase 1 = AI chatbot on website/WhatsApp/Instagram for instant booking replies. Phase 2 = deeper Booking Layer API integration + automated daily emails
- **Accounting Issues:** Journal.co.id lacks POS integration with Moka, requiring manual entry; previous system migration caused loss of historical data
- **Content Strategy:** AI to automate content creation and marketing, but Google Drive data organization is a major bottleneck
- **Training Needs:** Staff require training on AI tools; reliance on owner for communication highlights skill gaps

---

## Key Notes

### Booking System & Channel Management

**Booking Layer (04:37)**
- All bookings funnel through Booking Layer — packages, accommodations, notes, flight details, transfers
- Requires manual input throughout; limited automation
- Flight bookings handled *outside* the system to avoid commission fees — tracked manually
- System can block rooms manually but can't link grouped units (e.g. studio + 2-bed = deluxe booking)
- Many outdated prices, packages, and rooms exist in Booking Layer — causing confusion
- New rooms added: **Baja room** and **studio** — can't be booked as linked group rooms yet
- **Mashi** assigned to lead Booking Layer cleanup and coordinate with their support team

**Channel Manager & Agencies (14:20)**
- Channel manager: **ChanX** (connects Booking Layer to external agencies)
- Key agencies: **One Wave**, **World Safaris**
- Commission rates: ~12.5% (Surf Lines), ~20% (others)
- Bookings from agencies mostly arrive manually — no successful automated bookings yet through some partners
- Communication issues due to multiple consultants and commission-driven salespeople

**Team & Daily Operations (38:09)**
- **Danny** manages transportation and flights daily
- Guest communication sticks to whichever platform they first contacted on (WhatsApp or email)
- Staff lacks confidence in English — owner (Sean) ends up handling most direct replies himself

### AI Automation Plans

**Phase 1: Chatbot for bookings and inquiries (13:07)**
- Chatbot deployed on: **website (Squarespace), Instagram, and WhatsApp**
- Handles: instant booking replies, after-hours communication, FAQs about rooms, flights, transfers
- Reduces manual back-and-forth for Sean
- Catches guests immediately rather than losing them overnight

**Phase 2: Deeper Booking Layer integration (42:34)**
- AI connects to Booking Layer API to track booking statuses, flight details, packages
- Automated daily emails summarising tasks: flight bookings, transfers, pending actions
- Multi-language support for guests and local staff
- AI could suggest flight options for manual approval

### Financial & Accounting

- **Journal.co.id** = accounting platform; **Moka** = POS system
- Journal and Moka are disconnected — no integration; all entries manual
- Previous migration (from Xero) caused loss of historical financial data
- This is a known problem Sean needs to resolve separately from the AI work

### Content & Google Drive

- AI content automation is planned, but Google Drive is disorganised
- Files don't have consistent naming or folder structure
- Drive cleanup is a prerequisite before any automated content pipeline can work

---

## Action Items

### Sean's Actions
1. Assist Mashi with resolving Booking Layer issues — new rooms setup and synchronisation
2. Provide updated rates, inclusions, and booking availability to World Safaris agents
3. Continue manually booking flights and adding notes in Booking Layer until automation is feasible
4. Collaborate with Mashi on upcoming Booking Layer support meeting

### Jess's Actions
1. Coordinate AI chatbot implementation for WhatsApp, Instagram, and website
2. Prepare Phase 1 and Phase 2 scopes for AI integration
3. Work with developer and Mashi to set up the system for Baha Villas and test automated content
4. Deliver training materials/workshops for Baha Villas staff
5. Monitor API limitations and advise on workarounds (especially accounting integration)

### Mashi's Actions
1. Handle Booking Layer support call to address room additions, pricing updates, and technical issues

---

## Daily Digest — Sean's Prioritised Action Items

### 🔴 Bookings & Channel Management
- **Re-enable Jess in Booking Layer** — add jessmorrell@gmail as Manager role; also add developer access [Deadline: 25 Mar 2026]
- Schedule Booking Layer support deep-dive with Mashi + BL rep to resolve room-grouping issue [this week]
- Document canonical booking flows (website/WhatsApp/IG/OTA) and map manual blocking steps [next week]

### 🔴 AI Agent Deployment — Phase 1
- **Approve Phase 1 scope** — deploy chatbot on Squarespace + WhatsApp + Instagram; confirm FAQ list and flight capture logic [Deadline: 25 Mar 2026]
- **Grant Jess/dev Booking Layer API credentials** (read-only first) [1 week]
- Provide list of common guest languages + sample WhatsApp inquiry conversations [2 weeks]

### 🔴 Operations & Training
- Record a short screen-capture (5–10 min) showing "how to handle booking notes & flights" for frontline staff [Deadline: 26 Mar 2026]
- Approve 2–3 pilot staff for agent handoff testing; schedule 1 training session with Jess [after Phase 1 deployment]

### 🔴 Accounting & POS
- Investigate Journal ↔ Moka POS disconnection — contact Journal support and Moka rep [Deadline: 26–27 Mar 2026]
- Compile list of critical financial records missing from Xero migration [1 week]

### 🔴 Content & Drive Cleanup
- Grant Jess/dev temporary access to a structured Google Drive folder (or tag a sample content folder) [Deadline: 28 Mar 2026]
- Approve budget/time to clean Drive naming and folder structure (or assign a contractor) [2 weeks]

---

## Blockers

- **Booking Layer room grouping** — automatic linking of studio + 2-bed as a combined unit is not working; blocking sell-through logic for the deluxe room type. Mashi is working on this with Booking Layer support.
- **Booking Layer access** — Jess and developer need to be added as users before API work can begin
- **Journal ↔ Moka disconnect** — accounting data is siloed; manual only. Out of scope for AI Phase 1 but needs to be resolved for any financial reporting automation
- **Google Drive disorganisation** — content pipeline blocked until folders are cleaned up

---

## Open Questions

- **AI Integration Scope** — Is the Phase 1 priority the chatbot (website/WhatsApp/IG) or the daily ops brief email? Meeting described chatbot as Phase 1; proposal has daily brief as Phase 1. Needs alignment with Sean.
- **Booking Layer & Third-party Partners** — Which agencies are actually connected via ChanX vs manual? Full list needed for data model
- **Financial Ownership** — Who is responsible for accounting cleanup — Sean or a contractor?
- **POS/Accounting Path** — Is there a plan to connect Journal.co.id and Moka, or is this staying manual?

---

## Key New Discoveries (vs. What We Had Before)

| Item | Previous Understanding | Confirmed in Meeting |
|------|----------------------|---------------------|
| Phase 1 priority | Daily ops brief email | Chatbot on website/WhatsApp/IG (scope needs alignment) |
| Team members | Sean only mentioned | **Mashi** (Booking Layer + ops), **Danny** (transport/flights) |
| Room types | Unknown / placeholder | Baja room, studio (+ others — still need full list) |
| Agencies | World Surfaris (one) | One Wave + World Safaris; ChanX as channel manager |
| Booking Layer access | Sean has it | Jess needs to be re-added as Manager |
| Accounting | Jurnal.co.id | Journal.co.id + Moka POS (disconnected) |
| Drive | Not mentioned | Disorganised — blocker for content automation |
| Guest comms channel | Email + WhatsApp | Primarily WhatsApp — Phase 1 chatbot should prioritise WA |

---

*Compiled from Fireflies.ai meeting recording — Jess/Sean AI Setup, 23 Mar 2026*
