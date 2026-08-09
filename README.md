# 🚀 DemandIQ — AI-Powered Demand & Inventory Intelligence

An end-to-end **AI-powered Demand, Inventory, Product Recommendation & Visual Space Intelligence System** that combines **Machine Learning, Generative AI, RAG, Computer Vision, and What-If Analysis** to help businesses make smarter product and inventory decisions.

---

# 📌 Project Overview

**DemandIQ** is an intelligent business decision-support platform designed to predict product demand, identify inventory risks, recommend products, and provide AI-powered business insights.

The system combines:

* 📈 Machine Learning for demand prediction
* 📦 Inventory intelligence and stock-risk analysis
* 🛍️ Product recommendation
* 🤖 Generative AI business assistant
* 📚 RAG-based knowledge retrieval
* 🧠 LangChain / LangGraph
* 🔎 Vector database for semantic search
* 🖼️ AI-powered image-based space analysis
* 💡 What-if business analysis
* ⚡ FastAPI backend
* 📊 Power BI analytics
* ☁️ Cloud-ready deployment

The goal is to move from simply **predicting what will happen** to helping businesses understand **why it happens and what action should be taken**.

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
* Difficulty analyzing product documentation
* Limited decision support for business users
* No intelligent way to analyze a customer's room/space and recommend suitable products

Therefore, DemandIQ combines **ML + GenAI + RAG + Computer Vision** into a single intelligent platform.

---

# 🎯 Objective

The main objective of DemandIQ is to develop an intelligent AI system that can:

1. Predict future product demand
2. Identify stock-out and overstock risks
3. Recommend relevant products
4. Explain ML predictions using Generative AI
5. Retrieve information from business documents using RAG
6. Perform what-if analysis
7. Analyze uploaded room/space images
8. Suggest suitable products for the detected space
9. Provide personalized product recommendations
10. Provide actionable business insights through an AI assistant

---

# ⭐ Why DemandIQ?

Most traditional ML projects stop at:

> **"Here is the prediction."**

DemandIQ goes one step further:

> **"Here is the prediction, here is why it happened, here is the relevant business knowledge, and here is what you should consider doing."**

This makes DemandIQ a **decision-support system rather than only a prediction model**.

The combination of:

**ML + GenAI + RAG + Computer Vision + Recommendation System + What-If Analysis**

makes the project significantly more practical for real-world business applications.

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
* Inventory level
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
Product: P001

Current Inventory: 700 units
Predicted Demand: 1,250 units
Stock-Out Risk: HIGH

Recommendation:
Consider replenishing inventory before the expected demand period.
```

---

# 3️⃣ Overstock Detection

DemandIQ can identify products where inventory may significantly exceed expected demand.

Example:

```text
Product: P023

Current Inventory: 2,500 units
Expected Demand: 900 units

Risk:
Potential Overstock

Recommendation:
Consider reducing future procurement or using promotional strategies.
```

---

# 4️⃣ Product Recommendation Engine

The system recommends products based on:

* Product similarity
* Product category
* Customer requirements
* Historical purchasing patterns
* Product attributes
* User preferences

Example:

```text
User Product:
Office Chair A

Recommended:
1. Ergonomic Chair B
2. Adjustable Desk C
3. Lumbar Support D
```

---

# 5️⃣ 🖼️ AI-Powered Visual Space Recommendation

One of the advanced features of DemandIQ is **image-based product recommendation**.

The customer can upload an image of their:

* Room
* Office
* Workspace
* Living area
* Bedroom
* Other usable spaces

The AI analyzes the image and understands the available environment.

### Example

User uploads:

```text
Room Image
      ↓
Computer Vision / Vision LLM
      ↓
Detects:
- Room type
- Available space
- Existing furniture
- Approximate layout
- Style/context
      ↓
Recommendation Engine
      ↓
Suitable Product Suggestions
```

The system can then suggest products that may fit the space.

Example:

```text
Detected Space:
Modern Office

Suggested Products:

✓ Ergonomic Office Chair
✓ Compact Work Desk
✓ Storage Cabinet
✓ Meeting Table
✓ Desk Lamp
```

The GenAI layer can explain the recommendation:

> "This compact desk is recommended because the uploaded workspace appears to have limited floor space. Its dimensions and design are better suited for the available area."

---

# 6️⃣ 🤖 GenAI Business Assistant

DemandIQ includes a conversational AI assistant that allows business users to ask questions about products, inventory, predictions, and business policies.

Example:

```text
User:

Which products are at high stock-out risk next month?
```

The system combines:

**ML Prediction + Business Data + RAG Knowledge**

and generates an explanation.

Example response:

```text
Product P001 has a high stock-out risk.

Predicted demand:
1,250 units

Current inventory:
700 units

Lead time:
20 days

