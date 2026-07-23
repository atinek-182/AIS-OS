---
name: verify-design
description: Automatically build the project, run Playwright console checks, and generate responsive screenshots at all 5 viewports. Use when completing a front-end milestone, verifying layouts, or saying "/verify-design".
---

# Verify Design Milestone

Automate the visual, responsive, and console QA checklists using Playwright.

## Use When
- You are ready to verify a front-end milestone (e.g. Hero, Subsections).
- You want to check for horizontal overflows or layout breakages.
- You want to ensure there are no unhandled JavaScript errors in the browser console.
- The user runs `/verify-design` or asks to "verify the current build".

## Steps

1. **Locate Target Directory & Resolve Playwright Environment**:
   - By default, use the current active project directory.
   - If not specified, look in the `projects/` subdirectories or workspace root.
   - **Playwright Context check**: Playwright Node scripts require the `playwright` module. Before executing Playwright, verify where `playwright` is installed (e.g. check local `node_modules` or parent folders). Always write or copy scripts to the nearest folder containing `playwright` in its dependencies, and execute them in that directory's context to prevent "module not found" errors.

2. **Execute Audit Script**:
   - Run the automated verification script in the terminal (e.g. `python scripts/verify_design_milestone.py` or node scripts).
   - **Multi-Asset Regression Sweep**: If the project compiles multiple pages, cards, or assets (like our 50 micrographics templates), the verification script MUST run a visual audit sweep checking a representative sample of multiple items (e.g. all targeted templates or a set of 15+ cards). This prevents "dark fixes" where fixing one asset causes layout breakages in another.
   - Do NOT run manual browser steps; let the script handle the static server startup, navigation, console audits, and screenshot captures.

3. **Verify Outputs**:
   - Check the terminal output of the execution script.
   - If console errors are printed, highlight them as blocking items that must be resolved.
   - If screenshots are captured successfully, display clickable links to the generated audit screenshots (e.g. Mobile, Tablet, Desktop, or Layout cards).

4. **Code Quality and Regression Review**:
   - Ensure the build and verification scripts finish with exit code `0` and no console errors.
   - Inspect the compiled screenshots side-by-side to guarantee visual parity with designs, and double-check for regressions (e.g. text wrapping, overlapping elements, or broken borders) in unrelated components before claiming the work is complete.
