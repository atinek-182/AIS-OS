# 📸 Phase 6 Reference: Automated Playwright Visual QA & Verification

## 1. Automated Anti-Slop Audit Execution

Run the Hallmark runner script to execute automated static checks on the codebase:

```bash
python scripts/hallmark_runner.py
```

This verifies:
- Single accent color token usage across components.
- Eyebrow count restraint (max 1 per 3 sections).
- Pre-emit critique header presence.

---

## 2. Playwright Multi-Viewport Visual QA Sweep

Run the design verifier script to build the web project, launch Playwright, audit console errors, and capture screenshots across all 5 responsive viewports:

```bash
python scripts/verify_design_milestone.py
```

### The 5 Viewport Audit Suite:
1. **Desktop Large**: `1920px × 1080px` (Verifies max-container width, asymmetric grid math, single-line nav).
2. **Laptop Standard**: `1440px × 900px` (Verifies hero 100dvh fit and top padding).
3. **Tablet Portrait**: `768px × 1024px` (Verifies 2-col collapse and touch targets).
4. **Mobile Standard**: `375px × 812px` (Verifies single-column stack, mobile drawer nav, no horizontal scroll).
5. **Small Mobile**: `320px × 568px` (Verifies zero text truncation on ultra-small screens).

---

## 3. Console & Network Error Verification

Before declaring the website build complete:
1. Confirm **0 JavaScript console errors** in Playwright logs.
2. Confirm **0 broken 404 asset requests** (missing images, fonts, or icons).
3. Inspect generated screenshot PNGs in the test output directory to confirm visual alignment, typography contrast, and responsive layout integrity.
