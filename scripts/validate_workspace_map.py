import os
import sys
import re

workspace_root = r"d:\AI-OS"
workspace_map_path = os.path.join(workspace_root, "WORKSPACE_MAP.md")

ignored_root_items = {".git", ".obsidian", ".gitignore", ".gitattributes", ".env", "node_modules", "brainstorms", ".playwright-mcp"}

if not os.path.exists(workspace_map_path):
    print("ERROR: WORKSPACE_MAP.md not found at root.")
    sys.exit(1)

with open(workspace_map_path, 'r', encoding='utf-8') as f:
    map_content = f.read()

# 1. Parse markdown links [label](target)
markdown_links = re.findall(r'\[([^\]]+)\]\(([^)]+)\)', map_content)
# 2. Parse inline backtick code blocks `code`
backtick_codes = re.findall(r'`([^`\n]+)`', map_content)

referenced_paths = set()

# Helper to normalize path representation
def normalize_path(path_str):
    # Remove file protocol, clean backslashes, lowercase
    clean = path_str.replace("file:///d:/AI-OS/", "")
    clean = clean.replace("file:///d:/ai-os/", "")
    clean = clean.replace("file:///D:/AI-OS/", "")
    clean = clean.replace("file:///D:/ai-os/", "")
    clean = clean.replace("file:///", "")
    clean = clean.replace("file://", "")
    clean = clean.replace("\\", "/").strip().lower()
    # Strip leading/trailing slashes
    if clean.startswith("/"):
        clean = clean[1:]
    if clean.endswith("/"):
        clean = clean[:-1]
    return clean

# Populate referenced paths from links
for label, target in markdown_links:
    referenced_paths.add(normalize_path(label))
    referenced_paths.add(normalize_path(target))

# Populate referenced paths from code blocks
for code in backtick_codes:
    referenced_paths.add(normalize_path(code))

# Validator helper
def is_mapped(relative_path, is_dir):
    path_clean = relative_path.replace("\\", "/").lower().strip()
    if path_clean.startswith("/"):
        path_clean = path_clean[1:]
    if path_clean.endswith("/"):
        path_clean = path_clean[:-1]

    # Exact match in referenced paths
    if path_clean in referenced_paths:
        return True

    # If it is a directory, it also matches if any referenced path starts with "path_clean/"
    if is_dir:
        for ref in referenced_paths:
            if ref.startswith(path_clean + "/"):
                return True

    return False

unmapped = []

# 1. Scan root level items
for item in os.listdir(workspace_root):
    if item in ignored_root_items:
        continue
    
    item_path = os.path.join(workspace_root, item)
    is_dir = os.path.isdir(item_path)
    if not is_mapped(item, is_dir):
        unmapped.append(f"Root: {item}")

# 2. Scan custom skills in .agents/skills/
skills_dir = os.path.join(workspace_root, ".agents", "skills")
if os.path.exists(skills_dir):
    for skill in os.listdir(skills_dir):
        skill_path = os.path.join(skills_dir, skill)
        if os.path.isdir(skill_path):
            rel_skill_path = f".agents/skills/{skill}"
            if not is_mapped(rel_skill_path, True):
                unmapped.append(f"Workspace Skill: {rel_skill_path}")

# 3. Scan reference manuals in references/
references_dir = os.path.join(workspace_root, "references")
if os.path.exists(references_dir):
    for ref_file in os.listdir(references_dir):
        ref_path = os.path.join(references_dir, ref_file)
        if os.path.isfile(ref_path):
            rel_ref_path = f"references/{ref_file}"
            if not is_mapped(rel_ref_path, False):
                unmapped.append(f"Reference Manual: {rel_ref_path}")

if unmapped:
    print("\n[git pre-commit hook] ERROR: The following items are NOT registered in WORKSPACE_MAP.md:")
    for item in unmapped:
        print(f"  * {item}")
    print("\nPlease register them in WORKSPACE_MAP.md before committing changes.\n")
    sys.exit(1)

print("[git pre-commit hook] SUCCESS: WORKSPACE_MAP.md is fully aligned.")
sys.exit(0)
