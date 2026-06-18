# End-to-end tutorial

A full walkthrough that builds a data agent over the **AdventureWorks** dataset using a lakehouse — create and populate the lakehouse, add it to an agent, configure it, then consume it.

[Official docs](https://learn.microsoft.com/en-us/fabric/data-science/data-agent-end-to-end-tutorial)

!!! info "Preview"
    This tutorial covers preview features. Ensure the **Standalone Copilot experience** is enabled (Power BI admin portal → Tenant settings → Copilot).

## Steps

1. **Create a lakehouse (`AdventureWorksLH`)** — in a Fabric notebook, add a lakehouse data source and run the supplied script to upload the AdventureWorks tables (parquet) as lakehouse tables.
2. **Create the data agent** — **+ New Item** → search *Fabric data agent* → name it.
3. **Select data** — add the lakehouse and tick the tables to expose (e.g. `dimcustomer`, `dimdate`, `dimgeography`, `dimproduct`, `factinternetsales`, `factresellersales`, …).
4. **Provide instructions** — describe each table and when to use the source via **Data agent instructions**.
5. **Provide example queries** — add NL-question → SQL pairs per source (not supported for Power BI semantic models).
6. **Test and revise** — ask questions, refine instructions and examples, gather colleague feedback.
7. **Publish** — produces a shareable published URL.

## Consume the agent

- **Copilot in Power BI** — Copilot → *Add items for better results* → *Data agents* → confirm, then ask questions. Users only need **Read** on any included semantic model.
- **Programmatically** — call the published URL from a Fabric notebook using the OpenAI Assistants API pattern.

!!! warning "Capacity & API notes"
    - Stop the notebook session after loading data to avoid consuming capacity indefinitely.
    - The programmatic sample uses the OpenAI Assistants API, which OpenAI has **deprecated (shutdown 26 Aug 2026)**. Fabric will migrate this interface to the Responses API; plan accordingly.

*Curated from [Microsoft Learn](https://learn.microsoft.com/en-us/fabric/data-science/data-agent-end-to-end-tutorial) · Updated 2026-05-12*
