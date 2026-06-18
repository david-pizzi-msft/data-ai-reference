# MCP server

The **Model Context Protocol (MCP)** is an emerging standard that lets AI systems discover and use external tools and data in a consistent way. A published data agent can act as an **MCP server**, exposing enterprise data in Fabric OneLake to MCP clients.

[Official docs](https://learn.microsoft.com/en-us/fabric/data-science/data-agent-mcp-server)

!!! info "Preview"
    Consuming a data agent as an MCP server is in preview.

!!! warning "Data boundary"
    Responses may be sent outside Fabric's compliance boundary or region and processed/stored per your **MCP client's** terms and data-handling policies.

## How it works

- A data agent exposed as an MCP server presents a **single tool** representing the agent. The **publishing description** becomes the tool description — external AI systems use it to decide when and how to invoke the agent, so write it clearly.
- Currently usable in **VS Code** (or your own MCP client if you configure authentication).

## Set up in VS Code

1. **Publish** the agent → **Settings** → **Model Context Protocol** tab.
2. Note the **MCP server name**, **server URL**, **tool name**, and **tool description**; optionally download **`mcp.json`** to configure VS Code.
3. **Enable Agent Mode** — Command Palette → *Enable Agent Mode*.
4. Select an **orchestrator** (GPT-5, GPT-4.1, Claude Sonnet 4.5, Gemini 2.5 Pro, …).
5. Ask questions in VS Code — the orchestrator routes them to the agent, which answers from OneLake data.

*Curated from [Microsoft Learn](https://learn.microsoft.com/en-us/fabric/data-science/data-agent-mcp-server) · Updated 2025-12-18*
