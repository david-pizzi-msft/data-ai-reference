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

## Set up Git integration (step by step)

From the target workspace → **Workspace settings → Git integration**:

1. **Provider** — select **GitHub**, then sign in and authorize with your [personal access token](#prerequisites-github-token). The token must have **Contents: Read and write** (fine-grained) or `repo` scope (classic).
2. **Repository** — pick the repo (e.g. `david-pizzi-msft/data-ai-reference`).
3. **Branch** — `main`.
4. **Git folder** — enter the workspace's folder path exactly. One workspace per folder:

    | Workspace | Git folder value |
    | --- | --- |
    | Medallion | `git/ms-fabric-essentials/medallion-architecture` |
    | Analytics Dev (deployment pipelines) | `git/ms-fabric-essentials/deployment-pipelines` |

5. Select **Connect and sync**. On first sync, if the workspace has items and the folder is empty (or just a README), Fabric pushes the item definitions into that folder.

!!! tip "Get the folder name exact"
    Type the folder path exactly, including the trailing part and the plural **`ms-fabric-essentials`**.
    A typo creates a *new* folder in the repo (an earlier attempt produced a stray singular
    `ms-fabric-essential/` folder). Nested paths of 3+ levels work fine.

!!! warning "Disconnecting does not delete committed content"
    Disconnecting a workspace from Git in Fabric **removes the connection only** — it does **not**
    remove what was already committed to the repo. If you reconnect to a *different* folder, the old
    folder's content stays behind as a duplicate and must be deleted in the repo manually.

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
