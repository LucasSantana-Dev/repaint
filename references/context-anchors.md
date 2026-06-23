# Context Anchors — references beyond dev-tool/SaaS

The base skill anchors heavily to Linear/Vercel/Stripe (dev-tooling). That's wrong by reflex for an
e-commerce page, a patient portal, or an editorial feature. This file gives **named, context-fit
anchors + concrete tokens + the slop tells specific to each context**, plus a palette of aesthetic
directions for art-direction mode and the 2026 token defaults.

Synthesized 2026-06-22 from web research across Dribbble/Mobbin/SaaS galleries, the Figma Community +
design-system docs, and type-foundry/editorial trend writeups. Anchors are real, named products;
treat their token specifics as *approximate* unless you confirm them. Where a claim was inferred
rather than sourced it is marked `(inferred)`.

**Refreshed 2026-06-23:** added the AI-chat and command-palette contexts; added 2026 slop tells
(bento-outside-landing, gradient-on-data, over-animation, pixel-font-as-body, default variable fonts);
re-verified anchors — Linear, Warby Parker, Aesop, the fintech set, the healthcare set, and Material 3 /
Carbon all still current (Material 3 added an "Expressive" layer but kept semantic color intact); flagged
Medium's shift to a system serif and Glossier's unconfirmed 2026 direction. The purple→blue gradient is
*confirmed* across 2026 sources as the single most common AI-UI tell.

---

## A. Context → register, anchors, tokens, must-haves, tells

Pick the row matching the brief. The **anchor** is the named bar to hit; the **tells** are what makes
that *specific* context read as AI-made.

