# Fabric Git integration

This folder is the **Git integration target** for Microsoft Fabric workspaces. When a workspace
is connected to this repo (branch + a folder path below), Fabric serializes its item definitions
into the matching subfolder on commit — lakehouse, semantic model, report, and notebook metadata.

These are Fabric build **inputs**, not documentation, so they live outside `docs/` and are not
part of the MkDocs site.

## Folders

Each Git-connected workspace maps to its own subfolder, grouped by workshop.

| Folder | Fabric Git folder path | Corresponds to workshop |
| --- | --- | --- |
| `ms-fabric-essentials/medallion-architecture` | `/git/ms-fabric-essentials/medallion-architecture` | [1_MedallionArch](https://github.com/Cloud2BR-MSFTLearningHub/MS-Fabric-Essentials-Workshop/tree/main/AzurePortal/1_MedallionArch) |
| `ms-fabric-essentials/deployment-pipelines` | `/git/ms-fabric-essentials/deployment-pipelines` | [4_CICD/0_deployment-pipelines](https://github.com/Cloud2BR-MSFTLearningHub/MS-Fabric-Essentials-Workshop/tree/main/AzurePortal/4_CICD/0_deployment-pipelines) |
| `end-to-end/lakehouse` | `/git/end-to-end/lakehouse` | [Lakehouse end-to-end tutorial](https://learn.microsoft.com/en-us/fabric/data-engineering/tutorial-lakehouse-introduction) |
