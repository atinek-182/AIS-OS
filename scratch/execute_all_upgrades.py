import os

guide_path = r'd:\AI-OS\references\six-file-context-methodology\STEP_BY_STEP_SENIOR_AI_ENGINEERING_GUIDE.md'
skill_7file_path = r'd:\AI-OS\.agents\skills\six-file-context-methodology\SKILL.md'
skill_grillme_path = r'd:\AI-OS\.agents\skills\grill-me\SKILL.md'

# 1. STEP_BY_STEP_SENIOR_AI_ENGINEERING_GUIDE.md
guide_content = """# Masterclass Guide: How Senior AI Engineers Build With AI in 2026

## 📌 Executive Overview
This guide provides an unsummarized, complete blueprint of the Senior AI Engineering workflow taught by **JavaScript Mastery (Adrian Hajdin)** in the 4-hour masterclass *How Senior Engineers Actually Build With AI in 2026*, expanded with Atinek Maurya's **7-File Context System**, **Proactive Web Search Research**, **Playwright Visual QA Engine**, and **Global Zero-Hurry Mandate**.

In 2026, senior engineers do not manually type syntax line-by-line. They act as **Systems Architects** and **AI Supervisors**. They spend their time designing system boundaries, writing structured context files (`context/`), breaking products down into surgical feature specifications (`feature-specs/`), and directing AI agents (Cursor, Windsurf, Claude Code, Antigravity) to write production-ready code without architectural drift or slop.

---

## 🚨 Why Most AI-Assisted Projects Fail

1. **Failure Mode 1: Vibe Coding Collapse**
   - You open an AI tool, type a vague prompt (*"Build a dashboard"*), and let it run. The first hour feels incredible.
   - By week 3, adding a simple feature breaks the entire app. The AI contradicts earlier choices because every decision was an ungrounded guess.

2. **Failure Mode 2: Feature Drift**
   - You build a working MVP. Two weeks later, you start a new chat session to add a feature. The AI has **zero memory** between sessions.
   - It overwrites intentional architectural patterns, breaks styling, and "fixes" unbroken code.

**The Solution:** The 7-File Context System + Spec-Driven Development.

---

## 🏗️ The 7-File Context Methodology

Before writing a single prompt or opening a code editor, create a `context/` folder containing these 7 core context files (plus root entry instructions):

### 1. `AGENTS.md` / `CLAUDE.md` (System Entry Instructions)
- Entry point file read at the start of **every single AI session**.
- Forces the agent to read all 7 context files before touching any code.

### 2. `project-overview.md` (Product Intent & Scope)
- 1-paragraph overview of product value proposition.
- Step-by-step core user flow from sign-up to value creation.
- Explicit **In-Scope** list & **Out-of-Scope** list (prevents scope creep).
- Verifiable success criteria ("Signed-in user can create and save a canvas project").

### 3. `architecture.md` (Stack & Invariants)
- Stack table mapping every layer (Framework, DB, Auth, Real-time, Storage).
- Folder boundary definitions (which folder owns what responsibility).
- Storage & Auth model details.
- **Invariants**: Mandatory codebase rules that can NEVER be broken (e.g. *"Auth enforced at every mutation boundary"*, *"No long-running LLM calls inside synchronous HTTP routes"*).

### 4. `code-standards.md` (TypeScript & API Conventions)
- Strict TypeScript standards (no `any`, Zod schema validation for all inputs).
- Server Actions & API route structure.
- Naming conventions & folder layout rules.

### 5. `ui-context.md` (Design Tokens & Component Sourcing)
- Named color tokens (`globals.css` HSL/OKLCH variables, never raw hex values).
- Typography scale, spacing, border-radius rules.
- **Component Library Sourcing**: Integrated with AIOS's 4 curated libraries (**Aceternity UI**, **Animate UI React**, **Forge UI**, **Vengence UI**) containing 147 cataloged components queryable via `component_registry_cli.py`.

### 6. `ai-workflow-rules.md` (Disciplined Execution Commands)
- Direct imperative commands telling the AI agent how to behave.
- Rules for 1-spec-at-a-time execution and no speculative changes.

### 7. `progress-tracker.md` (Session Memory & Living Log)
- Tracks `Current Phase`, `Current Goal`, `Completed Specs`, `In Progress Spec`, `Next Up Specs`, `Open Questions`, and `Session Notes`.
- Restores 100% of project context in 5 seconds when starting a new session.

### 8. `seo-context.md` (Technical SEO & GEO AI Citation System)
- Target keywords & topic cluster architecture.
- Schema.org JSON-LD definitions (`SoftwareApplication`, `Organization`, `FAQPage`, `Article`).
- Dynamic metadata API & OpenGraph social sharing rules.
- **GEO (Generative Engine Optimization)** guidelines ensuring AI search engines (ChatGPT Search, Perplexity, Gemini) extract and cite your app.
- Deep integration with AIOS's 23-skill SEO vault (`d:\\AI-OS\\brain-aios\\wiki\\research\\skills-library\\seo-audit-reference\\`).

---

## ⚡ The Decoupled 3-Step Build Workflow

Never ask an AI agent to build a database schema, backend API, and rich UI component in a single prompt. Senior engineers execute every feature in 3 decoupled steps:

```
┌─────────────────────────────────────────────────────────────┐
│ STEP 1: UI Primitive Components & CSS Design Tokens          │
│ Build static UI layout, Shadcn/Aceternity components, tokens│
└──────────────────────────────┬──────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────┐
│ STEP 2: Database Schema & Headless Backend API Routes        │
│ Define Prisma model, run migrations, & create Server Actions│
└──────────────────────────────┬──────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────┐
│ STEP 3: UI-to-API Binding & Optimistic Updates               │
│ Connect UI state to backend Server Actions & Liveblocks room │
└──────────────────────────────┴──────────────────────────────┘
```

---

## 📋 Spec-Driven Development & Unbounded Spec Counts

1. **What is a Unit of Work?**
   - Small, scoped, verifiable piece of work built in one session.
   - *Example Unit*: *"Build project sidebar with My Projects & Shared tabs, empty placeholder states, and open/close behavior. No API calls yet."*
2. **Dynamic Spec Counts**:
   - Spec count is **unbounded** and matches app scope (can be 10, 15, 20, 40, 50+ specs).
3. **5 Mandatory Spec Sections**:
   - `Goal` (1-2 concrete sentences)
   - `Design` (UI tokens & component sources)
   - `Implementation` (Sub-sections per file/component)
   - `Dependencies` (Installed just-in-time)
   - `Verify when done` (Playwright CLI visual & console checklist)

---

## 🛡️ Pre-Write Roast Council & Gatekeeper Mode

Before writing any context or feature spec document, the AI agent runs the **Adversarial Roast Council** (`/roast`) against 5 quality gates:
1. **Security & Vulnerability Gate** (VibeSec check for unauthenticated actions or data leaks).
2. **Anti-AI-Slop Gate** (Hallmark & Obys check for generic colors or un-tokenized layouts).
3. **Scope Discipline Gate** (Karpathy check for unnecessary abstractions).
4. **Token Footprint Gate** (Context efficiency check).
5. **Verifiable MVP Gate** (Playwright testable output).

If risks are detected, the Roast Council **blocks document creation**, presents explicit flaws with recommended fixes, and waits for your confirmation before writing.

---

## 🧪 Playwright Visual QA Engine

Every feature spec verification is executed using **automated Playwright CLI scripts**:
- Captures 5-viewport responsive screenshots (Mobile, Tablet, Laptop, Desktop, Ultrawide).
- Audits browser console for zero JS runtime errors.
- Verifies visual component layout stability so you don't have to inspect manually.

---

## ⏱️ The Global Zero-Hurry & Rigor Mandate

Across all skills, workflows, and AIOS projects:
- **Never Rush**: Complex systems take time (weeks or months). Quality and architectural perfection take absolute precedence over speed.
- **Proactive Web Search**: Search the web for industry-leading technical solutions before proposing implementations.
- **Deep Option-Based Inquiries**: Ask detailed option-based questions with recommended answers at every stage.
- **Pre-Coding Backstop**: Always ask: *"Is there anything else remaining before we touch the code?"*
"""

