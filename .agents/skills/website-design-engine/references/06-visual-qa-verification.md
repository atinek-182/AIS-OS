# 📸 Phase 6 Reference: Automated Playwright Visual QA & Verification

## 1. Pre-Emit Anti-Slop Audit Execution

Run the Hallmark runner script to execute static checks on the codebase:

```bash
python scripts/hallmark_runner.py
```

This verifies:
- Single accent color OKLCH token usage across components.
- Eyebrow count restraint (max 1 per 3 sections).
- Pre-emit critique header presence (`/* Hallmark · pre-emit critique... */`).

---

## 2. Playwright Multi-Viewport Visual QA Sweep

Run the design verifier script to launch Playwright, audit live console logs, and capture screenshots across all 5 responsive viewports:

```bash
python scripts/verify_design_milestone.py
```

### The 5 Viewport Audit Suite:
1. **Desktop Large**: `1920px × 1080px` (Verifies max-container width, asymmetric grid math, single-line navbar).
2. **Laptop Standard**: `1440px × 900px` (Verifies hero 100dvh fit and top padding).
3. **Tablet Portrait**: `768px × 1024px` (Verifies 2-col collapse and touch targets).
4. **Mobile Standard**: `375px × 812px` (Verifies single-column stack, mobile drawer nav, zero horizontal scrollbar overflow).
5. **Small Mobile**: `320px × 568px` (Verifies zero text truncation on ultra-small screens).

---

## 3. Zero-Tolerance Console & Layout Verification Rules

Before declaring any website build complete:
1. **0 JavaScript Console Errors**: Confirm 0 runtime errors or unhandled exceptions in Playwright browser logs.
2. **0 Broken 404 Asset Requests**: Confirm all fonts, images, and video assets return HTTP 200/304.
3. **0 Horizontal Scroll Overflow**: Confirm `document.documentElement.scrollWidth <= window.innerWidth` across all 5 viewports.
4. **Cap Auto-Fix Retries**: If visual or console errors are detected, run up to **2 automated fix passes**. If errors persist after 2 passes, present specific visual screenshots and recommendations to the user instead of looping infinitely.
