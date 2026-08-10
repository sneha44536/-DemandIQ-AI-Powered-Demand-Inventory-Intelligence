import pandas as pd
import joblib
import os

from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import numpy as np


# ============================================================
# PROJECT PATHS
# ============================================================

BASE_DIR = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..")
)

DATA_DIR = os.path.join(BASE_DIR, "data", "raw")
MODEL_DIR = os.path.join(BASE_DIR, "models")


# ============================================================
# LOAD DATA
# ============================================================

sales = pd.read_csv(
    os.path.join(DATA_DIR, "sales.csv")
)

sales["date"] = pd.to_datetime(sales["date"])


# ============================================================
# CREATE FEATURES
# ============================================================

sales = sales.sort_values(
    ["product_id", "date"]
)

sales["month"] = sales["date"].dt.month
sales["day_of_week"] = sales["date"].dt.dayofweek
sales["day_of_month"] = sales["date"].dt.day
sales["week_of_year"] = sales["date"].dt.isocalendar().week.astype(int)
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
# REMOVE MISSING VALUES
# ============================================================

sales = sales.dropna()


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
# FEATURES
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

y = sales["units_sold"]


# ============================================================
# PREDICTION
# ============================================================

predictions = model.predict(X)


# ============================================================
# EVALUATION METRICS
# ============================================================

mae = mean_absolute_error(
    y,
    predictions
)

rmse = np.sqrt(
    mean_squared_error(
        y,
        predictions
    )
)

r2 = r2_score(
    y,
    predictions
)


# ============================================================
# RESULTS
# ============================================================

print("\n========================================")
print("DEMAND MODEL EVALUATION")
print("========================================")

print(f"MAE  : {mae:.2f}")
print(f"RMSE : {rmse:.2f}")
print(f"R²   : {r2:.4f}")

print("========================================")

# ============================================================
# ACTUAL VS PREDICTED DEMAND
# ============================================================

import matplotlib.pyplot as plt

plt.figure(figsize=(8, 6))

plt.scatter(
    y,
    predictions,
    alpha=0.5
)

# Perfect prediction reference line
plt.plot(
    [y.min(), y.max()],
    [y.min(), y.max()],
    linestyle="--"
)

plt.xlabel("Actual Demand")
plt.ylabel("Predicted Demand")
plt.title("Actual vs Predicted Demand")

plt.tight_layout()
plt.show()