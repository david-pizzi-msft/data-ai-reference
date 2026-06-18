# Data agent configurations

The configurations you add give the data agent **business context** so it generates accurate queries (SQL, DAX, KQL) and routes questions to the right source.

[Official docs](https://learn.microsoft.com/en-us/fabric/data-science/data-agent-configurations)

## Agent instructions

Agent-level instructions guide overall behaviour — which sources to prioritise, how to handle query types, and shared terminology. Recommended structure:

```md
## Objective
// Overall goal, e.g. "Analyze retail sales and customer behavior across regions."

## Data sources
// Which sources to use, in priority order.

## Key terminology
// Define terms/acronyms, e.g. "'GMV' = Gross Merchandise Value."

## Response guidelines
// How answers should be formatted.

## Handling common topics
// Special rules for frequent topics.
```

!!! warning "Semantic models are different"
    Agent instructions are **not** passed to the DAX generation tool. For semantic models, configure everything in **Prep for AI** instead (see [Semantic model best practices](semantic-model-best-practices.md)).

## Data source instructions

Applied when a question is routed to a specific source — provide tables, columns, relationships, and query logic:

```md
## General knowledge
## Table descriptions
## When asked about
// e.g. "When asked about shoe sales, always use the SalesProduct table."
```

## Data source description

A high-level summary of what a source contains and the questions it answers — the agent uses it (alongside schema and example queries) to **route** questions to the right source.

## Example queries

Few-shot question → query pairs that the agent references when forming responses. The top relevant examples are injected into generation. See [Example queries](example-queries.md).

*Curated from [Microsoft Learn](https://learn.microsoft.com/en-us/fabric/data-science/data-agent-configurations) · Updated 2025-12-02*
