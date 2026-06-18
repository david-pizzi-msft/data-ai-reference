# What is a data agent?

A **Fabric data agent** lets your team have conversations — in plain English — about data stored in Fabric OneLake, and receive relevant, context-rich answers. People without AI expertise or deep knowledge of the data structure can still get precise answers, because the agent handles query generation, validation, and execution for them.

[Official docs](https://learn.microsoft.com/en-us/fabric/data-science/concept-data-agent)

!!! info "Ontology as a source"
    A data agent can query an ontology alongside lakehouses, warehouses, Power BI semantic
    models, KQL databases, and Microsoft Graph — grounding natural-language answers in the
    enterprise vocabulary defined by Fabric IQ.

## How it works

The agent uses LLMs (Azure OpenAI Assistant APIs) to interpret a question, pick the most relevant data source, generate a query, validate it, and execute it — all **read-only**, under the requesting user's permissions.

1. **Question parsing & validation** — checks the question against security, responsible-AI (RAI), and Microsoft Purview policies.
2. **Data source identification** — evaluates the question against all configured sources using the user's schema access.
3. **Tool invocation & query generation** — picks the matching tool:
    - **NL2SQL** for lakehouses and warehouses
    - **NL2DAX** for Power BI semantic models
    - **NL2KQL** for KQL databases (can use KQL UDFs)
    - **Microsoft Graph** queries for organizational data
4. **Validation & execution** — runs the validated query and formats results into tables, summaries, or key insights, with the intermediate steps and generated code shown for transparency.

## Governance & intent layers

Multiple intent layers shape behaviour, from highest to lowest precedence:

| Layer | What it controls |
| --- | --- |
| **Organizational** | Tenant-wide policies and compliance — cannot be overridden. |
| **Role-based** | Workspace governance and permission boundaries. |
| **Developer** | Custom instructions, examples, and data source configuration. |
| **User** | Questions submitted during a conversation. |

Higher layers always override lower ones. Microsoft **Purview** controls (DLP, access restriction policies, sensitivity labels, audit, eDiscovery) apply to the underlying sources, so answers may be truncated or blocked accordingly.

## Data agent vs. copilot

- **Configurability** — data agents are highly configurable (custom instructions/examples); copilots are preconfigured.
- **Scope** — copilots assist with in-product tasks (generating notebook code, warehouse queries); data agents are standalone artifacts that query data across OneLake and can be invoked by Microsoft 365 Copilot, Copilot Studio, Azure AI Foundry, or Teams as part of multi-agent workflows.

## Key limitations

- **Read-only** — generates SELECT-style queries only; never creates, updates, or deletes data.
- **No unstructured data** (`.pdf`, `.docx`, `.txt`) and no standalone lakehouse files unless exposed as tables.
- **English only** for best performance; the underlying LLM can't be changed.
- Responses are capped at **25 rows × 25 columns** — designed for conversational insight, not full data export.
- Up to **100 example queries** per data source; conversation history may not always persist.
- Source and agent capacities must be in the **same region**.

*Curated from [Microsoft Learn](https://learn.microsoft.com/en-us/fabric/data-science/concept-data-agent) · Updated 2026-05-11*
