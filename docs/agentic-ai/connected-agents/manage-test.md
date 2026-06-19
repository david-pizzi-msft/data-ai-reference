# Manage and test your connected agent solution

With connections in place, the orchestrator is structurally complete. This unit covers confirming routing works and maintaining connections over time. [Official docs](https://learn.microsoft.com/en-us/training/modules/build-multi-agent-solutions-connected-agents-copilot-studio/6-manage-test-connected-agent-solution)

## Test routing in the test canvas

The **Test your agent** panel is the primary tool for validating routing. Send prompts representing each connected agent's intended scope. Enable **Show activity map when testing** — for connected agents the activity map confirms not just that a response came back, but **which agent** produced it and what the orchestrator's routing decision was.

!!! tip "Test boundary cases first"
    Write down three queries that could plausibly match more than one connected agent, and test those first — they reveal routing gaps that clear-cut prompts miss.

If the activity map shows a prompt routed to the wrong agent, that's a **description problem, not a connection problem**.

## Tune descriptions when routing is inaccurate

Misrouting usually means two agents share overlapping language. The fix is to make both descriptions more specific so a query matches only one. The diagnostic cycle is: **test → observe the activity map → refine descriptions → retest**.

## Supplement with orchestrator instructions

When description refinement alone isn't enough, add explicit routing guidance to the orchestrator's **instructions** field — e.g. *"For any question about supplier spend totals or procurement data trends, delegate to the Finance Data Agent."* You can reference connected agents by name. Use this selectively, for persistent ambiguity — not as a substitute for accurate descriptions.

## Enable and disable agents

The **Enabled** toggle on the **Agents** page temporarily suspends a connected agent without losing configuration. While disabled it's inactive for all users and the orchestrator won't route to it; re-enabling resumes routing immediately. Useful for planned maintenance and staged rollouts.

## Disconnect permanently

To remove an agent for good: **Agents** page → **…** menu next to the agent → **Disconnect agent**. This stops all routing to it; the connected agent itself and any other orchestrators are unaffected. Reconnecting later requires recreating the full connection — so if there's any chance you'll reconnect, **disable** instead.

## Monitor transcripts

Connected agents generate their **own transcripts**, separate from the orchestrator's. To debug an end-to-end interaction spanning multiple agents, review both. Plan for transcript correlation before production to make debugging far easier.
