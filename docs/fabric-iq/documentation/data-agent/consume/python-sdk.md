# Python client SDK

Use the **Python client SDK** to add a data agent to web apps and other external clients with **interactive browser authentication** — users sign in with their Microsoft Entra ID and the agent runs with their permissions.

[Official docs](https://learn.microsoft.com/en-us/fabric/data-science/consume-data-agent-python)

!!! info "Preview"
    The Python client SDK is in preview.

!!! warning "Data boundary"
    Responses may be sent outside Fabric's compliance boundary or region and processed/stored per the consuming app's terms and data-handling policies.

## Set up (VS Code)

1. Clone the [Fabric Data Agent External Client repo](https://github.com/microsoft/fabric_data_agent_client/tree/main).
2. Create and activate a virtual environment, then `pip install -r requirements.txt` (includes `azure-identity`).
3. Configure `TENANT_ID` and `DATA_AGENT_URL` (env vars, `.env`, or in-script).

## Authenticate & ask

```python
from azure.identity import InteractiveBrowserCredential
from fabric_data_agent_client import FabricDataAgentClient

credential = InteractiveBrowserCredential()      # opens a browser to sign in
client = FabricDataAgentClient(credential=credential)

response = client.ask("What were the total sales last quarter?")
print(f"Response: {response}")
```

## Inspect steps

Use `client.get_run_details(question)` to see the steps the agent took, the queries it generated, and any execution errors — useful for transparency and debugging.

*Curated from [Microsoft Learn](https://learn.microsoft.com/en-us/fabric/data-science/consume-data-agent-python) · Updated 2025-08-08*
