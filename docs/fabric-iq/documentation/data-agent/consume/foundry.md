# Consume from Microsoft Foundry

Add a Fabric data agent as a **knowledge source** to an Azure AI agent in **Foundry Agent Service**, so your AI agents tap into governed, semantic data in OneLake. Uses **Identity Passthrough (On-Behalf-Of)** so queries run under the end user's permissions.

[Official docs](https://learn.microsoft.com/en-us/fabric/data-science/data-agent-foundry)

!!! info "Preview"
    This integration is in preview. Use the latest preview release of the
    [`azure-ai-projects`](https://pypi.org/project/azure-ai-projects/) Python SDK.

## How it works

- In Agent Service, create an agent and add **one** Fabric data agent as a knowledge source (using its **workspace ID** and **artifact ID**).
- When a query arrives, the Azure AI agent decides whether the Fabric tool is the best fit, invokes Fabric to fetch/process data under the user's identity, then combines results with its own logic.
- The model chosen for the Azure AI agent only drives orchestration — it doesn't change the model the Fabric data agent uses.

!!! note "Requirements"
    Developers and end users need at least the **AI Developer** RBAC role in Foundry. The
    Fabric data agent and Foundry resources must be on the same tenant and account.

## Connect via the UI

1. **Build and customize → Agents** — open an existing agent or create a **New Agent**.
2. **Add** a knowledge source → choose **Microsoft Fabric**.
3. **New Connection** — provide the data agent's `workspace-id` and `artifact-id` as custom keys (mark **Is Secret**). Find them in the published endpoint: `https://fabric.microsoft.com/groups/<workspace_id>/aiskills/<artifact-id>`.
4. Name the connection, scope it to the project or all projects, and **Connect**.
5. Add **instructions** telling the agent when/how to use the Fabric tool, then **Try in playground**.

## Connect programmatically (Python)

Set `PROJECT_ENDPOINT`, `MODEL_DEPLOYMENT_NAME`, and `FABRIC_CONNECTION_NAME`, then:

```bash
pip install azure-identity
pip install --pre azure-ai-projects
```

```python
import os
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from azure.ai.agents.models import FabricTool, ListSortOrder

project_client = AIProjectClient(
    endpoint=os.environ["PROJECT_ENDPOINT"],
    credential=DefaultAzureCredential(),
)

# Look up the Fabric connection by name and initialize the Fabric tool
conn_id = project_client.connections.get(os.environ["FABRIC_CONNECTION_NAME"]).id
fabric = FabricTool(connection_id=conn_id)

with project_client:
    agents_client = project_client.agents

    agent = agents_client.create_agent(
        model=os.environ["MODEL_DEPLOYMENT_NAME"],
        name="my-agent",
        instructions="You are a helpful agent",
        tools=fabric.definitions,
    )

    thread = agents_client.threads.create()
    agents_client.messages.create(
        thread_id=thread.id,
        role="user",
        content="What is the top sold product in Contoso last month?",
    )

    run = agents_client.runs.create_and_process(thread_id=thread.id, agent_id=agent.id)
    print(f"Run finished with status: {run.status}")

    messages = agents_client.messages.list(thread_id=thread.id, order=ListSortOrder.ASCENDING)
    for msg in messages:
        if msg.text_messages:
            print(f"{msg.role}: {msg.text_messages[-1].text.value}")
```

For C# and JavaScript, see the [Azure AI Agent Fabric tool docs](https://aka.ms/AgentFabricDoc).

*Curated from [Microsoft Learn](https://learn.microsoft.com/en-us/fabric/data-science/data-agent-foundry) · Updated 2026-05-12*
