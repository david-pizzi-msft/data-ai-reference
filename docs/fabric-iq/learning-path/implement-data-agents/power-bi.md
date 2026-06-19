# Use Microsoft Fabric data agents within Power BI

Copilot in Power BI lets users ask natural-language questions and get answers from their available Fabric resources — semantic models, reports, and Fabric data agents — in a single conversational interface. [Official docs](https://learn.microsoft.com/en-us/training/modules/implement-fabric-data-agents/power-bi)

!!! note "Preview"
    This feature is currently in preview.

## Prerequisites

- Access to **Copilot in Power BI**.
- Required permissions for the relevant Fabric data agents and Power BI items.
- For Copilot search to auto-suggest agents, the **Standalone Copilot experience** must be enabled (**Tenant settings → Copilot → Standalone Copilot experience**).

## Two ways to use agents in Copilot

- **Copilot search** — when you ask a question, Copilot scans all items you can access (semantic models, reports, data agents), ranks them, and suggests the most relevant to answer from.
- **Directly add an agent** — if you know which one you want, select **Add items for better results → Data agents**, then pick it from the OneLake catalog. It's attached for relevant follow-ups; indicate a topic change to search across all resources again.

## Interaction flow

1. **Rephrase** — Copilot may rephrase your question for clarity or context.
2. **Send** — the question goes to the selected data agent.
3. **Retrieve** — the agent identifies the most relevant source (lakehouse, warehouse, semantic model, KQL database, ontology, or Azure AI Search index) and queries it, enforcing RLS and CLS based on your permissions.
4. **Return** — the agent sends the answer back to Copilot.
5. **Present** — Copilot shows the answer in the conversation.
