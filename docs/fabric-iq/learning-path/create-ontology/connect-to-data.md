# Connect an ontology to data

Whether you built your ontology manually or generated it from a semantic model, entity types need **data bindings** before they can be queried. The manual path has no bindings yet; the generated path has static bindings already, but still needs **time-series bindings** for streaming data. Both paths meet here.

## Understand data bindings

A binding maps each property in your ontology to a specific column in a source table — telling the system *"when someone queries `HospitalName`, read it from the `HospitalName` column in the `hospitals` table."* Without bindings, the ontology has structure but no values.

Two binding types serve different data characteristics:

- **Static bindings** connect to data that changes infrequently — hospital names, department locations, room numbers. Static data lives in **lakehouse** tables.
- **Time-series bindings** connect to streaming data arriving continuously — patient vital signs, sensor readings — each timestamped. Time-series data lives in **eventhouse** tables.

Both establish the entity type key that uniquely identifies each instance.

## Configure static data bindings

Selecting an entity type opens the configuration pane; the **Bindings** tab manages data connections.

![The entity type configuration pane on the Bindings tab with the Add data to entity type button.](https://learn.microsoft.com/en-us/training/wwl-data-ai/create-ontology-with-fabric-iq/media/binding-configuration.png){ .screenshot }

Select **Add data to entity type** to open the OneLake catalog and choose your source — for static bindings, the **lakehouse**.

![The OneLake catalog picker showing a lakehouse and an eventhouse as available sources.](https://learn.microsoft.com/en-us/training/wwl-data-ai/create-ontology-with-fabric-iq/media/onelake-catalog-picker.png){ .screenshot }

Choose the specific table to bind to.

![The Choose data source screen with the lakehouse selected and dbo/hospitals as the chosen table.](https://learn.microsoft.com/en-us/training/wwl-data-ai/create-ontology-with-fabric-iq/media/choose-data-source.png){ .screenshot }

The interface then maps source columns to entity properties.

![The property binding screen with source columns mapped to entity property names.](https://learn.microsoft.com/en-us/training/wwl-data-ai/create-ontology-with-fabric-iq/media/binding-completed.png){ .screenshot }

After saving, configure the entity type **key** to identify which property uniquely identifies each instance.

![The key configuration screen showing property selection for the entity type key.](https://learn.microsoft.com/en-us/training/wwl-data-ai/create-ontology-with-fabric-iq/media/entity-key-configuration.png){ .screenshot }

Each entity type needing static data — hospitals, departments, rooms, patients — follows this process to connect structure to lakehouse tables.

## Add time-series data bindings

Some entities need **both** static and time-series data. Vital-sign monitoring equipment has static attributes (which patient it monitors, equipment type) plus streaming measurements (heart rate, oxygen level updating every few seconds). This requires binding the entity to **two tables**.

### The dual-binding pattern

The equipment is defined in one source, and the readings it generates in another, related by `EquipmentId`:

**`VitalSignEquipment`** (lakehouse — static attributes)

| EquipmentId | PatientId | EquipmentType    | MonitoringStartDate |
| ----------- | --------- | ---------------- | ------------------- |
| M001        | 5         | HeartRateMonitor | 2024-01-15          |
| M002        | 8         | OxygenMonitor    | 2024-01-16          |

**`VitalSignsReadings`** (eventhouse — streaming measurements)

| ReadingId | EquipmentId | Timestamp           | HeartRate | OxygenSaturation |
| --------- | ----------- | ------------------- | --------- | ---------------- |
| 1         | M001        | 2024-01-15 08:00:01 | 72        | 98               |
| 2         | M001        | 2024-01-15 08:00:06 | 74        | 97               |
| 3         | M002        | 2024-01-15 08:00:02 | 68        | 99               |

The time-series data deliberately doesn't duplicate context — it focuses on measurements. The static binding creates the complete equipment entities; the time-series binding adds the continuously updating measurement properties.

!!! warning "Static binding must come first"
    Time-series data needs existing entities to attach to. The system uses `EquipmentId` from the static binding to match streaming readings to the correct equipment entity.

### Configure the time-series binding

Follow the same steps as a static binding — **Add data to entity type**, choose the **eventhouse**, select the `VitalSignsReadings` table — then on **Configure data binding** select **Timeseries** as the binding type and choose the timestamp column. The interface splits properties into **Static** (the linking key, `EquipmentId`) and **Timeseries** (the measured values, `HeartRate`, `OxygenSaturation`).

![Configure data binding with Timeseries type and properties divided into Static and Timeseries sections.](https://learn.microsoft.com/en-us/training/wwl-data-ai/create-ontology-with-fabric-iq/media/time-series-binding.png){ .screenshot }

With entity types connected to their data, the next step is [configuring relationship bindings](configure-relationships.md).
