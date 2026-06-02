# Get started with Fabric IQ

Fabric IQ is a workload in Microsoft Fabric for creating ontologies that define your business vocabulary. It sits alongside workloads like Data Engineering, Data Factory, Data Science, Data Warehouse, Real-Time Intelligence, and Power BI. Within IQ you create **ontology items** — Fabric artifacts that contain your ontology definitions and data bindings.

An ontology is a shared vocabulary of your business: the things in your environment (**entity types**), their facts (**properties**), and how they connect (**relationships**). Think of it as a business context layer with a catalogue of concepts, data bindings to lakehouse tables and eventhouse streams, a graph representation, and a query surface for federated queries across sources.

## Where Fabric IQ fits

- **Ingest and store** — references existing lakehouse tables and eventhouse streams; no data is moved or duplicated.
- **Model semantics** — the ontology defines entity types, properties, and relationship types (generated from a semantic model or built from scratch).
- **Analyze and visualise** — integrates with Graph in Microsoft Fabric for a visual graph and query experience, and grounds data agents with business context.

## Creating an ontology item

Create it like any Fabric item: **+ New item → Ontology (preview) → name it** (letters, numbers, underscores — no spaces or dashes) → **Create**. A [Fabric admin must enable the required tenant settings](../../documentation/ontology/required-tenant-settings.md) first.

The ontology has two views:

- **Configuration canvas** — where you build entity types, properties, and relationship types.
- **Preview experience** — shows instantiated entity instances and a graph visualisation, and lets you query in business language instead of SQL.

## The build–bind–query workflow

1. **Build** — define entity types, properties, and relationships (the concepts that matter to your business).
2. **Bind** — connect those definitions to data sources: lakehouse tables for static data, eventhouse streams for time-series data.
3. **Query** — ask questions using business concepts. The ontology federates queries to the most efficient engine (GQL for Graph, KQL for Eventhouse), so questions can span sources without knowing where data lives.

## Two paths to create an ontology

- **Generate from a Power BI semantic model** — auto-create entity types, properties, and relationships from an existing model, then refine.
- **Build from OneLake data** — create everything manually for full control when you have no semantic model.

[View this unit on Microsoft Learn](https://learn.microsoft.com/en-us/training/modules/understand-fabric-iq-fundamentals/2-get-started-with-fabric-iq/)
