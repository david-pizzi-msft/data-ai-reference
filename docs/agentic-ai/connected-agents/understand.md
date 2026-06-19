# Understand connected agents in Copilot Studio

Before connecting any agent, it helps to understand what connected agents are, how the orchestrator decides when to delegate, and what responsibilities you take on. [Official docs](https://learn.microsoft.com/en-us/training/modules/build-multi-agent-solutions-connected-agents-copilot-studio/2-understand-connected-agents)

## What connected agents are

A **connected agent** is a separately published, independently managed agent that an orchestrator connects to and delegates tasks to. It has its own lifecycle — built, configured, tested, and published independently, sometimes by a different team on a different platform. From the orchestrator's perspective it's a callable specialist: send a task, get back a result.

This differs from a **child agent**, which lives inside the parent orchestrator, is owned by the same team, and ships in the same solution. Because connected agents are published independently, the same one can be connected to multiple orchestrators across the organisation. Child and connected agents can coexist in one solution.

## How the orchestrator routes to connected agents

Routing depends on **descriptions**. When the orchestrator receives a message, it evaluates it against the descriptions of all options — topics, tools, child agents, and connected agents. Each connected agent is treated like a tool whose description states what requests it handles. When the orchestrator's generative AI judges a close match, it delegates; the connected agent uses its own orchestration (topics, tools, knowledge) and returns a result.

By default, the orchestrator passes **conversation history** to the connected agent for context (disableable per connection). Overlapping or ambiguous descriptions cause misrouting that is hard to diagnose later.

## Available connected agent types

- **Copilot Studio agents** — existing agents published in the same Power Platform environment (most common).
- **Microsoft Foundry agents** — agents hosted in Foundry, bringing fine-tuned models and complex reasoning.
- **Microsoft Fabric Data agents** — Fabric agents that translate natural language into queries over OneLake data.
- **Agent2Agent (A2A) protocol agents** — cross-platform agents via the open A2A standard (covered separately).
- **Microsoft 365 Agents SDK agents** — developer-built agents for Microsoft 365 scenarios.

## Governance responsibilities

Connecting to an agent you don't own makes you responsible for the connection — specifically the **data that flows between agents**, not the agent's internal behaviour:

- **Data flow appropriateness** — confirm data passed (including conversation history) is allowed under the agent's terms, org policy, and regulations.
- **Quality and security standards** — ensure the agent meets your responsible-AI and quality bar.
- **Permissions and approvals** — verify you're permitted to connect and the owning team approves.
- **Observability** — plan how to correlate the orchestrator's and connected agent's separate transcripts for debugging.

Next, [connect an existing Copilot Studio agent](connect-copilot-studio.md).
