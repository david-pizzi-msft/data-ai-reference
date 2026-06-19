# Connect a Microsoft Foundry agent

Some capabilities are built using AI frameworks outside Copilot Studio. Connecting your orchestrator to a **Microsoft Foundry agent** brings those in without rebuilding them. [Official docs](https://learn.microsoft.com/en-us/training/modules/build-multi-agent-solutions-connected-agents-copilot-studio/4-connect-foundry-agent)

## What Foundry agents bring

A Foundry agent is built and hosted in Microsoft Foundry and can incorporate fine-tuned models, complex reasoning chains, multi-step tool orchestration, and custom knowledge that go beyond what's practical to build directly in Copilot Studio. You connect using the agent's **project endpoint URL** and a unique **agent ID**, then the orchestrator invokes it like any other connected agent via generative orchestration.

!!! info "Preview"
    Connecting to Microsoft Foundry agents is a preview feature, not meant for production. Confirm availability in your environment first.

## Prerequisites

- **New Microsoft Foundry portal** — the agent must be created and published in the new portal, not the legacy Azure AI Studio portal (legacy agents return a 404).
- **Project endpoint URL** — from the Foundry project settings.
- **Agent ID** — from the agent's details page.
- **Access** — sufficient access to the Foundry project, or the URL and ID provided to you.

## Connect from the orchestrator

1. Open the orchestrator → **Agents** page → **Add an agent**.
2. Select **Connect to an external agent** → **Microsoft Foundry**.
3. Create a new connection with the **project endpoint URL**, or select an existing one.
4. Enter a **name** reflecting the agent's role (e.g. "Vendor Risk Analyst").
5. Enter a **description** — this is the routing signal.
6. Enter the **agent ID**, then select **Add agent**.

!!! tip "Update the agent ID in place"
    If the Foundry team ships a new version with a different agent ID, edit the **agent ID** field on the agent's details page — the connection, name, and description stay unchanged.

## Governance responsibilities

Any data sent to the Foundry agent (user messages, conversation history) is processed by the Foundry-hosted agent. Before going live, confirm: what data it processes and whether it's logged/retained, whether it passed responsible-AI review, the project's data-processing terms, and whether any users or use cases should not be routed to it.

Next, [connect a Microsoft Fabric Data agent](connect-fabric-data.md).
