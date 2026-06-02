# Build an ontology manually

Building an ontology manually gives you complete control over your business vocabulary from the start. There are three steps:

1. **Define entity types** — name each business concept, add properties, set a key.
2. **Define relationship types** — connect entity types with named, directional relationships.
3. **Bind to data** — connect entity types and relationships to OneLake sources.

This unit covers steps 1 and 2 (binding is covered in [Connect an ontology to data](connect-to-data.md)). The healthcare scenario uses entity types such as **Hospital**, **Department**, **Room**, and **Patient**.

## Create entity types

Entity types represent the things your organisation works with. Each needs **properties** describing its characteristics and a **key** uniquely identifying each instance.

Select **Add entity type** from the ribbon and enter a business-friendly name — "Hospital", not a technical table name. Choose names that make sense spoken aloud: *"Hospital contains Department"*, *"Patient assigned to Room"*.

![Ontology editor with the Add entity type button in the ribbon and the Entity Types pane on the left.](https://learn.microsoft.com/en-us/training/wwl-data-ai/create-ontology-with-fabric-iq/media/create-entity.png){ .screenshot }

The **ribbon** holds all ontology actions, the **Entity Types pane** lists entity types as you create them, and the **canvas** lays them out visually.

### Add properties

Select **Add properties** to open the configuration dialog, then specify each property's name, data type, and property type.

![The Add properties dialog with an empty table for Property name, Data type, and Property type.](https://learn.microsoft.com/en-us/training/wwl-data-ai/create-ontology-with-fabric-iq/media/entity-properties-unfilled.png){ .screenshot }

For each property you make three decisions:

- **Property name** — use specific terms like `HospitalName` rather than generic `Name`, so queries stay unambiguous across entity types. Names must be 1–26 characters, alphanumeric plus hyphens/underscores, starting and ending with an alphanumeric character. They often match the source column names.
- **Data type** — `string` for text, `integer` for whole numbers, and so on. The data type must match the source column when you bind the ontology later.
- **Property type** — **static** for attributes that change infrequently (a hospital's name, a patient's date of birth), or **time series** for continuously arriving observations (vital-sign readings every few seconds). All entity types in this unit use static properties.

For Hospital you add `HospitalName` (string), `City` (string), `State` (string), and `HospitalId` (integer), then **Save**.

![The Add properties dialog filled with the Hospital properties.](https://learn.microsoft.com/en-us/training/wwl-data-ai/create-ontology-with-fabric-iq/media/hospital-properties.png){ .screenshot }

### Configure the entity type key

Every entity type needs a **key** identifying each unique instance. Without one, the system can't tell whether incoming data describes a new hospital or an update to an existing one.

Select **Add entity type key** in the configuration pane and choose one or more properties that uniquely identify instances — `HospitalId` for Hospital, `DepartmentId` for Department, `PatientId` for Patient. Keys can only use string or integer properties and are **required** before you can bind the entity type to data.

![The Hospital entity type configuration with HospitalId set as the key.](https://learn.microsoft.com/en-us/training/wwl-data-ai/create-ontology-with-fabric-iq/media/configured-properties.png){ .screenshot }

Repeat this pattern for each business concept: business-friendly properties, appropriate data types, and a key.

## Create relationship types

Relationship types describe how entity types connect — *hospitals contain departments, departments contain rooms, patients occupy rooms* — turning isolated definitions into a connected business model.

Select an entity type on the canvas, then **Add relationship type** from the ribbon. Identify the **source** and **target** entity types: for "Hospital contains Department", Hospital is the source and Department is the target. Direction matters — choose the one that matches how people ask questions about your business.

![The Add relationship dialog with Hospital as source and Department as target.](https://learn.microsoft.com/en-us/training/wwl-data-ai/create-ontology-with-fabric-iq/media/relationship-structure.png){ .screenshot }

Name the relationship with vocabulary that reads naturally when you say *source · name · target* together: enter "contains" for Hospital → Department, "has rooms" for Department → Room, "has Patient" for Room → Patient.

At this stage relationship types are **conceptual** — which entities relate and what those connections mean. The data binding comes later, when you [connect the ontology to data](connect-to-data.md). The next unit shows how [generating from a semantic model](generate-from-semantic-model.md) automates this entire process.
