# Consume & integrate

A published data agent isn't limited to the in-product chat — external orchestrators and multi-agent runtimes can invoke it as a **read-only, governed knowledge source**.

## In this section

- **[Get visual responses](visuals.md)** — interactive charts in the agent conversation.
- **[Microsoft Foundry](foundry.md)** — add the agent to an Azure AI agent (UI or Python SDK).
- **[Copilot in Power BI](copilot-powerbi.md)** — invoke the agent from the Copilot pane.
- **[Copilot Studio](copilot-studio.md)** — connect the agent to a custom agent and publish to Teams.
- **[Python client SDK](python-sdk.md)** — embed the agent in external apps via browser auth.
- **[Microsoft 365 Copilot](microsoft-365-copilot.md)** — publish to the Agent Store for Teams/Copilot.
- **[MCP server](mcp-server.md)** — expose the agent as a Model Context Protocol server.

!!! warning "Data boundary"
    When consumed from non-Fabric services (Foundry, Copilot Studio, Microsoft 365 Copilot,
    or an MCP server), responses may be sent outside Fabric's compliance boundary or region,
    governed by that service's terms. Purview governance still applies to the underlying sources.

## Common requirements

- The data agent must be **published** with a rich, detailed description.
- The data agent and the consuming service must be on the **same tenant**, signed in with the **same account**.
- Consumers need at least **read** access to the data agent and the necessary permissions on all underlying data sources.
