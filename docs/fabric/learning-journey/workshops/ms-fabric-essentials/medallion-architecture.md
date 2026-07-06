# 1 · Medallion Architecture

!!! info "Source"
    [AzurePortal/1_MedallionArch](https://github.com/Cloud2BR-MSFTLearningHub/MS-Fabric-Essentials-Workshop/tree/main/AzurePortal/1_MedallionArch)

**Status:** 🟡 In progress

## What this lab does

Builds an end-to-end medallion pipeline in Microsoft Fabric — raw data lands in **Bronze**, gets cleaned in **Silver**, and is curated/aggregated in **Gold**, then surfaced to Power BI for reporting. Data moves between layers with notebooks (PySpark) and is orchestrated with Data Factory pipelines.

The three refinement layers:

| Layer | Lakehouse | Purpose |
| --- | --- | --- |
| 🥉 Bronze | `raw_Bronze` | Raw, append-only landing zone for ingested data. |
| 🥈 Silver | `cleansed_Silver` | Cleaned, transformed, enriched, quality-checked data. |
| 🥇 Gold | `curated_Gold` | Curated, aggregated data optimized for BI/reporting. |

## Flow

![Medallion architecture in Microsoft Fabric — SQL DB and Azure Data Lake feed Bronze via Data Pipelines/Data Factory, then Dataflows/Notebooks and Data Factory move data Bronze → Silver → Gold, with a Shortcut into a Lakehouse in OneLake, Z-Order/V-Order optimization, and a Power BI report in Direct Lake mode (with Copilot)](../images/medallion-architecture.png)

Simplified view:

```mermaid
flowchart LR
    SQL[(SQL DB)] -->|Data pipelines| B
    ADLS[(Azure Data Lake)] -->|Data Factory| B
    subgraph WS[Fabric Workspace]
        direction LR
        B[🥉 Bronze<br/>raw] -->|Dataflows /<br/>Notebooks| SL[🥈 Silver<br/>cleaned]
        SL -->|Data Factory| G[🥇 Gold<br/>curated]
    end
    G -->|Shortcut| LH[(Lakehouse<br/>in OneLake)]
    G --> OPT[Z-Order → V-Order]
    OPT --> PBI[📊 Power BI report<br/>Direct Lake mode]
    CP([Copilot]) -.-> PBI
```

## Things to remember

- Data written between layers using `write.format("delta")`; Silver→Gold aggregations use `groupBy()` / `agg()`.
- Fabric can auto-create the medallion flow for you.
- The **Gold** layer needs a **SQL Analytics Endpoint** to be reportable.
- Power BI reads Gold in **Direct Lake** mode; `auto-create report` / Copilot needs AI features enabled in the tenant.
- Alternative to pipelines for SQL sources: **SQL mirroring** (keeps a synced copy in Fabric).
- Requires an Azure subscription.

## Notes

- **Medallion architecture** is a data design pattern for lakehouses that organizes data into progressively refined layers (Bronze → Silver → Gold). It's a best practice for managing the data lifecycle and data quality.
- Each layer lives in its own lakehouse: `raw_Bronze`, `cleansed_Silver`, `curated_Gold`.
- Movement between layers is done in notebooks (PySpark, Delta format) and/or orchestrated with Data Factory pipelines that can be scheduled with triggers.
- Reporting: create a **semantic model** on Gold, then build Power BI reports in **Direct Lake** mode (optionally via Copilot `auto-create report`).

## Key takeaways

Why the medallion architecture is worth it:

- **Data quality** — layered structure lets you apply quality checks and transformations in stages, so Gold is reliable and analysis-ready.
- **Scalability** — each layer's pipelines scale independently, giving flexibility and efficiency.
- **Performance** — the Gold layer is optimized (incl. V-Order), so reporting/analytics queries run faster.
- **Simplicity** — the pipeline is broken into smaller, purposeful steps.
- **Auditability** — clear data lineage makes it easy to trace data origin and the transformations applied at each stage.
