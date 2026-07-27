---
name: jsmastery-audit
description: Fullstack JavaScript and Next.js App Router code auditor. Audits server actions, API routes, security boundaries, performance, rendering patterns, and type-safety. Triggered via /jsmastery-audit or naturally when auditing JS/TS codebases.
argument-hint: '[target_dir_or_file]'
---

# JS Mastery Fullstack Code Auditor (`/jsmastery-audit`)

## ⚡ Overview & Tri-Mode Routing

This skill performs comprehensive static and architectural audits on fullstack JavaScript, TypeScript, and Next.js applications, following JS Mastery Pro standards.

Invokable via:
- **Slash Command**: `/jsmastery-audit [path]`
- **Dynamic Intent**: Triggered automatically when auditing JavaScript/TypeScript code, Next.js projects, or checking code quality before release.
- **Inter-Skill Calling**: Invoked by `/verify-design`, `/website-design-engine`, `/vibesec`, `/gstack`, and `ingest-repo`.

---

## 🔍 The 6 Audit Gates

### 1. Next.js App Router & Server/Client Boundary Gate
- Verify `'use client'` is only used where client interactivity (state, hooks, DOM listeners) is required.
- Ensure sensitive logic, secret tokens, and DB queries never leak to client components.
- Check Server Action security: validate inputs with Zod and enforce authentication/authorization inside every action.

### 2. TypeScript & Type-Safety Gate
- Enforce strict type safety: zero `any` types allowed.
- Verify interface and type declarations for component props, API payloads, and database models (`/mattpocock-domain-modeling`).
- Ensure async functions have explicit return types where beneficial.

### 3. Security & Vulnerability Gate (Vibesec Alignment)
- Check environment variable hygiene: ensure private keys lack `NEXT_PUBLIC_` prefixes.
- Audit against SQL injection, XSS (`dangerouslySetInnerHTML`), and IDOR vulnerabilities (`/vibesec`).
- Ensure HTTP-only secure cookies are used for session tokens.

### 4. Performance & Caching Gate
- Verify route segment configs (`revalidate`, `dynamic`, `fetchCache`).
- Audit image optimization (`next/image`), font loading (`next/font`), and bundle size.
- Ensure expensive computations are memoized (`useMemo`, `useCallback`, `React.cache`).

### 5. UI/UX & Responsive Design Gate
- Ensure clean semantic HTML structure (`<main>`, `<nav>`, `<header>`, `<article>`).
- Verify Tailwind CSS or custom CSS responsiveness across 5 viewports (320px to 1920px).
- Audit accessibility (WCAG AA color contrast, ARIA labels, keyboard focus) and Hallmark anti-slop rules (`/hallmark`).

### 6. Error Handling & Resilience Gate
- Ensure `error.tsx` and `not-found.tsx` boundaries exist for key route segments.
- Check try/catch blocks in API routes and server actions with structured error logging.

---

## 📊 Output Audit Report Format

Generate a Markdown audit report containing:
1. **Executive Summary & Overall Health Score (0-100)**
2. **Critical Security & Architecture Violations (Must Fix)**
3. **Performance & Type Safety Warnings (Should Fix)**
4. **Recommended Action Plan**

---

## 🔗 Inter-Skill Connections & Handoff Pipeline
- **Visual & Console Verification**: Runs as Phase 5 in **`/website-design-engine`** and Step 1 in **`/verify-design`**.
- **Security Scans**: Aligns with **`/vibesec`**.
- **Anti-Slop QA**: Pairs with `python scripts/hallmark_runner.py audit <path>`.
- **Type Safety**: Aligns with **`/mattpocock-domain-modeling`**.
