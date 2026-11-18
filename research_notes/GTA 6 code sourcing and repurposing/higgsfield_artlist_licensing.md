# Higgsfield and Artlist: capabilities and licence terms for a GTA 6 codes YouTube/TikTok channel

Date checked: 18 Nov 2026.

**Important method caveat (read first).** This session's network blocked direct page fetches: the WebFetch tool failed with DNS errors for higgsfield.ai, artlist.io, help-center.artlist.io and startupfortune.com. **No primary terms page was opened in full.** Everything below comes from web-search result summaries and snippets, which point at the primary URLs. Text shown in quotation marks is snippet text the search engine attributed to that page. It is **not** a verified verbatim quote from the live document. Before anything is published or relied on legally, open these pages and confirm the wording:
- https://higgsfield.ai/terms-of-use-agreement (Higgsfield Terms of Use, updated version effective 27 Aug 2026 per its blog)
- https://higgsfield.ai/creator-hub/help-center/account/who-owns-my-generations-and-can-i-use-them-commercially
- https://artlist.io/help-center/privacy-terms/artlist-license/ and the Social licence PDF https://artlist.io/media/g2tebxpm/current-ver-social-license-permitting-assets-in-ai-clean-04012026.pdf
- https://artlist.io/page/pricing
- https://support.rockstargames.com/articles/200153756/rockstar-games-video-policy

Getting full text needs these hosts allowed in the session's network settings.

---

## 1. Higgsfield: products, pricing, terms, controversies

### Takeaway
Higgsfield is an AI video and image generation hub. It offers many third-party models, viral and motion presets, AI Influencer, Marketing/Ads Studio, a Virality Predictor and TikTok publishing. Its help centre says you own your outputs and can use them commercially on any plan, YouTube monetisation included. It also says you warrant that your inputs don't infringe anyone's copyright, trademark or likeness, and you indemnify Higgsfield if they do. IP indemnity *from* Higgsfield is reportedly offered on Enterprise only. A July 2026 press critique says the licence Higgsfield takes over user content is far broader than its "you own it" messaging suggests.

