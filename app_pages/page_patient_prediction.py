import streamlit as st
import pandas as pd
import joblib

def load_pipeline(base_path):
    return joblib.load(base_path)

def page_patient_prediction_body():
    input_data = get_user_input()

    if st.button("Run Predictive Analysis"):
        try:
            model_path = 'outputs/ml_pipeline/predict_severity/v1/regressor_pipeline.pkl'
            model_pipeline = load_pipeline(model_path)
            st.write("Input data shape:", input_data.shape)
            st.write("Input data columns:", input_data.columns.tolist())
            prediction = model_pipeline.predict(input_data)[0]
            st.write(f"Predicted Risk Level: {prediction}")
        except Exception as e:
            st.error(f"An error occurred during prediction: {str(e)}")

def get_user_input():
    st.header("Patient Risk Prediction")
    
    age = st.number_input("Age", min_value=0, max_value=120, value=30)
    pneumonia = st.selectbox("Pneumonia", ["Yes", "No"])
    intubed = st.selectbox("Intubed", ["Yes", "No"])
    icu = st.selectbox("ICU", ["Yes", "No"])

    input_data = pd.DataFrame({
        'AGE': [age],
        'PNEUMONIA': [1 if pneumonia == "Yes" else 0],
        'INTUBED': [1 if intubed == "Yes" else 0],
        'ICU': [1 if icu == "Yes" else 0]
    })

    return input_data