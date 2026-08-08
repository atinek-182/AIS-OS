---
title: Notion MCP API Reference
domain: architecture
summary: 'Interacts with Notion databases, pages, and blocks. - `notion-mcp-server/API-post-page`: Create a new Notion page.'
critical_directives:
- Follow document guidance without bypassing established safeguards.
section_outline:
- Notion MCP API Reference
- Tools
- Authentication
read_triggers:
- When working on architecture in references/notion-api.md
- When reading context for Notion MCP API Reference
tags:
- architecture
- notion-api
updated: '2026-08-08'
---

# Notion MCP API Reference

Interacts with Notion databases, pages, and blocks.

## Tools
- `notion-mcp-server/API-post-page`: Create a new Notion page.
- `notion-mcp-server/API-retrieve-a-database`: Fetch Notion database properties.
- `notion-mcp-server/API-patch-page`: Update page properties.

## Authentication
Uses `OPENAPI_MCP_HEADERS` environment variable with Authorization Bearer header.
