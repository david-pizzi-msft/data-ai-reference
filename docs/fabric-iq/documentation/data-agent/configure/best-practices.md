# Best practices for configuring

Practical tips for configuring a data agent so it returns accurate, relevant answers — covering data readiness, scope, instructions, and example queries.

[Official docs](https://learn.microsoft.com/en-us/fabric/data-science/data-agent-configuration-best-practices)

## Data & scope

1. **Get your data AI-ready** — use clear, descriptive table/column names (`CustomerOrders`, `order_submission_date`) instead of `Table1`, `col1`, `flag`.
2. **Create specialized agents** per domain rather than one broad general-purpose agent.
3. **Minimize source scope** — include only the sources, tables, and columns needed. Aim for **≤ 25 tables** per source.

## Writing instructions

4. **Be specific about what *to* do**, not just what to avoid.
5. **Define business terms, abbreviations, synonyms** — agent-level for cross-source terms (e.g. "quarter"), data-source-level for source-specific meanings (e.g. "sales").
6. **Use leading words** — embed SQL/DAX/KQL fragments (e.g. `LIKE '%bike%'`) to nudge query generation.
7. **Keep instructions clear and focused** — concise scope, correct source, clear fallback, defined tone.
8. **Write detailed agent instructions** — role, behaviour, tone, source routing, fallback when data is missing.
9. **Provide detailed data-source instructions** — purpose, target questions, required columns, join logic, typical value formats (e.g. `State` = `"CA"` not `"California"`). The agent can't see row values before querying.

## Example queries

10. **Use example queries for complex logic** — joins, filters, aggregations, date handling. For each question the agent runs a **vector similarity search** and passes the top 3 examples into the prompt. Examples needn't match questions verbatim — they demonstrate intent and structure.

!!! tip "Self-check"
    Ask: could someone unfamiliar with these sources understand which to use and how, from the instructions alone? If not, add the missing context.

*Curated from [Microsoft Learn](https://learn.microsoft.com/en-us/fabric/data-science/data-agent-configuration-best-practices) · Updated 2025-08-15*
