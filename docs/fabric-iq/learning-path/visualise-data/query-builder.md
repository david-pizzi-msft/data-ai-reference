# Filter and explore with the Query builder

The Query builder gives you controls to go further than the default query — filtering results by property values, focusing the graph on specific entity types, and switching between views.

## Cross-source querying

The Lamna ontology binds data from both a lakehouse and an eventhouse. When a query includes both Patient and VitalSignEquipment instances, the ontology translates that into separate queries against each source and connects the results through the `assignedToPatient` relationship binding — a unified view with **no JOIN statements** or knowledge of the underlying tables.

## Query builder controls

In the full graph view, the **Query builder** ribbon provides the controls, and the **Components** pane on the right controls which entity and relationship types are visible.

![The Patients graph view with the Query builder ribbon highlighted and the Components pane listing node and edge types.](https://learn.microsoft.com/en-us/training/wwl-data-ai/visualize-ontology-fabric-iq/media/query-builder-ribbon.png){ .screenshot }

Key controls:

- **Run query** — execute the current query and load instance data.
- **Add filter** — narrow results by property value on a specific entity type.
- **Remove filter** / **Reset filters** — remove one filter, or clear them all.
- **Diagram view** — switch between Diagram, Card, and Table views.

## Control components

The **Components** pane lists every entity and relationship type as checkboxes. Unchecking types that aren't relevant keeps the results graph readable.

![The Components pane with five node types and four edge types, where Rooms, Patients, VitalSignEquipment, admittedTo, and assignedToPatient are checked.](https://learn.microsoft.com/en-us/training/wwl-data-ai/visualize-ontology-fabric-iq/media/components.png){ .screenshot }

To answer *"Which vital-sign monitors are assigned to patients in Critical Care rooms?"*, only Rooms, Patients, VitalSignEquipment and the `admittedTo` and `assignedToPatient` edges are needed — Hospitals and Departments stay unchecked.

## Add filters

Select **Add filter**, then choose the entity type, property, and value to match.

![The Filter dialog with For set to Rooms and Where set to RoomType equals Critical Care.](https://learn.microsoft.com/en-us/training/wwl-data-ai/visualize-ontology-fabric-iq/media/query-filter.png){ .screenshot }

This limits results to rooms where `RoomType = Critical Care`. Multiple filters can be active at once — each narrows results further, and all must be satisfied simultaneously.

## View results

After running the query, results appear below the graph. Use the **Diagram view** dropdown to switch views.

![The query results panel in Card view showing three Critical Care room cards.](https://learn.microsoft.com/en-us/training/wwl-data-ai/visualize-ontology-fabric-iq/media/query-results-views.png){ .screenshot }

- **Diagram view** — the graph structure; select any node to inspect its properties.
- **Card view** — each instance as a card with property values inline.
- **Table view** — rows and columns, useful for comparing values across many results.
