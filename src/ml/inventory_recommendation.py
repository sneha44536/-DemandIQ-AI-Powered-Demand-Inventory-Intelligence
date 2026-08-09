import pandas as pd
import numpy as np
import joblib
import os

BASE_DIR = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../..")
)

DATA_DIR = os.path.join(BASE_DIR, "data", "raw")
MODEL_DIR = os.path.join(BASE_DIR, "models")

sales = pd.read_csv(
    os.path.join(DATA_DIR, "sales.csv")
)

inventory = pd.read_csv(
    os.path.join(DATA_DIR, "inventory.csv")
)

products = pd.read_csv(
    os.path.join(DATA_DIR, "products.csv")
)

sales["date"] = pd.to_datetime(sales["date"])

model = joblib.load(
    os.path.join(
        MODEL_DIR,
        "demand_prediction_model.pkl"
    )
)

print("=" * 60)
print("INVENTORY RECOMMENDATION SYSTEM")
print("=" * 60)

print("\nData loaded successfully.")
print("Products :", len(products))
print("Inventory:", len(inventory))
print("Sales    :", len(sales))


# ============================================================
# INVENTORY REORDER CALCULATION
# ============================================================

latest_date = sales["date"].max()

recent_sales = sales[
    sales["date"] > latest_date - pd.Timedelta(days=30)
]

daily_demand = (
    recent_sales
    .groupby("product_id")["units_sold"]
    .mean()
    .reset_index()
)

daily_demand.rename(
    columns={"units_sold": "avg_daily_demand"},
    inplace=True
)

recommendation = inventory.merge(
    daily_demand,
    on="product_id",
    how="left"
)

recommendation["avg_daily_demand"] = (
    recommendation["avg_daily_demand"].fillna(0)
)

planning_days = 30

recommendation["expected_demand"] = (
    recommendation["avg_daily_demand"]
    * planning_days
)

recommendation["safety_stock"] = (
    recommendation["expected_demand"]
    * 0.20
)

recommendation["required_inventory"] = (
    recommendation["expected_demand"]
    + recommendation["safety_stock"]
)

recommendation["reorder_quantity"] = (
    recommendation["required_inventory"]
    - recommendation["current_inventory"]
)

recommendation["reorder_quantity"] = (
    recommendation["reorder_quantity"]
    .clip(lower=0)
    .round()
    .astype(int)
)

recommendation["reorder_status"] = np.where(
    recommendation["reorder_quantity"] > 0,
    "REORDER",
    "SUFFICIENT"
)

print("\n" + "=" * 60)
print("INVENTORY REORDER RECOMMENDATIONS")
print("=" * 60)

print(
    recommendation[
        [
            "product_id",
            "current_inventory",
            "avg_daily_demand",
            "expected_demand",
            "safety_stock",
            "reorder_quantity",
            "reorder_status"
        ]
    ].head(20)
)
