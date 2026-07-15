import os
import shutil

claude_root = r"C:\Users\HP\.claude"
target_dir = r"C:\Users\HP\.gemini\config\skills"

os.makedirs(target_dir, exist_ok=True)

copied_skills = {}

# Walk C:\Users\HP\.claude to find all folders named 'skills'
for root, dirs, files in os.walk(claude_root):
    if os.path.basename(root).lower() == 'skills':
        # Check that this is a valid leaf skills folder (not inside .git or node_modules)
        parts = root.split(os.sep)
        if any(p in {'.git', 'node_modules'} for p in parts):
            continue
        
        # Each folder inside this 'skills' directory is a separate skill
        for skill_name in os.listdir(root):
            skill_src_path = os.path.join(root, skill_name)
            if os.path.isdir(skill_src_path):
                # Ensure we only copy from the most relevant source
                # If we've seen this skill name, skip cache folders if we have marketplace ones
                if skill_name in copied_skills:
                    prev_path = copied_skills[skill_name]
                    # Prefer plugins/marketplaces over plugins/cache
                    if 'marketplaces' in prev_path and 'cache' in root:
                        continue
                
                skill_target_path = os.path.join(target_dir, skill_name)
                try:
                    if os.path.exists(skill_target_path):
                        shutil.rmtree(skill_target_path)
                    shutil.copytree(skill_src_path, skill_target_path)
                    copied_skills[skill_name] = root
                except Exception as e:
                    print(f"Error copying {skill_name} from {root}: {e}")

print("\n=== ANTIGRAVITY GLOBAL SKILLS COPY REPORT ===")
print(f"Total unique skills copied: {len(copied_skills)}")
for name, src in sorted(copied_skills.items()):
    print(f"- {name} (from: ...{src[len(claude_root):]})")

print("\n[NOTE] Files have been copied RAW. Run your transpiler script/command to adapt them safely.")

