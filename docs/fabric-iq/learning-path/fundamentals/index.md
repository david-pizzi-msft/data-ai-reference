# 1 · Understand Microsoft Fabric IQ fundamentals

> **Module 1 of 4** · 6 units

Fabric IQ provides a way to define business vocabulary in an ontology and bind it to data sources. This module covers ontology items, data agents, Graph in Microsoft Fabric, and Power BI semantic models, and shows how ontology modelling differs from traditional analytical modelling by starting with **business concepts** rather than specific use cases.

## Introduction

Picture a data analyst at a healthcare provider. Patient records sit in lakehouse tables while vital signs stream continuously from ICU monitors into an eventhouse. When administrators ask *"Which ICU patients have elevated vital signs?"* or *"How many beds are occupied on the surgical floor?"*, the analyst has to manually join the lakehouse tables to the eventhouse streams, translate business terms into technical column names, and write complex queries. Business users can't explore the data themselves — they wait on the analyst, and by the time answers arrive, conditions may already have changed.

Fabric IQ removes that bottleneck. You define business vocabulary — concepts such as **Patient**, **Department**, and **Room** with their properties and relationships — in an ontology, then bind those concepts to your data sources in OneLake. This creates a semantic layer that business users can query in natural language through **data agents** or explore visually through **Graph in Microsoft Fabric**, without anyone writing a query.

By the end of this module you'll be able to:

- Explain what Fabric IQ is and how ontologies define business vocabulary.
- Describe the role of ontology items in creating entity types, properties, and relationships.
- Distinguish the roles of each component: ontology items, data agents, Graph, and Power BI semantic models.
- Compare ontology modelling's concept-driven approach with traditional use-case-driven modelling.

!!! info "Preview"
    Fabric IQ is currently in [preview](https://learn.microsoft.com/en-us/fabric/fundamentals/preview).

## Units

- **[Get started with Fabric IQ](get-started.md)** — where IQ fits, the ontology interface, and the build–bind–query workflow.
- **[Explore Fabric IQ components](components.md)** — ontology items, data agents, Graph, and semantic models.
- **[The ontology modeling paradigm](modeling-paradigm.md)** — business concepts over table schemas.

## Module assessment

Learn includes a short knowledge check covering what Fabric IQ is, how the components work together, and how ontology modelling differs from traditional modelling. [Take the module assessment on Microsoft Learn](https://learn.microsoft.com/en-us/training/modules/understand-fabric-iq-fundamentals/5-knowledge-check/) to earn a pass on your profile.

## Summary

Fabric IQ lets you define business vocabulary once in an ontology, enabling natural-language queries and graph visualisation over your data. Across this module you learned:

- **What Fabric IQ is** and how it fits within the Fabric data platform.
- **The build–bind–query workflow** — defining entity types and relationships, binding them to lakehouse tables and eventhouse streams, and querying through Graph or data agents. Ontologies can be generated from an existing Power BI semantic model or built from scratch on OneLake data.
- **The four components** — ontology items define vocabulary, data agents answer natural-language questions across sources, Graph visualises and analyses relationships, and Power BI semantic models can seed an initial ontology.
- **Why concept-driven modelling matters** — starting from core business concepts (rather than specific reporting needs) creates reusable definitions that both data agents and Graph can use, letting business users explore data in familiar terms.

[Start this module on Microsoft Learn](https://learn.microsoft.com/en-us/training/modules/understand-fabric-iq-fundamentals/)
