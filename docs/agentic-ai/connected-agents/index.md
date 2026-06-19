# Build multi-agent solutions using connected agents in Copilot Studio

> **Level:** Intermediate · **Units:** 8 · **Roles:** App Maker

Build multi-agent solutions in Copilot Studio by connecting an orchestrator to agents built across Microsoft's agentic platform. This [module](https://learn.microsoft.com/en-us/training/modules/build-multi-agent-solutions-connected-agents-copilot-studio/) covers connecting to Copilot Studio agents, Microsoft Foundry agents, and Microsoft Fabric Data agents, then managing the connected ecosystem for accurate orchestration.

By the end of this module you'll be able to:

- Connect an orchestrator to an existing published Copilot Studio agent.
- Connect a Microsoft Foundry agent to a Copilot Studio orchestrator.
- Connect a Microsoft Fabric Data agent to enable natural-language queries over Fabric data.
- Manage and test connected agents in Copilot Studio.

**Prerequisites**

- Ability to create, configure, and publish an agent in Microsoft Copilot Studio.
- Understanding of multi-agent design considerations.
- Access to Copilot Studio and permissions to create solutions and agents in a Power Platform environment.

!!! info "Preview"
    Connecting to **Microsoft Foundry** and **Microsoft Fabric Data** agents are preview features, not intended for production.

## Units

<div class="grid cards" markdown>

- **[Understand connected agents](understand.md)**

    What they are, how the orchestrator routes to them, and governance responsibilities.

- **[Connect a Copilot Studio agent](connect-copilot-studio.md)**

    Enable connections on the target, connect from the orchestrator, and tune descriptions.

- **[Connect a Microsoft Foundry agent](connect-foundry.md)**

    Connect with a project endpoint URL and agent ID; governance considerations.

- **[Connect a Fabric Data agent](connect-fabric-data.md)**

    Natural-language queries over OneLake; description-based routing constraint.

- **[Manage and test the solution](manage-test.md)**

    Validate routing, tune descriptions, enable/disable, and disconnect agents.

</div>

The module also includes a hands-on **exercise** completed directly on Learn.

## Module assessment

Learn includes a short knowledge check on connected agent types, connection configuration, and routing. [Take the module assessment on Microsoft Learn](https://learn.microsoft.com/en-us/training/modules/build-multi-agent-solutions-connected-agents-copilot-studio/7-knowledge-check/) to earn a pass on your profile.

## Summary

A **connected agent** is an independently published agent that an orchestrator delegates tasks to — unlike a child agent, it has its own lifecycle and can be owned by a different team or platform. The orchestrator routes to connected agents using their **descriptions**, so writing precise, non-overlapping descriptions is the central skill. Copilot Studio supports connecting to Copilot Studio agents, Foundry agents, Fabric Data agents, A2A protocol agents, and Microsoft 365 Agents SDK agents. Across all of them, you own the data flowing between agents and the governance of each connection.

[Start this module on Microsoft Learn](https://learn.microsoft.com/en-us/training/modules/build-multi-agent-solutions-connected-agents-copilot-studio/)
