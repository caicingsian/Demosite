# Efficient Context

An Agent Skill to reduce unnecessary token usage without dropping essential information.

## Principles

1. Accuracy and safety first.
2. Keep assumptions, numbers, caveats, sources, and risks.
3. Be concise without sacrificing clarity.
4. Avoid redundant searches and repeated file reads.
5. Optimize total task cost, not only final answer length.

## Install

From the public repository:

```bash
npx skills add caicingsian/Demosite --skill efficient-context
```

Select your supported coding agent when prompted. Consult the [Skills CLI](https://github.com/vercel-labs/skills) for agent-specific options.

## Skill source

[`SKILL.md`](./SKILL.md)

## Status

Initial minimal release. No token-saving or quality benchmarks have been performed yet.
