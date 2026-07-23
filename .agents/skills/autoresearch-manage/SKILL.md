---
name: autoresearch-manage
description: Use when managing Autoresearch loop targets — adding new optimization trials, removing obsolete ones, or registering folders.
argument-hint: "[add|remove] [target-name]"
---

# Autoresearch Loop Targets Manager

This skill helps you easily add or remove optimization targets for the Autoresearch self-improving loops. It manages the directory structure, adds boilerplate code, updates the main execution runner, and synchronizes the Workspace Map.

---

## How it works

The management script lives at [manage_autoresearch.py](file:///d:/AI-OS/scripts/manage_autoresearch.py). It automates all folder creation and target registration steps.

---

## Instructions

### Step 1: Parse Arguments
* If arguments specify `add [target-name]`, proceed to **Step 2 (Add Target)**.
* If arguments specify `remove [target-name]`, proceed to **Step 3 (Remove Target)**.
* If no arguments are provided, ask the user if they want to add or remove a target, and prompt for the name.

### Step 2: Add a Target
Run the management script to bootstrap a new trial target:
```powershell
python scripts/manage_autoresearch.py add [target-name]
```
This automatically:
1. Creates `trials/[target-name]/` directory.
2. Scaffolds `program.md` (optimization protocol), `train.py` (candidate code), and `prepare.py` (scoring harness).
3. Adds the target to the `TARGETS` list inside `trials/runner.py`.
4. Registers the new path in `WORKSPACE_MAP.md`.

### Step 3: Remove a Target
To clean up and unregister a trial:
```powershell
python scripts/manage_autoresearch.py remove [target-name]
```
This automatically:
1. Deletes the folder from `trials/`.
2. Removes the target from the `TARGETS` list inside `trials/runner.py`.
3. Unregisters the path from `WORKSPACE_MAP.md`.
