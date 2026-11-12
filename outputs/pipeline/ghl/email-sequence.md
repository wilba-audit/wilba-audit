# Clinic outreach sequence (GHL): 10 emails

Dean Jackson / Joe Polish style: short, plain, one easy question per email, and the
risk reversal up front. Ten emails over 40 days. Anyone who replies or books a call
drops out straight away.

**The offer:** you pay 10% of the bookings we bring in, nothing upfront, and if you
don't love what we build you get every cent back.

> **Check the guarantee with Griffin before go-live.** Nobody pays upfront, so "full
> refund" means refunding the 10% they've paid us. If he won't agree, swap it for:
> "If you don't love it, we switch it off and you owe nothing more."

**Calendar link:** https://calendly.com/hello-wilba (the one already live on the audit funnel). If you'd
rather book into a GHL calendar, swap the link and bookings will move the card to
Call booked on their own.

**Branded versions:** `templates/email-01.html` to `email-10.html`. In GHL, open the
email step, choose the code editor, and paste the file in. The branding is the WILBA
wordmark, colours and signature, all in text. There are no images, so it still lands
in the inbox like a personal email.

| # | Day | Subject | Job |
|---|---|---|---|
| 1 | 0 | `{{contact.cold_subject}}` | Personal opener + offer |
| 2 | 2 | `Re: {{contact.cold_subject}}` | Nudge |
| 3 | 4 | `Worst case` | Worst case / best case |
| 4 | 7 | `{{contact.company_name}}` | Nine-word email |
| 5 | 10 | `The maths on old enquiries` | The maths |
| 6 | 14 | `Why we only take 10%` | Why revenue share |
| 7 | 18 | `What your team actually does` | What the team does |
| 8 | 23 | `Quick question` | Curiosity question |
| 9 | 30 | `Should I close your file?` | Close the file? |
| 10 | 40 | `Last one from me` | Last one, door open |

---

## Email 1 · Day 0 · Personal opener + offer

**Subject:** `{{contact.cold_subject}}`

```
{{contact.cold_opener}}

Here's what I'd like to do. We plug into {{contact.crm_phrase}}, find those people, and follow them up by text and phone until they book or say stop. Nothing changes for your team.

You pay 10% of the bookings it brings in. Nothing upfront. And if you don't love what we build, you get every cent back.

{{contact.timezone_line}} Grab any time that suits here: https://calendly.com/hello-wilba

Jess

Jess Morrell
WILBA, wilba.ai
Book a call: https://calendly.com/hello-wilba

If this isn't for you, reply "no" and I won't email again.
```

---

## Email 2 · Day 2 · Nudge

**Subject:** `Re: {{contact.cold_subject}}`

```
Did you get a chance to see my note?

The short version: there's money sitting in {{contact.crm_phrase}} from people who enquired and never booked. We go and get it, and you only pay out of what comes back.

If it's easier, pick a time here: https://calendly.com/hello-wilba

Jess

Jess Morrell
WILBA, wilba.ai
Book a call: https://calendly.com/hello-wilba

If this isn't for you, reply "no" and I won't email again.
```

---

## Email 3 · Day 4 · Worst case / best case

**Subject:** `Worst case`

```
Here's the worst that can happen if you say yes:

We build it, it books nobody, and you've paid nothing.

Here's the best:

Patients who'd drifted away come back in, and you keep 90% of every booking.

And if you don't like what we've built, you get a full refund. No awkward conversation.

Fifteen minutes is all it takes to see which one you'd get: https://calendly.com/hello-wilba

Jess

Jess Morrell
WILBA, wilba.ai
Book a call: https://calendly.com/hello-wilba

If this isn't for you, reply "no" and I won't email again.
```

---

## Email 4 · Day 7 · Nine-word email

**Subject:** `{{contact.company_name}}`

```
Are you open to waking up your old leads?

Jess

Jess Morrell
WILBA, wilba.ai
Book a call: https://calendly.com/hello-wilba

If this isn't for you, reply "no" and I won't email again.
```

---

## Email 5 · Day 10 · The maths

**Subject:** `The maths on old enquiries`

```
Quick back-of-envelope.

Say {{contact.crm_phrase}} holds 500 people who enquired and never booked. If 1 in 20 comes back for a {{contact.currency}}400 treatment, that's {{contact.currency}}10,000 in bookings you've already paid to attract.

Our share is {{contact.currency}}1,000. Yours is {{contact.currency}}9,000. And you didn't spend another cent on ads.

Happy to run the real numbers with you: https://calendly.com/hello-wilba

Jess

Jess Morrell
WILBA, wilba.ai
Book a call: https://calendly.com/hello-wilba

If this isn't for you, reply "no" and I won't email again.
```

---

## Email 6 · Day 14 · Why revenue share

**Subject:** `Why we only take 10%`

```
Most agencies charge a setup fee, a monthly retainer, and hope it works.

We'd rather get paid when you do. That's why it's 10% of the bookings we bring in, nothing upfront, and a full refund if you don't love what we build.

If we don't deliver, we don't eat. It keeps us honest.

https://calendly.com/hello-wilba

Jess

Jess Morrell
WILBA, wilba.ai
Book a call: https://calendly.com/hello-wilba

If this isn't for you, reply "no" and I won't email again.
```

---

## Email 7 · Day 18 · What the team does

**Subject:** `What your team actually does`

```
The question I get most: "What does my team have to do?"

Almost nothing. The system works inside {{contact.crm_phrase}}, your team approves anything before it goes to a patient, and there's one "AI off" switch if they ever want to pause it.

No new software to learn. No migration.

Worth a look? https://calendly.com/hello-wilba

Jess

Jess Morrell
WILBA, wilba.ai
Book a call: https://calendly.com/hello-wilba

If this isn't for you, reply "no" and I won't email again.
```

---

## Email 8 · Day 23 · Curiosity question

**Subject:** `Quick question`

```
What happens at {{contact.company_name}} to an enquiry that doesn't book?

Just curious. Most clinics tell me "nothing, really", and that's the gap we fill.

Jess

Jess Morrell
WILBA, wilba.ai
Book a call: https://calendly.com/hello-wilba

If this isn't for you, reply "no" and I won't email again.
```

---

## Email 9 · Day 30 · Close the file?

**Subject:** `Should I close your file?`

```
I haven't heard back, so I'm guessing old enquiries aren't a priority right now. Totally fine.

Should I close your file, or would you like me to keep you on the list?

Either way, just reply with a quick "close" or "keep".

Jess

Jess Morrell
WILBA, wilba.ai
Book a call: https://calendly.com/hello-wilba

If this isn't for you, reply "no" and I won't email again.
```

---

## Email 10 · Day 40 · Last one, door open

**Subject:** `Last one from me`

```
I'll leave it here so I'm not cluttering your inbox.

If waking up old enquiries is ever worth a look, the offer stands: 10% of what it books, nothing upfront, full refund if you don't love it.

My calendar is always open: https://calendly.com/hello-wilba

Jess

Jess Morrell
WILBA, wilba.ai
Book a call: https://calendly.com/hello-wilba

If this isn't for you, reply "no" and I won't email again.
```

---

## Footer (needed for US and UK sends)

In the US, CAN-SPAM requires a real postal address and a working opt-out in every
commercial email. In the workflow's email settings, turn on GHL's unsubscribe
footer and add WILBA's business address to it.
