# MCP server

The **Model Context Protocol (MCP)** is an emerging standard that lets AI systems discover and use external tools and data in a consistent way, without building one-off integrations. A published data agent can act as an **MCP server**, exposing enterprise data in Fabric OneLake to any MCP client.

[Official docs](https://learn.microsoft.com/en-us/fabric/data-science/data-agent-mcp-server)

!!! info "Preview"
    Consuming a data agent as an MCP server is in preview.

!!! warning "Data boundary"
    Responses may be sent outside Fabric's compliance boundary or region and processed/stored per your **MCP client's** terms and data-handling policies.

## Client and server

- An **MCP client** is the app you interact with (e.g. VS Code) — it reaches out to MCP servers to find and use tools.
- An **MCP server** exposes tools, data, or services. A published Fabric data agent acts as an MCP server, exposing enterprise data an AI system can query.

## How it works

- A data agent exposed as an MCP server presents a **single tool** representing the agent. The **publishing description** becomes the tool description — clients and orchestrators use it to decide when and how to invoke the agent, so write it clearly.
- Works with **any MCP client** that speaks MCP over streamable HTTP and attaches a valid Fabric bearer token — not just one editor. Connections follow the MCP flow (`initialize` handshake → `tools/list` → `tools/call`); a plain REST call won't work.
- **Dynamic client registration is not supported** — acquire a Fabric token via your own auth flow and attach it to each request.

## Prerequisites

- A paid **F2+** Fabric capacity (or P1+ Power BI Premium with Fabric enabled).
- **Cross-geo processing and storing for AI** enabled (see data agent tenant settings).
- At least one data source with data (warehouse, lakehouse, semantic model, KQL DB, mirrored DB, or ontology) that you can read.
- A **published** data agent — the MCP server only works after publishing.

## Get the server details

Publish the agent → **Settings** → **Model Context Protocol** tab, which shows the **server name**, **server URL**, **tool name**, and **tool description**. You can download **`mcp.json`** to configure clients like VS Code, or build the URL yourself:

```http
https://api.fabric.microsoft.com/v1/mcp/workspaces/{WorkspaceId}/dataagents/{DataAgentId}/agent
```

## Authentication

Every request needs a **bearer token** in the `Authorization` header with access to the target workspace and agent (user or service principal). Request the token for the `https://api.fabric.microsoft.com/.default` scope. VS Code prompts you to sign in interactively; in Python, acquire the token via a library such as `azure-identity`.

## Connect

=== "VS Code"

    1. Create `.vscode/mcp.json`, then select **Add Server** → **HTTP** and paste the **MCP server URL**.
    2. Name the server, then **Allow** and sign in when prompted.
    3. **Enable Agent Mode** — Command Palette → *Enable Agent Mode*.
    4. Select an **orchestrator** (GPT-5, GPT-4.1, Claude Sonnet 4.5, Gemini 2.5 Pro, …).
    5. Ask questions — the orchestrator routes them to the agent, which answers from OneLake data.

=== "Python"

    ```bash
    pip install mcp azure-identity
    ```

    Sign in (e.g. `az login`), then connect with `AzureCliCredential`, run the MCP handshake, discover the single tool, and call it — the script reads the tool name and question argument from the tool's input schema, so nothing is hard-coded.

*Curated from [Microsoft Learn](https://learn.microsoft.com/en-us/fabric/data-science/data-agent-mcp-server) · Updated 2026-06-30*
