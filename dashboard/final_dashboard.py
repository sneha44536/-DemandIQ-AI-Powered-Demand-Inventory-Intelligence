import streamlit as st
import pandas as pd
import plotly.express as px
import os
import sys

# ============================================================
# PATHS
# ============================================================

BASE_DIR = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..")
)

DATA_PATH = os.path.join(
    BASE_DIR,
    "dashboard",
    "demand_dashboard.csv"
)

INVENTORY_PATH = os.path.join(
    BASE_DIR,
    "data",
    "raw",
    "inventory.csv"
)

sys.path.append(
    os.path.join(BASE_DIR, "genai")
)

from recommendation import get_recommendation


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="AI Furniture Intelligence",
    page_icon="🪑",
    layout="wide"
)


# ============================================================
# CUSTOM HEADER
# ============================================================

st.title("🪑 AI Furniture Intelligence")

st.markdown(
    """
    ### 📊 Demand Forecasting • 📦 Inventory Intelligence • 🤖 GenAI Assistant
    """
)

st.divider()


# ============================================================
# LOAD DATA
# ============================================================

df = pd.read_csv(DATA_PATH)

df["date"] = pd.to_datetime(df["date"])

inventory = pd.read_csv(INVENTORY_PATH)


# ============================================================
# SIDEBAR
# ============================================================

st.sidebar.title("🔎 Dashboard Controls")

products = sorted(
    df["product_id"].unique()
)

selected_product = st.sidebar.selectbox(
    "Select Product",
    products
)

filtered_df = df[
    df["product_id"] == selected_product
].sort_values("date")


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
# DEMAND ANALYTICS
# ============================================================

st.header("📊 Demand Analytics")

col1, col2 = st.columns(2)


# -------------------------------
# Demand Trend
# -------------------------------

with col1:

    st.subheader("📈 Demand Trend")

    fig = px.line(
        filtered_df,
        x="date",
        y="units_sold",
        markers=True,
        title=f"Demand Trend — {selected_product}"
    )

    fig.update_layout(
        xaxis_title="Date",
        yaxis_title="Units Sold"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )


# -------------------------------
# Actual vs Predicted
# -------------------------------

with col2:

    st.subheader("🤖 Actual vs Predicted")

    if "predicted_demand" in filtered_df.columns:

        fig2 = px.line(
            filtered_df,
            x="date",
            y=[
                "units_sold",
                "predicted_demand"
            ],
            title="Actual vs Predicted Demand"
        )

        fig2.update_layout(
            xaxis_title="Date",
            yaxis_title="Demand"
        )

        st.plotly_chart(
            fig2,
            use_container_width=True
        )

    else:

        st.info(
            "Predicted demand data unavailable."
        )


# ============================================================
# MODEL PERFORMANCE
# ============================================================

st.subheader("🎯 ML Model Performance")

col1, col2, col3 = st.columns(3)

col1.metric(
    "R² Score",
    "0.8982"
)

col2.metric(
    "MAE",
    "2.17"
)

col3.metric(
    "RMSE",
    "3.09"
)

st.divider()


# ============================================================
# INVENTORY INTELLIGENCE
# ============================================================

st.header("📦 Inventory Intelligence")

inventory_result = get_recommendation(
    selected_product
)

if isinstance(inventory_result, dict):

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "Current Inventory",
        inventory_result["current_inventory"]
    )

    col2.metric(
        "Safety Stock",
        inventory_result["safety_stock"]
    )

    col3.metric(
        "Reorder Point",
        inventory_result["reorder_point"]
    )

    col4.metric(
        "Lead Time",
        f'{inventory_result["lead_time_days"]} days'
    )

    st.subheader("🏭 Supplier Information")

    st.write(
        f'**Supplier:** {inventory_result["supplier"]}'
    )

    recommendation = inventory_result[
        "recommendation"
    ]

    if "URGENT" in recommendation:

        st.error(
            f"🚨 {recommendation}"
        )

    elif "Increase" in recommendation:

        st.warning(
            f"⚠️ {recommendation}"
        )

    else:

        st.success(
            f"✅ {recommendation}"
        )


else:

    st.error(inventory_result)


st.divider()


# ============================================================
# GENAI BUSINESS ASSISTANT
# ============================================================

st.header("🤖 AI Business Assistant")

st.markdown(
    """
    Ask about a product's inventory and get an AI-powered
    business recommendation.
    """
)

question_product = st.text_input(
    "Enter Product ID",
    placeholder="Example: P001",
    key="genai_product"
)

if st.button(
    "🧠 Get AI Recommendation"
):

    if not question_product:

        st.warning(
            "Please enter a Product ID."
        )

    else:

        result = get_recommendation(
            question_product.upper()
        )

        if isinstance(result, str):

            st.error(result)

        else:

            st.subheader(
                f"💡 AI Analysis — {result['product_id']}"
            )

            current = result[
                "current_inventory"
            ]

            reorder = result[
                "reorder_point"
            ]

            demand = result[
                "average_demand"
            ]

            supplier = result[
                "supplier"
            ]

            lead_time = result[
                "lead_time_days"
            ]

            recommendation = result[
                "recommendation"
            ]

            explanation = f"""
**Product:** {result['product_id']}

The product currently has **{current} units**
in inventory.

The average demand is approximately
**{demand} units per day**.

The reorder point is **{reorder} units**.

The supplier is **{supplier}**, with a lead time
of **{lead_time} days**.

### Recommendation

**{recommendation}**
"""

            st.markdown(explanation)


# ============================================================
# PRODUCT DATA
# ============================================================

st.divider()

st.header("📋 Recent Product Demand")

st.dataframe(
    filtered_df[
        [
            "date",
            "product_id",
            "units_sold"
        ]
    ].tail(20),
    use_container_width=True,
    hide_index=True
)


# ============================================================
# FOOTER
# ============================================================

st.divider()

st.caption(
    "AI Furniture Intelligence • ML + RAG + GenAI + Inventory Analytics"
)