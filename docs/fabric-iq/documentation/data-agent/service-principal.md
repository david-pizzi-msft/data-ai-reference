# Service principal

A Microsoft Entra **service principal (SPN)** is a non-interactive, app-based identity. Data agents support SPN authentication so you can call a **published** agent from automation, background services, custom apps, and CI/CD pipelines — without a signed-in user.

[Official docs](https://learn.microsoft.com/en-us/fabric/data-science/data-agent-service-principal)

!!! info "Preview"
    Service principal authentication for data agents is in preview.

## How it works

The data agent treats the SPN like any other Entra identity:

- The SPN needs access to the **workspace** where the agent is published.
- The SPN needs **read access to each data source** attached to the agent — it can only query data its identity can access.
- The SPN acquires an Entra token for the Fabric resource (`https://analysis.windows.net/powerbi/api/.default`) via the **client credentials flow** and uses it as a bearer token to ask questions.

## Setup steps

1. **Register an app** in Microsoft Entra ID → copy the **Application (client) ID** and **Directory (tenant) ID**; add a credential (certificate, federated credential, or secret).
2. **Enable Fabric APIs** — a tenant admin turns on **Service principals can use Fabric APIs** (Admin portal → Tenant settings → Developer settings), scoped to the org or a security group.
3. **Grant workspace access** — a workspace Admin/Member adds the SPN (Member or Contributor role).
4. **Grant data source access** — at least read on every attached source.
5. **Acquire a token and call** the agent using the client credentials flow.

## Limitations

- **Managed identities** aren't supported — use a service principal.
- The SPN must have explicit access to **every** attached data source; sharing the agent item alone isn't enough.
- Not yet supported for agents connected to a **KQL database (Kusto)**.

*Curated from [Microsoft Learn](https://learn.microsoft.com/en-us/fabric/data-science/data-agent-service-principal) · Updated 2026-05-12*
