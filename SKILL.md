---
name: repaint
description: Build production-grade frontend UI that doesn't read as "AI-made" — and behaves like an elite product, not just looks like one. A self-contained pipeline — research real references, lock a register + a named anchor, commit a concrete token system (OKLCH color, distinctive type), design the interaction (feedback, forgiving input, keyboard paths, recoverable actions), build in your framework, then iterate against a slop-audit + experience-audit + live browser-screenshot feedback loop. Use for any page, component, dashboard, landing page, hero, pricing section, settings panel, data table, onboarding, or app surface — especially when output looks generic, templated, or "AI-made", or when the interaction feels hollow, and you want it to feel like Linear, Vercel, Stripe, Notion, or a real design studio. Ships a reference library (named anchors per context, 8 art-direction directions, 2026 token defaults, a slop catalog, type-by-role, interaction/experience patterns, microcopy) and 19 evals.
license: Apache-2.0
metadata:
  homepage: https://github.com/LucasSantana-Dev/repaint
---

# repaint

A self-contained pipeline for frontend UI that looks designed, not generated — **and behaves like it, too.** It depends on **no other skills and no agents** — everything it needs ships in this folder. It stands on five pillars:

1. **Scraping** — research *real, current* references for the brief (your web search), not vibes.
2. **Tokens** — commit a concrete token system (OKLCH color + distinctive type) before any markup.
3. **References** — a curated library ([references/context-anchors.md](references/context-anchors.md)) of named anchors per context, art-direction directions, 2026 token defaults, a slop catalog, type-by-role, plus experience patterns and microcopy.
4. **Experience** — the *interaction* is designed, not just the pixels: honest feedback and perceived performance, forgiving input, recoverable actions, and a real keyboard path. Looks pass the eye; experience passes the hand. Gate 4, Gate 5, and the experience audit enforce it.
5. **Real iteration feedback** — build → render → screenshot → slop-audit + experience-audit → iterate, against live browser output, not a one-shot guess. The 19 [evals](evals/evals.json) are the regression harness.

## Where this skill earns its keep

A capable model already produces *competent generic structure* on a well-specified brief (a pricing page gets a comparison table and a "Most Popular" badge unaided). Don't spend effort re-adding structure the model nails alone. The real leverage — eval-verified — is in five places the model gets wrong without help:

1. **Killing cliché on open/creative briefs.** Left alone, "make it bold/memorable" collapses to the same neon-gradient-on-dark or purple-gradient tells. The register lock + slop audit prevent that. This is the single biggest win.
2. **Register-appropriate restraint.** A `product-app` settings panel should be calmer than a `saas-landing` hero. The model over-decorates by default; the register playbook pulls it back.
3. **Distinctive typography.** The model defaults to Inter/system fonts; Gate 3 forces a committed type choice.
4. **Compile-clean, durable output.** Generated copy and tokens must actually build and be written down (Phase 3 string rule + `DESIGN.md` persistence).
5. **Wired, honest interaction.** Generated UI *looks* fine but the interaction is hollow — handlers that do nothing, states styled but never reached, silent submits with no loading feedback, `<div onClick>` with no keyboard path, generic "Something went wrong" copy. This is the experiential "AI made that". Gate 4 + Gate 5 + the experience audit force real, reachable, honest interaction.

## Mode detection (before any phase)

**Art-direction mode** when the brief contains: bold, editorial, experimental, scroll-driven, unforgettable, striking, art-directed, motion-heavy, avant-garde, or when the visual concept itself is the primary challenge.

**Production mode** (default) for everything else: dashboards, landing pages, app surfaces, settings, onboarding, data tables, command palettes, marketing sites, and any surface where credibility with a tech-savvy audience matters.

---

## Phase 0 — Research references (the "scraping" pillar; skip if direction is locked)

When the design direction is open, gather *real, current* references before committing — do not invent a vibe:

- **Use your web search** for `<product type> <industry> <style> 2026` and for the named anchor's own site (e.g. "Linear pricing", "Stripe docs", "Warby Parker product page"). Pull: dominant palette, the actual typefaces, the layout pattern, and the spacing rhythm.
- **Open [references/context-anchors.md](references/context-anchors.md) §A** for the named anchor + concrete tokens that fit this context (retail, fintech, healthcare, editorial, mobile, b2b dashboards, auth) — it is the curated, offline version of the same research.

Extract: recommended palette, typography pairing, layout pattern, and the anti-patterns to avoid.

**Skip when:** the user gave a reference brand, an existing `DESIGN.md` is found, art-direction mode is detected, or the user gave explicit visual direction.

---

