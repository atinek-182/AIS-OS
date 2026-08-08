#!/usr/bin/env python
import os
import sys
import json
import argparse
import glob
import re

# Ensure standard UTF-8 encoding on Windows console
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

SECURITY_OS_DIR = r"d:\AI-OS\SecurityOs"
SKILLS_DIR = os.path.join(SECURITY_OS_DIR, "skills")

def load_domain_index():
    if not os.path.exists(SKILLS_DIR):
        print(f"[ERROR] SecurityOs skills directory not found at {SKILLS_DIR}")
        return []
    skills = [d for d in os.listdir(SKILLS_DIR) if os.path.isdir(os.path.join(SKILLS_DIR, d))]
    return sorted(skills)

def search_skills(query, domain_filter=None):
    skills = load_domain_index()
    results = []
    query_lower = query.lower()
    for s in skills:
        if domain_filter and domain_filter.lower() not in s.lower():
            continue
        if query_lower in s.lower():
            results.append(s)
    return results

def run_audit(target_path, severity_level="HIGH"):
    print(f"[SECURITY_OS AUDIT] Target: {target_path} | Threshold: {severity_level}")
    vulnerabilities = []
    
    # Static pattern rules
    patterns = [
        {"id": "SEC-001", "name": "Hardcoded Secret / Token", "severity": "CRITICAL", "regex": r"(?i)(api[_-]?key|secret|password|bearer|token)\s*=\s*['\"][A-Za-z0-9_\-]{16,}['\"]"},
        {"id": "SEC-002", "name": "Potential SQL Injection", "severity": "CRITICAL", "regex": r"(?i)SELECT\s+.*\s+FROM\s+.*WHERE\s+.*\+"},
        {"id": "SEC-003", "name": "Potential SSRF Vector", "severity": "HIGH", "regex": r"(?i)fetch\s*\(\s*(req\.query|req\.body|url|inputUrl)"},
        {"id": "SEC-004", "name": "Missing Zod / Input Sanitization", "severity": "HIGH", "regex": r"(?i)app\.(post|put|patch)\(.*req\.body"},
        {"id": "SEC-005", "name": "Insecure CORS Wildcard", "severity": "MEDIUM", "regex": r"(?i)Access-Control-Allow-Origin['\"]\s*:\s*['\"]\*\s*['\"]"},
        {"id": "SEC-006", "name": "Prompt Injection Exposure", "severity": "HIGH", "regex": r"(?i)user[_-]?prompt\s*\+\s*input"},
    ]
    
    if os.path.isfile(target_path):
        files_to_check = [target_path]
    else:
        files_to_check = []
        for root, dirs, files in os.walk(target_path):
            if any(p in root for p in ['.git', 'node_modules', '__pycache__', '.venv', 'SecurityOs']):
                continue
            for f in files:
                if f.endswith(('.js', '.ts', '.tsx', '.jsx', '.py', '.json', '.html', '.md')):
                    files_to_check.append(os.path.join(root, f))
                    
    for filepath in files_to_check:
        try:
            with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
                content = f.read()
                for line_num, line in enumerate(content.splitlines(), start=1):
                    for pat in patterns:
                        if re.search(pat["regex"], line):
                            vulnerabilities.append({
                                "file": os.path.relpath(filepath, target_path),
                                "line": line_num,
                                "rule_id": pat["id"],
                                "rule_name": pat["name"],
                                "severity": pat["severity"],
                                "snippet": line.strip()[:100]
                            })
        except Exception:
            pass
            
    print(f"[SECURITY_OS AUDIT] Completed scan across {len(files_to_check)} files.")
    print(f"[SECURITY_OS AUDIT] Found {len(vulnerabilities)} findings.")
    for v in vulnerabilities:
        print(f"  - [{v['severity']}] {v['rule_id']} {v['rule_name']} @ {v['file']}:L{v['line']} -> {v['snippet']}")
    return vulnerabilities

def export_rules(platform="antigravity"):
    skills = load_domain_index()
    print(f"[SECURITY_OS EXPORT] Compiling {len(skills)} skills into adapter format for target platform: {platform}")
    out_file = f"scratch/security_os_export_{platform}.json"
    os.makedirs("scratch", exist_ok=True)
    payload = {
        "platform": platform,
        "total_skills": len(skills),
        "domains_count": 29,
        "skills_sample": skills[:50],
        "frameworks": ["MITRE ATT&CK", "NIST CSF 2.0", "MITRE ATLAS", "D3FEND", "NIST AI RMF", "MITRE F3"]
    }
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2)
    print(f"[SUCCESS] Exported rule pack to {out_file}")

def main():
    parser = argparse.ArgumentParser(description="SecurityOs Unified CLI Security Runner & Adapter Exporter")
    subparsers = parser.add_subparsers(dest="command")
    
    # Search
    search_p = subparsers.add_parser("search", help="Search 817 security skills")
    search_p.add_argument("query", help="Search term")
    search_p.add_argument("--domain", help="Domain filter", default=None)
    
    # Audit
    audit_p = subparsers.add_parser("audit", help="Run security audit on target path")
    audit_p.add_argument("target", help="Directory or file path to scan", default=".")
    audit_p.add_argument("--threshold", help="Severity threshold (CRITICAL, HIGH, MEDIUM, LOW)", default="HIGH")
    
    # Export
    export_p = subparsers.add_parser("export", help="Export rule pack for target AI platform")
    export_p.add_argument("--target", help="Target platform (cursor, claude, gemini, antigravity, codex)", default="antigravity")
    
    args = parser.parse_args()
    
    if args.command == "search":
        res = search_skills(args.query, args.domain)
        print(f"[SECURITY_OS SEARCH] Query: '{args.query}' | Matches: {len(res)}")
        for r in res[:25]:
            print(f"  - {r}")
        if len(res) > 25:
            print(f"  ... and {len(res) - 25} more skills.")
    elif args.command == "audit":
        run_audit(args.target, args.threshold)
    elif args.command == "export":
        export_rules(args.target)
    else:
        skills = load_domain_index()
        print(f"[SECURITY_OS RUNNER] Active. Loaded {len(skills)} cybersecurity skills from SecurityOs.")
        print("Usage: python scripts/security_os_runner.py [search | audit | export]")

if __name__ == "__main__":
    main()
