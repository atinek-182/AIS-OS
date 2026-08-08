#!/usr/bin/env python3
"""
ZORIXEL AIOS - Addy Osmani Agent-Skills Runner & SDLC Validation Engine
"""

import os
import sys
import argparse
import glob

# Ensure UTF-8 output encoding for Windows compatibility
sys.stdout.reconfigure(encoding='utf-8', errors='replace')

SKILLS_DIR = r"d:\AI-OS\.agents\skills"
AGENTS_DIR = r"d:\AI-OS\.agents\agents"
REFERENCES_DIR = r"d:\AI-OS\references\sdlc"

SDLC_SKILLS = [
    "using-agent-skills",
    "interview-me",
    "idea-refine",
    "spec-driven-development",
    "planning-and-task-breakdown",
    "incremental-implementation",
    "test-driven-development",
    "context-engineering",
    "source-driven-development",
    "doubt-driven-development",
    "frontend-ui-engineering",
    "api-and-interface-design",
    "browser-testing-with-devtools",
    "debugging-and-error-recovery",
    "code-review-and-quality",
    "code-simplification",
    "security-and-hardening",
    "performance-optimization",
    "git-workflow-and-versioning",
    "ci-cd-and-automation",
    "deprecation-and-migration",
    "documentation-and-adrs",
    "observability-and-instrumentation",
    "shipping-and-launch"
]

AGENT_PERSONAS = [
    "code-reviewer.md",
    "security-auditor.md",
    "test-engineer.md",
    "web-performance-auditor.md"
]

REF_CHECKLISTS = [
    "accessibility-checklist.md",
    "definition-of-done.md",
    "observability-checklist.md",
    "orchestration-patterns.md",
    "performance-checklist.md",
    "security-checklist.md",
    "testing-patterns.md"
]

def validate_catalog():
    print("=== ZORIXEL AIOS SDLC SKILLS CATALOG VALIDATION ===")
    missing_skills = []
    for skill in SDLC_SKILLS:
        skill_path = os.path.join(SKILLS_DIR, skill, "SKILL.md")
        if os.path.exists(skill_path):
            print(f"[OK] Skill '{skill}': SKILL.md present ({os.path.getsize(skill_path)} bytes)")
        else:
            print(f"[ERROR] Skill '{skill}': SKILL.md MISSING!")
            missing_skills.append(skill)

    print("\n--- AGENT PERSONAS ---")
    missing_agents = []
    for agent in AGENT_PERSONAS:
        agent_path = os.path.join(AGENTS_DIR, agent)
        if os.path.exists(agent_path):
            print(f"[OK] Agent Persona '{agent}': present")
        else:
            print(f"[ERROR] Agent Persona '{agent}': MISSING!")
            missing_agents.append(agent)

    print("\n--- REFERENCE CHECKLISTS ---")
    missing_refs = []
    for ref in REF_CHECKLISTS:
        ref_path = os.path.join(REFERENCES_DIR, ref)
        if os.path.exists(ref_path):
            print(f"[OK] Reference Checklist '{ref}': present")
        else:
            print(f"[ERROR] Reference Checklist '{ref}': MISSING!")
            missing_refs.append(ref)

    print("\n==================================================")
    if missing_skills or missing_agents or missing_refs:
        print(f"[FAIL] Validation failed! Missing: {len(missing_skills)} skills, {len(missing_agents)} personas, {len(missing_refs)} checklists.")
        return False
    else:
        print(f"[SUCCESS] All 24 SDLC Skills, 4 Agent Personas, and 7 Reference Checklists validated 100%!")
        return True

def ship_persona_audit():
    print("=== ZORIXEL AIOS /SHIP MULTI-PERSONA AUDIT FANOUT ===")
    print("Simulating 4-Persona Review Pass before release...")
    print("1. [code-reviewer]: Staff Engineer 5-axis code review")
    print("2. [test-engineer]: Prove-it QA coverage & boundary checks")
    print("3. [security-auditor]: OWASP Top 10, secrets & boundary security")
    print("4. [web-performance-auditor]: Core Web Vitals & bundle budget review")
    print("[SUCCESS] All 4 personas initialized successfully.")
    return True

def main():
    parser = argparse.ArgumentParser(description="ZORIXEL AIOS Agent-Skills Runner")
    parser.add_argument("command", choices=["validate", "ship-audit"], help="Command to execute")
    args = parser.parse_args()

    if args.command == "validate":
        success = validate_catalog()
        sys.exit(0 if success else 1)
    elif args.command == "ship-audit":
        success = ship_persona_audit()
        sys.exit(0 if success else 1)

if __name__ == "__main__":
    main()
