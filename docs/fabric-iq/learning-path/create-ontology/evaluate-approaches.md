# Choose an ontology creation approach

Creating an ontology means defining business concepts (**entity types**), their characteristics (**properties**), and how they connect (**relationships**). Fabric IQ offers **two paths** — and both produce the same result: a complete ontology bound to your data sources in OneLake.

## Generate from a Power BI semantic model

Select an existing **Direct Lake** semantic model and Fabric IQ automatically generates entity types, properties, and relationship types: each table becomes an entity type, columns become properties, and model relationships become relationship types.

![A Power BI semantic model canvas with five tables and relationship connectors.](https://learn.microsoft.com/en-us/training/wwl-data-ai/create-ontology-with-fabric-iq/media/power-bi-semantic-model.png){ .screenshot }

Within minutes you have a working structure to refine. Auto-generated names like `hospitals_has_departments` are accurate but technical — you rename them to business vocabulary such as *"hospital contains department"*.

!!! note "Why Direct Lake?"
    For ontology generation the semantic model must use **Direct Lake** mode, which queries lakehouse data in place without copying it. This preserves the connection to OneLake's underlying structure that the ontology needs.

**Choose this when** you have a well-structured Direct Lake model representing your domain: you can explain what each table means as a business concept, relationships reflect how your business works, and most tables are relevant. You then invest time customising names to match your exact vocabulary.

## Build directly from OneLake

Start with an empty ontology and manually create each entity type by binding directly to OneLake sources — lakehouse tables and eventhouse streams. You define every business concept intentionally: which sources populate which entities, how properties are named, how entities connect.

This requires more upfront design work but produces clean structure immediately — no refinement phase, no cleanup of auto-generated technical names.

**Choose this when** you don't have a semantic model, existing models are optimised for reporting rather than business vocabulary, or you prefer designing from scratch. You need a clear understanding of your domain and how entities relate.

---

Both paths lead to the same destination. The next units teach the concepts through **manual creation** first (which reveals how ontology structure works), then show how **semantic-model generation** automates much of that process.
