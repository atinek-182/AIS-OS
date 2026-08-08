---
title: 'Phase 5 Reference: Anti-Slop Quality Gates, Security & Fullstack Audits (v4.0)'
domain: skill
summary: 'Before finalizing frontend output, score the page across 6 design axes (1-5 scale) and stamp a CSS critique header
  at the top of the stylesheet or root component: /* Hallmark · pre-emit critique: P5 H4 E5 S4 R5 V5 */'
critical_directives:
- 'Gate #58 (Boxy Grid Container Ban):** Never default to sharp 90-degree 1px square grid containers (`rounded-none`). Alwa'
- 'Gate #60 (Nuqun Logo Rule):** Always render the official `Nuqun` font vector logo mark (`zorixel`) in navigation headers'
- 'Gate #61 (Lenis + GSAP Requirement):** Web applications MUST integrate `Lenis` smooth inertia scroll + `GSAP ScrollTrigg'
- 'Gate #62 (Animated Accordion Rule):** FAQ accordions MUST use Motion/React `AnimatePresence` for smooth height expansion'
section_outline:
- 'Phase 5 Reference: Anti-Slop Quality Gates, Security & Fullstack Audits (v4.0)'
- Hallmark Pre-Emit Critique Stamp
- Fullstack Code Quality Audit (`/jsmastery-audit`)
- Technical SEO & GEO (Generative Engine Optimization) Engine
- Vibesec Security Hygiene & WCAG AA Accessibility
read_triggers:
- When working on skill in .agents/skills/website-design-engine/references/05-anti-slop-quality-gates.md
- 'When reading context for Phase 5 Reference: Anti-Slop Quality Gates, Security & Fullstack Audits (v4.0)'
tags:
- skill
- 05-anti-slop-quality-gates
updated: '2026-08-08'
---

# Phase 5 Reference: Anti-Slop Quality Gates, Security & Fullstack Audits (v4.0)

## Hallmark Pre-Emit Critique Stamp

Before finalizing frontend output, score the page across 6 design axes (1-5 scale) and stamp a CSS critique header at the top of the stylesheet or root component:

```css
/* Hallmark · pre-emit critique: P5 H4 E5 S4 R5 V5 */
```

- **P (Philosophy)**: Is there a clear, un-templated visual identity tailored specifically to this brief?
- **H (Hierarchy)**: Is the visual hierarchy clear with zero competing hero CTAs?
- **E (Execution)**: Is the code clean, responsive down to 320px, with clean selector specificity?
- **S (Specificity)**: Are colors, fonts, and grid measurements locked to design tokens?
- **R (Restraint)**: Is boldness spent in ONE signature place, avoiding scattered decorative clutter?
- **V (Variety)**: Does the section layout structure avoid repetitive 3-col card patterns?

---

## Fullstack Code Quality Audit (`/jsmastery-audit`)

Run `/jsmastery-audit` to verify 6 mandatory code gates:

1. **Next.js 15 App Router Async Params**: Route `params` and `searchParams` MUST be awaited (`const { id } = await params`). Never dereference params synchronously.
2. **Server Action Input Validation (Zod)**: All Server Actions and public form handlers MUST use Zod schema validation before processing data.
3. **Strict TypeScript Types**: Zero `any` types across all component props, state objects, and API handlers.
4. **Environment Secret Hygiene**: Never expose private API keys (`ANTHROPIC_API_KEY`, `SUPABASE_SERVICE_ROLE_KEY`) in client bundles.
5. **Error Boundaries & Fallbacks**: Provide `error.tsx`, `loading.tsx`, and `not-found.tsx` boundaries for all routes.
6. **Tailwind CSS v4 Standard**: Use CSS `@theme` directives instead of legacy Tailwind v3 `@apply` or `tailwind.config.js` blocks.

---

## Technical SEO & GEO (Generative Engine Optimization) Engine

1. **Semantic Heading Hierarchy**: Strictly ONE `<h1>` tag per page (the primary hero headline). Sub-sections use `<h2>`, and sub-cards use `<h3>`.
2. **JSON-LD Schema Markup**: Inject dynamic structured data in `<head>` (WebSite, Organization, Product).
3. **Canonical & Social Meta Tags**: Canonical `<link rel="canonical" href="...">`, OpenGraph (`og:title`, `og:image`, `og:description`), and Twitter Card tags.
4. **Crawl Infrastructure**: Generate dynamic `sitemap.xml` listing all sitemap routes and `robots.txt` disallowing sensitive endpoints.

---

## Vibesec Security Hygiene & WCAG AA Accessibility

1. **XSS Prevention**: Never use `dangerouslySetInnerHTML` with un-sanitized user input. Use DOMPurify if HTML rendering is required.
2. **External Link Safety**: All external links (`target="_blank"`) MUST include `rel="noopener noreferrer"`.
3. **WCAG AA Contrast**: Normal text minimum `4.5:1` contrast ratio; large text (18px+ bold or 24px+) minimum `3:1`.
4. **Keyboard Focus Rings**: Never remove focus rings (`outline-none`). Provide visible 2px-4px focus indicators (`focus-visible:ring-2`).

---

## User-Enforced Anti-Slop Quality Gates (#58-#63)

- **Gate #58 (Boxy Grid Container Ban):** Never default to sharp 90-degree 1px square grid containers (`rounded-none`). Always use organic rounded cards (`rounded-3xl` / `rounded-2xl`) or fluid full-bleed tracks.
- **Gate #59 (Gradient Text & Purple Blob Ban):** Strictly ban multi-color gradient text masks (`bg-gradient-to-r text-transparent`) and generic purple background glows (`blur-3xl bg-purple-500`). Use solid, high-contrast OKLCH colors.
- **Gate #60 (Nuqun Logo Rule):** Always render the official `Nuqun` font vector logo mark (`zorixel`) in navigation headers and footers.
- **Gate #61 (Lenis + GSAP Requirement):** Web applications MUST integrate `Lenis` smooth inertia scroll + `GSAP ScrollTrigger` for pinned narratives when Motion Dial > 4.
- **Gate #62 (Animated Accordion Rule):** FAQ accordions MUST use Motion/React `AnimatePresence` for smooth height expansion (`height: "auto"`) instead of static toggle blocks.
- **Gate #63 (Zero Fake Metrics Rule):** Never invent fake metrics or social proof cards ("+47% conversion", "50,000+ teams"). Use real user testimonials or product screenshots instead.
