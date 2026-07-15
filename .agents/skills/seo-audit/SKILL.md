---
name: seo-audit
description: Use when running SEO audits, technical SEO reviews, schema verification, sitemap checks, GEO/AEO analysis, page speed checks, keyword research, or backlinks verification.
---

# SEO Audit & GEO Router Skill

When this skill is triggered, you will execute or guide the SEO audit using the reference guides and Python scripts in the static skills-library.

## Step-by-Step Execution Workflow

### 1. Identify the Audit Category
Map the user's request to one of the following SEO sub-categories:
* **`seo-technical`**: Technical SEO checklist, redirects, robots.txt, rendering checks.
* **`seo-schema`**: JSON-LD schema generation and ecommerce schema verification.
* **`seo-geo`**: Generative Engine Optimization / AI Engine Optimization (GEO/AEO).
* **`seo-audit`**: Complete site audit, performance checklists.
* **`seo-sitemap`**: Sitemap extraction and crawling logic.
* **`seo-performance` / `pagespeed`**: Core Web Vitals, LCP subparts, PageSpeed API checks.
* **`seo-backlinks`**: Staging backlinks and checking authority scores.

### 2. Read the Reference Guide
Read the corresponding markdown agent or skill file using the `view_file` tool:
* `d:\AI-OS\brain-aios\wiki\research\skills-library/claude-seo/agents/{category}.md`
* OR `d:\AI-OS\brain-aios\wiki\research\skills-library/claude-seo/skills/{category}/SKILL.md`

### 3. Run Programmatic Audit Script (If Needed)
If a technical verification command is requested, execute the relevant python script located at `d:\AI-OS\brain-aios\wiki\research\skills-library/claude-seo/scripts/` using the terminal:
* **Schema Validation**: `python d:/AI-OS/brain-aios/wiki/research/skills-library/claude-seo/scripts/schema_ecommerce_validate.py [args]`
* **PageSpeed Check**: `python d:/AI-OS/brain-aios/wiki/research/skills-library/claude-seo/scripts/pagespeed_check.py [args]`
* **HTML Parsing**: `python d:/AI-OS/brain-aios/wiki/research/skills-library/claude-seo/scripts/parse_html.py [args]`
* **Visual Audit**: `python d:/AI-OS/brain-aios/wiki/research/skills-library/claude-seo/scripts/analyze_visual.py [args]`
* **Keywords**: `python d:/AI-OS/brain-aios/wiki/research/skills-library/claude-seo/scripts/keyword_planner.py [args]`
* **Drift Comparison**: `python d:/AI-OS/brain-aios/wiki/research/skills-library/claude-seo/scripts/drift_compare.py [args]`

*Note: Ensure any Python dependencies like `requests`, `beautifulsoup4`, or `jinja2` are installed using `pip install [package]` if the script errors due to missing imports.*

### 4. Output the SEO Report
Present a structured report outlining:
1. **Audited Target**: Page URL or file path.
2. **Key Metrics/Status**: Output from python scripts or checklists.
3. **Critical Issues**: High-priority issues that harm search ranking or GEO compatibility.
4. **Actionable Recommendations**: Clear, bulleted steps to resolve the issues.
