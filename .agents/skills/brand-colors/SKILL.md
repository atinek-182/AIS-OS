---
name: brand-colors
description: Automate brand color palette exploration, WCAG contrast audits, and swatch prototype page creation.
argument-hint: "[optional action or theme context]"
---

# Brand Colors & Contrast Audit Skill

This skill automates the exploration, generation, and verification of color palettes for the Zorixel brand to ensure high legibility and compliance with visual design guidelines.

## Capabilities

When this skill is invoked via `/brand-colors` or triggered:

1. **Color Generator Engine**:
   - Generates candidate palettes (Monochromatic, Analogous, Triadic, Contrast-Pairs) using color theory equations.
   - Outputs HSL and Hex codes along with color profiles.

2. **WCAG Legibility Verification (Playwright-based)**:
   - Evaluates the contrast ratio of text-to-background combinations on all page modules.
   - Flag any pairings that fail **WCAG 2.2 AA (4.5:1 ratio for normal text, 3:1 for large text)**.
   - Highlights contrast levels:
     - 🟢 **PASS AA (7.0+)** - Superb contrast.
     - 🟡 **PASS AA (4.5 - 6.9)** - Standard contrast.
     - 🔴 **FAIL (< 4.5)** - Low contrast warning.

3. **Interactive Swatch Prototypes**:
   - Compiles selected colors into a test page `swatches.html`.
   - Embeds sample buttons, card grids, paragraphs, and active headings (using the finalized `Rosehot` and `Outfit` fonts) to inspect colors under light and dark theme canvas views.

## Rendering Swatch Page Rules
- Theme Background Canvas: Light Warm Linen (`#fbfaf7`), Dark Charcoal (`#0c0d12`).
- Contrast Checkpoints: Check heading text, body copy, and CTA buttons.
- Design Rules: Avoid generic saturation (plain primary red/blue). Prefer curated, harmonious tones matching the Zorixel print editorial aesthetic.
