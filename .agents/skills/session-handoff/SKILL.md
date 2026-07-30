---
name: session-handoff
description: Generate a clean end-of-session handoff summary so you can clear context and resume work cleanly in a new session without losing state. Invokable directly via /session-handoff.
argument-hint: '[optional: specific topic or milestone focus]'
---

# Session Handoff — Clear Context, Preserve State

## ⚡ Invocation & Tri-Mode Routing

This skill supports **Tri-Mode Flexible Execution**:
- **Slash Command**: Explicitly run `/session-handoff` in chat.
- **Dynamic Intent Matching**: Triggered automatically when the user asks to summarize the session, prepare a handoff, or wrap up work.
- **Inter-Skill & AIOS Calling**: Invokable by parent skills or subagents.

## 🎯 Purpose

When a session grows long or a major milestone completes, generate a structured handoff note summarizing context, completed work, active decisions, and immediate next actions.

## 📋 Handoff Workflow

1. **Scan Recent Session Activity**:
   - Check modified files, git status (`git status --porcelain`), and decisions logged in `decisions/log.md`.
   - Read `hot.md` for active sprint context.

2. **Generate Handoff Structure**:
   - **Session Objective**: High-level summary of what was tackled.
   - **Completed Work**: Bulleted list of code changes, skills ingested, or files updated with markdown links.
   - **Key Decisions Logged**: Decisions added to `decisions/log.md`.
   - **Active State & Unfinished Threads**: Open questions or tasks in progress.
   - **Immediate Next Action for Next Session**: The single most clear next step to resume.

3. **Update Hot Cache (`hot.md`)**:
   - Update `hot.md` with the new active context and next actions so a fresh session reading `hot.md` instantly restores context.

4. **Output Handoff Note**:
   - Present the summary in chat and optionally save to `brain-aios/wiki/log.md`.
