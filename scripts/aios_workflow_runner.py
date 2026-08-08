import sys
import os
import json

sys.stdout.reconfigure(encoding='utf-8', errors='replace')

WORKFLOWS = {
    "1": {
        "name": "ZORIXEL Client Sprints & Acquisition",
        "description": "End-to-end client discovery, sprint scoping, visual development, and quality audit.",
        "steps": [
            "/grill-with-docs (Conduct socratic interview & build domain glossary in CONTEXT.md)",
            "/to-spec (Synthesize thread into formal spec)",
            "/to-tickets (Break spec into tracer-bullet tickets under .scratch/<sprint>/issues/)",
            "/implement + /website-design-engine + /hallmark (Build UI enforcing solid OKLCH brand tokens)",
            "/code-review (2-axis Standards + Spec diff audit)"
        ]
    },
    "2": {
        "name": "Superpowers Parallel Subagent System",
        "description": "Parallel autonomous feature implementation across independent ticket branches.",
        "steps": [
            "/to-tickets (Break plan into tickets with Blocked by: NN dependency graphs)",
            "subagent-driven-development (Launch parallel subagents per unblocked ticket)",
            "/tdd (Red-green-refactor testing loop per ticket)",
            "verification-before-completion (Run automated verification commands)"
        ]
    },
    "3": {
        "name": "GStack Executive Team Matrix",
        "description": "Garry Tan executive lens review for strategy, engineering depth, UI taste, and QA.",
        "steps": [
            "/gstack ceo (Verify user value & ROI)",
            "/grill-with-docs (Align on requirements & domain glossary)",
            "/gstack eng (Enforce /codebase-design deep modules)",
            "/implement (Build implementation slices test-first)",
            "/gstack qa + /code-review (Execute Playwright browser QA & 2-axis code review)"
        ]
    },
    "4": {
        "name": "Fullstack Next.js & UI Architecture",
        "description": "Production-grade fullstack web app development with type-safe server actions.",
        "steps": [
            "/jsmastery-architect (Define App Router structure, Server Actions, & Zod schemas)",
            "/prototype (Build throwaway UI/animation prototype)",
            "/to-spec (Convert prototype into buildable specification)",
            "/implement + /hallmark (Implement production code enforcing solid design tokens)"
        ]
    },
    "5": {
        "name": "Incident Response & Debugging",
        "description": "Disciplined root-cause bug resolution and technical debt refactoring.",
        "steps": [
            "/diagnosing-bugs (Execute 6-step loop: reproduce -> minimize -> hypothesize -> fix)",
            "/improve-codebase-architecture (Scan codebase for deep-module refactoring)",
            "/vibesec (Run security audit on touched endpoints)"
        ]
    },
    "6": {
        "name": "MCP Server & Application Engineering",
        "description": "Design, package, and integrate custom Model Context Protocol servers & apps.",
        "steps": [
            "/build-mcp-server (Design MCP tools & schema definitions)",
            "/build-mcpb (Package server into standalone binary/bundle)",
            "/build-mcp-app (Add interactive DOM UI widgets & rendering interfaces)",
            "/mcp-integration (Register & test server inside mcp_config.json)"
        ]
    },
    "7": {
        "name": "Multi-Platform SaaS Automation",
        "description": "Build 100% zero-subscription client operational hubs integrating 1000+ SaaS platforms.",
        "steps": [
            "/composio (Connect & execute OAuth actions across 1000+ SaaS apps)",
            "/gws-automation-engine (Provision Google Sheets, Drive folders, & free Apps Scripts)",
            "/notion-sync + /notion-formula-builder (Build Notion master DBs & Formula 2.0)",
            "/zero-paywall-client-os (Deliver zero-subscription client operational hub SOP)"
        ]
    },
    "8": {
        "name": "React Video & Motion Graphics Engine",
        "description": "Programmatic video creation, motion visual ads, and social media media rendering.",
        "steps": [
            "/canvas-design (Generate base vector graphic assets)",
            "/gsap-animation (Define ScrollTrigger physics keyframes)",
            "/remotion (Render programmatic React video compositions)",
            "/carousel-render (Output final HD PNG/MP4 media files)"
        ]
    },
    "9": {
        "name": "Autoresearch & System Observability",
        "description": "Autonomous codebase optimization, benchmark tuning, and AST knowledge graph maintenance.",
        "steps": [
            "/storm-research-project (Run 7-agent multi-perspective technical analysis)",
            "/smart-explore (Perform tree-sitter AST structural code search)",
            "/autoresearch-manage (Execute autonomous optimization loop)",
            "/graphify (Update tree-sitter AST knowledge graph)"
        ]
    },
    "10": {
        "name": "Visual Architecture & Executive Handoff",
        "description": "Awwwards-level visual handoff documentation, architecture diagrams, and slide decks.",
        "steps": [
            "/excalidraw-diagram (Generate visual system topology diagram)",
            "/frontend-slides (Build 16:9 interactive HTML presentation deck)",
            "/interactive-operator-guide-generator (Build copyable setup dashboard & SOP)",
            "/wowerpoint (Compile executive PDF slide deck for client delivery)"
        ]
    }
}

def print_help():
    print("ZORIXEL AIOS Master Workflows Orchestrator CLI")
    print("Usage:")
    print("  python scripts/aios_workflow_runner.py list")
    print("  python scripts/aios_workflow_runner.py inspect <1-10>")

def main():
    if len(sys.argv) < 2:
        print_help()
        sys.exit(0)

    cmd = sys.argv[1].lower()
    if cmd == "list":
        print("=== ZORIXEL AIOS 10 MASTER INTEGRATED WORKFLOWS ===")
        for key, wf in WORKFLOWS.items():
            print(f"Workflow {key}: {wf['name']}")
            print(f"  {wf['description']}")
            print(f"  Steps ({len(wf['steps'])}): {' -> '.join([s.split()[0] for s in wf['steps']])}")
            print("-" * 50)
    elif cmd == "inspect" and len(sys.argv) >= 3:
        key = sys.argv[2]
        if key in WORKFLOWS:
            wf = WORKFLOWS[key]
            print(f"=== WORKFLOW {key}: {wf['name']} ===")
            print(f"Description: {wf['description']}\n")
            print("Execution Sequence:")
            for idx, step in enumerate(wf["steps"], 1):
                print(f"  Step {idx}: {step}")
        else:
            print(f"Error: Unknown workflow '{key}'. Valid choices: 1 to 10.")
    else:
        print_help()

if __name__ == "__main__":
    main()
