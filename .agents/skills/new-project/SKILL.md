---
name: new-project
description: Initialize a new Premium Frontend website or web app project tailored for Atinek Maurya. Scaffolds project directories, runs Phase 0 /grill-me discovery + /roast council gate, compiles /mattpocock-to-spec build contract, scopes /jsmastery-scope tracer-bullet slices, and deconstructs /mattpocock-to-tickets execution tasks. Invokable via /new-project.
argument-hint: '[project-name]'
---

# New Project Initialization Engine (`/new-project`)

## ⚡ Invocation & Tri-Mode Routing

This skill initializes brand-new website applications, client landing pages, or digital product MVPs.

Invokable via:
- **Slash Command**: `/new-project [project-name]`
- **Dynamic Intent**: Triggered automatically when starting a new website project or initializing a web application.
- **Inter-Skill Calling**: Invoked by `/website-design-engine`, `/gstack`, and `ingest-repo`.

---

## 🎯 Specific Use Cases & Goal Alignment
- **Client Conversion Portfolios / Agency Sites**: Rapidly scaffold multi-page React/Vite/Next.js projects with locked OKLCH tokens, Obys grid canons, and Hallmark anti-slop rules.
- **Sellable AI SaaS / Micro-Products**: Scaffold fullstack Next.js App Router applications with Server Action boundaries, Zod validation, and Supabase/Clerk auth.

---

## 🚀 Execution Workflow

### Step 1: Resolve Directory & Scaffold Structure
1. Set project path: `projects/[project-name]`.
2. Scaffold directory structure:
   - `projects/[project-name]/design-briefs/`
   - `projects/[project-name]/assets-briefs/`
   - `projects/[project-name]/docs/specs/`
   - `projects/[project-name]/docs/scope/`
   - `projects/[project-name]/qa/`
   - `projects/[project-name]/src/`
3. **Copy Streamlined Brief Templates**:
   - Copy templates from `premium-frontend-experience-system/design-briefs/` to `projects/[project-name]/design-briefs/`.
   - Copy templates from `premium-frontend-experience-system/assets-briefs/` to `projects/[project-name]/assets-briefs/`.
   - Ensure copied templates contain relative Obsidian cross-links pointing to `../../PROJECT_BRIEF.md`.

### Step 2: Phase 0 Socratic Discovery (`/grill-me` + `/hallmark`)
Run `/grill-me` on the 10 Project Discovery questions:
1. Website/Product name & core goal.
2. Target audience & conversion outcome.
3. Emotional feel in the first 5 seconds.
4. Reference URLs & design references (run `/hallmark study <url>` to extract DNA into `design.md`).
5. Macrostructure selection (Pick 1 of 21 Hallmark archetypes).
6. Theme selection (Pick 1 of 20 OKLCH color palettes).
7. Motion language (GSAP ScrollTrigger, Lenis smooth scroll, magnetic cursor).
8. Tech stack (Next.js App Router / Vite React / Tailwind v4).
9. WebGL / 3D shaders / canvas requirements.
10. Explicit anti-slop bans (Enforce Hallmark 57 quality gates).

### Step 3: Adversarial Pre-Build Roast Council Gate (`/roast`)
Run `/roast` on the initial project brief:
- **Contrarian**: Challenge scope bloat, load-bearing assumptions, and technical risk.
- **Expansionist**: Identify 10x upside and additional feature leverage.
- **Buyer**: Validate user conversion and willingness to interact/buy.
- Obtain **GO / RESHAPE** verdict before proceeding to code.

### Step 4: Spec & Ticket Compilation (`/mattpocock-to-spec` & `/jsmastery-scope` & `/mattpocock-to-tickets`)
1. **Compile Technical SPEC (`/mattpocock-to-spec`)**: Save `docs/specs/SPEC-[project-name].md` detailing user stories (Gherkin style), system boundaries, and data contracts.
2. **Define Tracer-Bullet Vertical Slices (`/jsmastery-scope`)**: Save `docs/scope/scope.md` separating MVP tracer-bullet slices (DB -> API -> UI -> QA) from Phase 2 features.
3. **Initialize Base `PROJECT.md` & Atomic Execution Tickets (`/mattpocock-to-tickets`)**: Generate `PROJECT.md` at the project root outlining the 4 Milestones with atomic tickets and testable DoD:
   - Milestone 1: Hero Section & Brand Foundation
   - Milestone 2: Page Subsections & Interactivity
   - Milestone 3: Motion Choreography & Shaders
   - Milestone 4: Visual Polish, Security Audit & Playwright QA
4. **Establish Ubiquitous Language (`/mattpocock-domain-modeling`)**: Initialize `CONTEXT.md` with resolved project vocabulary.

### Step 5: Verification & Pre-Commit Link Audit
Execute `python scripts/hallmark_runner.py audit projects/[project-name]` and confirm all cross-links and project files are intact.

---

## 🔗 Inter-Skill Connections & Handoff Pipeline
- **Web Creation Hand-off**: Hands off to **`/website-design-engine`** for Phase 1-7 layout build and grid math execution.
- **Architecture & Build Specs**: Leverages **`/jsmastery-architect`** and **`/mattpocock-to-spec`**.
- **Verification & QA**: Hands off to **`/verify-design`** for 5-viewport visual QA screenshots.
