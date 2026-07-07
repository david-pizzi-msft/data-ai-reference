# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "440ca1cf-69d9-465f-8478-a1a334ba1fed",
# META       "default_lakehouse_name": "cleansed_Silver",
# META       "default_lakehouse_workspace_id": "3fde5055-2967-43fb-885a-85a5d422e684",
# META       "known_lakehouses": [
# META         {
# META           "id": "440ca1cf-69d9-465f-8478-a1a334ba1fed"
# META         },
# META         {
# META           "id": "73c2c570-5aae-40cc-bd98-5c30ff723969"
# META         }
# META       ]
# META     }
# META   }
# META }

# CELL ********************

from pyspark.sql.types import *
import pyspark.sql.functions
from pyspark.sql import *
from pyspark.sql.functions import sum

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# Read the data from the silver layer:
df_cleansed_2020orders = spark.read.format("delta").load("Tables/2020orders_silver")
df_cleansed_2020orders.head(2)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# Cast the 'tax' column from double to int:
df_cleansed_2020orders = df_cleansed_2020orders.withColumn("tax", df_cleansed_2020orders["tax"].cast("int"))  # type to int
df_cleansed_2020orders.printSchema()

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# Group and aggregate the data:
df_aggregated = df_cleansed_2020orders.groupBy("Style").agg(sum("price").alias("total_price_vehicles"))
df_aggregated.show(10, truncate=False)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# Save the aggregated data to the "curated_Gold" table in the Gold lakehouse:
df_aggregated.write.format("delta").mode("overwrite").saveAsTable("curated_Gold.2020orders_gold")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# Read data from the Silver layer
silver_df = spark.read.format("delta").load("Tables/products_silver")
# Perform transformations (if any)
silver_df = silver_df  # Assuming no transformations for simplicity
# Write data to the Gold layer
silver_df.write.mode("overwrite").format("delta").saveAsTable("curated_Gold.products_gold")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
