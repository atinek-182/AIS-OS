---
title: Storm Research Project (`/storm-research-project`)
domain: skill
summary: 'This skill supports Tri-Mode Flexible Execution: - Slash Command: Explicitly run `/storm-research-project [topic]
  [--domain general|tech|design|content|audit]` in chat.'
critical_directives:
- If new error patterns or execution safeguards are discovered, append them to `references/GLOBAL_ERROR_PREVENTION_RULES.m
section_outline:
- Storm Research Project (`/storm-research-project`)
- Invocation & Tri-Mode Routing
- What this does
- Domain Persona Presets (7-Lens Expanded Suite)
- Execution Pipeline
read_triggers:
- When working on skill in .agents/skills/storm-research-project/SKILL.md
- When reading context for Storm Research Project (`/storm-research-project`)
tags:
- skill
- SKILL
updated: '2026-08-08'
name: storm-research-project
description: Run Stanford's STORM multi-perspective research method for project architecture. Spawns 7 expert lenses (Systems
  Architect, Vibesec Security Pen-Tester, DB/Scaling Specialist, Frontend UX Lead, Product/SaaS Economist, AI/LLM Integration
  Specialist, Developer Ergonomics & Token Footprint Auditor) -> contradiction map -> self-contained verified HTML report
  -> persistent brain logging. Invokable directly via /storm-research-project.
argument-hint: '[topic to research] [--domain tech|design|content|audit|general]'
---

# Storm Research Project (`/storm-research-project`)

## Invocation & Tri-Mode Routing

This skill supports Tri-Mode Flexible Execution:
- Slash Command: Explicitly run `/storm-research-project [topic] [--domain general|tech|design|content|audit]` in chat.
- Dynamic Intent Matching: Triggered automatically when task context involves keywords in the description or complex architecture trade-offs.
- Inter-Skill & AIOS Programmatic Calling: Programmatically invokable by parent skills (e.g. `/six-file-context-methodology`, `/website-design-engine`, `/ingest-repo`) via `/storm-research-project` or reading `SKILL.md` directly.

---

## What this does

Turns a complex project topic or architectural decision into a verified, 7-perspective HTML briefing and logs the synthesis directly into AIOS persistent brain memory. It simulates seven expert lenses on the topic, maps where they contradict each other, synthesizes everything into a self-contained HTML report, and logs key insights to `brain-aios/wiki/research/` and `MEMORY.md` to prevent redundant research.

---

## Domain Persona Presets (7-Lens Expanded Suite)

When running `/storm-research-project`, specify `--domain` or use the default 7-lens tech architecture suite:

1. `tech` (7-Lens Project Architecture Suite):
   - Systems Architect: Core modularity, clean boundaries, decoupled contracts.
   - Vibesec Security Pen-Tester: Vulnerability prevention, tenant isolation, IDOR, OWASP LLM top 10.
   - DB & Scaling Specialist: Schema design, indexing, query execution efficiency.
   - Frontend UX & Motion Lead: Core Web Vitals, micro-interactions, responsive accessibility.
   - Product & SaaS Economist: Free-tier limits, business logic, MVP scope discipline.
   - AI / LLM Integration & Latency Specialist: Token costs, RAG latency, context limits, prompt caching, model selection.
   - Developer Ergonomics & Token Footprint Auditor: Maintainability, build-tooling tax, and AI context token optimization.

2. `design` (UI/UX & Web Creation):
   - Visual Artist, UX Usability Architect, WebGL Motion Specialist, Conversion Marketer, Accessibility Auditor, Component Vault Curator, Token Design Auditor.

3. `content` (ZORIXEL Content & Viral Research):
   - Target Audience Practitioner, Growth Strategist, Educational Pedagogue, Industry Skeptic, Monetization Economist, Visual Storyteller, Script Ergonomics Auditor.

4. `audit` (Repo & Codebase Ingestion):
   - Code Quality Auditor, Security Pen-Tester, Maintainability Historian, Developer Ergonomics Practitioner, Performance Economist, Dependency Auditor, Token Footprint Auditor.

