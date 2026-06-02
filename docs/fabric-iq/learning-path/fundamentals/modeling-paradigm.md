# The ontology modeling paradigm

Ontology modelling defines business concepts independent of specific analytical use cases — a different mindset from traditional analytical modelling.

## Business concepts over table schemas

Traditional modelling starts from *"What reports do we need? Which dimensions and facts?"* and designs star schemas with abbreviated columns (`pt_id`, `rm_num`). Independent teams often end up with inconsistent definitions of the same concept.

Ontology modelling inverts this: start from *"What are the core concepts in our business? How do they relate? What facts matter?"* You define Patient, Room, and Department as **entity types** using business language, with named relationships (*Department has Room*, *Room assigned to Patient*) that become the foundation for AI agents and graph queries.

![Hospital, Department, Room, and Patient entities connected by labeled relationships in Fabric IQ.](https://learn.microsoft.com/en-us/training/wwl-data-ai/understand-fabric-iq-fundamentals/media/ontology-modeling.png){ .screenshot }

## Entity types as reusable concepts

Entity types are conceptual definitions created **before** binding to data (unlike tables that combine schema and storage). Defining what "patient" means — its properties and identifier — at the entity-type level separates the conceptual model from the underlying table structure.

## Properties with semantic meaning

Source columns vary (`temp`, `temperature`, `body_temp`) for the same concept. In ontology modelling you define a standard property name (e.g. `Temperature`) once, then map it to whatever column exists during binding. Tools always see the standardised name. Properties can be marked as **identifiers** to ensure consistent entity resolution across sources.

![A VitalSign entity type showing standardised properties such as HeartRate, OxygenSaturation, and RespiratoryRate.](https://learn.microsoft.com/en-us/training/wwl-data-ai/understand-fabric-iq-fundamentals/media/vital-sign-properties.png){ .screenshot }

## Relationships between concepts

Relationships are **named, directional** connections between entity types — explicit concepts tools can query and visualise, unlike foreign keys that stay implicit until a JOIN. You can traverse them in the graph or with GQL (e.g. *Department has Room* → *Room assigned to Patient* to find all patients in a department).

## Bind concepts to data without duplication

Data binding connects entity types to data sources **without copying or moving data** — it stays in lakehouse tables or eventhouse streams. Different entity types bind to appropriate sources (e.g. Patient → lakehouse demographics, VitalSign → eventhouse stream), and queries federate across them, returning integrated results with no data movement.

![Data binding configuration mapping eventhouse source columns to entity type properties in Fabric IQ.](https://learn.microsoft.com/en-us/training/wwl-data-ai/understand-fabric-iq-fundamentals/media/data-binding.png){ .screenshot }

[View this unit on Microsoft Learn](https://learn.microsoft.com/en-us/training/modules/understand-fabric-iq-fundamentals/4-understand-ontology-modeling-paradigm/)
