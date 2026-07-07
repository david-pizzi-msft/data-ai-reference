# Deployment pipelines — Fabric Git folder

Git integration target for the **Analytics Dev** workspace used in the deployment pipelines lab.
Fabric serializes its item definitions (lakehouse, semantic model, report) into this folder on
commit. Promotion to **Analytics Prod** is handled by the deployment pipeline, not Git.

- **Fabric Git folder path:** `/git/ms-fabric-essentials/deployment-pipelines`
- **Connected workspace:** `Analytics Dev`
- **Source workshop:** [AzurePortal/4_CICD/0_deployment-pipelines](https://github.com/Cloud2BR-MSFTLearningHub/MS-Fabric-Essentials-Workshop/tree/main/AzurePortal/4_CICD/0_deployment-pipelines)
