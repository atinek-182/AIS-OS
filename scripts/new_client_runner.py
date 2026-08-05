import os
import sys
import json
import re
import shutil
from datetime import datetime

CLIENTS_ROOT = r"d:\AI-OS\clients"
TEMPLATES_DIR = r"d:\AI-OS\brain-aios\wiki\templates\clients"
WORKSPACE_ROOT = r"d:\AI-OS"

def slugify(text):
    text = text.lower().strip()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[\s_-]+', '-', text)
    return text

def get_next_client_id():
    if not os.path.exists(CLIENTS_ROOT):
        os.makedirs(CLIENTS_ROOT, exist_ok=True)
        return "001"
    
    existing = []
    for item in os.listdir(CLIENTS_ROOT):
        full_path = os.path.join(CLIENTS_ROOT, item)
        if os.path.isdir(full_path):
            match = re.match(r'^(\d{3})-', item)
            if match:
                existing.append(int(match.group(1)))
    
    if not existing:
        return "001"
    
    next_id = max(existing) + 1
    return f"{next_id:03d}"

def read_template(filename):
    path = os.path.join(TEMPLATES_DIR, filename)
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    return f"# {filename}\nCreated automatically.\n"

def scaffold_stage1(client_name, channel="Outbound Audit"):
    client_slug = slugify(client_name)
    client_id = get_next_client_id()
    folder_name = f"{client_id}-{client_slug}"
    client_dir = os.path.join(CLIENTS_ROOT, folder_name)
    
    p1 = os.path.join(client_dir, "01-pre-outreach-audit")
    p2 = os.path.join(client_dir, "02-proposal-and-agreement")
    
    os.makedirs(p1, exist_ok=True)
    os.makedirs(p2, exist_ok=True)
    
    today_str = datetime.now().strftime("%Y-%m-%d")
    
    # Audit.md
    t1 = read_template("01-AUDIT.md")
    t1 = t1.replace("{{CLIENT_NAME}}", client_name)
    t1 = t1.replace("{{CLIENT_ID}}", client_id)
    t1 = t1.replace("{{LEAD_CHANNEL}}", channel)
    t1 = t1.replace("{{DATE}}", today_str)
    with open(os.path.join(p1, "AUDIT.md"), "w", encoding="utf-8") as f:
        f.write(t1)
        
    # Proposal.md
    t2 = read_template("02-PROPOSAL.md")
    t2 = t2.replace("{{CLIENT_NAME}}", client_name)
    t2 = t2.replace("{{CLIENT_ID}}", client_id)
    t2 = t2.replace("{{DATE}}", today_str)
    t2 = t2.replace("{{OPTION_1_PRICE}}", "1500")
    t2 = t2.replace("{{OPTION_2_PRICE}}", "3000")
    t2 = t2.replace("{{OPTION_3_PRICE}}", "5000")
    with open(os.path.join(p2, "PROPOSAL.md"), "w", encoding="utf-8") as f:
        f.write(t2)
        
    print(f"SUCCESS: Stage 1 scaffolded for '{client_name}' at '{client_dir}'. Client ID: {client_id}")
    return client_id, folder_name

def scaffold_stage2(client_id_or_slug):
    # Find client dir
    target_dir = None
    if not os.path.exists(CLIENTS_ROOT):
        print(f"ERROR: Clients root directory '{CLIENTS_ROOT}' does not exist.")
        return False
        
    for item in os.listdir(CLIENTS_ROOT):
        full_path = os.path.join(CLIENTS_ROOT, item)
        if os.path.isdir(full_path):
            if item.startswith(f"{client_id_or_slug}-") or item == client_id_or_slug or item.startswith(f"00{client_id_or_slug}-") or item.startswith(f"0{client_id_or_slug}-"):
                target_dir = full_path
                break
                
    if not target_dir:
        print(f"ERROR: Could not find client folder matching '{client_id_or_slug}'.")
        return False
        
    folder_name = os.path.basename(target_dir)
    client_id = folder_name.split("-")[0]
    client_slug = "-".join(folder_name.split("-")[1:])
    client_name = client_slug.replace("-", " ").title()
    today_str = datetime.now().strftime("%Y-%m-%d")
    
    stages = [
        ("03-post-hire-onboarding", "03-INTAKE.md", "INTAKE.md"),
        ("04-architecture-and-specs", "04-SPEC.md", "SPEC.md"),
        ("05-development-and-build", "05-BUILD.md", "BUILD.md"),
        ("06-client-deliverables", "06-HANDOFF.md", "HANDOFF.md"),
        ("07-training-and-offboarding", "07-HANDOVER.md", "HANDOVER.md"),
        ("08-retainer-and-tracker", "08-TRACKER.md", "TRACKER.md"),
    ]
    
    for folder, t_name, out_name in stages:
        p = os.path.join(target_dir, folder)
        os.makedirs(p, exist_ok=True)
        t_content = read_template(t_name)
        t_content = t_content.replace("{{CLIENT_NAME}}", client_name)
        t_content = t_content.replace("{{CLIENT_ID}}", client_id)
        t_content = t_content.replace("{{CLIENT_SLUG}}", client_slug)
        t_content = t_content.replace("{{DATE}}", today_str)
        t_content = t_content.replace("{{CONTRACT_VALUE}}", "3000")
        t_content = t_content.replace("{{BUILD_HOURS}}", "0")
        t_content = t_content.replace("{{HOURLY_RATE}}", "0")
        t_content = t_content.replace("{{PROFIT_MARGIN}}", "0")
        t_content = t_content.replace("{{RETAINER_AMOUNT}}", "0")
        
        out_path = os.path.join(p, out_name)
        if not os.path.exists(out_path):
            with open(out_path, "w", encoding="utf-8") as f:
                f.write(t_content)
                
    # Sub-group deliverables in 06-client-deliverables
    p6 = os.path.join(target_dir, "06-client-deliverables")
    os.makedirs(os.path.join(p6, "01-web-application"), exist_ok=True)
    os.makedirs(os.path.join(p6, "02-automation-workflows"), exist_ok=True)
    os.makedirs(os.path.join(p6, "03-mcp-tools"), exist_ok=True)
    
    print(f"SUCCESS: Stage 2 unlocked and scaffolded for client '{folder_name}'.")
    return True

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python new_client_runner.py [lead <name> | accept <id/slug>]")
        sys.exit(1)
        
    cmd = sys.argv[1].lower()
    if cmd == "accept":
        if len(sys.argv) < 3:
            print("Usage: python new_client_runner.py accept <client_id>")
            sys.exit(1)
        scaffold_stage2(sys.argv[2])
    else:
        # Default is lead scaffolding
        if cmd == "lead" and len(sys.argv) >= 3:
            client_name = " ".join(sys.argv[2:])
        else:
            client_name = " ".join(sys.argv[1:])
        scaffold_stage1(client_name)
