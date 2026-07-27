---
name: verify-design
description: Automatically build the project, run Fullstack /jsmastery-audit code checks, Playwright console audits, Hallmark anti-slop tests, and generate responsive screenshots across all 5 viewports. Invokable via /verify-design.
argument-hint: '[optional_target_directory]'
---

# ZORIXEL Visual & Fullstack Verification Engine (`/verify-design`)

## ⚡ Invocation & Tri-Mode Routing

This skill automates fullstack code quality audits and 5-viewport visual QA using Playwright and static analysis tools.

Invokable via:
- **Slash Command**: `/verify-design [target_dir]`
- **Dynamic Intent**: Triggered automatically when completing frontend milestones, verifying layouts, or preparing for release.

---

## 🎯 Specific Use Cases
- **Web App Release QA**: Audit Next.js App Router code (`/jsmastery-audit`), test Server Action security, check console errors, and verify responsive design across 5 viewports before deployment.
- **Micrographics & Component Library QA**: Execute visual regression sweeps across compiled cards, SVGs, and layouts to ensure 0 layout breakages.

---

## 🛠️ Verification Execution Steps

### Step 1: Fullstack Code Quality Audit (`/jsmastery-audit`)
1. Run `/jsmastery-audit` on the target project directory.
2. Check 6 Audit Gates:
   - Next.js `'use client'` boundaries & Server Action input validation (Zod).
   - Strict TypeScript types (zero `any`).
   - Environment variable hygiene (no private keys exposed).
   - Performance caching & image optimization.
   - Accessibility (WCAG AA contrast, keyboard focus).
   - Error boundaries (`error.tsx`, `not-found.tsx`).

### Step 2: Hallmark Anti-Slop Audit (`/hallmark`)
Run `python scripts/hallmark_runner.py audit <target-dir>` to verify compliance with 57 anti-slop quality gates:
- Confirm zero generic purple/blue gradients (`bg-gradient-to-r`).
- Confirm zero invented fake metric cards ("+47% conversion").
- Confirm zero un-tokenized Hex/HSL colors.
- Verify presence of Hallmark pre-emit self-critique headers.

### Step 3: Playwright 5-Viewport Visual Sweep
Run `python scripts/verify_design_milestone.py` across 5 viewports:
- Mobile Small (320px / 375px)
- Mobile Large (414px)
- Tablet (768px)
- Laptop (1024px)
- Desktop (1440px / 1920px)

### Step 4: Verification Report Output
Generate a clean Markdown verification summary:
- **Build Status**: Exit code 0, 0 linter/TS errors.
- **Console Audit**: 0 unhandled JS errors or network failures.
- **Hallmark Score**: Anti-slop pass / pre-emit score.
- **Visual Links**: Clickable links to generated screenshots.

---

## 🔗 Inter-Skill Connections & Handoff Pipeline
- **Web Creation QA**: Executed as Phase 6 in **`/website-design-engine`** and Milestone 4 in **`/new-project`**.
- **Code Auditor**: Calls **`/jsmastery-audit`** for fullstack static code analysis.
- **Anti-Slop & Quality Gates**: Invokes `python scripts/hallmark_runner.py` and **`/hallmark`**.
- **Executive Team QA**: Serves as the QA lens for **`/gstack`** (`/gstack qa` and `/gstack design`).

