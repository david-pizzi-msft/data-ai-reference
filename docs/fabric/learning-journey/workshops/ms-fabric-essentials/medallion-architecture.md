# 1 · Medallion Architecture

!!! info "Source"
    [AzurePortal/1_MedallionArch](https://github.com/Cloud2BR-MSFTLearningHub/MS-Fabric-Essentials-Workshop/tree/main/AzurePortal/1_MedallionArch)

**Status:** 🟡 In progress

## What this lab does

Builds an end-to-end medallion pipeline in Microsoft Fabric — raw data lands in **Bronze**, gets cleaned in **Silver**, and is curated/aggregated in **Gold**, then surfaced to Power BI for reporting. Data moves between layers with notebooks (PySpark) and is orchestrated with Data Factory pipelines.

The three refinement layers:

| Layer | Lakehouse | Purpose |
| --- | --- | --- |
| 🥉 Bronze | `raw_Bronze` | Raw, append-only landing zone for ingested data. |
| 🥈 Silver | `cleansed_Silver` | Cleaned, transformed, enriched, quality-checked data. |
| 🥇 Gold | `curated_Gold` | Curated, aggregated data optimized for BI/reporting. |

## Flow

![Medallion architecture in Microsoft Fabric — SQL DB and Azure Data Lake feed Bronze via Data Pipelines/Data Factory, then Dataflows/Notebooks and Data Factory move data Bronze → Silver → Gold, with a Shortcut into a Lakehouse in OneLake, Z-Order/V-Order optimization, and a Power BI report in Direct Lake mode (with Copilot)](../images/medallion-architecture.png)

Simplified view:

```mermaid
flowchart LR
    SQL[(SQL DB)] -->|Data pipelines| B
    ADLS[(Azure Data Lake)] -->|Data Factory| B
    subgraph WS[Fabric Workspace]
        direction LR
        B[🥉 Bronze<br/>raw] -->|Dataflows /<br/>Notebooks| SL[🥈 Silver<br/>cleaned]
        SL -->|Data Factory| G[🥇 Gold<br/>curated]
    end
    G -->|Shortcut| LH[(Lakehouse<br/>in OneLake)]
    G --> OPT[Z-Order → V-Order]
    OPT --> PBI[📊 Power BI report<br/>Direct Lake mode]
    CP([Copilot]) -.-> PBI
```

## Ingesting into Bronze (Step 2)

Step 2 shows **several ways** to land data in Bronze — you only need **one**. Azure SQL is **not** required.

| Source | How | Needs Azure SQL? |
| --- | --- | --- |
| **CSV / files** | Upload to `raw_Bronze` → **Load to Tables** | ❌ |
| **SQL — Data pipeline** | Data Factory **Copy activity** into Bronze (batch/scheduled) | ✅ (source is SQL) |
| **SQL — Mirroring** | Continuously **synced replica** of the SQL DB in Fabric (near real-time, no pipeline authoring) | ✅ (source is SQL) |

- **Pipeline vs mirroring** are *alternatives* for a SQL source — pick one. Pipeline = you control a copy step; mirroring = auto-synced copy.
- The provided sample datasets are **different**: the CSVs are `2020orders.csv` + `products.csv` (a sales scenario); the SQL script creates a separate `dbo.Employees` table (an HR scenario).

!!! tip "Recommended path for this lab"
    Use the **CSV path**. The sample notebooks ([bronze→silver](https://github.com/Cloud2BR-MSFTLearningHub/MS-Fabric-Essentials-Workshop/blob/main/AzurePortal/1_MedallionArch/src/0_notebook_bronze_to_silver.ipynb), [silver→gold](https://github.com/Cloud2BR-MSFTLearningHub/MS-Fabric-Essentials-Workshop/blob/main/AzurePortal/1_MedallionArch/src/1_notebook_silver_to_gold.ipynb)) run against the `2020orders` and `products` tables end-to-end — the SQL/`Employees` path is only an alternative ingestion illustration and isn't used in Steps 3–6. Just fix the `abfss://` lakehouse paths to match your workspace.

## Bronze → Silver notebook (Step 3)

Create a notebook, then **attach both lakehouses** in the Explorer pane: add **`raw_Bronze`** (keep it as the **default** — the 📌 pin) and **`cleansed_Silver`**. With both attached you can skip the `abfss://` URLs entirely — read from the default lakehouse with relative `Tables/…` paths and write to Silver with `saveAsTable("cleansed_Silver.<table>")`.

Run each cell in order.

=== "1 · Imports"

    ```python
    from pyspark.sql.types import *
    import pyspark.sql.functions
    from pyspark.sql import *
    ```

=== "2 · Read orders (Bronze)"

    ```python
    # Read the data from the bronze layer:
    df_raw_2020orders = spark.read.format("delta").load("Tables/2020orders")

    df_raw_2020orders.head(2)
    ```

=== "3 · Clean orders"

    ```python
    # Clean the data (filter out rows with null values in the 'Date' column):
    df_cleaned = df_raw_2020orders.filter(df_raw_2020orders["Date"].isNotNull())
    print(df_cleaned)
    ```

=== "4 · Write orders (Silver)"

    ```python
    # Save the cleaned data to the "cleansed_Silver" table in the Silver lakehouse:
    df_cleaned.write.format("delta").mode("overwrite").saveAsTable("cleansed_Silver.2020orders_silver")
    ```

=== "5 · Products (read → pass-through → write)"

    ```python
    # Read data from the Bronze layer
    bronze_df = spark.read.format("delta").load("Tables/products")
    # Perform transformations (if any)
    silver_df = bronze_df  # Assuming no transformations for simplicity
    # Write data to the Silver layer
    silver_df.write.mode("overwrite").format("delta").saveAsTable("cleansed_Silver.products_silver")
    ```

!!! warning "Two changes vs. the sample notebook"
    The sample uses hard-coded `abfss://…` paths from the author's environment. Here:

    - `.load("abfss://…/raw_Bronze.Lakehouse/Tables/2020orders")` → `.load("Tables/2020orders")` — resolves to your **default** lakehouse (`raw_Bronze`).
    - `.save("abfss://…/cleansed_test_Silver.Lakehouse/Tables/…")` → `.saveAsTable("cleansed_Silver.…")` — relative `Tables/…` paths only point to the *default* lakehouse, so writing to a **different** attached lakehouse uses `saveAsTable("<lakehouse>.<table>")`.

!!! success "Expected result"
    All cells run without error, and the **`cleansed_Silver`** lakehouse gains two tables under **Tables** (refresh the Explorer if needed):

    - `2020orders_silver` — columns `ID`, `Count`, `Date`, `Name`, `Style`, `price`, `tax`; rows like `SO45376`.
    - `products_silver` — pass-through copy of the products data.

    A *"SQL analytics endpoint was created"* banner on the lakehouse is normal.

## Silver → Gold notebook (Step 4)

Create a second notebook and attach **`cleansed_Silver`** (set as **default** 📌) and **`curated_Gold`**. This reads the Silver tables, aggregates the orders, and writes curated tables into `curated_Gold`.

Run each cell in order.

=== "1 · Imports"

    ```python
    from pyspark.sql.types import *
    import pyspark.sql.functions
    from pyspark.sql import *
    from pyspark.sql.functions import sum
    ```

=== "2 · Read orders (Silver)"

    ```python
    # Read the data from the silver layer:
    df_cleansed_2020orders = spark.read.format("delta").load("Tables/2020orders_silver")
    df_cleansed_2020orders.head(2)
    ```

=== "3 · Cast tax → int"

    ```python
    # Cast the 'tax' column from double to int:
    df_cleansed_2020orders = df_cleansed_2020orders.withColumn("tax", df_cleansed_2020orders["tax"].cast("int"))  # type to int
    df_cleansed_2020orders.printSchema()
    ```

=== "4 · Aggregate"

    ```python
    # Group and aggregate the data:
    df_aggregated = df_cleansed_2020orders.groupBy("Style").agg(sum("price").alias("total_price_vehicles"))
    df_aggregated.show(10, truncate=False)
    ```

=== "5 · Write orders (Gold)"

    ```python
    # Save the aggregated data to the "curated_Gold" table in the Gold lakehouse:
    df_aggregated.write.format("delta").mode("overwrite").saveAsTable("curated_Gold.2020orders_gold")
    ```

=== "6 · Products (read → pass-through → write)"

    ```python
    # Read data from the Silver layer
    silver_df = spark.read.format("delta").load("Tables/products_silver")
    # Perform transformations (if any)
    silver_df = silver_df  # Assuming no transformations for simplicity
    # Write data to the Gold layer
    silver_df.write.mode("overwrite").format("delta").saveAsTable("curated_Gold.products_gold")
    ```

!!! note "Path & naming changes vs. the sample"
    - `abfss://…` load/save paths → relative `Tables/…` reads (default = `cleansed_Silver`) and `saveAsTable("curated_Gold.…")` writes, same as Step 3.
    - The sample writes the products table into Gold as `products_silver`; here it's renamed `products_gold` for clarity.

!!! success "Expected result"
    All cells run without error. Cell 4's `show()` prints an aggregated table (one row per `Style` with a `total_price_vehicles` total), and the **`curated_Gold`** lakehouse gains two tables under **Tables**:

    - `2020orders_gold` — aggregated: `Style`, `total_price_vehicles`.
    - `products_gold` — pass-through copy of the products data.

## Orchestration pipeline (Step 5)

!!! question "Notebook or pipeline?"
    Step 5 is a **pipeline** — *not* a notebook. You don't write new PySpark here. You build a **Data Factory pipeline** that *runs* the two notebooks from Steps 3–4 in order and on a schedule. The notebooks stay unchanged; the pipeline just orchestrates them.

Your transformation logic (cleaning, casting, aggregating) lives in the **notebooks**. A pipeline **Notebook activity** runs a whole notebook, so chaining two of them reproduces Bronze → Silver → Gold automatically.

!!! tip "Naming"
    Name the pipeline **`bronze_to_gold`** — it follows the same `x_to_y` pattern as the `bronze_to_silver` and `silver_to_gold` notebooks and reads as the end-to-end flow they combine into.

1. In your workspace, select **+ New item** (or **New → Data pipeline**), choose **Data pipeline**, name it **`bronze_to_gold`**, and select **Create**.
2. In the pipeline canvas, select **Add pipeline activity → Notebook** (or drag **Notebook** from the **Activities** ribbon). On the **Settings** tab, set **Notebook** = **`bronze_to_silver`**. Give the activity a clear name (e.g. *Run bronze_to_silver*) on the **General** tab.
3. Add a second **Notebook activity** the same way, with **Notebook** = **`silver_to_gold`** (e.g. name it *Run silver_to_gold*).
4. Drag the first activity's **On success** (green ✓) connector into the second, so Silver→Gold only runs after Bronze→Silver succeeds.
5. Select **Run** to test it once, then **Schedule** (top ribbon) → turn **On**, set the recurrence (e.g. daily) to match how often your source data changes, and **Apply**. Use **Save** to persist the pipeline.

```mermaid
flowchart LR
    T([⏰ Schedule trigger]) --> N1[Notebook activity<br/>bronze_to_silver]
    N1 -->|On success| N2[Notebook activity<br/>silver_to_gold]
```

!!! warning "\"Copy activity\" in the workshop text"
    The README says to add a **Copy activity** between layers. A Copy activity only *moves data as-is* — it won't apply your cleaning/aggregation. Use it for **ingestion** into Bronze (e.g. from SQL or ADLS) or pure pass-through; use a **Notebook activity** for the Silver and Gold stages that need your PySpark logic.

## Enable data access for reporting (Step 6)

Surface the Gold data to Power BI. This step creates a **semantic model** over `curated_Gold`, then a report in **Direct Lake** mode (no data copy — Power BI reads the Delta tables directly).

1. **Confirm the SQL analytics endpoint.** Fabric auto-creates one with the `curated_Gold` lakehouse (you saw the *"SQL analytics endpoint was created"* banner). From the workspace list, check the **SQL analytics endpoint** item for `curated_Gold` exists — it's what makes Gold queryable/reportable.
2. **Create a semantic model.** Open the `curated_Gold` lakehouse → **New semantic model**. Name it **`gold_semantic_model`**, then select the tables to include (`2020orders_gold`, `products_gold`) and **Confirm**.
3. **Build a Power BI report (Direct Lake).** From the semantic model, select **Create report** (an empty report) or **Auto-create report** to let Copilot draft one. Save it as **`gold_sales_report`**.
4. Reports built on the semantic model read Gold in **Direct Lake** mode — fast queries with no import/refresh. You can also use **Copilot** to add or refine visuals.

!!! tip "Names (matching the lab convention)"
    | Item | Name |
    | --- | --- |
    | Semantic model | `gold_semantic_model` |
    | Power BI report | `gold_sales_report` |

!!! info "Copilot / auto-create requirements"
    **Auto-create report** and Copilot need **AI features enabled** in the tenant (Fabric admin setting). Without them, build the report manually — Direct Lake still works.

!!! success "Expected result"
    You have a `gold_semantic_model` over the Gold tables and a `gold_sales_report` that visualizes the curated data (e.g. `total_price_vehicles` by `Style`) — the full medallion flow now runs on a schedule and surfaces in Power BI.

## Things to remember

- Data written between layers using `write.format("delta")`; Silver→Gold aggregations use `groupBy()` / `agg()`.
- Fabric can auto-create the medallion flow for you.
- The **Gold** layer needs a **SQL Analytics Endpoint** to be reportable.
- Power BI reads Gold in **Direct Lake** mode; `auto-create report` / Copilot needs AI features enabled in the tenant.
- Alternative to pipelines for SQL sources: **SQL mirroring** (keeps a synced copy in Fabric).
- Requires an Azure subscription.

## Notes

- **Medallion architecture** is a data design pattern for lakehouses that organizes data into progressively refined layers (Bronze → Silver → Gold). It's a best practice for managing the data lifecycle and data quality.
- Each layer lives in its own lakehouse: `raw_Bronze`, `cleansed_Silver`, `curated_Gold`.
- Movement between layers is done in notebooks (PySpark, Delta format) and/or orchestrated with Data Factory pipelines that can be scheduled with triggers.
- Reporting: create a **semantic model** on Gold, then build Power BI reports in **Direct Lake** mode (optionally via Copilot `auto-create report`).

## Key takeaways

Why the medallion architecture is worth it:

- **Data quality** — layered structure lets you apply quality checks and transformations in stages, so Gold is reliable and analysis-ready.
- **Scalability** — each layer's pipelines scale independently, giving flexibility and efficiency.
- **Performance** — the Gold layer is optimized (incl. V-Order), so reporting/analytics queries run faster.
- **Simplicity** — the pipeline is broken into smaller, purposeful steps.
- **Auditability** — clear data lineage makes it easy to trace data origin and the transformations applied at each stage.
