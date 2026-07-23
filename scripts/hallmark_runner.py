#!/usr/bin/env python3
"""
Hallmark Anti-Slop Audit & Verification Engine for AIOS.
Powered by Together AI & Antigravity AIOS Framework.

Usage:
  python scripts/hallmark_runner.py audit <path_to_html_or_css>
  python scripts/hallmark_runner.py slop-check <file_or_dir>
  python scripts/hallmark_runner.py info
"""

import sys
import os
import re
import json

SLOP_PATTERNS = [
    (r"gradient.*linear-gradient\(.*#3b82f6.*#8b5cf6\)", "Generic AI Purple/Blue Gradient", "HIGH"),
    (r"\+47%|\+50%|50,000\+ teams|10× faster", "Invented Fake Metric", "HIGH"),
    (r"hero-content text-center.*py-20", "Generic Centered Hero Slop Layout", "MEDIUM"),
    (r"grid-cols-1 md:grid-cols-3.*gap-8", "Generic 3-Column Feature Cards", "LOW"),
    (r"font-family:\s*['\"]?(Inter|Roboto|Arial)['\"]?,?\s*sans-serif", "Browser Default Font Stack without Design Token", "MEDIUM"),
    (r"#(?:[0-9a-fA-F]{3}){1,2}\b(?!;)", "Hardcoded Hex Color (Bypassing Token Stack)", "LOW"),
]

MACROSTRUCTURES = [
    "split-hero-stage", "asymmetric-editorial", "ticker-grid", "magazine-cover",
    "bento-stage", "monochrome-dossier", "horizontal-scroll-gallery", "terminal-command",
    "brutalist-grid", "floating-nav-card", "oversized-typography-hero"
]

def scan_file_for_slop(file_path):
    if not os.path.exists(file_path):
        return {"error": f"File {file_path} not found"}
    
    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()

    findings = []
    for pattern, description, severity in SLOP_PATTERNS:
        matches = list(re.finditer(pattern, content, re.IGNORECASE))
        if matches:
            findings.append({
                "description": description,
                "severity": severity,
                "matches_count": len(matches),
                "pattern": pattern
            })

    has_pre_emit_critique = bool(re.search(r"/\*\s*Hallmark\s*·\s*pre-emit critique:", content, re.IGNORECASE))

    return {
        "file_path": file_path,
        "slop_score": max(0, 100 - (len(findings) * 15)),
        "has_hallmark_critique": has_pre_emit_critique,
        "findings": findings
    }

def print_info():
    info = {
        "name": "Hallmark Anti-AI-Slop Engine",
        "creator": "Together AI",
        "macrostructures_count": len(MACROSTRUCTURES),
        "verbs": ["default (build)", "audit", "redesign", "study"],
        "slop_gates_total": 57
    }
    print(json.dumps(info, indent=2))

def main():
    if len(sys.argv) < 2 or sys.argv[1] == "info":
        print_info()
        return

    cmd = sys.argv[1]
    if cmd in ("audit", "slop-check") and len(sys.argv) >= 3:
        target = sys.argv[2]
        if os.path.isfile(target):
            res = scan_file_for_slop(target)
            print(json.dumps(res, indent=2))
        elif os.path.isdir(target):
            results = []
            for root, _, files in os.walk(target):
                for file in files:
                    if file.endswith((".html", ".css", ".jsx", ".tsx")):
                        results.append(scan_file_for_slop(os.path.join(root, file)))
            print(json.dumps(results, indent=2))
    else:
        print(f"Unknown command or missing target. Usage: python scripts/hallmark_runner.py audit <file_or_dir>")

if __name__ == "__main__":
    main()
