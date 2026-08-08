import os
import yaml
import sys
from pathlib import Path

# Ensure UTF-8 output encoding for Windows terminal
sys.stdout.reconfigure(encoding='utf-8', errors='replace')

TARGET_DIRECTORIES = [
    "context",
    "docs",
    "references",
    "brain-aios",
    "second-brain-zorixel",
    "zorixel-brand-os",
    "projects",
    "clients",
    "audits",
    "decisions",
    "errors-and-lessons",
    ".agents/skills"
]

EXCLUDE_DIRS = {".git", "node_modules", "venv", "scratch", "archives", "graphify-out", ".playwright-mcp", "dist", "build", ".scratch", "skills-library"}

REQUIRED_FIELDS = ["title", "domain", "summary", "critical_directives", "section_outline", "read_triggers", "tags", "updated"]

def is_reparse_or_link(path):
    if os.path.islink(path):
        return True
    if hasattr(os.path, 'isjunction') and os.path.isjunction(path):
        return True
    try:
        attrs = os.stat(path, follow_symlinks=False).st_file_attributes
        if attrs & 1024:  # FILE_ATTRIBUTE_REPARSE_POINT
            return True
    except Exception:
        pass
    return False

def validate_file(file_path, base_dir):
    rel_path = os.path.relpath(file_path, base_dir)
    try:
        with open(file_path, 'r', encoding='utf-8', errors='replace') as f:
            content = f.read()

        if not content.startswith("---"):
            return False, "Missing opening '---' frontmatter boundary"

        parts = content.split("---", 2)
        if len(parts) < 3:
            return False, "Missing closing '---' frontmatter boundary"

        raw_yaml = parts[1]
        data = yaml.safe_load(raw_yaml)

        if not isinstance(data, dict):
            return False, "Frontmatter is not a valid YAML dictionary"

        missing = [field for field in REQUIRED_FIELDS if field not in data]
        if missing:
            return False, f"Missing required fields: {', '.join(missing)}"

        return True, "OK"
    except Exception as e:
        return False, f"YAML Parse Exception: {str(e)}"

def main():
    base_dir = Path("d:/AI-OS")
    valid_count = 0
    invalid_count = 0
    issues = []

    print("[AIOS FRONTMATTER VALIDATOR] Auditing workspace Markdown files...", flush=True)

    for target_dir in TARGET_DIRECTORIES:
        target_path = base_dir / target_dir
        if not target_path.exists():
            continue

        dir_valid = 0
        dir_invalid = 0
        for root, dirs, files in os.walk(target_path, followlinks=False):
            dirs[:] = [d for d in dirs if d not in EXCLUDE_DIRS and not is_reparse_or_link(os.path.join(root, d))]
            for file in files:
                if file.endswith(".md"):
                    file_path = os.path.join(root, file)
                    if is_reparse_or_link(file_path):
                        continue
                    is_valid, msg = validate_file(file_path, base_dir)
                    rel_path = os.path.relpath(file_path, base_dir)
                    if is_valid:
                        valid_count += 1
                        dir_valid += 1
                    else:
                        invalid_count += 1
                        dir_invalid += 1
                        issues.append((rel_path, msg))
        print(f"  [AUDIT] {target_dir}: {dir_valid} valid, {dir_invalid} invalid.", flush=True)

    print(f"\n==========================================", flush=True)
    print(f"AUDIT SUMMARY: {valid_count} Valid | {invalid_count} Invalid", flush=True)
    print(f"==========================================", flush=True)

    if issues:
        print("\n[ISSUES DETECTED]:", flush=True)
        for path, err in issues[:20]:
            print(f"  - {path}: {err}", flush=True)
        if len(issues) > 20:
            print(f"  ... and {len(issues) - 20} more.", flush=True)
        sys.exit(1)
    else:
        print("[SUCCESS] 100% of scanned Markdown files have valid, compliant YAML Frontmatter!", flush=True)

if __name__ == "__main__":
    main()
