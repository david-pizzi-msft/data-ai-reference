# Source control, CI/CD & ALM

Manage data agents with Microsoft Fabric's **Application Lifecycle Management** — version configurations in Git and promote updates across dev, test, and production with deployment pipelines.

[Official docs](https://learn.microsoft.com/en-us/fabric/data-science/data-agent-source-control)

!!! info "Preview"
    Source control for Fabric data agents is in preview.

Two complementary approaches:

- **Git integration** — sync a workspace with Azure DevOps or GitHub for version control, branching, and history.
- **Deployment pipelines** — promote agents between workspaces mapped to lifecycle stages.

## Git integration

- Connect a workspace to a Git repo from **Workspace settings**; data agents then appear in the **Source control** pane.
- Supports **selective branching** (switch the connected branch per workspace) and a built-in **diff** experience before commit/pull.
- Any change — schema selection, AI instructions, data source instructions, example queries, or publishing description — marks the agent as **Uncommitted changes**.

### Repository structure

Each data agent is stored under `files/config/`:

| Item | Contents |
| --- | --- |
| `data_agent.json` | Agent definition. |
| `publish_info.json` | Publishing description. |
| `draft/` | Draft config — one folder per data source (`lakehouse-tables-`, `warehouse-tables-`, `semantic-model-`, `kusto-`, `ontology-`), plus `stage_config.json` (`aiInstructions`). |
| `published/` | Mirror of draft for the published version — **don't edit directly**. |

Each source folder holds `datasource.json` (instructions, `displayName`, `elements` schema map with table/column `is_selected`) and `fewshots.json` (example queries). Semantic-model sources have only `datasource.json`.

## Deployment pipelines

1. Build or update the agent in the **development** workspace.
2. Promote to **test** for validation.
3. Promote to **production** for end users.

Assign a workspace to each stage; unassigned test/prod workspaces are auto-created. Review the deployment plan before applying. Automate with the **Azure DevOps Pipelines extension for Fabric** (runs Fabric CLI tasks), or bulk-sync via the Import/Export Item Definitions Batch APIs (preview).

!!! note "Publish for consumption"
    A data agent must be **published** to be consumed anywhere (Copilot in Power BI, Copilot Studio, Foundry). End users should consume only versions published from **production**.

## Best practices & limits

- Use a dedicated dev branch; merge to main after review. Keep related items in one workspace for easier promotion.
- Never edit the `published/` folder directly. Use environment-agnostic config (e.g. Variable Library references).
- Only Git-connected workspaces get ALM features. Deployment pipelines require source and target in the **same tenant**.
- **Service principals** are supported **only** for ALM scenarios (Git integration, deployment pipelines) — not for other data agent features.

*Curated from [Microsoft Learn](https://learn.microsoft.com/en-us/fabric/data-science/data-agent-source-control) · Updated 2025-08-08*
