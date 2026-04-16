# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repo is

This repo **is** a Claude Code Skill (AgentSkills standard). The repo root **is** the skill directory — it gets cloned directly into `.claude/skills/side-hustle/` or `~/.claude/skills/side-hustle/`. There is no application code, no build step, and no test suite; every asset is Markdown consumed at runtime by the Claude agent.

Because of this, "editing the code" means editing prompts. Changes to `SKILL.md`, files under `prompts/`, or `knowledge/categories.md` directly alter runtime behavior — they are the program.

## Architecture

`SKILL.md` is the single entry point. Its YAML frontmatter (`name`, `description`, `allowed-tools`, `user-invocable: true`) is what the Claude Code harness loads when the user types `/side-hustle` or a trigger phrase. Everything else is referenced from there.

Runtime flow is a four-step pipeline, each step delegating to a prompt file:

1. **Intake** → `prompts/intake.md` — 5-question user profile (job, skills, time, budget, exclusions)
2. **Discovery** → `prompts/discovery.md` — map skills to categories (using `knowledge/categories.md`), filter by constraints, validate via `WebSearch`/`WebFetch`
3. **Scoring** → `prompts/scorer.md` — 6-dimension rubric (skill fit, time fit, cost, ceiling, cold-start difficulty, sustainability), 1–5 per dimension, 30 max
4. **Kickstart** → `prompts/kickstart.md` — week-by-week cold-start checklist for a chosen direction

`SKILL.md` references prompt files as `${CLAUDE_SKILL_DIR}/prompts/*.md` — keep that convention when adding new prompt references, since paths resolve relative to the installed skill directory, not the user's CWD.

There are four alternate entry flows besides the main `/side-hustle`: `/side-hustle-quick` (one-question shortcut), `/side-hustle-score {方向}` (single-direction deep scoring), `/side-hustle-kickstart {方向}` (skip to step 4), `/side-hustle-history` (`ls ./results/`). Each short-circuits part of the pipeline — when modifying pipeline semantics, check all five entry points.

## Output contract

Results are written to `./results/{date}_{slug}/` (relative to the skill directory) as `profile.md`, `recommendations.md`, and `kickstart_{direction}.md`. The `results/` directory is gitignored — it holds per-user output, not source. Do not commit anything under `results/`.

## Bilingual behavior

The skill detects the user's language from their first message and must respond in that same language for the entire session. When editing prompts, preserve both-language examples where present (the scoring rubric, intake questions, and kickstart templates all assume the runtime agent will translate on the fly rather than branching on language).

## Commands

There is nothing to build, lint, or test. Verification is manual: install the skill (see `INSTALL.md`), restart the Claude Code session, and run `/side-hustle-quick` — if it produces a recommendation, the skill loads correctly.

## Editing guardrails (from `SKILL.md` "重要原则")

When changing prompts, preserve these invariants — they are the product's thesis:

- **No hype** — do not introduce language that promises unrealistic income ("月入十万", "躺赚"). The discovery prompt explicitly down-weights such sources.
- **Hard constraints are hard** — time budget, money budget, and user exclusions must filter out directions, not just warn about them.
- **Concrete over generic** — recommendations must name a platform and format (e.g., "在小红书发 Figma 教程图文"), never a category ("做自媒体").
- **No upsell** — the skill must not recommend paid courses or paid communities; it positions itself as a replacement for them.
