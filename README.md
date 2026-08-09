# 🚀 DemandIQ — AI-Powered Demand & Inventory Intelligence

An end-to-end **AI-powered Demand, Inventory, Product Recommendation & Visual Space Intelligence System** combining **Machine Learning, Generative AI, RAG, Computer Vision, Recommendation Systems, and What-If Analysis** to support smarter business decisions.

---

# 📌 Project Overview

**DemandIQ** is an intelligent business decision-support platform designed to predict product demand, identify inventory risks, recommend relevant products, analyze uploaded space images, and provide AI-powered business insights.

The system follows the principle:

> **ML predicts what is likely to happen, while GenAI explains why it is happening and recommends what the business should consider doing.**

The platform combines:

* 📈 Demand Forecasting
* 📦 Inventory Intelligence
* ⚠️ Stock-Out Risk Prediction
* 📊 Overstock Detection
* 🛍️ Product Recommendation
* 🤖 Generative AI Business Assistant
* 📚 RAG-based Knowledge Retrieval
* 🧠 LangChain / LangGraph
* 🔎 Vector Database
* 🖼️ Image-Based Space Analysis
* 💡 What-If Analysis
* ⚡ FastAPI
* 📊 Power BI
* ☁️ Cloud-ready Deployment

---

# 🚨 Problem Statement

Traditional demand and inventory systems mainly focus on historical data and numerical forecasting.

Businesses still face challenges such as:

* Unpredictable product demand
* Stock-out situations
* Overstocking
* Difficulty understanding ML predictions
* Manual product selection
* Lack of personalized recommendations
* Difficulty accessing business knowledge
* Limited decision support
* No intelligent image-based product recommendation

DemandIQ addresses these challenges by combining **ML + GenAI + RAG + Recommendation Systems + Computer Vision** into a single intelligent platform.

---

# 🎯 Objective

The primary objective of DemandIQ is to build an intelligent AI-powered system that can:

1. Predict future product demand
2. Identify stock-out risk
3. Detect potential overstock situations
4. Recommend relevant products
5. Explain ML predictions using Generative AI
6. Retrieve relevant information using RAG
7. Perform what-if business analysis
8. Analyze uploaded room/workspace images
9. Suggest suitable products for a detected space
10. Provide actionable business recommendations

---

# ⭐ Why DemandIQ?

Most traditional ML projects stop at:

> **"Here is the prediction."**

DemandIQ goes one step further:

> **"Here is the prediction, why it happened, the relevant business knowledge, and what action should be considered."**

The project integrates:

```text
Machine Learning
       +
Recommendation Systems
       +
Generative AI
       +
RAG
       +
Vector Database
       +
Computer Vision
       +
What-If Analysis
       =
AI-Powered Business Decision Support
```

This makes the project more than a simple prediction model. It is designed as an **end-to-end intelligent decision-support platform**.

---

# 🧠 Core AI Capabilities

## 1️⃣ Demand Prediction

The ML model predicts future product demand using features such as:

* Historical sales
* Product information
* Region
* Price
* Discount
* Season
* Month
* Inventory
* Lead time
* Customer/order information

Example:

```text
Product ID: P001

Predicted Demand:
1,250 units

Forecast Period:
Next Month
```

---

# 2️⃣ Stock-Out Risk Prediction

The system analyzes predicted demand, current inventory, lead time, and historical patterns to identify products that may run out of stock.

Example:

```text
Current Inventory: 700 units
Predicted Demand: 1,250 units

Risk:
HIGH STOCK-OUT RISK

Recommendation:
Review replenishment requirements before the
expected demand period.
```

---

# 3️⃣ Overstock Detection

The system identifies products where inventory may significantly exceed expected demand.

Example:

```text
Current Inventory: 2,500 units
Expected Demand: 900 units

Risk:
Potential Overstock

Recommendation:
Review future procurement and promotional strategies.
```

---

