---
name: storm-research
description: Run Stanford's STORM multi-perspective research method on a topic. Spawns 5 expert lenses (Practitioner, Academic, Skeptic, Economist, Historian - or domain-customized personas) -> contradiction map -> self-contained verified HTML report -> primary-source verification subagents. Invokable directly via /storm-research.
argument-hint: "[topic to research] [--domain tech|design|content|audit|general]"
---

# ⚡ Storm Research (`/storm-research`)

## ⚡ Invocation & Tri-Mode Routing

This skill supports **Tri-Mode Flexible Execution**:
- **Slash Command**: Explicitly run `/storm-research [topic] [--domain general|tech|design|content|audit]` in chat.
- **Dynamic Intent Matching**: Triggered automatically when someone asks for deep multi-perspective research, a STORM briefing, or fact-checked research report.
- **Inter-Skill & AIOS Programmatic Calling**: Programmatically invokable by parent skills (e.g. `/six-file-context-methodology`, `/website-design-engine`, `/ingest-repo`, `/carousel-copy`) via `/storm-research` or reading `SKILL.md` directly.

---

## 📌 What this does

Turns a topic or architectural decision into a verified, multi-perspective HTML briefing. It simulates five expert lenses on the topic, maps where they contradict each other, synthesizes everything into a single self-contained HTML report, then adversarially peer-reviews its own output and verifies every citation against primary sources before delivering. The output is a self-contained HTML file in `storm-reports/` with zero blind spots and zero unverified claims.

---

## 🎭 Domain Persona Presets

When running `/storm-research`, specify `--domain` or let the AI select the best persona suite:

1. **`general` (Default STORM)**: Practitioner, Academic, Skeptic, Economist, Historian.
2. **`tech` (Architectural & Tech Stack)**: Systems Architect, Vibesec Security Pen-Tester, DB/Scaling Specialist, Frontend UX Lead, Product/SaaS Economist.
3. **`design` (UI/UX & Web Creation)**: UI Visual Artist (Hallmark Anti-Slop), UX Usability Architect, WebGL & Motion Specialist, Conversion Marketer, WCAG 2.2 AAA Accessibility Auditor.
4. **`content` (ZORIXEL Content & Viral Research)**: Target Audience Practitioner (Freelancer/Designer), Viral Growth Strategist, Educational Pedagogue, Industry Skeptic, Product Monetization Economist.
5. **`audit` (Repo & Codebase Ingestion)**: Code Quality Auditor, Security Pen-Tester, Maintainability Historian, Developer Ergonomics Practitioner, Performance Benchmark Economist.

---

## 🛠️ Execution Pipeline

### Phase 0: Scope & Reader Identification
1. Extract topic and `--domain` preset from arguments.
2. State interpretation in one line and proceed.
3. Identify **reader's role** (e.g., Senior Architect, Frontend Engineer, Growth Marketer, SaaS Founder).
4. Derive kebab-case `topic-slug` for output filenames (`storm-reports/{topic-slug}-briefing.html`).

### Phase 1: Five Expert Lenses (Parallel Research Subagents)
Spawn 5 parallel background research agents in a single step using domain-matched expert lenses.
Each agent executes live web research (via Google/Serp/search tools), seeking concrete data, primary papers, numbers, and operator insights.

### Phase 2: Map the Contradictions
Analyze briefs inline to extract:
1. **Direct Conflicts**: Opposite claims between lenses.
2. **Evidence Quality Ranking**: Ranked by source hierarchy (peer-reviewed > official data > survey > anecdote).
3. **Resolving Question**: Single empirical question settling the core conflict.
4. **Universal Agreement**: What all 5 lenses confirm.
5. **Blind Spot / Missing 6th Lens**: What no lens covered.

### Phase 3: Synthesize HTML Report
1. Read `storm-research-report-template.html` in this skill directory.
2. Populate 60-second summary, ranked key findings (1-10 scores, chips), hidden connections, 6th lens, actionable steps, claim safety guide (assert/caveat/avoid), and frontier question.
3. Save to `storm-reports/{topic-slug}-briefing.html`.

### Phase 4: Adversarial Peer Review & Primary-Source Verification
1. Inline self-review: score findings 1-10, identify weakest link, run bias check.
2. Verification subagents: Spawn 4-6 subagents to verify each distinct citation cluster against actual primary sources (confirming paper titles, numbers, peer-review status).
3. Apply corrections to HTML: update scores, demote preprints/unverified claims, fill verification banner (`X fabricated, Y corrected, Z demoted`).

### Phase 5: AIOS Action Asset Extraction (Optional / Inter-Skill Handoff)
- For `six-file-context-methodology`: Append findings to `context/architecture.md` or feature spec.
- For `website-design-engine`: Inject design tokens & constraints into `design-direction.md`.
- For `second-brain-zorixel`: Save Markdown summary to `second-brain-zorixel/wiki/research/`.

---

## 🔗 Inter-Skill Connections
- **`six-file-context-methodology`**: Supplies evidence-backed architecture research before generating feature specs.
- **`website-design-engine`**: Supplies design council insights and anti-slop benchmarks.
- **`agent-reach` / `scrape-web`**: Enhances Phase 1 & Phase 4 primary-source retrieval.
- **`vibesec`**: Integrated into tech & audit persona suites for security verification.

---

## 🔄 Post-Execution Auto-Evolution & Adversarial `/roast` Gate

At the completion of every execution of this skill:

1. **Adversarial `/roast` Council Review**: Convene the 5-Persona ZORIXEL AIOS Roast Council (`/roast`) to stress-test the output, code edits, or strategy generated by this skill. Red-team for missing edge cases, terminal shell bugs, token leaks, or optimization gaps.
2. **Autonomous Tool, Script & Skill Auto-Upgrade Loop**:
   - If new error patterns or execution safeguards are discovered, append them to `references/GLOBAL_ERROR_PREVENTION_RULES.md` and execute `python scripts/sync_global_rules.py` via `run_command` so system prompts (`AGENTS.md` and `GEMINI.md`) auto-update inline.
   - Run pre-flight health checks (`aios_gws_health_check.py`, `test_notion_formula.py`, `graphify_runner.py`).
   - Self-upgrade this `SKILL.md` instruction file with newly learned edge cases using `replace_file_content` or `write_to_file`.
3. **Register & Log**: Log milestone upgrades in [WORKSPACE_MAP.md](file:///d:/AI-OS/WORKSPACE_MAP.md) and [decisions/log.md](file:///d:/AI-OS/decisions/log.md).

