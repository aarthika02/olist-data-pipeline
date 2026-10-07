import os
import duckdb

# Database file location
db_path = "/workspaces/olist-data-pipeline/olist_warehouse.db"

# Connect to DuckDB
con = duckdb.connect(db_path)

# Ensure bronze schema exists
con.execute("CREATE SCHEMA IF NOT EXISTS bronze;")

raw_data_dir = "/workspaces/olist-data-pipeline/data/raw"

# Loop through all raw CSV files
for file_name in os.listdir(raw_data_dir):
    if file_name.endswith(".csv"):
        # Format table name: olist_orders_dataset.csv -> raw_orders
        clean_name = file_name.replace("olist_", "").replace("_dataset.csv", "").replace(".csv", "")
        table_name = f"raw_{clean_name}"
        file_path = os.path.join(raw_data_dir, file_name)
        
        # Load raw CSV directly into DuckDB bronze schema
        query = f"""
            CREATE OR REPLACE TABLE bronze.{table_name} AS 
            SELECT * FROM read_csv_auto('{file_path}');
        """
        con.execute(query)
        print(f"Loaded {file_name} into bronze.{table_name}")

con.close()
print("Ingestion complete!")