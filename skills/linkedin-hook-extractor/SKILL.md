---
name: linkedin-hook-extractor
description: Generate, diagnose, and rank LinkedIn opening-line options against a supplied post body, audience, evidence, and voice. Use for hook exploration rather than full post drafting.
---

# LinkedIn hook extractor

Develop opening lines that set up the actual post instead of optimizing for empty curiosity. Read [LinkedIn hooks](../../references/linkedin-hooks.md) and use the evidence rules in [LinkedIn writing](../../references/linkedin-writing.md).

## Required context

Get the post body or detailed brief, intended reader, author voice, central claim, objective, and source evidence. A topic alone is enough for exploratory angles, but label them as directions rather than ready-to-use hooks.

## Workflow

1. Reduce the post to the one promise its opening must make.
2. Identify the reader's awareness: unaware of the issue, problem-aware, method-aware, or already familiar with the author's point of view.
3. Select two to four materially different angles from the hook reference. Do not create cosmetic paraphrases.
4. Draft concise candidates in the author's plausible voice.
5. Reject candidates that overclaim, manufacture conflict, conceal essential context, or fail to connect to the next paragraph.
6. Score surviving candidates using the reference rubric and explain any close tradeoff.

## Output

Return `Post promise`, then a table with `Hook`, `Angle`, `Best use`, `Risk`, and `Score`. Recommend one candidate only when the evidence and voice support a clear choice. Include a suggested transition into the body so the hook is evaluated in context.

Do not promise performance or label a hook “viral.” Testing proposals must name the variable, success measure, and comparison window.
