---
title: '🚀 Next Chat Kickoff Brief: Component Extractor Refinement & Phase 2 Sweep'
domain: architecture
summary: '> **Copy and paste this brief into your next chat to immediately kick off Phase 2 execution!** In the previous session,
  we successfully:'
critical_directives:
- Follow document guidance without bypassing established safeguards.
section_outline:
- '🚀 Next Chat Kickoff Brief: Component Extractor Refinement & Phase 2 Sweep'
- 📋 Overview & Task Goal
- 🎯 Next Chat Immediate Action Required
- '💡 Suggested Prompt to Paste in Next Chat:'
read_triggers:
- When working on architecture in references/phase2-execution-brief.md
- 'When reading context for 🚀 Next Chat Kickoff Brief: Component Extractor Refinement & Phase 2 Sweep'
tags:
- architecture
- phase2-execution-brief
updated: '2026-08-08'
---

# 🚀 Next Chat Kickoff Brief: Component Extractor Refinement & Phase 2 Sweep

> **Copy and paste this brief into your next chat to immediately kick off Phase 2 execution!**

---

### 📋 Overview & Task Goal
In the previous session, we successfully:
1. Expanded component registries from 147 to **300+ items across 11 sources** in `component-registry-index.json`.
2. Created **Dual Dedicated Reference Vaults** (`component-vault/` and `shader-canvas-vault/`).
3. Upgraded `scrape_full_site_mirror.py` with WebGL GLSL shader hooks, 3D asset interceptors, and path traversal security patches.
4. Updated `INGESTION_QUEUE.md` with 6 Awwwards targets (TRIONN, Resn, Active Theory, Locomotive, Merci Michel, Bruno Simon).

### 🎯 Next Chat Immediate Action Required

Before launching the Phase 2 Awwwards Sweep on Site #19 (TRIONN Agency `https://trionn.com/`), we need to:

1. **Refine Unbounded Component Extractor:**
   - Enhance the AST / DOM component parser in `scrape_full_site_mirror.py` so it parses EVERY unique UI component on target sites without missing any elements (extracting into `code-extracts/components/nav/`, `hero/`, `cards/`, `scrolly/`, `modals/`, `footers/`, `3d/`).
   - Remove any artificial component limits.

2. **Execute Site #19 (TRIONN Agency):**
   - Run `/scrape-reference https://trionn.com/ trionn-agency`.
   - Verify raw code extracts, `.glsl` fragment shaders, screenshots across 5 viewports, and unbounded component `.tsx` files.
   - Update `INGESTION_QUEUE.md` and present raw file links.

---

### 💡 Suggested Prompt to Paste in Next Chat:

```markdown
Let's refine the Unbounded Component Extractor in `scripts/scrape_full_site_mirror.py` to ensure it extracts EVERY unique UI component from target sites into `code-extracts/components/`, and then run Phase 2 Site #19: TRIONN Agency (https://trionn.com/).
```
