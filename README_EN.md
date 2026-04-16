<div align="center">

# side-hustle.skill

> *"Stop paying for side-hustle courses. Let AI find the one that actually fits you."*

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-Skill-blueviolet)](https://claude.ai/code)
[![AgentSkills](https://img.shields.io/badge/AgentSkills-Standard-green)](https://agentskills.io)

<br>

Want to start a side hustle but don't know where to begin?<br>
Spent hundreds on courses only to realize the topic doesn't fit you?<br>
Drowning in "$10k/month passive income" posts and getting more anxious by the day?<br>

**Stop guessing. Let AI analyze your profile and surface the directions that actually fit.**

<br>

Feed in your skills, time, budget, and interests.<br>
AI Agents search the web in parallel, cross-evaluate, and quantify each direction.<br>
You get a **personalized side-hustle report** — not another generic "start a YouTube channel."

[Quick Start](#install) · [Usage](#usage) · [Example Output](#example-output) · [Scoring System](#scoring-system) · [Full Install Guide](INSTALL.md) · [**中文**](README.md)

</div>

---

## What it does

| Step | Description |
|------|-------------|
| **1. Know you** | A short structured conversation builds your profile (skills, time, budget, interests, constraints) |
| **2. Find options** | AI Agents search and analyze side-hustle directions that match your profile in parallel |
| **3. Rank them** | Each option scored on 6 dimensions (30 pts total), with per-direction pros/cons |
| **4. Get started** | For the direction you pick, generate a concrete kickstart checklist |

---

## Install

### Claude Code

```bash
# Install into the current project (run from your git repo root)
mkdir -p .claude/skills
git clone https://github.com/xz1220/side-hustle-skill .claude/skills/side-hustle

# Or install globally (available in every project)
git clone https://github.com/xz1220/side-hustle-skill ~/.claude/skills/side-hustle
```

### OpenClaw

```bash
git clone https://github.com/xz1220/side-hustle-skill ~/.openclaw/workspace/skills/side-hustle
```

Restart your session and type `/side-hustle` to start.

> Detailed install notes: [INSTALL.md](INSTALL.md)

---

## Usage

In Claude Code, type:

```
/side-hustle
```

Answer a few questions and the AI takes it from there.

### Commands

| Command | Description |
|---------|-------------|
| `/side-hustle` | Full flow: profile → search → score → recommend |
| `/side-hustle-quick` | Quick mode: skip deep profiling, recommend based on a one-sentence description |
| `/side-hustle-score {direction}` | Deep scoring analysis for a single direction |
| `/side-hustle-kickstart {direction}` | Generate a kickstart checklist for a specific direction |
| `/side-hustle-history` | Browse past recommendations |

---

## Example Output

> 👉 Real end-to-end run: [`examples/ui_designer_figma/`](examples/ui_designer_figma/) (UI designer / 10h weekend / $0, top pick scored 26/30).<br>
> 👉 Want one for your situation? [Open a "Run it for me" issue](https://github.com/xz1220/side-hustle-skill/issues/new?template=run_it_for_me.yml) and we'll run it for you.

### Profile stage

```
AI   > Let's start with a few quick questions:
     >
     > 1. What do you do for work? (role / industry)
     > 2. What are you good at? Work skills, life skills, hobbies all count
     > 3. How many hours per week can you spend on this?
     > 4. Any starting budget? (0 is totally fine)
     > 5. Anything you absolutely don't want to do?

User > I'm a UI designer, strong in Figma and illustration
     > Weekends, around 10 hours
     > No budget, $0 start
     > No on-camera work — I'm introverted
```

### Recommendation stage

```
AI   > Based on your profile, I found 8 directions. Ranked:
     >
     > ## #1 Figma Templates / UI Kits  25/30
     > Why it fits: Direct monetization of existing skill, no camera, zero startup cost
     > First step: Publish 3 free templates on Gumroad + Xiaohongshu to build funnel
     >
     > ## #2 Illustration Commissions (Xiaohongshu / Fiverr)  23/30
     > Why it fits: Skill maps directly, introvert-friendly (text-based comms)
     > First step: Post 3 style samples on Fiverr, price $8-30
     >
     > ## #3 Design-focused content (Xiaohongshu visual posts)  21/30
     > Why it fits: No camera needed, visual format suits you
     > Risk: Audience-building takes 3+ months with possibly zero income early
     >
     > ...
     >
     > Want a deep dive on any of these? I can draft a kickstart plan.
```

---

## Scoring System

Each direction is scored across 6 dimensions, 30 points total:

| Dimension | 1 point | 5 points |
|-----------|---------|----------|
| **Skill Match** | Start from scratch | Use existing skills directly |
| **Time Fit** | Needs full-time | Works with scattered spare time |
| **Startup Cost** | Large upfront investment | Zero cost to start |
| **Income Ceiling** | Capped at a few hundred / month | Scales to 5-figure / month |
| **Cold Start** | Needs long buildup | First sale within a week |
| **Sustainability** | One-off income | Compounds over time |

**Thresholds:**
- 25-30: Strong match — start now
- 20-24: Worth trying — mind the risk notes
- 15-19: Potential, but high barrier
- <15: Not recommended — poor fit

---

## Project Structure

```
side-hustle-skill/
├── SKILL.md              # Skill entry (AgentSkills standard frontmatter)
├── prompts/              # Prompt templates
│   ├── intake.md         #   Profile intake questions
│   ├── discovery.md      #   Search & analysis methodology
│   ├── scorer.md         #   6-dimension scoring rubric
│   └── kickstart.md      #   Kickstart checklist generation
├── knowledge/            # Knowledge base
│   └── categories.md     #   Side-hustle category library
├── examples/             # Public real runs (linked from README)
├── results/              # Your recommendation archive (gitignored)
├── INSTALL.md            # Detailed install notes
├── README.md             # 中文文档
└── LICENSE
```

---

## Privacy

- All conversation and analysis happens locally
- No personal data collected, nothing uploaded
- Recommendations are stored only in your local `results/` directory
- Delete your data any time

---

## FAQ

**Q: How is this different from just asking ChatGPT "what side hustle should I do"?**

A: ChatGPT gives generic advice. side-hustle.skill builds a structured profile of you, then runs quantitative scoring across multiple directions — systematic analysis, not off-the-cuff suggestions.

**Q: Does it cost anything?**

A: No. Open source, free. You just need Claude Code or OpenClaw access.

**Q: Does it support Chinese?**

A: Yes. The skill auto-switches language based on your first message.

---

## License

[MIT](LICENSE)
