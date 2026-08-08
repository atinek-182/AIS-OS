---
title: H4 Stat Led
domain: skill
summary: A giant number or metric is the hero. A small qualifier line below. *Use when:* you have one defensible, externally-verifiable
  number.
critical_directives:
- Follow document guidance without bypassing established safeguards.
section_outline:
- H4 · Stat-Led
read_triggers:
- When working on skill in .agents/skills/hallmark/references/components/h4-stat-led.md
- When reading context for H4 Stat Led
tags:
- skill
- h4-stat-led
updated: '2026-08-08'
---

### H4 · Stat-Led
A giant number or metric is the hero. A small qualifier line below.
*Use when:* you have one defensible, externally-verifiable number.
*Don't confuse with:* T4 Numbered stat strip (which is several stats in a row, not one focal).

```html
<section class="hero-stat">
  <p class="figure tnum">99.97<span class="unit">%</span></p>
  <p class="qualifier">…</p>
</section>
```
```css
.figure { font-size: clamp(6rem, 18vw, 16rem); font-variant-numeric: tabular-nums; line-height: 0.85; }
```
