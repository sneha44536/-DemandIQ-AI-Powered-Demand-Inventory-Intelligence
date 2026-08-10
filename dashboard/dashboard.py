import streamlit as st
import pandas as pd
import plotly.express as px
import requests

# ============================================================

# PAGE CONFIG

# ============================================================

st.set_page_config(
page_title="AI Furniture Intelligence",
page_icon="🪑",
layout="wide"
)

# ============================================================

# PATHS

# ============================================================

DATA_PATH = "dashboard/demand_dashboard.csv"
API_URL = "http://127.0.0.1:8000"

# ============================================================

# LOAD DATA

# ============================================================

df = pd.read_csv(DATA_PATH)
df["date"] = pd.to_datetime(df["date"])

# ============================================================

# HEADER

# ============================================================

st.title("🪑 AI Furniture Intelligence Dashboard")
st.markdown(
"### 📊 Demand Forecasting • Inventory Intelligence • Product Analytics"
)

st.divider()

# ============================================================

# SIDEBAR

# ============================================================

st.sidebar.header("🔎 Dashboard Filters")

products = sorted(df["product_id"].unique())

selected_product = st.sidebar.selectbox(
"Select Product",
products
)

filtered_df = (
df[df["product_id"] == selected_product]
.sort_values("date")
)

# ============================================================

# KPI SECTION

# ============================================================

total_sales = filtered_df["units_sold"].sum()
avg_demand = filtered_df["units_sold"].mean()
max_demand = filtered_df["units_sold"].max()
latest_demand = filtered_df.iloc[-1]["units_sold"]

col1, col2, col3, col4 = st.columns(4)

col1.metric(
"📦 Total Units Sold",
f"{total_sales:,.0f}"
)

col2.metric(
"📈 Average Demand",
f"{avg_demand:.2f}"
)

col3.metric(
"🔥 Peak Demand",
f"{max_demand:.0f}"
)

col4.metric(
"📅 Latest Demand",
f"{latest_demand:.0f}"
)

st.divider()

# ============================================================

# DEMAND TREND

# ============================================================

st.subheader("📈 Demand Trend")

fig = px.line(
filtered_df,
x="date",
y="units_sold",
title=f"Demand Trend — {selected_product}",
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

# ============================================================

# ACTUAL VS PREDICTED

# ============================================================

if "predicted_demand" in filtered_df.columns:

```
st.subheader("🤖 Actual vs Predicted Demand")

fig2 = px.line(
    filtered_df,
    x="date",
    y=["units_sold", "predicted_demand"],
    title=f"Actual vs Predicted Demand — {selected_product}",
    markers=True
)

fig2.update_layout(
    xaxis_title="Date",
    yaxis_title="Demand",
    hovermode="x unified"
)

st.plotly_chart(
    fig2,
    use_container_width=True
)
```

else:

```
st.info(
    "Predicted demand column is not available in demand_dashboard.csv."
)
```

# ============================================================

# MODEL EVALUATION

# ============================================================

st.subheader("🎯 Demand Model Evaluation")

metric1, metric2, metric3 = st.columns(3)

metric1.metric(
"MAE",
"2.17"
)

metric2.metric(
"RMSE",
"3.09"
)

metric3.metric(
"R² Score",
"0.8982"
)

st.caption(
"Evaluation results from the trained demand prediction model."
)

st.divider()

# ============================================================

# INVENTORY RECOMMENDATION

# ============================================================

st.subheader("📦 Inventory Intelligence")

if st.button("🔍 Check Inventory"):

```
try:

    response = requests.get(
        f"{API_URL}/inventory/{selected_product}",
        timeout=10
    )

    if response.status_code == 200:

        data = response.json()

        if "error" in data:

            st.error(data["error"])

        else:

            inv1, inv2, inv3, inv4 = st.columns(4)

            inv1.metric(
                "Current Inventory",
                data["current_inventory"]
            )

            inv2.metric(
                "Expected Demand",
                data["expected_demand"]
            )

            inv3.metric(
                "Safety Stock",
                data["safety_stock"]
            )

            inv4.metric(
                "Reorder Quantity",
                data["reorder_quantity"]
            )

            if data["reorder_status"] == "REORDER":

                st.warning(
                    "⚠️ REORDER REQUIRED — Inventory is below the required level."
                )

            else:

                st.success(
                    "✅ Inventory level is sufficient."
                )

    else:

        st.error(
            "Inventory API returned an error."
        )

except requests.exceptions.ConnectionError:

    st.error(
        "❌ Backend API is not running. Start FastAPI first."
    )
```

# ============================================================

# PRODUCT RECOMMENDATION

# ============================================================

st.divider()

st.subheader("🛋️ Similar Product Recommendations")

top_n = st.slider(
"Number of recommendations",
1,
10,
5
)

if st.button("🛋️ Get Recommendations"):

```
try:

    response = requests.get(
        f"{API_URL}/recommend/{selected_product}",
        params={"top_n": top_n},
        timeout=10
    )

    if response.status_code == 200:

        data = response.json()

        if "error" in data:

            st.error(data["error"])

        else:

            st.success(
                f"Products similar to {selected_product}"
            )

            st.dataframe(
                data["recommendations"],
                use_container_width=True,
                hide_index=True
            )

    else:

        st.error(
            "Recommendation API error."
        )

except requests.exceptions.ConnectionError:

    st.error(
        "❌ Backend API is not running. Start FastAPI first."
    )
```

# ============================================================

# PRODUCT SUMMARY

# ============================================================

st.divider()

st.subheader("📋 Product Demand Summary")

summary = filtered_df[
["date", "product_id", "units_sold"]
].tail(20)

st.dataframe(
summary,
use_container_width=True,
hide_index=True
)
