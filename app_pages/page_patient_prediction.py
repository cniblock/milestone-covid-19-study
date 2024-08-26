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
            prediction = model_pipeline.predict(input_data)[0]
            
            if prediction < 0.33:
                risk_level = "Low Risk"
            elif prediction < 0.66:
                risk_level = "Medium Risk"
            else:
                risk_level = "High Risk"
            
            st.write(f"Predicted Risk Level: {risk_level} ({prediction})")
        except Exception as e:
            st.error(f"An error occurred during prediction: {str(e)}")

def get_user_input():
    st.header("Patient Risk Prediction")
    
    age_bin = st.selectbox("Age", [
        '<30.0',
        '30.0 to 41.0',
        '41.0 to 48.0',
        '48.0 to 53.0',
        '53.0 to 58.0',
        '58.0 to 63.0',
        '63.0 to 68.0',
        '68.0 to 73.0',
        '73.0 to 80.0',
        '>80.0'
    ])
    
    pneumonia = st.selectbox("Pneumonia", ["Yes", "No"])
    intubed = st.selectbox("Intubed", ["Yes", "No"])
    icu = st.selectbox("ICU", ["Yes", "No"])

    age_map = {
        '<30.0': 0,
        '30.0 to 41.0': 1,
        '41.0 to 48.0': 2,
        '48.0 to 53.0': 3,
        '53.0 to 58.0': 4,
        '58.0 to 63.0': 5,
        '63.0 to 68.0': 6,
        '68.0 to 73.0': 7,
        '73.0 to 80.0': 8,
        '>80.0': 9
    }
    
    input_data = pd.DataFrame({
        'AGE': [age_map[age_bin]],
        'PNEUMONIA': [1 if pneumonia == "Yes" else 0],
        'INTUBED': [1 if intubed == "Yes" else 0],
        'ICU': [1 if icu == "Yes" else 0],
        'SEX': [0],
        'DIABETES': [0],
        'COPD': [0],
        'ASTHMA': [0],
        'INMSUPR': [0],
        'HIPERTENSION': [0],
        'OTHER_DISEASE': [0],
        'CARDIOVASCULAR': [0],
        'OBESITY': [0],
        'RENAL_CHRONIC': [0],
        'TOBACCO': [0]
    })

    return input_data