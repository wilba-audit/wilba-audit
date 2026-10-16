# Jess's email signature

Checked against her sent mail on 24 Sep 2026: jess@wilba.ai signs with the designed
signature (Jess Morrell, Founder & AI Automation Strategist, wilba.ai, hello@wilba.ai,
@wilba.ai, Victoria, Australia, the wilba.ai wordmark, a "Get Your Free AI Business
Audit" button and the "bleeding time" tagline). Drafts created through the Gmail API do
not get it appended, so it goes in the draft body.

## Cold outreach — use this one

Her real signature with the audit button and the tagline row removed. A cold email to a
clinic should not carry a button for a different offer, and link-heavy first-contact
mail lands in spam more often. The exact HTML used for batch 3 is in
`outputs/pipeline/email-signature-cold.html`.

Plain-text equivalent for the `body` field:

```
Jess

Jess Morrell

Founder & AI Automation Strategist
wilba.ai <https://www.wilba.ai/>
hello@wilba.ai
@wilba.ai <https://www.instagram.com/wilba.ai>
Victoria, Australia
```

## Warm and existing conversations

The full block at `outputs/wilba-email-signature.html`, including the tagline and the
"Get Your Free AI Business Audit" button. Fine once someone has replied.

## Still to confirm with Jess

- The contact address in the signature is `hello@wilba.ai`. If outreach sends from
  `jess@wilba.ai`, replies should come back to the address she actually watches.
- The tagline "We find where your business is bleeding time. Then we fix it."
  describes the old offer better than the aged-leads one.
