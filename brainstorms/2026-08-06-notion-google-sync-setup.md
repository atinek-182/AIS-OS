# Notion to Google Sheets Sync: Discovery & Setup Notes
Date: 2026-08-06 · Goal: Detailed Google Sheets & Apps Script Setup + Code Audit · Operator: Atinek Maurya

## Executive Summary & Key Decisions
- **Notion Database ID Extracted**: `355543dfcd8541af9d2420adb903959b` from user provided URL `https://app.notion.com/p/355543dfcd8541af9d2420adb903959b?v=c74c512ff33b4d70b90ff44922f927b1`.
- **Script Review Verdict**: `GoogleAppsScript_NotionSync.gs` is structurally sound with dynamic column mapping, defensive property extractors, and automated ledger calculations. 3 minor refinements recommended: (1) Notion pagination handling for >100 records, (2) Notion integration connection step in Notion UI, (3) Exact property name matching.

## Domain Vocabulary & Glossary (CONTEXT.md updates)
- **Notion Integration Token**: A secret key starting with `secret_` or `ntn_` created in Notion Developers console that grants Apps Script permission to read/write pages.
- **Time-Driven Trigger**: A built-in Google Apps Script cron mechanism that executes `runMasterSync()` automatically every 15 minutes or 1 hour.
- **Dynamic Header Mapping**: Lookup function (`getHeaderMap`) that dynamically matches sheet headers to column numbers to prevent layout changes from breaking scripts.

## Q&A Log
### Q1 — Setup Guide & Code Review
- **Concept Explained**: Google Apps Script acts as a free, serverless backend. It calls Notion's REST API, processes the JSON response, and writes directly into Google Sheets without third-party subscriptions like Make or n8n.
- **Notion Database ID**: `355543dfcd8541af9d2420adb903959b`
- **Code Audit Summary**: Code is 95% complete. Highlighted 3 key refinements (Pagination, Property Name Alignment, Notion Internal Connection Link).
