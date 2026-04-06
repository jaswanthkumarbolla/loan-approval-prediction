# Loan Approval Prediction System

A Machine Learning application that predicts whether a loan application will be approved based on applicant details. This project demonstrates data preprocessing, feature engineering, model training, evaluation, and deployment using a Streamlit web application.


## Features

- Predicts loan approval status (Approved / Rejected)
- Displays approval probability
- Provides basic decision insights 
- Shows top features influencing the model
- Interactive web interface using Streamlit

---

## Machine Learning Workflow

- Data Cleaning (handling missing values)
- Feature Engineering (TotalIncome, IncomeLoanRatio)
- Categorical Encoding (one-hot encoding)
- Model Training using Random Forest Classifier
- Handling class imbalance
- Model Evaluation (Accuracy, Confusion Matrix, F1-score)

---

## Tech Stack

- Python
- Pandas, NumPy
- Scikit-learn
- Streamlit

---

## How to Run

1. Clone the repository:
```bash
git clone https://github.com/jaswanthkumarbolla/loan-approval-prediction.git
cd loan-approval-prediction
```

2. Install dependencies:
```bash
pip install pandas numpy scikit-learn streamlit
```

3. Run the application:
```bash
streamlit run app.py
```
---


### Output

- Loan approval prediction (Approved / Rejected)  
- Probability score of approval  
- Key factors influencing the decision  
- Top features used by the model  
