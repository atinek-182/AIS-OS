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

def infer_domain(rel_path_str):
    path_lower = rel_path_str.lower().replace("\\", "/")
    if "skill" in path_lower or ".agents/skills" in path_lower:
        return "skill"
    elif "brand" in path_lower:
        return "brand"
    elif "decision" in path_lower:
        return "decision"
    elif "audit" in path_lower:
        return "audit"
    elif "research" in path_lower:
        return "research"
    elif "sop" in path_lower or "guide" in path_lower:
        return "SOP"
    elif "task" in path_lower or "checklist" in path_lower:
        return "task"
    return "architecture"

def parse_existing_frontmatter(content):
    if content.startswith("---"):
        parts = content.split("---", 2)
        if len(parts) >= 3:
            raw_yaml = parts[1]
            body = parts[2]
            try:
                data = yaml.safe_load(raw_yaml)
                if isinstance(data, dict):
                    return data, body
            except Exception:
                pass
    return {}, content

def extract_headings(lines):
    headings = []
    for line in lines:
        stripped = line.strip()
        if stripped.startswith("#") and not stripped.startswith("#####"):
            h_text = stripped.lstrip("#").strip()
            if h_text and len(h_text) < 80:
                headings.append(h_text)
            if len(headings) >= 5:
                break
    return headings

def extract_directives(lines):
    directives = []
    keywords = ("mandatory", "must", "never", "always", "rule", "important", "warning", "caution")
    for line in lines:
        stripped = line.strip()
        if stripped.startswith(">") or stripped.startswith("-") or stripped.startswith("*"):
            lower = stripped.lower()
            if any(k in lower for k in keywords):
                clean_text = stripped.lstrip("> -*").strip()
                if clean_text.startswith("[!") and "]" in clean_text:
                    clean_text = clean_text.split("]", 1)[1].strip()
                if clean_text and len(clean_text) > 10:
                    directives.append(clean_text[:120])
                if len(directives) >= 4:
                    break
    if not directives:
        directives = ["Follow document guidance without bypassing established safeguards."]
    return directives[:4]

def extract_summary(lines, title):
    paragraphs = []
    for line in lines:
        stripped = line.strip()
        if stripped and not stripped.startswith("#") and not stripped.startswith("---") and not stripped.startswith(">"):
            if len(stripped) > 20:
                paragraphs.append(stripped)
            if len(paragraphs) >= 2:
                break
    if paragraphs:
        return " ".join(paragraphs)[:250]
    return f"Documentation and architectural context for {title}."

def extract_title(lines, filename):
    for line in lines:
        stripped = line.strip()
        if stripped.startswith("# "):
            return stripped[2:].strip()
    return Path(filename).stem.replace("-", " ").replace("_", " ").title()

def process_file(file_path, base_dir):
    try:
        rel_path = os.path.relpath(file_path, base_dir)
        with open(file_path, 'r', encoding='utf-8', errors='replace') as f:
            content = f.read()

        existing_data, body = parse_existing_frontmatter(content)
        lines = body.splitlines()

        title = existing_data.get("title") or extract_title(lines, file_path)
        domain = existing_data.get("domain") or infer_domain(rel_path)
        summary = existing_data.get("summary") or extract_summary(lines, title)

        directives = existing_data.get("critical_directives")
        if not directives:
            directives = extract_directives(lines)

        headings = existing_data.get("section_outline")
        if not headings:
            headings = extract_headings(lines)
            if not headings:
                headings = [title]

        read_triggers = existing_data.get("read_triggers")
        if not read_triggers:
            read_triggers = [
                f"When working on {domain} in {rel_path.replace('\\', '/')}",
                f"When reading context for {title}"
            ]

        tags = existing_data.get("tags")
        if not tags:
            tags = [domain, Path(file_path).stem]

        frontmatter_dict = {
            "title": title,
            "domain": domain,
            "summary": summary,
            "critical_directives": directives,
            "section_outline": headings,
            "read_triggers": read_triggers,
            "tags": tags,
            "updated": "2026-08-08"
        }

        for k, v in existing_data.items():
            if k not in frontmatter_dict:
                frontmatter_dict[k] = v

        formatted_yaml = yaml.dump(frontmatter_dict, sort_keys=False, allow_unicode=True, width=120).strip()
        new_content = f"---\n{formatted_yaml}\n---\n\n{body.lstrip()}"

        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)

        return True, rel_path
    except Exception as e:
        return False, f"{rel_path}: {str(e)}"

def main():
    base_dir = Path("d:/AI-OS")
    processed_count = 0
    error_count = 0

    print("[AIOS FRONTMATTER STANDARDIZER] Fast sweep running...", flush=True)

    for target_dir in TARGET_DIRECTORIES:
        target_path = base_dir / target_dir
        if not target_path.exists():
            print(f"  [SKIP] {target_dir} (Does not exist)", flush=True)
            continue

        dir_processed = 0
        for root, dirs, files in os.walk(target_path, followlinks=False):
            dirs[:] = [d for d in dirs if d not in EXCLUDE_DIRS and not is_reparse_or_link(os.path.join(root, d))]
            for file in files:
                if file.endswith(".md"):
                    file_path = os.path.join(root, file)
                    if is_reparse_or_link(file_path):
                        continue
                    success, msg = process_file(file_path, base_dir)
                    if success:
                        processed_count += 1
                        dir_processed += 1
                    else:
                        print(f"  [ERROR] {msg}", flush=True)
                        error_count += 1
        print(f"  [DONE] {target_dir}: {dir_processed} files processed.", flush=True)

    print(f"\n[SUCCESS] Standardized YAML Frontmatter across {processed_count} Markdown files ({error_count} errors).", flush=True)

if __name__ == "__main__":
    main()