# 4️⃣ Product Recommendation

The recommendation engine suggests products using:

* Product similarity
* Product category
* Product attributes
* Customer preferences
* Historical purchasing patterns
* TF-IDF/product feature similarity

Example:

```text
Input Product:
Product A

Recommended Products:

1. Product B
2. Product C
3. Product D
```

---

# 5️⃣ 🖼️ AI-Powered Visual Space Recommendation

DemandIQ can allow customers to upload an image of their:

* Room
* Office
* Workspace
* Living area
* Bedroom
* Other usable spaces

The system analyzes the image and identifies relevant visual information about the space.

### Workflow

```text
Uploaded Image
      ↓
Computer Vision / Vision LLM
      ↓
Space & Object Understanding
      ↓
Available Space / Style Analysis
      ↓
Product Recommendation Engine
      ↓
Suitable Product Suggestions
```

Example:

```text
Detected Space:
Modern Workspace

Suggested Products:

✓ Ergonomic Chair
✓ Compact Work Desk
✓ Storage Cabinet
✓ Desk Lamp
```

The GenAI assistant can also explain the recommendation:

> "The compact desk is recommended because the available workspace appears limited and the product is better suited to the detected layout."

---

# 6️⃣ 🤖 GenAI Business Assistant

The GenAI assistant allows users to ask questions about demand, inventory, products, and business policies.

Example:

```text
User:

Which products are at high stock-out risk next month?
```

The system combines:

```text
ML Predictions
      +
Business Data
      +
RAG Knowledge
      ↓
Generative AI
      ↓
Business Explanation
```

Example response:

```text
Product P001 has a high stock-out risk.

Predicted Demand: 1,250 units
Current Inventory: 700 units
Lead Time: 20 days

Recommendation:
Review replenishment requirements before
the expected demand period.
```

---

# 7️⃣ 📚 RAG-Based Knowledge Assistant

DemandIQ can retrieve information from business documents such as:

* Product catalogs
* Product specifications
* Inventory policies
* Supplier information
* Business reports
* Product manuals
* Demand-planning guidelines
* Procurement guidelines
* Return policies

### RAG Pipeline

```text
Business Documents
        ↓
Document Loading
        ↓
Text Chunking
        ↓
Embeddings
        ↓
Vector Database
        ↓
Semantic Search
        ↓
Relevant Context
        ↓
LLM
        ↓
Grounded Response
```

RAG helps the LLM generate responses based on relevant business information rather than relying only on its general knowledge.

---

# 8️⃣ 🔥 What-If Analysis

DemandIQ allows users to simulate possible business scenarios.

Example:

```text
User:

What happens if we increase the product price by 10%?
```

The system modifies the relevant input and runs the ML model again.

Example:

```text
Current Price:
₹10,000

Current Expected Demand:
1,250 units

Price Increase:
+10%

New Expected Demand:
1,080 units

Estimated Demand Change:
-13.6%
```

GenAI can then explain the result and provide a business recommendation.

---

# 📊 Machine Learning Model Evaluation

Model performance is evaluated using appropriate metrics based on the ML task.

## 📈 Demand Prediction — Regression Metrics

Since demand prediction is a **regression problem**, the following metrics are used:

### MAE — Mean Absolute Error

Measures the average absolute difference between actual and predicted demand.

```text
MAE = average(|Actual - Predicted|)
```

Lower MAE indicates better performance.

### MSE — Mean Squared Error

Penalizes larger prediction errors more heavily.

```text
MSE = average((Actual - Predicted)²)
```

Lower MSE is better.

### RMSE — Root Mean Squared Error

RMSE is the square root of MSE and represents the error in the same unit as demand.

```text
RMSE = √MSE
```

Lower RMSE indicates better performance.

### R² Score

Measures how much variation in demand is explained by the model.

```text
R² = 1 - (SSres / SStotal)
```

A value closer to **1.0** indicates stronger predictive performance.

