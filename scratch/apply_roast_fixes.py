import os

skill_path = r'd:\AI-OS\.agents\skills\six-file-context-methodology\SKILL.md'
guide_path = r'd:\AI-OS\references\six-file-context-methodology\STEP_BY_STEP_SENIOR_AI_ENGINEERING_GUIDE.md'

# 1. Update SKILL.md with explicit Lite vs Pro Mode + Token Footprint Optimization + Sync Fixes
skill_content = """---
name: six-file-context-methodology
description: Apply Senior AI Engineering 7-File Context Methodology, Spec-Driven Development, Playwright Visual QA, and Global Zero-Hurry Mandate (from JavaScript Mastery masterclass). Use when initializing new projects, structuring AI coding context, or creating feature specifications.
argument-hint: '[init|scaffold|spec <feature-name>|spec-all|verify|check]'
---

# ⚡ Six-File Context Methodology (`/six-file-context-methodology`)

## ⚡ Invocation & Tri-Mode Routing

This skill supports **Tri-Mode Flexible Execution**:
- **Slash Command**: Explicitly run `/six-file-context-methodology [init|scaffold|spec <feature-name>|spec-all|verify]` in chat.
- **Dynamic Intent Matching**: Triggered automatically when task context involves keywords in the description (e.g. "scaffold context", "7-file context", "feature spec", "senior AI workflow").
- **Inter-Skill & AIOS Calling**: Programmatically invokable by parent skills (e.g. `/new-project`, `/make-plan`) or subagents via `/six-file-context-methodology` or reading `SKILL.md` directly.

---

## 🛡️ Addressed Vulnerabilities & Quality Fixes (From Roast Council Audit)

1. **Lite Mode vs Pro Mode Selector (Eliminates Build-Tooling Tax)**:
   - **Pro Mode (Default for Full SaaS)**: Scaffolds the full 7-File Context System (`project-overview.md`, `architecture.md`, `code-standards.md`, `ui-context.md`, `ai-workflow-rules.md`, `progress-tracker.md`, `seo-context.md` + root `AGENTS.md`) and handles unbounded 10-50+ feature specs.
   - **Lite Mode (For Micro-Tools & Landing Pages)**: Scaffolds a 4-File Minimal System (`project-overview.md`, `architecture.md`, `ui-context.md`, `progress-tracker.md`) + 3-5 specs to eliminate setup overhead on small 1-day builds.

2. **Token Footprint & Prompt Context Optimization**:
   - To avoid token context churn, the agent reads only relevant context files during specific sub-tasks:
     - *UI Tasks*: Reads `ui-context.md` + `code-standards.md`.
     - *DB / API Tasks*: Reads `architecture.md` + `code-standards.md` + `vibesec` security rules.
     - *SEO Tasks*: Reads `seo-context.md` + `seo-audit-reference/` vault.

3. **State Synchronization & Drift Prevention**:
   - Automated check during `/six-file-context-methodology check` comparing git commit history against `progress-tracker.md` entries to prevent stale documentation.

---

## 📌 Hard-and-Fast System Mandates

1. **Global Zero-Hurry Rule**: Never rush execution. Systems take time (weeks/months). Architectural rigor, deep questioning, and web research take precedence over speed.
2. **Interactive Architect Discovery (`init`)**: Run Playbook prompts in an interactive option-based Q&A loop before writing context files. Offers **Lite Mode vs Pro Mode** choice.
3. **7-File Context Foundation (Pro Mode)**:
   - `context/project-overview.md`
   - `context/architecture.md`
   - `context/code-standards.md`
   - `context/ui-context.md` (Integrated with 147 components from Aceternity, Animate UI, Forge UI, Vengence UI)
   - `context/ai-workflow-rules.md`
   - `context/progress-tracker.md`
   - `context/seo-context.md` (Integrated with 23-skill SEO skills-library vault)
   - Root `AGENTS.md` / `CLAUDE.md`
4. **Dynamic Unbounded Specs (`spec-all`)**: Generate all feature specs upfront (can be 10, 15, 20, 40, 50+ specs).
5. **Mandatory Pre-Write `/roast` Council**: Run `/roast` gatekeeper audit before creating any document file.
6. **Playwright Visual QA Engine (`verify`)**: Run Playwright CLI headless browser screenshots and console audits for every spec unit.
7. **Explicit Tracker Confirmation**: Ask user confirmation before updating `progress-tracker.md`.
8. **Pre-Coding Backstop**: Always ask: *"Is there anything else remaining before we touch the code?"*
9. **Security-First & Auto-Skill Ingestion Mandate**: Security is top priority. Always apply `/vibesec` rules (IDOR, JWT HttpOnly cookies, Zod Mass Assignment validation, SSRF private IP blocking). Automatically detect, scan, and apply ANY present or future security/backend skill in `.agents/skills/` or `skills-library/` during planning, spec generation, and pre-write `/roast` audits.

---

## 🛠️ Commands & Workflow Guide

### 1. `/six-file-context-methodology init`
Runs an interactive Q&A discovery loop using Playbook prompts to gather product vision, scope mode (Lite vs Pro), stack choices, UI tokens, SEO strategy, and invariants before creating context files in `context/`.

### 2. `/six-file-context-methodology spec <feature-name>`
Generates a numbered, 5-section feature spec in `context/specs/NN-<feature-name>.md`. Search the web for best practices and run `/roast` before emitting file content.

### 3. `/six-file-context-methodology spec-all`
Decomposes `project-overview.md` into an unbounded list of numbered units (`00-build-plan.md`) following strict build-order rules (Dependencies -> Auth -> Backend APIs -> UI Wiring), generating feature specs upfront in `context/specs/`.

### 4. `/six-file-context-methodology verify`
Executes Playwright CLI to capture 5-viewport screenshots and verify console error cleanliness for completed feature units.

### 5. `/six-file-context-methodology check`
Audits context state synchronization against git commit history to detect and fix any documentation drift.

---

## 📚 Knowledge Base References

- **Masterclass Handbook**: [STEP_BY_STEP_SENIOR_AI_ENGINEERING_GUIDE.md](file:///d:/AI-OS/references/six-file-context-methodology/STEP_BY_STEP_SENIOR_AI_ENGINEERING_GUIDE.md)
- **Full Video Transcript**: [FULL_TRANSCRIPT.md](file:///d:/AI-OS/references/six-file-context-methodology/FULL_TRANSCRIPT.md)
- **29 Ghost AI Specs Library**: [feature-specs-library/](file:///d:/AI-OS/references/six-file-context-methodology/feature-specs-library/)
- **SEO Skills Library Vault**: [seo-audit-reference/](file:///d:/AI-OS/brain-aios/wiki/research/skills-library/seo-audit-reference/)
"""

