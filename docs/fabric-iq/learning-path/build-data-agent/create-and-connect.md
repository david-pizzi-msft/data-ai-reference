# Create an agent and connect an ontology

This unit walks through creating a data agent in a Fabric workspace, connecting an ontology as its data source, and configuring instructions to improve query accuracy.

## Create the data agent item

Creating a data agent follows the same pattern as other workspace items:

1. In a Fabric workspace, select **+ New item**.
2. Type `data agent` in the search box and select **Data agent**.
3. Enter a name, such as `LamnaHealthcareAgent`, and select **Create**.

The agent interface opens immediately. The **Explorer** pane is empty until a data source is added — without one, the agent has no knowledge base to query.

![The Fabric data agent interface showing No data added in the Explorer pane.](https://learn.microsoft.com/en-us/training/wwl-data-ai/build-fabric-data-agent-ontology/media/data-agent-empty.png){ .screenshot }

## Add the ontology as a data source

1. Select **Add a data source**.
2. In the OneLake catalog, search for the ontology by name (e.g. `LamnaHealthcareOntology`).
3. Select it and choose **Add**.

The ontology's entity types appear in the **Explorer** pane — Hospital, Department, Room, Patient, and VitalSignEquipment — each expandable to view its attributes and relationships.

![The Explorer pane showing five entity types: Departments, Hospitals, Patients, Rooms, and VitalSignEquipment.](https://learn.microsoft.com/en-us/training/wwl-data-ai/build-fabric-data-agent-ontology/media/data-agent-explorer.png){ .screenshot }

## Configure agent instructions

**Instructions** are plain-language guidance that bridge how people ask questions and how concepts are defined in the ontology. Select **Agent instructions** from the ribbon to open a text area accepting up to 15,000 characters. Effective instructions typically include:

- **Domain description** — what the ontology models and its purpose. *"This ontology models hospital operations at Lamna Healthcare…"*
- **Terminology mappings** — common terms to ontology concepts. *"ICU refers to the Intensive Care Unit department. Critical Care rooms are ICU patient rooms."*
- **Scope guidance** — what the agent should and shouldn't answer. *"Answer questions about room assignments, department occupancy, and equipment allocation. Do not answer questions about billing or staffing."*

Instructions apply automatically as you type — there's no save button, and changes take effect immediately.

![The agent instructions pane showing example Lamna Healthcare instructions with domain description, terminology mappings, and scope guidance.](https://learn.microsoft.com/en-us/training/wwl-data-ai/build-fabric-data-agent-ontology/media/data-agent-instructions.png){ .screenshot }

With the agent created, the ontology connected, and instructions configured, the agent is ready to [test, validate, and publish](test-validate-publish.md).
