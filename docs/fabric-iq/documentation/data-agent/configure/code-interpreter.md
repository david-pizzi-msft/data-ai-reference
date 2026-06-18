# Code interpreter

The **code interpreter** tool gives a data agent a secure, sandboxed **Python** environment to analyse the data it retrieves — so it can go beyond querying to run calculations, detect correlations, and generate visualizations.

[Official docs](https://learn.microsoft.com/en-us/fabric/data-science/data-agent-code-interpreter)

!!! info "Preview"
    The code interpreter tool is in preview.

## Add the tool

1. Open the data agent → **Tools** tab.
2. Select **Add code interpreter** → **Confirm**.

The tool is then ready to use.

## How it works

Ask questions in natural language — the agent queries connected sources, passes results to the code interpreter, and uses Python to analyse them. No code required. Examples:

- *Generate a heatmap of claim frequency by region and cause of loss over five years.*
- *Build a correlation heatmap across supplier performance metrics.*
- *Forecast next quarter's revenue from the past three years of sales data.*

## Inspect & guide

- Expand the **code interpreter run step** to see the generated Python, its inputs, and outputs — useful for validation and troubleshooting.
- You can't instruct the tool directly, but **agent-level instructions** can shape when the agent calls it, what context to include, and how to format results.

*Curated from [Microsoft Learn](https://learn.microsoft.com/en-us/fabric/data-science/data-agent-code-interpreter) · Updated 2026-05-26*
