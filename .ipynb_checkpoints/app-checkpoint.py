import streamlit as st
import pickle
import numpy as np
import json
import os
import pandas as pd

st.set_page_config(
    page_title="Loan Predictor",
    page_icon="💰",
    layout="centered"
)

st.markdown("""
    <style>
    .main {
        background-color: #0E1117;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        font-size: 18px;
        border-radius: 10px;
        padding: 10px 20px;
    }
    </style>
""", unsafe_allow_html=True)

# loading files
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

model = pickle.load(open(os.path.join(BASE_DIR, "loan_model.pkl"), 'rb'))

with open(os.path.join(BASE_DIR, "columns.json"), "r") as f:
    columns = json.load(f)

st.title("Loan Approval Prediction System")
st.write("Fill the details below to check loan approval status")
# inputs

col1, col2 = st.columns(2)

with col1:
    Gender = st.selectbox("Gender", ["Male", "Female"])
    Married = st.selectbox("Married", ["Yes", "No"])
    Dependents = st.selectbox("Dependents", ["0", "1", "2", "3+"])
    Education = st.selectbox("Education", ["Graduate", "Not Graduate"])
    Self_Employed = st.selectbox("Self Employed", ["Yes", "No"])

with col2:
    ApplicantIncome = st.number_input("Applicant Income", min_value=0.0)
    CoapplicantIncome = st.number_input("Coapplicant Income", min_value=0.0)
    LoanAmount = st.number_input("Loan Amount", min_value=0.0)
    Loan_Amount_Term = st.number_input("Loan Term", min_value=0.0)
    Credit_History = st.selectbox("Credit History", [1, 0])
    Property_Area = st.selectbox("Property Area", ["Urban", "Semiurban", "Rural"])

TotalIncome = ApplicantIncome + CoapplicantIncome
IncomeLoanRatio = TotalIncome / LoanAmount if LoanAmount != 0 else 0

input_dict = {
    'ApplicantIncome': ApplicantIncome,
    'CoapplicantIncome': CoapplicantIncome,
    'LoanAmount': LoanAmount,
    'Loan_Amount_Term': Loan_Amount_Term,
    'Credit_History': Credit_History,
    'TotalIncome': TotalIncome,
    'IncomeLoanRatio': IncomeLoanRatio,
}

input_df = pd.DataFrame([input_dict])

# Add categorical columns manually
input_df['Gender_Male'] = 1 if Gender == "Male" else 0
input_df['Married_Yes'] = 1 if Married == "Yes" else 0
input_df['Education_Not Graduate'] = 1 if Education == "Not Graduate" else 0
input_df['Self_Employed_Yes'] = 1 if Self_Employed == "Yes" else 0

# Dependents encoding
input_df['Dependents_1'] = 1 if Dependents == "1" else 0
input_df['Dependents_2'] = 1 if Dependents == "2" else 0
input_df['Dependents_3+'] = 1 if Dependents == "3+" else 0

# Property area encoding
input_df['Property_Area_Semiurban'] = 1 if Property_Area == "Semiurban" else 0
input_df['Property_Area_Urban'] = 1 if Property_Area == "Urban" else 0

input_df = input_df.reindex(columns=columns, fill_value=0)

if st.button("Predict Loan Status"):

    prediction = model.predict(input_df)
    probability = model.predict_proba(input_df)[0][1]

    if prediction[0] == 1:
        st.markdown("### ✅ Loan Approved")
        st.success("This applicant is likely eligible for the loan.")
    else:
        st.markdown("### ❌ Loan Rejected")
        st.error("This applicant is likely not eligible for the loan.")

    st.write(f" Approval Probability: {probability:.2f}")