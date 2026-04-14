# 📄✏ Credit Card Default Risk Prediction Project
**Brief:** The **Credit Card Default Risk Prediction Project** is a comprehensive endeavor aimed at developing systems and strategies to detect and prevent fraudulent activities related to credit card usage. It involves utilizing advanced technologies such as data analytics, machine learning, and artificial intelligence to analyze transactional data, identify suspicious patterns, and flag potentially fraudulent transactions. The project's goal is to safeguard consumers' financial information, minimize financial losses for individuals and businesses, and maintain the integrity of the global financial system.

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


💿 Installing
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

🔧 Built with
- flask
- Python 3.8
- Machine learning
- Scikit learn
- 🏦 Industrial Use Cases

