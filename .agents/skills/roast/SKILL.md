---
name: roast
description: Adversarial 5-persona roast council engine tailored for Atinek Maurya. Pressure-tests business ideas, feature designs, web app architectures, marketing copy, or technical plans from every angle before writing code. Delivers a GO / RESHAPE / KILL verdict with a 48-hour validation test. Invokable via /roast or naturally when validating ideas.
argument-hint: '[idea_or_plan_to_roast] [optional focus]'
---

# ZORIXEL AIOS Adversarial Roast Council (`/roast`)

## ⚡ Overview & Tri-Mode Execution

This skill is the non-negotiable validation gate across all AIOS workflows. It convenes a 5-persona council to tear an idea, architecture, design mockup, or marketing plan apart before Atinek Maurya invests time or capital into building it.

Invokable via:
- **Slash Command**: `/roast [idea_or_plan]`
- **Dynamic Intent**: Triggered automatically before writing major specs, deploying web apps, launching marketing carousels, or finalizing repository ingestions.
- **Programmatic Inter-Skill Calling**: Programmatically invoked by `/grill-me`, `/website-design-engine`, `/new-project`, `/design-direction`, `/ingest-repo`, `/carousel-copy`, `/jsmastery-architect`, and `/mattpocock-to-spec`.

---

## 🎯 When & Why to Use `/roast`

| Workflow / Area | Specific Use Case | Key Output |
|---|---|---|
| **AI SaaS / Product Launch** | Validate business model, customer willingness-to-pay, time-to-first-dollar (target: ₹1,00,000 revenue) | GO / RESHAPE / KILL + 48-hr validation test |
| **Web App Architecture** | Pressure-test DB schema, auth boundaries, server action security, and performance risks | Hardened technical spec + risk mitigation |
| **Zorixel Content & Carousels** | Roast hook headlines, slide copy, visual contrast, and audience resonance | High-converting slide copy + scroll-stopping hooks |
| **Repository Ingestion** | Red-team external code security, license compliance, bloat, and token leaks | Ingestion verdict (GO / RESHAPE / KILL) |

---

## 👥 The 5-Persona Council & Prompts

Run all five council members in parallel (using `subagent_type: general-purpose` or internal parallel evaluation):

### 1. The Contrarian (Red Team)
> **Role**: Finds fatal flaws, security vulnerabilities, workspace bloat, token leaks, and load-bearing assumptions that are wrong.
> **Prompt**: *"Assume this idea/architecture fails catastrophically. Be ruthless and specific. What is the fastest way it dies? What load-bearing assumption is false?"*

### 2. The Expansionist (Bull)
> **Role**: Uncovers 10x upside, adjacent monetization opportunities, viral hooks, and unmentioned leverage for ZORIXEL.
> **Prompt**: *"Make the strongest case FOR this idea. What is the 10x version? Where is the hidden revenue or audience leverage that the founder is missing?"*

### 3. The Logician (First Principles)
> **Role**: Reasons strictly from first principles without hype. Evaluates core mechanisms, state transitions, math, and logical integrity.
> **Prompt**: *"Strip away all hype. Does the core mechanism hold together mathematically and logically? Do the incentives and system states align cleanly?"*

### 4. The Researcher (Evidence)
> **Role**: Web search researcher fetching real-world benchmarks, competitor pricing, tech stack performance, and community consensus.
> **Prompt**: *"Use web search. Bring hard market data, competitor pricing, performance benchmarks, and real-world consensus. Is the market saying yes or no?"*

### 5. The Buyer (Voice of Customer / User)
> **Role**: Role-plays as Atinek Maurya's target customer (UI designer, freelancer, vibe coder, or agency owner).
> **Prompt**: *"Role-play as the exact target customer. Would you actually pay for this? What is your immediate objection? What price makes you buy today?"*

---

## ⚖️ Output Verdict Format (The Judge)

```markdown
## THE VERDICT: GO / RESHAPE / KILL
Confidence: [Low / Medium / High] · Operator: Atinek Maurya

**The Call in One Line:** [Decisive verdict statement]

**Why:** [2-3 sentences resolving the council's tension]

**Biggest Risk:** [The single fatal flaw identified by the Contrarian]
**Biggest Upside:** [The strongest leverage point identified by the Expansionist]

**Money & Velocity Read:** [Price point, time-to-first-dollar, ship timeline vs ₹1,00,000 target]

**The Cheapest 48-Hour Test:** [Smallest, fastest test to validate riskiest assumption BEFORE building]

**If RESHAPE:** [Specific pivot that fixes the fatal flaw while preserving upside]

---
**Council Scores:** Contrarian X/10 · Expansionist X/10 · Logician X/10 · Researcher X/10 · Buyer X/10
```

---

## 🔗 Inter-Skill Connections & Handoff Pipeline
- **Adversarial Gate**: Gate 2 validation embedded in **/grill-me**, **/website-design-engine**, **/new-project**, **/ingest-repo**, **/carousel-copy**, and **/jsmastery-architect**.

---

## 🔄 Post-Execution Auto-Evolution & Adversarial `/roast` Gate

At the completion of every execution of this skill:

1. **Adversarial `/roast` Council Review**: Convene the 5-Persona ZORIXEL AIOS Roast Council (`/roast`) to stress-test the output, code edits, or strategy generated by this skill. Red-team for missing edge cases, terminal shell bugs, token leaks, or optimization gaps.
2. **Autonomous Tool, Script & Skill Auto-Upgrade Loop**:
   - If new error patterns or execution safeguards are discovered, append them to `references/GLOBAL_ERROR_PREVENTION_RULES.md` and execute `python scripts/sync_global_rules.py` via `run_command` so system prompts (`AGENTS.md` and `GEMINI.md`) auto-update inline.
   - Run pre-flight health checks (`aios_gws_health_check.py`, `test_notion_formula.py`, `graphify_runner.py`).
   - Self-upgrade this `SKILL.md` instruction file with newly learned edge cases using `replace_file_content` or `write_to_file`.
3. **Register & Log**: Log milestone upgrades in [WORKSPACE_MAP.md](file:///d:/AI-OS/WORKSPACE_MAP.md) and [decisions/log.md](file:///d:/AI-OS/decisions/log.md).

