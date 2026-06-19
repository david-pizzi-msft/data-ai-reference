# Connect an existing Copilot Studio agent

This unit walks through connecting an existing Copilot Studio agent to your orchestrator — from preparing the target agent to configuring the orchestrator-side connection with a description tuned for accurate routing. [Official docs](https://learn.microsoft.com/en-us/training/modules/build-multi-agent-solutions-connected-agents-copilot-studio/3-connect-copilot-studio-agent)

## Prerequisites for the connection

- **Same environment** — target agent and orchestrator are in the same Power Platform environment.
- **Published** — the target agent has at least one published version.
- **Connections enabled** — the target agent has *Let other agents connect to and use this one* turned on.
- **Owner or shared access** — you own the target agent or it's shared with you.

## Prepare the target agent

On the **target** agent: open it in Copilot Studio → **Settings** → **General** → turn on **Let other agents connect to and use this one**. Until this is enabled, the agent won't appear in the connection list even if published in the same environment. Align authentication and user-access settings if end users must authenticate to use its capabilities.

## Connect from the orchestrator

1. Open the orchestrator agent → **Agents** page → **Add an agent**.
2. Select **Connect to an external agent** → **Copilot Studio**.
3. Pick the target agent (only same-environment agents with connections enabled appear).
4. Review its **name**, **instructions**, and **description** — the orchestrator routes on the description.
5. Adjust the description locally if a more specific version improves routing.
6. Configure **pass conversation history** (on by default).
7. Select **Add agent**.

## Write descriptions that route accurately

The description is the primary signal the orchestrator uses to delegate. Effective descriptions have:

- **Scope clarity** — name specific topics/question types, not broad categories.
- **Boundary setting** — avoid language that could describe another connected agent.
- **Query-language alignment** — use the words users would naturally ask with.

!!! important "The orchestrator's copy doesn't auto-sync"
    The orchestrator stores a **local copy** of the description and routes on it. If the source agent's description, scope, or capabilities change, the local copy doesn't update automatically — review and update it manually to keep routing accurate.

Next, [connect a Microsoft Foundry agent](connect-foundry.md).
