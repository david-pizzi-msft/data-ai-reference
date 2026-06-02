# Preview the ontology

With entity types bound to data and relationships configured, the ontology is ready to explore. Select an entity type and choose **Entity type overview** from the ribbon to open the preview — a dashboard showing how your bound data looks as a populated ontology.

## The entity type overview

The overview shows three sections for the selected entity type:

- **Relationship graph** — a visual map of how this entity type connects to others. For Room, you see connections to VitalSignEquipment, Department, and Patient — confirmation that your relationship configuration worked.
- **Property charts** — bar charts showing the distribution of property values across all instances (e.g. the spread of `RoomNumber`, `DepartmentId`, and `RoomType` across all room instances).
- **Entity instances table** — the actual instances populated from your bound data. Selecting an instance opens its detail view, showing that row's property values and its connections to other entities.

![Room entity overview with the relationship graph, property charts, and entity instances table.](https://learn.microsoft.com/en-us/training/wwl-data-ai/create-ontology-with-fabric-iq/media/preview-experience.png){ .screenshot }

!!! note "First-time load"
    When you first open the preview you'll see an **"Updating your ontology"** message while the system processes your data. After 1–2 minutes, refresh your browser to display the overview.

The overview confirms your ontology is working — definitions populated with real data and connected across entity types. The [next module](../visualise-data/index.md) covers how to query and visualise this data using the Query builder and relationship graph.
