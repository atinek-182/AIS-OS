---
name: ingest-skills
description: Automatically clone a community skill or reference manual repository from GitHub, copy its modules into the Obsidian wiki skills library, register the paths, and index them in logs. Use when running "/ingest-skills [repo_url]".
---

# Ingest Community Skills & References

Automate the progressive-disclosure cloning and indexing of massive community skills databases.

## Use When
- The user provides a GitHub repository link for Claude/Cursor/Antigravity skills, rules, or reference manuals.
- You run `/ingest-skills [repo_url]` or say "ingest this skill repository".

## Steps

1. **Extract Repository Name**:
   - Determine the name of the repository from the URL (e.g. `github.com/user/repo-name` -> `repo-name`).

2. **Clone & Extract**:
   - Create a temporary folder inside `scratch/` (e.g. `scratch/temp_ingest`).
   - Run `git clone [repo_url] scratch/temp_ingest` to download the assets.
   - Look for standard directories: `skills/`, `rules/`, `.cursorrules`, `.cursor/rules/`.

3. **Copy to Research Library**:
   - Create a target subdirectory at `brain-aios/wiki/research/skills-library/[repo-name]/`.
   - Copy all markdown guides, configuration files, and folders from the source `skills` or `rules` directory into the target folder.

4. **Register and Index**:
   - Add the new directory path `| [brain-aios/wiki/research/skills-library/[repo-name]/](file:///d:/AI-OS/brain-aios/wiki/research/skills-library/[repo-name]/) | Folder | Static reference library for [repo-name]. | AIOS |` to [WORKSPACE_MAP.md](file:///d:/AI-OS/WORKSPACE_MAP.md).
   - Add an index link `* [[wiki/research/skills-library/[repo-name]/|[Repo Name] Reference Library]] — Cloned community guide.` to [brain-aios/wiki/index.md](file:///d:/AI-OS/brain-aios/wiki/index.md).
   - Log the ingest event `## [YYYY-MM-DD] ingest | [repo_url] -> Created static [[wiki/research/skills-library/[repo-name]/]] reference library.` inside [brain-aios/wiki/log.md](file:///d:/AI-OS/brain-aios/wiki/log.md).
   - Append details of the ingest in [decisions/log.md](file:///d:/AI-OS/decisions/log.md).

5. **Clean up & Validate**:
   - Force-delete the temporary `scratch/temp_ingest` folder.
   - Run the map validator script `python scripts/validate_workspace_map.py` to ensure map compliance.
