---
name: grill-me
description: Deep Socratic discovery and grilling engine tailored for Atinek Maurya. Relentlessly interviews the user about a plan, feature design, business idea, content carousel, or tech stack, explaining concepts before asking questions, presenting structured options, and logging answers to brainstorm capture files. Invokable via /grill-me or naturally when starting any discovery session.
argument-hint: '[topic_or_idea] [optional focus]'
---

# ZORIXEL AIOS Discovery & Socratic Grilling Engine (`/grill-me`)

## ⚡ Overview & Tri-Mode Execution

This skill is the primary discovery gate for Atinek Maurya's AIOS (`AI-OS`). It combines Matt Pocock's Socratic grilling (`grilling`, `grill-with-docs`), domain modeling (`domain-modeling`), and JS Mastery's option evaluation (`architect`) into a relentless, structured discovery workflow.

Invokable via:
- **Slash Command**: `/grill-me [topic_or_idea]`
- **Dynamic Intent**: Triggered automatically when starting new features, designing web apps, planning content carousels, or extracting ideas.
- **Programmatic Inter-Skill Calling**: Called by parent skills (`new-project`, `website-design-engine`, `design-direction`, `carousel-copy`, `ingest-repo`, `mattpocock-wayfinder`, `jsmastery-architect`).

---

## 🎯 When & Why to Use `/grill-me`

| Scenario / Goal | Specific Use Case | Key Output |
|---|---|---|
| **New Web App / Feature** | Uncover user requirements, DB models, tech stack choices, and UX conversion paths | `brainstorms/{date}-{slug}.md` + `docs/specs/SPEC-[slug].md` |
| **Zorixel Content / Carousel** | Define slide hooks, visual contrast themes, audience pain points, and CTAs | `brainstorms/{date}-carousel-{slug}.md` |
| **AI SaaS / Automation Idea** | Stress-test business model, price points, and time-to-first-dollar before coding | `brainstorms/{date}-saas-{slug}.md` -> feed into `/roast` |
| **System Refactor / Architecture** | Resolve domain vocabulary (`CONTEXT.md`) and state machine edge cases | `brainstorms/{date}-architecture-{slug}.md` + ADRs |

---

## 📌 Non-Negotiable Core Execution Rules

### 1. Global Zero-Hurry & Rigor Mandate
Never rush discovery. Quality, deep option-based Q&A, web research, and architectural rigor take absolute precedence over speed.

### 2. Concept Explanation BEFORE Every Question
If the operator hasn't watched a video, read documentation, or touched a specific topic, **ALWAYS explain the underlying concept in clear, plain language FIRST** before asking any question or offering options.

### 3. Proactive Web Research & Documentation Sourcing
Before asking a question, use `search_web` or `context7` to fetch industry best practices, current library APIs (e.g. Next.js 15 App Router, Supabase, Tailwind v4, Motion), and competitive benchmarks.

### 4. Categorized Option-Based Inquiries (INFER / ASK / RECOMMEND)
Sort every discovery item into:
- **INFER**: Framework details, dependencies, and file layout derived from codebase (never ask what code reveals).
- **ASK**: Only what Atinek Maurya alone knows (business targets, revenue model, personal preferences).
- **RECOMMEND**: Expert recommendations with a clear 1-line rationale and runner-up alternative (highlight recommended option as `[RECOMMENDED]`).

### 5. Checkpoint to Disk After Every Single Response
Append to `brainstorms/{YYYY-MM-DD}-{topic-slug}.md` immediately after every response before moving to the next question. The capture file is the immutable record of truth.

### 6. Domain Vocabulary & Ubiquitous Language Maintenance (`mattpocock-domain-modeling`)
When ambiguous or overloaded terms are used (e.g., "User" vs "Customer", "Workspace" vs "Project"), challenge them immediately and record resolved terms into `CONTEXT.md`.

### 7. Mandatory Pre-Write `/roast` Council Gate
Convene the 5-persona `/roast` council (Contrarian, Expansionist, Logician, Researcher, Buyer) to audit captured decisions before generating specs, layouts, or code.

### 8. Pre-Coding Backstop Check
Before concluding the interview or proceeding to implementation, ask:
> *"Is there anything else remaining before we touch the code or generate artifacts?"*

---

## 📝 Capture File Structure (`brainstorms/{date}-{slug}.md`)

```markdown
# {Topic}: Discovery & Brainstorm Notes
Date: {date} · Goal: {one-line summary} · Operator: Atinek Maurya

## Executive Summary & Key Decisions
(Running synthesis updated as questions resolve)

## Domain Vocabulary & Glossary (CONTEXT.md updates)
- **[Term]**: Canonical definition resolved during discovery.

## Q&A Log
### Q1 — {Topic}
- **Concept Explained**: {short concept summary}
- **Asked**: {question}
- **Options Provided**: 1. Option A | 2. Option B [RECOMMENDED] | 3. Option C
- **Captured Decision**: {user's answer}
- **Rationale & Trade-offs**: {why this pick works}

## Open Flags & Deferred Decisions
- [ ] {Item} -> {Who/When to resolve}
```

---

## 🔗 Inter-Skill Connections & Handoff Pipeline
- **Phase 0 Discovery Engine**: Called as Gate 1 discovery by **`/new-project`**, **`/website-design-engine`**, **`/ingest-repo`**, **`/carousel-copy`**, and **`/design-direction`**.
- **Adversarial Audit**: Hands off captured decisions to **`/roast`** (Gate 2 5-persona council audit).
- **Domain Modeling**: Updates **`CONTEXT.md`** vocabulary via **`/mattpocock-domain-modeling`**.
- **Spec Compilation**: Feeds discovery notes into **`/mattpocock-to-spec`** and **`/jsmastery-architect`**.

