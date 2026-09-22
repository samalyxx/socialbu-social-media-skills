---
name: social-post-writer
description: Draft accurate, platform-aware social posts and captions from a brief.
---

# Social post writer

## Inputs
Ask for or infer only: platform, audience, objective, source facts, voice, call to action, and any required links or assets. Flag missing facts rather than inventing them.

## Workflow
1. Restate the intended audience and one post objective.
2. Choose a structure that fits the platform and requested format.
3. Draft one primary post and, if useful, one meaningfully different alternate hook.
4. Check every factual claim against the supplied source.

## Output
Return `Draft`, `Why it fits`, `Assumptions`, and `Optional next step`. Clearly label placeholders. This skill drafts only; use the MCP operator only if the user separately asks to create a SocialBu draft or scheduling action.

## Guardrails
Do not fabricate outcomes, testimonials, statistics, urgency, or customer stories. Do not publish or schedule.
