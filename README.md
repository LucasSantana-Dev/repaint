# repaint

> The anti-slop frontend skill — research, tokens, a reference library, and a live browser feedback loop.

Build production-grade frontend UI that doesn't read as "AI-made" — a **self-contained** skill for agentic coding tools (Claude Code, and any agent that supports [`npx skills`](https://github.com/vercel-labs/skills)).

It depends on **no other skills and no agents**. Everything ships in this repo: the pipeline (`SKILL.md`), a curated reference library (`references/`), and 19 evals (`evals/`).

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

A pipeline that produces UI that looks *designed*, not generated — **and behaves like it** — built on five pillars:

| Pillar | What it means |
|---|---|
| **Scraping** | Research *real, current* references for the brief (your web search), not vibes. |
| **Tokens** | Commit a concrete token system (OKLCH color + distinctive type) before any markup. |
| **References** | A curated library — named anchors per context, 8 art-direction directions, 2026 token defaults, a slop catalog, type-by-role, plus experience patterns and microcopy. |
| **Experience** | Design the *interaction*, not just the pixels: honest feedback + perceived performance, forgiving input, recoverable actions, a real keyboard path. Enforced by Gate 4, Gate 5, and the experience audit. |
| **Real iteration feedback** | Build → render → screenshot → slop-audit + experience-audit → iterate, against live browser output — not a one-shot guess. |

The leverage (eval-verified) is in the five places a capable model gets wrong unaided: cliché on creative briefs, register-appropriate restraint, distinctive typography, compile-clean durable output, and hollow/AI-generated interaction (handlers that do nothing, silent submits, no keyboard path, generic error copy).

## What's in the box

- **`SKILL.md`** — the 5-phase pipeline (research → gates/tokens → scaffold → build → slop-audit + experience-audit + browser-verify loop), with five Phase-1 gates including Gate 4 (component anatomy + interaction affordances) and Gate 5 (experience contract).
- **`references/context-anchors.md`** — named anchors + tokens + per-context slop tells (e-commerce, fintech, healthcare, editorial, mobile, b2b dashboards, auth, AI-chat, command palette); 8 named art-direction directions; 2026 token defaults; an extended slop catalog; type-by-role; **§F interaction & experience patterns** (+ the experience anti-pattern catalog and latency thresholds); **§G microcopy by interaction type**.
- **`evals/evals.json`** — 19 evals across all 5 registers + the regression guards (design-system-present, existing-`DESIGN.md`, non-dev-tool anchor per context, accessibility, mobile thumb-zone, data-viz restraint, register disambiguation, copy-compiles) and the **experience guards** (feedback/loading honesty, specific microcopy, keyboard + visible focus, recoverable destructive actions), in the canonical `assertions`-as-strings format (fixtures in `evals/files/`) runnable by `agent-skills-eval`. Run these to check changes don't regress.

## License

Apache-2.0 (see [LICENSE](LICENSE)). The `references/` library is deliberately open and forkable — extend it.
