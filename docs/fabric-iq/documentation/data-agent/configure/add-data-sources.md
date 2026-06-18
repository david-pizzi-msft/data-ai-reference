# Add a data source

Connecting Fabric artifacts to a data agent lets users turn natural-language questions into precise queries. A single agent can combine **up to five** data sources in any mix — structured, real-time, semantic, and unstructured.

[Official docs](https://learn.microsoft.com/en-us/fabric/data-science/data-agent-add-datasources)

## Supported sources

| Category | Artifacts | Query language | Key scenario |
| --- | --- | --- | --- |
| **SQL** | Lakehouse, Warehouse, SQL Database, Mirrored Databases | T-SQL (NL2SQL) | Structured analytics over relational / Delta data |
| **Eventhouse** | KQL Database | KQL (NL2KQL) | Real-time & time-series analytics |
| **Semantic model** | Power BI semantic models | DAX (NL2DAX) | Business logic, measures, curated metrics |
| **Graph** | Graph model | GQL (NL2GQL) | Relationship-rich exploration |
| **Ontology** | Fabric ontology | Ontology-native | Domain knowledge & semantic context |
| **Azure AI Search** | Azure AI Search index | NL + search | Unstructured retrieval (PDFs, text) |

For each source the agent translates the question, **validates** the query against the selected schema, then executes against the source endpoint.

## Configuration support by source

| Configuration | SQL | Eventhouse | Semantic model | Graph | Ontology |
| --- | :-: | :-: | :-: | :-: | :-: |
| Schema selection | ✅ | ✅ | ✅* | ❌ | ❌ |
| Agent instructions | ✅ | ✅ | ✅ | ✅ | ✅ |
| Data source instructions | ✅ | ✅ | ❌* | ✅ | ❌ |
| Data source description | ✅ | ✅ | ❌ | ✅ | ✅ |
| Example queries | ✅ | ✅ | ❌* | ✅ | ❌ |

*\*Semantic models are configured mainly through **Prep for AI** (AI data schemas, AI instructions, verified answers). See [Semantic model best practices](semantic-model-best-practices.md).*

For **Azure AI Search** indexes, configure Display Name, Search Type (full-text / hybrid / semantic), Number of Documents (3–20), Context/Description, and Agent instructions — see [Connect to a Foundry Search Index](foundry-search-index.md).

*Curated from [Microsoft Learn](https://learn.microsoft.com/en-us/fabric/data-science/data-agent-add-datasources) · Updated 2026-02-06*
