# 1 · GitHub integration

!!! info "Source"
    [AzurePortal/4_CICD/1_github-integration.md](https://github.com/Cloud2BR-MSFTLearningHub/MS-Fabric-Essentials-Workshop/blob/main/AzurePortal/4_CICD/1_github-integration.md)

**Status:** ✅ Documented

!!! note "Set up in this repo"
    Git integration for this workshop targets the `git/ms-fabric-essentials/deployment-pipelines`
    folder in **this** repo (see `git/README.md`). Because the **Analytics Dev** workspace from the
    [Deployment pipelines](deployment-pipelines.md) lab is connected to Git, running that lab
    syncs the items automatically — no separate GitHub integration lab is needed here.

## Git-integrated labs in this repo

Each Git-connected workspace maps to its own folder under `git/` (see `git/README.md`):

| Lab | Fabric Git folder path | Status |
| --- | --- | --- |
| [Medallion Architecture](../medallion-architecture.md) | `/git/ms-fabric-essentials/medallion-architecture` | ✅ Complete |
| [Deployment pipelines](deployment-pipelines.md) | `/git/ms-fabric-essentials/deployment-pipelines` | 🟡 In progress |

**Git integration** connects a Fabric workspace to a **GitHub** (or Azure DevOps) repository so
item definitions are version-controlled. You edit the workspace as normal, then **commit**
changes to a branch and **update** the workspace when the branch changes — giving you source
control, history, and ALM for Fabric items.

## Prerequisites — GitHub token

To connect Fabric to a GitHub repo you must authenticate with a GitHub **personal access token**.
Create **one** of the following on your GitHub account and paste it into Fabric's *Personal access
token* field when connecting:

| Token type | Required permission / scope |
| --- | --- |
| **Fine-grained token** (recommended) | Repository permission **Contents → Read and write** |
| **Classic token** | `repo` scope enabled |

!!! tip "Create a fine-grained token"
    GitHub → **Settings → Developer settings → Personal access tokens → Fine-grained tokens → Generate new token**.
    Scope it to the target repository, set **Contents** to **Read and write**, and set a sensible expiry.
    Store the token securely — it grants write access to the repo.

!!! warning "Keep the token secret"
    Never commit the token to the repo or paste it into docs. It is entered only in Fabric's Git
    integration connection dialog.

Fabric and tenant prerequisites (capacity + the Git-integration tenant switches) also apply — see
the official docs below.

## Workspace ↔ Git lifecycle

```mermaid
flowchart LR
    WS[Fabric workspace] -->|Commit| GIT[(Git branch)]
    GIT -->|Update| WS
    ADMIN([Workspace admin]) -->|Connect / Disconnect| WS
```

## Key operations

- **Connect a workspace to a Git repo** — only a **workspace admin** can link a workspace to a repo. Once linked, anyone with the right permission can work in it.
- **Connect to an already-linked workspace** — if the workspace is already integrated, follow the shared-workspace connection flow.
- **Commit changes to Git** — edits are saved to the workspace first; when ready, **commit** them to the branch (or revert to the previous state).
- **Update workspace from Git** — when a new commit lands on the connected branch, the workspace shows a notification; use the **Source control** panel to pull, merge, or revert into live items.
- **Disconnect a workspace from Git** — only a **workspace admin** can disconnect a workspace from its repo.

!!! note "Admin-only actions"
    Connecting and disconnecting a workspace both require **workspace admin** rights. If you're
    not an admin, ask one to set up (or remove) the connection.

## Official references

- [Get started with Git integration](https://learn.microsoft.com/en-us/fabric/cicd/git-integration/git-get-started)
- [The Git integration process](https://learn.microsoft.com/en-us/fabric/cicd/git-integration/git-integration-process)
- [Considerations and limitations](https://learn.microsoft.com/en-us/fabric/cicd/git-integration/git-get-started#considerations-and-limitations)
