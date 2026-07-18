# Autoresearch Self-Improving Loops: Brainstorm / Discovery Notes
Date: 2026-07-17 · Goal: Configure, run and verify sandboxed Autoresearch optimization loops for prompt tuning, vision-in-the-loop design, and web speed.

## Summary / key decisions
- **Sandbox Container**: Docker image `aios-sandbox` based on `python:3.10-slim` + `uv` to be built in `/trials/`.
- **Resource Hard-Caps**: CPU limit `--cpus="0.5"`, memory limit `--memory="1.5g"` (increased to 1.5 GB to prevent Playwright/Chromium OOM issues).
- **Execution Architecture (Host-Controlled)**: Git commands (`git checkout`, `git commit`, `git reset --hard`) will run on the host machine. The Docker container will act purely as an isolated evaluator, avoiding permission/ownership conflicts inside the sandbox.
- **Docker Image Setup**: Use a Dockerfile that installs Playwright system dependencies (`playwright install-deps chromium`) so that Playwright can launch headless Chromium inside the container without OOMs.
- **Evaluation Consistency**: Use `temperature=0` and structured checklists for Gemini checklist queries. Web speed benchmarks will track both deterministic file sizes and median page-load times over 10 iterations.
- **Target Skill for Prompt Tuning**: Optimize workspace-scoped `excalidraw-diagram` skill (`d:/AI-OS/.agents/skills/excalidraw-diagram/SKILL.md`).
- **Global Skill Cleanup**: Delete the global `excalidraw-diagrams` skill folder from `C:\Users\HP\.gemini\config\skills\excalidraw-diagrams` to prevent duplication.
- **LLM Evaluator & Vision API**: Use Gemini API with `gemini-2.5-flash` (or `gemini-1.5-flash`), passing `GEMINI_API_KEY` from the host environment to the docker sandbox.
- **Target Asset for Vision-in-the-Loop Design**: Optimize a generic, highly visually appealing Instagram carousel slide card template (`slide.html` + `styles.css`) for layout, component structure, content hierarchy, and CTA across various use cases (inspired by external reference carousels, not constrained by predetermined branding).
- **Web Speed Optimizations Setup**: Build a reusable, modular speed optimization and minifier engine. The scripts (`train.py` and `prepare.py`) will be generic so they can be pointed at any website folder in the future to minify, optimize, and benchmark page load speeds.

## Q&A log
### Q1 — Target Skill for Prompt Tuning
- Asked: Which skill prompt should we optimize for the prompt tuning target?
- Captured: Optimize the workspace-scoped `excalidraw-diagram` skill. Also, delete the global `excalidraw-diagrams` skill from `C:\Users\HP\.gemini\config\skills\excalidraw-diagrams`.
- Flags: None

### Q2 — Vision API and LLM Provider
- Asked: What LLM API provider and key should we use for optimization loops?
- Captured: Use Gemini API (`gemini-2.5-flash` or `gemini-1.5-flash`) for evaluations, passing `GEMINI_API_KEY` from the host environment.
- Flags: User must ensure `GEMINI_API_KEY` is set in the host environment or added to the `.env` file before running the loops.

### Q3 — Web Speed Benchmarking Engine
- Asked: Should we use Python Playwright for the web speed optimization benchmark?
- Captured: Implement the local benchmark inside `prepare.py` using Python's `playwright` library instead of Node/Puppeteer, and use Python's built-in `http.server` to serve the website.
- Flags: None

### Q4 — Target Asset for Vision-in-the-Loop Design
- Asked: Which visual asset would you like to optimize first?
- Captured: Optimize an Instagram carousel slide card template (`slide.html` + `styles.css`). The goal is to build a highly visually appealing, content-rich layout with strong CTAs and component designs adapted for multiple use-cases. We'll scrape reference carousel designs for inspiration.
- Flags: User will provide reference carousel links to scrape.

### Q5 — Target Website for Web Speed Optimization
- Asked: Do you agree with using a sample landing page template for the speed optimization loop?
- Captured: Build a generic, reusable speed-optimization framework. The scripts (`train.py` and `prepare.py`) will be written modularly so the user can easily point them at any local website directory to automate minification and load-time benchmarking.
- Flags: None

### Q6 — Reference Carousel Links for Scraping
- Asked: What links or accounts would you like to target for scraping?
- Captured: Initialize `references.json` with a placeholder list of URLs. The system will be built to read from this, and the user can later run the `scrape-carousel` skill to fetch the design references which the loop will then ingest.
- Flags: User will provide the actual links/scrape the carousels later.

### Q7 — Final Folder Layout and Branching
- Asked: Are there any specific folder layout or branching preferences?
- Captured: Initialize dedicated directories for all three targets under `/trials/`. Code will run on a dedicated branch `autoresearch/optimization-loops`.
- Flags: None.

## Open flags (pending input)
- Set host-level `GEMINI_API_KEY` for API evaluations -> Operator.
- Provide Instagram carousel links to `references.json` and scrape them -> Operator.
