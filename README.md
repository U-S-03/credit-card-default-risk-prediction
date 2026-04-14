# 📄✏ Credit Card Default Risk Prediction Project
### 📌 Overview
- This project builds a Machine Learning system to predict whether a credit card user is likely to default on their payment.
- It follows an end-to-end ML pipeline, from data preprocessing to deployment, making it suitable for real-world financial risk analysis.

### 🎯 Problem Statement
- Credit card defaults cause significant financial losses for banks and financial institutions.
- The goal of this project is to identify high-risk customers in advance, enabling better decision-making and risk mitigation.

### 📊 Dataset
- Taken from Kaggle and stored in mongodb
- The dataset contains financial and demographic information of credit card users:
  - Credit limit (LIMIT_BAL)
  - Payment history (PAY_*)
  - Bill amounts (BILL_AMT*)
  - Previous payments (PAY_AMT*)

### 🎯 Target Variable:

- default_payment_next_month
  - 0 -> No Default
  - 1 -> Default

### ⚙️ ML Pipeline:
- Data Cleaning & Preprocessing
- Exploratory Data Analysis (EDA)
- Feature Engineering
- Model Training
- Model Evaluation
- Prediction System

#### 📈 Evaluation Metrics
- Accuracy
- Precision
- Recall
- F1 Score

***⚠️ Recall is prioritized because failing to identify a defaulter can lead to financial loss.***


### 💿 Installing
1. Environment setup.
```
conda create --prefix venv python==3.8 -y
```
```
conda activate venv/
````
2. Install Requirements and setup
```
pip install -r requirements.txt
```
5. Run Application
```
python app.py
```

#### 🔧 Built with
- flask
- Python 3.8
- Machine learning
- Scikit learn
- 🏦 Industrial Use Cases
