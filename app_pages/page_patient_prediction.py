import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt

def load_pipeline(base_path):
    return joblib.load(base_path)

def page_patient_prediction_body():
    version = 'v1'
    model_path_reg = f'outputs/ml_pipeline/predict_severity/{version}/regressor_pipeline.pkl'
    model_pipeline_reg = load_pipeline(model_path_reg)

    input_data = get_user_input()

    if st.button("Run Predictive Analysis"):
        try:
            reg_prediction = model_pipeline_reg.predict(input_data)[0]

            if reg_prediction < 0.5:
                risk_level_reg = "Low Risk"
                risk_color_reg = "green"
            elif reg_prediction < 0.8:
                risk_level_reg = "Medium Risk"
                risk_color_reg = "orange"
            else:
                risk_level_reg = "High Risk"
                risk_color_reg = "red"

            st.markdown(f"**Predicted Risk Level:** <span style='color:{risk_color_reg};'>{risk_level_reg} ({reg_prediction:.2f})</span>", unsafe_allow_html=True)

        except Exception as e:
            st.error(f"An error occurred during prediction: {str(e)}")


def get_user_input():
    st.header("Patient Risk Prediction")

    age = st.number_input("Age", min_value=0, max_value=120, value=20)
    intubed = st.selectbox("Intubed", ["Yes", "No"])
    icu = st.selectbox("ICU", ["Yes", "No"])
    pneumonia = st.selectbox("Pneumonia", ["Yes", "No"])
    hypertension = st.selectbox("Hypertension", ["Yes", "No"])
    diabetes = st.selectbox("Diabetes", ["Yes", "No"])
    obesity = st.selectbox("Obesity", ["Yes", "No"])

    input_data = pd.DataFrame({
        'AGE': [age],
        'INTUBED': [1 if intubed == "Yes" else 0],
        'ICU': [1 if icu == "Yes" else 0],
        'PNEUMONIA': [1 if pneumonia == "Yes" else 0],
        'HIPERTENSION': [1 if hypertension == "Yes" else 0],
        'DIABETES': [1 if diabetes == "Yes" else 0],
        'OBESITY': [1 if obesity == "Yes" else 0],
        'SEX': [0],
        'COPD': [0],
        'ASTHMA': [0],
        'INMSUPR': [0],
        'OTHER_DISEASE': [0],
        'CARDIOVASCULAR': [0],
        'RENAL_CHRONIC': [0],
        'TOBACCO': [0]
    })

    return input_data
