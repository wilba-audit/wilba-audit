---
name: outreach-daily
description: Run one day of WILBA outreach — source and qualify med spa / plastic surgery prospects, draft the day's batch on the aged-leads revenue-share offer, stage them in Gmail, and update the pipeline. Use when the daily outreach routine fires, or when Jess asks to run outreach for the day.
---

# Daily outreach

One run = one day of outreach. Everything here is unattended except the send.

Read `outputs/pipeline/ICP.md` first. It is the qualification standard and the offer
description, and it changes more often than this file.

## 1. Check where the pipeline stands

```
python3 scripts/wilba_outreach.py status
```

This prints today's cap (the domain is cold, so volume ramps 5 → 10 → 15 → 20 over
the first fifteen send-days) and how many qualified, contactable, unapproached
prospects are left.

**If it says LOW, source before you draft.** A day spent sourcing is a fine day.
Drafting into an empty list is not.

## 2. Source, when the list is short

Target: enough qualified prospects for a week at the current cap.

Run several `Agent` workers in parallel, each on a different metro. Give each one a
short list of search terms ("med spa <city>", "plastic surgery <city>",
"cosmetic surgery clinic <city>") and the Must-have list from `ICP.md`. Require of
every worker:

- **Never construct an email address.** Only report one seen in fetched page content,
  with the URL it was seen on. A clinic with no published address is recorded as a
  form/phone row, not skipped and not guessed at.
- Report `crm_detected` from the booking flow or page source, `scale_signals`
  (practitioners, locations, menu, memberships), and `dormant_lead_signal`
  (lead magnets, waitlists, redeemable consults, membership schemes).
- Quote the specific fact each opening angle will be built from.

Append accepted rows to `outputs/pipeline/clinic-pipeline.csv` with `status` New,
`icp_fit` A or B per `ICP.md`, and `email_source` saying where the address was read
and on what date.

## 3. Draft the day's batch

```
python3 scripts/wilba_outreach.py batch
```

It selects A grade before B, oldest first, capped at today's ramp. It prints the
verified facts for each prospect. Write from those facts only.

**The offer.** Reactivate the dormant leads already sitting in their CRM, converted
into booked procedures, paid as a share of what it books with nothing upfront. We
integrate with the CRM they run — no migration. A human approves before anything
goes to a patient.

> **Do not state a percentage.** The 10% figure from the 22 Sep call is unconfirmed.
> Write "a share of what it books, nothing upfront" until Jess confirms it.

**The shape**, matching the voice already established in `outreach-batch-2.md`:

1. One specific, verified fact about *their* practice. Never a generic opener.
2. The consequence, in one line, dry rather than salesy.
3. The offer, concretely, tied to their CRM by name where known.
4. The risk reversal — they pay out of what it books.
5. "Worth 15 minutes?" plus the timezone line (Jess is in Indonesia / on Bali time).
6. Sign-off:
   ```
   Jess

   Jess Morrell
   WILBA — wilba.ai
   ```

Around 120-140 words. Australian and British spelling. No "I hope this finds you
well". No em-dash in the subject line.

Stage each one with `mcp__Gmail__create_draft`. Never `send_message`.

Then:
```
python3 scripts/wilba_outreach.py mark --ids <ids> --status "Draft ready"
```

## 4. Report

Post one short reply in the thread: how many are staged, who they are, and anything
that needs Jess. Keep it to a few lines — the detail is in the pipeline file.

If nothing was staged because the list was empty, say that plainly and say how many
prospects were sourced instead.

## 5. Commit

Commit the pipeline and any new prospect rows to the working branch and push.

## What is not automatic

**Jess clicks send.** The drafts are staged, correct and ready, but they go out under
her name to people who did not ask to hear from her. A send cannot be recalled. So a
human presses the button on each batch — that is a deliberate design choice, not a
missing feature.

After she sends, record it so the ramp advances:
```
python3 scripts/wilba_outreach.py mark --ids <ids> --status Emailed
```
That also schedules follow-up 1 for three days later.
