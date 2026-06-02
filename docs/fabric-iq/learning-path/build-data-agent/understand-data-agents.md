# Understand data agents and ontology as a data source

A **Fabric data agent** is a conversational interface to your data. People ask questions in natural language and get data-backed answers without writing queries or building reports. This module focuses on using an **ontology** as the data source.

## What a data agent does

When you ask a question, the agent identifies the relevant data source, generates a query in the appropriate language (SQL, DAX, KQL, or GQL), executes it, and returns the result. Each agent can connect to up to **five data sources** in any combination:

- **Lakehouses** / **Warehouses** — query tables using SQL.
- **KQL databases** — query event streams and time-series data using KQL.
- **Power BI semantic models** — query business metrics using DAX.
- **Ontologies** — query graph-structured domain models using GQL.
- **Microsoft Graph** — query organisational data (people, calendars, files).

!!! note "Identity and access"
    The agent runs under the querying user's Entra ID identity — it can only reach data that user is authorised to view, and it's strictly **read-only**.

## Why an ontology

An ontology uses business terms like `Room`, `Patient`, and `admittedTo` instead of raw column names like `rm_id` or `adm_flag`. The Lamna ontology defines entity types (Hospital, Department, Room, Patient, VitalSignEquipment), their properties, and relationships (a Patient is `admittedTo` a Room; a Room is `inDepartment` a Department).

Connecting the ontology gives the agent a **structured vocabulary** so it maps natural-language questions to defined entity types, properties, and relationship labels rather than guessing from raw column names — while still accessing the real data the ontology is bound to.

## How the agent uses the ontology

With an ontology source, the agent generates **GQL (Graph Query Language)**, designed to traverse the graph by following relationships. When a nurse manager asks *"Which departments have patients without vital-sign equipment assigned?"*, the agent matches "departments" to the `Department` entity type, traverses `inDepartment` to rooms, follows `admittedTo` to patients, and checks for a linked `VitalSignEquipment`.

Terms like "ICU" or "beds" aren't always exact matches to entity names, though — that's where **instructions** come in: natural-language guidance you write to explain how domain vocabulary maps to ontology concepts. The agent's GQL accuracy depends on how well the ontology models your domain and how clearly your instructions explain common question patterns.

## What the ontology layer provides

The agent inherits the ontology's **governance layer** — entity definitions, relationships, and data bindings are managed in one place rather than configured per agent. Add a new entity type and the agent immediately understands questions about it. This centralised structure also means every user asking the same question gets the same, repeatable interpretation. Next, you [create the agent and connect the ontology](create-and-connect.md).
