# Connect to a Foundry Search Index

Connect a data agent directly to an **Azure AI Search index** built in Microsoft Foundry to reason over **unstructured content** (PDFs, text, enriched documents) — and join those insights with your structured sources for a unified view.

[Official docs](https://learn.microsoft.com/en-us/fabric/data-science/data-agent-ai-search-index)

!!! info "Preview"
    This feature is in preview. The agent fully respects the permissions of your Azure AI resources.

## Set up the search resource

1. **Create an Azure AI Search index** (start with sample or your own data).
2. **Enable role-based access control** on the search service and index — the agent accesses it using the **asking user's identity**.
3. **Assign roles** — `Search Index Data Contributor` and `Search Index Data Reader`.
4. **Copy the resource URL** — needed when adding the connection.

!!! tip "Citations"
    Citations appear only if the index contains at least one of these (case-sensitive) fields: `url`, `sourceUrl`, `filePath`, `path`, or `folderPath`.

## Connect to the agent

1. **Data** tab → **Add AI Search Index**.
2. Provide the **resource URL**.
3. Ask a question to query the index; view the **documents used** in the reasoning steps.

The agent sends the user's identity to the index so its access controls are respected.

## Configure

| Setting | Purpose |
| --- | --- |
| **Context** | Describe index contents and key fields to aid routing. |
| **Display Name** | Name shown for the index in the agent. |
| **Search Type** | Full-text, hybrid, or semantic (per your index). |
| **Number of Documents** | Documents retrieved per query (recommended 3–20). |
| **Agent instructions** | How to interpret results and compose the final answer. |

*Curated from [Microsoft Learn](https://learn.microsoft.com/en-us/fabric/data-science/data-agent-ai-search-index) · Updated 2025-12-09*
