# 4 · CI/CD

!!! info "Source"
    [AzurePortal/4_CICD](https://github.com/Cloud2BR-MSFTLearningHub/MS-Fabric-Essentials-Workshop/tree/main/AzurePortal/4_CICD)

**Status:** 🟡 In progress

The workshop's CI/CD module covers the two ways to promote and version Fabric content:
**deployment pipelines** (stage-to-stage promotion inside Fabric) and **GitHub integration**
(source control for a workspace). They are complementary — Git tracks the source of truth,
pipelines push content between environments.

## What this section covers

| # | Workshop | What it does | Status |
| --- | --- | --- | --- |
| 0 | [Deployment pipelines](deployment-pipelines.md) | Promote a lakehouse, semantic model, and report across Dev → Prod stages. | 🟡 In progress |
| 1 | [GitHub integration](github-integration.md) | Connect a workspace to a Git repo and commit/update items. | ✅ Documented |

## Pipelines vs. Git — when to use which

- **Deployment pipelines** — move *content between workspaces* (dev/test/prod). Copies structure and metadata, **not** the data in tables.
- **Git integration** — version *item definitions* in a repo; commit changes and pull updates. The system of record for source control and ALM.
- Use them **together**: develop in a Git-connected workspace, then promote validated content downstream with a pipeline.
