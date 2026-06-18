# Example queries

Example queries (**few-shot examples**) give the agent concrete question → query patterns to learn from. When a user asks a question, the agent retrieves the most relevant examples (typically the top four) and feeds them into generation for more accurate, consistent results.

[Official docs](https://learn.microsoft.com/en-us/fabric/data-science/data-agent-example-queries)

## Providing examples

Each example needs a **natural-language question** and its **query**. Every example is validated against the source schema — queries that fail validation aren't sent to the agent.

| Data source | Supports example queries? |
| --- | --- |
| Lakehouse | ✅ Yes |
| Warehouse | ✅ Yes |
| Eventhouse / KQL database | ✅ Yes |
| Semantic model | ❌ No |
| Ontology | ❌ No |

Use the **run steps** view to debug which examples were retrieved for a question.

## Best practices

- Make questions map clearly to the query; avoid ambiguity.
- Add comments (`-- substitute customer_id here`) to guide substitution/logic.
- Show join logic and complex patterns hard to express in prose.
- Keep examples distinct — avoid overlap or contradictions.
- Reflect real user behaviour.

## Validate with the SDK

`evaluate_few_shots` validates each pair and returns a success rate plus pass/fail cases:

```python
result = datasource.evaluate_few_shots(batch_size=20)
print(f"Success rate: {result.success_rate:.2f}% "
      f"({result.success_count}/{result.total_examples})")
```

Each example is scored on **Clarity**, **Relatedness**, and **Mapping** — high quality requires all three positive. The SDK also runs **conflict detection** (same intent → different tables/aggregation/results) with confidence ratings.

!!! note "SQL only"
    The validation utility currently supports **SQL-based** example queries only; KQL and other types aren't yet supported.

*Curated from [Microsoft Learn](https://learn.microsoft.com/en-us/fabric/data-science/data-agent-example-queries) · Updated 2025-09-11*
