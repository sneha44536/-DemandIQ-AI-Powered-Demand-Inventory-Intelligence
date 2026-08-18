import pandas as pd
import numpy as np
import joblib
import os

# ============================================================
# PROJECT PATHS
# ============================================================

BASE_DIR = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..")
)

DATA_DIR = os.path.join(BASE_DIR, "data", "raw")
MODEL_DIR = os.path.join(BASE_DIR, "models")

OUTPUT_FILE = os.path.join(
    BASE_DIR,
    "dashboard",
    "demand_dashboard.csv"
)

# ============================================================
# LOAD SALES DATA
# ============================================================

sales = pd.read_csv(
    os.path.join(DATA_DIR, "sales.csv")
)

sales["date"] = pd.to_datetime(sales["date"])

# ============================================================
# SORT DATA
# ============================================================

sales = sales.sort_values(
    ["product_id", "date"]
).reset_index(drop=True)

# ============================================================
# CREATE FEATURES
# ============================================================

sales["month"] = sales["date"].dt.month

sales["day_of_week"] = (
    sales["date"].dt.dayofweek
)

sales["day_of_month"] = (
    sales["date"].dt.day
)

sales["week_of_year"] = (
    sales["date"].dt.isocalendar().week.astype(int)
)

sales["is_weekend"] = (
    sales["date"].dt.dayofweek >= 5
).astype(int)

sales["lag_1"] = (
    sales.groupby("product_id")["units_sold"]
    .shift(1)
)

sales["lag_7"] = (
    sales.groupby("product_id")["units_sold"]
    .shift(7)
)

sales["lag_30"] = (
    sales.groupby("product_id")["units_sold"]
    .shift(30)
)

sales["rolling_7"] = (
    sales.groupby("product_id")["units_sold"]
    .transform(
        lambda x: x.shift(1).rolling(7).mean()
    )
)

sales["rolling_30"] = (
    sales.groupby("product_id")["units_sold"]
    .transform(
        lambda x: x.shift(1).rolling(30).mean()
    )
)

# ============================================================
# REMOVE ROWS WITHOUT ENOUGH HISTORY
# ============================================================

sales = sales.dropna().reset_index(drop=True)

# ============================================================
# LOAD TRAINED MODEL
# ============================================================

model = joblib.load(
    os.path.join(
        MODEL_DIR,
        "demand_prediction_model.pkl"
    )
)

# ============================================================
# MODEL FEATURES
# ============================================================

features = [
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
]

X = sales[features]

# ============================================================
# PREDICTION
# ============================================================

sales["predicted_demand"] = model.predict(X)

sales["predicted_demand"] = (
    sales["predicted_demand"]
    .round(2)
)

# ============================================================
# ERROR
# ============================================================

sales["prediction_error"] = (
    sales["units_sold"]
    - sales["predicted_demand"]
).round(2)

sales["absolute_error"] = (
    sales["prediction_error"]
    .abs()
).round(2)

# ============================================================
# SELECT POWER BI COLUMNS
# ============================================================

dashboard_data = sales[
    [
        "date",
        "product_id",
        "units_sold",
        "predicted_demand",
        "prediction_error",
        "absolute_error",
        "discount_percent",
        "selling_price"
    ]
]

# ============================================================
# SAVE
# ============================================================

dashboard_data.to_csv(
    OUTPUT_FILE,
    index=False
)

print("\n========================================")
print("POWER BI DATA CREATED")
print("========================================")

print("Rows:", len(dashboard_data))

print("\nColumns:")
print(dashboard_data.columns.tolist())

print("\nSaved to:")
print(OUTPUT_FILE)

print("========================================")