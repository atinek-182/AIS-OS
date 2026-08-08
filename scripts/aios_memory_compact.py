import os
import sys
import re
import datetime

# Force UTF-8 stdout
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

root_dir = r"d:\AI-OS"
decisions_log = os.path.join(root_dir, "decisions", "log.md")
archive_dir = os.path.join(root_dir, "decisions", "archive")
memory_file = os.path.join(root_dir, "MEMORY.md")

os.makedirs(archive_dir, exist_ok=True)

def parse_decisions(content):
    # Splits decisions log by decision entry headers (e.g. ## Decision ... or ### [2026-...)
    entries = []
    current_entry = []
    current_title = "Header"
    current_date = "2026-08-07"
    
    date_pattern = re.compile(r'\b(202\d-[0-1]\d-[0-3]\d)\b')

    for line in content.splitlines():
        if line.startswith("# ") or line.startswith("## ") or line.startswith("### "):
            if current_entry:
                entries.append({
                    "title": current_title,
                    "date": current_date,
                    "text": "\n".join(current_entry)
                })
                current_entry = []
            current_title = line
            dmatch = date_pattern.search(line)
            if dmatch:
                current_date = dmatch.group(1)
        current_entry.append(line)
        
    if current_entry:
        entries.append({
            "title": current_title,
            "date": current_date,
            "text": "\n".join(current_entry)
        })
        
    return entries

def get_quarter(date_str):
    try:
        dt = datetime.datetime.strptime(date_str, "%Y-%m-%d")
        quarter = (dt.month - 1) // 3 + 1
        return f"{dt.year}-Q{quarter}"
    except Exception:
        return "2026-Q1"

def compact_decisions(dry_run=False):
    print("==================================================")
    print(" ZORIXEL AIOS: DECISION LOG & MEMORY AUTO-COMPACTOR ")
    print("==================================================")
    
    if not os.path.exists(decisions_log):
        print(f"[ERROR] Decisions log not found at: {decisions_log}")
        return
        
    with open(decisions_log, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()
        
    lines = content.splitlines()
    print(f"[STATUS] Initial decisions/log.md stats: {len(lines)} lines | {len(content.split())} words")
    
    entries = parse_decisions(content)
    print(f"[STATUS] Parsed decision blocks: {len(entries)} total entries")
    
    today = datetime.datetime.now()
    active_entries = []
    archived_by_quarter = {}
    
    for entry in entries:
        try:
            dt = datetime.datetime.strptime(entry["date"], "%Y-%m-%d")
            age_days = (today - dt).days
        except Exception:
            age_days = 0
            
        # Keep entries younger than 60 days in active log, archive older
        if age_days < 60 or entry["title"].startswith("# ZORIXEL AIOS"):
            active_entries.append(entry)
        else:
            q_key = get_quarter(entry["date"])
            if q_key not in archived_by_quarter:
                archived_by_quarter[q_key] = []
            archived_by_quarter[q_key].append(entry)
            
    print(f"[STATUS] Active entries retained: {len(active_entries)}")
    print(f"[STATUS] Quarters to archive: {list(archived_by_quarter.keys())}")
    
    if dry_run:
        print("\n[DRY RUN COMPLETE] No files modified.")
        return

    # Write archived entries to quarterly archive files
    for q_key, q_entries in archived_by_quarter.items():
        q_file = os.path.join(archive_dir, f"{q_key}.md")
        archive_content = f"# ZORIXEL AIOS Decisions Archive — {q_key}\n\n"
        archive_content += f"*Archived on: {today.strftime('%Y-%m-%d')} · Total Entries: {len(q_entries)}*\n\n"
        archive_content += "\n\n---\n\n".join([e["text"] for e in q_entries])
        
        with open(q_file, "w", encoding="utf-8") as f:
            f.write(archive_content)
        print(f"[OK] Archived {len(q_entries)} entries into: {q_file}")

    # Rewrite active decisions log
    new_log_content = "# ZORIXEL AIOS System Decisions Log (`decisions/log.md`)\n\n"
    new_log_content += f"> **Active Log Status**: Compacted on {today.strftime('%Y-%m-%d')}. Historical decisions are archived in [decisions/archive/](file:///d:/AI-OS/decisions/archive/).\n\n"
    
    if archived_by_quarter:
        new_log_content += "## Archived Quarters Index\n"
        for q_key in sorted(archived_by_quarter.keys()):
            new_log_content += f"- [{q_key} Archive](file:///d:/AI-OS/decisions/archive/{q_key}.md) ({len(archived_by_quarter[q_key])} decisions)\n"
        new_log_content += "\n---\n\n"
        
    new_log_content += "\n\n---\n\n".join([e["text"] for e in active_entries if not e["title"].startswith("# ZORIXEL AIOS")])

    with open(decisions_log, "w", encoding="utf-8") as f:
        f.write(new_log_content)
        
    new_lines = len(new_log_content.splitlines())
    print(f"[SUCCESS] Decisions log compacted: {len(lines)} lines -> {new_lines} lines!")

    # Self-Improving Step: Append system evolution entry to MEMORY.md if missing
    if os.path.exists(memory_file):
        with open(memory_file, "r", encoding="utf-8", errors="ignore") as f:
            mem_content = f.read()
            
        evo_marker = "## System Auto-Evolution Log"
        if evo_marker not in mem_content:
            mem_content += f"\n\n{evo_marker}\n- **{today.strftime('%Y-%m-%d')}**: Automated decision log compaction executed. Historical logs archived under `decisions/archive/` keeping active log high-density under 250 lines.\n"
            with open(memory_file, "w", encoding="utf-8") as f:
                f.write(mem_content)
            print("[OK] MEMORY.md updated with Auto-Evolution Log entry.")

if __name__ == "__main__":
    dry_run_flag = "--dry-run" in sys.argv
    compact_decisions(dry_run=dry_run_flag)
