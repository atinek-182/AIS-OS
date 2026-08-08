---
title: C2 Inline Form As Cta
domain: skill
summary: The CTA *is* the form — a single email input with a "Submit →" beside it. No separate landing for sign-up. *Use when:*
  the action is collecting an email.
critical_directives:
- Follow document guidance without bypassing established safeguards.
section_outline:
- C2 · Inline form-as-CTA
read_triggers:
- When working on skill in .agents/skills/hallmark/references/components/c2-inline-form-as-cta.md
- When reading context for C2 Inline Form As Cta
tags:
- skill
- c2-inline-form-as-cta
updated: '2026-08-08'
---

### C2 · Inline form-as-CTA
The CTA *is* the form — a single email input with a "Submit →" beside it. No separate landing for sign-up.
*Use when:* the action is collecting an email.
*Don't confuse with:* C1 Outlined chip (which navigates, not submits).

```html
<form class="cta-form">
  <label for="email" class="visually-hidden">Email</label>
  <input id="email" type="email" placeholder="you@example.com" />
  <button type="submit">Send →</button>
</form>
```
```css
.cta-form { display: grid; grid-template-columns: 1fr auto; border-bottom: 1px solid var(--color-ink); }
.cta-form input { background: none; border: 0; padding: 0.7rem 0; min-height: 44px; }
```
