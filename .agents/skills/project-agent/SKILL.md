---
name: project-agent
description: Delegate a complex coding task or feature development to an autonomous developer subagent running in the background of a specific project directory. Use this skill when you want to run a major task, implement a feature, or resolve a bug inside a specific folder in the projects/ directory (e.g. Websites, Zorixel brand, etc.) without cluttering the main conversation window. Format: /project-agent [project-name] "[task description]"
argument-hint: "[project-name] \"[task description]\""
---

# Scoped Project Developer Agent

This skill allows the user to delegate complex features, refactoring, or debugging tasks to an autonomous developer agent running in the background of a specific project directory under `d:\AI-OS\projects\`.

## Invocation Parameters
- **$1 (Project Name):** The name or nested path of the project (e.g., `my-website` or `Websites/my-website`).
- **$2 (Task Description):** The specific programming or content task to perform.

## Execution Workflow

1. **Resolve Target Path:**
   - Check if `d:\AI-OS\projects\$1` exists.
   - If not, search recursively inside `d:\AI-OS\projects\` (including subfolders like `Websites/`, `Zorixel brand/`, `For AIOS/`, `My advisors/`, `Products/`, `Learning/`, `Sandbox/`) for a directory matching `$1` case-insensitively.
   - If exactly one match is found (e.g., `projects/Websites/my-site`), resolve to that path.
   - If multiple matches are found, present them in a list and ask the user to clarify.
   - If no matches are found, output a list of available directories and exit.

2. **Detect Environment & Setup Credentials:**
   - Determine which Google Workspace account to use:
     - If the project path is inside `projects/Zorixel brand/` or related to Zorixel marketing, set:
       `$env:GOOGLE_WORKSPACE_CLI_CREDENTIALS_FILE="C:\Users\HP\.config\gws\credentials_brand.json"`
     - Otherwise, set:
       `$env:GOOGLE_WORKSPACE_CLI_CREDENTIALS_FILE="C:\Users\HP\.config\gws\credentials_personal.json"`
   - The subagent will automatically inherit this environment variable during execution.

3. **Construct the Subagent Prompt:**
   Write a print prompt for the developer subagent structured as follows:
   ```
   You are the lead developer for the project at [RESOLVED_PATH].
   Your task is: [Task Description]

   You must run strictly under the following rules:
   1. Follow the Superpowers workflow:
      - Brainstorm and create a plan first (using brainstorming or plan-first workflows).
      - Write failing tests first (TDD) and verify they fail before writing solution code.
      - Implement the solution.
      - Verify the solution programmatically (run tests, compile, run lints).
   2. Automatically document your work:
      - Locate or create a `walkthrough.md` file at the root of this project folder.
      - Update it with a detailed log of the changes made, tests run, and verification results.
   3. Check for any possibilities of system improvements in the project files and refactor where clean.
   4. Report back with a final summary of modified files, test outputs, and links to the updated documentation.
   ```

4. **Spawn the Background Process:**
   Propose a PowerShell command using the `run_command` tool:
   - **CommandLine:**
     `$env:GOOGLE_WORKSPACE_CLI_CREDENTIALS_FILE="[CREDENTIALS_PATH]"; agy --dangerously-skip-permissions --agent developer --print "[PROMPT]"`
   - **Cwd:** `[RESOLVED_PATH]`
   - **WaitMsBeforeAsync:** `500` (so it sends to the background as a task)
   
   *Tip: You can assign the prompt to a PowerShell variable first to handle multi-line escaping safely, e.g.:*
   `$prompt = '[PROMPT]'; agy --dangerously-skip-permissions --agent developer --print $prompt`

5. **Notification and Monitor:**
   - Tell the user that the project-agent has been dispatched to the background.
   - When the background task completes, read the console output, extract the subagent's final report, and print a clean, high-level summary in the main chat.
