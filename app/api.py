
from fastapi import FastAPI
import pandas as pd
import numpy as np
import joblib
import os

app = FastAPI(
    title="AI Furniture Intelligence System",
    description="Demand Prediction, Inventory Recommendation and Product Recommendation API",
    version="1.0"
)

BASE_DIR = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..")
)

DATA_DIR = os.path.join(BASE_DIR, "data", "raw")
MODEL_DIR = os.path.join(BASE_DIR, "models")

# ============================================================
# LOAD DATA
# ============================================================

products = pd.read_csv(
    os.path.join(DATA_DIR, "products.csv")
)

similarity_matrix = np.load(
    os.path.join(
        MODEL_DIR,
        "product_similarity_matrix.npy"
    )
)

demand_model = joblib.load(
    os.path.join(
        MODEL_DIR,
        "demand_prediction_model.pkl"
    )
)

# ============================================================
# HOME
# ============================================================

@app.get("/")
def home():
    return {
        "message": "AI Furniture Intelligence System API is running"
    }


# ============================================================
# HEALTH
# ============================================================

@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


# ============================================================
# PRODUCT RECOMMENDATION
# ============================================================

@app.get("/recommend/{product_id}")
def recommend_product(product_id: str, top_n: int = 5):

    if product_id not in products["product_id"].values:
        return {
            "error": "Product ID not found"
        }

    product_index = products[
        products["product_id"] == product_id
    ].index[0]

    similarity_scores = similarity_matrix[
        product_index
    ]

    similar_indices = similarity_scores.argsort()[::-1]

    similar_indices = [
        i
        for i in similar_indices
        if i != product_index
    ][:top_n]

    recommendations = products.iloc[
        similar_indices
    ][
        [
            "product_id",
            "product_name",
            "category",
            "material",
            "style",
            "color",
            "price"
        ]
    ]

    return {
        "product_id": product_id,
        "recommendations": recommendations.to_dict(
            orient="records"
        )
    }


# ============================================================
# DEMAND PREDICTION
# ============================================================

@app.get("/predict-demand/{product_id}")
def predict_demand(product_id: str):

    if product_id not in products["product_id"].values:
        return {
            "error": "Product ID not found"
        }

    # --------------------------------------------------------
    # LOAD SALES DATA
    # --------------------------------------------------------

    sales = pd.read_csv(
        os.path.join(DATA_DIR, "sales.csv")
    )

    sales["date"] = pd.to_datetime(
        sales["date"]
    )

    # --------------------------------------------------------
    # PRODUCT SALES
    # --------------------------------------------------------

    product_sales = sales[
        sales["product_id"] == product_id
    ].sort_values("date")

    if len(product_sales) < 30:
        return {
            "error": "Not enough sales history"
        }

    # --------------------------------------------------------
    # LATEST SALES RECORD
    # --------------------------------------------------------

    latest = product_sales.iloc[-1]

    date = latest["date"]

    # --------------------------------------------------------
    # LAG FEATURES
    # --------------------------------------------------------

    lag_1 = product_sales["units_sold"].iloc[-1]

    lag_7 = product_sales["units_sold"].iloc[-7]

    lag_30 = product_sales["units_sold"].iloc[-30]

    # --------------------------------------------------------
    # ROLLING FEATURES
    # --------------------------------------------------------

    rolling_7 = (
        product_sales["units_sold"]
        .tail(7)
        .mean()
    )

    rolling_30 = (
        product_sales["units_sold"]
        .tail(30)
        .mean()
    )

    # ========================================================
    # CREATE FEATURES
    # IMPORTANT:
    # SAME FEATURE NAMES AND SAME ORDER AS MODEL TRAINING
    # ========================================================

    features = pd.DataFrame([[
        date.month,
        date.dayofweek,
        date.day,
        int(date.isocalendar().week),
        int(date.dayofweek >= 5),
        lag_1,
        lag_7,
        lag_30,
        rolling_7,
        rolling_30
    ]], columns=[
        "month",
        "day_of_week",
        "day_of_month",
        "week_of_year",
        "is_weekend",
        "lag_1",
        "lag_7",
        "lag_30",
        "rolling_7",
        "rolling_30"
    ])

    # ========================================================
    # PREDICTION
    # ========================================================

    prediction = demand_model.predict(
        features
    )[0]

    # ========================================================
    # RESPONSE
    # ========================================================

    return {
        "product_id": product_id,
        "predicted_demand": round(
            float(prediction),
            2
        )
    }
