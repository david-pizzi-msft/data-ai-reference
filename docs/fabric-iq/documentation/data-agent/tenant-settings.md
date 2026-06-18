# Tenant settings

Before anyone can use a data agent, a Fabric admin must enable the required tenant settings in the **Admin Portal → Tenant settings**. Changes can take up to **one hour** to take effect.

[Official docs](https://learn.microsoft.com/en-us/fabric/data-science/data-agent-tenant-settings)

!!! warning "Data boundary"
    Configuring a data agent for consumption from **non-Fabric services** (Microsoft Foundry,
    Copilot Studio, Microsoft 365 Copilot, or as an MCP server) may send responses outside
    Fabric's compliance boundary or geographic region, governed by that service's terms.

## Required settings (Copilot and Azure OpenAI Service)

| Setting | Why it's needed |
| --- | --- |
| **Users can use Copilot and other features powered by Azure OpenAI** | Allows access to Copilot-powered features, including data agents. Manageable at tenant and capacity level. |
| **Capacities can be designated as Fabric Copilot capacities** | Lets capacity admins mark capacities for Copilot usage, including data agents. |
| **Data sent to Azure OpenAI can be processed outside your region / compliance boundary / national cloud** | Required when the capacity's region is outside the EU data boundary and the US. |
| **Data sent to Azure OpenAI can be stored outside your region / compliance boundary / national cloud** | Required (outside EU data boundary and US) for Copilot in Notebooks and data agents. |
| **Conversation history stored outside your region / compliance boundary / national cloud** | Needed for conversational experiences that retain context across sessions (outside EU data boundary and US). |

!!! note "Conversation history"
    History is stored for as long as the user allows — up to **28 days** if not manually
    removed. Users can delete it any time by clearing the chat.

*Curated from [Microsoft Learn](https://learn.microsoft.com/en-us/fabric/data-science/data-agent-tenant-settings) · Updated 2026-04-20*
