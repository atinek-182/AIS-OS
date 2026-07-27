import json
import re
import os

INDEX_FILE = r"d:\AI-OS\premium-frontend-experience-system\source-registries\component-registry-index.json"
CATALOG_MD = r"d:\AI-OS\premium-frontend-experience-system\source-registries\MASTER_COMPONENT_CATALOG.md"

NEW_LIBRARIES = [
    "Magic UI",
    "21st.dev",
    "Motion Primitives",
    "React Bits",
    "Origin UI",
    "Kokonut UI / Cult UI",
    "Uiverse"
]

NEW_COMPONENTS = [
    # Magic UI
    {
        "name": "Animated Beam",
        "library": "Magic UI",
        "category": "Backgrounds & Effects",
        "cli_command": "npx shadcn@latest add https://magicui.design/r/animated-beam",
        "url": "https://magicui.design/docs/components/animated-beam",
        "is_favorite": True,
        "pattern": "hero"
    },
    {
        "name": "Retro Grid",
        "library": "Magic UI",
        "category": "Backgrounds & Effects",
        "cli_command": "npx shadcn@latest add https://magicui.design/r/retro-grid",
        "url": "https://magicui.design/docs/components/retro-grid",
        "is_favorite": True,
        "pattern": "backgrounds"
    },
    {
        "name": "Particles",
        "library": "Magic UI",
        "category": "Backgrounds & Effects",
        "cli_command": "npx shadcn@latest add https://magicui.design/r/particles",
        "url": "https://magicui.design/docs/components/particles",
        "is_favorite": True,
        "pattern": "backgrounds"
    },
    {
        "name": "Orbiting Circles",
        "library": "Magic UI",
        "category": "Data & Visualization",
        "cli_command": "npx shadcn@latest add https://magicui.design/r/orbiting-circles",
        "url": "https://magicui.design/docs/components/orbiting-circles",
        "is_favorite": True,
        "pattern": "hero"
    },
    {
        "name": "Rainbow Button",
        "library": "Magic UI",
        "category": "Buttons",
        "cli_command": "npx shadcn@latest add https://magicui.design/r/rainbow-button",
        "url": "https://magicui.design/docs/components/rainbow-button",
        "is_favorite": True,
        "pattern": "buttons"
    },
    {
        "name": "Shine Border",
        "library": "Magic UI",
        "category": "Card Components",
        "cli_command": "npx shadcn@latest add https://magicui.design/r/shine-border",
        "url": "https://magicui.design/docs/components/shine-border",
        "is_favorite": True,
        "pattern": "bento"
    },
    {
        "name": "Animated List",
        "library": "Magic UI",
        "category": "Layouts",
        "cli_command": "npx shadcn@latest add https://magicui.design/r/animated-list",
        "url": "https://magicui.design/docs/components/animated-list",
        "is_favorite": False,
        "pattern": "scrollytelling"
    },
    {
        "name": "Velocity Scroll",
        "library": "Magic UI",
        "category": "Text Components",
        "cli_command": "npx shadcn@latest add https://magicui.design/r/scroll-based-velocity",
        "url": "https://magicui.design/docs/components/scroll-based-velocity",
        "is_favorite": True,
        "pattern": "hero"
    },
    {
        "name": "Gradual Spacing Text",
        "library": "Magic UI",
        "category": "Text Components",
        "cli_command": "npx shadcn@latest add https://magicui.design/r/gradual-spacing",
        "url": "https://magicui.design/docs/components/gradual-spacing",
        "is_favorite": False,
        "pattern": "hero"
    },

    # 21st.dev
    {
        "name": "Glow Card Matrix",
        "library": "21st.dev",
        "category": "Card Components",
        "cli_command": "npx 21st@latest add glow-card-matrix",
        "url": "https://21st.dev/r/glow-card-matrix",
        "is_favorite": True,
        "pattern": "bento"
    },
    {
        "name": "Fluid Glass Cursor",
        "library": "21st.dev",
        "category": "Overlays & Popovers",
        "cli_command": "npx 21st@latest add fluid-glass-cursor",
        "url": "https://21st.dev/r/fluid-glass-cursor",
        "is_favorite": True,
        "pattern": "backgrounds"
    },
    {
        "name": "Radial Glow Hero",
        "library": "21st.dev",
        "category": "Layouts",
        "cli_command": "npx 21st@latest add radial-glow-hero",
        "url": "https://21st.dev/r/radial-glow-hero",
        "is_favorite": True,
        "pattern": "hero"
    },

    # Motion Primitives
    {
        "name": "Morphing Dialog",
        "library": "Motion Primitives",
        "category": "Overlays & Popovers",
        "cli_command": "npx shadcn@latest add https://motion-primitives.com/r/morphing-dialog",
        "url": "https://motion-primitives.com/docs/morphing-dialog",
        "is_favorite": True,
        "pattern": "modal"
    },
    {
        "name": "Text Effect Loop",
        "library": "Motion Primitives",
        "category": "Text Components",
        "cli_command": "npx shadcn@latest add https://motion-primitives.com/r/text-effect",
        "url": "https://motion-primitives.com/docs/text-effect",
        "is_favorite": True,
        "pattern": "hero"
    },
    {
        "name": "Accordion Transition",
        "library": "Motion Primitives",
        "category": "Navigation",
        "cli_command": "npx shadcn@latest add https://motion-primitives.com/r/accordion",
        "url": "https://motion-primitives.com/docs/accordion",
        "is_favorite": False,
        "pattern": "forms"
    },

    # React Bits
    {
        "name": "Raymarching Noise Background",
        "library": "React Bits",
        "category": "Backgrounds & Effects",
        "cli_command": "npx react-bits@latest add raymarching-noise",
        "url": "https://reactbits.dev/backgrounds/raymarching-noise",
        "is_favorite": True,
        "pattern": "backgrounds"
    },
    {
        "name": "Distorted Text Warp",
        "library": "React Bits",
        "category": "Text Components",
        "cli_command": "npx react-bits@latest add distorted-text",
        "url": "https://reactbits.dev/text-animations/distorted-text",
        "is_favorite": True,
        "pattern": "hero"
    },
    {
        "name": "Iridescence Shader Card",
        "library": "React Bits",
        "category": "Card Components",
        "cli_command": "npx react-bits@latest add iridescence-card",
        "url": "https://reactbits.dev/components/iridescence",
        "is_favorite": True,
        "pattern": "3d-cards"
    },

    # Origin UI
    {
        "name": "Micro Input Group",
        "library": "Origin UI",
        "category": "Inputs & Forms",
        "cli_command": "npx shadcn@latest add @originui/input-group",
        "url": "https://originui.com/inputs",
        "is_favorite": False,
        "pattern": "forms"
    },
    {
        "name": "Tooltip Range Slider",
        "library": "Origin UI",
        "category": "Inputs & Forms",
        "cli_command": "npx shadcn@latest add @originui/slider-tooltip",
        "url": "https://originui.com/sliders",
        "is_favorite": True,
        "pattern": "pricing"
    },
    {
        "name": "Multi-Step Form Stepper",
        "library": "Origin UI",
        "category": "Inputs & Forms",
        "cli_command": "npx shadcn@latest add @originui/stepper",
        "url": "https://originui.com/steppers",
        "is_favorite": True,
        "pattern": "forms"
    },

    # Kokonut UI / Cult UI
    {
        "name": "AI Chat Bento Interface",
        "library": "Kokonut UI / Cult UI",
        "category": "Layouts",
        "cli_command": "npx kokonut@latest add ai-chat-bento",
        "url": "https://kokonutui.com/components/ai-chat-bento",
        "is_favorite": True,
        "pattern": "bento"
    },
    {
        "name": "Interactive Pricing Matrix",
        "library": "Kokonut UI / Cult UI",
        "category": "Card Components",
        "cli_command": "npx cultui@latest add pricing-matrix",
        "url": "https://www.cultui.com/docs/components/pricing-matrix",
        "is_favorite": True,
        "pattern": "pricing"
    },

    # Uiverse
    {
        "name": "Cyberpunk Neon Button",
        "library": "Uiverse",
        "category": "Buttons",
        "cli_command": "npx uiverse@latest get button-neon-cyber",
        "url": "https://uiverse.io/buttons/neon-cyber",
        "is_favorite": False,
        "pattern": "buttons"
    },
    {
        "name": "Glassmorphism Card Border",
        "library": "Uiverse",
        "category": "Card Components",
        "cli_command": "npx uiverse@latest get glass-card-border",
        "url": "https://uiverse.io/cards/glass-border",
        "is_favorite": False,
        "pattern": "bento"
    }
]

