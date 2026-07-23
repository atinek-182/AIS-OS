# Site Reference Ingestion & DNA Extraction Queue: Brainstorm / Discovery Notes
Date: 2026-07-23 · Goal: Ingest 18 curated award-winning reference sites sequentially into AIOS vault with visual screenshots, WebP video recordings, and 5-layer site DNA analysis.

## Summary / Key Decisions
- **Execution Mode:** Strictly one site at a time. Do not touch site N+1 until explicit user command is given.
- **Visual Assets Required:**
  - 5-viewport crisp screenshots (1920, 1440, 1024, 768, 375).
  - Browser interaction WebP screen recording.
- **Storage Location:** `premium-frontend-experience-system/reference-inputs/sites/[site-slug]/`

## Q&A Log
### Q1 — Batching & Order of Execution
- Asked: How should the 18 reference websites be ingested?
- Captured: Ingest one website at a time. Finish site #1 completely (screenshots, video, 5-layer DNA report, code mirror), present preference checklist, and wait for user's explicit signal before starting the next website.

---

## Open Flags (Pending Input)
- User approval for Site #1 (`sondaven.com`) components after DNA extraction -> User input needed before cross-vault indexing.
