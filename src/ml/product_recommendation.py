import pandas as pd
import numpy as np
import os

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# ============================================================
# PROJECT PATHS
# ============================================================

BASE_DIR = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../..")
)

DATA_DIR = os.path.join(BASE_DIR, "data", "raw")


# ============================================================
# LOAD PRODUCTS
# ============================================================

products = pd.read_csv(
    os.path.join(DATA_DIR, "products.csv")
)

print("=" * 60)
print("AI FURNITURE PRODUCT RECOMMENDATION SYSTEM")
print("=" * 60)

print("\nProducts loaded successfully.")
print("Total products:", len(products))


# ============================================================
# CREATE PRODUCT FEATURES
# ============================================================

products["product_features"] = (
    products["category"].fillna("") + " " +
    products["material"].fillna("") + " " +
    products["style"].fillna("") + " " +
    products["color"].fillna("")
)


# ============================================================
# TF-IDF VECTORIZATION
# ============================================================

vectorizer = TfidfVectorizer(
    lowercase=True,
    stop_words="english"
)

feature_matrix = vectorizer.fit_transform(
    products["product_features"]
)


# ============================================================
# COSINE SIMILARITY
# ============================================================

similarity_matrix = cosine_similarity(
    feature_matrix
)


# ============================================================
# RECOMMENDATION FUNCTION
# ============================================================

def recommend_products(product_id, top_n=5):

    if product_id not in products["product_id"].values:
        print("Product ID not found.")
        return

    product_index = products[
        products["product_id"] == product_id
    ].index[0]

    similarity_scores = similarity_matrix[
        product_index
    ]

    similar_indices = (
        similarity_scores
        .argsort()[::-1]
    )

    similar_indices = [
        i for i in similar_indices
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

    print("\n" + "=" * 60)
    print(
        f"RECOMMENDATIONS FOR PRODUCT: {product_id}"
    )
    print("=" * 60)

    print(recommendations.to_string(index=False))


# ============================================================
# TEST RECOMMENDATION
# ============================================================

recommend_products("P001", top_n=5)
# ============================================================
# SAVE RECOMMENDATION MODEL
# ============================================================

MODEL_DIR = os.path.join(BASE_DIR, "models")

os.makedirs(MODEL_DIR, exist_ok=True)

np.save(
    os.path.join(
        MODEL_DIR,
        "product_similarity_matrix.npy"
    ),
    similarity_matrix
)

import joblib

joblib.dump(
    vectorizer,
    os.path.join(
        MODEL_DIR,
        "product_tfidf_vectorizer.pkl"
    )
)

print("\nRecommendation model saved successfully.")