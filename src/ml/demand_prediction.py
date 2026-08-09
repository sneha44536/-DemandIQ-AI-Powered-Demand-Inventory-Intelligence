import pandas as pd
import os

# Project root
BASE_DIR = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../..")
)

# Sales dataset path
SALES_FILE = os.path.join(
    BASE_DIR,
    "data",
    "raw",
    "sales.csv"
)

# Load sales data
sales = pd.read_csv(SALES_FILE)

# Convert date
sales["date"] = pd.to_datetime(sales["date"])

# Sort data
sales = sales.sort_values(
    ["product_id", "date"]
)

print("=" * 60)
print("DEMAND PREDICTION - DATA PREPARATION")
print("=" * 60)

print(f"\nSales shape: {sales.shape}")

print("\nDate range:")
print(sales["date"].min(), "to", sales["date"].max())

print("\nNumber of products:")
print(sales["product_id"].nunique())

print("\nMissing values:")
print(sales.isnull().sum())


# ============================================================
# CREATE DEMAND FEATURES
# ============================================================

sales["month"] = sales["date"].dt.month
sales["day_of_week"] = sales["date"].dt.dayofweek
sales["day_of_month"] = sales["date"].dt.day
sales["week_of_year"] = sales["date"].dt.isocalendar().week.astype(int)

# Weekend indicator
sales["is_weekend"] = (
    sales["day_of_week"] >= 5
).astype(int)

# Create lag features product-wise
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

# Rolling demand
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

print("\nFEATURES CREATED")
print("-" * 60)

print(sales[
    [
        "date",
        "product_id",
        "units_sold",
        "lag_1",
        "lag_7",
        "lag_30",
        "rolling_7",
        "rolling_30"
    ]
].head(40))


# ============================================================
# TRAIN DEMAND PREDICTION MODEL
# ============================================================

from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import numpy as np

# Remove rows where lag/rolling features are not available
model_data = sales.dropna().copy()

# Features used by the model
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

target = "units_sold"


# ============================================================
# TIME-BASED TRAIN / TEST SPLIT
# ============================================================

# Important:
# We DON'T randomly split time-series data.
# We train on older data and test on newer data.

split_date = pd.Timestamp("2025-07-01")

train_data = model_data[
    model_data["date"] < split_date
]

test_data = model_data[
    model_data["date"] >= split_date
]

X_train = train_data[features]
y_train = train_data[target]

X_test = test_data[features]
y_test = test_data[target]


print("\nMODEL DATA")
print("-" * 60)

print("Training samples:", len(X_train))
print("Testing samples :", len(X_test))


# ============================================================
# RANDOM FOREST MODEL
# ============================================================

model = RandomForestRegressor(
    n_estimators=100,
    max_depth=15,
    random_state=42,
    n_jobs=-1
)

model.fit(
    X_train,
    y_train
)


# ============================================================
# PREDICTION
# ============================================================

y_pred = model.predict(X_test)


# ============================================================
# MODEL EVALUATION
# ============================================================

mae = mean_absolute_error(
    y_test,
    y_pred
)

rmse = np.sqrt(
    mean_squared_error(
        y_test,
        y_pred
    )
)

r2 = r2_score(
    y_test,
    y_pred
)


print("\nMODEL PERFORMANCE")
print("-" * 60)

print(f"MAE  : {mae:.2f}")
print(f"RMSE : {rmse:.2f}")
print(f"R²   : {r2:.4f}")


# ============================================================
# FEATURE IMPORTANCE
# ============================================================

importance = pd.DataFrame({
    "feature": features,
    "importance": model.feature_importances_
}).sort_values(
    "importance",
    ascending=False
)

print("\nFEATURE IMPORTANCE")
print("-" * 60)

print(importance)


# ============================================================
# SAVE TRAINED MODEL
# ============================================================

import joblib

MODEL_DIR = os.path.join(
    BASE_DIR,
    "models"
)

os.makedirs(
    MODEL_DIR,
    exist_ok=True
)

model_file = os.path.join(
    MODEL_DIR,
    "demand_prediction_model.pkl"
)

joblib.dump(
    model,
    model_file
)

print("\nMODEL SAVED SUCCESSFULLY")
print(f"Model path: {model_file}")