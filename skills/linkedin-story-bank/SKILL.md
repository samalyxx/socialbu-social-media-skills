---
name: linkedin-story-bank
description: Capture real professional experiences as a structured, reusable LinkedIn story inventory without inventing events, dialogue, emotions, or lessons. Use for interviews, notes, and ongoing idea capture.
---

# LinkedIn story bank

Build a source-of-truth inventory from the user's actual experiences. Read [LinkedIn content planning](../../references/linkedin-content-planning.md) for editorial fields and [LinkedIn writing](../../references/linkedin-writing.md) for evidence boundaries.

## Capture method

For each candidate story, collect:

- who experienced it and what their role was;
- setting and timeframe at an appropriate level of specificity;
- the starting situation, decision or tension, action, and observable outcome;
- artifacts or people that can verify material claims;
- what is confidential, attributable, anonymized, or not approved for use;
- the honest lesson, audience relevance, and possible content objective;
- the author's own phrases when supplied verbatim.

Ask neutral follow-ups such as “What changed after that decision?” or “Which detail can be shared publicly?” Do not lead the user toward a more dramatic version.

## Workflow

1. Separate recorded fact, direct quotation, interpretation, and missing detail.
2. Split distinct moments into separate story records rather than forcing a broad narrative.
3. Tag each record by theme, audience, evidence strength, sensitivity, and readiness.
4. Suggest possible angles only after the factual record is established.
5. Mark stale, duplicated, sensitive, or verification-blocked entries.

## Output

Return a `Story bank` table with `ID`, `Working title`, `Situation`, `Decision/action`, `Outcome`, `Lesson`, `Audience`, `Evidence`, `Sensitivity`, and `Status`. Follow it with `Follow-up questions` and an `Editorial queue` of the strongest ready records.

Statuses are `captured`, `needs detail`, `needs verification`, `needs permission`, or `ready to brief`. Never promote a story to ready when a material claim or permission is unresolved. This skill stores nothing outside the response unless the user explicitly asks for a repository artifact.
