# Baha Baha Villas — Unified Booking Data Model

**Version:** 1.0 (Draft — pending confirmation of room types and packages from Sean)
**Last updated:** 2026-03-23

> This is the master data schema for every booking, regardless of source. All scripts read from and write to this model.

---

## Unified Booking Record

Each booking is represented as a single record with these fields:

```
booking_id          — Unique ID (from Booking Layer or generated for manual bookings)
source              — Where booking came from (see Sources below)
status              — confirmed | tentative | cancelled | checked_in | checked_out

guest_name          — Full name
guest_email         — Email address
guest_phone         — WhatsApp / mobile
guest_language      — Detected or declared language code (en, fr, es, id, ja, de, pt, etc.)
guest_nationality   — Country (for language/transfer context)
guest_count         — Total pax

room_type           — See Room Types table below
room_name           — Specific villa/room name if applicable

check_in_date       — YYYY-MM-DD
check_out_date      — YYYY-MM-DD
nights              — Calculated: check_out - check_in

package_type        — See Package Types table below
meal_plan           — none | breakfast | half_board | full_board
surf_included       — true | false
surf_level          — beginner | intermediate | advanced | none
surf_guide          — true | false

transfer_in         — true | false
transfer_in_time    — HH:MM (WITA)
transfer_in_from    — airport | ferry | other
transfer_out        — true | false
transfer_out_time   — HH:MM (WITA)
transfer_out_to     — airport | ferry | other

special_requests    — Free text (dietary, accessibility, celebrations, etc.)
internal_notes      — Staff notes
vendor              — booking_layer | world_surfaris | direct | walk_in | instagram | whatsapp

total_amount        — Total booking value (IDR or USD)
currency            — IDR | USD | AUD
payment_status      — paid | partial | unpaid | refunded

created_at          — ISO timestamp when booking was created
updated_at          — ISO timestamp of last update
```

---

## Booking Sources

| Source Code | Description | How Data Arrives |
|-------------|-------------|-----------------|
| `booking_layer` | Direct website or OTA via Channex | Booking Layer API |
| `world_surfaris` | World Surfaris surf packages | Email confirmation (parse) or manual CSV |
| `direct` | Direct email / phone booking | Manual entry |
| `walk_in` | Walk-in at property | Manual entry |
| `instagram` | Instagram DM inquiry converted to booking | Manual entry |
| `whatsapp` | WhatsApp inquiry converted to booking | Manual entry |

---

## Room Types

> ⚠️ **Placeholder — confirm exact room names with Sean**

| room_type Code | Description | Beds | Notes |
|---------------|-------------|------|-------|
| `villa_private` | Private villa | King or Twin | Standalone, ensuite |
| `villa_garden` | Garden villa | King or Twin | Garden view |
| `room_standard` | Standard room | Queen | Shared areas |
| `room_budget` | Budget/dorm | Bunk | Backpacker option |

*Update this table once Sean confirms room names from Booking Layer.*

---

## Package Types

> ⚠️ **Placeholder — confirm exact package names with Sean**

| package_type Code | Description | Includes |
|------------------|-------------|---------|
| `accommodation_only` | Room only | Accommodation |
| `surf_stay` | Surf + accommodation | Accommodation + surf guiding |
| `full_package` | All-inclusive | Accommodation + surf + meals |
| `world_surfaris_package` | World Surfaris special | Per WS agreement |

---

## Meal Plans

| meal_plan Code | Description |
|---------------|-------------|
| `none` | No meals included |
| `breakfast` | Breakfast only |
| `half_board` | Breakfast + dinner |
| `full_board` | All meals |

---

## Transfer Types

| Type | Description | Notes |
|------|-------------|-------|
| Airport pickup | Guest arrives at Sumbawa Besar / Taliwang airport | Confirm flight number + time |
| Ferry pickup | Guest arrives via ferry | Confirm ferry schedule |
| Airport drop | Guest departs via airport | Need departure time |
| Surf spot transfer | Drop to/from nearby surf breaks | Coordinated with surf guide |

---

## Booking Layer Field Mapping

> Map Booking Layer API field names → Unified model field names

| Booking Layer Field | Unified Field | Notes |
|--------------------|---------------|-------|
| `reservation_id` | `booking_id` | |
| `channel` | `source` | Map channel names to source codes |
| `guest.first_name` + `guest.last_name` | `guest_name` | Concatenate |
| `guest.email` | `guest_email` | |
| `guest.phone` | `guest_phone` | |
| `accommodation.name` | `room_type` | Map to room_type codes |
| `check_in` | `check_in_date` | Format: YYYY-MM-DD |
| `check_out` | `check_out_date` | Format: YYYY-MM-DD |
| `extras` | `surf_included`, `meal_plan` | Parse from extras array |
| `notes` | `special_requests` | |
| `total` | `total_amount` | |
| `currency` | `currency` | |
| `status` | `status` | Map to unified status codes |

*Exact field names to be confirmed once API access is granted.*

---

## World Surfaris Booking Mapping

> World Surfaris sends booking confirmations by email. Fields to extract:

| WS Email Field | Unified Field | Parse Method |
|----------------|---------------|-------------|
| Guest name | `guest_name` | Text extract |
| Arrival date | `check_in_date` | Date parse |
| Departure date | `check_out_date` | Date parse |
| Package name | `package_type` | Map to codes |
| Pax count | `guest_count` | Number extract |
| Special notes | `special_requests` | Text extract |
| WS ref number | `booking_id` (prefix: `WS-`) | |

*Requires a sample confirmation email from Sean to finalize parser.*

---

## Daily Brief Data Requirements

For the morning brief, we need these fields per booking for today:

**Check-ins today:**
- guest_name, room_type, package_type, meal_plan, transfer_in, transfer_in_time, transfer_in_from, special_requests, guest_count, source

**Check-outs today:**
- guest_name, room_type, nights, transfer_out, transfer_out_time, transfer_out_to

**Transfers today:**
- All bookings where transfer_in_date = today OR transfer_out_date = today
- Fields: guest_name, transfer_type, time, from/to, notes

**In house:**
- All bookings where check_in <= today AND check_out > today
- Fields: guest_name, room_type, package_type, nights remaining, special_requests

**Upcoming (48 hours):**
- All bookings where check_in = tomorrow OR day after
- Fields: guest_name, check_in_date, room_type, package_type, transfer_in

---

_Update this document once Sean confirms room types, package names, and Booking Layer API access._