### MAPE — Mean Absolute Percentage Error

Measures prediction error as a percentage.

```text
MAPE = mean(|Actual - Predicted| / Actual) × 100
```

Lower MAPE is better.

---

# 🏆 Model Performance

Add the actual values obtained from the trained model here:

| Metric   |             Result |
| -------- | -----------------: |
| MAE      |  **[Your Result]** |
| MSE      |  **[Your Result]** |
| RMSE     |  **[Your Result]** |
| R² Score |  **[Your Result]** |
| MAPE     | **[Your Result]%** |

> **Note:** The values should be updated with the actual evaluation results from the final trained model.

---

# 📊 Classification Evaluation

If stock-out/overstock prediction is implemented as a classification problem, the system can be evaluated using:

### Accuracy

Percentage of correctly classified observations.

### Precision

Measures how many predicted positive cases were actually positive.

### Recall

Measures how many actual positive cases were successfully detected.

### F1-Score

Harmonic mean of precision and recall.

### Confusion Matrix

Used to visualize:

```text
                 Predicted
               Positive Negative

Actual Positive    TP       FN

Actual Negative    FP       TN
```

For stock-out detection, **recall is particularly important** because missing an actual stock-out can have a significant business impact.

---

# 📈 Recommendation System Evaluation

The recommendation engine can be evaluated using:

* Precision@K
* Recall@K
* Hit Rate@K
* Recommendation coverage
* Similarity score

Example:

```text
Top-K Recommendations

K = 5

Precision@5
Recall@5
Hit Rate@5
```

These metrics help determine whether the recommended products are relevant to users.

---

# 🧪 Model Validation

The ML pipeline can include:

* Train/Test Split
* Cross-Validation
* Feature Engineering
* Hyperparameter Tuning
* Error Analysis
* Residual Analysis
* Model Comparison

Possible models:

```text
Baseline Model
      ↓
Linear Regression
      ↓
Random Forest
      ↓
Gradient Boosting / XGBoost
      ↓
Best Performing Model
```

The final model is selected based on evaluation metrics rather than simply choosing the most complex algorithm.

---

# 🏗️ System Architecture

```text
                         USER
                           │
            ┌──────────────┼──────────────┐
            │              │              │
            ▼              ▼              ▼
       Web Interface   Image Upload   AI Assistant
            │              │              │
            │              ▼              │
            │       Computer Vision       │
            │              │              │
            │              ▼              │
            │       Space Understanding   │
            │              │              │
            └──────────────┼──────────────┘
                           ▼
                    FastAPI Backend
                           │
             ┌─────────────┼─────────────┐
             │             │             │
             ▼             ▼             ▼
       ML Prediction   Recommendation   GenAI
             │             │             │
             │             │             ▼
             │             │          RAG Pipeline
             │             │             │
             │             │       Embeddings
             │             │             │
             │             │       Vector Database
             │             │             │
             │             │             ▼
             │             │             LLM
             │             │             │
             └─────────────┼─────────────┘
                           ▼
                  Business AI Insights
                           │
             ┌─────────────┴─────────────┐
             ▼                           ▼
        Power BI                    User Dashboard
```

---

# 🔄 Complete Project Workflow

```text
Sales / Inventory / Product Data
              ↓
         Data Cleaning
              ↓
       Feature Engineering
              ↓
        Exploratory Analysis
              ↓
        Model Training
              ↓
       Model Evaluation
              ↓
 ┌────────────┼──────────────┐
 ↓            ↓              ↓
Demand     Stock Risk     Product
Prediction  Prediction   Recommendation
 ↓            ↓              ↓
 └────────────┼──────────────┘
              ↓
       Prediction Results
              ↓
       FastAPI Backend
              ↓
 ┌────────────┼───────────────────┐
 ↓            ↓                   ↓
Power BI    GenAI Assistant   Image Analysis
             ↓                   ↓
            RAG              Product Matching
             ↓                   ↓
       Vector Database       Recommendations
             ↓
            LLM
             ↓
      Business Explanation
             ↓
     Actionable Recommendation
```

