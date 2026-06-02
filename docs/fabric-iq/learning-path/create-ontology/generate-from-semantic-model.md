# Generate an ontology from a Power BI semantic model

If you already have a Power BI semantic model representing your domain, you can generate an ontology directly from it — getting entity types, properties, and relationship structure in minutes instead of recreating everything by hand. Fabric reads the model and translates it: **tables become entity types, columns become properties** (data types preserved), and **model relationships define how entity types connect**.

## Generate the structure

Navigate to your semantic model in Fabric and select **Generate ontology**. Choose a workspace and name, and the system creates the foundational components automatically from all visible tables.

![The Generate Ontology button in the Power BI semantic model ribbon in Fabric.](https://learn.microsoft.com/en-us/training/wwl-data-ai/create-ontology-with-fabric-iq/media/generate-ontology-button.png){ .screenshot }

In the Lamna Healthcare scenario, tables like `hospitals`, `departments`, `rooms`, `patients`, and `vitalsignequipment` become entity types with those same names.

## Review what was generated

When generation completes, the ontology editor opens with the new entity types listed in the **Entity Types pane**.

![The ontology editor with the Entity Types pane listing hospitals, departments, rooms, patients, and vitalsignequipment.](https://learn.microsoft.com/en-us/training/wwl-data-ai/create-ontology-with-fabric-iq/media/ontology-editor.png){ .screenshot }

Generation handles several tasks automatically:

- **Entity types and properties** — each table becomes an entity type, each column a property with its data type preserved.
- **Entity data bindings** — configured automatically, because the model already connects to your lakehouse tables through Direct Lake.
- **Entity type keys** — inferred and configured where unique identifiers can be determined (e.g. `HospitalId` for hospitals).
- **Relationship type definitions** — created from the relationships in your semantic model.

## Complete the remaining configuration

After generation, finalise the ontology by:

- **Reviewing entity type keys** — verify each entity type has a key; most are configured automatically.
- **Verifying relationship types** — some bindings are configured automatically, others require manual configuration to become queryable (see [Configure ontology relationships](configure-relationships.md)).
- **Adding time-series bindings** — static lakehouse bindings are automatic; for streaming data, add time-series bindings to connect eventhouse sources (see [Connect an ontology to data](connect-to-data.md)).
