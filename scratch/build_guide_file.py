import os

guide_path = r'd:\AI-OS\references\six-file-context-methodology\STEP_BY_STEP_SENIOR_AI_ENGINEERING_GUIDE.md'

content = """# Masterclass Guide: How Senior Engineers Build With AI in 2026

## 📌 Executive Overview
This guide provides an unsummarized, complete blueprint of the Senior AI Engineering workflow taught by **JavaScript Mastery (Adrian Hajdin)** in the 4-hour masterclass *How Senior Engineers Actually Build With AI in 2026*.

In 2026, senior engineers do not manually type syntax line-by-line. They act as **Systems Architects** and **AI Supervisors**. They spend their time designing system boundaries, writing structured context files (`context/`), breaking products down into surgical feature specifications (`feature-specs/`), and directing AI agents (Cursor, Windsurf, Claude Code, Antigravity) to write production-ready code without architectural drift or slop.

---

## 🏗️ The 6-File Context Methodology

The core foundation of AI-assisted engineering is **Context Architecture**. Giving an AI agent a blank prompt or a vague request results in broken styles, incorrect ORM calls, and unmaintainable code within 3 weeks.

Before writing a single line of feature code, create a dedicated `context/` folder in your project root containing these 6 core context files (plus system instructions):

### 1. `AGENTS.md` / `CLAUDE.md` (System Persona & Agent Directives)
- Defines the agent's role (Senior Full-Stack Systems Architect).
- Lists forbidden anti-patterns (no inline hex colors, no monolithic components, no black-box code).
- Sets primary CLI commands, framework constraints, and code verification rules.

### 2. `project-overview.md` (High-Level Product Requirements)
- High-level business goal and user experience contract.
- Lists target users, key user flows, core domain entities, and non-functional performance requirements.

### 3. `architecture-context.md` (System Boundaries & Data Flow)
- Defines application layers: Next.js 15 App Router, Prisma ORM + PostgreSQL, Clerk Auth, Liveblocks WebSocket engine, Trigger.dev background workers, Vercel Blob storage.
- Outlines exact state management policies (Liveblocks rooms vs React state vs Server Actions).

### 4. `code-standards.md` (TypeScript & Linting Rules)
- Strict TypeScript rules (no `any`, explicit return types for Server Actions, Zod schema validation for all API inputs).
- Naming conventions, folder layout conventions (`components/ui`, `components/editor`, `lib/actions`).

### 5. `ui-context.md` (Design Tokens & Component Rules)
- Complete design system token mapping (`globals.css` HSL/OKLCH color variables).
- Color tokens for dark mode canvas: background, card, primary accent, node border colors, cursor colors.
- Rules for Shadcn UI primitive usage.

### 6. `ai-workflow-rules.md` (Agent Prompting & Execution Workflow)
- Defines the 3-step build workflow (UI Primitives -> Database Schema & Headless APIs -> UI-to-API Integration).
- Rules for referencing feature specs (`context/features/*.md`) step-by-step.

### 7. `progress-tracker.md` (Active Feature Checklist)
- Living document tracking completed vs in-progress feature specs.
- Updated by the agent after completing each feature verification.

---

## ⚡ The Decoupled 3-Step Build Workflow

Never ask an AI agent to build a database schema, backend API, and rich UI component in a single prompt. Senior engineers execute every feature in 3 decoupled steps:

```
┌─────────────────────────────────────────────────────────────┐
│ STEP 1: UI Primitive Components & CSS Design Tokens          │
│ Build static UI layout, Shadcn components, & CSS variables   │
└──────────────────────────────┬──────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────┐
│ STEP 2: Database Schema & Headless Backend API Routes        │
│ Define Prisma model, run migrations, & create Server Actions│
└──────────────────────────────┬──────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────┐
│ STEP 3: UI-to-API Binding & Optimistic Updates               │
│ Connect UI state to backend Server Actions & Liveblocks room │
└─────────────────────────────────────────────────────────────┘
```

---

## 🛠️ Step-by-Step Build Order (29 Production Feature Specs)

To build the real-time AI system architecture app (**Ghost AI**), execute the 29 feature specifications in strict sequence:

### Phase 1: Design System & Foundation (Specs 01 - 04)
1. **`01-design-system.md`**: Configure `globals.css` color tokens, dark mode palette, typography fonts, and Shadcn primitives (`Button`, `Dialog`, `Input`, `DropdownMenu`).
2. **`02-editor-chrome.md`**: Build editor top navigation bar, left action sidebar shell, and room title header.
3. **`03-auth.md`**: Implement Clerk Authentication (`<ClerkProvider>`, sign-in modal, user button avatar, auth middleware protection).
4. **`04-project-dialogs.md`**: Build modal dialogs for creating, renaming, and deleting project canvases.

### Phase 2: Database & Headless APIs (Specs 05 - 09)
5. **`05-prisma.md`**: Setup Prisma ORM with PostgreSQL database connection. Define `User`, `Project`, and `Collaborator` models.
6. **`06-project-apis.md`**: Implement Server Actions for CRUD operations (`createProject`, `getProjects`, `updateProjectName`, `deleteProject`).
7. **`07-wire-editor-home.md`**: Connect project sidebar UI to Prisma Server Actions to display user's projects dynamically.
8. **`08-editor-workspace-shell.md`**: Create dynamic route `/workspace/[projectId]` with project access verification.
9. **`09-share-dialog.md`**: Build project access sharing dialog to invite team members by email with owner/editor permissions.

### Phase 3: Real-Time Multiplayer Canvas (Specs 10 - 19)
10. **`10-liveblocks-setup.md`**: Install `@liveblocks/client`, `@liveblocks/react`, `@liveblocks/react-ui`. Configure Liveblocks room provider and authorization API route `/api/liveblocks-auth`.
11. **`11-base-canvas.md`**: Setup React Flow (`@xyflow/react`) inside Liveblocks room for real-time infinite canvas zooming & panning.
12. **`12-shape-panel.md`**: Build drag-and-drop shape sidebar panel (Rectangles, Circles, System Icons, Text nodes).
13. **`13-node-shape.md`**: Implement custom React Flow nodes for System Architecture elements (Database, API Gateway, Server, Cache, Client).
14. **`14-node-editing.md`**: Add inline text editing, resizing, and label customization to canvas nodes.
15. **`15-node-color-toolbar.md`**: Implement node floating action toolbar (Background color picker, Border style, Delete, Duplicate).
16. **`16-edge-behavior.md`**: Configure custom connection edges (Smoothstep, Animated dashed lines, Directional arrowheads).
17. **`17-canvas-ergonomics.md`**: Implement keyboard shortcuts (Delete, Duplicate, Copy/Paste, Undo/Redo via Liveblocks history).
18. **`18-starter-templates.md`**: Add pre-built architecture system templates (Microservices architecture, Auth flow, Serverless backend).
19. **`19-presence-avatars-cursors.md`**: Implement real-time live cursors (`useOthers()`) and user presence avatars header showing active collaborators on the canvas.

### Phase 4: Async Background AI Jobs (Specs 20 - 29)
20. **`20-ai-sidebar-shell.md`**: Build AI Agent interaction sidebar panel (`<AISidebar>`).
21. **`21-canvas-autosave.md`**: Implement automatic canvas state serialization and Vercel Blob persistence.
22. **`22-design-agent-api.md`**: Create API route `/api/ai/generate-architecture` triggering Trigger.dev background worker.
23. **`23-design-agent-logic.md`**: Implement Trigger.dev task (`@trigger.dev/sdk`) calling OpenAI/Anthropic structured outputs to layout system architecture nodes & edges.
24. **`24-ai-presence-state.md`**: Render live "AI Agent is designing..." indicator on canvas while background job executes.
25. **`25-sidebar-chat-feed.md`**: Build conversational AI chat interface in the right sidebar.
26. **`26-ai-chat-functional.md`**: Connect AI chat feed to background task execution for interactive architectural refactoring.
27. **`27-spec-generation-flow.md`**: Create background job for generating comprehensive technical PRDs and system architecture documentation from canvas nodes.
28. **`28-spec-persistence-download.md`**: Save generated PRD specs to Vercel Blob and provide PDF/Markdown download links.
29. **`29-spec-ui-integration.md`**: Add full-screen PRD spec viewer modal with copy-to-clipboard and export tools.

---

## 🔄 Async AI Job Architecture (Trigger.dev)

```
┌──────────────┐       POST /api/ai/generate       ┌────────────────┐
│ Next.js App  ├──────────────────────────────────►│ Next.js API    │
│ Frontend     │                                   │ Route          │
└──────▲───────┘                                   └───────┬────────┘
       │                                                   │
       │ WebSocket / Liveblocks Room Update                │ triggerTask()
       │                                                   ▼
┌──────┴───────┐   Updates Node Storage   ┌─────────────────────────┐
│ Liveblocks   │◄─────────────────────────┤ Trigger.dev Background  │
│ Room State   │                          │ Worker (LLM Generation) │
└──────────────┘                          └─────────────────────────┘
```

1. **Client Action**: User types prompt: *"Design a high-availability e-commerce microservices system"*.
2. **API Trigger**: Frontend sends POST request to `/api/ai/generate`.
3. **Background Job Launch**: API route calls `tasks.trigger("generate-architecture-task", payload)` and returns job ID immediately (`202 Accepted`). No serverless HTTP timeout!
4. **Worker Execution**: Trigger.dev worker runs in the background, calls LLM with Zod JSON schema validation, and computes node X/Y positions using layout algorithm (Dagr / ELK).
5. **Real-time Sync**: Worker streams generated nodes directly into the Liveblocks room state or updates database, rendering nodes on client canvas live.

---

## 🚀 Production Deployment Checklist

Before deploying to Vercel:
1. **Environment Variables**: Verify `.env.production` contains production keys for:
   - `NEXT_PUBLIC_CLERK_PUBLISHABLE_KEY` & `CLERK_SECRET_KEY`
   - `DATABASE_URL` (Neon / Supabase Postgres pooled connection string)
   - `LIVEBLOCKS_SECRET_KEY` (Production room environment)
   - `TRIGGER_SECRET_KEY` & `TRIGGER_API_URL`
   - `BLOB_READ_WRITE_TOKEN` (Vercel Blob)
2. **Prisma Migration**: Run `npx prisma migrate deploy` in build script.
3. **Trigger.dev Deploy**: Run `npx trigger.dev@latest deploy` to publish background tasks to production workers.
"""

with open(guide_path, 'w', encoding='utf-8') as f:
    f.write(content)

print(f"Step-by-step masterclass guide created at {guide_path}")
