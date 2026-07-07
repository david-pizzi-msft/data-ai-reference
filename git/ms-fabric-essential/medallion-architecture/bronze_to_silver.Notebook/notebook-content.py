# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "148d5b98-8603-4f78-90de-a9ad6bba2b93",
# META       "default_lakehouse_name": "raw_Bronze",
# META       "default_lakehouse_workspace_id": "3fde5055-2967-43fb-885a-85a5d422e684",
# META       "known_lakehouses": [
# META         {
# META           "id": "148d5b98-8603-4f78-90de-a9ad6bba2b93"
# META         },
# META         {
# META           "id": "440ca1cf-69d9-465f-8478-a1a334ba1fed"
# META         }
# META       ]
# META     }
# META   }
# META }

# CELL ********************

from pyspark.sql.types import *
import pyspark.sql.functions
from pyspark.sql import *

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# Read the data from the bronze layer:
df_raw_2020orders = spark.read.format("delta").load("Tables/2020orders")

df_raw_2020orders.head(2)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# Clean the data (filter out rows with null values in the 'Date' column):
df_cleaned = df_raw_2020orders.filter(df_raw_2020orders["Date"].isNotNull())
print(df_cleaned)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# Save the cleaned data to the "cleansed_Silver" table in the Silver lakehouse:
df_cleaned.write.format("delta").mode("overwrite").saveAsTable("cleansed_Silver.2020orders_silver")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# Read data from the Bronze layer
bronze_df = spark.read.format("delta").load("Tables/products")
# Perform transformations (if any)
silver_df = bronze_df  # Assuming no transformations for simplicity
# Write data to the Silver layer
silver_df.write.mode("overwrite").format("delta").saveAsTable("cleansed_Silver.products_silver")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
