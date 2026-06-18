# Evaluate a data agent

Use the Fabric SDK to **programmatically test** how well a data agent answers natural-language questions — define ground-truth examples, run evaluations, and analyse results, all inside a notebook.

[Official docs](https://learn.microsoft.com/en-us/fabric/data-science/evaluate-data-agent)

!!! info "Preview"
    Evaluation with the Fabric SDK is in preview.

## Workflow

1. **Install the SDK** — `%pip install -U fabric-data-agent-sdk`.
2. **Load a ground-truth dataset** — sample questions plus expected answers, as a pandas DataFrame or a CSV with `question` and `expected_answer` columns.
3. **Run the evaluation** — `evaluate_data_agent(...)` compares responses against expected answers and writes metrics to output tables.
4. **Review results** — summary and detail helpers.

```python
from fabric.dataagent.evaluation import evaluate_data_agent

evaluation_id = evaluate_data_agent(
    df,
    data_agent_name="AgentEvaluation",
    table_name="demo_evaluation_output",
    data_agent_stage="production",   # or "sandbox"
)
```

## Inspect results

| Function | Returns |
| --- | --- |
| `get_evaluation_summary(table_name)` | High-level metrics — total questions, counts of true / false / unclear, accuracy. |
| `get_evaluation_details(evaluation_id, table_name)` | Row-level results — question, expected vs actual answer, result, and a thread link (visible only to the runner). |

## Customize the judge

Pass a `critic_prompt` to `evaluate_data_agent` for domain-specific scoring. The prompt must include the `{query}`, `{expected_answer}`, and `{actual_answer}` placeholders — useful when answers are semantically equivalent but differ in format.

!!! tip "Diagnostics button"
    Export a full snapshot of the agent's configuration and execution steps to debug behaviour or share with Microsoft Support.

*Curated from [Microsoft Learn](https://learn.microsoft.com/en-us/fabric/data-science/evaluate-data-agent) · Updated 2025-05-06*
