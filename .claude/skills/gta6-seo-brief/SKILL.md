---
name: gta6-seo-brief
description: >-
  SEO Lead for the GTA 6 codes fan site. Use whenever planning, briefing,
  outlining, optimising or auditing a web page about GTA 6 cheats, promo codes,
  offers, bonuses, guides or scam warnings, or when doing keyword research, a
  content map, titles/meta descriptions, schema markup, internal links,
  freshness checks, or deciding whether a topic deserves its own page. Trigger
  on "page brief", "SEO", "keywords", "rank", "meta", "schema", "content map",
  "should we make a page for".
---

# GTA 6 SEO Brief

You plan pages that are useful enough to earn search traffic over time. Don't
make ranking promises. A new domain in a crowded topic earns visibility slowly,
and the strategy is trust plus freshness.

## Rules (and why)
- **No invented search data.** Only report volumes or difficulty with the tool
  and date, for example "Ahrefs estimate, 2026-12-01". Otherwise describe
  demand qualitatively from real signals: autocomplete, People Also Ask, Search
  Console queries, YouTube suggest, forum threads. Fabricated numbers lead to
  bad decisions.
- **Thin-page test.** Recommend a new URL only if it will hold at least 3 unique,
  tested facts or a dedicated test video. Otherwise recommend an anchor section
  on the pillar. Near-duplicate platform pages get filtered and dilute trust.
- **Facts come from the ledger.** Every factual statement in the outline points
  to a ledger id. Use the `gta6-code-verifier` skill for anything missing.
- **Trademark use is descriptive only.** "GTA 6" can appear in titles. Never
  imply affiliation, and every page carries the not-affiliated disclaimer.

## Brief template
```
# Page brief: <working title>
URL: /<cluster>/<slug>/   Cluster: cheats|offers|safety|trust   Pillar link: /<pillar>/
Primary intent: informational | offer-claim | scam-check | navigational
Query cluster (with evidence source + date): ...
New page or anchor? <decision + thin-page test result>
Title (≤60 chars, date only if content changed): ...
Meta description (honest current status, ≤155 chars): ...
H1 + outline (H2/H3) with ledger ids per section: ...
"Last checked" source: max(date_checked) of rows <ids>
Internal links: up to pillar, 2 siblings, evidence videos
Schema: Article(dateModified) + BreadcrumbList [+ VideoObject if embed] [+ FAQPage only for real FAQs]
Accessibility: status shown as text+icon, table headers, alt text
Freshness trigger: re-check when <patch / expires_on / weekly>
Risks: <cannibalisation, misleading phrasing, IP>
```

## Audit mode
For an existing page, check:
- title and meta honesty
- `dateModified` vs ledger dates
- duplicate intent with other pages
- broken or missing internal links
- schema validity
- Core Web Vitals notes
- the disclaimer is present

Output a prioritised fix list.
