import streamlit as st
import pandas as pd
import joblib

model = joblib.load("fraud_detector.pkl")

st.write("Expected Features:", model.n_features_in_)
st.title("Credit Card Fraud Dection System")
st.write("Enter transaction details below:")

time = st.number_input("Time", value = 0.0)
amount = st.number_input("Amount", value = 0.0)
inputs = []

for i in range(1, 29):
    val = st.number_input(f"V{i}", value = 0.0)
    inputs.append(val)

if st.button("Predict"):
    data = [[time] + inputs + [amount]]
    st.write("Input Features:", len(data[0]))
    prediction = model.predict(data)

    if prediction[0] == 1:
        st.error("The transaction is fraudulent.")
    else:
        st.success("The transaction is legitimate.")