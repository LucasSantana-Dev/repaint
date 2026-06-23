# repaint

> The anti-slop frontend skill — research, tokens, a reference library, and a live browser feedback loop.

Build production-grade frontend UI that doesn't read as "AI-made" — a **self-contained** skill for agentic coding tools (Claude Code, and any agent that supports [`npx skills`](https://github.com/vercel-labs/skills)).

It depends on **no other skills and no agents**. Everything ships in this repo: the pipeline (`SKILL.md`), a curated reference library (`references/`), and 9 evals (`evals/`).

## Install

```bash
npx skills add LucasSantana-Dev/repaint
```

That copies `SKILL.md` + `references/` + `evals/` into your agent's skills directory (`.claude/skills/` or `.agents/skills/`). Then just ask your agent to build, redesign, or "make X look less AI-made" — the skill auto-applies. Update later with `npx skills update`.

Or clone manually:

```bash
git clone https://github.com/LucasSantana-Dev/repaint ~/.claude/skills/repaint
```

## What it does

A pipeline that produces UI that looks *designed*, not generated, built on four pillars:

| Pillar | What it means |
|---|---|
| **Scraping** | Research *real, current* references for the brief (your web search), not vibes. |
| **Tokens** | Commit a concrete token system (OKLCH color + distinctive type) before any markup. |
| **References** | A curated library — named anchors per context, 8 art-direction directions, 2026 token defaults, a slop catalog, type-by-role. |
| **Real iteration feedback** | Build → render → screenshot → slop-audit → iterate, against live browser output — not a one-shot guess. |

The leverage (eval-verified) is in the four places a capable model gets wrong unaided: cliché on creative briefs, register-appropriate restraint, distinctive typography, and compile-clean durable output.

## What's in the box

- **`SKILL.md`** — the 5-phase pipeline (research → gates/tokens → scaffold → build → audit + browser-verify loop).
- **`references/context-anchors.md`** — named anchors + tokens + per-context slop tells (e-commerce, fintech, healthcare, editorial, mobile, b2b dashboards, auth); 8 named art-direction directions; 2026 token defaults; an extended slop catalog; type-by-role.
- **`evals/evals.json`** — 9 evals across all 5 registers + the regression guards (design-system-present, existing-`DESIGN.md`, non-dev-tool anchor, copy-compiles). Run these to check changes don't regress.

## License

Apache-2.0 (see [LICENSE](LICENSE)). The `references/` library is deliberately open and forkable — extend it.
