import streamlit as st
import sys
import os

# ============================================================
# PROJECT PATH
# ============================================================

BASE_DIR = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..")
)

sys.path.append(
    os.path.join(BASE_DIR, "genai")
)

from recommendation import get_recommendation


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="AI Furniture Assistant",
    page_icon="🤖",
    layout="wide"
)


# ============================================================
# HEADER
# ============================================================

st.title("🤖 AI Furniture Business Assistant")

st.markdown(
    """
    ### Intelligent Inventory Recommendation System

    Get AI-powered inventory insights for your furniture products.
    """
)

st.divider()


# ============================================================
# PRODUCT INPUT
# ============================================================

st.subheader("🔎 Product Analysis")

product_id = st.text_input(
    "Enter Product ID",
    placeholder="Example: P001"
)


# ============================================================
# ANALYZE
# ============================================================

if st.button("🚀 Analyze Product"):

    if not product_id:

        st.warning("Please enter a Product ID.")

    else:

        result = get_recommendation(
            product_id.upper()
        )

        if isinstance(result, str):

            st.error(result)

        else:

            st.success("Product analysis completed!")

            # =================================================
            # KPI CARDS
            # =================================================

            col1, col2, col3, col4 = st.columns(4)

            col1.metric(
                "📦 Current Inventory",
                result["current_inventory"]
            )

            col2.metric(
                "📈 Average Demand",
                result["average_demand"]
            )

            col3.metric(
                "🔄 Reorder Point",
                result["reorder_point"]
            )

            col4.metric(
                "🛡️ Safety Stock",
                result["safety_stock"]
            )

            st.divider()

            # =================================================
            # PRODUCT DETAILS
            # =================================================

            st.subheader("📋 Inventory Details")

            col1, col2 = st.columns(2)

            with col1:

                st.write(
                    "**Product ID:**",
                    result["product_id"]
                )

                st.write(
                    "**Supplier:**",
                    result["supplier"]
                )

            with col2:

                st.write(
                    "**Lead Time:**",
                    f'{result["lead_time_days"]} days'
                )

                st.write(
                    "**Recommendation:**",
                    result["recommendation"]
                )

            st.divider()

            # =================================================
            # AI RECOMMENDATION
            # =================================================

            st.subheader("💡 AI Inventory Recommendation")

            recommendation = result["recommendation"]

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