### E-commerce product detail (DTC / retail) — register `marketing`/`ecommerce`
- **Anchors:** Warby Parker (editorial product discipline — the brand's edge is its product/features; the *web* lesson is presentation restraint), Nike (scroll-revealed product story), Aesop (quiet, typography-led, calm motion). *(Glossier was the classic pairing but its current direction is unconfirmed for 2026 — verify before anchoring to it.)*
- **Tokens:** warm-neutral ground (not dark dev-tool); serif or characterful sans for product name + clean sans for price/CTA; 24–32px section gaps, 80–120px between major blocks; *intentionally varied* card spacing, not uniform 16px radius everywhere.
- **Must-haves:** gallery with zoom; variant selectors (shade/size) with live preview; price + add-to-cart above the fold; reviews/social proof *before* the CTA; real product photography, never AI-smooth stock.
- **Tells:** uniform 16px radius on everything; stock "diverse team" photos; vague copy ("elevate your routine"); purple→blue gradient; missing a real product image.

### Fintech / banking dashboard — register `product-app` (fintech)
- **Anchors:** Revolut, Monzo, Cash App, Robinhood (data-viz), YNAB (category color-coding).
- **Tokens:** dark-first; semantic status colors (green=up, red=down, amber=warn) applied *consistently*; tight internal spacing (8–16px) with 24px+ between sections; mono for figures/balances; **no gradients inside data viz** (kills clarity).
- **Must-haves:** balance summary; account cards; transactions list; one clear chart; a primary money action (transfer/pay). Trust signals near sensitive data.
- **Tells:** inconsistent accent meaning; circular-progress overload; decorative gradient charts; system-default font pairing; gamification bolted on without purpose.

### Healthcare / patient portal — register `product-app` (healthcare)
- **Anchors:** Teladoc (one-tap telehealth), b.well, Sidekick/Reframe (calm chronic-care). 
- **Tokens:** **calm soft palette** (soft green/blue, warm neutrals), never harsh saturation; large type + generous whitespace; WCAG AA+ contrast and **44px touch targets** mandatory; visible trust signals (lock, privacy, certification) near data entry.
- **Must-haves:** appointments; medications; lab/results; message-your-doctor; progressive disclosure (show only what's relevant); smart defaults / pre-filled values.
- **Tells:** generic "doctor in white coat" imagery; hedging copy; missing trust badges; unexplained medical jargon; anxiety-inducing reds; cramped density.

### Editorial / long-form article — register `marketing` (editorial)
- **Anchors:** Substack (serif body + author-controlled branding), The Verge (custom type + real imagery), ProPublica (Tiempos, institutional rigor), classic magazine features. *(Medium shifted to a system serif ~2024–25, so it is no longer the custom-serif exemplar — keep Lyon/Tiempos/GT Sectra as the type benchmark, not Medium's own stack.)*
- **Tokens:** **serif body** (Tiempos, Lyon, GT Sectra, Editorial New, Spectral, Cormorant) at **1.5–1.65 line-height**, measure **~60–75 chars (650–800px)**; sans only for UI/metadata; 80–120px side margins; paragraph spacing ~1.5–2× line-height; **no cards/boxes around prose**.
- **Must-haves:** headline + byline + read-time; hero image; pull-quotes; section breaks; related-stories footer (not a competing sidebar).
- **Tells:** system serif (Georgia) with no personality; cards around text; AI-smooth article illustrations; "The Ultimate Guide to…" headings; filler ("In today's world").

### Mobile app home screen — register `product-app` (mobile)
- **Anchors:** Spotify (adaptive shelves), Apple Music, Telegram (gesture system), Apple Maps (context modes).
- **Tokens:** **bottom-centric navigation** (thumb reach); 8px internal padding, 16–24px section gaps; single driving accent; dark-first; design at the stated width (e.g. 390px) — don't ship a desktop layout shrunk.
- **Must-haves:** bottom tab bar OR bottom sheet; primary stat/CTA in thumb zone; recent/list section; touch targets ≥44px; pull-to-refresh / gesture affordances where natural.
- **Tells:** top-heavy nav forcing thumb stretch; uniform 8px everywhere; generic shelf labels ("Recommended"); oversized stock illustration; desktop-shrunk layout.

### B2B analytics dashboard / enterprise admin — register `product-app` (b2b-data-dense)
- **Anchors:** Tableau (presentation-grade viz), Looker (semantic metrics), Carbon (enterprise grid).
- **Tokens:** dark-first; resizable card grid (4–12 col); **semantic data colors, no decorative gradients**; mono for metrics; sticky filter/date header; chart margins on the 4px grid; "updated Xs ago" real-time cue.
- **Must-haves:** date-range picker; collapsible filters; drill-down; export (CSV/PDF); density that respects importance (lead metric larger).
- **Tells:** placeholder chart icons / fake data; generic metric names ("KPI", "Performance"); decorative gradients; no drill-down; no freshness indicator.

### Auth (sign-up/login) + error/404 — register `product-app` (utility) / `utility`
- **Anchors:** Vercel (high-contrast minimal), Stripe (explicit errors), Clerk (passkey/social-first).
- **Tokens:** purposeful heading ("Sign in to continue to Acme", not "Login"); 24px between fields, 32px between sections; full-width CTA on mobile, 48px targets; single semantic accent.
- **Must-haves:** email-first; password visibility toggle; inline (not modal) errors with *specific* text ("Incorrect email or password"); social/passkey ordered by audience (consumer→social first, B2B→email/SSO first); on 404: branded illustration + clear "Go home" + search/related links.
- **Tells:** "Something went wrong" / generic errors; placeholder-as-label; stock illustration on the 404; tiny targets; oversized desktop fields.

### Marketing event / product-launch — register `saas-landing` / `marketing`
- **Anchors:** Stripe ("Financial infrastructure for the internet" — 5-word clarity), Vercel launch pages, Linear.
- **Tokens:** display headline 40–80px; one accent on a committed light or dark hero; 80–120px section padding; real product screenshots/video over mockups.
- **Must-haves:** hero (headline + sub + CTA + product visual); features 3–4 col; trust signals (named logos, G2/specific metrics); pricing/comparison if relevant; founder voice.
- **Tells:** "Build the future of work"/"Scale without limits"; stock office photo; rounded-corner-everything; purple→blue gradient; no named/measurable proof.

### AI / LLM chat & agent interface — register `product-app` (ai-chat)
- **Anchors:** ChatGPT (streaming thread + left-rail history), Claude.ai (centered ~768px measure, side artifact panel), Perplexity (citation-forward, numbered inline sources), Raycast AI (compact, OS-native density), v0 (prompt → live code + preview).
- **Tokens:** dark-first baseline; one restrained action accent (teal/blue), **never a purple→blue gradient** (the #1 AI-UI tell); semantic status (error/success/warn/info); full-width message containers on a subtle ground, *not* chat bubbles everywhere; mono (JetBrains Mono, Geist Mono) for code; body 16px / 1.6; a committed sans, not Inter-by-default; radius varied by role (don't paint 16px on everything).
- **Must-haves:** streaming output (token-by-token) with a **stop** control; a growing multiline composer (Cmd/Ctrl+Enter to send); a per-message action row (copy, edit, regenerate); markdown with syntax-highlighted, copy-able code blocks; citations as numbered footnotes / inline links (Perplexity); left-rail conversation history grouped by date (Today / Yesterday / 7d+); a model picker if multi-model; explicit error recovery (stop, retry, visible failure).
- **Tells:** purple→blue gradient; the generic **"centered input + sparkle icon + 'How can I help you today?'"** template dropped into an unrelated domain; chat-bubble UI forced everywhere; no streaming affordance (waits for the full response — feels broken); visible markdown artifacts mid-stream (half-open code fences); uniform 16px radius; Inter/system-by-default; vague "Ask anything" over specific capability language.

### Command palette / action launcher — register `product-app` (utility)
- **Anchors:** Superhuman (centered modal, monospaced commands, icon per row, toggle), Linear (Cmd+K convention, fuzzy + context-aware filtering), VS Code / Figma (the power-user baseline users now expect).
- **Tokens:** inherit the app theme; subtle backdrop (app bg + opacity, not a heavy black scrim); selected row uses the app accent; **no gradients**; a monospaced or tight UI face for commands (JetBrains / IBM Plex / Geist Mono); rows 40–48px (touch ≥44px); centered modal 500–700px desktop, near-full-width mobile.
- **Must-haves:** Cmd+K trigger (same shortcut toggles open/closed); fuzzy search with typo tolerance, not exact-match; an icon per command; context-aware filtering (hide commands unavailable in the current state/role); action-focused titles (Create…, Find…, Export…) with aliases for discoverability; displayed keyboard shortcuts; an overflow hint (more below the fold); focus restoration on close.
- **Tells:** a bare text-only list with no icons or hierarchy; the default system font (loses the "powerful tool" signal); no shortcuts shown; a corner dropdown instead of a centered modal; exact-match-only search; generic category names ("Features", "Tools") instead of verbs.

---

## B. Aesthetic directions for art-direction mode

When the brief is creative/open ("surprise me", "bold", brand-expression), pick ONE of these named
directions instead of inventing a vibe. Each carries real typefaces + a color stance.

1. **Warm editorial serif** — refined, cinematic. *Editorial New, Tiempos, GT Sectra, Lyon.* Warm grays + terracotta/ochre. Use: luxury, heritage, long-form.
2. **Swiss / neo-grotesque** — rational, grid-native, trustworthy. *Neue Montreal, GT America, Söhne.* Off-white/charcoal + one restrained accent. Use: systematic tech, modern corporate.
3. **Soft-organic / biophilic** — calm, wellness, grounded. *Neue Gstaad, Palma* + humanist body. Mushroom/clay/moss, softened blues. Use: health, eco, meditative.
4. **Brutalist / neo-brutalist** — raw, confrontational, honest. *Monument Extended* + a mono. Bold primaries, solid (un-blurred) 4px drop shadows, visible grid seams. Use: provocative indie/tech.
5. **Typographic maximalism / kinetic** — type as hero. *Neue York, GT Flexa* (variable). Saturated, layered color within type. Use: music, entertainment, expressive campaigns.
6. **Retro-futurist / material 3D** — tactile, exuberant, Y2K-revived. Bold display + tactile glass/metal (with real texture, not CGI sheen). Saturated. Use: consumer delight, gaming.
7. **Imperfect-by-design** — anti-sterile, crafted, human. Hand-drawn display + mono body; grain/riso texture. Warm wheat/caramel/sage. Use: indie/DTC, editorial identity.
8. **Deconstructed / specimen** — intellectual, curatorial, "pinned specimen". Experimental lettersets, numbered cut-outs, B&W + one accent. Use: gallery, academic, catalogues.

Foundries to draw from (named, current): **Pangram Pangram, Grilli Type, Klim, Commercial Type, ABC Dinamo.** Free routes: Bricolage Grotesque, Fraunces, Spectral, Cormorant, Geist, IBM Plex, JetBrains Mono.

---

## C. 2026 token defaults (when the project has none)

- **Spacing:** 8px grid for layout, 4px sub-grid for internal padding. Steps 4/8/12/16/24/32/48/80/120.
- **Type scale:** 16px base, modular ratio ~1.25; line-height snapped to the 4px grid (e.g. 14/20, 16/24). Editorial body 1.5–1.65.
- **Radius:** semantic XS/S/M/L/XL/Full = 2/4/8/12/16–24/9999. Assign per component; don't paint one radius on everything.
- **Elevation:** ≤5 levels; modern depth = two-part shadow (sharp key + soft ambient), or color-contrast elevation (Carbon). Avoid the default `0 4px 6px rgba(0,0,0,.1)`.
- **Color naming:** semantic tokens (`bg-surface`, `text-muted`, `border`, `accent`), one name → per-theme value. Dark mode is a first-class context, not a `dark:` afterthought; step surfaces +5–8% luminance.
- **Accessibility:** 4.5:1 text / 3:1 UI+large; focus ring ≥2px at ≥3:1; touch targets ≥44px (24px is the AA floor).
- **2026 color stance:** the field shifted from cool steely grays (2022) to **warm earthy neutrals + one restrained accent**. Tint neutrals; reserve saturation for a single accent. Concrete warm neutrals: wheat `#E3DAC9`, taupe `#CAB9A9`, warm gray `#908D87`; earthy accents: terracotta `#CC5959`, ochre `#E6B35A`, smokey-jade `#4A635D`.

---

## D. Updated slop catalog (additions to the base hard bans)

The base SKILL.md already bans purple gradients, generic bento, glassmorphism-by-default, default
shadow, em dashes, and emoji-as-icons. Add these, confirmed across 2026 trend sources:

- **Decorative glassmorphism** — frosted cards/blur as spectacle reads as 2021–22. *Nuance:* restrained, **functional** depth ("glass 2.0" — blur used for legible layering over content, e.g. a now-playing bar) is fine. Decoration out; function in.
- **Oversaturated hyper-smooth 3D** — pristine CGI gradient spheres / liquid-metal blobs. If 3D, give it real texture/imperfection.
- **Perfect symmetry + dead-center everything** — reads as algorithm. Use grid-based but human-adjusted asymmetry.
- **Neumorphism** — soft debossed/embossed buttons; dated to ~2020.
- **AI-smooth stock imagery** — impossibly polished + "diverse office". Prefer real photography (with grain/character), custom illustration, or data-as-imagery.
- **Algorithmic HSL color ramps** — evenly-stepped lightness ladders with no human curation; tells as generated. Curate with reasoning (warm vs cool, where saturation goes).
- **Uniform-everything** — identical radius + identical padding on every element. Vary by role.
- **Vague/averaging copy** — "Scale", "Transform", "Seamlessly integrate", "Build the future of X". Replace with specific, measurable, founder-voiced lines.
- **Bento outside its lane** — the bento grid is a *landing-page* device. On a product-app dashboard, a dense data table, or a product-detail page it reads as trend-chasing; those registers want scannable hierarchy and functional density, not modular tiles. (Extends the base generic-bento ban to non-landing registers.)
- **Gradient on data** — gradient-filled chart series, or the "big hero metric + gradient accent line" pattern (now in ~90% of generated SaaS dashboards). Numbers and data viz take *solid semantic* color; a gradient on a value is decoration that costs clarity.
- **Over-animation on dense UI** — Framer Motion / Motion.dev / Spline make it trivial to animate everything; on dashboards, tables, and feeds that obscures scannability. Motion is for feedback and state change, not decoration on information-dense surfaces.
- **Pixel / bitmap display fonts as body** *(critical)* — Geist Pixel and similar bitmap faces are a real 2026 trend but **logotype/campaign-only**; using them for body text, sustained reading, or any accessibility-critical copy is an instant tell.
- **Variable fonts left at defaults** — loading a variable face (GT Flexa, etc.) but never setting weight/width/optical-size reads as "installed the tech without designing with it." Variable fonts demand intentional axis choices.

---

## E. Typeface by role (stop defaulting to Inter)

- **Display (tech):** Geist, Neue Montreal, GT America, Bricolage Grotesque.
- **Display (editorial/luxury):** Editorial New, Tiempos, GT Sectra, Fraunces, Playfair Display.
- **Body (reading):** Tiempos/Lyon/Spectral/Cormorant (serif); Geist Sans, Söhne (sans).
- **Body (calm / wellness):** Neue Gstaad — humanist sans, soft apertures; health, eco, meditative surfaces.
- **Functional UI:** Geist Sans, IBM Plex Sans (Inter only if `DESIGN.md` already commits to it).
- **Mono (flavor/metrics):** JetBrains Mono, Geist Mono, GT America Mono, Söhne Mono.
- **Never for body:** pixel/bitmap display faces (Geist Pixel) and any mono — logotype, code, and retro/zine campaigns only.
- **2026 shift:** the field moved from geometric sans (Circular, Montserrat) to **neo-grotesque** — prefer Neue Montreal, Söhne, or the free Bricolage Grotesque for display/UI in systematic contexts.

---

## Sources (condensed)
Dribbble/Mobbin/SaaS-gallery context research, Figma Community + design-system docs (Material 3,
Polaris, Carbon, Fluent 2, Ant, Primer, Mantine, Radix/shadcn), and foundry/editorial trend writeups
(Pangram Pangram, Grilli Type, Klim, Commercial Type; Adobe/Fontfabric/It's Nice That 2026 trend
reports; NN/g neobrutalism). Full URL list in the research run logs. Token specifics for named
products are approximate unless confirmed in that product's own design docs.

2026-06-23 refresh drew on the AI-UI anti-pattern writeups (BSWEN AI-UX anti-patterns; Muzli "why every
AI app looks the same"), AI-chat anatomy guides (Setproduct, thefrontkit), Superhuman's command-palette
notes, Fontfabric's 2026 typography trends + Vercel's Geist Pixel release, the bento-in-2026 critiques,
and primary design docs (Linear design-refresh notes, Aesop, ProPublica typography, Material 3 / m3.material.io).