## Phase 1 — Quality gates (production) / Design thinking (art-direction)

### Production mode: run all 5 gates in order

**Gate 0.5 — Register lock.** Classify the brief into exactly one of:
- `personal-portfolio` — identity-first, single person
- `saas-landing` — product marketing, convert visitors
- `product-app` — post-login app surface
- `marketing` — blog, launch page, campaign
- `docs` — API reference, developer docs, KB

If the brief matches 2+ registers, ask one disambiguation question first. **Default-DENY:** SaaS-landing patterns (bento grid, dual-CTA hero, feature-row rhythm) must NOT apply to other registers without affirmative intent. In particular **marketing ≠ saas-landing**: a launch/announcement page gets a narrative/editorial layout + an editorial anchor (Stripe-marketing, Medium, The Verge, Linear changelog), never a feature-card grid (and NOT a .map() loop over identical feature cards: fold highlights into the narrative prose, or give each a distinct, varied treatment — alternating sides, different sizes) or product-UX anchor.

**Gate 2 — Reference anchor.** Pick ≥1 named industry pattern; the anchor is a contract — use actual tokens, not vibes. State it in one sentence: *"Sidebar anchored to Linear; cards anchored to Stripe Dashboard."* **Don't reflex to Linear/Vercel** — those are dev-tooling anchors, the wrong bar for an e-commerce page, a patient portal, an editorial feature, or a banking app. For ANY non-dev-tool brief, open [references/context-anchors.md](references/context-anchors.md) §A and use the named anchor for that context.

**Gate 3 — Token spec.** Lock concrete tokens before writing markup:

| Category | Must specify |
|---|---|
| Color | OKLCH triplets for `bg`, `fg`, `muted`, `border`, one `accent` — tinted toward the accent hue. Never `#000`/`#fff`. |
| Type | Display family + weight, body family + weight, mono. Weight contrast ≥400 between display and body. **Name the actual faces** — never Inter/Roboto/Arial as the default body, not even in the fallback stack, and not a bare `font-serif`/`font-sans` generic (that resolves to Georgia/system — the "no-personality" tell). Pick a real face from [context-anchors.md](references/context-anchors.md) §E. |
| Spacing | Base unit (4pt or 8pt). Max 6 steps. State where each applies. |
| Radius | ≤3 values, assigned per component. |
| Motion | Duration tokens (120/200/320ms). Ease curve. No bounce. |
| Accessibility | WCAG 2.2: 4.5:1 (normal text), 3:1 (large/UI), focus ring ≥2px at ≥3:1, touch targets ≥44px. |

When the project has no tokens, use the **2026 token defaults** in [context-anchors.md](references/context-anchors.md) §C (warm earthy neutrals + one restrained accent, 8/4px grid, semantic radius, two-part-shadow elevation).

**Gate 4 — Component anatomy + interaction affordances.** Every interactive component designs all 8 states: default, hover, focus, active, loading, empty, error, disabled (loading/empty/error are the most-skipped). Each state must carry three things, not just a look:
- **Visual feedback** — the state is *perceivable* (a real spinner/skeleton on load, a pressed look on active), never a silent change.
- **Keyboard access** — a `:focus-visible` ring per Gate 3 (≥2px at ≥3:1); semantic `<button>`/`<a>`/`<input>` not `<div onClick>`. For a custom control, document its interaction model (focus order, keys, state changes) in `DESIGN.md`.
- **Outcome clarity** — the result is announced ("Copied", `Saving…` → `Saved`, an inline error), not left for the user to guess.

**Gate 5 — Experience contract.** The cross-cutting interaction guarantees, beyond any single component (cross-references Gate 3 for the a11y numbers and §A for per-context density — does not restate them):
- **Honest feedback + perceived performance.** Optimistic UI or a skeleton for content; a spinner only for brief actions; never a silent wait >1s. <100ms feels instant; show progress by ~800ms; explicit progress + cancel beyond ~1s. (See [§F](references/context-anchors.md).)
- **Forgiving input.** Smart defaults; validate on blur or submit, **not on every keystroke**; specific, inline, non-blaming errors; autosave/draft for anything long. (Microcopy patterns in [§G](references/context-anchors.md).)
- **Recoverable actions.** A destructive action (delete, charge, publish) needs **confirm *or* undo** — a clear confirmation (safe option focused, the verb named: "Delete invoice") or a live undo affordance. Never a bare immediate delete.
- **Keyboard path to the primary task.** The main action is reachable and operable by keyboard end-to-end; modals trap focus intentionally and `Esc` closes, returning focus to the trigger.
- **Motion safety.** Honor `prefers-reduced-motion`; no parallax/auto-play that can't be stopped.

