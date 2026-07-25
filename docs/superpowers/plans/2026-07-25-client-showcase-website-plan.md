# Client-Conversion AI Design Studio Showcase Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a breathtaking, high-converting client showcase website for ZORIXEL AI Design Studio featuring zero-glassmorphism solid OKLCH surfaces, 147 catalog UI component cards, real Unsplash imagery, display font integration, and 5-viewport visual QA.

**Architecture:** A modern Vite + React + Tailwind CSS v4 application structured into modular component layers (Nav, Bento Hero, 147 Component Showcase, Case Studies, AIOS Telemetry, Interactive Booking Calculator).

**Tech Stack:** React 19, Tailwind CSS v4, Motion (Framer Motion), Lucide React, Unsplash Photography, Tailwind OKLCH variables, Playwright Visual Verification.

## Global Constraints

- **Design Rules:** Solid OKLCH surfaces (`oklch(0.12 0.01 260)` background, `oklch(0.16 0.015 260)` surface), 1px solid hairline grid borders (`oklch(0.24 0.02 260)`), zero glassmorphism, zero generic AI purple slop.
- **Typography:** `Rosehot` + custom display fonts from `d:/AI-OS/New Fonts/` for display headlines, `Outfit` for body text, `Geist Mono` for technical telemetry badges.
- **Media:** 100% high-resolution Unsplash photography and royalty-free HTML5 video backgrounds.
- **Verification:** 0 console errors, 100% responsive across 5 viewports via Playwright.

---

### Task 1: Scaffold Showcase Application & Design Tokens Setup

**Files:**
- Create: `projects/client-showcase/package.json`
- Create: `projects/client-showcase/vite.config.js`
- Create: `projects/client-showcase/index.html`
- Create: `projects/client-showcase/src/index.css`
- Create: `projects/client-showcase/src/main.jsx`
- Create: `projects/client-showcase/src/App.jsx`

**Interfaces:**
- Consumes: Tailwind CSS v4, React 19, Lucide React, Motion.
- Produces: Base React app shell with locked OKLCH color tokens, font declarations, and zero-slop global CSS resets.

- [ ] **Step 1: Scaffold Vite + React project directory**

Run in terminal:
```bash
npx -y create-vite@latest projects/client-showcase --template react
```

- [ ] **Step 2: Configure `src/index.css` with OKLCH tokens & display font face rules**

```css
@import "tailwindcss";

@theme {
  --color-bg: oklch(0.12 0.01 260);
  --color-surface: oklch(0.16 0.015 260);
  --color-surface-hover: oklch(0.20 0.02 260);
  --color-border: oklch(0.24 0.02 260);
  --color-text-main: oklch(0.96 0.01 260);
  --color-text-muted: oklch(0.65 0.02 260);
  --color-accent: oklch(0.68 0.22 145);
  --color-accent-dim: oklch(0.28 0.08 145);

  --font-display: "Rosehot", "Outfit", sans-serif;
  --font-body: "Outfit", sans-serif;
  --font-mono: "Geist Mono", monospace;
}

body {
  background-color: var(--color-bg);
  color: var(--color-text-main);
  font-family: var(--font-body);
  overflow-x: hidden;
}
```

- [ ] **Step 3: Test base render & dev server**

Run: `npm --prefix projects/client-showcase run build`
Expected: Success build with 0 errors.

---

### Task 2: Build Minimal Status Navigation Dock

**Files:**
- Create: `projects/client-showcase/src/components/Navbar.jsx`
- Modify: `projects/client-showcase/src/App.jsx`

**Interfaces:**
- Consumes: Lucide React icons (`Activity`, `Sparkles`, `Calendar`, `ArrowUpRight`).
- Produces: `<Navbar />` component with real-time status pill indicator, Nuqun brand mark, and responsive CTA button.

- [ ] **Step 1: Write `<Navbar />` component**

