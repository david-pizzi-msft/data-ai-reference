# 2 · Create an ontology with Fabric IQ

> **Module 2 of 4** · 11 units

Ontologies in Fabric IQ transform your data into a business vocabulary everyone can understand. This module covers **two ways** to create ontologies — building manually to learn the core components, or generating automatically from Power BI semantic models to accelerate development. You practise both approaches and connect your ontology to data sources in OneLake, including lakehouse tables and eventhouse streams.

## Introduction

The module follows a fictional medical centre, **Lamna Healthcare**, that manages hospitals, departments, and rooms. Hospital, department, room, and patient records live as **lakehouse tables**, while continuous vital-signs monitoring from ICU equipment streams into an **eventhouse**. To enable natural-language queries across all of it, you create an ontology that unifies these sources with consistent business vocabulary.

You face one key decision up front: **how to start**. You can automatically generate structure from an existing Power BI semantic model, or build from scratch on OneLake data. Both paths reach the same destination — a complete ontology bound to your lakehouse tables and eventhouse streams, ready for natural-language queries and graph exploration.

By the end of this module you'll be able to:

- Evaluate the two approaches for creating an ontology in Fabric IQ.
- Build an ontology manually by working with entity types, properties, keys, and relationships.
- Generate an ontology from a Power BI semantic model.
- Connect an ontology to data sources and preview the result.

!!! info "Preview"
    Fabric IQ is currently in [preview](https://learn.microsoft.com/en-us/fabric/fundamentals/preview).

## Units

- **[Choose an ontology creation approach](evaluate-approaches.md)** — generate from a semantic model vs. build from OneLake, and how to decide.
- **[Build an ontology manually](build-manually.md)** — entity types, properties, keys, and relationship types.
- **[Generate from a Power BI semantic model](generate-from-semantic-model.md)** — automate the initial structure.
- **[Connect an ontology to data](connect-to-data.md)** — static and time-series data bindings.
- **[Configure ontology relationships](configure-relationships.md)** — bind relationship types to source data.
- **[Preview the ontology](preview.md)** — the entity type overview: graph, charts, and instances.

The module also includes two hands-on **exercises** (build manually, and generate from a semantic model) completed directly on Learn.

## Module assessment

Learn includes a short knowledge check on the two creation approaches, binding types, and relationship configuration. [Take the module assessment on Microsoft Learn](https://learn.microsoft.com/en-us/training/modules/create-ontology-with-fabric-iq/10-knowledge-check/) to earn a pass on your profile.

## Summary

Across this module you learned **two approaches** for creating ontologies in Fabric IQ — building manually to understand the core concepts, or generating from a Power BI semantic model to automate the initial structure. Both produce entity types, properties, relationship types, and entity type keys that define your business vocabulary.

You then connected those definitions to actual data through **bindings** — static data from lakehouse tables and time-series data from eventhouse streams. Bindings let the ontology represent real data without copying it, creating a unified layer that AI agents and other tools can query using business concepts instead of technical schemas. With a complete ontology in place, you're ready to explore and query it using Graph visualisation and the Query builder (module 3).

[Start this module on Microsoft Learn](https://learn.microsoft.com/en-us/training/modules/create-ontology-with-fabric-iq/)
