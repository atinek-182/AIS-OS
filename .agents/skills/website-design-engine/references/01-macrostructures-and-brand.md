# 🏛️ Phase 1 Reference: Macrostructures, Token Extraction & Brand Systems

## 1. 21 Hallmark Macrostructure Archetypes

Select ONE macrostructure archetype that fits the brief's subject matter. Do not default to standard hero -> 3-column feature -> CTA:

1. **Asymmetric Editorial**: Off-center hero, wide display typography, generous whitespace, staggered content blocks.
2. **Bento Showcase**: Asymmetric grid tiles with varied cell spans, mixed media, and high-density visual storytelling.
3. **Fullscreen Canvas / WebGL Stage**: Interactive 3D/GLSL background canvas with floating minimalist UI controls.
4. **Split-Screen Studio**: 50/50 sticky split; left column pins narrative copy, right column scrolls interactive assets.
5. **Kinetic Type Focus**: Massive display typography as primary visual anchor, scroll-driven text scaling.
6. **Monolithic Hero**: Dominant single-focus image or video hero with micro-overlay controls and hidden drawer nav.
7. **Minimal Dock**: Floating pill navigation, ultra-airy layout, high-contrast typography, zero card borders.
8. **Broadside Newspaper**: Dense multi-column grid, hairline borders, mono captions, editorial precision.
9. **Horizontal Pan Showcase**: Vertical scroll hijacked to horizontal track for portfolio projects or product walkthroughs.
10. **Sticky Stack Narrative**: Card stack on scroll; cards stack and shrink as user scrolls vertically down the page.
11. **Dark Tech Terminal**: Monospace accents, neon status indicators, command palette UI, dense telemetry metrics.
12. **Bento Hero Integration**: Hero section itself is an integrated multi-tile bento grid containing live widgets.
13. **Editorial Magazine Split**: Serif/display typography, drop caps, multi-column articles, pull quotes, rich captions.
14. **Floating Glass Layers**: Layered frosted glass panels over ambient mesh/aurora background.
15. **Brutalist Grid**: Raw thick borders, sharp zero-radius containers, high-contrast monochrome, bold typography.
16. **Product Stage / 3D Viewer**: Centered 3D product interactive canvas with floating spec callouts.
17. **App-Native Showcase**: Floating phone/tablet mockup stage with live interactive component preview.
18. **Launch Manifesto**: Center-aligned typography-first narrative flow with subtle scroll reveals.
19. **Interactive Playground**: Integrated live controls (sliders, swatches, toggles) driving instant UI preview.
20. **Color Block Story**: Sequential full-viewport color block transitions on scroll.
21. **Asymmetric Gallery**: Staggered masonry layout for creative media, photography, or case studies.

---

## 2. Automated Design Token Extraction (`hallmark study` / `scrape-reference`)

When a reference URL or screenshot is provided during initial discovery:
1. **Extract Visual DNA**: Inspect reference styles to capture the primary color accent, background tone, font stack, and border radius.
2. **Generate Token Variables**: Automatically map findings into CSS custom properties in `index.css`:

```css
@theme {
  --color-bg-primary: oklch(0.14 0.01 260);
  --color-bg-surface: oklch(0.18 0.02 260);
  --color-border: oklch(0.25 0.02 260);
  --color-text-main: oklch(0.95 0.01 260);
  --color-text-muted: oklch(0.65 0.02 260);
  --color-accent: oklch(0.65 0.22 140); /* Emerald Pop */
  --font-logo: "Nuqun", sans-serif;
  --font-display: "Rosehot", sans-serif;
  --font-body: "Outfit", sans-serif;
  --font-mono: "Geist Mono", monospace;
}
```

---

## 3. Brand Typography Discipline

- **Nuqun**: Signature brandmark logo typeface.
- **Rosehot**: Display typography for hero headlines, major titles, and section headers.
- **Outfit**: Body text for paragraphs, feature descriptions, and UI labels.
- **Geist Mono / JetBrains Mono**: Monospace font for telemetry, metrics, code, and structural tags.

### Typography Rules:
- **Hero Headline**: `text-4xl md:text-6xl lg:text-7xl tracking-tighter leading-none`.
- **Body Paragraphs**: `text-base text-zinc-400 leading-relaxed max-w-[65ch]`.
- **No Mixed-Family Emphasis**: Use italic/bold of the SAME font family for emphasis. Never inject a random serif word into a sans headline.
- **Italic Descender Clearance**: When italic display text contains `y g j p q`, set minimum `leading-[1.1]` and `pb-1` to prevent clipping.

---

## 4. OKLCH Color Math & AI Slop Ban

Always use locked CSS OKLCH tokens. Max 1 accent color per page.

### ⛔ BANNED AI SLOP GRADIENTS & STEREOTYPES:
- **BANNED**: Generic purple/blue gradient backgrounds (`bg-gradient-to-r from-purple-500 to-indigo-600` or `#8b5cf6` glows over `#09090b`).
- **BANNED**: Floating blurred color blobs (`blur-3xl opacity-30 bg-purple-500`).
- **BANNED**: Fake invented statistics cards ("+47% conversion", "50,000+ teams").
- **BANNED**: Un-tokenized raw Hex strings in inline styles.

### Rotational OKLCH Palette Families:
1. **Pure Dark Pop**: Off-black (`oklch(0.12 0.01 260)`) + stark white + 1 Emerald or Cyan accent.
2. **Cold Luxury**: Silver-grey (`oklch(0.92 0.005 240)`) + smoke + chrome accent.
3. **Forest Studio**: Deep forest (`oklch(0.20 0.04 150)`) + bone + amber accent.
4. **Cobalt + Cream**: Deep saturated cobalt pop against cool neutral.
5. **Slate + Terracotta**: Rust accent against slate-grey structure.
