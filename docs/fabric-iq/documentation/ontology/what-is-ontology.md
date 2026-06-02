# What is an ontology? (preview)

An ontology is a shared, machine-understandable vocabulary of your business — the things in your environment (**entity types**), their facts (**properties**), and the ways they connect (**relationships**), plus constraints and rules that keep everything consistent. It's the core item of the Fabric IQ workload.

Think of it as a **business context layer** that provides:

- A catalogue of concepts (Product, Order, Plant, Sensor, Route) defined once and reused everywhere.
- **Data bindings** that link those concepts to real data in OneLake.
- A **graph** representation for navigation, lineage, and reasoning.
- A **query surface** to ask questions about concepts (not tables), including federated queries across sources.

Both humans and AI agents use this shared language for cross-domain reasoning and governed, decision-ready actions.

!!! note "Preview"
    Ontology is in preview. Enable the [required tenant settings](required-tenant-settings.md) before you start.

## Core concepts: defining an ontology

| Concept | What it is |
| --- | --- |
| **Entity type** | The reusable logical model of a real-world concept (Shipment, Product, Sensor). Standardises name, identifiers, properties, and constraints so every team means the same thing. |
| **Entity instance** | A concrete occurrence of an entity type, populated from data bindings. Tracks its source and when it was true, and can participate in relationships. |
| **Property** | A named fact about an entity, with a declared data type. May carry bindings and semantic annotations; enforces consistent types, units, and naming. |
| **Relationship** | A typed, directional link between entity types or instances, with attributes (distance, confidence, effectiveAt) and cardinality rules (one Customer → many Orders). |

## Core concepts: your data in the ontology

- **Data binding** — connects entity types, properties, and relationships to concrete data in OneLake ([lakehouse tables](https://learn.microsoft.com/en-us/fabric/data-engineering/lakehouse-overview), [eventhouse streams](https://learn.microsoft.com/en-us/fabric/real-time-intelligence/eventhouse), [semantic models](https://learn.microsoft.com/en-us/fabric/data-warehouse/semantic-models)). Adds schema-evolution rules, data-quality checks, and provenance, turning raw rows into governed business objects.

    !!! warning "Manual refresh"
        Upstream changes (e.g. new rows) must be **manually refreshed** before they appear in the ontology. See [refresh the graph model](https://learn.microsoft.com/en-us/fabric/iq/ontology/how-to-view-entity-type-details#refresh-the-graph-model).

- **Ontology graph** — a queryable instance graph built from your bindings and relationships. Nodes are entity instances, edges are links (asserted or derived) with metadata and lineage. Enables visual exploration, graph algorithms (paths, centrality, communities), and rule-driven inference. Requires [Graph in Microsoft Fabric](https://learn.microsoft.com/en-us/fabric/graph/overview) (enable the [Graph tenant setting](required-tenant-settings.md)). View it in the [entity type details](https://learn.microsoft.com/en-us/fabric/iq/ontology/how-to-view-entity-type-details).
- **Querying** — ask business-level questions over bound data. Start from entity types, filter by properties, traverse relationships, and aggregate over time. The layer routes queries to the most efficient engine ([GQL](https://learn.microsoft.com/en-us/fabric/graph/overview) for Graph, [KQL](https://learn.microsoft.com/en-us/kusto/query/) for Eventhouse). **NL2Ontology** converts natural-language questions into structured federated queries.

## Key benefits

- Cross-domain consistency and governance.
- AI/agent grounding for consistent reasoning.
- Explicit, navigable relationships for analytics and decisions — no custom join logic.

## Next steps

- Enable the [required tenant settings](required-tenant-settings.md).
- Work through the [ontology tutorial](tutorial.md) ([Learn tutorial](https://learn.microsoft.com/en-us/fabric/iq/ontology/tutorial-0-introduction)).
- See [generating an ontology from a semantic model](concepts/generating-from-semantic-model.md) ([Learn how-to](https://learn.microsoft.com/en-us/fabric/iq/ontology/tutorial-1-create-ontology?pivots=semantic-model#generating-an-ontology-from-a-semantic-model)).

[Official documentation](https://learn.microsoft.com/en-us/fabric/iq/ontology/overview)
