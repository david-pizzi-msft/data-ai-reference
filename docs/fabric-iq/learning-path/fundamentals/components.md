# Explore Microsoft Fabric IQ components

Fabric IQ has four core components that work as an integrated ecosystem.

## Ontology items — define your business vocabulary

Where you build your shared vocabulary: define the concepts that matter (e.g. Hospital, Department, Room, Patient, VitalSign) with properties and named relationships, then bind them to data sources in OneLake. The ontology is consumed by Graph (for visualisation and traversal) and by data agents (for natural-language Q&A).

## Data agents — query data with natural language

A conversational Q&A system powered by generative AI (Azure OpenAI Assistant APIs). Configure up to **five data sources** in any combination (lakehouses, warehouses, KQL databases, Power BI semantic models, or ontologies). The agent parses a question, picks the most relevant source, and generates the right query — SQL for lakehouses/warehouses, DAX for semantic models, KQL for KQL databases, and business vocabulary for ontologies.

- Improve accuracy with **agent instructions** (which source to use for which question types) and **example queries** (question–query pairs).
- Enforces **read-only** access and security so users only see permitted data.
- Can be published to Microsoft 365 Copilot or integrated with Copilot Studio.

![The data agent chat interface showing a natural-language question and answer.](https://learn.microsoft.com/en-us/training/wwl-data-ai/understand-fabric-iq-fundamentals/media/data-agent-interface.png){ .screenshot }

## Graph in Microsoft Fabric — visualise and traverse relationships

Native graph storage and compute using a **labeled property graph** model (nodes and edges carry labels and properties). A managed graph is created automatically from your ontology's entity types and relationships; query it with **GQL**. Graph excels at relationship-heavy questions (hierarchies, assignments, dependency analysis) and operates directly on OneLake — no duplication or ETL. Ontology declares the concepts; Graph stores and computes the traversals.

![The graph interface for exploring relationships visually.](https://learn.microsoft.com/en-us/training/wwl-data-ai/understand-fabric-iq-fundamentals/media/graph-interface.png){ .screenshot }

## Semantic models — generate ontologies from existing data models

A Power BI semantic model is a structured representation (tables, columns, relationships, business logic) that's an excellent starting point. Generating an ontology from one automatically creates entity types (from tables), properties (from columns), relationship types (from model relationships), and keys — far faster than building from scratch. Afterwards, refine by verifying keys, confirming bindings, adding entity types from other sources (like eventhouse streams), and enriching relationships.

[View this unit on Microsoft Learn](https://learn.microsoft.com/en-us/training/modules/understand-fabric-iq-fundamentals/3-explore-fabric-iq-components/)
