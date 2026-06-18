# Fabric data agent SDK

The **Fabric Data Agent Python SDK** gives code-first users programmatic access to data agent artifacts — create, manage, and consume agents directly from a Fabric notebook, built on the OpenAI Assistants API.

[Official docs](https://learn.microsoft.com/en-us/fabric/data-science/fabric-data-agent-sdk)

!!! info "Preview"
    The SDK is in preview. It runs **only inside Microsoft Fabric notebooks** — local execution isn't supported.

## What it does

- **Programmatic management** — create, update, and delete data agent artifacts.
- **Data source integration** — connect and manage multiple sources in code.
- **OpenAI Assistants API support** — rapid prototyping and experimentation.
- **Workflow automation** — automate routine tasks.
- **Resource optimization** — tune agent configuration to fit your scenario.

## Prerequisites

- Python **≥ 3.10** (a Fabric-compatible version).
- Runs exclusively within a Fabric notebook session.

## Install

```python
%pip install fabric-data-agent-sdk
```

Pip installs any required dependencies automatically.

!!! tip "Sample notebooks"
    See the [data-agent-sdk samples](https://github.com/microsoft/fabric-samples/tree/main/docs-samples/data-science/data-agent-sdk)
    on GitHub for end-to-end usage.

*Curated from [Microsoft Learn](https://learn.microsoft.com/en-us/fabric/data-science/fabric-data-agent-sdk) · Updated 2025-12-05*
