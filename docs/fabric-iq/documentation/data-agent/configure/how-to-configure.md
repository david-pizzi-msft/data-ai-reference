# How to configure a data agent

Tuning a data agent is an **ongoing, iterative process** — experiment, observe, refine. Treat it as an evolving system improved through regular testing and feedback, not a one-time setup.

[Official docs](https://learn.microsoft.com/en-us/fabric/data-science/develop-iterative-process-data-agent)

## The iterative loop

1. **Start with a benchmark set** — a table of *question · expected query · expected answer* to guide configuration and measure performance. Expand it over time to cover more question types. (See [Evaluate](../evaluate.md).)
2. **Diagnose incorrect responses** — for each failure ask: missing instruction? vague/misleading instructions? inaccurate example query? ambiguous question vs schema naming? inconsistently formatted values (`ca` / `CA` / `Ca`)?
3. **Improve agent instructions** — clarify source usage and priority, define expected response behaviour (tone, structure, detail), guide reasoning steps, and explain terminology.
4. **Improve data-source instructions** — clarify filter usage, add typical value examples and formats, reinforce consistency, and update as schema/business rules evolve.
5. **Use targeted example queries** — demonstrate join logic, correct filter patterns, expected output columns; split overly broad examples; keep them aligned with current schema.
6. **Address join issues** — document join relationships and keys, include join examples, clarify required columns across tables, and flatten to a denormalized table when joins are too complex.

!!! tip
    Most failures trace back to one of: missing/unclear instructions, unrepresentative examples, ambiguous schema naming, or inconsistent value formatting. Fix the root cause rather than over-instructing.

*Curated from [Microsoft Learn](https://learn.microsoft.com/en-us/fabric/data-science/develop-iterative-process-data-agent) · Updated 2025-06-12*
