# 3 · Visualise ontology data with Fabric IQ

> **Module 3 of 4** · 7 units

Explore entity instances, visualise business-concept connections in the relationship graph, and filter across multiple data sources using the **Query builder** in Fabric IQ — without writing SQL joins.

## Introduction

Continuing the **Lamna Healthcare** scenario: the ontology is built — Hospital, Department, Room, Patient, and VitalSignEquipment entity types are defined and bound to the lakehouse and eventhouse. Now comes the reason you built it.

A clinical operations manager asks: *"Which rooms in the Intensive Care Unit currently have patients, and which vital-sign monitors are active there?"* Before the ontology, answering that meant a multi-table SQL join. With it, you explore the answer **visually** by following named relationships across your semantic layer.

By the end of this module you'll be able to:

- Explore entity instances to see real records from your data sources in the ontology.
- Expand the relationship graph to visualise entity connections.
- Filter and explore ontology data using the Query builder with filters and components.

!!! info "Preview"
    Fabric IQ is currently in [preview](https://learn.microsoft.com/en-us/fabric/fundamentals/preview).

## Units

- **[Explore the ontology](explore.md)** — nodes and edges, the entity type overview, and drilling into individual instances.
- **[Visualise relationships in the graph](visualize-relationships.md)** — expand the graph, run a query, and explore live nodes and edges.
- **[Filter and explore with the Query builder](query-builder.md)** — cross-source querying, filters, components, and result views.

The module also includes a hands-on **exercise** completed directly on Learn.

## Module assessment

Learn includes a short knowledge check on entity instances, the relationship graph, and the Query builder. [Take the module assessment on Microsoft Learn](https://learn.microsoft.com/en-us/training/modules/visualize-ontology-fabric-iq/6-knowledge-check/) to earn a pass on your profile.

## Summary

You explored the Lamna Healthcare ontology and saw how bound data appears as **entity instances** and how those instances connect through the **relationship graph**. The entity type overview showed individual records drawn from your lakehouse and eventhouse; expanding the graph populated it with real nodes and edges — departments connected to rooms, rooms to patients, patients to monitoring equipment. The **Query builder** let you filter (e.g. `RoomType = Critical Care`), control which entity and relationship types appear via the Components pane, and view results as a diagram, cards, or a table.

With visualisation in place, you've completed the core workflow: define business vocabulary, bind it to data, and explore the connected semantic layer to answer questions without writing joins. Module 4 turns this into a natural-language **data agent**.

[Start this module on Microsoft Learn](https://learn.microsoft.com/en-us/training/modules/visualize-ontology-fabric-iq/)
