# Connect a Microsoft Fabric Data agent

Microsoft Fabric Data agents bridge conversational interfaces and enterprise data — translating natural-language questions into database queries that return structured answers. This unit covers connecting one to your orchestrator. [Official docs](https://learn.microsoft.com/en-us/training/modules/build-multi-agent-solutions-connected-agents-copilot-studio/5-connect-fabric-data-agent)

## What they bring to your solution

A Fabric Data agent is a conversational analytics agent published in Fabric. It translates natural language into queries over OneLake sources and returns structured answers, using the right query language per source:

- **SQL** — lakehouses and warehouses.
- **DAX** — Power BI semantic models.
- **KQL** — KQL databases.

Connecting one lets the orchestrator answer highly specific data questions (e.g. total spend with a supplier this quarter) without building a custom SQL tool or data integration.

!!! info "Preview"
    Connecting to Microsoft Fabric Data agents is a preview feature, not meant for production.

## Prerequisites

- **Fabric connection** in the Power Platform environment (or create one during the flow).
- **F2 or higher** Fabric capacity (or Power BI Premium P1+ with Fabric enabled).
- **Published Fabric Data agent** accessible to the maker connecting to it.

## Connect from the orchestrator

1. Open the orchestrator → **Agents** page → **Add an agent**.
2. Select **Connect to an external agent** → **Microsoft Fabric**.
3. Create a new Fabric connection (provide credentials) or select an existing one.
4. Choose the Fabric Data agent from the list.
5. Review and adjust the **description** to scope the data domain precisely.
6. Select **Add agent**.

## Write descriptions for data-specific routing

Because the agent answers questions about a specific data domain, the description must reflect that scope precisely — "Answers data questions" is too broad. Consider the **data domain**, the **types of questions** it answers (spend totals, supplier rankings, contract values), and the **scope boundaries** of what it does *not* cover.

## Governance and data access

The agent enforces the **requesting user's Fabric permissions** — users only retrieve data they can access. **Microsoft Purview** controls (DLP and access-restriction policies) are respected, limiting what confidential or restricted data the agent can surface.

!!! warning "Generative orchestration only"
    Routing to a Fabric Data agent is supported **only** through generative orchestration (description-based). You can't route to it from a topic using an agent redirect node — so the description must be specific enough to match the right queries without topic-level help.

Next, [manage and test your connected agent solution](manage-test.md).
