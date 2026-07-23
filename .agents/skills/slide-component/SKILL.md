---
name: slide-component
description: This skill should be used when the user asks to "generate slide component", "inject animated block", "create slide element", or "add custom component to library". Handles block-injection, compounding libraries, and Playwright verification.
version: 1.0.0
---

# Slide Component Generator

Generate standalone, highly-animated HTML/CSS/JS components and inject them into slide decks, while maintaining a self-optimizing, compounded personal component library.

## Core Principles

1. **Vanilla HTML/CSS/JS Only** — All components must be zero-dependency. Do not use React, Framer Motion, or external bundles. Use pure CSS keyframes, SVGs, and Vanilla JS.
2. **Animation with Purpose** — Prioritize smooth, tasteful micro-interactions and reveals (using `transition` and `@keyframes`) that explain the topic, avoiding distracting layout jitter.
3. **Compound Curated Library** — Save every unique component to the central library. Compare new versions against existing ones, and prompt the user before discarding or archiving older versions.
4. **Automated and Manual Gates** — Verify every component visually via Playwright before asking the user for final approval to write to the slide file.

---

## Operating Instructions

### Step 1: Identify Category & Copy

When a component is requested, identify its target category and layout style:

* **Bento Grids**: Multi-panel modular layouts displaying features, stats, or logs.
* **Token Streams**: Flowing data/particle nodes representing processing pipelines.
* **Perspective Grids**: 3D wireframe canvas grids or matrix overlays.
* **Animated Charts**: Interactive line, bar, or pie charts with entrance transitions.
* **Interactive Terminals**: Mock shell/editor windows with typed script simulations.
* **Agent Loops**: Cyclic state transitions with pulsing nodes.

---

### Step 2: Generate Code Block

Draft the component HTML, CSS, and JS. Use CSS variables to inherit the presentation's styling context.

* **Layout Constraints**: Design components to fill their target grid cell or slide container. Do not enforce a rigid 16:9 canvas on the component level; make them layout-flexible.
* **Transitions**: Use CSS keyframe animations triggered by the slide's active visibility class (e.g. `.slide.visible .reveal-item`).
* **Visuals**: Use SVG elements for custom paths, badges, and illustrations.

---

### Step 3: Run Playwright Verification

Before presenting the component to the user, run the automated verification script:

```powershell
python scripts/verify-component.py <path-to-temp-component.html>
```

The script will:
1. Load the component in a headless Playwright instance.
2. Verify that there are no console errors or styling leaks.
3. Capture a PNG screenshot and save it to the `.slide-component/previews/` directory.

---

### Step 4: Compounding Library & User Gate

1. Scan the vault directory `d:\Brain For my AIOS\wiki\research\skills-library\slide-components\<category>\` to see if a similar component exists.
2. Compare the new code and layout against the existing files.
3. Prompt the user with the Playwright screenshot:
   *"I generated a new [Category] component. Here is the visual preview. Compared to the previous library version, this one adds [features/style]. Would you like to save it to your library and set it as the primary template? (This will archive the old file on approval)."*
4. On approval, save the code to the vault library folder.

---

### Step 5: Slide Block-Injection

Surgically inject the approved HTML/CSS/JS block into the target slide container:

1. Open the target HTML slide deck.
2. Locate the specific slide section (e.g., `<section class="slide" id="slide-3">`).
3. Replace the placeholder container or append the compiled component block inside the slide's `.slide-content` wrapper.
4. Verify the full presentation loads correctly without text overlaps or viewport scroll overflows.
