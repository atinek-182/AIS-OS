import os
import shutil
import json

base_target = r'd:\AI-OS\references\six-file-context-methodology'
os.makedirs(os.path.join(base_target, '6-file-context-templates'), exist_ok=True)
os.makedirs(os.path.join(base_target, 'feature-specs-library'), exist_ok=True)
os.makedirs(os.path.join(base_target, 'current-issues-templates'), exist_ok=True)

dir1 = r'C:\Users\HP\Downloads\Six-File+Context+Methodology'
dir2 = r'C:\Users\HP\Downloads\01 — How Real Engineers Build  Liveblocks, Trigger.dev-20260717T164124Z-1-001'

# Copy templates from dir1
templates_src = os.path.join(dir1, 'templates')
if os.path.exists(templates_src):
    for root, dirs, files in os.walk(templates_src):
        if '__MACOSX' in root: continue
        for f in files:
            if f.startswith('._'): continue
            src_path = os.path.join(root, f)
            rel_path = os.path.relpath(src_path, templates_src)
            dest_path = os.path.join(base_target, '6-file-context-templates', os.path.basename(f))
            shutil.copy2(src_path, dest_path)
            print(f"Copied template: {os.path.basename(f)}")

# Copy context files from dir2 completed project
context_src = None
for root, dirs, files in os.walk(dir2):
    if root.endswith(os.path.join('context', 'context')):
        context_src = root
        break

if context_src:
    for f in os.listdir(context_src):
        if not f.startswith('._') and os.path.isfile(os.path.join(context_src, f)):
            src_path = os.path.join(context_src, f)
            dest_path = os.path.join(base_target, '6-file-context-templates', f)
            shutil.copy2(src_path, dest_path)
            print(f"Copied completed context file: {f}")

# Copy feature specs from dir2
specs_src = None
for root, dirs, files in os.walk(dir2):
    if root.endswith(os.path.join('feature-specs', 'feature-specs')):
        specs_src = root
        break

if specs_src:
    for f in os.listdir(specs_src):
        if not f.startswith('._') and os.path.isfile(os.path.join(specs_src, f)):
            # normalize filename (remove double .md.md)
            clean_name = f.replace('.md.md', '.md')
            src_path = os.path.join(specs_src, f)
            dest_path = os.path.join(base_target, 'feature-specs-library', clean_name)
            shutil.copy2(src_path, dest_path)
            print(f"Copied feature spec: {clean_name}")

# Copy current issues from dir2
issues_src = None
for root, dirs, files in os.walk(dir2):
    if root.endswith(os.path.join('current-issues', 'current-issues')):
        issues_src = root
        break

if issues_src:
    for f in os.listdir(issues_src):
        if not f.startswith('._') and os.path.isfile(os.path.join(issues_src, f)):
            src_path = os.path.join(issues_src, f)
            dest_path = os.path.join(base_target, 'current-issues-templates', f)
            shutil.copy2(src_path, dest_path)
            print(f"Copied current issue template: {f}")

print("\nIngestion complete! Target files populated under:", base_target)