---

# 🧰 Technologies Used

## 🐍 Programming & Data

* Python
* Pandas
* NumPy
* SQL

## 🤖 Machine Learning

* Scikit-learn
* XGBoost
* Regression
* Classification
* Recommendation Systems
* Feature Engineering
* Model Evaluation

## 🧠 Generative AI

* Large Language Models
* RAG
* LangChain
* LangGraph
* Prompt Engineering
* Embeddings

## 🔎 Vector Database

* Pinecone
* FAISS

## 👁️ Computer Vision

* OpenCV
* Vision Models / Vision LLM

## ⚡ Backend

* FastAPI
* REST APIs

## 📊 Visualization

* Power BI
* Matplotlib
* Seaborn

## 🗄️ Database

* SQL
* MongoDB

## 🚀 Deployment

* Docker
* AWS / Azure

---

# 📁 Project Structure

```text
DemandIQ/
│
├── app/
│   ├── api.py
│   └── ...
│
├── data/
│   └── raw/
│       ├── inventory.csv
│       ├── products.csv
│       └── sales.csv
│
├── models/
│   ├── demand_prediction_model.pkl
│   ├── product_similarity_matrix.npy
│   └── product_tfidf_vectorizer.pkl
│
├── notebooks/
│   └── 01_eda.ipynb
│
├── src/
│   ├── data/
│   │   ├── eda.py
│   │   ├── generate_dataset.py
│   │   ├── generate_inventory.py
│   │   └── generate_sales.py
│   │
│   └── ml/
│       ├── demand_prediction.py
│       ├── inventory_recommendation.py
│       └── product_recommendation.py
│
├── requirements.txt
├── .gitignore
└── README.md
```

---

# 🔌 API Layer

The backend is developed using **FastAPI**.

Current endpoint:

```text
GET /predict-demand/{product_id}
```

Example:

```text
GET /predict-demand/P001
```

Future endpoints:

```text
/predict-demand/{product_id}
/stock-risk/{product_id}
/recommend-products/{product_id}
/inventory-insights
/analyze-image
/ask-ai
/what-if
```

---

# 📊 Power BI Dashboard

The Power BI layer can provide business-level visualization of:

* Historical sales
* Predicted demand
* Actual vs predicted demand
* Inventory levels
* Stock-out risk
* Overstock products
* Product performance
* Regional demand
* Revenue trends
* Recommendation insights
* Model performance

---

# 💡 Example Business Questions

### Demand

> What will be the demand for Product P001 next month?

### Inventory

> Which products are likely to run out of stock?

### Overstock

> Which products currently have excess inventory?

### Recommendation

> Which products should be recommended to this customer?

### Visual Intelligence

> What products would suit this uploaded room?

### What-If

> What happens if we increase the price by 10%?

### GenAI

> Why is Product P001 at high stock-out risk?

### RAG

> What does the inventory policy recommend for products with high demand variability?

---

# 🌟 What Makes DemandIQ Different?

DemandIQ integrates multiple AI capabilities into one platform:

```text
             DemandIQ
                 │
     ┌───────────┼────────────┐
     ↓           ↓            ↓
  Predict     Recommend    Explain
     │           │            │
     ↓           ↓            ↓
    ML       Recommendation  GenAI
                 │            │
                 ↓            ↓
            Image Analysis    RAG
                 │            │
                 └──────┬─────┘
                        ↓
                Business Decision
```

The system therefore connects:

**Prediction → Explanation → Recommendation → Action**

instead of providing only a numerical prediction.

---

# 🏆 Business Value

DemandIQ can help businesses:

* Reduce stock-outs
* Reduce excess inventory
* Improve demand planning
* Improve product discovery
* Personalize recommendations
* Reduce manual analysis
* Understand ML predictions
* Retrieve business knowledge quickly
* Support data-driven decisions
* Improve customer experience