def auto_assign_pattern(c):
    cat = c.get("category", "").lower()
    name = c.get("name", "").lower()
    
    if "pattern" in c and c["pattern"]:
        return c["pattern"]
        
    if "nav" in name or "header" in name or "sidebar" in name or "dock" in name or "notch" in name:
        return "navigation"
    if "hero" in name or "parallax" in name or "macbook" in name or "globe" in name:
        return "hero"
    if "price" in name or "pricing" in name or "cost" in name:
        return "pricing"
    if "card" in name or "bento" in name or "grid" in name or "board" in name:
        return "bento"
    if "scroll" in name or "timeline" in name or "tracing" in name or "scrolly" in name:
        return "scrollytelling"
    if "modal" in name or "dialog" in name or "preview" in name or "popover" in name:
        return "modal"
    if "form" in name or "input" in name or "signup" in name or "upload" in name or "button" in name:
        return "forms"
    if "3d" in name or "shader" in name or "canvas" in name or "globe" in name:
        return "3d-cards"
    if "background" in cat or "sparkle" in name or "star" in name:
        return "backgrounds"
        
    return "bento"

def run_expansion():
    with open(INDEX_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)

    # 1. Expand libraries list
    existing_libs = set(data["metadata"]["libraries"])
    for lib in NEW_LIBRARIES:
        existing_libs.add(lib)
    data["metadata"]["libraries"] = sorted(list(existing_libs))

    # 2. Assign pattern to existing components
    for c in data["components"]:
        c["pattern"] = auto_assign_pattern(c)

    # 3. Add new components
    existing_names = set(c["name"].lower() for c in data["components"])
    added_count = 0
    for nc in NEW_COMPONENTS:
        if nc["name"].lower() not in existing_names:
            nc["raw_line"] = f"**{nc['name']} -** {nc['cli_command'] if nc['cli_command'] else nc['url']}"
            data["components"].append(nc)
            added_count += 1

    # Save index
    with open(INDEX_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print(f"Updated index JSON: Total components = {len(data['components'])} (Added {added_count} new entries).")

    # 4. Generate Master Catalog Markdown
    lines = [
        "# Master UI Component Catalog",
        "",
        "> **Mandatory System Directive**: Before creating any new UI component or visual block for ZORIXEL or web applications, Antigravity MUST search this catalog to install and adapt a matching component.",
        "",
        f"Total Components Indexed: **{len(data['components'])}** (Enriched with 100% URLs, CLI Commands, and UX Pattern Tags)",
        ""
    ]

    # Group by Library
    components_by_lib = {}
    for c in data["components"]:
        lib = c["library"]
        if lib not in components_by_lib:
            components_by_lib[lib] = []
        components_by_lib[lib].append(c)

    for lib, comps in sorted(components_by_lib.items()):
        lines.append(f"## {lib} ({len(comps)} Components)")
        lines.append("")
        lines.append("| Component Name | Category | UX Pattern | Favorite | CLI Command | Doc Link |")
        lines.append("|---|---|---|---|---|---|")
        for c in comps:
            fav = "⭐ YES" if c.get("is_favorite") else "No"
            cli = f"`{c['cli_command']}`" if c.get('cli_command') else "-"
            link = f"[View Component Docs]({c['url']})" if c.get('url') else "-"
            pattern = f"`{c.get('pattern', 'bento')}`"
            lines.append(f"| **{c['name']}** | {c['category']} | {pattern} | {fav} | {cli} | {link} |")
        lines.append("")

    with open(CATALOG_MD, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    print(f"Master Catalog markdown regenerated at {CATALOG_MD}")

if __name__ == "__main__":
    run_expansion()
