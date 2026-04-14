# 📄✏ Credit Card Default Risk Prediction Project
### 📌 Overview
This project builds a Machine Learning system to predict whether a credit card user is likely to default on their payment.
It implements an end-to-end ML pipeline, from data preprocessing to deployment using Flask, making it suitable for real-world financial risk analysis.

### 🎯 Problem Statement
Credit card defaults cause significant financial losses for financial institutions.
The objective of this project is to identify high-risk customers in advance to support better decision-making and risk management.

### 📊 Dataset
Source: Kaggle
Stored in MongoDB
Features include:
Credit limit (LIMIT_BAL)
Payment history (PAY_*)
Bill amounts (BILL_AMT*)
Previous payments (PAY_AMT*)
🎯 Target Variable

### default_payment_next_month

|Value|	Meaning   |
|-----|--------   |
|0    |	No Default|
|1	  | Default   |

### ⚙️ ML Pipeline
Data Cleaning & Preprocessing
Exploratory Data Analysis (EDA)
Feature Engineering
Model Training
Model Evaluation
Prediction System (Flask Web App)

### 📈 Model & Results
Model Used: XGBoost Classifier
Accuracy: ~77%

Classification Report:
Precision, Recall, F1-score evaluated on test data

⚠️ Key Insight
The dataset is imbalanced, leading to lower recall for defaulters
Threshold tuning (0.5 → 0.3) was applied to improve recall

👉 This improves detection of high-risk customers

🧠 Important Learning
Accuracy alone is not sufficient for imbalanced datasets
Recall is critical in financial risk problems
Trade-off exists between precision and recall

🖥️ Application Flow
Train model (/train)
Upload CSV file
Model predicts default risk
Download prediction results

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