---

# 🌍 Real-World Applications

* Retail analytics
* E-commerce
* Supply chain management
* Inventory optimization
* Demand forecasting
* Product recommendation
* Smart shopping assistants
* Workspace planning
* Visual product recommendation
* Business intelligence

---

# 🚀 Current Project Status

### Completed

* [x] Dataset generation
* [x] Sales data processing
* [x] Inventory data processing
* [x] Exploratory Data Analysis
* [x] Demand prediction model
* [x] Product recommendation system
* [x] Inventory recommendation logic
* [x] Trained ML model
* [x] FastAPI backend
* [x] Demand prediction API
* [x] Model evaluation framework
* [x] GitHub project setup

### In Progress / Planned

* [ ] Advanced GenAI assistant
* [ ] RAG pipeline
* [ ] Pinecone/FAISS integration
* [ ] Image-based space analysis
* [ ] Visual product recommendation
* [ ] What-if analysis
* [ ] Power BI dashboard
* [ ] Docker deployment
* [ ] AWS/Azure deployment
* [ ] LLMOps and monitoring

---

# 🚀 Getting Started

## 1. Clone the Repository

```bash
git clone https://github.com/sneha44536/-DemandIQ-AI-Powered-Demand-Inventory-Intelligence.git
```

## 2. Navigate to the Project

```bash
cd -DemandIQ-AI-Powered-Demand-Inventory-Intelligence
```

## 3. Create Virtual Environment

```bash
python -m venv .venv
```

## 4. Activate Environment

### Windows

```bash
.venv\Scripts\activate
```

## 5. Install Dependencies

```bash
pip install -r requirements.txt
```

## 6. Run FastAPI

```bash
uvicorn app.api:app --reload
```

## 7. Open API Documentation

```text
http://127.0.0.1:8000/docs
```

---

# 🔐 Environment Variables

Create a `.env` file for sensitive credentials:

```text
OPENAI_API_KEY=
PINECONE_API_KEY=
```

Never commit API keys, passwords, or other secrets to GitHub.

---

# ☁️ Deployment

The final architecture is designed for cloud deployment:

```text
User
 ↓
Frontend
 ↓
AWS / Azure
 ↓
FastAPI
 ↓
ML Models
 ↓
Recommendation Engine
 ↓
RAG Pipeline
 ↓
Vector Database
 ↓
LLM
 ↓
AI Business Response
```

### Deployment URLs

**Live Demo:** Coming Soon

**API:** Coming Soon

**Swagger Documentation:** Coming Soon

**Power BI Dashboard:** Coming Soon

---

# 🔮 Future Improvements

* Fine-tuned domain-specific LLM
* Advanced multimodal AI
* Real-time inventory monitoring
* Customer personalization
* Voice-based AI assistant
* Agentic AI workflow
* Automated procurement recommendations
* Supplier optimization
* Advanced forecasting models
* Real-time streaming data
* AWS production deployment
* CI/CD pipeline
* Model monitoring
* LLMOps
* AI-powered visual room redesign
* Personalized spatial product recommendations

---

# 📚 Key Learning Outcomes

This project demonstrates practical experience in:

* Machine Learning
* Regression
* Classification
* Recommendation Systems
* Feature Engineering
* Model Evaluation
* Data Analysis
* FastAPI
* REST APIs
* Generative AI
* RAG
* Vector Databases
* LangChain
* LangGraph
* Embeddings
* Computer Vision
* Multimodal AI
* Power BI
* Docker
* Cloud Deployment

---

# 👩‍💻 Author

**Sneha Pise**

Data Science | Machine Learning | Generative AI | RAG

DemandIQ demonstrates the integration of **Machine Learning, Generative AI, Recommendation Systems, Computer Vision, and Business Intelligence** into an end-to-end intelligent decision-support platform.
