# Security policy

## Reporting a vulnerability

Report instruction-injection risks, unsafe publishing paths, credential exposure, or other security concerns privately through the repository host's private vulnerability-reporting channel when available. If no private reporting channel is available, ask the maintainers for a private contact method in a public issue without including exploit details, account data, or private content.

Do not place OAuth tokens, API keys, session cookies, SocialBu or LinkedIn account identifiers, unpublished posts, private conversations, analytics exports, or personal data in an issue, pull request, fixture, screenshot, log, or commit. Revoke and rotate any credential that was exposed outside its intended secret store.

## Security boundary

This repository contains Markdown instructions, a static image, manifests, and a local validation script. It must not contain credentials, SDKs, client libraries, telemetry, or a custom SocialBu integration.

SocialBu MCP authentication belongs to the compatible client and uses the endpoint `https://socialbu.com/mcp`. A connected session authorizes access only within the permissions exposed by that session; it does not authorize publishing.

Only `socialbu-linkedin-publisher` may perform a publish, schedule, or autopost mutation. It must display the exact action, account, content, media or link details, and time or settings, then receive fresh confirmation immediately before each call. Confirmation is invalid after any material change and cannot be reused for another action or an uncertain retry.

See [SocialBu capability and execution boundary](references/socialbu-capabilities.md) for the complete operating protocol.
