import os
import sys

# Force UTF-8 standard output encoding on Windows console
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

root_dir = r"d:\AI-OS"

def read_first_n_lines(path, n=15):
    if not os.path.exists(path):
        return None
    try:
        with open(path, "r", encoding="utf-8", errors="ignore") as f:
            lines = [f.readline().strip() for _ in range(n)]
        return [l for l in lines if l]
    except Exception:
        return None

def main():
    print("=== ZORIXEL AIOS CHAT BOOTUP CONTEXT SNAPSHOT ===")
    
    # 1. Master Index Pointer
    print(f"Master Index: {os.path.join(root_dir, 'context', '00_MASTER_INDEX.md')}")
    
    # 2. Active Session Focus (hot.md)
    hot_p = os.path.join(root_dir, "hot.md")
    hot_lines = read_first_n_lines(hot_p, 10)
    if hot_lines:
        print("\n--- ACTIVE SESSION FOCUS (hot.md) ---")
        for l in hot_lines:
            print(f"  {l}")
            
    # 3. Persistent Memory Highlights (MEMORY.md)
    mem_p = os.path.join(root_dir, "MEMORY.md")
    mem_lines = read_first_n_lines(mem_p, 10)
    if mem_lines:
        print("\n--- PERSISTENT MEMORY HIGHLIGHTS (MEMORY.md) ---")
        for l in mem_lines:
            print(f"  {l}")
            
    # 4. Master Task Status
    task_p = os.path.join(root_dir, "brain-aios", "wiki", "checklists", "master-task-list.md")
    task_lines = read_first_n_lines(task_p, 10)
    if task_lines:
        print("\n--- CANONICAL TASK STATUS ---")
        for l in task_lines:
            print(f"  {l}")
            
    print("\n--- MANDATORY ACTION DIRECTIVE ---")
    print("Before pitching features or writing code, run: python scripts/aios_deep_search.py '<query>'")
    print("==================================================")

if __name__ == "__main__":
    main()
