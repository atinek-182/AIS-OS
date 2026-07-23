import os
import sys
import shutil
import re

WORKSPACE_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TRIALS_DIR = os.path.join(WORKSPACE_ROOT, "trials")
RUNNER_PATH = os.path.join(TRIALS_DIR, "runner.py")
MAP_PATH = os.path.join(WORKSPACE_ROOT, "WORKSPACE_MAP.md")

# Boilerplate templates for new trials
PROGRAM_TEMPLATE = """# Autoresearch: {target_name} Protocol

You are an autonomous agent tasked with optimizing the logic in `train.py` to maximize the performance score.

## Objectives
* Improve the output quality, efficiency, or success rate of the candidate code.
* Maximize the evaluation score returned by `prepare.py`.

## Experimentation Rules
1. **Target File**: You are only allowed to edit `train.py`.
2. **Read-Only Lock**: Do NOT modify `prepare.py`.
3. **Execution**: Run the evaluation using `python prepare.py`.
4. **Git Controls**:
   * If the evaluation score increases: Commit the change.
   * If the evaluation score does not improve: Discard the edits.
5. **No Interruption**: Run autonomously.
"""

TRAIN_TEMPLATE = """# Candidate script under test.
# The Autoresearch mutation loop will edit this file to optimize its logic.

def main():
    print("Baseline candidate output")

if __name__ == "__main__":
    main()
"""

PREPARE_TEMPLATE = """import os
import sys
import time
import subprocess

def evaluate_output():
    # Write your scoring logic here. Return a numeric score.
    # Higher scores represent better performance.
    return 10

def main():
    score = evaluate_output()
    print(f"Evaluation Complete. Score: {score}")
    
    # Save the score to results.tsv
    with open("results.tsv", "a") as f:
        f.write(f"{int(time.time())}\\t{score}\\t10\\n")

if __name__ == "__main__":
    main()
"""

def add_target(target_name):
    target_dir = os.path.join(TRIALS_DIR, target_name)
    if os.path.exists(target_dir):
        print(f"Error: Target folder '{target_name}' already exists at {target_dir}")
        return False
        
    print(f"Creating folder structure for '{target_name}'...")
    os.makedirs(target_dir, exist_ok=True)
    os.makedirs(os.path.join(target_dir, "tests"), exist_ok=True)
    
    # Write templates
    with open(os.path.join(target_dir, "program.md"), "w") as f:
        f.write(PROGRAM_TEMPLATE.format(target_name=target_name))
    with open(os.path.join(target_dir, "train.py"), "w") as f:
        f.write(TRAIN_TEMPLATE)
    with open(os.path.join(target_dir, "prepare.py"), "w") as f:
        f.write(PREPARE_TEMPLATE)
    with open(os.path.join(target_dir, "results.tsv"), "w") as f:
        f.write("timestamp\tscore\tmax_score\n")
        
    print("Writing runner registry...")
    update_runner_registry(target_name, add=True)
    
    print("Updating Workspace Map...")
    update_workspace_map(target_name, add=True)
    
    print(f"Success! Trial '{target_name}' initialized and registered successfully.")
    return True

def remove_target(target_name):
    target_dir = os.path.join(TRIALS_DIR, target_name)
    if not os.path.exists(target_dir):
        print(f"Error: Target folder '{target_name}' does not exist.")
        return False
        
    print(f"Deleting folder '{target_name}'...")
    shutil.rmtree(target_dir)
    
    print("Removing runner registry...")
    update_runner_registry(target_name, add=False)
    
    print("Updating Workspace Map...")
    update_workspace_map(target_name, add=False)
    
    print(f"Success! Trial '{target_name}' removed and unregistered.")
    return True

def update_runner_registry(target_name, add=True):
    if not os.path.exists(RUNNER_PATH):
        print("Warning: runner.py not found, skipping registry update.")
        return
        
    with open(RUNNER_PATH, "r") as f:
        content = f.read()
        
    # Match: TARGETS = [...]
    match = re.search(r'TARGETS\s*=\s*\[(.*?)\]', content)
    if not match:
        print("Warning: Could not parse TARGETS list in runner.py")
        return
        
    targets_str = match.group(1)
    targets = [t.strip().strip('"').strip("'") for t in targets_str.split(",") if t.strip()]
    
    if add:
        if target_name not in targets:
            targets.append(target_name)
    else:
        if target_name in targets:
            targets.remove(target_name)
            
    new_targets_str = "TARGETS = [" + ", ".join([f'"{t}"' for t in targets]) + "]"
    new_content = re.sub(r'TARGETS\s*=\s*\[.*?\]', new_targets_str, content)
    
    with open(RUNNER_PATH, "w") as f:
        f.write(new_content)

def update_workspace_map(target_name, add=True):
    if not os.path.exists(MAP_PATH):
        return
        
    with open(MAP_PATH, "r") as f:
        lines = f.readlines()
        
    target_line = f"| [trials/{target_name}/](file:///d:/AI-OS/trials/{target_name}/) | Folder | Autoresearch trial folder for {target_name}. | AIOS / Operator |\n"
    
    new_lines = []
    found = False
    
    for line in lines:
        if f"trials/{target_name}/" in line:
            found = True
            if not add:
                continue # Skip to remove
        new_lines.append(line)
        
        # If adding, insert after templates/trials entry
        if add and "trials/" in line and not found and f"trials/{target_name}/" not in line:
            new_lines.append(target_line)
            found = True
            
    if add and not found:
        # Find where to append
        for i, line in enumerate(new_lines):
            if "### Reference Manuals" in line:
                new_lines.insert(i, target_line)
                break
                
    with open(MAP_PATH, "w") as f:
        f.writelines(new_lines)

def main():
    if len(sys.argv) < 3:
        print("Usage:")
        print("  python manage_autoresearch.py add [target-name]")
        print("  python manage_autoresearch.py remove [target-name]")
        sys.exit(1)
        
    action = sys.argv[1]
    target = sys.argv[2]
    
    if not re.match(r'^[a-zA-Z0-9_-]+$', target):
        print("Error: Invalid target name. Only alphanumeric characters, dashes, and underscores are allowed.")
        sys.exit(1)
        
    if action == "add":
        add_target(target)
    elif action == "remove":
        remove_target(target)
    else:
        print(f"Error: Unknown action '{action}'")

if __name__ == "__main__":
    main()
