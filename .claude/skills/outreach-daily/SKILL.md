---
name: outreach-daily
description: Run one day of WILBA outreach — source and qualify med spa / plastic surgery prospects, draft the day's batch on the aged-leads revenue-share offer, stage them in Gmail, and update the pipeline. Use when the daily outreach routine fires, or when Jess asks to run outreach for the day.
---

# Daily outreach

One run = one day of outreach. Everything here is unattended except the send.

Read `outputs/pipeline/ICP.md` first. It is the qualification standard and the offer
description, and it changes more often than this file.

## 1. Stop chasing anyone who replied

Before anything else, check for replies. Search Gmail for inbound mail from the
domains of everyone whose status is Emailed or Follow-up N:

```
python3 scripts/wilba_outreach.py due          # who is mid-sequence
```

For each, `mcp__Gmail__search_threads` on their domain. Anyone who has written back
gets marked immediately:

```
python3 scripts/wilba_outreach.py mark --ids <ids> --status Replied
```

That ends their sequence. **Nobody gets a follow-up after they have answered** — it
is the fastest way to burn a prospect and a sender reputation. Surface the replies to
Jess in the daily report; they are the whole point of the exercise.

## 2. If Gmail is unavailable, source instead

If the Gmail tools return a sign-in or authorisation error, no drafts can be staged
this run. Do not treat that as a failed day: write the batch to
`outputs/pipeline/outreach-batch-N.md` anyway so the copy is ready and reviewable,
then spend the rest of the run on step 3, sourcing and qualifying, which needs no
mailbox.

**Connectors are read once, when a session starts.** If Jess reconnects Gmail while a
session is already running, that session will never see it — retrying is pointless and
so is asking her to reconnect again. The fix is a new session. Say that plainly rather
than reporting the same error twice.

The same applies to a permission prompt that blocks web fetching. Report what stopped
rather than looping on it.

## 3. Check where the pipeline stands

```
python3 scripts/wilba_outreach.py status
```

This prints today's cap (the domain is cold, so volume ramps 5 → 10 → 15 → 20 over
the first fifteen send-days) and how many qualified, contactable, unapproached
prospects are left.

**If it says LOW, source before you draft.** A day spent sourcing is a fine day.
Drafting into an empty list is not.

## 4. Source, when the list is short

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

## 5. Draft the day's batch

```
python3 scripts/wilba_outreach.py batch
```

It selects A grade before B, oldest first, capped at today's ramp. It prints the
verified facts for each prospect. Write from those facts only.

**The offer.** Reactivate the dormant leads already sitting in their CRM, converted
into booked procedures, paid as 10% of what it books with nothing upfront. We
integrate with the CRM they run — no migration. A human approves before anything
goes to a patient.

> **The percentage is 10%**, confirmed by Jess on 24 Sep 2026. Write it as
> "10% of what it books, nothing upfront". If she ever changes it, change it here
> and in `ICP.md` together.

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

**The signature.** Every draft carries Jess's signature block. Pass it in `htmlBody`
using the cold-outreach variant in `outputs/pipeline/email-signature.md` — the short
one, without the audit CTA button. Give `body` the plain-text equivalent so the email
degrades cleanly.

Stage each one with `mcp__Gmail__create_draft`. Never `send_message`.

Then:
```
python3 scripts/wilba_outreach.py mark --ids <ids> --status "Draft ready"
```

## 6. Draft the follow-ups that are due

`python3 scripts/wilba_outreach.py due` lists them. The cadence runs from the day the
initial went out:

| Touch | Day | What it does |
|---|---|---|
| Initial | 0 | The verified opening fact, the offer, the risk reversal |
| Follow-up 1 | +3 | Four lines. Restate only the risk reversal: they pay out of what it books. No new pitch. |
| Follow-up 2 | +7 | A different angle — the size of the idle list, or what a comparable practice recovered. Still short. |
| Follow-up 3 | +14 | The close-out. "I'll stop here — if it's ever worth a look, the offer stands." Leaves the door open and stops. |
| — | after +14 | Retire as Lost. |

Follow-ups reply into the **same Gmail thread** (`replyToMessageId` on the original),
so it reads as one conversation rather than four cold emails. Keep each one shorter
than the last. Nobody ever gets a fifth.

Anything the `due` output lists under `RETIRE:` gets
`mark --ids <ids> --status Lost`.

## 7. Report

Post one short reply in the thread: how many are staged, who they are, and anything
that needs Jess. Keep it to a few lines — the detail is in the pipeline file.

If nothing was staged because the list was empty, say that plainly and say how many
prospects were sourced instead.

## 8. Commit

Commit the pipeline and any new prospect rows to the working branch and push.

## What is not automatic

**Jess clicks send.** The drafts are staged, correct and ready, but they go out under
her name to people who did not ask to hear from her. A send cannot be recalled. So a
human presses the button on each batch — that is a deliberate design choice, not a
missing feature.

After she sends, record it so the ramp advances and the sequence starts:
```
python3 scripts/wilba_outreach.py mark --ids <ids> --status Emailed
```
That also schedules follow-up 1 for three days later. The same command records each
follow-up as it goes out, which schedules the next one.

**The From address.** Drafts are staged in whichever mailbox the Gmail connection
points at. If that is still the personal account, the drafts are correct but the From
needs switching at send time. Once `jess@wilba.ai` is connected, that stops being a
step and nothing else about this changes.
