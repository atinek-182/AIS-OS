import os
import re
import yaml

SKILLS_DIR = r"d:\AI-OS\.agents\skills"

def parse_frontmatter(content):
    if not content.startswith("---"):
        return None, content
    
    parts = content.split("---", 2)
    if len(parts) < 3:
        return None, content
    
    try:
        fm = yaml.safe_load(parts[1])
        body = parts[2]
        return fm, body
    except Exception as e:
        print(f"YAML Parse error: {e}")
        return None, content

def standardize_skill(skill_dir):
    skill_name = os.path.basename(skill_dir)
    skill_file = os.path.join(skill_dir, "SKILL.md")
    
    if not os.path.isfile(skill_file):
        print(f"Skipping {skill_name}: SKILL.md not found.")
        return
    
    with open(skill_file, "r", encoding="utf-8") as f:
        content = f.read()
    
    fm, body = parse_frontmatter(content)
    
    if fm is None:
        print(f"Warning: No YAML frontmatter in {skill_name}, creating default.")
        fm = {
            "name": skill_name,
            "description": f"Use when running {skill_name} or invoking /{skill_name}.",
            "argument-hint": "[optional parameters]"
        }
    else:
        # Ensure name matches directory name
        fm["name"] = skill_name
        
        # Ensure argument-hint exists
        if "argument-hint" not in fm or not fm["argument-hint"]:
            fm["argument-hint"] = "[optional parameters]"
        
        # Ensure description mentions slash command
        desc = fm.get("description", "")
        if f"/{skill_name}" not in desc:
            fm["description"] = f"{desc.strip()} Invokable directly via /{skill_name}."
    
    # Check if Invocation & Tri-Mode Routing section exists in body
    invocation_block = f"""
## ⚡ Invocation & Tri-Mode Routing

This skill supports **Tri-Mode Flexible Execution**:
- **Slash Command**: Explicitly run `/{skill_name} {fm.get('argument-hint', '[args]')}` in chat.
- **Dynamic Intent Matching**: Triggered automatically when task context involves keywords in the description.
- **Inter-Skill & AIOS Calling**: Programmatically invokable by parent skills or subagents via `/{skill_name}` or by reading `SKILL.md` directly.
"""

    if "## ⚡ Invocation & Tri-Mode Routing" not in body and "## ⚡ Dual-Trigger" not in body:
        # Append or insert after first heading
        lines = body.split("\n")
        insert_idx = 0
        for i, line in enumerate(lines):
            if line.startswith("# "):
                insert_idx = i + 1
                break
        
        lines.insert(insert_idx, invocation_block)
        body = "\n".join(lines)
    
    # Reconstruct file content
    new_fm_str = yaml.dump(fm, sort_keys=False, allow_unicode=True).strip()
    new_content = f"---\n{new_fm_str}\n---\n{body}"
    
    with open(skill_file, "w", encoding="utf-8") as f:
        f.write(new_content)
    
    print(f"Successfully standardized: {skill_name}")

def main():
    if not os.path.exists(SKILLS_DIR):
        print(f"Error: {SKILLS_DIR} does not exist.")
        return
    
    skills = [os.path.join(SKILLS_DIR, d) for d in os.listdir(SKILLS_DIR) if os.path.isdir(os.path.join(SKILLS_DIR, d))]
    print(f"Found {len(skills)} skills to audit.")
    
    for s in sorted(skills):
        standardize_skill(s)

if __name__ == "__main__":
    main()
