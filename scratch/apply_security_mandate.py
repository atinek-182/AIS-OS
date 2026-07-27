import os

guide_path = r'd:\AI-OS\references\six-file-context-methodology\STEP_BY_STEP_SENIOR_AI_ENGINEERING_GUIDE.md'
skill_7file_path = r'd:\AI-OS\.agents\skills\six-file-context-methodology\SKILL.md'

# 1. Append Security-First Mandate & Auto-Ingestion Rule to Guide
with open(guide_path, 'r', encoding='utf-8') as f:
    guide_text = f.read()

security_section = """

---

## 🔒 Security-First Architecture & Automatic Security Skill Ingestion

Security is the **primary non-negotiable requirement** for all web applications and AI SaaS tools.

### Core Security Rules (`/vibesec` Protocol):
1. **User & Tenant Level Authorization**: Ownership MUST be verified at the database query layer (never rely on route-level or client-side parameters). Return `404 Not Found` (never `403 Forbidden`) for unauthorized resource attempts to prevent IDOR enumeration.
2. **JWT & Cookie Hygiene**: JWT tokens MUST be stored in `httpOnly`, `Secure`, `SameSite=Strict` cookies. Never store sensitive tokens in `localStorage` or `sessionStorage`.
3. **Mass Assignment Prevention**: Always whitelist allowed mutation fields (Zod validation schemas). Never pass unfiltered request bodies (`req.body`) into ORM create/update calls.
4. **File Upload Security**: Validate file magic bytes server-side (not just extension/MIME header). Rename uploaded files with UUIDv4, store outside webroot, and set `X-Content-Type-Options: nosniff`.
5. **SSRF & Cloud Metadata Protection**: Resolve and block all private IP ranges (`127.0.0.1`, `10.0.0.0/8`, `169.254.169.254` cloud metadata) when fetching external URLs.

### 🔄 Automatic Skill Discovery & Ingestion Mandate:
Whenever a new security skill or backend reference guide (e.g. `/vibesec`, OWASP tools, backend security audits) is installed in `.agents/skills/` or `skills-library/`:
- The 7-File Context System automatically ingests its rules into `architecture.md` and `code-standards.md`.
- The Pre-Write `/roast` Council automatically applies its audit checklist before any context file or spec document is emitted.
"""

if "Security-First Architecture & Automatic Security Skill Ingestion" not in guide_text:
    guide_text += security_section
    with open(guide_path, 'w', encoding='utf-8') as f:
        f.write(guide_text)

print("Updated guide with Security-First section.")

# 2. Append Security Mandate to Skill
with open(skill_7file_path, 'r', encoding='utf-8') as f:
    skill_text = f.read()

if "Security-First & Automatic Security Skill Ingestion Mandate" not in skill_text:
    skill_text = skill_text.replace(
        "8. **Pre-Coding Backstop**: Always ask: *\"Is there anything else remaining before we touch the code?\"*",
        "8. **Pre-Coding Backstop**: Always ask: *\"Is there anything else remaining before we touch the code?\"*\n9. **Security-First & Auto-Skill Ingestion Mandate**: Security is the top priority. Always apply `/vibesec` rules (IDOR, JWT HttpOnly cookies, Mass Assignment Zod validation, SSRF protection). Automatically detect, scan, and apply ANY present or future security/backend skill in `.agents/skills/` or `skills-library/` during planning, spec generation, and pre-write `/roast` audits."
    )
    with open(skill_7file_path, 'w', encoding='utf-8') as f:
        f.write(skill_text)

print("Updated 7-file skill with Security Mandate.")
