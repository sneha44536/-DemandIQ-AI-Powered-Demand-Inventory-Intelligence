import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="AI Furniture Intelligence Dashboard",
    page_icon="🪑",
    layout="wide"
)

st.title("🪑 AI Furniture Intelligence Dashboard")
st.markdown("### Demand Forecasting & Inventory Intelligence")

# ============================================================
# LOAD SALES DATA
# ============================================================

sales = pd.read_csv("data/raw/sales.csv")
sales["date"] = pd.to_datetime(sales["date"])

# ============================================================
# PRODUCT SELECTION
# ============================================================

product_ids = sales["product_id"].unique()

selected_product = st.selectbox(
    "Select Product",
    product_ids
)

product_sales = sales[
    sales["product_id"] == selected_product
].sort_values("date")

# ============================================================
# LINE CHART
# ============================================================

st.subheader("📈 Actual Sales Trend")

fig = px.line(
    product_sales,
    x="date",
    y="units_sold",
    title=f"Daily Sales Trend — {selected_product}",
    markers=True
)

fig.update_layout(
    xaxis_title="Date",
    yaxis_title="Units Sold",
    hovermode="x unified"
)

st.plotly_chart(
    fig,
    use_container_width=True
)