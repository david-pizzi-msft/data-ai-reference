# Explore the ontology

The ontology preview experience lets you explore your data — the real records from your lakehouse and eventhouse bound to your entity types. This unit covers navigating that experience: viewing entity instances and drilling into individual records.

## Nodes and edges

Your ontology is a **graph database**, built from two elements:

- **Nodes** — a single real record represented as a point in the graph. Each entity instance (a room, a department, a patient) is a node. Nodes have **labels** (the entity type), **properties** (attributes like `roomNumber`), and **a unique identity** (the key value).
- **Edges** — the connection between two nodes. The `admittedTo` relationship between Patient and Room creates edges. Edges have **a direction** (Patient → Room), **a type** (`admittedTo`, `inDepartment`), **source and target nodes**, and optionally their own properties.

![The Fabric IQ Graph view for Rooms with a query schema and a live populated graph of patient, room, and department nodes connected by admittedTo and inDepartment edges.](https://learn.microsoft.com/en-us/training/wwl-data-ai/visualize-ontology-fabric-iq/media/room-instance-graph.png){ .screenshot }

Those named connections make graph exploration powerful. To answer *"Which patients are in the ICU?"*, the graph starts at the ICU department node, follows `inDepartment` edges to its rooms, then `admittedTo` edges to the patients — no complex queries required.

## Open the entity type overview

Select an entity type in the **Entity Types** pane — for example, **Rooms** — then choose **Entity type overview** from the ribbon. The overview shows three sections: the relationship graph tile, property charts, and the entity instances table.

![The Rooms entity type overview with the relationship graph tile, property charts for RoomNumber/DepartmentId/RoomType, and an instances table of 10 rooms.](https://learn.microsoft.com/en-us/training/wwl-data-ai/visualize-ontology-fabric-iq/media/room-overview.png){ .screenshot }

The graph tile shows Rooms at the centre of two connections (Patients `admittedTo` Rooms `inDepartment` Departments). The instances table reflects the bound data source — each row is one room, each column a property defined on the Rooms entity type.

## Explore an entity instance

Select any row to open the **instance view** for that specific record. The instance properties panel shows the actual values for that one record — for room SUR-202: `RoomId` 8, `RoomNumber` SUR-202, `DepartmentId` 3, `RoomType` Post-Op.

![The Rooms instance view for Room 8 (SUR-202) with instance properties highlighted, a relationship graph tile, and property charts.](https://learn.microsoft.com/en-us/training/wwl-data-ai/visualize-ontology-fabric-iq/media/room-instance.png){ .screenshot }

The instance properties panel is the key difference from the overview: it shows the specific values for one record, not aggregates across all rooms. Next, you [expand the relationship graph](visualize-relationships.md) to see all instances and their connections together.
