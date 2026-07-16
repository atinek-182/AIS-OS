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

1. **Locate Target Directory**:
   - By default, use the current active project directory.
   - If not specified, look in the `projects/` subdirectories or workspace root.

2. **Execute Audit Script**:
   - Run the automated python verification script in the terminal:
     ```bash
     python scripts/verify_design_milestone.py [project_dir]
     ```
   - Do NOT run manual browser steps; let the script handle the static server startup, navigation, console audits, and screenshot captures.

3. **Verify Outputs**:
   - Check the terminal output of the execution script.
   - If console errors are printed, highlight them as blocking items that must be resolved.
   - If screenshots are captured successfully, display clickable links in the format:
     - [Mobile Small (360px)](file:///[project_path]/qa/screenshot_mobile_small.png)
     - [Mobile Large (390px)](file:///[project_path]/qa/screenshot_mobile_large.png)
     - [Tablet (768px)](file:///[project_path]/qa/screenshot_tablet.png)
     - [Laptop (1024px)](file:///[project_path]/qa/screenshot_laptop.png)
     - [Desktop (1440px)](file:///[project_path]/qa/screenshot_desktop.png)

4. **Code Quality and Console Check**:
   - Ensure the build finishes with exit code `0`.
   - If console errors were found, recommend fixes in the target components.
