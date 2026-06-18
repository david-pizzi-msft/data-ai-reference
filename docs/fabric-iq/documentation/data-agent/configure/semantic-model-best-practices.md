# Semantic model best practices

How you prepare a **Power BI semantic model** drives data agent accuracy. When querying a model, the **DAX generation tool** relies solely on the model's metadata and **Prep for AI** configuration — it ignores data-agent-level instructions.

[Official docs](https://learn.microsoft.com/en-us/fabric/data-science/semantic-model-best-practices)

## How it works

User questions flow through an **Orchestrator** that picks the source and invokes the right tool. For semantic models, the DAX tool generates, validates, and runs DAX using the schema, metadata (synonyms, value ranges, report-visual metadata), Prep for AI context, and conversation history.

## Prep for AI (three components)

| Component | Purpose |
| --- | --- |
| **AI data schema** | A focused subset of tables/columns/measures the AI should prioritise — reduces ambiguity, improves accuracy, lowers latency. Configure in Power BI → *Prep data for AI → Simplify data schema*. |
| **Verified answers** | User-approved responses triggered by specific questions (5–7 trigger phrasings each). Stored at model level; guide DAX generation toward the right query. |
| **AI instructions** | Business terminology, analysis defaults, routing rules — set here, **not** at agent level. |

!!! important "Keep model instructions in Prep for AI"
    Data agent doesn't support data-source instructions/descriptions for semantic models, and agent instructions aren't passed to the DAX tool. Put all model-specific guidance in Prep for AI; reserve agent instructions for cross-source rules (formatting, tone, routing).

## Recommended workflow

1. **Optimize the model** — star schema, efficient DAX, descriptions; use Best Practice / Memory Analyzer.
2. Define the **AI data schema** (only relevant objects, plus dependent objects).
3. Create **verified answers** for common questions.
4. Add the model to the agent and **test** responses.
5. Add **AI instructions** based on findings.
6. Prepare **report visuals** with descriptive titles.
7. **Verify the DAX** in each response; adjust config as needed.
8. Add **agent instructions** only for cross-source guidance.
9. **Validate & iterate** (optionally with the SDK); involve stakeholders.
10. Add **source control & deployment pipelines**.

## Common pitfalls

- Flat/denormalised tables instead of star schema; hidden fields in verified answers.
- Unnecessary or duplicate/overlapping measures; non-descriptive names (`TR_AMT`).
- Implicit measures; ambiguous date fields; conflicting or overly complex instructions.

!!! tip "Tooling"
    Use the [fabric-toolbox checklist & utilities](https://github.com/microsoft/fabric-toolbox/tree/main/samples/data_agent_checklist_notebooks), the Power BI MCP server, and Semantic Link Labs.

*Curated from [Microsoft Learn](https://learn.microsoft.com/en-us/fabric/data-science/semantic-model-best-practices) · Updated 2026-01-21*
