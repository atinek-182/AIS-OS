---
title: ZORIXEL AIOS Universal Adversarial Roast Council (`/roast`)
domain: skill
summary: 'This skill is the non-negotiable validation gate across all AIOS workflows. It convenes an adversarial multi-agent
  red-teaming council to stress-test any proposal, architecture, design mockup, pricing model, marketing campaign, or AI workflow
  before '
critical_directives:
- Follow document guidance without bypassing established safeguards.
section_outline:
- ZORIXEL AIOS Universal Adversarial Roast Council (`/roast`)
- Overview & Tri-Mode Execution
- Flags & Execution Parameters
- Universal Domain Adapters
- Smart Trigger Recommendations
read_triggers:
- When working on skill in .agents/skills/roast/SKILL.md
- When reading context for ZORIXEL AIOS Universal Adversarial Roast Council (`/roast`)
tags:
- skill
- SKILL
updated: '2026-08-08'
name: roast
description: Adversarial multi-agent red-teaming engine tailored for Atinek Maurya. Universal, domain-agnostic, zero-emoji,
  persistent red-teaming council that pressure-tests business ideas, feature designs, web app architectures, marketing copy,
  AI workflows, or technical plans from every angle before writing code. Supports domain adapters, baseline 5-persona council
  + 6th/7th specialized personas, multi-turn attack & patch loops (--deep), risk matrix scoring, and disk artifact persistence
  (--save). Invokable via /roast or naturally when validating ideas.
argument-hint: '[idea_or_plan_to_roast] [--domain code|offer|copy|workflow|strategy] [--deep] [--save]'
---

# ZORIXEL AIOS Universal Adversarial Roast Council (`/roast`)

## Overview & Tri-Mode Execution

This skill is the non-negotiable validation gate across all AIOS workflows. It convenes an adversarial multi-agent red-teaming council to stress-test any proposal, architecture, design mockup, pricing model, marketing campaign, or AI workflow before Atinek Maurya invests time or capital into building it.

Invokable via:
- **Slash Command**: `/roast [idea_or_plan] [--domain type] [--deep] [--save]`
- **Dynamic Intent**: Triggered automatically before writing major specs, deploying web apps, launching marketing carousels, or finalizing repository ingestions.
- **Programmatic Inter-Skill Calling**: Programmatically invoked by `/grill-me`, `/website-design-engine`, `/new-project`, `/design-direction`, `/ingest-repo`, `/carousel-copy`, `/jsmastery-architect`, and `/mattpocock-to-spec`.

---

## Flags & Execution Parameters

| Flag | Name | Purpose & Function |
|---|---|---|
| `--domain [type]` | Domain Adapter | Explicitly forces specialized evaluation criteria (`code`, `offer`, `copy`, `workflow`, `strategy`). If omitted, auto-detects from context. |
| `--deep` | Multi-Turn Attack & Patch Loop | Triggers a 2-turn adversarial loop where Contrarian attacks, Logician patches, and Contrarian re-tests. Saves artifact automatically. |
| `--save` | Disk Persistence | Writes full structured roast report and refinement spec to `brainstorms/roast_{date}_{slug}.md`. |

---

## Universal Domain Adapters

When roasting a target, the domain adapter dynamically injects specialized red-teaming criteria into persona evaluations:

1. **Code & Architecture (`--domain code`)**: Focuses on security boundaries (`/vibesec`), IDOR/SSRF, state machine transitions, performance bottlenecks, and dependency bloat.
2. **Business & Pricing Offer (`--domain offer`)**: Focuses on Nate Herk 3-Number Corridor, Client SaaS Zero-Fee Mandate (GAS + Notion), willingness-to-pay, time-to-first-dollar, and payback velocity.
3. **Marketing & Copy (`--domain copy`)**: Focuses on scroll-stopping hooks, visual contrast, audience resonance, CTA conversion friction, and anti-slop guidelines.
4. **AI & LLM Workflow (`--domain workflow`)**: Focuses on goal hijacking, tool misuse, context limits, prompt injection, fallback recovery, and token cost economics.
5. **General Strategy (`--domain strategy`)**: Focuses on core mechanics, first principles, competitive moats, and operational leverage.

---

## Smart Trigger Recommendations

Before running a single-pass roast, inspect the input target. If any of the following high-impact triggers are detected, output a recommendation banner:

`[RECOMMENDED: Re-run with --deep for multi-turn attack & patch loop]`

- **Security & Auth Boundaries**: Database schemas, JWT auth, permission models, API secret handling.
- **Core Revenue & Pricing**: Client proposals, pricing tiers, business pitches, financial models.
- **Multi-Module Architecture**: Structural system refactors spanning 3+ core modules.

---

## The Council Personas

### Baseline Council (Always Active)

#### 1. The Contrarian (Red Team)
> **Role**: Finds fatal flaws, security vulnerabilities, workspace bloat, token leaks, and load-bearing assumptions that are wrong.
> **Prompt**: *"Assume this idea/architecture fails catastrophically. Be ruthless and specific. What is the fastest way it dies? What load-bearing assumption is false?"*

