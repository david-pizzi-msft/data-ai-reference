# Integrations

Fabric IQ surfaces your governed business data in the tools people already use. The first integration brings it into Microsoft 365.

## Fabric IQ in Microsoft 365 Copilot Cowork (Frontier) (preview)

The **Fabric IQ plugin** connects [Microsoft 365 Copilot Cowork (Frontier)](https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/cowork-available-plugins) to your Fabric and Power BI data. A Power BI report stops being the end of a workflow and becomes the **starting point** — you ground a Cowork chat in trusted data, then chain it into other Cowork skills (drafting emails, creating documents, scheduling reviews) without leaving the conversation.

The plugin is installed by default for Frontier customers.

!!! note "Preview"
    This feature is in preview. Capabilities and limitations are expected to change.

### What you can do

- Ground a Cowork chat in a specific Power BI report and ask questions about its data.
- Reference a report you have access to and ask Cowork to summarise it, compare values, or explain a trend.
- Chain a data answer into other skills — draft an email, create a document, or schedule a follow-up — in the same chat.

Under the covers, Cowork queries Power BI semantic models and reports **as you**, so item permissions and row-level security (RLS) still apply.

### Grounding a chat in Power BI data

| Scenario | How to use it |
| --- | --- |
| **Attach** a report | Use the **+** (attach) control in the Cowork composer to attach a Power BI report, then ask a data question. |
| **Paste** a report link | Paste the report URL into the composer and ask a question; Cowork grounds on the linked report. |
| **Reference** a report by name | Mention the report by name; Cowork searches artifacts you can access and grounds on the best match. |

### Chaining with other Cowork skills

The real value shows when you combine a data answer with another skill in the same chat — for example:

- *"Using this report, identify significant changes in the last week and email my manager a short summary with next steps."*
- *"Create a recurring Friday summary of this report and send it to the exec staff."*
- *"If any KPI is trending down, create an agenda and schedule a review meeting with stakeholders."*

Each step runs with your existing Microsoft 365 and Fabric permissions.

### Current limitations

- Grounds on **Power BI reports and their semantic models only** — not dashboards, paginated (RDL) reports, reports inside an app, share links, semantic models referenced by name, or other Fabric items (lakehouses, eventhouses, ontologies, data agents).
- **No source citations** in answers today — open the source report to confirm a value before acting on it.
- Sensitivity labels aren't surfaced in the Cowork UI (they still apply at the Power BI layer).

### Prerequisites

- **User** — enrolled in the [Microsoft 365 Copilot Frontier program](https://adoption.microsoft.com/copilot/frontier-program/), a Copilot Premium licence, and at least **Read** on the reports/semantic models.
- **Tenant** — a Fabric/Power BI admin must enable *Share Fabric data with your Microsoft 365 services* (plus the cross-region toggle if tenants are in different regions) and *Users can use the Power BI Model Context Protocol server endpoint (preview)*.

No extra Fabric capacity, F SKU, or PPU licence is required beyond what your Power BI content already needs.

*Curated from [Microsoft Learn](https://learn.microsoft.com/en-us/fabric/iq/connectors/cowork-overview) · Updated 2026-05-08*
