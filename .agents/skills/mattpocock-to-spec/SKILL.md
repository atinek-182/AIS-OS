---
name: mattpocock-to-spec
description: Convert loose user prompts into sharp technical specs. Asks clarifying questions, resolves architectural choices, and outputs structured design contracts. Triggered via /mattpocock-to-spec or naturally when creating technical specs.
argument-hint: '[loose_idea_or_requirement]'
---

# Matt Pocock Prompt-to-SPEC Engine (`/mattpocock-to-spec`)

## ⚡ Overview & Tri-Mode Routing

Adapted from Matt Pocock's engineering skills, this tool converts loose, high-level requests into rigorous, unambiguous technical specs before any code is touched.

Invokable via:
- **Slash Command**: `/mattpocock-to-spec [idea]`
- **Dynamic Intent**: Triggered automatically when turning informal user requests into structured engineering contracts.
- **Inter-Skill Calling**: Invoked by `/new-project`, `/website-design-engine`, `/mattpocock-wayfinder`, and `/jsmastery-architect`.

---

## 🛠️ The 4-Step Spec Compilation Process

### Step 1: Intent Extraction & Socratic Discovery (`/grill-me`)
If the request is ambiguous, run `/grill-me` with 1-3 crisp clarifying questions. Do NOT make silent assumptions about core data models, security boundaries, or library choices.

### Step 2: System Boundary & Interface Definition (`/mattpocock-domain-modeling`)
Define exact inputs, outputs, types, and boundaries:
- Data flow schema (JSON payload / TypeScript types).
- Error conditions & edge case behaviors.
- State mutation expectations.

### Step 3: Write Technical SPEC (`SPEC.md`)
Compile the specification into `docs/specs/SPEC-[slug].md`:
- **Context & Problem Statement**
- **User Stories & Acceptance Criteria (Gherkin style: Given/When/Then)**
- **Technical Architecture & Data Contract**
- **Non-Functional Requirements (Security, Speed, Accessibility)**
- **Edge Cases & Failure Modes**

### Step 4: Verification & Approval Checkpoint (`/roast`)
Run `/roast` on the spec summary to obtain a **GO / RESHAPE** verdict before proceeding to ticket creation or implementation.

---

## 🔗 Inter-Skill Connections & Handoff Pipeline
- **Upstream Discovery**: Driven by **`/grill-me`** and **`/mattpocock-domain-modeling`**.
- **Adversarial Audit**: Verified by **`/roast`**.
- **Downstream Ticket Decomposition**: Hands off compiled `SPEC.md` to **`/mattpocock-to-tickets`** and **`/jsmastery-scope`**.
