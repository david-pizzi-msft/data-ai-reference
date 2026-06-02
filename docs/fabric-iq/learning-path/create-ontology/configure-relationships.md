# Configure ontology relationships

Entity types bound to data give you facts about individual concepts — a hospital, a department, a patient. **Relationship types** define the connections between them: a department *belongs to* a hospital, a patient *is admitted to* a room, equipment *monitors* a patient.

Like entity types, relationship types need two things: a **definition** (which entity types can connect) and a **binding** (which table and columns contain the actual connection data). Without the binding, the relationship exists but can't be queried.

## Definitions vs. bindings

A relationship type establishes the *possibility* of a connection — a *monitors* type says vital-sign equipment can monitor patients, but not *which* equipment monitors *which* patients. That requires binding to source data.

- When you **generate** an ontology from a semantic model, relationship type definitions are created automatically — but they're not yet bound to source data.
- When you **build** manually, you create both the definitions and their bindings yourself.

Either way, every relationship type requires configuration to become queryable.

## Create relationship types

Give the relationship a name describing the connection — *monitoredBy*, *contains*, *admittedTo* — and specify the two entity types it connects.

![The Add relationship type dialog with a name field and source/target entity type dropdowns.](https://learn.microsoft.com/en-us/training/wwl-data-ai/create-ontology-with-fabric-iq/media/add-relationship-type.png){ .screenshot }

The source and target must be **different** entity types. For a relationship showing which equipment monitors which patients, `VitalSignEquipment` is the source and `Patient` is the target.

## Configure the relationship source data

Configuration connects the definition to actual data. Under **Source data**, select the workspace, lakehouse, and table that contains identifying information for **both** entity types — each row references a source entity and a target entity by ID.

For a *contains* relationship between Hospital and Department, the source table is `departments`: it contains `HospitalId` (which hospital each department belongs to) and `DepartmentId` (each department), so each row links a specific hospital to a specific department.

After selecting the table, choose a **source column** for each entity type — the column whose values match that entity type's key. For Hospital select `HospitalId`; for Department select `DepartmentId`.

![Relationship configuration with the departments table and HospitalId and DepartmentId mapped to entity keys.](https://learn.microsoft.com/en-us/training/wwl-data-ai/create-ontology-with-fabric-iq/media/relationship-configuration.png){ .screenshot }

Every row with values in both columns creates one relationship instance. Each relationship type needs its own configuration — a Patient–Room relationship uses the `patients` table (`PatientId`, `CurrentRoomId`), a VitalSignEquipment–Patient relationship uses the `vitalsignequipment` table (`EquipmentId`, `PatientId`). The same table can serve multiple relationships if it contains the necessary keys.

With entity types bound to data and relationship types configured, your ontology is **complete** — definitions backed by source data, connections established, ready to [preview](preview.md).
