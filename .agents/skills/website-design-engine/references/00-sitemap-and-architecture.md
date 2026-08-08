---
title: 'Phase 0 Reference: Sitemap & Shared Architecture Scaffolding (v4.0)'
domain: skill
summary: 'Before writing individual page components or route handlers: 1. **Phase 0 Stack Inquiry (`/grill-me`)**:'
critical_directives:
- Follow document guidance without bypassing established safeguards.
section_outline:
- 'Phase 0 Reference: Sitemap & Shared Architecture Scaffolding (v4.0)'
- Phase 0 & Phase 0.1 Verification Protocol
- Multi-Page Sitemap Specification
- Master RootLayout Standards
read_triggers:
- When working on skill in .agents/skills/website-design-engine/references/00-sitemap-and-architecture.md
- 'When reading context for Phase 0 Reference: Sitemap & Shared Architecture Scaffolding (v4.0)'
tags:
- skill
- 00-sitemap-and-architecture
updated: '2026-08-08'
---

# Phase 0 Reference: Sitemap & Shared Architecture Scaffolding (v4.0)

## Phase 0 & Phase 0.1 Verification Protocol

Before writing individual page components or route handlers:

1. **Phase 0 Stack Inquiry (`/grill-me`)**:
   - Inquire: *"Do you need Fullstack (Next.js 15 App Router with `await params` + React 19 + Server Actions) or a Lightweight SPA (Vite + React + Tailwind v4)?"*
   - Establish Motion Dial (0-10) and primary lead conversion path.

2. **Phase 0.1 Document & Complete Project Sweep**:
   - Inspect Six-File Context files (`TECH_STACK.md`, `REQUIREMENTS.md`, `ARCHITECTURE.md`, `PROJECT.md`, `ROADMAP.md`, `STATE.md`).
   - Read project root config files (`package.json`, `drizzle.config.ts`, `prisma/schema.prisma`, `.env.example`).
   - Execute `python scripts/graphify_runner.py query "<project-topic>"` and `python scripts/aios_deep_search.py "<project-topic>"` to extract AST node connections across all 8 workspace vaults.
   - Solicit clarification for underspecified context BEFORE making design/code decisions.

3. **Phase 0.2 Adversarial Pre-Build Audit (`/roast`)**:
   - Convene `/roast --domain code --save` to stress-test proposed architecture, routes, and risk matrix.

---

## Multi-Page Sitemap Specification

Establish a clean site tree with conversion routing:

```json
{
  "site_title": "Project Name",
  "base_url": "https://example.com",
  "routes": [
    {
      "path": "/",
      "name": "Home",
      "layout": "RootLayout",
      "purpose": "Hero narrative, custom bottleneck text field, key feature highlights, CTA"
    },
    {
      "path": "/about",
      "name": "About / Story",
      "layout": "RootLayout",
      "purpose": "Brand story, team narrative, philosophy, visual timeline"
    },
    {
      "path": "/features",
      "name": "Features / Product Matrix",
      "layout": "RootLayout",
      "purpose": "Deep product breakdown, interactive feature tabs, comparison matrix"
    },
    {
      "path": "/pricing",
      "name": "Pricing / Value Lock",
      "layout": "RootLayout",
      "purpose": "Nate Herk value-first price delay, 3-tier card comparison, FAQ accordion"
    },
    {
      "path": "/contact",
      "name": "Contact / Audit",
      "layout": "RootLayout",
      "purpose": "Interactive bottleneck form, Google Sheets CRM auto-sync, office location visual"
    }
  ]
}
```

---

## Master RootLayout Standards

Every multi-page site generated MUST use a shared master `RootLayout` component wrapping child pages:

1. **Persistent Header Navigation (`<Navbar>`)**:
   - Logo anchor on top-left (Nuqun brand font or clean geometric vector).
   - Centered route navigation links with active state indicator styling (`aria-current="page"`).
   - Primary action CTA button on top-right ("Get Started", "Book Demo").
   - Responsive Mobile Hamburger menu overlay with smooth fade/slide transitions.

2. **Persistent Global Footer (`<Footer>`)**:
   - Brand mission statement & copyright.
   - Categorized sitemap links matching the route tree.
   - Newsletter signup or primary contact trigger.
   - Social links & legal policy anchors.

3. **SEO Meta Inheritance**:
   - Next.js 15: Export metadata via `generateMetadata()` or static `metadata` object.
   - Vite React SPA: Use dynamic document title updates.
