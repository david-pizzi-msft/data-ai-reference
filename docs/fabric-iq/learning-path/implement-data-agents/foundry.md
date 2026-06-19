# Integrate Microsoft Fabric data agents with Microsoft Foundry

Connecting **Microsoft Foundry agents** with **Fabric data agents** exposes enterprise data through interactive Q&A, letting users explore and retrieve information in natural language. [Official docs](https://learn.microsoft.com/en-us/training/modules/implement-fabric-data-agents/azure-ai-foundry)

## Why integrate

- Users interact with enterprise data through chat to obtain data-driven insights for decision-making.
- **Identity passthrough** (On-Behalf-Of) means all access is governed by the user's permissions, supporting security and compliance.
- Reduces the steps and complexity of connecting AI agents to enterprise data.

!!! important "Identity passthrough only"
    The agent runs queries using the signed-in user's identity. **Service principal authentication isn't supported** for the Fabric data agent.

## Prerequisites

- A **published** Fabric data agent endpoint.
- Developers and end users have at least the **Azure AI User** RBAC role in Microsoft Foundry.
- Developers and end users have at least **read access** to the Fabric data agent.
- Minimum permission on each underlying data source:

    | Data source | Minimum permission |
    | --- | --- |
    | Power BI semantic model | **Build** (Read alone isn't sufficient — the agent generates model queries) |
    | Lakehouse | Read on the lakehouse item |
    | Warehouse | Read (SELECT on relevant tables) |
    | KQL database | Reader role on the database |

## How to integrate

1. **Create and publish** a Fabric data agent to obtain an endpoint.
2. **Configure access and permissions** per the prerequisites.
3. **Update agent instructions** in Foundry to describe the Fabric data agent and the data it provides — e.g. *"For customer and product sales related data, please use the Fabric tool."*
4. **Add the Fabric tool**: in the Foundry portal, under **Knowledge** select **Add** → **Microsoft Fabric**. Only one Fabric tool per agent. Supply the `workspace-id` and `artifact-id` from the endpoint (`https://fabric.microsoft.com/groups/<workspace_id>/aiskills/<artifact-id>`), adding them as a connection (mark as secret if needed).
5. **Test the integration**: select **Try in playground** and send queries. The agent decides when to use the Fabric tool and responds based on the data the user is authorised to access.

Next, [use the agent within Power BI](power-bi.md).