### Art-direction mode: design thinking instead

Commit to ONE bold named direction from [context-anchors.md](references/context-anchors.md) §B — warm-editorial-serif, Swiss/neo-grotesque, soft-organic/biophilic, brutalist, typographic-maximalism, retro-futurist-3D, imperfect-by-design, or deconstructed/specimen. Each carries real typefaces + a color stance. Choose an extreme and execute with precision. What makes it unforgettable? One distinctive thing the user will remember.

### Persist the decisions to `DESIGN.md` (both modes)

Before writing component code, write the locked register, anchor(s), token table, and direction to a `DESIGN.md` at the project root (or update it if present). A rationale that lives only in chat is lost when the session ends, and the surface drifts. **If a `DESIGN.md` already exists, its tokens are non-negotiable — adopt them; do not invent a competing palette.**

---

## Phase 2 — Scaffold

Route by project setup, and **defer to any established design system — it overrides Gate 3.** This is the most common way a UI pipeline regresses below a no-skill baseline: a custom OKLCH spec *conflicts* with a system that already owns tokens, and you get the worst of both (raw `bg-red-50` colors instead of either system).

- **shadcn `components.json` present** → use its **semantic tokens** (`bg-primary`, `text-muted-foreground`, `bg-destructive`, `border-input`) — never raw color classes, never a parallel OKLCH palette — and its primitives (`Field`/`Label`, `Button` variants, `cn()`), and its `iconLibrary`.
- **Tailwind config present** → adopt its token structure and primitives.
- **An existing `DESIGN.md`** → adopt its tokens verbatim.
- **Neither** → scaffold from the project's conventions; Gate 3 supplies the tokens.

---

## Phase 3 — Build

Implement in the project's framework + file conventions; the code should look like the team wrote it.

- Write realistic content (not "Lorem ipsum" or "Item 1").
- One H1 per page; no restated headings; no em dashes in UI copy.
- **Copy must compile — but never corrupt the apostrophe.** Contractions ("you're", "we'll", "don't") break a *single-quoted* JS/TS string. The fix is about the **string's outer quotes**, never the apostrophe:
  - In JSX text nodes, leave it exactly as written — `<span>Don't have an account?</span>` is already valid.
  - In string literals (props, `data` arrays, `aria-label`), wrap the whole value in **double quotes** (`"you're"`) or a **template literal**.
  - **NEVER replace the apostrophe** with a double-quote or backtick — `Don"t` is a visible typo, not a fix.
- **Microcopy carries the experience.** High-stakes text is specific and human, never generic placeholder: errors name the problem *and* the next step ("Email already in use — try another or reset your password", never "Something went wrong" / "Invalid input"); CTAs are verb-forward ("Create workspace", not "Submit"/"OK"); empty states reassure and point somewhere ("You're all caught up — we'll let you know"); confirmations name the action ("Delete this conversation?", not "Are you sure?"). Test each: does it tell the user what happened and what to do *without* reading the surrounding prose? Full patterns in [§G](references/context-anchors.md).

---

## Phase 4 — Audit + verify (the "real iteration feedback" pillar)

This is a loop, not a one-shot check: **build → render → screenshot → audit → iterate** until it passes.

### Slop audit (mandatory)

Run these on the output. Any critical finding = fix before done.

| Pattern | Severity | Signal |
|---|---|---|
| Distributional convergence | critical | All of: Inter + purple gradient + rounded cards + 3-icon row |
| Sophisticated-dark mismatch | critical | Dark + cyan palette on a non-SaaS register |
| Clarity / identity fail | critical | 3-second scan fails OR a portfolio passes the name-swap test |
| Purple gradient | major | violet→pink/blue gradient in the hero |
| Bento trifecta | major | bento + dark + repeated feature blocks |

