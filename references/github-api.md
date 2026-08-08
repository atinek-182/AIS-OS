---
title: GitHub MCP API Reference
domain: architecture
summary: 'Allows full-circle repository management, issues, PRs, and commits. - `github/list_issues`: Search open issues.'
critical_directives:
- Follow document guidance without bypassing established safeguards.
section_outline:
- GitHub MCP API Reference
- Tools
- Authentication
read_triggers:
- When working on architecture in references/github-api.md
- When reading context for GitHub MCP API Reference
tags:
- architecture
- github-api
updated: '2026-08-08'
---

# GitHub MCP API Reference

Allows full-circle repository management, issues, PRs, and commits.

## Tools
- `github/list_issues`: Search open issues.
- `github/create_issue`: Create a new issue ticket.
- `github/create_pull_request`: Submit a new pull request.
- `github/list_commits`: View commit history.

## Authentication
Uses `GITHUB_PERSONAL_ACCESS_TOKEN` environment variable.
