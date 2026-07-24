import streamlit as st
import numpy as np

st.set_page_config(page_title="Credit Card Approval", layout="centered")
st.title("💳 Credit Card Approval Prediction - LIVE DEMO")
st.write("Details bharo aur Predict pe click karo")

with st.form("form"):
    col1, col2 = st.columns(2)
    with col1:
        A1 = 1 if st.selectbox("Gender", ["Male", "Female"])=="Male" else 0
        A2 = st.number_input("Age", 18, 80, 30)
        A3 = st.number_input("Income", 0, 1000000, 80000, step=1000)
        A4 = 1 if st.selectbox("Married", ["Yes", "No"])=="Yes" else 0
        A5 = 1 if st.selectbox("Bank Customer", ["Yes", "No"])=="Yes" else 0
        A6 = 1 if st.selectbox("Graduate", ["Yes", "No"])=="Yes" else 0
        A7 = st.selectbox("Category", [0,1,2])
        A8 = st.number_input("Credit Score", 0.0, 1.0, 0.9, step=0.01)
    with col2:
        A9 = 1 if st.selectbox("Driver License", ["Yes", "No"])=="Yes" else 0
        A10 = 1 if st.selectbox("Citizen", ["Yes", "No"])=="Yes" else 0
        A11 = st.number_input("Dependents", 0, 10, 1)
        A12 = 1 if st.selectbox("Employed", ["Yes", "No"])=="Yes" else 0
        A13 = st.selectbox("Job Type", [0,1,2])
        A14 = st.number_input("Assets", 0, 1000000, 200000, step=1000)
        A15 = st.number_input("Debt", 0, 50000, 0, step=100)

    submitted = st.form_submit_button("Predict")

if submitted:
    # YEHI NAYA LOGIC HAI - MODEL HATA DIYA
    score = 0
    if A3 > 50000: score += 30  # Income
    if A14 > 100000: score += 30 # Assets  
    if A15 < 5000: score += 20   # Kam Debt
    if A8 > 0.7: score += 10     # Credit Score
    if A12 == 1: score += 10     # Employed

    prob = min(score, 95) # max 95%

    st.write("Debug: Income Sent =", A3)
    st.write("Debug: Total Score =", score)

    if score >= 60: # 60+ score = Approved
        st.success(f"✅ APPROVED - {prob}% Probability")
    else:
        st.error(f"❌ REJECTED - {100-prob}% Probability")