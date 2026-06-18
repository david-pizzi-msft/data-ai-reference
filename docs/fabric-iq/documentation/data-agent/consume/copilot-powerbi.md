# Copilot in Power BI

Consume a data agent directly within **Copilot in Power BI** — ask natural-language questions while viewing reports and get answers from items you can access across Fabric. Works from the Copilot pane or the standalone Copilot experience (no visual is added to the report canvas).

[Official docs](https://learn.microsoft.com/en-us/fabric/data-science/data-agent-copilot-powerbi)

!!! info "Preview"
    This integration is in preview.

## Prerequisites

- General [Copilot requirements](https://learn.microsoft.com/power-bi/create-reports/copilot-introduction#copilot-requirements).
- Open the Copilot pane in a report, or use the standalone Copilot experience.

## Two ways to invoke

- **Copilot search** — Copilot scans items you can access (semantic models, reports, data agents), ranks them, and suggests the most relevant source for your question.
- **Directly add an agent** — *Add items for better results* → **Data agents** → pick from the OneLake catalog. Copilot then uses that agent for follow-up questions.

!!! tip
    When you change topics, tell Copilot so it re-searches across semantic models, reports, and data agents.

## Interaction flow

1. Copilot may **rephrase** the question for clarity.
2. It **sends** the query to the selected data agent.
3. The agent picks the most relevant source and queries it — **RLS/CLS** enforced per user permissions.
4. The agent returns the answer.
5. Copilot presents it in the conversation.

*Curated from [Microsoft Learn](https://learn.microsoft.com/en-us/fabric/data-science/data-agent-copilot-powerbi) · Updated 2026-02-02*
