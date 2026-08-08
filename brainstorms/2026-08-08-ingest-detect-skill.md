# Discovery Capture: Ingesting `resemble-ai/detect-skill`

- **Repository URL**: https://github.com/resemble-ai/detect-skill
- **Ingestion Date**: 2026-08-08
- **Target Slug**: `detect-skill`
- **Native Skill Name**: `resemble-detect`
- **License**: Apache-2.0 (100% Permissive Open Source)

## Stage 1 Deep Analysis Summary
- **Core Purpose**: Deepfake detection & media intelligence for Audio, Video, and Image files powered by Resemble AI v2 REST API.
- **Key Features**:
  1. Deepfake Detection (`POST /detect`, `GET /detect/{uuid}`) for Audio, Images, and Videos with score (0.0-1.0) and label (`real`/`fake`).
  2. Audio Source Tracing (`audio_source_tracing: true`) to identify creator platform (ElevenLabs, Resemble AI, etc.).
  3. Media Intelligence (`POST /intelligence`) for speaker info, emotion, dialect, abnormalities, and misinformation analysis.
  4. Detect Intelligence (`POST /detects/{uuid}/intelligence`) for natural language Q&A on completed detection jobs.
  5. Privacy Safeguards (`zero_retention_mode: true`) and Secure Uploads (`POST /secure_uploads`) for >150MB media.
- **Iron Law**: "NEVER DECLARE MEDIA AS REAL OR FAKE WITHOUT A COMPLETED DETECTION RESULT."

## 5-Persona Roast Council Evaluation
- **Contrarian**: Warns about relying solely on external API keys ($RESEMBLE_API_KEY); requires robust environment variable checks, graceful handling of missing keys, and strict score interpretation (0.3-0.5 is inconclusive).
- **Expansionist**: Sees massive value for ZORIXEL agency client audits, media verification SOPs, automated content provenance checking, and video sales call authenticity verification.
- **Logician**: Appreciates zero-heavy-model local architecture — uses direct HTTP curl/Python REST calls, keeping AIOS lightweight.
- **Researcher**: Confirms Resemble AI v2 API is state-of-the-art for synthetic voice and talking-head detection.
- **Buyer (Operator)**: Extremely high ROI for agency deliverables and media verification workflows.

## Next Step
- Present Stage 1 Report to Operator and wait for explicit "YES" to execute Stage 2 adaptation (Python runner script + Tier 1 native skill + system rules).

