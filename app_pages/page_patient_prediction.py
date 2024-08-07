import streamlit as st
import numpy as np
import joblib

def page_patient_prediction_body():
    st.header("Patient Risk Prediction")

    age = st.number_input("Age", min_value=0, max_value=120, value=30)
    pneumonia = st.selectbox("Pneumonia", ["Yes", "No"])
    intubed = st.selectbox("Intubed", ["Yes", "No"])
    hypertension = st.selectbox("Hypertension", ["Yes", "No"])
    diabetes = st.selectbox("Diabetes", ["Yes", "No"])

    if st.button("Run Predictive Analysis"):
        prediction = predict_risk(age, pneumonia, intubed, hypertension, diabetes)
        st.write(f"Predicted Risk Level: {prediction}")

def predict_risk(age, pneumonia, intubed, hypertension, diabetes):
    model = joblib.load('outputs/ml_pipeline/predict_severity/v1/regressor_pipeline.pkl')

    input_data = np.array([[age,
                            1 if pneumonia == "Yes" else 0,
                            1 if intubed == "Yes" else 0,
                            1 if hypertension == "Yes" else 0,
                            1 if diabetes == "Yes" else 0]])
    
    return model.predict(input_data)[0]