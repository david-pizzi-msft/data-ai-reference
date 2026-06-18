# Get visual responses

A data agent can return **interactive charts** alongside text and tables — helping you spot trends, patterns, and outliers without leaving the conversation.

[Official docs](https://learn.microsoft.com/en-us/fabric/data-science/data-agent-visuals)

!!! info "Preview"
    Visual responses are in preview and enabled by default.

## How visuals are generated

The agent produces a visual when you **explicitly** ask ("create a bar chart of sales by region"), **implicitly** ask ("show me sales by region"), or when it **infers** one would help ("what are the sales trends over the past year?"). Specify a type to force it — e.g. "as a line chart".

## Supported types & sources

Works across all supported data sources (lakehouse, warehouse, semantic model, …). Supported charts:

- Line / multi-line, column / multi-column / stacked column
- Pie, scatter, area / stacked area

## Customize & limits

- Use **agent instructions** to always/never include visuals or prefer certain chart types.
- Colors, fonts, titles, and labels are **preset** — not customizable.
- Visuals chart up to **200 rows** (extra rows are truncated).
- Only available in the **Fabric data agent experience** — not via SDK, M365 Copilot, Teams, or Foundry. (In M365 Copilot, use the code interpreter to generate visuals from returned results.)

*Curated from [Microsoft Learn](https://learn.microsoft.com/en-us/fabric/data-science/data-agent-visuals) · Updated 2026-05-08*
