# Sharing & permissions

Creating a data agent is iterative — select tables, write instructions, add example queries, then **publish**. Publishing produces a **read-only version** you can share, while you keep refining the draft.

[Official docs](https://learn.microsoft.com/en-us/fabric/data-science/data-agent-sharing)

## Publishing & versioning

- Publishing requires a **description** of what the agent does — consumers (and other orchestrators) use it to understand and invoke the agent.
- After publishing you have two versions: a **published** (read-only, shared) version and a **draft** you can refine without affecting users. Switch between them to compare query performance.
- Update the description any time via **Settings → Publishing**.

!!! tip "Generate the description"
    Ask the agent to describe what it does, then refine that response and use it as the
    published description.

## Sharing permission models

When you share, you control what others can do. **You must also grant access to the underlying data** — the agent honours all user permissions, including Row-Level Security (RLS) and Column-Level Security (CLS).

| Permission | What the user can do |
| --- | --- |
| **No extra permission** | Query the **published** version only — no access to view or edit configuration. |
| **View details** | View (not edit) configuration of published and draft versions; can still query. |
| **Edit and view details** | Full view/edit of published and draft versions; can query. Ideal for collaboration. |

!!! note "Sharing before publishing"
    If you share before publishing, users with default permission **can't** query it (there's
    no published version yet). Users granted *View* or *Edit* can access the draft.

## Required source permissions

A user needs at least these **minimum effective permissions** on each connected source, or queries fail / return empty results:

| Data source | Minimum permission | Notes |
| --- | --- | --- |
| Power BI semantic model | **Read** | Workspace access and Build aren't required via a data agent. Build/Write only to modify the model or use Prep for AI. |
| Lakehouse | Read on the item (plus table access if enforced) | Write only to modify data. |
| Warehouse | Read (SELECT on relevant tables) | Higher perms only for DML/DDL. |
| KQL database | Reader role | Higher roles only for management commands. |
| Ontology | Read on the ontology **and** on the bound semantic model / lakehouse / KQL database | — |
| Microsoft Graph in Fabric | Read on the graph item and underlying data | — |

Follow **least privilege**: grant Read for query-only access; grant broader roles only when users must modify a model or use features such as Prep for AI. This relaxed semantic-model rule applies **only** to data agent interactions — other entry points (e.g. Analyze in Excel) may still need Build.

*Curated from [Microsoft Learn](https://learn.microsoft.com/en-us/fabric/data-science/data-agent-sharing) · Updated 2026-05-12*
