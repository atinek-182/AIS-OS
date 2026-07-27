---
name: mattpocock-domain-modeling
description: TypeScript domain modeling and ubiquitous language engine. Sharpen domain terms, define discriminated unions, prevent domain ambiguity, and record Architectural Decision Records (ADRs). Triggered via /mattpocock-domain-modeling or naturally when modeling domain types.
argument-hint: '[domain_concept_or_feature]'
---

# Matt Pocock TypeScript Domain Modeling Engine (`/mattpocock-domain-modeling`)

## ⚡ Overview & Tri-Mode Routing

This skill provides TypeScript-driven domain modeling, ubiquitous language sharpening, and Architectural Decision Record (ADR) management, directly adapted from Matt Pocock's engineering practices.

Invokable via:
- **Slash Command**: `/mattpocock-domain-modeling [concept]`
- **Dynamic Intent**: Triggered automatically when defining complex TypeScript types, domain models, or pinning down project vocabulary.
- **Inter-Skill Calling**: Invoked by `/grill-me`, `/mattpocock-wayfinder`, `/mattpocock-to-spec`, `/jsmastery-architect`, and `/new-project`.

---

## 🧠 Domain Modeling Principles

### 1. Challenge Against Glossary (`CONTEXT.md`)
When domain terms are ambiguous or conflicting, challenge them immediately:
> *"Your glossary defines 'Subscription' as an active billing cycle, but you seem to mean 'License' — which one is it?"*

### 2. Type-Driven Domain Design
Model domain concepts using strong, self-documenting TypeScript constructs:
- **Discriminated Unions**: Represent exclusive states unambiguously (e.g. `{ status: 'idle' } | { status: 'loading' } | { status: 'success'; data: T } | { status: 'error'; error: Error }`).
- **Branded Types**: Prevent primitive obsession (e.g. `type UserId = string & { readonly __brand: unique symbol }`).
- **Zero `any` / Zero Loose Strings**: Replace raw strings with strict string literals or enums.

### 3. Concrete Edge-Case Scenario Testing
Invent probing edge cases to stress-test relationships before writing code:
> *"What happens if a user cancels mid-billing cycle while a payment is pending?"*

### 4. Inline `CONTEXT.md` Glossary Maintenance
Maintain a crisp, implementation-devoid glossary in `CONTEXT.md`. Do not pollute it with implementation details or code snippets.

### 5. Selective ADR Generation
Create Architectural Decision Records (`docs/adr/0001-title.md`) ONLY when ALL 3 conditions are met:
1. **Hard to reverse** (High cost of changing mind later).
2. **Surprising without context** (Future engineers will wonder "why?").
3. **Result of a real trade-off** (Genuine alternatives were evaluated and rejected).

---

## 🔗 Inter-Skill Connections & Handoff Pipeline
- **Discovery Engine**: Called during Phase 0 discovery by **`/grill-me`**.
- **Macro Planning**: Used by **`/mattpocock-wayfinder`** to name destinations and resolve ticket vocabularies.
- **Spec Compilation**: Feeds type definitions into **`/mattpocock-to-spec`** and **`/jsmastery-architect`**.
- **Code Audit**: Audited during release checks by **`/jsmastery-audit`**.
