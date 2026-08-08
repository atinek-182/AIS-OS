# Phase 3 Reference: 300+ Component Catalog & Sourcing Guide (v4.0)

## Top Priority Precedence Hierarchy

When building UI components, follow the strict 4-level precedence hierarchy:

1. **Priority 1 [TOP PRIORITY]**: **Six-File Context & Project Codebase Specs** (`TECH_STACK.md`, `REQUIREMENTS.md`, `ARCHITECTURE.md`, `PROJECT.md`, existing TSX components).
2. **Priority 2**: **Project-Local Visual Assets** (`reference/*.png`, `reference/*.html`, `reference/*.mp4`).
3. **Priority 3**: **Operator Favorite Components** (`component_registry_cli.py search "<keyword>" --favorite-only`).
4. **Priority 4**: **300+ Component Catalog** (`references/23-sites-matrix.json` & `python scripts/design_synthesis_engine.py search-pattern <query>`).

---

## 300+ Component Catalog Search CLI

Query your local component catalog using the CLI tool:

```bash
python scripts/component_registry_cli.py search "<category or effect keyword>"
```

### Example Commands:
- Search backgrounds: `python scripts/component_registry_cli.py search "background"`
- Search cards: `python scripts/component_registry_cli.py search "card"`
- Search text animation: `python scripts/component_registry_cli.py search "text"`
- Filter favorite components: `python scripts/component_registry_cli.py search "hero" --favorite-only`

---

## Catalog Library Breakdown (11 Libraries across 23 Reference Sites)

### A. Aceternity UI & Animate UI React
- **Backgrounds & FX**: Background Beams, Wavy Background, Aurora Background, Shooting Stars, Sparkles, Vortex, Canvas Reveal Effect.
- **Card Components**: Card 3D, Focus Cards, Glowing Stars, Direction Aware Hover, Hover Effect, Evergreen Bento Grid.
- **Hero & Navigation**: Hero Parallax, Floating Navbar, Navbar Menu, Container Scroll Animation, Sticky Scroll Reveal.
- **Interactive Text**: Text Generate Effect, Typewriter Effect, Flip Words, Cover, Text Hover Effect.

### B. 23-Sites Extracted Showroom (300+ TSX/CSS Components)
- **Active Theory / Obys / Locomotive**: Custom GLSL shader stages, split-text kinetic typography, magnetic cursor triggers, full-page scrollytelling.

---

## Component JSX & SVG Geometry Safeguards

1. **JSX SVG Style Object Conversion**: Convert inline SVG `style="..."` string attributes into camelCase JSX style objects (`style={{...}}`) during conversion to prevent React runtime rendering errors.
2. **Invisible Placeholder Filter**: Filter out invisible background placeholders (`if not child.get("visible", True): continue`) during symbol extraction.
3. **SVG Stroke Bleed Prevention (Rule 1.17)**: Never apply CSS/SVG `stroke` or `stroke-width` attributes to converted text path SVGs that contain inner counter holes ('o', 'e', 'a'). Enforce pure solid fills with `fill-rule="evenodd"`.

---

## Shadcn MCP Integration

For standard primitive components (buttons, dialogs, dropdowns, inputs, tables), query the `shadcn` MCP server:
1. `search_items_in_registries`: Search Shadcn registry items.
2. `get_add_command_for_items`: Get exact `npx shadcn@latest add <component>` installation commands.
