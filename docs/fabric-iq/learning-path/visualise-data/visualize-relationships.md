# Visualise relationships in the relationship graph

Having explored entity instances, you now expand the relationship graph to see how those instances connect, run a query to load real data, and explore the results interactively.

## Expand the graph

From the entity type overview, select **Expand** on the relationship graph tile to open the full graph view in Graph in Microsoft Fabric.

![The Rooms entity type overview with the Expand button highlighted on the relationship graph tile.](https://learn.microsoft.com/en-us/training/wwl-data-ai/visualize-ontology-fabric-iq/media/expand-graph.png){ .screenshot }

The full view opens showing the **schema** — Patients `admittedTo` Rooms `inDepartment` Departments. This is the structure of the ontology; no instance data has loaded yet.

## Run the default query

Select **Run query** from the ribbon. The default query retrieves the selected entity type and all entities one relationship hop away.

![The Rooms graph view with Run query highlighted and a populated graph of patient, room, and department nodes connected by edges.](https://learn.microsoft.com/en-us/training/wwl-data-ai/visualize-ontology-fabric-iq/media/default-query.png){ .screenshot }

The lower panel populates with real instance nodes — individual rooms, the patients admitted to them, and the departments they belong to. Each labelled arrow is a live edge — an actual connection from the data, not a constructed join.

## Select nodes and navigate

The graph is interactive — select any node to view its property values. Selecting a room surfaces its `RoomNumber`, `DepartmentId`, and `RoomType`; a department shows its name and ID; a patient shows admission details.

The Lamna ontology extends further: Patients connect to VitalSignEquipment via `assignedToPatient`. Following the full path Department → Room → Patient → VitalSignEquipment answers *"Which monitors are active for patients in the ICU?"* — by following named edges, not writing joins. Next, the [Query builder](query-builder.md) adds filters and component controls to target specific questions directly.
