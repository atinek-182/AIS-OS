import os
import re
import sys

# Base directory for the premium frontend experience system
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'premium-frontend-experience-system'))

def get_all_markdown_files(base_dir):
    """
    Returns a dictionary of all markdown files mapping their lowercase basename (without .md)
    to their absolute paths.
    """
    md_map = {}
    for root, _, files in os.walk(base_dir):
        # Skip git or system directories
        if '.git' in root or '.obsidian' in root:
            continue
        for file in files:
            if file.endswith('.md'):
                name_key = os.path.splitext(file)[0].lower()
                abs_path = os.path.abspath(os.path.join(root, file))
                # Store absolute path
                md_map[name_key] = abs_path
    return md_map

def check_file_links(file_path, md_map):
    """
    Scans a markdown file for relative links and Obsidian bracket links [[WikiLink]],
    verifying if the targets exist.
    Returns a list of errors (broken links).
    """
    errors = []
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Match Obsidian bracket links: [[WikiLink]] or [[WikiLink#Section]] or [[WikiLink|Label]]
    # Regex matches [[anything except ]]
    bracket_links = re.findall(r'\[\[([^\]]+)\]\]', content)
    for link in bracket_links:
        # Strip section anchors or custom labels
        clean_link = link.split('#')[0].split('|')[0].strip()
        if not clean_link:
            continue
        
        # Check if the clean link refers to a file name in our vault map
        link_key = clean_link.lower()
        # Also check if it might be an absolute/relative path within the bracket
        # (e.g. [[workflows/README]] or [[README]])
        link_key_base = os.path.basename(clean_link).lower().replace('.md', '')
        
        # Skip template placeholders
        if link_key in ['project_brief', 'wikilink'] or link_key_base in ['project_brief', 'wikilink']:
            continue
            
        if link_key not in md_map and link_key_base not in md_map:
            # Check if it exists as a direct physical file relative to this file
            rel_check = os.path.abspath(os.path.join(os.path.dirname(file_path), clean_link))
            if not os.path.exists(rel_check) and not os.path.exists(rel_check + '.md'):
                errors.append(f"Broken Obsidian link: [[{link}]]")


    # 2. Match standard relative markdown links: [label](path)
    # Exclude external URLs (http, https) and symbols/variables (e.g. [url])
    markdown_links = re.findall(r'\[[^\]]*\]\(([^)]+)\)', content)
    for link in markdown_links:
        link = link.strip()
        # Skip external links, anchors, or placeholders/place-variables
        if (link.startswith('http://') or 
            link.startswith('https://') or 
            link.startswith('#') or 
            '[' in link or 
            ']' in link or
            link == '[url]'):
            continue
        
        # Parse file scheme if any
        if link.startswith('file:///'):
            # Convert URI to absolute OS path
            path = link.replace('file:///', '')
            # Under Windows, check if it starts with drive letter
            if os.name == 'nt' and path[1] == ':':
                pass
            else:
                path = '/' + path
            resolved_path = os.path.abspath(path)
        else:
            # Resolve relative to the containing file's directory
            # Strip anchors if any
            clean_path = link.split('#')[0]
            if not clean_path:
                continue
            resolved_path = os.path.abspath(os.path.join(os.path.dirname(file_path), clean_path))
        
        # Verify existence
        if not os.path.exists(resolved_path):
            errors.append(f"Broken relative link: ({link}) -> Resolved to: {resolved_path}")

    return errors

def main():
    scan_dir = sys.argv[1] if len(sys.argv) > 1 else BASE_DIR
    scan_dir = os.path.abspath(scan_dir)
    
    if not os.path.exists(scan_dir):
        print(f"Error: Scan directory {scan_dir} does not exist.")
        sys.exit(1)

    print(f"Scanning markdown files at: {scan_dir}...")
    md_map = get_all_markdown_files(scan_dir)
    
    # If scanning a specific subproject, also pull in the core system's markdown map
    # so cross-system references to global files (like [[POLICIES.md]] or [[README]]) resolve correctly.
    if scan_dir != BASE_DIR and os.path.exists(BASE_DIR):
        system_map = get_all_markdown_files(BASE_DIR)
        for k, v in system_map.items():
            if k not in md_map:
                md_map[k] = v

    print(f"Found {len(md_map)} markdown files in scope for WikiLink resolution.")

    total_errors = 0
    # Walk all files under the directory
    for root, _, files in os.walk(scan_dir):
        if '.git' in root or '.obsidian' in root:
            continue
        for file in files:
            if file.endswith('.md'):
                abs_path = os.path.abspath(os.path.join(root, file))
                errors = check_file_links(abs_path, md_map)
                if errors:
                    rel_file = os.path.relpath(abs_path, scan_dir)
                    print(f"\n[ERROR] Broken links in {rel_file}:")
                    for err in errors:
                        print(f"  - {err}")
                    total_errors += len(errors)

    if total_errors > 0:
        print(f"\n[FAIL] Found {total_errors} broken links.")
        sys.exit(1)
    else:
        print("\n[SUCCESS] All Obsidian bracket links and relative Markdown links resolved successfully.")
        sys.exit(0)

if __name__ == '__main__':
    main()

