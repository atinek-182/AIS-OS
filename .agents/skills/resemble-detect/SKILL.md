---
name: resemble-detect
description: Deepfake detection, synthetic audio/image/video manipulation analysis, audio source tracing, and media safety — powered by direct Resemble AI API calls and CLI runner.
argument-hint: '[media_url_or_file_path] [--intelligence] [--audio-source-tracing] [--visualize]'
---

# Resemble Detect — Deepfake Detection & Media Safety (`/resemble-detect`)

Analyze audio, image, and video for synthetic manipulation, AI-generated content, source tracing, and media intelligence using direct **Resemble AI REST API v2** calls via `python scripts/resemble_detect_runner.py`.

---

## ⚡ Core Principle — THE IRON LAW

**"NEVER DECLARE MEDIA AS REAL OR FAKE WITHOUT A COMPLETED DETECTION RESULT."**

Do not guess, infer, or speculate about media authenticity based on raw visual/auditory inspection alone. Every authenticity claim must be backed by a completed Resemble Detect job with a returned `label`, `score`, and `status: "completed"`. If the detection is still processing, wait. If it failed, report the failure.

---

## 🎯 When to Use

Use this skill whenever the user's request involves:
- Checking if audio, video, or image media is AI-generated or manipulated
- Detecting deepfakes or verifying media authenticity
- Identifying which AI platform synthesized audio (audio source tracing, e.g. ElevenLabs, Resemble AI)
- Analyzing media for speaker info, emotion, transcription, or misinformation signals
- Asking natural-language follow-up questions about completed detection jobs
- Trigger words: `deepfake`, `fake detection`, `synthetic media`, `media safety`, `is this real`, `source tracing`, `resemble detect`

---

## 🛠️ Requirements & Setup

- **Environment Variable**: Requires `RESEMBLE_API_KEY` set in the environment or `.env`.
- **API Base URL**: `https://app.resemble.ai/api/v2`
- **CLI Runner**: `python scripts/resemble_detect_runner.py`

---

## 🧭 Capability Decision Tree

| User Objective | Subcommand | CLI Command Example |
|---|---|---|
| **Detect Deepfake from URL** | `detect --url` | `python scripts/resemble_detect_runner.py detect --url "https://example.com/media.mp4" --intelligence --audio-source-tracing --poll` |
| **Detect Deepfake from Local File** | `detect --file` | `python scripts/resemble_detect_runner.py detect --file "scratch/sample.wav" --visualize --poll` |
| **Poll Pending Job** | `poll` | `python scripts/resemble_detect_runner.py poll "<DETECT_UUID>"` |
| **Standalone Intelligence** | `intelligence` | `python scripts/resemble_detect_runner.py intelligence --url "https://example.com/audio.mp3"` |
| **Ask Follow-Up Q&A** | `ask` | `python scripts/resemble_detect_runner.py ask "<DETECT_UUID>" "Summarize detection results in plain language."` |

---

## 📊 Score & Result Interpretation

| Aggregated / Final Score | Verdict Interpretation |
|---|---|
| **0.0 – 0.3** | Strong indication of authentic / real media |
| **0.3 – 0.5** | **Inconclusive** — recommend manual review or additional analysis |
| **0.5 – 0.7** | Likely synthetic — flag for verification |
| **0.7 – 1.0** | **High confidence synthetic / AI-generated media** |

---

## 🛡️ Operational Safeguards & Red Flags

- **Zero Retention Mode**: Set `--zero-retention` for privacy-sensitive client assets.
- **Large Files (>150MB)**: The Python runner automatically routes files larger than 150MB through `POST /secure_uploads`.
- **Never report score without context**: Say *"The detection returned a score of 0.87, indicating high confidence of synthetic manipulation"* — never just *"it's fake"*.

---

## 🔗 Inter-Skill Connections
- **`/vibesec`**: Invoked for deepfake and media authenticity verification during security audits.
- **`/client-audit`**: Used during agency audits to analyze promotional videos and podcast authenticity.
- **`/scrape-web`**: Extracts target media URLs for automated batch provenance checks.
