"""
23-Site AIOS Design Synthesis & Intelligence Engine
Lightweight, zero-bloat CLI indexer and recommendation engine synthesizing 23 award-winning reference sites.
Addresses /roast Contrarian risk by decoupling indexing from LLM context and enforcing strict snippet limits.
"""

import os
import sys
import json
import re
import argparse
from pathlib import Path

WORKSPACE_ROOT = Path(__file__).resolve().parent.parent
SITES_DIR = WORKSPACE_ROOT / "premium-frontend-experience-system" / "reference-inputs" / "sites"
INDEX_FILE = WORKSPACE_ROOT / "references" / "23-sites-matrix.json"


def scan_and_index_sites():
    """Scans all 23 sites in reference-inputs/sites and extracts design matrix data."""
    if not SITES_DIR.exists():
        print(f"Error: Sites directory not found at {SITES_DIR}")
        return {}

    matrix = {
        "sites_count": 0,
        "sites": {},
        "section_taxonomy": {
            "hero": [],
            "nav": [],
            "bento_feature": [],
            "stage_3d_canvas": [],
            "proof_metrics": [],
            "case_study": [],
            "pricing": [],
            "faq": [],
            "footer": []
        },
        "animation_profiles": {},
        "color_palettes": {}
    }

    site_dirs = [d for d in SITES_DIR.iterdir() if d.is_dir()]
    print(f"[INDEXER] Indexing {len(site_dirs)} reference sites...")

    for site_dir in sorted(site_dirs):
        site_name = site_dir.name
        dna_file = site_dir / "site-dna.md"
        analysis_file = site_dir / "DEEP_ANALYSIS.md"
        extracts_dir = site_dir / "code-extracts"

        dna_content = dna_file.read_text(encoding="utf-8", errors="ignore") if dna_file.exists() else ""
        analysis_content = analysis_file.read_text(encoding="utf-8", errors="ignore") if analysis_file.exists() else ""

        # Component extraction scan
        components = []
        if extracts_dir.exists():
            for root, _, files in os.walk(extracts_dir):
                for f in files:
                    if f.endswith((".tsx", ".jsx", ".ts", ".js")):
                        full_path = Path(root) / f
                        rel_path = str(full_path.relative_to(WORKSPACE_ROOT)).replace("\\", "/")
                        category = Path(root).name
                        components.append({
                            "name": f,
                            "category": category,
                            "path": rel_path
                        })

        # Classify sections based on component names and analysis
        section_tags = set()
        for comp in components:
            name_lower = comp["name"].lower()
            if "hero" in name_lower or "header" in name_lower:
                section_tags.add("hero")
                matrix["section_taxonomy"]["hero"].append({"site": site_name, "component": comp["name"], "path": comp["path"]})
            if "nav" in name_lower or "menu" in name_lower:
                section_tags.add("nav")
                matrix["section_taxonomy"]["nav"].append({"site": site_name, "component": comp["name"], "path": comp["path"]})
            if "bento" in name_lower or "feature" in name_lower or "card" in name_lower or "grid" in name_lower:
                section_tags.add("bento_feature")
                matrix["section_taxonomy"]["bento_feature"].append({"site": site_name, "component": comp["name"], "path": comp["path"]})
            if "canvas" in name_lower or "3d" in name_lower or "three" in name_lower or "webgl" in name_lower or "stage" in name_lower:
                section_tags.add("stage_3d_canvas")
                matrix["section_taxonomy"]["stage_3d_canvas"].append({"site": site_name, "component": comp["name"], "path": comp["path"]})
            if "footer" in name_lower:
                section_tags.add("footer")
                matrix["section_taxonomy"]["footer"].append({"site": site_name, "component": comp["name"], "path": comp["path"]})

        # Extract Color & Motion cues
        has_gsap = "gsap" in dna_content.lower() or "gsap" in analysis_content.lower()
        has_three = "three" in dna_content.lower() or "webgl" in dna_content.lower() or "canvas" in dna_content.lower()
        has_framer = "framer-motion" in dna_content.lower() or "motion" in analysis_content.lower()

        site_entry = {
            "name": site_name,
            "dna_summary": dna_content[:300].replace("\n", " ") + "..." if dna_content else "DNA available on disk.",
            "components_count": len(components),
            "components": components,
            "section_tags": list(section_tags),
            "tech_stack": {
                "gsap": has_gsap,
                "three_webgl": has_three,
                "framer_motion": has_framer
            }
        }

        matrix["sites"][site_name] = site_entry
        matrix["animation_profiles"][site_name] = {
            "gsap": has_gsap,
            "webgl": has_three,
            "motion": has_framer
        }

    matrix["sites_count"] = len(matrix["sites"])

    # Ensure output directory exists
    INDEX_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(INDEX_FILE, "w", encoding="utf-8") as f:
        json.dump(matrix, f, indent=2)

    print(f"[SUCCESS] Successfully indexed {matrix['sites_count']} sites into {INDEX_FILE}")
    return matrix


