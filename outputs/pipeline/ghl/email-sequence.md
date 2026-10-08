# Clinic outreach sequence (GHL)

Written in the Dean Jackson / Joe Polish style. Every email is short and plain, reads like
one person writing to another, asks one easy question, and leads with the risk reversal.
There are four emails over seven days, and anyone who replies drops out of the sequence
straight away.

**The offer, in one line:** you pay 10% of the bookings we bring in, nothing upfront, and
if you don't love what we build you get every cent back.

> **Check the guarantee with Griffin before go-live.** Nobody pays upfront, so "full refund"
> means refunding the 10% they've paid us so far. That costs Griffin money, so he has to
> agree to it. If he won't, use the fallback line instead:
> "If you don't love it, we switch it off and you owe nothing more."

Each contact carries these custom fields, which are filled in for every clinic in
`ghl-import.csv`:

| Field | GHL merge tag | What it holds |
|---|---|---|
| Cold subject | `{{contact.cold_subject}}` | A subject line written for that clinic |
| Cold opener | `{{contact.cold_opener}}` | Two short lines built from a verified fact about that clinic |
| CRM phrase | `{{contact.crm_phrase}}` | The booking system we saw them using, such as "Zenoti" |
| Timezone line | `{{contact.tz_line}}` | The "worth a chat?" line, worded for their country |

All four emails are plain text, with no images, no links in the body and no tracking
pixel. That is the biggest single thing that keeps cold mail out of spam.

---

## Email 1 · Day 0 · the personal one

**Subject:** `{{contact.cold_subject}}`

```
{{contact.cold_opener}}

Here's what I'd like to do. We plug into {{contact.crm_phrase}}, find those people, and follow them up by text and phone until they book or say stop. Nothing changes for your team.

You pay 10% of the bookings it brings in. Nothing upfront. And if you don't love what we build, you get every cent back.

{{contact.tz_line}}

Jess

Jess Morrell
WILBA, wilba.ai

If this isn't for you, reply "no" and I won't email again.
```

---

## Email 2 · Day 2 · the nudge

**Subject:** `Re: {{contact.cold_subject}}`

```
Did you get a chance to see my note?

The short version: there's money sitting in {{contact.crm_phrase}} from people who enquired and never booked. We go and get it, and you only pay out of what comes back.

Jess
```

---

## Email 3 · Day 4 · worst case, best case

**Subject:** `Worst case`

```
Here's the worst that can happen if you say yes:

We build it, it books nobody, and you've paid nothing.

Here's the best:

Patients who'd drifted away come back in, and you keep 90% of every booking.

And if you don't like what we've built, you get a full refund. No awkward conversation.

Shall I send you a couple of times?

Jess
```

---

## Email 4 · Day 7 · the nine-word email

**Subject:** `{{contact.company_name}}`

```
Are you open to waking up your old leads?

Jess
```

That's the whole email. One question, nine words, easy to answer with a yes. Dean Jackson
built his name on it, because it gets replies when longer emails don't.

Nobody gets a fifth email. After day 7 with no reply, the opportunity moves to
**No response** and can be tried again in three months.

---

## Footer (needed for US and UK sends)

In the US, CAN-SPAM requires a real postal address and a working opt-out in every
commercial email. UK and Australian rules also expect a clear way to opt out. In the
workflow's email settings, turn on GHL's unsubscribe footer and add WILBA's business
address to it.
