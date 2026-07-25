# 🛡️ Phase 5 Reference: Anti-Slop Quality Gates & Accessibility

## 1. Hallmark Pre-Emit Critique Stamp

Before finalizing any frontend output, score the generated page across 6 design axes (1-5 scale) and stamp a CSS pre-emit critique header at the top of the main stylesheet or root component:

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

## 2. Dieter Rams 10 Principles Audit (`design-is`)

1. **Innovative**: Advances the visual form without imitating competitors wholesale.
2. **Useful**: Serves the user's primary task without decoy interactions or detours.
3. **Aesthetic**: Spacing, type, and color follow a single visible, harmonious system.
4. **Understandable**: Controls and structure are self-explanatory; zero confusing jargon.
5. **Unobtrusive**: UI chrome recedes; content is figure, interface is ground.
6. **Honest**: No deceptive dark patterns, fake countdowns, or inflated claims.
7. **Long-lasting**: Avoids fleeting design trends (no skeuomorphic residue or random fads).
8. **Thorough**: Empty, loading, error, success, focus, and disabled states are all explicitly handled.
9. **Environmentally Friendly**: Zero layout thrashing, optimized asset weight, respects reduced motion.
10. **As Little Design as Possible**: Concentrates on essentials; removes unnecessary decorative clutter.

---

## 3. Vercel Web Interface Guidelines & Accessibility

- **WCAG AA Contrast**: Normal text minimum `4.5:1` contrast ratio; large text (18px+ bold or 24px+) minimum `3:1`.
- **Keyboard Focus Rings**: Never remove focus rings (`outline-none`). Provide visible 2px-4px focus indicators on all interactive elements (`focus-visible:ring-2`).
- **Form Input Labels**: Every form input MUST have an associated `<label>` or `aria-label`. Placeholders as labels are BANNED.
- **Alt Text**: Every image MUST contain descriptive `alt` text. Decorative icons get `aria-hidden="true"`.
- **Skip Links**: Include a "Skip to main content" link for keyboard navigation users.

---

## 4. Vibesec Security Hygiene

1. **XSS Prevention**: Never use `dangerouslySetInnerHTML` with un-sanitized user input. Use DOMPurify if HTML rendering is required.
2. **External Link Safety**: All external links (`target="_blank"`) MUST include `rel="noopener noreferrer"`.
3. **API Key Hygiene**: Never hardcode API keys or secret tokens in client-side code. Use server-side env variables (`process.env`).

---

## 5. User-Enforced Anti-Slop Quality Gates (#58-#62)

- **Gate #58 (Boxy Grid Container Ban):** Never default to sharp 90-degree 1px square grid containers (`rounded-none`). Always use organic rounded cards (`rounded-3xl` / `rounded-2xl`) or fluid full-bleed tracks with generous whitespace.
- **Gate #59 (Gradient Text Ban):** Strictly ban multi-color gradient text masks (`bg-gradient-to-r text-transparent`). Use solid, high-contrast OKLCH/HSL colors.
- **Gate #60 (Nuqun Logo Rule):** Always render the official `Nuqun` font vector logo mark (`zorixel`) in navigation headers and footers.
- **Gate #61 (Lenis + GSAP Requirement):** Web applications MUST integrate `Lenis` smooth inertia scroll + `GSAP ScrollTrigger` for pinned narratives and kinetic text reveals.
- **Gate #62 (Animated Accordion Rule):** FAQ accordions MUST use Motion/React `AnimatePresence` for smooth height expansion (`height: "auto"`) instead of static toggle blocks.
