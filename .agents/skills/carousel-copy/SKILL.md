---
name: carousel-copy
description: Plan slide-by-slide copywriting and layouts for viral carousels following the Zorixel Design System and adarshxdesign rules. Runs Phase 0 /grill-me topic discovery and /roast hook critique. Invokable via /carousel-copy.
argument-hint: '[topic_or_idea]'
---

# ZORIXEL Viral Carousel Copywriter (`/carousel-copy`)

## ⚡ Invocation & Tri-Mode Routing

This skill converts a topic, prompt, or concept into a viral Instagram carousel copy plan following ZORIXEL brand rules and adarshxdesign visual contracts.

Invokable via:
- **Slash Command**: `/carousel-copy [topic]`
- **Dynamic Intent**: Triggered automatically when planning Instagram carousels, social media graphics, or reel outlines.
- **Inter-Skill Calling**: Invoked by `/carousel-render`, `/scrape-carousel`, `/grill-me`, `/roast`, and `/canvas-design`.

---

## 🎯 Specific Use Cases & Target Audience
- **ZORIXEL Educational Carousels**: Create high-converting 5-10 slide carousels teaching UI/UX design, web creation, AI tools, or vibe coding to freelancers and designers.
- **Micro-Offer / Product Launches**: Generate scroll-stopping carousels promoting digital products or AI tools (target: ₹1,00,000 revenue goal).

---

## 🚀 Execution Workflow

### Step 1: Phase 0 Socratic Discovery (`/grill-me`)
If the topic is vague, run `/grill-me` on:
1. Target audience pain point & outcome.
2. Hook style (Curiosity, Direct Value, Before/After, Contradiction).
3. Primary CTA goal (DM keyphrase, save post, visit website).

### Step 2: Adversarial Hook & Copy Roast Gate (`/roast`)
Run `/roast` on Slide 1 Hook & Slide 2 payoff:
- **Contrarian**: Flag weak/cliché hooks or boring slides.
- **Expansionist**: Elevate the 10x viral angle and psychological curiosity gap.
- **Buyer**: Validate if the target reader will actually stop scrolling and swipe.

### Step 3: Rules of Viral Slides
1. **Slide Count**: Keep it between 5 and 20 slides total. Recommend 5-10 for reader retention, unless a deep-dive tutorial requires more.
2. **Aspect Ratio Consistency**: Select a single format for the post (`portrait` [4:5], `square` [1:1], or `landscape` [1.91:1]) and specify it in the header. Do not mix formats to avoid forced cropping by Instagram.
3. **Safe Zones**: Ensure all layouts keep text and core visuals away from the 10% outer boundaries (no text within 130px of top, 110px of bottom) to avoid native UI overlaps.
4. **Rule 1 (Scan-Friendly)**: Bold, big text. Word count ≤ 25 words per slide.
5. **Rule 2 (Visual Metaphors)**: Use split comparisons, bento boxes, or code windows. Avoid raw text blocks.
6. **Rule 3 (Benefit Hook)**: Hook slide must focus on results/payoffs. No agenda/agenda-style filler slides.
7. **Rule 4 (Contrast)**: Specify high-contrast layout configurations.
8. **Rule 5 (Simplicity)**: Focus on one core idea per slide.

### Step 4: Available Presets & Layout Options
Select slide layouts matching our stylesheet presets:
- `hook`: Slide 1 hook with title, subtitle, mini card list, and footnote.
- `split-comparison`: Side-by-side comparison of "Before" vs. "After" concepts (perfect for rules/do's-and-don'ts).
- `editorial-quote`: Minimalist serif typography for impactful statements.
- `code-showcase`: Code block in a dark window for developer tutorials.
- `bento-features`: Grid layout for multiple features, tools, or benefits.
- `full-bleed-callout`: Bold primary-colored slide with button callout for major takeaways.
- `cta`: Slide last, featuring a single, clear button overlay and DM keyphrase.

### Step 5: Zorixel Visual Contract Guidelines
- **Editorial Magazine Identity**: Target `Style: light` by default (warm linen off-white paper canvas background `#fbfaf7` with charcoal `#141413` text and brand coral `#ff6b4a` accents under 10% screen space).
- **Large Typography Scale**: All font sizes must be styled to be very large (Hooks at `68px`, headings at `46px`, body text inside panels at `22px`-`32px`, captions at `18px`). Ensure words wrap cleanly without orphans (`text-wrap: balance`).
- **Elevated Paper Cards**: Avoid raw flat columns or border-heavy grids. Style comparison columns on slides 3-5 as pure white floating cards with a highly diffused, soft shadow offset to feel like physical print sheets.
- **CTA Contrast**: Button text must be styled as solid white on a solid black/charcoal button background (no low-contrast grey or primary color texts inside buttons).
- **No AI Slop Elements**: Ban standard SaaS-cream colors, thick border card grids, repetitive uppercase kickers/eyebrows, and numbered section marking prefixes (01 / 02) unless representing a sequential process.

---

## 📄 Target Markdown File Schema (`d:\AI-OS\brainstorms\temp_carousel\copy.md`)

Always write the output plan to `d:\AI-OS\brainstorms\temp_carousel\copy.md` in this exact format:

```markdown
# Carousel: [Topic Title]
Style: light
AspectRatio: portrait

## Slide 1: Hook
Layout: hook
Title: [Scroll-stopping Headline]
Subtitle: [Sub-headline payoff]
Kicker: ZORIXEL DESIGN SYSTEM

## Slide 2: Problem / Before State
Layout: split-comparison
Before: [Common mistake or naive code]
After: [Professional Zorixel standard]

## Slide 3-9: High-Value Steps
Layout: bento-features
Panel1: [Core takeaway 1]
Panel2: [Core takeaway 2]

## Slide 10: Call To Action
Layout: cta
Title: Want the full template?
Subtitle: Comment "SYSTEM" below to get instant access.
ButtonText: GET THE TEMPLATE
```

---

## 🔗 Inter-Skill Connections & Handoff Pipeline
- **Next Step**: Once `copy.md` is generated, run **`/carousel-render`** to compile HTML slides and capture final PNG images using Playwright headless browser rendering.
- **Design Tuning**: If custom color swatches or contrast audits are needed, run **`/brand-colors`**.
- **Reference Ingestion**: If extracting copy outlines from a reference Instagram carousel URL, run **`/scrape-carousel [url]`**.

---

## 🔄 Post-Execution Auto-Evolution & Adversarial `/roast` Gate

At the completion of every execution of this skill:

1. **Adversarial `/roast` Council Review**: Convene the 5-Persona ZORIXEL AIOS Roast Council (`/roast`) to stress-test the output, code edits, or strategy generated by this skill. Red-team for missing edge cases, terminal shell bugs, token leaks, or optimization gaps.
2. **Autonomous Tool, Script & Skill Auto-Upgrade Loop**:
   - If new error patterns or execution safeguards are discovered, append them to `references/GLOBAL_ERROR_PREVENTION_RULES.md` and execute `python scripts/sync_global_rules.py` via `run_command` so system prompts (`AGENTS.md` and `GEMINI.md`) auto-update inline.
   - Run pre-flight health checks (`aios_gws_health_check.py`, `test_notion_formula.py`, `graphify_runner.py`).
   - Self-upgrade this `SKILL.md` instruction file with newly learned edge cases using `replace_file_content` or `write_to_file`.
3. **Register & Log**: Log milestone upgrades in [WORKSPACE_MAP.md](file:///d:/AI-OS/WORKSPACE_MAP.md) and [decisions/log.md](file:///d:/AI-OS/decisions/log.md).

