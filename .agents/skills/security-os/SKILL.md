---
title: ZORIXEL AIOS Active Security Engine (`/security-os`)
domain: skill
summary: This skill is the central cybersecurity defense, AI agent safety, and compliance auditing engine for Atinek Maurya's
  AIOS (`AI-OS`) and ZORIXEL Agency. Powered by **817 cybersecurity skills** from `SecurityOs` linked at [SecurityOs/](file:///d:/AI-OS
critical_directives:
- '`CRITICAL`** (IDOR, SQLi, hardcoded tokens, RCE, severe prompt injection): **ALWAYS Hard-Stop**, zero exceptions, across'
- '`HIGH`** (Missing rate limits, unvalidated redirects, CSRF): **Hard-Stop** during shipping (`/ship` & `/vibesec`); Warni'
section_outline:
- ZORIXEL AIOS Active Security Engine (`/security-os`)
- Overview & Tri-Mode Execution
- 29 Security Domains & 6 Frameworks Covered
- CLI Execution Parameters (`scripts/security_os_runner.py`)
- Unified Smart Severity Engine
read_triggers:
- When working on skill in .agents/skills/security-os/SKILL.md
- When reading context for ZORIXEL AIOS Active Security Engine (`/security-os`)
tags:
- skill
- SKILL
updated: '2026-08-08'
name: security-os
description: Active Cybersecurity Audit & Enforcement Engine powered by 817 structured security skills from SecurityOs (Anthropic
  Cybersecurity Skills). Enforces MITRE ATT&CK, NIST CSF 2.0, MITRE ATLAS (AI Safety & Prompt Injection Protection), OWASP
  Top 10, D3FEND, NIST AI RMF, and MITRE F3 frameworks. Features smart severity hard-stops, multi-agent platform export (--target
  cursor|claude|gemini|antigravity|codex), AST graph delta scanning, and dual client deliverables (Interactive HTML Audit
  Dashboard + Executive PDF Certificate). Invokable via /security-os or integrated into Phase 5 SDLC security gates (/vibesec,
  /code-review, /ship).
argument-hint: '[search <query> | audit <path> | export --target <platform> | cert <client_name>]'
---

# ZORIXEL AIOS Active Security Engine (`/security-os`)

## Overview & Tri-Mode Execution

This skill is the central cybersecurity defense, AI agent safety, and compliance auditing engine for Atinek Maurya's AIOS (`AI-OS`) and ZORIXEL Agency. Powered by **817 cybersecurity skills** from `SecurityOs` linked at [SecurityOs/](file:///d:/AI-OS/SecurityOs/), it actively audits code, prevents vulnerabilities (IDOR, SQLi, SSRF, CORS, hardcoded secrets), enforces **MITRE ATLAS** AI safety rules, and generates high-ticket client security deliverables ($2,500–$5,000 Sprints).

Invokable via:
- **Slash Command**: `/security-os [search | audit | export | cert]`
- **Dynamic Intent**: Triggered automatically during Phase 5 (Review & Hardening) of the 6-Phase SDLC Master Engine (`/vibesec`, `/code-review`, `/ship`).
- **Programmatic Inter-Skill Calling**: Called by `/website-design-engine`, `/six-file-context-methodology`, `/new-project`, `/ingest-repo`, `/gstack`, `/hallmark`, `/ai-pricing-engine`, `/zero-paywall-client-os`, `/interactive-operator-guide-generator`, `/gws-automation-engine`, and `/composio`.

---

## 29 Security Domains & 6 Frameworks Covered

`SecurityOs` maps all 817 skills to 6 international standards:
1. **MITRE ATT&CK**: Adversary Tactics, Techniques, and Procedures (TTPs).
2. **NIST CSF 2.0**: NIST Cybersecurity Framework (Identify, Protect, Detect, Respond, Recover).
3. **MITRE ATLAS**: Artificial Intelligence & Machine Learning threat matrix (prompt injection, model theft, data poisoning).
4. **D3FEND**: Defensive countermeasure architecture.
5. **NIST AI RMF**: Risk management framework for artificial intelligence.
6. **MITRE F3**: Fight Fraud framework for financial and e-commerce security.

---

## CLI Execution Parameters (`scripts/security_os_runner.py`)

| Command | Purpose | Example |
|---|---|---|
| `search <query>` | Search 817 cybersecurity skills | `python scripts/security_os_runner.py search "prompt injection"` |
| `audit <path>` | Run static vulnerability scan on codebase | `python scripts/security_os_runner.py audit . --threshold HIGH` |
| `export --target <platform>` | Export rule pack for Cursor, Claude Code, Gemini CLI, Codex CLI, or Antigravity | `python scripts/security_os_runner.py export --target cursor` |

---

## Unified Smart Severity Engine

- **`CRITICAL`** (IDOR, SQLi, hardcoded tokens, RCE, severe prompt injection): **ALWAYS Hard-Stop**, zero exceptions, across all development phases.
- **`HIGH`** (Missing rate limits, unvalidated redirects, CSRF): **Hard-Stop** during shipping (`/ship` & `/vibesec`); Warning + auto-patch suggestions during early prototyping (`/prototype`).
- **`MEDIUM / LOW`** (Missing security headers, minor lints): Logged to `audits/security_report.md` without blocking builds.

---

## Personalized Skill & Workflow Integrations

- **`website-design-engine`**: Integrates OWASP Top 10, DOM XSS prevention, CORS policy checks, Zod mass assignment validation, and httpOnly cookie setups into Phase 5 visual QA.
- **`six-file-context-methodology`**: Enforces zero secret/token leaks across context files and adds threat modeling parameters to specs.
- **`new-project`**: Bootstraps `.env.example`, security headers middleware, and MITRE ATLAS AI safety boilerplate.
- **`ingest-repo`**: Scans external repositories for malware, backdoors, dependency CVEs, and obfuscated code before workspace ingestion.
- **`gstack`**: Adds the **Executive Security Auditor Lens** to score threat exposure and IDOR/SSRF risks before shipping.
- **`hallmark`**: Enforces zero hardcoded API keys or personal data in visual previews and verifies sanitization.
- **`ai-pricing-engine` & `zero-paywall-client-os`**: Integrates the **$2,500 ZORIXEL Security Audit Sprint** and **NIST CSF 2.0 Compliance Certificate** deliverables into client pitches.
- **`interactive-operator-guide-generator`**: Generates copyable, secure setup steps with safe credential handling guidance and secret rotation SOPs.
- **`gws-automation-engine`**: Enforces minimal OAuth scope requests, GCP API enablement verification, and refresh token safety.
- **`composio` & `agent-reach`**: Enforces SSRF private IP blocking (127.0.0.1, 10.x.x.x), HMAC webhook verification, and outbound API payload sanitization.

---

## Post-Execution Auto-Evolution

At the completion of every execution of this skill:
1. Run pre-flight health validation: `python scripts/test_security_os_health.py`.
2. Sync living rules into `AGENTS.md` and `GEMINI.md` via `python scripts/sync_global_rules.py`.
3. Log major audit results to `WORKSPACE_MAP.md` and `decisions/log.md`.