#### 2. The Expansionist (Bull)
> **Role**: Uncovers 10x upside, adjacent monetization opportunities, viral hooks, and unmentioned leverage for ZORIXEL.
> **Prompt**: *"Make the strongest case FOR this idea. What is the 10x version? Where is the hidden revenue or audience leverage that the founder is missing?"*

#### 3. The Logician (First Principles)
> **Role**: Reasons strictly from first principles without hype. Evaluates core mechanisms, state transitions, math, and logical integrity.
> **Prompt**: *"Strip away all hype. Does the core mechanism hold together mathematically and logically? Do the incentives and system states align cleanly?"*

#### 4. The Researcher (Evidence)
> **Role**: Web search researcher fetching real-world benchmarks, competitor pricing, tech stack performance, and community consensus.
> **Prompt**: *"Use web search. Bring hard market data, competitor pricing, performance benchmarks, and real-world consensus. Is the market saying yes or no?"*

#### 5. The Buyer (Voice of Customer / Target User)
> **Role**: Role-plays as Atinek Maurya's target customer (UI designer, freelancer, vibe coder, SMB owner, or agency lead).
> **Prompt**: *"Role-play as the exact target customer. Would you actually pay for this? What is your immediate objection? What price makes you buy today?"*

### Extended Personas (Summoned in `--deep` or Specialized Domains)

#### 6. The Security Auditor (Code / Architecture / Workflow)
> **Role**: Deep `/vibesec` pen-testing, tenant isolation, SSRF, injection, and data boundary audit.

#### 7. The Product Economist (SaaS / Pricing Offer)
> **Role**: API token cost modeling, margin analysis, payback velocity, and zero-SaaS fee compliance.

#### 8. The UX & Friction Specialist (Web App UI / Workflow)
> **Role**: Cognitive load reduction, visual hierarchy, mobile responsiveness, and zero-slop UI standards.

---

## 4-Axis Quantitative Risk Matrix

Every roast calculates four numerical scores (1-10 scale):
1. **Security & Failure Risk (1-10)**: 1 = bulletproof, 10 = catastrophic vulnerability/failure.
2. **Implementation Friction (1-10)**: 1 = trivial build, 10 = multi-week bottleneck.
3. **Value & ROI (1-10)**: 1 = worthless, 10 = massive ROI / high willingness-to-pay.
4. **System Simplicity (1-10)**: 1 = bloated over-engineering, 10 = elegant first-principles design.

### Verdict Decision Logic
- **KILL**: If Security/Failure Risk >= 8 OR Value & ROI <= 3.
- **RESHAPE**: If Security/Failure Risk >= 5 OR Value & ROI <= 6 OR Implementation Friction >= 8.
- **GO**: If Security/Failure Risk <= 3 AND Value & ROI >= 7 AND System Simplicity >= 6.

---

## Output Verdict Format (The Judge)

```markdown
## THE VERDICT: GO / RESHAPE / KILL
Confidence: [Low / Medium / High] · Operator: Atinek Maurya · Domain: [code|offer|copy|workflow|strategy]

**The Call in One Line:** [Decisive verdict statement]

**Why:** [2-3 sentences resolving the council's tension]

**Biggest Risk:** [The single fatal flaw identified by the Contrarian]
**Biggest Upside:** [The strongest leverage point identified by the Expansionist]

**Money & Velocity Read:** [Price point, time-to-first-dollar, ship timeline vs target]

**4-Axis Risk Matrix:**
- Security / Failure Risk: X/10
- Implementation Friction: X/10
- Value & ROI: X/10
- System Simplicity: X/10

**Council Scores:** Contrarian X/10 · Expansionist X/10 · Logician X/10 · Researcher X/10 · Buyer X/10 [· Extended Persona X/10]

**The Cheapest 48-Hour Test:** [Smallest, fastest test to validate riskiest assumption BEFORE building]

**ROAST_REFINEMENT_SPEC (Required if RESHAPE):**
- [ ] Fix 1: [Actionable fix for fatal flaw]
- [ ] Fix 2: [Actionable fix for risk boundary]
- [ ] Fix 3: [Actionable optimization for ROI/simplicity]
```

---

## Inter-Skill Connections & Handoff Pipeline
- **Adversarial Gate**: Gate 2 validation embedded in `/grill-me`, `/website-design-engine`, `/new-project`, `/ingest-repo`, `/carousel-copy`, `/jsmastery-architect`, and `/gstack`.
- **Refinement Spec Handoff**: When verdict is `RESHAPE`, the generated `ROAST_REFINEMENT_SPEC` feeds directly into `/make-plan` or `/website-design-engine` for wave execution.

---

## Post-Execution Auto-Evolution & Skill Maintenance

At the completion of every execution of this skill:
1. **Artifact Persistence**: If `--save` or `--deep` flag is active, write complete report to `brainstorms/roast_{date}_{slug}.md`.
2. **Auto-Upgrade Rule Registry**: If new security vulnerabilities or failure patterns are uncovered, log them into `references/GLOBAL_ERROR_PREVENTION_RULES.md` and run `python scripts/sync_global_rules.py`.
3. **Workspace Mapping**: Log major architectural roast outcomes in `WORKSPACE_MAP.md` and `decisions/log.md`.
