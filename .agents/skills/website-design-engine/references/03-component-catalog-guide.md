# 🧩 Phase 3 Reference: 147 Component Catalog & Sourcing Guide

## 1. Mandatory Component Sourcing Rule

When building UI sections, **do NOT invent generic placeholder divs from scratch**. You MUST query your local 147-component catalog using the CLI tool:

```bash
python scripts/component_registry_cli.py search "<category or effect keyword>"
```

### Example Commands:
- Search backgrounds: `python scripts/component_registry_cli.py search "background"`
- Search cards: `python scripts/component_registry_cli.py search "card"`
- Search text animation: `python scripts/component_registry_cli.py search "text"`
- Filter favorite components: `python scripts/component_registry_cli.py search "hero" --favorite-only`

---

## 2. 147 Component Library Breakdown (21 Categories)

### A. Aceternity UI (56 Components)
- **Backgrounds & FX**: Background Beams, Wavy Background, Aurora Background, Shooting Stars, Sparkles, Vortex, Canvas Reveal Effect.
- **Card Components**: Card 3D, Focus Cards, Glowing Stars, Direction Aware Hover, Hover Effect, Evergreen Bento Grid.
- **Hero & Navigation**: Hero Parallax, Floating Navbar, Navbar Menu, Container Scroll Animation, Sticky Scroll Reveal.
- **Interactive Text**: Text Generate Effect, Typewriter Effect, Flip Words, Cover, Text Hover Effect.

### B. Animate UI React (42 Components)
- **Buttons & Controls**: Dynamic Action Buttons, Smooth Border Buttons, Magnetic Buttons.
- **Text & Motion**: Morphing Text, Kinetic Word Reveal, Split Text Reveal, Counting Numbers.
- **Layout & Overlays**: Smooth Accordions, Animated Tabs, Dynamic Tooltips, Glass Drawers.

### C. Vengence UI (37 Components)
- **Visual FX**: Ambient Glowing Cards, Gradient Border Wrappers, Glassmorphism Panels, Floating Navbars.

### D. Forge UI (12 Components)
- **App Containers**: Action Cards, Drawer Popovers, Modal Dialogs, Interactive Sliders.

---

## 3. Shadcn MCP Integration

For standard primitive components (buttons, dialogs, dropdowns, inputs, tables), query the `shadcn` MCP server:
1. `search_items_in_registries`: Search Shadcn registry items.
2. `get_add_command_for_items`: Get exact `npx shadcn@latest add <component>` installation commands.