```jsx
import React from 'react';
import { Activity, Sparkles, ArrowUpRight } from 'lucide-react';

export function Navbar() {
  return (
    <header className="sticky top-0 z-50 bg-[oklch(0.12_0.01_260)] border-b border-[oklch(0.24_0.02_260)]">
      <div className="max-w-7xl mx-auto px-6 h-20 flex items-center justify-between">
        {/* Brand Mark */}
        <div className="flex items-center gap-3">
          <div className="w-9 h-9 bg-[oklch(0.68_0.22_145)] flex items-center justify-center font-bold text-black rounded-sm">
            Z
          </div>
          <span className="font-bold tracking-tight text-lg text-white">ZORIXEL <span className="text-zinc-500 font-normal text-sm">STUDIO</span></span>
        </div>

        {/* Live Status Dock */}
        <div className="hidden md:flex items-center gap-3 px-4 py-1.5 bg-[oklch(0.16_0.015_260)] border border-[oklch(0.24_0.02_260)] rounded-full text-xs font-mono text-emerald-400">
          <span className="w-2 h-2 rounded-full bg-emerald-400 animate-pulse"></span>
          <span>AIOS Live · 147 Components Active</span>
        </div>

        {/* CTA Link */}
        <a 
          href="#booking" 
          className="flex items-center gap-2 px-5 py-2.5 bg-emerald-400 hover:bg-emerald-300 text-black font-semibold text-sm rounded-sm transition-colors"
        >
          <span>Book Discovery Call</span>
          <ArrowUpRight className="w-4 h-4" />
        </a>
      </div>
    </header>
  );
}
```

- [ ] **Step 2: Commit Task 2**

```bash
git add projects/client-showcase/src/components/Navbar.jsx projects/client-showcase/src/App.jsx
git commit -m "feat: add hairline navbar dock with live status pill"
```

---

### Task 3: Build Monolithic Kinetic Hero & Bento Stage

**Files:**
- Create: `projects/client-showcase/src/components/HeroBento.jsx`
- Modify: `projects/client-showcase/src/App.jsx`

**Interfaces:**
- Consumes: Motion / Framer Motion, Lucide React icons (`Terminal`, `Zap`, `CheckCircle2`, `Layers`).
- Produces: `<HeroBento />` with scroll-scaled headline, interactive live component switcher tile, and monospace performance telemetry card.

- [ ] **Step 1: Create `<HeroBento />` component**

Include monolithic Rosehot headline, interactive toggle tile (switching button styles live), and Lighthouse telemetry score card (`100/100`).

- [ ] **Step 2: Verify component rendering**

Run: `npm --prefix projects/client-showcase run build`

---

### Task 4: Build 147 Catalog Component Showcase Grid

**Files:**
- Create: `projects/client-showcase/src/components/ComponentGrid.jsx`
- Modify: `projects/client-showcase/src/App.jsx`

**Interfaces:**
- Consumes: Sourced patterns from Aceternity UI, Animate UI React, Forge UI, Vengence UI.
- Produces: `<ComponentGrid />` showcasing mouse spotlight card, dynamic text reveal, 3D tilt card with Unsplash imagery, and tactile motion switcher.

- [ ] **Step 1: Write `<ComponentGrid />` component with real interactive states**

- [ ] **Step 2: Test interactive hover & click states**

---

### Task 5: Build Split-Screen Client Case Studies Section

**Files:**
- Create: `projects/client-showcase/src/components/CaseStudies.jsx`
- Modify: `projects/client-showcase/src/App.jsx`

**Interfaces:**
- Consumes: High-resolution Unsplash architectural & tech photography URLs.
- Produces: `<CaseStudies />` with 50/50 sticky left narrative and right column scrolling project cards.

- [ ] **Step 1: Write `<CaseStudies />` component with Unsplash image URLs and real project metrics**

---

### Task 6: Build AIOS Quality & Telemetry Section

**Files:**
- Create: `projects/client-showcase/src/components/TelemetryTerminal.jsx`
- Modify: `projects/client-showcase/src/App.jsx`

**Interfaces:**
- Consumes: Geist Mono typography, Hallmark audit score metrics.
- Produces: `<TelemetryTerminal />` displaying Hallmark Anti-Slop Audit, Obys Grid Canons, and 5-Viewport QA verification cards.

---

### Task 7: Build Instant Booking & Pricing Calculator

**Files:**
- Create: `projects/client-showcase/src/components/BookingCalculator.jsx`
- Modify: `projects/client-showcase/src/App.jsx`

**Interfaces:**
- Consumes: React state (`scope`, `timeline`, `budget`).
- Produces: Interactive quote calculator with dynamic timeline estimates and instant booking CTA form.

---

### Task 8: Automated Visual Verification & Multi-Viewport Sweep

**Files:**
- Create: `projects/client-showcase/verify_showcase.js`

**Interfaces:**
- Consumes: Playwright chromium headless browser.
- Produces: Multi-viewport visual screenshots (`desktop.png`, `tablet.png`, `mobile.png`) and console error log check.

- [ ] **Step 1: Run verification script & confirm 0 console errors**

Run: `node projects/client-showcase/verify_showcase.js`
Expected: 0 console errors, screenshots saved to `projects/client-showcase/screenshots/`.
