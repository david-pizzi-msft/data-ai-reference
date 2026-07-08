# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "bbfdb079-1edb-4bb9-9888-ea1ae958a6d1",
# META       "default_lakehouse_name": "wwilakehouse",
# META       "default_lakehouse_workspace_id": "292b5ad3-c5c5-454d-bf5d-c36fafdec4af",
# META       "known_lakehouses": [
# META         {
# META           "id": "bbfdb079-1edb-4bb9-9888-ea1ae958a6d1"
# META         }
# META       ]
# META     }
# META   }
# META }

# MARKDOWN ********************

# # Prepare and transform data in the lakehouse (PySpark)
# 
# This is a companion notebook for the [Microsoft Learn tutorial](https://learn.microsoft.com/fabric/data-engineering/tutorial-lakehouse-data-preparation) that follows Path 1 in this notebook.
# 
# This notebook includes two execution paths:
# - Path 1: Lakehouse schemas enabled (`Tables/dbo/...`) — this is the supported path for the tutorial article.
# - Path 2: Lakehouse schemas not enabled (`wwilakehouse....`) — use this alternate path when schemas are not enabled in your environment.

# MARKDOWN ********************

# ## Path 1 - Lakehouse schemas enabled (tutorial-supported path)
# ### Create Delta tables
# Run these cells to create Delta tables from raw data using schema-qualified paths (`Tables/dbo/...`).
# 
# #### Cell 1 - Spark session configuration
# This cell enables two Fabric features that optimize how data is written and read in subsequent cells. V-order optimizes parquet layout for faster reads and better compression. Optimize Write reduces the number of files written and increases individual file size.

# CELL ********************

spark.conf.set("spark.sql.parquet.vorder.enabled", "true")
spark.conf.set("spark.microsoft.delta.optimizeWrite.enabled", "true")
spark.conf.set("spark.microsoft.delta.optimizeWrite.binSize", "1073741824")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# #### Cell 2 - Fact - Sale
# This cell reads raw parquet data from `Files/wwi-raw-data/full/fact_sale_1y_full`, adds date part columns (`Year`, `Quarter`, and `Month`), and writes `fact_sale` as a Delta table partitioned by `Year` and `Quarter`.

# CELL ********************

from pyspark.sql.functions import col, year, month, quarter

df = spark.read.format("parquet").load("Files/wwi-raw-data/full/fact_sale_1y_full")
df = df.withColumn("Year", year(col("InvoiceDateKey")))
df = df.withColumn("Quarter", quarter(col("InvoiceDateKey")))
df = df.withColumn("Month", month(col("InvoiceDateKey")))

df.write.mode("overwrite").format("delta").partitionBy("Year", "Quarter").save("Tables/dbo/fact_sale")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# #### Cell 3 - Dimensions
# This cell reads the five dimension parquet datasets and writes them as Delta tables (`dimension_city`, `dimension_customer`, `dimension_date`, `dimension_employee`, and `dimension_stock_item`) under `Tables/dbo/...`.

# CELL ********************

def load_full_data_from_source(table_name):
    df = spark.read.format("parquet").load('Files/wwi-raw-data/full/' + table_name)
    df = df.drop("Photo")
    df.write.mode("overwrite").option("overwriteSchema", "true").format("delta").save("Tables/dbo/" + table_name)

full_tables = [
    "dimension_city",
    "dimension_customer",
    "dimension_date",
    "dimension_employee",
    "dimension_stock_item",
]

for table in full_tables:
    load_full_data_from_source(table)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# ### Transform data for business aggregates
# Run the transformation cells to create aggregate outputs for reporting in the schema-enabled path.

# MARKDOWN ********************

# #### Cell 4 - Load source tables
# This cell loads the source Delta tables needed for business aggregate transformations.

# CELL ********************

df_fact_sale = spark.read.format("delta").load("Tables/dbo/fact_sale")
df_dimension_date = spark.read.format("delta").load("Tables/dbo/dimension_date")
df_dimension_city = spark.read.format("delta").load("Tables/dbo/dimension_city")
df_dimension_employee = spark.read.format("delta").load("Tables/dbo/dimension_employee")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# #### Cell 5 - Aggregate sale by date and city
# This cell computes monthly sales totals by city and writes the result to `aggregate_sale_by_date_city`.

# CELL ********************

