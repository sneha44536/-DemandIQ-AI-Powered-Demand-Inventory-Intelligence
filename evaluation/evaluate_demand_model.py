import pandas as pd
import numpy as np

from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor


# ==========================================
# 1. Load Dataset
# ==========================================

DATA_PATH = "data/demand_data.csv"

df = pd.read_csv(DATA_PATH)

print("Dataset loaded successfully!")
print("Shape:", df.shape)
print("\nColumns:")
print(df.columns.tolist())


# ==========================================
# 2. Prepare Data
# ==========================================

# Change these columns if your dataset uses different names
TARGET = "demand"

X = df.drop(columns=[TARGET])
y = df[TARGET]


# Convert categorical columns into numerical values
X = pd.get_dummies(X, drop_first=True)

# Handle missing values
X = X.fillna(0)
y = y.fillna(0)


# ==========================================
# 3. Train-Test Split
# ==========================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


# ==========================================
# 4. Train Model
# ==========================================

model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)


# ==========================================
# 5. Make Predictions
# ==========================================

y_pred = model.predict(X_test)


# ==========================================
# 6. Calculate Evaluation Metrics
# ==========================================

mae = mean_absolute_error(y_test, y_pred)

rmse = np.sqrt(mean_squared_error(y_test, y_pred))

r2 = r2_score(y_test, y_pred)


# ==========================================
# 7. Display Results
# ==========================================

print("\n======================================")
print("     DEMAND MODEL EVALUATION")
print("======================================")

print(f"MAE  : {mae:.4f}")
print(f"RMSE : {rmse:.4f}")
print(f"R²   : {r2:.4f}")

print("======================================")