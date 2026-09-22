# Optional SocialBu publishing boundary

Use this reference only when the user explicitly requests a connected LinkedIn publishing action. The optional MCP endpoint is `https://socialbu.com/mcp`; this repository does not ship credentials, an API client, or an automatic publishing command.

## Required sequence

1. Verify that the client has an authorized SocialBu MCP connection and inspect only the minimum necessary account or schedule data.
2. Prepare a preview containing the exact LinkedIn target, full final content, media or links, and exact schedule time with timezone.
3. Ask for a fresh confirmation tied to that unchanged preview.
4. Make one state-changing call only after that confirmation.
5. Report the returned identifier and status. If the result is uncertain, stop; never retry automatically.

An editorial approval, a request to prepare a post, a previous confirmation, or a modified draft does not authorize publishing.
