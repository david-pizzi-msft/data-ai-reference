# Consume in Copilot Studio

Add a Fabric data agent to a custom agent in **Microsoft Copilot Studio** as a **connected agent**. This agent-to-agent setup lets the custom agent securely ground its responses in enterprise data through the Fabric data agent, then publish to channels such as **Microsoft Teams**.

[Official docs](https://learn.microsoft.com/en-us/fabric/data-science/data-agent-microsoft-copilot-studio)

!!! info "Preview"
    This integration is in preview.

## Prerequisites

- Data agent **published** and responding to queries, with a rich description.
- Fabric data agent and Copilot Studio on the **same tenant**, signed in with the **same account**.
- A **Microsoft 365 Copilot** license, plus permission to build agents in Copilot Studio.
- At least **read** access to the data agent and its underlying data sources.

## Steps

1. In [Copilot Studio](https://copilotstudio.microsoft.com), select an environment, then **Create → + New agent** (or open an existing one) and give it a name and description.
2. Go to **Agents** (top pane) → **+ Add** → choose **Microsoft Fabric** under *Choose how you want to extend your agent*.
3. Reuse an existing Fabric connection or **Create new connection**.
4. Select your published data agent from the list, optionally adjust its description, and **Add agent**.
5. On the connected agent, choose authentication: **User authentication** (users need access to the agent and its sources) or **Agent author authentication**.
6. Enable **generative AI orchestration** (Settings → Orchestration), test in the chat pane, then **Publish**.
7. Add the **Teams and Microsoft 365 Copilot** channel, then **See agent in Teams** to use it.

!!! note "Channel support"
    A custom agent with a connected Fabric data agent is only **validated for Microsoft Teams**.
    It isn't currently supported in Microsoft 365 Copilot; other channels may work but aren't
    formally tested. Anyone you share the custom agent with needs read access to the data agent
    and its underlying sources.

*Curated from [Microsoft Learn](https://learn.microsoft.com/en-us/fabric/data-science/data-agent-microsoft-copilot-studio) · Updated 2026-05-12*