with open(skill_path, 'w', encoding='utf-8') as f:
    f.write(skill_content)

print("Updated SKILL.md with addressed vulnerabilities.")

# 2. Append Roast Council Audit fixes to Guide
with open(guide_path, 'r', encoding='utf-8') as f:
    guide_text = f.read()

roast_fixes_section = """

---

## 🛡️ Addressed Vulnerabilities & Optimization Modes (Roast Council Audit)

### 1. Lite Mode vs. Pro Mode Project Selection
To eliminate the "build-tooling tax" on small 1-day builds or landing pages:
- **Lite Mode (4 Context Files + 3-5 Specs)**: For simple landing pages, single-page tools, or micro-utilities.
- **Pro Mode (7 Context Files + 10-50+ Specs)**: For multi-tenant SaaS products, complex web apps, and real-time collaboration tools.

### 2. Context Window & Token Optimization
To prevent reading 7 files on every turn and wasting context tokens:
- Task-scoped context loading is enforced: the AI agent only reads the context files relevant to the current task layer (e.g. `ui-context.md` for styling, `architecture.md` + `vibesec` for API routes).

### 3. State Drift Sync Check
`/six-file-context-methodology check` verifies git commit logs against `progress-tracker.md` to ensure code changes and documentation remain 100% synchronized.
"""

if "Addressed Vulnerabilities & Optimization Modes" not in guide_text:
    guide_text += roast_fixes_section
    with open(guide_path, 'w', encoding='utf-8') as f:
        f.write(guide_text)

print("Updated Guide with addressed vulnerabilities.")