The system recommends reviewing replenishment
requirements before the expected demand period.
```

---

# 7️⃣ 📚 RAG-Based Knowledge Assistant

DemandIQ can use **Retrieval-Augmented Generation (RAG)** to retrieve relevant information from business documents.

Possible knowledge sources:

* Product catalogs
* Product specifications
* Inventory policies
* Supplier information
* Business reports
* Product manuals
* Demand planning guidelines
* Return policies
* Procurement guidelines

### RAG Workflow

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
Semantic Retrieval
       ↓
Relevant Context
       ↓
LLM
       ↓
Grounded Answer
```

This helps reduce hallucinations and allows the assistant to answer questions using relevant business knowledge.

---

# 8️⃣ 🔥 What-If Analysis

DemandIQ allows users to explore possible business scenarios.

Example:

```text
User:

What happens if we increase the product price by 10%?
```

The system modifies the relevant input features and sends them through the ML model.

Example output:

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

The GenAI assistant can then explain the result and provide a business recommendation.

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
            │      Space Understanding    │
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

# 🔄 Complete Workflow

```text
Sales / Inventory / Product Data
              ↓
         Data Cleaning
              ↓
       Feature Engineering
              ↓
        Machine Learning
              ↓
 ┌────────────┼─────────────┐
 ↓            ↓             ↓
Demand     Stock Risk    Product
Prediction  Prediction   Recommendation
 ↓            ↓             ↓
 └────────────┼─────────────┘
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
* Regression Models
* Classification Models
* Recommendation Algorithms

## 🧠 Generative AI

* Large Language Models (LLMs)
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
* Vision-based AI / Vision LLM

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
* Cloud-ready architecture

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

Example endpoint:

```text
GET /predict-demand/{product_id}
```

Example:

```text
GET /predict-demand/P001
```

The API returns the predicted demand for the selected product.

Future APIs can include:

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

# 📊 Dashboard

Power BI can be used to visualize:

* Historical sales
* Predicted demand
* Inventory levels
* Stock-out risk
* Overstock products
* Product performance
* Regional demand
* Revenue trends
* Recommendation insights

---

# 💡 Example Business Questions

DemandIQ can help answer questions such as:

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

# 🌟 What Makes This Project Different?

DemandIQ combines multiple AI capabilities into one system:

```text
                 DemandIQ
                    │
       ┌────────────┼────────────┐
       ↓            ↓            ↓
   Predict       Recommend     Explain
       │            │            │
       ↓            ↓            ↓
     ML Model   Recommendation   GenAI
                    │            │
                    ↓            ↓
              Image Analysis    RAG
                    │            │
                    └─────┬──────┘
                          ↓
                   Business Decision
```

Instead of building separate ML, recommendation, and GenAI demos, DemandIQ integrates them into a single business-oriented platform.

---

# 🏆 Why This Is Valuable for Businesses

The system can help businesses:

* Reduce stock-outs
* Reduce excess inventory
* Improve demand planning
* Improve product discovery
* Personalize recommendations
* Reduce manual analysis
* Provide explainable AI insights
* Improve decision-making
* Enable AI-assisted business operations

---

# 🎯 Real-World Applications

* Retail analytics
* E-commerce
* Supply chain management
* Inventory optimization
* Product recommendation
* Demand forecasting
* Smart shopping assistants
* Workspace planning
* Interior/product recommendations
* Business intelligence

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
* Model monitoring and LLMOps

---

# ☁️ Deployment

The application is designed to be deployed as a cloud-based AI service.

Possible deployment architecture:

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
RAG Pipeline
 ↓
Vector Database
 ↓
LLM
 ↓
AI Response
```

### Deployment URL

**Live Demo:** Coming Soon

**API Documentation:** Coming Soon

**Power BI Dashboard:** Coming Soon

---

# 📈 Project Status

### Currently Completed

* [x] Dataset generation
* [x] Sales data processing
* [x] Inventory data processing
* [x] Exploratory Data Analysis
* [x] Demand prediction model
* [x] Product recommendation system
* [x] Inventory recommendation logic
* [x] Trained ML model
* [x] FastAPI backend
* [x] API endpoint for demand prediction
* [ ] GenAI assistant
* [ ] RAG pipeline
* [ ] Vector database integration
* [ ] Image-based space analysis
* [ ] Visual product recommendation
* [ ] What-if analysis
* [ ] Power BI dashboard
* [ ] Docker deployment
* [ ] AWS/Azure deployment

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

Create a `.env` file for sensitive credentials such as:

```text
OPENAI_API_KEY=
PINECONE_API_KEY=
```

**Never commit API keys or secrets to GitHub.**

---

# 📌 Key Learning Outcomes

Through DemandIQ, the project demonstrates practical experience in:

* Machine Learning
* Regression
* Classification
* Recommendation Systems
* Feature Engineering
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

This project demonstrates the integration of **Machine Learning, Generative AI, Recommendation Systems, Computer Vision, and Business Intelligence** into an end-to-end intelligent decision-support platform.




