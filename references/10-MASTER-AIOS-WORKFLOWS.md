---
title: ZORIXEL AIOS 10 Master Integrated Workflows Reference Manual
domain: architecture
summary: 'This document defines the canonical execution specification for all 10 integrated multi-skill workflow chains operating
  within ZORIXEL AIOS. **Goal**: End-to-end client discovery, sprint scoping, visual development, and quality audit.'
critical_directives:
- '**Step 3**: `/gstack eng` — Enforce `/codebase-design` deep module rules (simple interface over deep'
section_outline:
- ZORIXEL AIOS 10 Master Integrated Workflows Reference Manual
- 1. ZORIXEL Client Sprints & Acquisition
- 2. Superpowers Parallel Subagent System
- 3. GStack Executive Team Matrix
- 4. Fullstack Next.js & UI Architecture
read_triggers:
- When working on architecture in references/10-MASTER-AIOS-WORKFLOWS.md
- When reading context for ZORIXEL AIOS 10 Master Integrated Workflows Reference Manual
tags:
- architecture
- 10-MASTER-AIOS-WORKFLOWS
updated: '2026-08-08'
---

# ZORIXEL AIOS 10 Master Integrated Workflows Reference Manual

This document defines the canonical execution specification for all 10 integrated multi-skill workflow chains operating within ZORIXEL AIOS.

---

## 1. ZORIXEL Client Sprints & Acquisition
**Goal**: End-to-end client discovery, sprint scoping, visual development, and quality audit.
- **Step 1**: `/grill-with-docs` — Conduct socratic interview and build client domain glossary in `CONTEXT.md` & ADRs.
- **Step 2**: `/to-spec` — Synthesize conversation into a formal technical specification document.
- **Step 3**: `/to-tickets` — Break spec into tracer-bullet ticket files under `.scratch/<sprint>/issues/`.
- **Step 4**: `/implement` + `/website-design-engine` + `/hallmark` — Build UI using OKLCH solid brand tokens and 57 anti-slop gates.
- **Step 5**: `/code-review` — Perform 2-axis Standards + Spec diff audit before client demo.

---

## 2. Superpowers Parallel Subagent System
**Goal**: Parallel autonomous feature implementation across independent ticket branches.
- **Step 1**: `/to-tickets` — Break plan into ticket files declaring `Blocked by: NN` dependency graphs.
- **Step 2**: `subagent-driven-development` — Launch parallel subagents per unblocked ticket file.
- **Step 3**: `/tdd` — Execute red-green-refactor testing loop for each ticket slice.
- **Step 4**: `verification-before-completion` — Run automated verification scripts before merging.

---

## 3. GStack Executive Team Matrix
**Goal**: Garry Tan executive lens review for product strategy, engineering depth, UI taste, and QA.
- **Step 1**: `/gstack ceo` — Verify user value, MVP scope discipline, and ROI.
- **Step 2**: `/grill-with-docs` — Align on requirements and capture domain terms.
- **Step 3**: `/gstack eng` — Enforce `/codebase-design` deep module rules (simple interface over deep functionality).
- **Step 4**: `/implement` — Build implementation slices test-first.
- **Step 5**: `/gstack qa` + `/code-review` — Execute Playwright browser QA and 2-axis code review.

---

## 4. Fullstack Next.js & UI Architecture
**Goal**: Production-grade fullstack web application development with type-safe server actions.
- **Step 1**: `/jsmastery-architect` — Define Next.js App Router structure, Server Actions, and Zod input validation schemas.
- **Step 2**: `/prototype` — Build throwaway UI/animation prototype to test state and UX.
- **Step 3**: `/to-spec` — Convert proven prototype into a buildable specification.
- **Step 4**: `/implement` + `/hallmark` — Implement production code enforcing solid brand design tokens.

---

## 5. Incident Response & Debugging
**Goal**: Disciplined root-cause bug resolution and technical debt refactoring.
- **Step 1**: `/diagnosing-bugs` — Execute 6-step loop: reproduce -> minimize -> hypothesize -> instrument -> fix -> regression test.
- **Step 2**: `/improve-codebase-architecture` — If bug reveals fragile architecture, scan codebase for deep-module refactoring opportunities.
- **Step 3**: `/vibesec` — Run security audit on touched endpoints (IDOR, SSRF, JWT, mass assignment).

---

## 6. MCP Server & Application Engineering
**Goal**: Design, package, and integrate custom Model Context Protocol servers and interactive apps.
- **Step 1**: `/build-mcp-server` — Design MCP tools, resources, and JSON-RPC schema definitions.
- **Step 2**: `/build-mcpb` — Package server into standalone production binary or bundle.
- **Step 3**: `/build-mcp-app` — Add interactive DOM UI widgets and rendering interfaces.
- **Step 4**: `/mcp-integration` — Register and test server inside workspace `mcp_config.json`.

---

## 7. Multi-Platform SaaS Automation
**Goal**: Build 100% zero-subscription client operational hubs integrating 1000+ SaaS platforms.
- **Step 1**: `/composio` — Connect and execute OAuth actions across HubSpot, Stripe, Linear, Salesforce, Shopify, or Zoom.
- **Step 2**: `/gws-automation-engine` — Provision Google Sheets, Drive folders, and free Google Apps Scripts.
- **Step 3**: `/notion-sync` + `/notion-formula-builder` — Build Notion master databases with defensive Formula 2.0 expressions.
- **Step 4**: `/zero-paywall-client-os` — Deliver zero-subscription client operational hub SOP.

---

## 8. React Video & Motion Graphics Engine
**Goal**: Programmatic video creation, motion visual ads, and social media media rendering.
- **Step 1**: `/canvas-design` — Generate base vector graphic assets and layout elements.
- **Step 2**: `/gsap-animation` — Define ScrollTrigger physics keyframes and motion curves.
- **Step 3**: `/remotion` — Render programmatic React video compositions.
- **Step 4**: `/carousel-render` — Output final HD PNG/MP4 media files for distribution.

---

## 9. Autoresearch & System Observability
**Goal**: Autonomous codebase optimization, benchmark tuning, and AST knowledge graph maintenance.
- **Step 1**: `/storm-research-project` — Run 7-agent multi-perspective technical analysis.
- **Step 2**: `/smart-explore` — Perform tree-sitter AST structural code search.
- **Step 3**: `/autoresearch-manage` — Execute autonomous optimization and benchmark loop.
- **Step 4**: `/graphify` — Update tree-sitter AST knowledge graph (`graph.json`, `graph.html`).

---

## 10. Visual Architecture & Executive Handoff
**Goal**: Awwwards-level visual handoff documentation, architecture diagrams, and slide decks.
- **Step 1**: `/excalidraw-diagram` — Generate visual system topology diagram in Excalidraw format.
- **Step 2**: `/frontend-slides` — Build 16:9 interactive HTML presentation deck with Havock & Rosehot brand fonts.
- **Step 3**: `/interactive-operator-guide-generator` — Build copyable setup dashboard and SOP.
- **Step 4**: `/wowerpoint` — Compile executive PDF slide deck for client delivery.