**Hard bans** (instant rewrite): purple/blue gradient on white · generic bento hero (3×2 colored tiles) · identical card grid (icon + heading + 2 lines × N) · glassmorphism by default · `box-shadow: 0 4px 6px rgba(0,0,0,0.1)` as elevation · em dashes in UI copy · **emoji as UI icons** (`📊` `🔧` in cards/nav/buttons — one of the loudest "AI made that" tells; use the project's icon set or inline SVG). The extended 2026 catalog is in [context-anchors.md](references/context-anchors.md) §D.

**Five-second test:** would an engineer at Linear/Vercel/Stripe say "AI made that" within 5 seconds? If yes, return to Gate 2 and pick a stronger anchor.

### Experience audit (mandatory)

The slop audit catches the *looks*; this catches the *behaviour* — the experiential "AI made that". Run it on the output. Any critical finding = fix before done.

| Pattern | Severity | Signal |
|---|---|---|
| Hollow interaction | critical | `onClick` that does nothing · states styled in CSS but no code path reaches them · `<div onClick>` with no key handler/role |
| Destructive w/o recovery | critical | delete/charge/publish fires immediately — no confirm, no undo |
| Silent action | critical | submit/load with no spinner/skeleton/optimistic feedback; the user can't tell it worked (and double-submits) |
| No keyboard path / invisible focus | major | the primary action is unreachable by Tab, or `outline:none` with no replacement |
| Validation on every keystroke | major | a red error on the first character, before the user has finished typing |
| Dead-end empty/error state | major | "No data" / "An error occurred" with no cause and no next step |
| Generic microcopy | major | "Something went wrong" / "Submit" / "No items" instead of specific, actionable copy |
| Motion ignores reduced-motion | major | animation/parallax with no `prefers-reduced-motion` guard |

**Experience hard bans** (instant rewrite): `<div onClick>` for an action (use `<button>`) · placeholder-as-label · `outline: none` with no focus replacement · a destructive action with neither confirm nor undo · a blocking full-page spinner as the default loading state · toast-only reporting of a *critical* error that auto-dismisses before the user can act. Extended catalog + the elite alternative for each: [context-anchors.md](references/context-anchors.md) §F.

**Experience test:** could you complete the primary task **keyboard-only**, see honest feedback at every step, recover from a mistake, and never hit a dead end? If no, return to Gate 4 / Gate 5.

### Browser verification (the real feedback)

Render it for real and look — don't trust the code alone:
- Run the project's dev server, navigate with **Playwright** (or your browser tooling), and **save desktop + mobile screenshots**.
- Capture console errors and check responsive breakpoints + a11y (axe-core).
- **Interaction:** `Tab` through the page — every interactive element shows a visible focus ring, in a logical order; the primary action is reachable and fires on `Enter`/`Space`. Trigger one **error** state (is the copy specific?) and one **loading** state (does feedback appear before it resolves?). **Screenshot a loading and an error state — not just the happy path.**
- **If the screenshot fails the slop audit *or the experience audit*, a console error appears, focus is invisible/trapped, or a breakpoint breaks → return to the relevant phase, fix, and re-screenshot.** Repeat. Do not declare done on a one-shot render.

**Fallback:** if no browser is available, mark verify as PARTIAL and recommend a manual smoke test.

---

## Reconciliation output (signal-first)

```
FRONTEND — <surface name>
Mode:      <production|art-direction>
Register:  <register> — <DONE|SKIPPED>
Anchor:    <named references> — <DONE|SKIPPED>
Tokens:    <locked table or "from DESIGN.md"> — <DONE|SKIPPED>
DESIGN.md: <path written, or "inline — no repo"> — <DONE|SKIPPED>
Built:     <files created/modified> — <DONE|BLOCKED>
Audit:     <slop pass|N rewrites; copy compiles> — <DONE|BLOCKED>
Experience: <feedback on load/error states Y/N; keyboard path + visible focus Y/N; destructive action recoverable Y/N; microcopy specific Y/N> — <DONE|BLOCKED>
Verified:  <a11y score, console clean Y/N, breakpoints, loading+error screenshots> — <DONE|PARTIAL|BLOCKED>
```

If any phase is BLOCKED: state the blocker + next action. If all DONE: link the screenshot.

---

## Reference library

Everything heavy ships in this folder — no external skills required:

- **[references/context-anchors.md](references/context-anchors.md)** — §A named anchors + tokens + per-context slop tells (e-commerce, fintech, healthcare, editorial, mobile, b2b dashboards, auth, AI-chat, command palette) · §B 8 art-direction directions · §C 2026 token defaults · §D extended slop catalog · §E type-by-role · §F interaction & experience patterns (+ the experience anti-pattern catalog and latency thresholds) · §G microcopy by interaction type. **Open §A first for any non-dev-tool brief; §F/§G back Gate 5 and the experience audit.**
- **[evals/evals.json](evals/evals.json)** — 19 evals across all 5 registers + the regression guards (design-system-present, DESIGN.md-exists, non-dev-tool anchor per context, accessibility, mobile thumb-zone, data-viz restraint, register disambiguation, copy-compiles) and the experience guards (feedback/loading honesty, specific microcopy, keyboard + visible focus, recoverable destructive actions), in the canonical `assertions`-as-strings eval format (`evals/files/` holds the fixtures). Use them to verify changes to this skill don't regress.
