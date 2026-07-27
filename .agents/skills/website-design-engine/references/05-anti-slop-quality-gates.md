# 🛡️ Phase 5 Reference: Anti-Slop Quality Gates, SEO/GEO & Security

## 1. Hallmark Pre-Emit Critique Stamp

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

## 2. Technical SEO & GEO (Generative Engine Optimization) Engine

Every generated page MUST adhere to strict technical search engine and generative engine optimization standards:

1. **Semantic Heading Hierarchy**: Strictly ONE `<h1>` tag per page (the primary hero headline). Sub-sections use `<h2>`, and sub-cards use `<h3>`.
2. **JSON-LD Schema Markup**: Inject dynamic structured data in `<head>`:
   ```html
   <script type="application/ld+json">
   {
     "@context": "https://schema.org",
     "@type": "WebSite",
     "name": "Project Name",
     "url": "https://example.com",
     "description": "Page meta description"
   }
   </script>
   ```
3. **Canonical & Social Meta Tags**: Canonical `<link rel="canonical" href="...">`, OpenGraph (`og:title`, `og:image`, `og:description`), and Twitter Card tags.
4. **Crawl Infrastructure**: Generate dynamic `sitemap.xml` listing all sitemap routes and `robots.txt` disallowing sensitive endpoints.

---

## 3. Vibesec Security Hygiene & WCAG AA Accessibility

1. **XSS Prevention**: Never use `dangerouslySetInnerHTML` with un-sanitized user input. Use DOMPurify if HTML rendering is required.
2. **External Link Safety**: All external links (`target="_blank"`) MUST include `rel="noopener noreferrer"`.
3. **API Key Hygiene**: Never hardcode API keys or secret tokens in client-side code.
4. **WCAG AA Contrast**: Normal text minimum `4.5:1` contrast ratio; large text (18px+ bold or 24px+) minimum `3:1`.
5. **Keyboard Focus Rings**: Never remove focus rings (`outline-none`). Provide visible 2px-4px focus indicators (`focus-visible:ring-2`).

---

## 4. User-Enforced Anti-Slop Quality Gates (#58-#63)

- **Gate #58 (Boxy Grid Container Ban):** Never default to sharp 90-degree 1px square grid containers (`rounded-none`). Always use organic rounded cards (`rounded-3xl` / `rounded-2xl`) or fluid full-bleed tracks.
- **Gate #59 (Gradient Text & Purple Blob Ban):** Strictly ban multi-color gradient text masks (`bg-gradient-to-r text-transparent`) and generic purple background glows (`blur-3xl bg-purple-500`). Use solid, high-contrast OKLCH colors.
- **Gate #60 (Nuqun Logo Rule):** Always render the official `Nuqun` font vector logo mark (`zorixel`) in navigation headers and footers.
- **Gate #61 (Lenis + GSAP Requirement):** Web applications MUST integrate `Lenis` smooth inertia scroll + `GSAP ScrollTrigger` for pinned narratives when Motion Dial > 4.
- **Gate #62 (Animated Accordion Rule):** FAQ accordions MUST use Motion/React `AnimatePresence` for smooth height expansion (`height: "auto"`) instead of static toggle blocks.
- **Gate #63 (Zero Fake Metrics Rule):** Never invent fake metrics or social proof cards ("+47% conversion", "50,000+ teams"). Use real user testimonials or product screenshots instead.
