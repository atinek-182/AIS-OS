---
name: jsmastery-scope
description: Project scoping and feature breakdown engine. Scopes complex project ideas into MVP milestones, user stories, tracer-bullet vertical slices, and actionable task tables. Triggered via /jsmastery-scope or naturally when scoping new features.
argument-hint: '[project_or_feature_idea]'
---

# JS Mastery Feature Scoping Engine (`/jsmastery-scope`)

## ⚡ Overview & Tri-Mode Routing

This skill converts high-level project ideas or complex feature requests into disciplined, structured scopes with clear MVP boundaries and vertical slices, derived from JS Mastery Pro workflows.

Invokable via:
- **Slash Command**: `/jsmastery-scope [idea_description]`
- **Dynamic Intent**: Triggered automatically when decomposing feature ideas or scoping new project releases.
- **Inter-Skill Calling**: Invoked by `/new-project`, `/website-design-engine`, `/jsmastery-architect`, and `/mattpocock-wayfinder`.

---

## 🎯 Scoping Discipline & Rules

1. **Tracer Bullet Slices**: Break work into thin end-to-end vertical slices (DB -> API -> UI -> Verification) rather than horizontal layer dumps.
2. **Strict MVP Discipline**: Separate core must-haves from nice-to-have bloat. Keep initial releases minimal and ship-ready.
3. **Scope Location**: Write scope files into `docs/scope/NNNN-[epic_slug].md` or `brain-aios/wiki/checklists/`.

---

## 📝 Scope File Format (`docs/scope/NNNN-[slug].md`)

```markdown
# Scope: [Epic / Feature Name]

## 🎯 High-Level Goal
Brief description of user outcome and business value.

## 🚀 Delivery Strategy
- **Approach**: Tracer Bullet / Skateboard / Facade / Journey
- **MVP Target Date**: [Target]

## 📑 Feature Breakdown Table

| ID | User Story | Delivery Slice | Dependencies | Status |
|---|---|---|---|---|
| US-01 | As a user, I want to sign up with email... | DB User Schema + Server Action + Auth UI | None | Proposed |
| US-02 | As a user, I want to view my dashboard... | Dashboard API + Card Components | US-01 | Proposed |

## 🚫 Out of Scope for MVP
Explicitly listed features deferred to Phase 2 to protect timeline and prevent bloat.

## 🛠️ Definition of Done (DoD)
- [ ] Automated tests pass
- [ ] TypeScript zero errors
- [ ] 5-viewport visual QA verified
```

---

## 🔗 Inter-Skill Connections & Handoff Pipeline
- **Upstream Spec Engine**: Receives build specs from **`/jsmastery-architect`** and **`/mattpocock-to-spec`**.
- **Downstream Ticket Engine**: Hands off task tables to **`/mattpocock-to-tickets`** to generate atomic developer tickets.
- **Macro Planning**: Feeds vertical slices into **`/mattpocock-wayfinder`**.
