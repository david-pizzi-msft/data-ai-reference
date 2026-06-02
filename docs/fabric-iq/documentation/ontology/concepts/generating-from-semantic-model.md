# Generating an ontology from a semantic model (preview)

A [Power BI semantic model](https://learn.microsoft.com/en-us/fabric/data-warehouse/semantic-models) is a logical description of a domain, holding your data and the relationships among it. When your data is in a semantic model, you can generate an ontology directly from it — a fast way to bootstrap when you already have a well-structured model.

!!! note "Preview"
    This feature is in preview.

## What gets created automatically

- A new **ontology item** in your workspace (you choose the name).
- **Entity types** matching the tables in the semantic model.
- **Static properties** from the table columns, plus **data bindings** linking rows to those properties.
- **Relationship types** following the relationships defined in the semantic model.

## What you must finish manually

- Bind **time-series data** to entity types (not created automatically).
- Review entity type **keys** and add any missing ones (especially multi-key scenarios).
- Bind **relationship types** to data.
- Review the whole ontology for completeness (entity types, properties, bindings, relationships).

## Support by semantic model mode

| Capability | Direct Lake | Import | DirectQuery |
| --- | --- | --- | --- |
| Generate entity types / properties / relationships | Supported | Supported | Supported |
| Generate entity type bindings to data | Not supported | Supported* | Not supported |
| Generate relationship bindings to data | Not supported | Supported (when primary key identified) | Not supported |
| Query data using bindings | Not supported | Supported (without measures / calculated columns) | Not supported |

\* Import mode: only when the backing lakehouse is in a workspace with inbound public access enabled; otherwise the ontology is created but the entity type has no data bindings.

## Key limitations

- Only **managed lakehouse tables** are supported (not external tables residing elsewhere).
- The ontology graph doesn't support delta tables with **column mapping** enabled (auto-enabled for special characters in column names, and for import-mode tables).
- Fabric Graph doesn't support the **`Decimal`** type — such properties return null on queries. (Floating-point `Double` is supported; `Decimal` is the fixed-precision type often used for currency.)
- Property names can only be **duplicated across entities when of the same type** (e.g. two string `ID` properties are fine; a string `ID` and an integer `ID` are not).
- You **can't** generate an ontology from a semantic model in the default **My workspace** — use a different workspace.
- Standard Power BI service limits apply (e.g. [model size](https://learn.microsoft.com/en-us/fabric/enterprise/powerbi/service-premium-large-models), [XMLA endpoint](https://learn.microsoft.com/en-us/fabric/enterprise/powerbi/service-premium-connect-tools#unsupported-semantic-models)).

For troubleshooting, see [Troubleshoot ontology](https://learn.microsoft.com/en-us/fabric/iq/ontology/resources-troubleshooting#troubleshoot-ontology-generated-from-a-semantic-model).

## Next steps

For a worked example, see the [ontology tutorial](../tutorial.md) ([Learn: Create an ontology](https://learn.microsoft.com/en-us/fabric/iq/ontology/tutorial-1-create-ontology?pivots=semantic-model)).

*Curated from [Microsoft Learn](https://learn.microsoft.com/en-us/fabric/iq/ontology/concepts-generate) · Updated 2026-01-20*
