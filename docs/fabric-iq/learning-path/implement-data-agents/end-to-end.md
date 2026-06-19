# Implement an end-to-end Microsoft Fabric data agent

This unit walks through creating, configuring, and using a Fabric data agent to enable conversational AI over enterprise data. [Official docs](https://learn.microsoft.com/en-us/training/modules/implement-fabric-data-agents/end-to-end-scenario)

!!! info "Prerequisites"
    A paid **F2 or higher** Fabric capacity, the **Fabric data agent** tenant setting and **Copilot** tenant switch enabled, and at least one data source with data (warehouse, lakehouse, Power BI semantic model, or KQL database).

## 1. Create the data agent

In your workspace, select **+ New item**, choose **Fabric data agent**, give it a meaningful name, and create it.

## 2. Select data sources

Connect up to **five data sources** in any combination (lakehouses, warehouses, Power BI semantic models, KQL databases). Add each one individually from the **OneLake catalog**, using filters to narrow source types.

After adding a source, the **Explorer** pane lists its tables — use the checkboxes to control which tables the AI can access.

!!! tip "Use descriptive names"
    Descriptive table and column names help the AI generate more accurate, reliable queries.

**Ask questions:** the agent analyses the prompt, decides which tool to invoke, and uses natural language to SQL/DAX/KQL. It shows both the final result and the **intermediate steps** it took, so you can review and validate its reasoning. The agent supports **read** operations only and doesn't perform advanced analytics, machine learning, or causal inference.

## 3. Configure the agent

- **Instructions** — plain-language guidance (up to **15,000 characters**) that shapes behaviour: point certain questions at a specific source, or describe tables and columns. Open via **AI instructions**.
- **Example queries** — provide question/query pairs per data source to improve accuracy. This **few-shot learning** technique guides the agent toward expected answers. *Power BI semantic models don't support example query pairs at this time.*

## 4. Publish

When satisfied, select **Publish** and provide a detailed description — this helps colleagues understand the agent and lets other AI orchestrators invoke it automatically. Publishing creates two versions: an editable **draft** and the stable **published** version you share.

## 5. Consume

A published agent can be consumed in **Microsoft Fabric**, **Copilot Studio**, **Microsoft Teams**, **Power BI Copilot**, **Microsoft Foundry**, and **custom applications via API**.

## Best practices

- Keep **instructions clear and concise**; define acronyms or domain jargon the agent misreads.
- The agent handles **simple queries** best — complex queries with many joins or sophisticated logic are less reliable.
- Avoid including **too many tables and columns**, which lowers performance.
- When **sharing**, also share access to the underlying data — the agent honours all user permissions, including RLS and CLS.

Next, [integrate the agent with Microsoft Foundry](foundry.md).