### Cited Findings
**Products**
- The site navigation lists models including Seedance 2.0, Kling 3.0, Sora 2, Veo 3.1 and WAN 2.6. "AI Influencer" and "Draw to Video" appear as navigation items. — [Pasquale Pillitteri blog (secondary)](https://pasqualepillitteri.it/en/news/2273/higgsfield-virality-predictor-hook-score-hold-rate-2026)
- Virality Predictor scores a clip of up to about 15 seconds for hook score, hold rate and viral potential, with a "brain-activity heatmap". It reportedly launched on 9 May 2026 and is available on the web, CLI and MCP. The blogger cautions it "is not a substitute for real A/B testing". — [Pillitteri](https://pasqualepillitteri.it/en/news/2273/higgsfield-virality-predictor-hook-score-hold-rate-2026); [Le Big Data (FR)](https://www.lebigdata.fr/higgsfield-lance-une-ia-qui-sait-deja-quelles-videos-deviendront-virales); [Higgsfield blog](https://higgsfield.ai/blog/how-to-make-viral-videos-viral-presets)
- Higgsfield also has Similarity Score, Relight and Angles apps. — [higgsfield.ai/apps/similarity-score](https://higgsfield.ai/apps/similarity-score); [higgsfield.ai/apps/relight](https://higgsfield.ai/apps/relight)
- In March 2026 Higgsfield announced a content-scoring tool that "assigns a score signaling how closely output resembles protected intellectual property, including celebrity likeness". — [Programming Insider](https://programminginsider.com/higgsfield-unveils-content-scoring-tool-to-help-hollywood-navigate-the-ai-likeness-minefield/)
- **Direct observation in this session:** the Higgsfield connector attached here exposes tools for TikTok account connection, publishing and trending music (`tiktok_connect`, `tiktok_prepare_publish`, `tiktok_music_trending`). It also has Ads Studio (`ads_studio_generate`, brand/product setup), AI Influencer (`ai_influencer_generate`), `virality_predictor`, voice cloning and changing (`create_voice`, `voice_change`), `upscale_video`, `reframe`, `remove_background`, `motion_control`, a Meta Ads connector, a website builder and `media_import_url` (import media from a URL). This confirms the product surface exists. It says nothing about rights. — source: Higgsfield MCP tool list in this Claude session, 18 Nov 2026 (no public URL)

**Pricing (not verified on the official page, and the figures conflict)**
- Krea: Free $0 (no credits). Starter $19/mo for 270 credits (no annual discount). Plus $47/mo billed annually for 1,200 credits. Ultra $99/mo billed annually for 3,000 credits. — [Krea](https://www.krea.ai/blog/higgsfield-pricing-explained-2026-unlimited-credits-and-real-monthly-costs)
- HeyGen (Oct 2026): Starter $19. Plus $59 monthly ($47 annual). Ultra $129 monthly ($99 annual). Subscription credits reset at renewal, and credit packs expire after 90 days. — [HeyGen blog](https://www.heygen.com/blog/higgsfield-pricing)
- Conflicting: a page dated 24 Oct 2026 gives Starter $15 for 200 credits, Plus $49 for 1,000 and Ultra $129. Other August 2026 pages describe Basic, Pro and Max tiers instead. — [diyai](https://diyai.io/ai-tools/video-generation/higgsfield-pricing/)
- Note: several of these pricing pages are competitor marketing (HeyGen, Krea, Luma, Creatify).

**Terms: ownership and commercial use**
- Higgsfield's help centre cites Terms §4.4 as saying Higgsfield does not claim ownership of inputs or outputs and does not restrict commercial use. It lists ads, client work, products and YouTube monetisation as covered. Commercial rights are not tied to a plan. Outputs may not be used to train other AI models. — [Higgsfield Help: Who owns my generations](https://higgsfield.ai/creator-hub/help-center/account/who-owns-my-generations-and-can-i-use-them-commercially)
- The updated Terms and Privacy Policy took effect on 27 Aug 2026. — [Higgsfield blog: terms update](https://higgsfield.ai/blog/terms-of-use-privacy-policy-update)
- Critique (24 Jul 2026): StartupFortune says the licence Higgsfield takes over creator content is "non-exclusive, irrevocable, perpetual, worldwide, royalty-free, fully paid, transferable and sublicensable". It says this could allow training on, and marketing with, creator content. Higgsfield-hosted pages instead say the licence is limited to running the service. **These sources conflict, and I could not read the Terms to resolve it.** — [StartupFortune](https://startupfortune.com/higgsfield-ai-tells-creators-they-own-their-videos-but-quietly-claims-a-perpetual-worldwide-license-to-train-on-them/)

**Terms: uploading content you don't own, likeness and indemnity**
- Snippet attributed to the Terms of Use, as a user warranty: "Your Content does not infringe or violate the copyright, trademark, publicity rights, privacy rights, or other intellectual property or proprietary rights of any third party." — [Higgsfield Terms of Use](https://higgsfield.ai/terms-of-use-agreement) (snippet only, not opened)
- The help centre says you are responsible for making sure your content doesn't infringe third-party rights, "including copyright, trademark, and likeness rights" (§5.1(ii)(b)). It also says you may not upload or use an image of another person without their permission (§5.3). — [Higgsfield Help](https://higgsfield.ai/creator-hub/help-center/account/who-owns-my-generations-and-can-i-use-them-commercially)
- Indemnity, per a third-party summary of §12: you indemnify Higgsfield for losses "to the extent arising from content you provided without the necessary rights or from your use of the Service in violation of this Agreement or applicable law". IP indemnity from Higgsfield is Enterprise-only. — [Aliteq](https://aliteq.com/higgsfield-commercial-use); [Blur Studio](https://www.blurstudio.ai/knowledge/is-higgsfield-safe-and-legit)
- Higgsfield runs a DMCA and legal-notice process. — [Higgsfield Help: DMCA](https://higgsfield.ai/creator-hub/help-center/business/how-do-i-submit-a-dmca-notice-or-legal-inquiry)
- Higgsfield contest rules (a separate instrument, stricter than the ToS) ban "protected third-party intellectual property, such as characters, franchises, brands, logos, music or artwork, used without authorization". They also ban any identifiable real person's likeness or voice, "Not even yourself, and not even with consent". — [Higgsfield Talent Contest rules](https://higgsfield.ai/contests/talent-contest?tab=rules)

**Controversies**
- Feb 2026: a Forbes exposé accused Higgsfield of fake AI demos, unlicensed celebrity deepfakes and racist AI videos. It also alleged that Higgsfield commissioned creators to make marketing material with unlicensed IP. Co-founder Mahi de Silva said a marketing employee made the media kit "to generate ideas" and it was sent by mistake. — [Forbes Kazakhstan](https://forbes.kz/articles/startap-higgsfield-obvinyayut-v-manipulyatsiyah-s-marketingom-42a2a0); [Dealroom](https://dealroom.co/news/125907-higgsfields-rapid-growth-draws-scrutiny-over-racist-ai-videos-and-billin/); [TBPN digest](https://tbpn-digest.vercel.app/story/2026-02-12/higgsfield-accused-of-fake-ai-demos-racist-deepfakes-and-copyright-violations-in-forbes-expose)
- Feb 2026: backlash over marketing that boasted about replacing creative jobs. Separate criticism targeted marketing and subscription/billing practices. — [The Register](https://www.theregister.com/2026/02/06/higgsfield_ai_job_loss/); [Grit Daily](https://gritdaily.com/kazakh-startup-higgsfield-criticism/)
- I found no lawsuit filed against Higgsfield itself.

### Inferences
- Higgsfield is safe to use for **original** assets: a channel intro, an abstract or neon "city at night" b-roll that does not copy GTA's look, a thumbnail background, and resizing your own footage for Shorts and TikTok. Its commercial-use position covers YouTube monetisation.
- Uploading a Rockstar trailer, someone else's YouTube video or GTA character art and remixing it would breach the user warranty. Under the indemnity Jess (WILBA) carries the legal risk, not Higgsfield. A `media_import_url` tool existing does not grant any rights.
- Given the reporting on the broad licence, don't upload anything confidential, such as unreleased tester footage you want to keep exclusive, until the actual §4 licence wording has been read.
- Treat Virality Predictor as a pre-screen only. It is not evidence of performance.

### Gaps
- I could not open the Terms of Use, so exact §4.4, §5 and §12 wording, the licence scope and whether a "no uploading third-party video" clause exists are all unverified.
- Official pricing as of Nov 2026 is unverified, and third-party figures conflict.
- No source described Higgsfield's TikTok publishing terms, for example whether publishing through Higgsfield auto-labels AI content.

---

## 2. Artlist: catalog, licence types, YouTube claims, after cancellation, pricing

### Takeaway
Artlist sells subscription access to music, SFX, stock footage, templates and AI tools (image/video generation, voiceover). Its licence covers YouTube monetisation for content published while you are subscribed. To avoid Content ID claims you register your channel or videos on the **Clearlist** while your plan is active. Videos published during the subscription stay cleared after you cancel. New videos published after cancellation are not covered. The Social licence covers your own channels only. Client or business use needs Pro or Business. You must not use inputs or outputs that infringe third-party IP, and Artlist does not indemnify you for that.

### Cited Findings
**Catalog and AI**
- Artlist covers music, SFX, footage, templates and generative AI tools. — [artlist.io](https://artlist.io/); [Lovart review](https://www.lovart.ai/blog/artlist-ai-review); [Kingy AI](https://kingy.ai/ai-tools/artlist/)
- AI outputs are yours to use and commercialise, but you acquire no rights in the models. Artlist says it and its partners do not train on your prompts, uploads or outputs. It incorporates third-party models that are contractually barred from training on your data "unless Artlist clearly indicates otherwise". — [Artlist Enterprise plan explained](https://help.artlist.io/hc/en-us/articles/33980035053213-Enterprise-plan-explained); [Artlist Licence](https://artlist.io/help-center/privacy-terms/artlist-license/)
- AI-generated content that Artlist itself made and that you download from its catalog/Explore is reportedly treated as an "Asset", not as your Output. The source review is marked overdue for recheck. — [Lovart](https://www.lovart.ai/blog/artlist-ai-review)
- A new Social licence version dated 04-01-2026 (filename: "permitting assets in AI") exists. Its contents were not opened. — [Social License PDF](https://artlist.io/media/g2tebxpm/current-ver-social-license-permitting-assets-in-ai-clean-04012026.pdf)

**Third-party IP restriction and indemnity**
- Users must not provide inputs or generate output that infringes third-party rights "including copyright, trademarks, or other intellectual property rights". Business terms say Artlist "shall not be liable for alleged infringement of third-party rights arising from the Inputs or Outputs". Uploaded inputs are licensed to Artlist "solely to operate, provide, and secure the AI Services". — [Artlist Business Package terms](https://artlist.io/help-center/privacy-terms/business-package/) (snippet only)
- If you work with collaborators or clients, "your collaborator and/or client must comply with the License". — [Artlist Licence](https://artlist.io/help-center/privacy-terms/artlist-license/)

**YouTube monetisation, Content ID and Clearlist**
- Artlist's music is in YouTube Content ID. Clearlist is the internal tool for preventing claims. A claim can still fire on legally downloaded music if the channel or video is not registered. — [Understanding Artlist's Clearlist](https://help.artlist.io/hc/en-us/articles/29648622402333-Understanding-Artlist-s-Clearlist)
- Channel limits reportedly differ by plan: Pro allows 3 channels per platform, Social 1 per platform. — [Artlist Help (snippet)](https://help.artlist.io/hc/en-us/articles/29648622402333-Understanding-Artlist-s-Clearlist); [artlistio.com explainer (unofficial domain)](https://artlistio.com/license/)
- Clearlist covers content containing Artlist **music** only, not SFX or footage. It "can't make an unlicensed use legal". — [DaVinci Resolve 21 guide (secondary)](https://davinciresolve21.com/blog/artlist-clearlist-youtube-claims)

**After cancellation**
- "Any project completed and published during an active subscription remains cleared for monetization, even after the subscription ends." The Clearlist must be updated while the plan is active. After expiry you can't add channels or content, and content published after the subscription ends "won't be covered by the license and is at risk of getting claims". — [Artlist Help Center](https://help.artlist.io/hc/en-us/articles/29490991524253)
- Older accounts may have different rules: reports say pre-Nov 2020 (or pre-Nov 2022) subscribers kept rights to use assets in future projects. The sources conflict. — [Larry Jordan](https://larryjordan.com/articles/caution-be-careful-with-music-licenses/); [Legis Music](https://legismusic.com/the-truth-about-royalty-free-music-licenses-after-cancellation)

**Pricing (not verified on artlist.io/page/pricing)**
- Music & SFX Social: $9.99/mo billed annually or $14.99 billed monthly. Artlist Max (all-in-one): about $39.99/mo billed annually. Max Social: about $29.99 (possibly pre-2026). Max Teams: $33.99 per member per month for 2–7 members. — [Activepieces](https://www.activepieces.com/blog/artlist-pricing-2026-what-every-plan-costs); [CC Hound](https://www.cchound.com/artlist/artlist-subscription-plans-and-pricing/); [Artlist pricing page (not opened)](https://artlist.io/page/pricing)
- Other aggregators (Subger, Vendr) list different Pro-tier prices.

### Inferences
- For Jess's channel, Artlist covers background music, SFX (whooshes, UI clicks, "code entered" stings), non-game stock b-roll and templates for intros and lower-thirds. Add every channel (YouTube, plus any others the plan allows) to the Clearlist before publishing.
- Keep the subscription active for as long as new videos are being published. Music in videos published after cancellation will get claims.
- If WILBA produces videos *for clients*, the Social tier is not enough. Pro or Business is needed.
- An Artlist track only clears the Artlist music. It does nothing for Rockstar radio music or game audio that also appears in the video.

### Gaps
- I could not open the licence PDFs or the pricing page, so exact clause wording and current prices are unconfirmed.
- I could not confirm Clearlist channel limits by plan, or whether TikTok/Instagram need separate registration.
- I could not confirm whether Artlist AI voiceover allows cloning your own voice, or its licence terms for that.

---

## 3. Do either tool permit uploading or remixing other creators' YouTube videos or Rockstar trailers/gameplay?

### Takeaway
No. Neither tool grants rights it doesn't have. Both put the burden on the uploader to warrant they hold rights in what they upload, and neither indemnifies a normal subscriber against third-party IP claims. Remixing another creator's video or a Rockstar trailer is therefore governed by copyright law, Rockstar's own video policy and YouTube's reused-content rules, not by Higgsfield or Artlist. Rockstar's policy targets "occasional, non-commercial" fan use. Take-Two has been actively issuing takedowns, cease-and-desists and DMCA subpoenas over GTA 6 content, including AI-generated GTA 6 videos.

### Cited Findings
- Higgsfield user warranty: inputs must not infringe "copyright, trademark, publicity rights…". You indemnify Higgsfield, and IP indemnity from Higgsfield is Enterprise-only. — [Higgsfield ToS](https://higgsfield.ai/terms-of-use-agreement); [Aliteq](https://aliteq.com/higgsfield-commercial-use)
- Artlist: users must not provide inputs or generate outputs that infringe third-party IP, and Artlist is not liable for third-party infringement arising from Inputs or Outputs. — [Artlist Business terms](https://artlist.io/help-center/privacy-terms/business-package/)
- Rockstar's video policy welcomes fan clips and machinima. It is described as intended for "occasional, non-commercial in-game content use by individual members of the fan community". Footage from leaked copies before release "will be taken down". — [Rockstar Support: Policy on posting copyrighted Rockstar Games material](https://support.rockstargames.com/articles/200153756/rockstar-games-video-policy) (snippet only, not opened)
- YouTube's reused content policy covers commentary, clips, compilations and reactions. Monetisation requires significant original value. Non-original Shorts, such as "re-uploads of other creators' content and compilations with nothing added", are ineligible. The repetitious-content policy was renamed "inauthentic content" (dated 15 Jul 2025 by several sources). — [YouTube Help (support.google.com/youtube/answer/1311392)](https://support.google.com/youtube/answer/1311392); [vidIQ](https://vidiq.com/blog/post/youtube-reused-content-policy-guide/)
- GTA's in-game licensed radio music is a known Content ID claim source. Claimed revenue goes to the rights holder. — [vidIQ](https://vidiq.com/blog/post/get-full-youtube-monetization-gaming-videos/)
- YouTube's advertiser-friendly guidance changed ahead of GTA 6. Graphic gameplay violence in the first ~7 seconds is not ad-eligible. Shock compilations can be demonetised. Thumbnails and titles are reviewed separately. — [Dexerto](https://www.dexerto.com/gta/youtube-updates-gaming-violence-monetization-rules-ahead-of-gta-6-launch-3405945/); [GTA Boom](https://www.gtaboom.com/youtube-wants-your-gta-6-gameplay-and-it-changed-the-rules-to-get-it-44dd)

### Inferences
- Legitimate path: Jess's own captured gameplay from a legitimately purchased copy (released 19 Nov 2026), plus real commentary and testing, fits Rockstar's fan policy best. Even then, a monetised channel sits outside what the policy explicitly blesses, so it is tolerated rather than licensed. Mute or avoid in-game radio.
- Short trailer excerpts used for commentary *might* be fair use (US) or fair dealing (AU: criticism/review/reporting news). That is a legal judgement, not something either tool's licence grants. Default to avoiding trailers and linking to them instead.
- Re-uploading or "AI-remixing" other creators' videos is a copyright, reused-content and channel-wide demonetisation risk. Don't do it.

### Gaps
- I could not open Rockstar's current video policy to quote it exactly or check for GTA VI-specific updates.
- No legal opinion on Australian fair dealing for trailer clips. Jess needs qualified advice if she wants to use trailers.

---

## 4. AI-generated GTA-style characters, logos and scenes: IP risk and platform AI-disclosure rules

### Takeaway
Take-Two has specifically gone after AI-generated GTA 6 content: a cease-and-desist to an AI fake-leak account (apology 24 Apr) and DMCA takedowns of the "Vice Nation" AI-shorts channel featuring Lucia and Jason. Since Aug 2026 it has also filed DMCA subpoenas against platforms to unmask leakers. Generating Lucia, Jason, GTA logos or recognisable Vice City/Leonida scenes is high risk. YouTube and TikTok both require labels on realistic AI content and now auto-detect it.

### Cited Findings
- AI fake-leak account got a Take-Two cease-and-desist and apologised on 24 Apr. Take-Two issued DMCA takedowns against AI-generated GTA 6 videos, including the "Vice Nation" channel (AI shorts of Lucia and Jason). — [GTA Boom](https://www.gtaboom.com/the-gta-6-ai-fake-problem-just-got-its-latest-legal-takedown-779e); [Virlan](https://www.virlan.co/iogames/article/take-two-gta-6-ai-fakes-dmca-takedowns/)
- Since Aug 2026 Take-Two has filed DMCA subpoenas in a New York federal court directed at Discord, Microsoft, X and Google. — [heise](https://www.heise.de/en/news/GTA-6-Leaks-Take-Two-holds-Discord-and-Microsoft-accountable-11423140.html)
- The GTA 6 Mapping Project Discord went offline on 11 Nov 2026. A Take-Two takedown is suspected but unconfirmed. — [Notebookcheck](https://www.notebookcheck.net/Take-Two-reportedly-targets-GTA-6-Mapping-Project-closing-Discord-that-shared-leaks.1448191.0.html)
- Dec 2025: a fan GTA: Vice City browser port was taken down via Ebrand, citing trademark, copyright and circumvention. — [Generation Amiga](https://www.generationamiga.com/2025/12/27/take-twos-dmca-hammer-falls-on-fan-made-gta-browser-revival/)
- Rockstar faces a fake-leak problem it "can't fully stop". — [TheStreet](https://www.thestreet.com/entertainment/rockstar-faces-a-fake-leak-problem-it-cant-fully-stop)
- YouTube requires creators to disclose realistic altered or synthetic content via a Studio toggle. Since a May 2026 update YouTube auto-labels undisclosed AI content and shows the label below the player for photorealistic content. AI voiceover is treated as production assistance and doesn't require the label (secondary sources). — [TechWyse](https://www.techwyse.com/news/platform-updates/youtube-automatic-ai-labels-disclosure-may-2026); [Music Business Worldwide](https://www.musicbusinessworldwide.com/youtube-will-now-automatically-detect-and-label-ai-videos/); [AIR Media-Tech](https://air.io/en/youtube-hacks/youtube-ai-disclosure-in-2026-label-it-yourself-or-youtube-will)
- TikTok requires labels on realistic AI-generated content and may auto-apply an "AI-generated" label, which can't be removed. Ad disclosure became mandatory on 21 Jul 2026 (secondary). — [TikTok Newsroom, Mar 2026](https://newsroom.tiktok.com/tiktok-ssa-shares-more-ways-to-spot-shape-and-understand-ai-generated-content?lang=en-ZA); [Magic Hour](https://magichour.ai/blog/tiktok-ai-generated-content-labels); [Common Thread](https://commonthreadco.com/blogs/coachs-corner/tiktok-ai-ad-disclosure-rules-ecommerce-2026)
- Higgsfield's own contest rules ban unauthorised "characters, franchises, brands, logos". — [Higgsfield contest rules](https://higgsfield.ai/contests/talent-contest?tab=rules)

### Inferences
- Any AI image or video that could pass as a "leak" or as real GTA 6 footage is the exact category Take-Two is targeting. It also damages a trust-first "verified ledger" brand.
- Safe AI visual style: clearly stylised, original, non-GTA art (e.g. a ledger or detective motif), no Rockstar or GTA logos, fonts or characters, and no fake gameplay. Label realistic AI scenes on YouTube and TikTok.

### Gaps
- I did not open YouTube's official help page (support.google.com/youtube/answer/14328491) or TikTok's AIGC support page. The voiceover exemption and the auto-label specifics come from secondary sources.
- No source on Take-Two enforcement against fan *thumbnails* specifically.

---

## 5. Legitimate high-value uses for the channel

### Takeaway
The safe, valuable uses are: Artlist music and SFX (Clearlisted), Artlist stock b-roll that isn't game footage, Higgsfield/Artlist AI for an original channel intro, logo motion and thumbnail backgrounds, reformatting Jess's own long-form into vertical Shorts, and voice tools only with Jess's own voice, disclosed.

### Cited Findings
- Artlist music and SFX are licensed for YouTube monetisation while subscribed, and the Clearlist prevents Content ID claims. — [Artlist Help: Clearlist](https://help.artlist.io/hc/en-us/articles/29648622402333-Understanding-Artlist-s-Clearlist)
- Higgsfield outputs can be used commercially, including YouTube monetisation, on any plan. — [Higgsfield Help](https://higgsfield.ai/creator-hub/help-center/account/who-owns-my-generations-and-can-i-use-them-commercially)
- The Higgsfield help centre bars using another person's image without permission. Contest rules go further and bar even your own likeness or voice in contests. — [Higgsfield Help](https://higgsfield.ai/creator-hub/help-center/account/who-owns-my-generations-and-can-i-use-them-commercially); [contest rules](https://higgsfield.ai/contests/talent-contest?tab=rules)
- YouTube reportedly treats AI voiceover as production assistance, so it isn't label-triggering. A realistic synthetic person would be. — [AIR Media-Tech](https://air.io/en/youtube-hacks/youtube-ai-disclosure-in-2026-label-it-yourself-or-youtube-will)
- Watermarks on lower tiers may make output unsuitable for some uses. — [Higgsfield Help (via search summary)](https://higgsfield.ai/creator-hub/help-center/account/who-owns-my-generations-and-can-i-use-them-commercially)

### Inferences
- Use **Artlist** as the default audio layer: one plan covers music and SFX for every video, as long as the subscription stays active.
- Use **Higgsfield** for original branding, intro stings, stylised thumbnail backdrops, `reframe` of Jess's own footage to 9:16, and Virality Predictor as a hook pre-check. Don't use Higgsfield's AI Influencer to create a fake "host": it conflicts with the channel's "real tester" trust promise.
- If Jess clones her own voice (Higgsfield `create_voice`), use it for pickups or corrections only, keep a consent record, and disclose where realistic.
- Don't use any tool to generate fake "leaked" GTA 6 footage, GTA character likenesses or Rockstar logos.

### Gaps
- No primary-source confirmation of whether Higgsfield's TikTok publishing applies TikTok's AIGC label automatically.
- No primary-source confirmation of Higgsfield watermark rules by plan.
