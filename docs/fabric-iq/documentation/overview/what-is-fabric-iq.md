# What is Fabric IQ? (preview)

Fabric IQ is a Fabric **workload** that unifies data across OneLake and contextualises it in the language of your business, then exposes it to analytics, AI agents, and apps with consistent semantic meaning.

!!! note "Preview"
    Fabric IQ is in preview. Capabilities and tenant settings are subject to change.

!!! info "Part of Microsoft IQ"
    Fabric IQ is the data-context capability within **Microsoft IQ**, working alongside
    **Work IQ** (how employees work), **Foundry IQ** (policies and authoritative docs), and
    **Web IQ** (context from the web). Fabric IQ provides context on business entities and data.

## Three layers of context

Fabric IQ brings three layers of business context, delivered through two core items —
**ontology** and **semantic model** — over shared OneLake data:

- **Unified data (OneLake)** — shortcuts, mirroring, and the OneLake catalog unify multicloud and on-premises data into one governed source of truth, and distribute it to Fabric workloads, Foundry, and Copilot Studio.
- **Business intelligence (Power BI semantic models)** — curated measures, hierarchies, and dimensions; ontologies can be generated from production semantic models to keep business language consistent.
- **Operational intelligence (ontologies)** — define entities, relationships, properties, rules, and actions; query in natural language via the **NL2Ontology** layer; operations agents monitor live data, detect anomalies, and take governed action.

## Why use it

- **Unify data** — combine lakehouses, eventhouses, and Power BI semantic models into one consistent model; reference external data in place via OneLake shortcuts (no ETL/copy).
- **Consistent language** — define a concept like *Customer* or *Asset* once, and have Power BI, notebooks, and agents interpret it the same way.
- **Faster onboarding** — new dashboards and AI experiences inherit business meaning automatically.
- **Governance & trust** — fewer duplicate, conflicting definitions; constraints improve data quality.
- **Cross-domain reasoning** — graph links let you traverse relationships (e.g. *Order → Shipment → Sensor → Cold-chain breach*) to explain outcomes.
- **AI-ready actions** — grounds copilots/agents in your ontology, and (via Fabric Activator) turns rules into governed, real-time actions like alerts.

## Where Fabric IQ fits in Fabric

Fabric IQ maps onto the standard Fabric capability stack:

- **Ingest & store** — builds on lakehouse tables, eventhouse streams, and existing Power BI semantic models. It can also consume data shared across tenants via [OneLake external data sharing](https://learn.microsoft.com/en-us/fabric/governance/external-data-sharing-overview), and Plan uses [OneLake mirroring](https://learn.microsoft.com/en-us/fabric/database/mirrored-database/overview) and [shortcuts](https://learn.microsoft.com/en-us/fabric/onelake/onelake-shortcuts) to keep data in place.
- **Model & represent semantics** — semantic models describe an analytical domain and can be exported to an ontology; the ontology adds entity types, properties, and relationship types, then binds them to data and builds a navigable graph automatically.
- **Analyze & visualize** — Power BI reports sit on semantic models; ontology and Graph add a visual graph and concept-level query experience. Sharing terminology keeps analysis consistent across items.
- **Operate & govern** — version, validate, and govern ontology definitions; lineage and auditing apply across all sources (including shortcuts and cross-tenant shares). Plan adds workflow approvals and audit trails for writeback.

## Items in the workload

| Item | Role |
| --- | --- |
| **[Ontology](https://learn.microsoft.com/en-us/fabric/iq/ontology/overview)** (preview) | Core item — the enterprise vocabulary and semantic layer (entity types, properties, relationships, rules) bound to real data. |
| **[Plan](https://learn.microsoft.com/en-us/fabric/iq/plan/overview)** (preview) | No-code platform for collaborative planning, reporting, and analytics on a shared data foundation. |
| **[Graph](https://learn.microsoft.com/en-us/fabric/graph/overview)** (preview) | Native graph storage/compute for path finding, dependency analysis, and graph algorithms. Integrated with ontology. |
| **[Data agent](https://learn.microsoft.com/en-us/fabric/data-science/concept-data-agent)** | Conversational Q&A built on generative AI; can use the ontology as a source. |
| **[Operations agent](https://learn.microsoft.com/en-us/fabric/real-time-intelligence/operations-agent)** (preview) | AI agent that monitors real-time data and recommends business actions. |
| **[Power BI semantic model](https://learn.microsoft.com/en-us/fabric/data-warehouse/semantic-models)** | Curated analytics model for reporting; ontologies can be generated from it to keep language consistent. |

Several items are shared with the Real-Time Intelligence and Power BI workloads.

## How the items fit together

- **Ontology + semantic model** — define concepts once; keep terminology and KPIs aligned across reports.
- **Ontology + Graph** — ontology declares *what connects and why*; Graph stores and computes the traversals.
- **Ontology + agents** — grounds data and operations agents in shared semantics and rules so they can reason and trigger governed actions.
- **Plan + semantic model** — reuse dimensions and measures for plan-versus-actuals analytics and dynamic forecasts.

## Choosing the right item

| Need | Use |
| --- | --- |
| Cross-domain consistency, governance, AI grounding | **Ontology** |
| Relationship-heavy questions (impact chains, shortest paths) | **Graph** |
| Trusted KPIs and fast self-service visuals | **Power BI semantic model** |
| Operational context, stateful twins, what-if simulation | **[Digital twin builder](https://learn.microsoft.com/en-us/fabric/real-time-intelligence/digital-twin-builder/overview)** (Real-Time Intelligence) |

*Curated from [Microsoft Learn](https://learn.microsoft.com/en-us/fabric/iq/overview) · Updated 2026-05-26*
