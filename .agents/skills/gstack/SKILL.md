---
name: gstack
description: "Garry Tan's virtual engineering team workflow (CEO strategy, EM architecture, UI/UX design, browser QA, release audit). Automatically triggers when reviewing plans, auditing code, evaluating feature value, checking UI quality, or running executive reviews — even without explicit /gstack command."
argument-hint: "[ceo | eng | design | qa | full] [optional target or plan]"
---

# `gstack` — Garry Tan's AI Engineering Team Workflow

Use `/gstack` (or invoke naturally via phrases like "run Garry Tan review", "GStack review", "CEO product check", "EM architecture audit", "UI/UX design review", or "QA browser audit") whenever you want to evaluate a project, plan, feature, or code change through Garry Tan's Virtual Engineering Team (CEO, Engineering Manager, UI/UX Designer, QA Officer, Security/Release Officer).

> [!TIP]
> **Dynamic Triggering**: This skill runs automatically during major architectural planning, code reviews, design evaluations, and pre-release audits without requiring explicit `/` slash commands.


---

## The Virtual Engineering Team Roles

### 1. CEO Product Review (`/gstack ceo`)
Evaluate feature proposals from a YC CEO & Product Founder perspective:
- **Value & Impact**: Does this solve a high-value problem for users?
- **Scope Discipline**: Is this the minimum viable product (MVP) slice or is it over-engineered bloat?
- **User Delight**: Will this wow the user at first glance?
- **Clear Tradeoffs**: What are we giving up by building this now?

### 2. Engineering Manager Review (`/gstack eng`)
Evaluate code & architecture against strict senior EM standards:
- **Simplicity & Surgical Edits**: Is the implementation simple, readable, and surgical?
- **No Over-Abstraction**: Are there unnecessary patterns, speculative abstractions, or unused dependencies?
- **Type Safety & Reliability**: Are error states, edge cases, and empty states handled cleanly?
- **Performance & Scalability**: Are there unnecessary re-renders, expensive loops, or memory leaks?

### 3. UI/UX Design Review (`/gstack design`)
Evaluate frontend interface & aesthetics against premium web standards:
- **Visual Distinction**: Does the interface look custom, intentional, and high-end (not default/templated)?
- **Typography & Color Hierarchy**: Are curated Google Fonts, dark mode themes, and smooth gradients applied?
- **Interactive Polish**: Are subtle hover states, micro-animations, and smooth transitions active?
- **Responsive Layout**: Is the design responsive across Mobile, Tablet, Desktop, and Ultrawide?

### 4. Browser QA Audit (`/gstack qa`)
Physically verify built web applications:
- Launch headless browser validation via Playwright / DevTools.
- Verify console logs for 0 JavaScript errors or unhandled warnings.
- Capture responsive screenshots across 5 viewports (Mobile 375px, Mobile 414px, Tablet 768px, Laptop 1024px, Desktop 1440px).

### 5. Full Executive Council Review (`/gstack full` or `/gstack`)
Run an end-to-end multi-role sweep across all 4 perspectives before shipping major features:
1. **CEO Gate**: Approve product scope & user value.
2. **EM Gate**: Verify architecture & surgical code changes.
3. **Design Gate**: Audit aesthetics & UX responsiveness.
4. **QA Gate**: Run automated browser testing & screenshot audit.

---

## Execution Workflow
When `/gstack` is triggered:
1. Identify the target file, plan, or workspace folder.
2. Synthesize feedback per requested role (`CEO`, `ENG`, `DESIGN`, `QA`, or `FULL`).
3. Output a structured **GStack Executive Report** highlighting:
   - **Green Lights (What to Keep)**
   - **Red Flags (Critical Fixes)**
   - **Recommended Actions**
