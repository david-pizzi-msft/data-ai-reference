# Fabric data agent SDK

The **Fabric Data Agent Python SDK** gives code-first users programmatic access to data agent artifacts — create, configure, update, and publish agents without the Fabric portal. Run it inside a Fabric notebook, or from your own environment after authenticating to Fabric.

[Official docs](https://learn.microsoft.com/en-us/fabric/data-science/fabric-data-agent-sdk)

!!! info "Preview"
    The SDK is in preview.

## Management plane vs runtime

- The SDK is a **management-plane** tool — create the artifact, add and configure data sources, set instructions and example queries, and publish. It runs on the **Fabric public REST API**.
- Querying at **runtime** is separate: after publishing, query the agent through its [MCP endpoint](consume/mcp-server.md).

## Prerequisites

- A Fabric workspace with a capacity that supports data agents.
- A supported data source (lakehouse, warehouse, Power BI semantic model, or KQL database).
- Python **≥ 3.10**.
- For execution **outside** a Fabric notebook, a way to authenticate to Fabric (Azure CLI or a service principal).

## Install

```python
%pip install fabric-data-agent-sdk
```

Published on PyPI as [`fabric-data-agent-sdk`](https://pypi.org/project/fabric-data-agent-sdk/).

## Authenticate

- **Inside a Fabric notebook** — authentication is handled for you.
- **Outside Fabric** — sign in first, e.g. with `AzureCliCredential` and `SetFabricAnalyticsDefaultTokenCredentialsGlobally`. Use a user account or service principal with permission to manage items in the target workspace.

## Typical flow

1. `create_data_agent(...)` — create the artifact in a workspace.
2. `agent.update_settings(...)` and `agent.add_staging_datasource(...)` — configure instructions and add data sources.
3. `agent.publish_staging(...)` — publish for querying.

!!! tip "Sample notebooks"
    See the [data-agent-sdk samples](https://github.com/microsoft/fabric-samples/tree/main/docs-samples/data-science/data-agent-sdk)
    on GitHub for end-to-end usage.

*Curated from [Microsoft Learn](https://learn.microsoft.com/en-us/fabric/data-science/fabric-data-agent-sdk) · Updated 2026-06-24*
