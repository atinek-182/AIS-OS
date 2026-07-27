import os

skill_dir = r'd:\AI-OS\.agents\skills\six-file-context-methodology'
os.makedirs(skill_dir, exist_ok=True)

skill_file = os.path.join(skill_dir, 'SKILL.md')

content = """---
name: six-file-context-methodology
description: Apply Senior AI Engineering 6-File Context Methodology & 3-Step Decoupled Workflow (from JavaScript Mastery masterclass). Use when initializing new projects, structuring AI coding context, or creating feature specifications.
argument-hint: '[init|scaffold|spec <feature-name>|check]'
---

# ⚡ Six-File Context Methodology (`/six-file-context-methodology`)

## ⚡ Invocation & Tri-Mode Routing

This skill supports **Tri-Mode Flexible Execution**:
- **Slash Command**: Explicitly run `/six-file-context-methodology [init|scaffold|spec <feature-name>]` in chat.
- **Dynamic Intent Matching**: Triggered automatically when task context involves keywords in the description (e.g., "scaffold context", "6-file context", "feature spec", "senior AI workflow").
- **Inter-Skill & AIOS Calling**: Programmatically invokable by parent skills (e.g. `/new-project`, `/make-plan`) or subagents via `/six-file-context-methodology` or reading `SKILL.md` directly.

---

## 📌 What This Skill Does

This skill enforces the **Senior AI Engineering Workflow** taught in the 4-hour JavaScript Mastery masterclass (*How Senior Engineers Build With AI in 2026*):

1. **Scaffolds the 6 Core Context Files** (`context/`) before a single line of feature code is written.
2. **Enforces Decoupled 3-Step Execution**:
   - **Step 1**: UI Primitives & Design System CSS tokens in `globals.css`.
   - **Step 2**: Database Schema & Headless Backend API Routes / Server Actions.
   - **Step 3**: UI-to-API Integration & State Binding.
3. **Generates Surgical Feature Specifications** (`context/features/*.md`) following the 29-spec production architecture pattern.

---

## 🛠️ Commands & Usage Guide

### 1. `init` / `scaffold`
Scaffolds the complete `context/` directory in the current project root:
- `context/AGENTS.md`
- `context/project-overview.md`
- `context/architecture-context.md`
- `context/code-standards.md`
- `context/ui-context.md`
- `context/ai-workflow-rules.md`
- `context/progress-tracker.md`

Reference templates are available under:
`file:///d:/AI-OS/references/six-file-context-methodology/6-file-context-templates/`

### 2. `spec <feature-name>`
Generates a numbered, surgical feature spec in `context/features/XX-<feature-name>.md` detailing:
- Feature Purpose & User Story
- UI Primitives Required
- Database Schema Modifiers (Prisma/PostgreSQL)
- API Routes & Server Actions Contract
- Verification Checkpoints

Reference specs are available under:
`file:///d:/AI-OS/references/six-file-context-methodology/feature-specs-library/`

### 3. `check`
Audits the active project against the 6-file context methodology rules and flags missing context files or unsaved progress tracking.

---

## 📚 Knowledge Base References

- **Masterclass Handbook**: [STEP_BY_STEP_SENIOR_AI_ENGINEERING_GUIDE.md](file:///d:/AI-OS/references/six-file-context-methodology/STEP_BY_STEP_SENIOR_AI_ENGINEERING_GUIDE.md)
- **Full Video Transcript**: [FULL_TRANSCRIPT.md](file:///d:/AI-OS/references/six-file-context-methodology/FULL_TRANSCRIPT.md)
- **29 Production Feature Specs**: [feature-specs-library/](file:///d:/AI-OS/references/six-file-context-methodology/feature-specs-library/)
"""

with open(skill_file, 'w', encoding='utf-8') as f:
    f.write(content)

print(f"Custom skill created at {skill_file}")