with open(guide_path, 'w', encoding='utf-8') as f:
    f.write(guide_content)

print("Updated guide written to:", guide_path)

# 2. .agents/skills/six-file-context-methodology/SKILL.md
skill_7file_content = """---
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

## 📌 Hard-and-Fast System Mandates

1. **Global Zero-Hurry Rule**: Never rush execution. Systems take time (weeks/months). Architectural rigor, deep questioning, and web research take precedence over speed.
2. **Interactive Architect Discovery (`init`)**: Run Playbook prompts in an interactive option-based Q&A loop before writing context files.
3. **7-File Context Foundation**:
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

---

## 🛠️ Commands & Workflow Guide

### 1. `/six-file-context-methodology init`
Runs an interactive Q&A discovery loop using Playbook prompts to gather product vision, stack choices, UI tokens, SEO strategy, and invariants before creating the 7 context files in `context/`.

### 2. `/six-file-context-methodology spec <feature-name>`
Generates a numbered, 5-section feature spec in `context/specs/NN-<feature-name>.md`. Search the web for best practices and run `/roast` before emitting file content.

### 3. `/six-file-context-methodology spec-all`
Decomposes the entire `project-overview.md` into an unbounded list of numbered units (`00-build-plan.md`) following strict build-order rules (Dependencies -> Auth -> Backend APIs -> UI Wiring), and generates all feature specs upfront in `context/specs/`.

### 4. `/six-file-context-methodology verify`
Executes Playwright CLI to capture 5-viewport screenshots and verify console error cleanliness for completed feature units.

---

## 📚 Knowledge Base References

- **Masterclass Handbook**: [STEP_BY_STEP_SENIOR_AI_ENGINEERING_GUIDE.md](file:///d:/AI-OS/references/six-file-context-methodology/STEP_BY_STEP_SENIOR_AI_ENGINEERING_GUIDE.md)
- **Full Video Transcript**: [FULL_TRANSCRIPT.md](file:///d:/AI-OS/references/six-file-context-methodology/FULL_TRANSCRIPT.md)
- **29 Ghost AI Specs Library**: [feature-specs-library/](file:///d:/AI-OS/references/six-file-context-methodology/feature-specs-library/)
- **SEO Skills Library Vault**: [seo-audit-reference/](file:///d:/AI-OS/brain-aios/wiki/research/skills-library/seo-audit-reference/)
"""

