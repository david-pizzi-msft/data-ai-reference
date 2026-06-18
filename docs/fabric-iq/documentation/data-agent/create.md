# Create a data agent

Build a conversational AI experience over data in lakehouses, warehouses, Power BI semantic models, KQL databases, ontologies, and Microsoft Graph. Building a data agent is like building a Power BI report — design and refine it, then publish and share.

[Official docs](https://learn.microsoft.com/en-us/fabric/data-science/how-to-create-data-agent)

## Prerequisites

- A paid **F2 or higher** Fabric capacity (or P1+ with Fabric enabled).
- **Cross-geo** processing/storing for AI enabled — see [Tenant settings](tenant-settings.md).
- At least one data source with data, and **read** access to it.

!!! note "No keys or tokens"
    Fabric uses a Microsoft-managed Azure OpenAI Assistant and handles authentication for you.
    Data access runs under your Microsoft Entra ID identity and your workspace/data permissions —
    the agent reads schemas and runs queries only against data you can access.

## Steps

1. **Create** — in your workspace, select **+ New item**, search for **Fabric data agent**, and give it a name.
2. **Add data sources** — the OneLake catalog opens; add up to **five** sources in any combination, one at a time. The **Explorer** then lists each source's tables.
3. **Select tables** — use the checkboxes to make specific tables available to the AI (lakehouse *tables*, not raw files). Use **descriptive table and column names** so the AI generates accurate queries.
4. **Ask questions** — questions that translate to a structured query work well; questions needing causal reasoning or ML (e.g. *"why did sales spike?"*) are out of scope.
5. **Publish** — once it generates accurate queries, publish with a detailed description.

!!! tip "Suitable vs. out-of-scope questions"
    Good: *"What were total sales in California in 2023?"*, *"Top 5 products by list price and their categories?"*
    Out of scope: *"Why is factory productivity lower in Q2 2024?"* — requires correlation/causal analysis the agent doesn't perform.

## Configuration

- **Instructions** — up to **15,000 characters** of plain-English guidance: route question types to specific sources (e.g. financial → semantic model, sales → lakehouse, operational metrics → KQL) and define domain terminology/acronyms.
- **Example queries** — sample question/query pairs (**few-shot learning**) per data source to improve accuracy. Supported for lakehouse, warehouse, and KQL databases; **not** for Power BI semantic models or ontologies. Only valid queries matching the table schema are used.

## Managing data sources

- **Remove / refresh** — hover a source in the Explorer, open the three-dot menu, then **Remove** or **Refresh** (refresh picks up schema changes).
- **Clear chat** — erases all chat history and starts a new session (not recoverable).

## Versions, ALM & deployment

- Publishing creates a **read-only published version** plus an editable **draft** — refine the draft without affecting what others use, and switch between them to compare.
- **Diagnostics** to troubleshoot query generation, **Git integration** to version-control configs, and **deployment pipelines** to promote dev → test → production.

!!! info "Cross-tenant & shortcuts"
    Agents can query tables backed by [OneLake shortcuts](https://learn.microsoft.com/en-us/fabric/onelake/onelake-shortcuts) and data shared from other tenants via [OneLake external data sharing](https://learn.microsoft.com/en-us/fabric/governance/external-data-sharing-overview) — no extra auth; the consumer tenant's governance applies.

*Curated from [Microsoft Learn](https://learn.microsoft.com/en-us/fabric/data-science/how-to-create-data-agent) · Updated 2026-05-20*
