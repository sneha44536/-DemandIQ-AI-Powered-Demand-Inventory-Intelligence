import streamlit as st
import requests

st.set_page_config(
    page_title="AI Furniture Intelligence",
    page_icon="🪑",
    layout="wide"
)

API_URL = "http://127.0.0.1:8000"

st.title("🪑 AI Furniture Intelligence System")
st.write(
    "Demand Prediction • Inventory Recommendation • Product Recommendation"
)

# ============================================================
# PRODUCT ID
# ============================================================

product_id = st.text_input(
    "Enter Product ID",
    placeholder="Example: P001"
)

# ============================================================
# DEMAND PREDICTION
# ============================================================

st.header("📈 Demand Prediction")

if st.button("Predict Demand"):

    if product_id:

        response = requests.get(
            f"{API_URL}/predict-demand/{product_id}"
        )

        if response.status_code == 200:

            data = response.json()

            if "error" in data:
                st.error(data["error"])

            else:
                st.metric(
                    "Predicted Demand",
                    f"{data['predicted_demand']} units"
                )

        else:
            st.error("Demand prediction API error.")

    else:
        st.warning("Please enter a Product ID.")


# ============================================================
# INVENTORY RECOMMENDATION
# ============================================================

st.header("📦 Inventory Recommendation")

if st.button("Check Inventory"):

    if product_id:

        response = requests.get(
            f"{API_URL}/inventory/{product_id}"
        )

        if response.status_code == 200:

            data = response.json()

            if "error" in data:
                st.error(data["error"])

            else:

                col1, col2, col3 = st.columns(3)

                col1.metric(
                    "Current Inventory",
                    data["current_stock"]
                )

                col2.metric(
                    "Expected Demand",
                    data["expected_demand"]
                )

                col3.metric(
                    "Reorder Quantity",
                    data["reorder_quantity"]
                )

                if data["reorder_status"] == "REORDER":

                    st.warning(
                        "⚠️ Inventory is low. Reorder recommended."
                    )

                else:

                    st.success(
                        "✅ Inventory level is sufficient."
                    )

        else:
            st.error("Inventory API error.")

    else:
        st.warning("Please enter a Product ID.")


# ============================================================
# PRODUCT RECOMMENDATION
# ============================================================

st.header("🛋️ Similar Product Recommendations")

top_n = st.slider(
    "Number of recommendations",
    1,
    10,
    5
)

if st.button("Get Recommendations"):

    if product_id:

        response = requests.get(
            f"{API_URL}/recommend/{product_id}",
            params={"top_n": top_n}
        )

        if response.status_code == 200:

            data = response.json()

            if "error" in data:
                st.error(data["error"])

            else:

                st.success(
                    f"Products similar to {product_id}"
                )

                st.dataframe(
                    data["recommendations"],
                    use_container_width=True
                )

        else:
            st.error("Recommendation API error.")

    else:
        st.warning("Please enter a Product ID.")