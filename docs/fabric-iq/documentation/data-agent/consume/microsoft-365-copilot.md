# Microsoft 365 Copilot

Publish a data agent to the **Agent Store in Microsoft 365 Copilot** so business users can interact with organizational knowledge from Fabric OneLake — directly inside Teams and Copilot chat.

[Official docs](https://learn.microsoft.com/en-us/fabric/data-science/data-agent-microsoft-365-copilot)

!!! info "Preview"
    This integration is in preview.

!!! warning "Data boundary"
    Responses may be sent outside Fabric's compliance boundary or region and processed/stored per Microsoft 365's terms and data-handling policies.

## Prerequisites

- Microsoft 365 Copilot license (or Office 365 commercial subscription) and per-user licenses.
- The agent and M365 Copilot must be on the **same tenant**, signed in with the **same account**.

## Publish & use

1. During publish, select **Publish to Agent Store** — the agent appears in the M365 Copilot Agent Store (may take a few seconds; refresh via *Expand Navigation*).
2. Chat with it **directly**, or **`@`-mention** it from the main Copilot chat.
3. **Share** with colleagues via the agent's Share link (1:1, group, or Teams channel) — recipients need access to the agent **and** its underlying data sources.

Results respect your access to the underlying data, including **RLS/CLS**. Users can also use the **code interpreter** in M365 Copilot to generate visualizations from returned results.

## Control the output

The agent runs inside the M365 Copilot orchestrator, which reasons over the returned data. To minimize changes, add instructions in the **publishing description** (it becomes `description_for_model`) — e.g. deliver output as-is without summarizing. Some variation is still inevitable.

*Curated from [Microsoft Learn](https://learn.microsoft.com/en-us/fabric/data-science/data-agent-microsoft-365-copilot) · Updated 2026-05-12*
