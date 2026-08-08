---
title: Triage Labels
domain: architecture
summary: The skills speak in terms of five canonical triage roles. This file maps those roles to the actual label strings
  used in this repo's issue tracker. | Label in mattpocock/skills | Label in our tracker | Meaning                                  |
critical_directives:
- Follow document guidance without bypassing established safeguards.
section_outline:
- Triage Labels
read_triggers:
- When working on architecture in docs/agents/triage-labels.md
- When reading context for Triage Labels
tags:
- architecture
- triage-labels
updated: '2026-08-08'
---

# Triage Labels

The skills speak in terms of five canonical triage roles. This file maps those roles to the actual label strings used in this repo's issue tracker.

| Label in mattpocock/skills | Label in our tracker | Meaning                                  |
| -------------------------- | -------------------- | ---------------------------------------- |
| `needs-triage`             | `needs-triage`       | Maintainer needs to evaluate this issue  |
| `needs-info`               | `needs-info`         | Waiting on reporter for more information |
| `ready-for-agent`          | `ready-for-agent`    | Fully specified, ready for an AFK agent  |
| `ready-for-human`          | `ready-for-human`    | Requires human implementation            |
| `wontfix`                  | `wontfix`            | Will not be actioned                     |

When a skill mentions a role (e.g. "apply the AFK-ready triage label"), use the corresponding label string from this table.
