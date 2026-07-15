# Upstash Context7 API Guide

Upstash Context7 is a service that fetches up-to-date, version-specific documentation and code examples directly into the AI agent's context, reducing hallucinations and outdated code generation.

## Endpoints

*   **Remote MCP URL:** `https://mcp.context7.com/mcp`
*   **OAuth MCP URL:** `https://mcp.context7.com/mcp/oauth`
*   **API Dashboard:** [context7.com/dashboard](https://context7.com/dashboard)

## Authentication

Context7 is free to use but can be configured with an API key for higher rate limits.
*   **Header Name:** `CONTEXT7_API_KEY`
*   **CLI Setup:** Run `npx ctx7 setup` to configure locally.

## MCP Tools

### `context7/resolve-library-id`
Resolves a library or framework name into a specific library ID.
*   **Arguments:**
    *   `libraryName` (string, required): The name of the library (e.g. "next.js")
    *   `query` (string, required): The context or question to help rank results.

### `context7/query-docs`
Retrieves documentation snippets and code examples for a resolved library.
*   **Arguments:**
    *   `libraryId` (string, required): The unique library ID returned by `resolve-library-id` (e.g., `/vercel/next.js`).
    *   `query` (string, required): The specific question or code task.

## CLI & Skill Command
*   **Query CLI command:** `npx ctx7 query <library-id> "<query>"`
