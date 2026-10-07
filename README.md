# olist-data-pipeline
End-to-end e-commerce data engineering pipeline with DuckDB, dbt, and Streamlit.

[ Raw CSV Files ] 
       │
       ▼
[ DuckDB / Python Extraction ]  ───► Ingestion Layer
       │
       ▼
[ dbt-duckdb ]                 ───► Transformation & Testing Layer (SQL + Data Quality)
       │
       ▼
[ DuckDB Data Warehouse ]      ───► Analytics-Ready Data Models
       │
       ▼
[ Streamlit / Evidence.dev ]   ───► Interactive BI & Dashboarding
