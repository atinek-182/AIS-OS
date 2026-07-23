# Global Rules & Design Conflict Resolution Guide

This reference outlines the unified design rules for Atinek Maurya's AIOS. It resolves contradictions between the global design skills (`impeccable` vs. `ui-ux-pro-max`) and Zorixel's custom brand identity.

---

## 1. Core Visual Priority & Easing Overrides

When generating User Interfaces, components, or slides, follow this hierarchy:
1. **Zorixel Brand Identity (Primary Override):** `MEMORY.md` guidelines take precedence over all standard styles.
2. **Impeccable Constraints (Secondary Override):** High-craft, editorial layout limitations.
3. **UI-UX Pro Max (General Fallback):** Interactive states, touch target sizes, forms, and charts.

---

## 2. Resolving Specific Design Conflicts

### A. Body Background & Colors
* **The Conflict:** `impeccable` bans warm cream/beige backgrounds (`--cream`, `--sand`) as a saturated AI default. `ui-ux-pro-max` lists warm neutrals as a common palette. Zorixel's committed identity is a warm linen off-white paper canvas background (`#fbfaf7`).
* **The Resolution:** Zorixel's brand canvas (`#fbfaf7` body bg, `#141413` charcoal text) is a **non-negotiable committed identity**. Use it. However, avoid standard "SaaS cream slop" by not layering cream cards on a cream background. Use pure white card sheets (`#ffffff`) with highly diffused, soft shadows (`box-shadow: 0 20px 48px rgba(20, 20, 19, 0.04)`) to separate content layers.

### B. Typography & Headers
* **The Conflict:** `ui-ux-pro-max` allows uppercase eyebrows above headings. `impeccable` bans small all-caps kickers ("PROCESS", "PRICING") and sequential number prefixes ("01", "02") as AI grammar.
* **The Resolution:** **DO NOT** use uppercase tracked eyebrows or sequential numbering prefixes on headings unless the section represents an actual ordered process or sequential timeline. Use clean, unbalanced editorial heading hierarchies (Title Case, `Rosehot` or display serif) and sentence-case prose.

### C. Glassmorphism & Gradients
* **The Conflict:** `ui-ux-pro-max` includes glassmorphism, claymorphism, and gradient text. `impeccable` bans gradient text and glassmorphism by default.
* **The Resolution:** **BANNED BY DEFAULT**. Never generate gradient text (`background-clip: text`) or glassmorphic blur panels unless explicitly requested by Atinek. Use clean solid colors, paper sheet elevations, and high-contrast styling.

### D. Motion & Animations
* **The Conflict:** `ui-ux-pro-max` allows bounce/elastic interactions. `impeccable` bans bounce/elastic animations, requiring exponential ease-out quart/quint/expo curves.
* **The Resolution:** For all layout transitions, sliding panels, and fade-reveals, use clean exponential ease-out curves (no bounce). Subtle spring/scale shrink states are allowed **only** for button press-states (micro-interactions).

---

## 3. Playwright Headless Verification Guidelines

To prevent regressions during visual audits:
1. **Relative Paths:** Ensure all node script packages (like playwright) resolve relative to the nearest active folder containing local `node_modules` instead of the execution CWD.
2. **Local HTTP Server:** Never load local `.html` files using the `file://` protocol. Always spin up `scripts/serve.js` dynamic server on `http://localhost:3000` to bypass sandbox restrictions.
3. **Base64 Font URIs:** Always embed brand typography (`Rosehot`, `Vixa`, `Outfit`) as base64 Data URIs inside temporary test files to guarantee fonts render correctly in Chromium screenshots.
4. **Viewport Sweeps:** Automatically audit visual layouts across all 5 responsive breakpoints (Mobile, Tablet, Small Desktop, Desktop, Ultra-wide).
