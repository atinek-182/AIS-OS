# Premium Frontend Experience System Integration: Brainstorm / Discovery Notes
Date: 2026-07-16 · Goal: Safely integrate the premium frontend experience design system as a "design brain" without mixing with brand assets, check benefit, address deleted skills, review vulnerabilities, and update AIOS configurations.

## Summary / key decisions
- **Junction Established**: Successfully linked `C:\Users\HP\Documents\Premium-Frontend-Experience_System` to `d:\AI-OS\premium-frontend-experience-system`.
- **System Value**: The system acts as a high-leverage "Design Brain," enforcing visual restraint (no visual noise, no generic AI-style dark gradients) and rigorous browser-based verification (Playwright, responsive breakpoints, accessibility).
- **Deleted Skill Strategy**: Identified `vercel-composition-patterns` as a missing reference. Recommended removing it from the design system prompt files and substituting it with `vercel-web-design-guidelines` and `frontend-design`.
- **Integration Plan**: Update global and workspace `AGENTS.md` and `GEMINI.md` to trigger these design system rules automatically for web engineering and interface design.

## Q&A log
### Q1 — Integration & Missing Skills
- **Asked**: How should we handle the deleted `vercel-composition-patterns` skill, and do you approve of mapping the design system's guidelines directly to our core AIOS rules?
- **Captured**: Approved recommended strategy. We will not reinstall the deleted `vercel-composition-patterns` skill. Instead, we'll clean up its references in the design system files and use `vercel-web-design-guidelines` and `frontend-design` as active substitutes. We will update `GEMINI.md` and `WORKSPACE_MAP.md` to make this system our default frontend design brain, incorporating a "fast-track" bypass for minor edits to prevent rigidity.
- **Flags**: None.

## Open flags (pending input)
- Confirm deleted skills clean-up and substitute -> User
- Verify Next.js support additions -> User

## Initial Analysis Details

### 1. How It Benefits Us
- **visual Restraint & Taste**: Prevents typical LLM mistakes like over-animating elements or using cheap templates.
- **Rigor in verification**: Enforces Playwright browser testing, multi-viewport checks, and accessibility audits.
- **Structured intake**: Prevents starting work on vague requests.

### 2. Can It Be Improved?
- **Next.js Adaptation**: Current docs are highly biased toward client-side React + Vite. We should add Next.js-specific rules (RSC compatibility, hydration safety for Canvas/WebGL, Next.js routing/image optimization).
- **Automation Integration**: Link the QA checks to automated terminal tests or pre-commit hooks to make verification seamless.

### 3. Can It Improve Our AIOS?
- **Yes**: We can hook it into our workspace-scoped agents and global guidelines (`AGENTS.md` and `GEMINI.md`) so that any front-end task automatically references these files.

### 4. Does It Reduce Quality?
- **No, it raises it**: By banning generic templates and lazy coding, it guarantees high-quality, custom front-end delivery.

### 5. Deleted Skills Check
- Missing: `vercel-composition-patterns`.
- Solution: Do not install it. Instead, clean up references in the design system files and use `vercel-web-design-guidelines` and `frontend-design` which are already active.

### 6. Vulnerabilities & Risks
- **Rigidity**: Enforcing a full Q&A and design brief for trivial tweaks is a waste. We need a "fast-track" rule for minor edits.
- **Dependency Bloat**: High reliance on Lenis, GSAP, and Framer Motion can lead to bundle issues. We should audit dependencies for every reused component.
