# /mj-birthday — Monkey Joe's Birthday Party Funnel

> Birthday parties are the highest-value booking Monkey Joe's sells. There are two automations
> plus (per Jess) a **GHL-native workflow** running. This command reports funnel health and
> operates the controls — and its first job is making sure these don't overlap and double-send.

## When Jess runs this
`/mj-birthday` = "how's the birthday funnel doing / is it actually sending?" Report status,
then surface blockers and offer controls.

## The moving parts
1. **Birthday Drip** — `scripts/mj_birthday_sequence.py`, runs **daily** via GitHub Action
   `mj-birthday-drip.yml`. A 180-day, 10-touchpoint nurture that starts from each contact's
   **enrollment date** (`bday-start-YYYY-MM-DD` tag). Idempotent via `bday-sent-dN` tags. Exits
   on `birthday-{loc}-booked` or `unsubscribed`.
2. **Birthday Radar** — `scripts/mj_birthday_radar.py`, runs **weekly** (Wed) via
   `mj-birthday-radar.yml`. Reminders at **90 / 60 / 30 days before the child's actual birthday**.
   Needs each child's birthday in a GHL custom field.
3. **GHL-native workflow** — Jess says one exists in GHL. **Reconcile it.** If the GHL workflow
   already nurtures birthday leads, our Python Drip may be **duplicating** messages. Determine
   which is the source of truth and either (a) turn off one, or (b) scope them so they don't
   overlap. Do NOT leave both blasting the same contacts. Flag this to Jess explicitly.

## Booking link
Both currently point to `https://monkeyjoespo.com/birthday-party`. Check whether **Winter Park**
should route to its own page — if so, split `BOOK_LINK` per location in both scripts.

## Status check (default)
1. Load creds (same GHL keys as `/mj-ghl`).
2. **Drip status:** `python3 scripts/mj_birthday_sequence.py status` → enrolled vs booked per location.
3. **Radar coverage:** `python3 scripts/mj_birthday_radar.py coverage` → how many contacts have a
   usable child birthday on file. If this is near zero, Radar is effectively dormant.
4. **Custom field check:** confirm `CHILD_BDAY_FIELD_ID` is set (as a secret / in `.env`). Jess
   says the field was created — get its **field ID** via `/mj-ghl` custom-fields pull and make
   sure it's wired into the Radar secret. Without it, Radar falls back to the parent's DOB and
   reaches almost nobody.
5. **Dry-run the sends:** `mj_birthday_sequence.py run` and `mj_birthday_radar.py run` (no
   `--execute`) to show exactly who WOULD get a message this cycle.

## The data-capture blocker
Radar only works if children's birthdays are collected. If coverage is low, the fix is a
**data-capture campaign** — an email/SMS to the `voucher-delivered` audience asking parents to
tell us the birthday (writes into the custom field). Offer to design and build it if Jess wants;
until it runs, Radar delivering little is expected, not broken.

## Missing design doc
`mj_birthday_sequence.py` references `outputs/monkey-joes/MJ-180Day-Birthday-Sequence-2026-06-22.md`,
which **isn't in the repo**. Offer to regenerate it from the touchpoints defined in the script so
the strategy is documented.

## Controls (when she asks)
- Enroll a fresh cohort: `mj_birthday_sequence.py tag-cohort --loc POL --execute` (dry-run first).
- Mark someone booked: apply `birthday-{loc}-booked` to stop their sequence.
- Adjust touchpoints/copy: edit the `TOUCHPOINTS` list in the script; keep it in sync with the
  design doc.

## Guardrails
- Reconcile against the GHL-native workflow BEFORE running any send — no double-messaging.
- Dry-run → confirm → execute for anything that sends.
- Report in parent-friendly language, not tag names.
