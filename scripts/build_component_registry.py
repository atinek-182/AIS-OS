import os
import json
import re

RAW_DIR = r"d:\AI-OS\premium-frontend-experience-system\raw\Raw Components"
OUTPUT_JSON = r"d:\AI-OS\premium-frontend-experience-system\source-registries\component-registry-index.json"
OUTPUT_MD = r"d:\AI-OS\premium-frontend-experience-system\source-registries\MASTER_COMPONENT_CATALOG.md"

def clean_component_name(raw_name):
    name = raw_name.replace("**", "").replace("(Fav)", "").replace("(Most Fav)", "").replace("cli cmd:", "").strip()
    name = re.sub(r'^[:\s\-]+|[:\s\-]+$', '', name)
    return name

def parse_files():
    registry = {
        "metadata": {
            "title": "Master Component Registry Index",
            "version": "1.0.0",
            "libraries": ["Aceternity UI", "Animate UI React", "Forge UI", "Vengence UI"]
        },
        "components": []
    }

    files = [f for f in os.listdir(RAW_DIR) if f.endswith(".md")]
    for filename in files:
        filepath = os.path.join(RAW_DIR, filename)
        library_name = filename.replace(".md", "").replace("(Fav)", "").strip()
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()

        current_category = "General"
        lines = content.splitlines()
        for line in lines:
            line_str = line.strip()
            if not line_str:
                continue
            if line_str.startswith("## "):
                current_category = line_str.replace("## ", "").replace("I liked", "").replace(":-", "").strip()
                continue
            if line_str.startswith("# "):
                continue

            # Skip pure doc/guide header links if they aren't specific components
            if any(k in line_str.lower() for k in ["for docs -", "for components -", "for labs -", "for primitives -", "for icons -", "also link:"]):
                continue

            if "**" in line_str or "npx shadcn" in line_str or "http" in line_str:
                is_fav = "(Fav)" in line_str or "(Most Fav)" in line_str
                
                # Extract name
                name_match = re.search(r'\*\*(.*?)\*\*', line_str)
                raw_name = name_match.group(1).strip() if name_match else ""
                if not raw_name and "-" in line_str:
                    raw_name = line_str.split("-")[0].strip()
                
                clean_name = clean_component_name(raw_name)
                
                # Extract CLI command
                cli_match = re.search(r'(npx shadcn[^\s]* add [^\s\n]+(\s+[^\s\n]+)?)', line_str)
                cli_cmd = cli_match.group(1).strip() if cli_match else ""

                # Extract URL
                url_match = re.search(r'https?://[^\s]+', line_str)
                url = url_match.group(0).strip() if url_match else ""

                if clean_name or cli_cmd or url:
                    registry["components"].append({
                        "name": clean_name if clean_name else "Unnamed Component",
                        "library": library_name,
                        "category": current_category if current_category else "General",
                        "cli_command": cli_cmd,
                        "url": url,
                        "is_favorite": is_fav,
                        "raw_line": line_str
                    })

    # Save JSON
    with open(OUTPUT_JSON, "w", encoding="utf-8") as f:
        json.dump(registry, f, indent=2)

    # Save Markdown Catalog
    md_output = []
    md_output.append("# Master UI Component Catalog\n")
    md_output.append("> **Mandatory System Directive**: Before creating any new UI component or visual block for ZORIXEL or web applications, Antigravity MUST search this catalog to install and adapt a matching component.\n")
    md_output.append(f"Total Components Indexed: **{len(registry['components'])}**\n")

    by_library = {}
    for comp in registry["components"]:
        lib = comp["library"]
        if lib not in by_library:
            by_library[lib] = []
        by_library[lib].append(comp)

    for lib, comps in by_library.items():
        md_output.append(f"## {lib} ({len(comps)} Components)\n")
        md_output.append("| Component Name | Category | Favorite | CLI Command / URL |")
        md_output.append("|---|---|---|---|")
        for c in comps:
            fav_str = "⭐ YES" if c["is_favorite"] else "No"
            cmd_url = f"`{c['cli_command']}`" if c['cli_command'] else f"[Docs Link]({c['url']})" if c['url'] else "N/A"
            md_output.append(f"| **{c['name']}** | {c['category']} | {fav_str} | {cmd_url} |")
        md_output.append("\n")

    with open(OUTPUT_MD, "w", encoding="utf-8") as f:
        f.write("\n".join(md_output))

    print(f"Successfully indexed {len(registry['components'])} components into {OUTPUT_JSON} and {OUTPUT_MD}")

if __name__ == "__main__":
    parse_files()