def search_pattern(query, max_results=3):
    """Searches the lightweight matrix index returning capped snippet results to prevent context bloat."""
    if not INDEX_FILE.exists():
        print("Index file not found. Running index process...")
        matrix = scan_and_index_sites()
    else:
        with open(INDEX_FILE, "r", encoding="utf-8") as f:
            matrix = json.load(f)

    query_lower = query.lower()
    matches = []

    # Search in taxonomy
    for sec_type, items in matrix.get("section_taxonomy", {}).items():
        if query_lower in sec_type:
            for item in items[:max_results]:
                matches.append({
                    "type": "taxonomy",
                    "section": sec_type,
                    "site": item["site"],
                    "component": item["component"],
                    "path": item["path"]
                })

    # Search in site components
    for site_name, site_data in matrix.get("sites", {}).items():
        if query_lower in site_name.lower():
            for comp in site_data.get("components", [])[:max_results]:
                matches.append({
                    "type": "component",
                    "site": site_name,
                    "component": comp["name"],
                    "path": comp["path"]
                })
        else:
            for comp in site_data.get("components", []):
                if query_lower in comp["name"].lower():
                    matches.append({
                        "type": "component",
                        "site": site_name,
                        "component": comp["name"],
                        "path": comp["path"]
                    })

    # Deduplicate & cap
    unique_matches = []
    seen = set()
    for m in matches:
        key = (m["site"], m["component"])
        if key not in seen:
            seen.add(key)
            unique_matches.append(m)
            if len(unique_matches) >= max_results:
                break

    print(json.dumps({
        "query": query,
        "results_count": len(unique_matches),
        "results": unique_matches
    }, indent=2))


def recommend_layout(niche="saas"):
    """Returns a recommended section sequence & design archetype synthesized from reference sites."""
    recommendations = {
        "saas": {
            "niche": "AI SaaS / Product Launch",
            "recommended_archetype": "Interactive WebGL Stage + Bento Feature Grid",
            "inspired_by": ["oryzo-ai", "active-theory", "grids-obys-agency"],
            "section_sequence": [
                "1. Nav (Header_01 with logo, nav links, CTA)",
                "2. Hero (Interactive WebGL/Canvas Stage + High-Contrast Headline)",
                "3. Social Proof (Metrics Ticker & Press Badges)",
                "4. Agitation / Problem (2-Column Visual Contrast Grid)",
                "5. Solution Bento (Modular 3x3 Bento Feature Cards with magnetic hover)",
                "6. Performance & Tech Proof (Interactive Spec Sandbox)",
                "7. Pricing & Offers (Clean 3-Tier Card Comparison)",
                "8. Action CTA (High-Contrast Magnetic Contact Stage)",
                "9. Footer (Multi-Column Links + Noise Texture Overlay)"
            ],
            "typography_stack": "Outfit (Headings) + Inter (Body)",
            "motion_profile": "GSAP ScrollTrigger Inertia + Spring Physics"
        },
        "agency": {
            "niche": "High-Ticket Design / Dev Studio",
            "recommended_archetype": "Obys Horizontal Grid + Custom Split-Text Reveal",
            "inspired_by": ["grids-obys-agency", "locomotive-agency", "merci-michel"],
            "section_sequence": [
                "1. Minimal Floating Nav",
                "2. Hero (Massive Typographic Punch + Custom Noise Mask)",
                "3. Manifesto / Philosophy Section (Split-Type Scroll Reveal)",
                "4. Selected Works (Fullscreen Canvas Preview Stage)",
                "5. Capability Bento Grid (Hover Video/Image Previews)",
                "6. Awards & Client Proof Matrix",
                "7. Magnetic Project Inquiry CTA",
                "8. Modern Dark Mode Footer"
            ],
            "typography_stack": "Rosehot / Nuqun (Brand Display) + Outfit (Headings)",
            "motion_profile": "Magnetic Cursor + Smooth Inertia Scroll"
        }
    }

    selected = recommendations.get(niche.lower(), recommendations["saas"])
    print(json.dumps(selected, indent=2))


def main():
    parser = argparse.ArgumentParser(description="23-Site AIOS Design Synthesis & Intelligence Engine")
    subparsers = parser.add_subparsers(dest="command")

    # Index command
    subparsers.add_parser("index", help="Index all 23 reference sites")

    # Search command
    search_parser = subparsers.add_parser("search-pattern", help="Search design components & taxonomy")
    search_parser.add_argument("query", help="Keyword or section type to search")
    search_parser.add_argument("--max-results", type=int, default=3, help="Max results to return (prevents token bloat)")

    # Recommend command
    rec_parser = subparsers.add_parser("recommend-layout", help="Get recommended section sequence")
    rec_parser.add_argument("--niche", type=str, default="saas", help="Niche (saas, agency, creator)")

    args = parser.parse_args()

    if args.command == "index":
        scan_and_index_sites()
    elif args.command == "search-pattern":
        search_pattern(args.query, args.max_results)
    elif args.command == "recommend-layout":
        recommend_layout(args.niche)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
