---
name: jsmastery-architect
description: Fullstack JavaScript & Next.js architecture design engine. Use when choosing tech stacks, designing complex features, selecting state/database patterns, or writing load-bearing build specs. Triggered via /jsmastery-architect or naturally when planning fullstack JS/TS apps.
argument-hint: '[feature_or_system_name] [optional focus]'
---

# JS Mastery Fullstack Architecture Engine (`/jsmastery-architect`)

## ⚡ Overview & Tri-Mode Routing

This skill provides fullstack JavaScript and Next.js architectural discipline adapted from JavaScript Mastery Pro. Use it when making load-bearing technical decisions, choosing tech stacks, designing Next.js App Router architectures, or defining database/state/auth patterns.

Invokable via:
- **Slash Command**: `/jsmastery-architect [feature_or_system_name]`
- **Dynamic Intent**: Triggered automatically when planning fullstack JavaScript, Next.js, or React app architectures.
- **Inter-Skill Calling**: Invoked by `/website-design-engine`, `/new-project`, `/grill-me`, `/roast`, `/jsmastery-scope`, and `/mattpocock-to-spec`.

---

## 🏗️ The 4 Architectural Modes

| Mode | Trigger | Focus |
|---|---|---|
| `FEATURE` | Designing a new fullstack feature from scratch | First-principles API, DB schema, UI/Server action boundaries |
| `ARCHITECTURE` | Selecting tech stack, ORM, Auth, state engine | Fullstack stack evaluation, serverless/edge compatibility |
| `ENHANCEMENT` | Refactoring or scaling existing architecture | Codebase inspection, focused option trade-offs |
| `CROSS-CUTTING` | Standardizing auth, error handling, logging, ORM | Uniform patterns across all routes and components |

---

## 📋 Architectural Workflow

### Step 1: Pre-Flight & Workspace Inspection
1. Read root `AGENTS.md` and project `package.json` to infer tech stack (Next.js, React, Tailwind, Prisma/Drizzle, Supabase, NextAuth/Clerk, etc.).
2. Locate or create build spec directory at `docs/specs/` (or `brain-aios/wiki/specs/` if in AIOS vault).
3. Determine spec numbering (`0001-feature-name.md`).

### Step 2: Staged Discovery & Option Evaluation (`/grill-me` + `/roast`)
1. **Run Socratic Discovery (`/grill-me`)**: Ask targeted, single-topic questions using **INFER / ASK / RECOMMEND**:
   - **INFER**: Infer framework details, dependencies, and file layout from codebase.
   - **ASK**: Ask only what the operator alone knows (business logic, security boundaries, user flows).
   - **RECOMMEND**: Provide expert recommendation for tools, state engines, or database patterns with a clear rationale and runner-up alternative.
2. **Convene Adversarial Roast Council (`/roast`)**: Audit spec decisions against 5 personas (Contrarian, Expansionist, Logician, Researcher, Buyer) to obtain a **GO / RESHAPE** verdict.

### Step 3: Spec Compilation & Domain Vocabulary (`/mattpocock-to-spec` & `/mattpocock-domain-modeling`)
Write the complete build spec using the standard structure:
- `## Summary`: High-level goal.
- `## Requirements`: Functional and technical requirements.
- `## Stack & Components`: Components, routes, server actions, database schema, state management.
- `## Options Considered`: Trade-offs and why the recommendation was selected.
- `## Build Plan`: Sequential, verifiable implementation steps.
- `## Security & Performance`: Authz, input validation (Zod), caching (revalidatePath/tags), and rate limiting.

### Step 4: Spec Handoff & Verification (`/jsmastery-scope` & `/jsmastery-audit`)
1. Save the spec file to `docs/specs/NNNN-[slug].md`.
2. Hand off to **`/jsmastery-scope`** to break the spec into tracer-bullet vertical slices.
3. Verify implementation via **`/jsmastery-audit`** post-build.

---

## 🔗 Inter-Skill Connections & Handoff Pipeline
- **Discovery & Validation**: Uses **`/grill-me`** and **`/roast`**.
- **Domain Modeling**: Uses **`/mattpocock-domain-modeling`** and **`/mattpocock-to-spec`**.
- **Scoping & Tickets**: Hands off to **`/jsmastery-scope`** and **`/mattpocock-to-tickets`**.
- **Code Audit & QA**: Hands off to **`/jsmastery-audit`** and **`/verify-design`**.
