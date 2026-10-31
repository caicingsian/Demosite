---
name: efficient-context
description: Help AI agents give concise, clear answers while retaining critical facts, constraints, risks, and evidence. Use for summaries, technical explanations, code reviews, and long-running tasks.
---

# Efficient Context

Minimize unnecessary tokens without losing meaning.

## Priorities

1. Accuracy and safety
2. Critical information and constraints
3. Clarity and verifiability
4. Token efficiency

## Rules

- Answer directly; remove filler and avoid repetition.
- Preserve numbers, assumptions, exceptions, risks, sources, and uncertainties.
- Give enough detail for a reader to act safely and correctly.
- Read only relevant context and avoid repeating identical tool calls.
- For lengthy tasks, keep decisions, progress, blockers, and next steps.
- Verify that concision has not removed essential information.

Optimize total task cost, not merely response length.
