import streamlit as st
import duckdb

st.set_page_config(page_title="E-Commerce Analytics", layout="wide")
st.title("📦 Olist E-Commerce Performance Dashboard")

con = duckdb.connect("/workspaces/olist-data-pipeline/olist_warehouse.db")

# Key Metrics
metrics = con.execute("""
    SELECT 
        COUNT(order_id) AS total_orders,
        ROUND(SUM(order_revenue), 2) AS total_revenue,
        ROUND(AVG(order_revenue), 2) AS avg_order_value
    FROM main.fct_orders
""").fetchone()

col1, col2, col3 = st.columns(3)
col1.metric("Total Orders", f"{metrics[0]:,}")
col2.metric("Total Revenue ($)", f"${metrics[1]:,.2f}")
col3.metric("Avg Order Value ($)", f"${metrics[2]:,.2f}")

# Monthly Trend
st.subheader("Monthly Revenue Growth")
monthly_df = con.execute("""
    SELECT 
        DATE_TRUNC('month', purchased_at) AS month,
        SUM(order_revenue) AS revenue
    FROM main.fct_orders
    WHERE purchased_at IS NOT NULL
    GROUP BY 1
    ORDER BY 1
""").df()

st.line_chart(data=monthly_df, x="month", y="revenue")