sale_by_date_city = (
    df_fact_sale.alias("sale")
    .join(df_dimension_date.alias("date"), df_fact_sale.InvoiceDateKey == df_dimension_date.Date, "inner")
    .join(df_dimension_city.alias("city"), df_fact_sale.CityKey == df_dimension_city.CityKey, "inner")
    .select("date.Date", "date.CalendarMonthLabel", "date.Day", "date.ShortMonth", "date.CalendarYear", "city.City", "city.StateProvince", "city.SalesTerritory", "sale.TotalExcludingTax", "sale.TaxAmount", "sale.TotalIncludingTax", "sale.Profit")
    .groupBy("date.Date", "date.CalendarMonthLabel", "date.Day", "date.ShortMonth", "date.CalendarYear", "city.City", "city.StateProvince", "city.SalesTerritory")
    .sum("sale.TotalExcludingTax", "sale.TaxAmount", "sale.TotalIncludingTax", "sale.Profit")
    .withColumnRenamed("sum(TotalExcludingTax)", "SumOfTotalExcludingTax")
    .withColumnRenamed("sum(TaxAmount)", "SumOfTaxAmount")
    .withColumnRenamed("sum(TotalIncludingTax)", "SumOfTotalIncludingTax")
    .withColumnRenamed("sum(Profit)", "SumOfProfit")
    .orderBy("date.Date", "city.StateProvince", "city.City")
)

sale_by_date_city.write.mode("overwrite").format("delta").option("overwriteSchema", "true").save("Tables/dbo/aggregate_sale_by_date_city")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# #### Cell 6 - Aggregate sale by date and employee
# This cell computes monthly sales totals by employee and writes the result to `aggregate_sale_by_date_employee`.

# CELL ********************

sale_by_date_employee = (
    df_fact_sale.alias("sale")
    .join(df_dimension_date.alias("date"), df_fact_sale.InvoiceDateKey == df_dimension_date.Date, "inner")
    .join(df_dimension_employee.alias("employee"), df_fact_sale.SalespersonKey == df_dimension_employee.EmployeeKey, "inner")
    .select("date.Date", "date.CalendarMonthLabel", "date.Day", "date.ShortMonth", "date.CalendarYear", "employee.PreferredName", "employee.Employee", "sale.TotalExcludingTax", "sale.TaxAmount", "sale.TotalIncludingTax", "sale.Profit")
    .groupBy("date.Date", "date.CalendarMonthLabel", "date.Day", "date.ShortMonth", "date.CalendarYear", "employee.PreferredName", "employee.Employee")
    .sum("sale.TotalExcludingTax", "sale.TaxAmount", "sale.TotalIncludingTax", "sale.Profit")
    .withColumnRenamed("sum(TotalExcludingTax)", "SumOfTotalExcludingTax")
    .withColumnRenamed("sum(TaxAmount)", "SumOfTaxAmount")
    .withColumnRenamed("sum(TotalIncludingTax)", "SumOfTotalIncludingTax")
    .withColumnRenamed("sum(Profit)", "SumOfProfit")
    .orderBy("date.Date", "employee.PreferredName", "employee.Employee")
)

sale_by_date_employee.write.mode("overwrite").format("delta").option("overwriteSchema", "true").save("Tables/dbo/aggregate_sale_by_date_employee")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# ## Path 2 - Lakehouse schemas not enabled (alternate path)
# ### Create Delta tables
# Run these cells to create Delta tables from raw data using non-schema table names (`wwilakehouse....`).
# 
# #### Cell 1 - Spark session configuration
# This cell enables two Fabric features that optimize how data is written and read in subsequent cells. V-order optimizes parquet layout for faster reads and better compression. Optimize Write reduces the number of files written and increases individual file size.

# CELL ********************

spark.conf.set("spark.sql.parquet.vorder.enabled", "true")
spark.conf.set("spark.microsoft.delta.optimizeWrite.enabled", "true")
spark.conf.set("spark.microsoft.delta.optimizeWrite.binSize", "1073741824")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# #### Cell 2 - Fact - Sale
# This cell reads raw parquet data from `Files/wwi-raw-data/full/fact_sale_1y_full`, adds date part columns (`Year`, `Quarter`, and `Month`), and writes `wwilakehouse.fact_sale` as a Delta table partitioned by `Year` and `Quarter`.

# CELL ********************

from pyspark.sql.functions import col, year, month, quarter

df = spark.read.format("parquet").load("Files/wwi-raw-data/full/fact_sale_1y_full")
df = df.withColumn("Year", year(col("InvoiceDateKey")))
df = df.withColumn("Quarter", quarter(col("InvoiceDateKey")))
df = df.withColumn("Month", month(col("InvoiceDateKey")))

df.write.mode("overwrite").format("delta").partitionBy("Year", "Quarter").saveAsTable("wwilakehouse.fact_sale")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# #### Cell 3 - Dimensions
# This cell reads the five dimension parquet datasets and writes them as Delta tables (`dimension_city`, `dimension_customer`, `dimension_date`, `dimension_employee`, and `dimension_stock_item`) under `wwilakehouse....`.

