# 📘 data-ai-reference

> **Personal knowledge base & quick-reference site for Microsoft Fabric, Fabric IQ, and Agentic AI.**
>
> Built to be pulled up during customer calls — concise, scannable, and always up to date.

[![GitHub Pages](https://img.shields.io/badge/docs-GitHub%20Pages-blue?logo=github)](https://david-pizzi-msft.github.io/data-ai-reference/)
[![MkDocs Material](https://img.shields.io/badge/built%20with-MkDocs%20Material-526CFE?logo=materialformkdocs&logoColor=white)](https://squidfunk.github.io/mkdocs-material/)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

---

## 📑 Table of Contents

- [Microsoft Fabric](#-microsoft-fabric)
- [Fabric IQ](#-fabric-iq)
- [Agentic AI](#-agentic-ai)
- [Getting Started](#-getting-started)
- [Tech Stack](#-tech-stack)
- [License](#-license)

---

## 🔷 Microsoft Fabric

### DP-600: Implement Analytics Solutions Using Microsoft Fabric

> **Level:** Advanced · **Duration:** 4 days · **Certification:** Fabric Analytics Engineer Associate

The [DP-600T00 course](https://learn.microsoft.com/en-gb/training/courses/dp-600t00) covers preparing, enriching, and serving data for analysis across lakehouses, warehouses, and eventhouses in Microsoft Fabric.

| # | Learning Path | Focus |
|---|---|---|
| 1 | Explore analytics data stores in Microsoft Fabric | Lakehouses, warehouses, eventhouses, SQL analytics endpoints |
| 2 | Design and transform analytics data in Microsoft Fabric | Dataflows, notebooks, T-SQL, data transformation patterns |
| 3 | Design and manage semantic models in Microsoft Fabric | Dimensional modelling, DAX, semantic model optimisation |
| 4 | Prepare AI-ready analytics data in Microsoft Fabric | Data prep for AI agents and Copilot experiences |
| 5 | Secure and govern analytics data in Microsoft Fabric | RLS, workspace security, governance, lifecycle management |

### Foundational Documentation

- 📖 [What is Microsoft Fabric?](https://learn.microsoft.com/en-us/fabric/fundamentals/microsoft-fabric-overview) — Unified SaaS analytics platform covering ingestion, transformation, storage, real-time processing, data science, and BI.
- 📖 [Fabric fundamentals documentation](https://learn.microsoft.com/en-us/fabric/fundamentals/) — Getting started, workspaces, Copilot, task flows, and OneLake catalog.
- 📖 [Fabric terminology](https://learn.microsoft.com/en-us/fabric/fundamentals/fabric-terminology) — Definitions for capacity, items, workloads, and all Fabric experiences.

---

## 🧠 Fabric IQ

### Get Started with Fabric IQ (MS Learn)

> **Level:** Beginner · **Duration:** ~5 hours · **Modules:** 4

The [Get Started with Fabric IQ](https://learn.microsoft.com/en-us/training/paths/get-started-fabric-iq/) learning path covers:

| # | Module | Duration | Key Topics |
|---|---|---|---|
| 1 | Understand Microsoft Fabric IQ fundamentals | 37 min | What is IQ, ontology modelling vs traditional modelling |
| 2 | Create an ontology with Fabric IQ | 2 hr 23 min | Entity types, properties, relationships, data bindings |
| 3 | Visualise ontology data with Microsoft Fabric IQ | 46 min | Entity instances, relationship graph, Query builder |
| 4 | Build a Fabric data agent with an ontology | 1 hr 5 min | Data agents, agent instructions, NL queries, publishing |

### Fabric IQ Documentation

- 📖 [Fabric IQ documentation hub](https://learn.microsoft.com/en-us/fabric/iq/) — Central landing page for all IQ content.
- 📖 [What is Fabric IQ (preview)?](https://learn.microsoft.com/en-us/fabric/iq/overview) — Overview of the IQ workload, items, and how they fit together.

**Core IQ Components:**

| Component | Description |
|---|---|
| **Ontology** (preview) | Enterprise vocabulary — entity types, relationships, properties, rules, bound to real data |
| **Graph** (preview) | Native graph storage & compute for relationship-heavy queries (GQL) |
| **Data Agent** (preview) | Conversational Q&A grounded in ontology — NL to governed data answers |
| **Operations Agent** (preview) | Monitors real-time data, detects anomalies, recommends/triggers actions |
| **Plan** (preview) | No-code collaborative planning, reporting, and analytics |
| **Power BI Semantic Model** | Curated analytics model — measures, hierarchies, DAX, visuals |

---

## 🤖 Agentic AI

### CE&S Power Up Programme

> **Duration:** 8 weeks (4–6 hrs/week) · **Platform:** [aka.ms/powerupcens](https://aka.ms/powerupcens)
>
> Hands-on learning experience focused on building AI agents with Copilot Studio for real CE&S business scenarios. Earn Credly badges on completion.

#### Level 1 — Foundations

`🔲 Placeholder — notes to be added after completing L1`

- Introduction to Copilot Studio
- Understanding AI agents and their capabilities
- First agent creation walkthrough

#### Level 2 — Builder

`🔲 Placeholder — notes to be added after completing L2`

- Designing agents for real business workflows
- L2 Challenge completion
- Copilot Studio Maker track deep dive

#### Level 3 — Advanced

`🔲 Placeholder — notes to be added after completing L3`

- Complex multi-step agent orchestration
- Integration with enterprise data sources
- Production deployment patterns

---

## 🚀 Getting Started

### Browse the site

Once deployed, visit: **[https://david-pizzi-msft.github.io/data-ai-reference/](https://david-pizzi-msft.github.io/data-ai-reference/)**

### Run locally

```bash
# Clone the repo
git clone https://github.com/david-pizzi-msft/data-ai-reference.git
cd data-ai-reference

# Install dependencies
pip install -r requirements.txt

# Serve locally (hot reload at http://127.0.0.1:8000)
mkdocs serve
```

### Add new content

1. Create/edit a `.md` file under the relevant `docs/` subfolder
2. Update `mkdocs.yml` nav if adding a new page
3. Commit, push → GitHub Actions auto-deploys to Pages

---

## 🛠️ Tech Stack

| Tool | Purpose |
|---|---|
| [MkDocs Material](https://squidfunk.github.io/mkdocs-material/) | Static site generator with search, dark mode, admonitions |
| [GitHub Pages](https://pages.github.com/) | Free hosting directly from the repo |
| [GitHub Actions](https://github.com/features/actions) | CI/CD — auto-deploy on push to `main` |
| Markdown | All content authored in plain Markdown |

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

> _Built by [David Pizzi](https://github.com/david-pizzi-msft) — Cloud Solution Architect @ Microsoft_