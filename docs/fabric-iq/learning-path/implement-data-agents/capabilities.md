# Understand Microsoft Fabric data agent capabilities

A **Fabric data agent** uses generative AI to let people interact with enterprise data in plain language. This unit covers what makes data agents useful for data accessibility and usability. [Official docs](https://learn.microsoft.com/en-us/training/modules/implement-fabric-data-agents/data-agent-capabilities)

## Interact with your data

Ask questions in plain English and get structured, human-readable answers. The agent analyses the input, determines the most appropriate data source, and selects the right tool to generate, validate, and execute the query — translating to SQL, DAX, or KQL behind the scenes.

!!! note "Read-only and permission-aware"
    The agent supports **read** operations only — it never creates, updates, or deletes data. It enforces the same permissions assigned to the user interacting with it, including Row-Level Security (RLS) and Column-Level Security (CLS).

## Configuration

Creators can test and evaluate how the agent interprets questions, then refine responses by iterating on queries and adjusting configuration. Organisation-specific **instructions**, **example queries**, and guidance fine-tune the agent so its answers align with your needs.

## Reasoning across multiple data sources

A single agent can reason over up to **five data sources** in any combination:

- Power BI semantic models.
- Eventhouse KQL databases.
- Lakehouses and warehouses.
- Ontologies (for semantic, business-term-aligned queries).
- Azure AI Search indexes (preview, via a connected Microsoft Foundry index, for unstructured content).

!!! important "Keep the table count low"
    The agent works best with **25 or fewer tables** selected across all data sources. It doesn't read unstructured files (.pdf, .docx, .txt) natively — connect an Azure AI Search index in Microsoft Foundry to reason over that content (preview).

## Integration inside and outside Fabric

Agents can be consumed beyond Fabric through **Copilot Studio**, **Microsoft Teams**, **Microsoft Foundry**, and **custom applications**.

| Aspect | Fabric data agents | Copilot for Microsoft Fabric |
| --- | --- | --- |
| Flexibility | Customisable with instructions and examples. | Preconfigured, limited customisation. |
| Use case | Broader scope; integrates with external tools (Copilot Studio, Teams, …). | Focused on in-Fabric tasks like notebooks and warehouse queries. |

Next, [implement an end-to-end data agent](end-to-end.md).