# CELL ********************

def load_full_data_from_source_no_schema(table_name):
    df = spark.read.format("parquet").load("Files/wwi-raw-data/full/" + table_name)
    if "Photo" in df.columns:
        df = df.drop("Photo")
    df.write.mode("overwrite").format("delta").saveAsTable("wwilakehouse." + table_name)

full_tables = [
    "dimension_city",
    "dimension_customer",
    "dimension_date",
    "dimension_employee",
    "dimension_stock_item",
]

for table in full_tables:
    load_full_data_from_source_no_schema(table)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# ### Transform data for business aggregates
# Run the transformation cells to create aggregate outputs for reporting in the non-schema path.

# MARKDOWN ********************

# #### Cell 4 - Load source tables
# This step prepares the source tables for aggregation in Path 2. For PySpark, this cell explicitly loads the Delta source tables used in the transformation code below.

# CELL ********************

df_fact_sale = spark.read.table("wwilakehouse.fact_sale")
df_dimension_date = spark.read.table("wwilakehouse.dimension_date")
df_dimension_city = spark.read.table("wwilakehouse.dimension_city")
df_dimension_employee = spark.read.table("wwilakehouse.dimension_employee")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# #### Cell 5 - Aggregate sale by date and city
# This cell computes monthly sales totals by city and writes the result to `wwilakehouse.aggregate_sale_by_date_city`.

# CELL ********************

sale_by_date_city = (
    df_fact_sale.alias("sale")
    .join(df_dimension_date.alias("date"), df_fact_sale.InvoiceDateKey == df_dimension_date.Date, "inner")
    .join(df_dimension_city.alias("city"), df_fact_sale.CityKey == df_dimension_city.CityKey, "inner")
    .select("date.Date", "date.CalendarMonthLabel", "date.Day", "date.ShortMonth", "date.CalendarYear", "city.City", "city.StateProvince", "city.SalesTerritory", "sale.TotalExcludingTax", "sale.TaxAmount", "sale.TotalIncludingTax", "sale.Profit")
    .groupBy("date.Date", "date.CalendarMonthLabel", "date.Day", "date.ShortMonth", "date.CalendarYear", "city.City", "city.StateProvince", "city.SalesTerritory")
    .sum("sale.TotalExcludingTax", "sale.TaxAmount", "sale.TotalIncludingTax", "sale.Profit")
    .withColumnRenamed("sum(TotalExcludingTax)", "SumOfTotalExcludingTax")
    .withColumnRenamed("sum(TaxAmount)", "SumOfTaxAmount")
    .withColumnRenamed("sum(TotalIncludingTax)", "SumOfTotalIncludingTax")
    .withColumnRenamed("sum(Profit)", "SumOfProfit")
    .orderBy("date.Date", "city.StateProvince", "city.City")
)

sale_by_date_city.write.mode("overwrite").format("delta").option("overwriteSchema", "true").save("Tables/aggregate_sale_by_date_city")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# #### Cell 6 - Aggregate sale by date and employee
# This cell computes monthly sales totals by employee and writes the result to `wwilakehouse.aggregate_sale_by_date_employee`.

# CELL ********************

sale_by_date_employee = (
    df_fact_sale.alias("sale")
    .join(df_dimension_date.alias("date"), df_fact_sale.InvoiceDateKey == df_dimension_date.Date, "inner")
    .join(df_dimension_employee.alias("employee"), df_fact_sale.SalespersonKey == df_dimension_employee.EmployeeKey, "inner")
    .select("date.Date", "date.CalendarMonthLabel", "date.Day", "date.ShortMonth", "date.CalendarYear", "employee.PreferredName", "employee.Employee", "sale.TotalExcludingTax", "sale.TaxAmount", "sale.TotalIncludingTax", "sale.Profit")
    .groupBy("date.Date", "date.CalendarMonthLabel", "date.Day", "date.ShortMonth", "date.CalendarYear", "employee.PreferredName", "employee.Employee")
    .sum("sale.TotalExcludingTax", "sale.TaxAmount", "sale.TotalIncludingTax", "sale.Profit")
    .withColumnRenamed("sum(TotalExcludingTax)", "SumOfTotalExcludingTax")
    .withColumnRenamed("sum(TaxAmount)", "SumOfTaxAmount")
    .withColumnRenamed("sum(TotalIncludingTax)", "SumOfTotalIncludingTax")
    .withColumnRenamed("sum(Profit)", "SumOfProfit")
    .orderBy("date.Date", "employee.PreferredName", "employee.Employee")
)

sale_by_date_employee.write.mode("overwrite").format("delta").option("overwriteSchema", "true").save("Tables/aggregate_sale_by_date_employee")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