---

## Execution Pipeline

### Phase 0: Scope & Reader Identification
1. Extract topic and `--domain` preset.
2. State interpretation in one line and proceed.
3. Identify reader's role (e.g. Senior Architect, Fullstack Engineer).
4. Derive kebab-case `topic-slug` for output filenames (`storm-reports/{topic-slug}-briefing.html`).

### Phase 1: Seven Expert Lenses (Parallel Research Subagents)
Spawn 7 parallel background research agents with surgical context boundaries.
Each agent executes live web research seeking concrete data, benchmarks, primary documentation, and operational metrics.
Token Efficiency Rule: Each subagent is capped at 2 execution steps with strict prompt scope limits to prevent token burn. When fetching long-form tech blogs or documentation, subagents may pipe fetched content through `npx defuddle parse <URL> --markdown --frontmatter` to strip nav/footer clutter and minimize context token usage.

### Phase 2: Map the Contradictions
Analyze briefs inline to extract:
1. Direct Conflicts: Opposite claims between lenses.
2. Evidence Quality Ranking: Ranked by source hierarchy (official docs > peer-reviewed > survey > anecdote).
3. Resolving Question: Single empirical question settling the core conflict.
4. Universal Agreement: What all 7 lenses confirm.
5. Blind Spot Analysis: What was missed across lenses.

### Phase 3: Synthesize HTML Report
1. Read `storm-research-report-template.html` if available or compile clean HTML structure.
2. Populate summary, ranked key findings, hidden connections, actionable steps, and claim safety guide.
3. Save to `storm-reports/{topic-slug}-briefing.html`.

### Phase 4: Adversarial Verification & Memory Logging
1. Verify key claims against primary source documentation.
2. Append core executive summary, decisions, and trade-offs to `brain-aios/wiki/research/{topic-slug}-summary.md`.
3. Update `MEMORY.md` with persistent learnings so future sessions retain this context without re-invoking tools.

---

## Token Efficiency & Zero-Emoji Policy
- Surgical Context: Subagents receive only target topic scope.
- Zero-Emoji Mandate: No emojis used anywhere in markdown, generated HTML reports, or logs.
- Hard Step Cap: Maximum 2 attempts per subagent.

---

## Inter-Skill Connections
- `six-file-context-methodology`: Supplies 7-lens evidence-backed research before writing `context/architecture.md` or feature specs.
- `website-design-engine`: Supplies design council insights and anti-slop benchmarks.
- `agent-reach` / `scrape-web`: Enhances primary-source retrieval.
- `vibesec`: Integrated into security persona for vulnerability verification.

---

## Post-Execution Auto-Evolution & Adversarial `/roast` Gate

At the completion of every execution of this skill:

1. **Adversarial `/roast` Council Review**: Convene the 5-Persona ZORIXEL AIOS Roast Council (`/roast`) to stress-test the output, code edits, or strategy generated by this skill. Red-team for missing edge cases, terminal shell bugs, token leaks, or optimization gaps.
2. **Autonomous Tool, Script & Skill Auto-Upgrade Loop**:
   - If new error patterns or execution safeguards are discovered, append them to `references/GLOBAL_ERROR_PREVENTION_RULES.md` and execute `python scripts/sync_global_rules.py` via `run_command` so system prompts (`AGENTS.md` and `GEMINI.md`) auto-update inline.
   - Run pre-flight health checks (`aios_gws_health_check.py`, `test_notion_formula.py`, `graphify_runner.py`).
   - Self-upgrade this `SKILL.md` instruction file with newly learned edge cases using `replace_file_content` or `write_to_file`.
3. **Register & Log**: Log milestone upgrades in [WORKSPACE_MAP.md](file:///d:/AI-OS/WORKSPACE_MAP.md) and [decisions/log.md](file:///d:/AI-OS/decisions/log.md).