with open(skill_7file_path, 'w', encoding='utf-8') as f:
    f.write(skill_7file_content)

print("Updated 7-file skill written to:", skill_7file_path)

# 3. .agents/skills/grill-me/SKILL.md
skill_grillme_content = """---
name: grill-me
description: Interview the user relentlessly about a plan, design, or topic, checkpointing
  every answer to a brainstorm file so nothing is lost. Use when the user wants to
  stress-test a plan, get grilled on a design, run a brainstorm or discovery session,
  extract what's in their head into a doc, or says "grill me". Invokable directly
  via /grill-me.
argument-hint: '[optional parameters]'
---

# Grill Me (`/grill-me`)

## ⚡ Invocation & Tri-Mode Routing

This skill supports **Tri-Mode Flexible Execution**:
- **Slash Command**: Explicitly run `/grill-me [optional parameters]` in chat.
- **Dynamic Intent Matching**: Triggered automatically when task context involves keywords in the description.
- **Inter-Skill & AIOS Calling**: Programmatically invokable by parent skills or subagents via `/grill-me` or by reading `SKILL.md` directly.

---

## 📌 Hard-and-Fast Execution Rules

1. **Global Zero-Hurry Rule**: Never rush the interview. Complex systems take time (weeks or months). Deep exploration and architectural perfection take absolute precedence over speed.
2. **Concept Explanation Before Every Question**: If the user hasn't watched a video, read source docs, or touched a specific topic, **ALWAYS explain the underlying concept in clear, plain language FIRST** before asking any question or making a suggestion.
3. **Proactive Web Search Research**: Before asking a question or offering options, search the web to discover industry-leading best practices, tools, or solutions.
4. **Structured Option-Based Inquiries**: For every question, present clear multiple-choice options (with your recommended answer highlighted) so the user can easily confirm, correct, or redirect. Ask unlimited questions — never artificially limit inquiries to 2-3 questions.
5. **Checkpoint to Disk After Every Single Answer**: Immediately update `brainstorms/{YYYY-MM-DD}-{topic-slug}.md` after every user response before asking the next question.
6. **Pre-Write `/roast` Council**: Run the `/roast` skill to pressure-test every captured document concept before writing final deliverable files.
7. **Pre-Coding Backstop**: Before concluding or moving to implementation, ask: *"Is there anything else remaining before we touch the code?"*

---

## Setup (do this BEFORE the first question)

1. Create capture file at `brainstorms/{YYYY-MM-DD}-{topic-slug}.md`.
2. Notify the user of the file path in one line.
3. Explain Concept 1 in clear language, then ask Q1 with recommended options.

---

## Capture File Structure

```markdown
# {Topic}: Brainstorm / Discovery Notes
Date: {date} · Goal: {one line}

## Summary / key decisions
(running synthesis, updated as you go)

## Q&A log
### Q1 — {topic}
- Asked: {question}
- Captured: {facts, decisions, in their words where it matters}
- Flags: {open item -> owner}

## Open flags (pending input)
- {item} -> {who can answer}
```
"""

with open(skill_grillme_path, 'w', encoding='utf-8') as f:
    f.write(skill_grillme_content)

print("Updated grill-me skill written to:", skill_grillme_path)
