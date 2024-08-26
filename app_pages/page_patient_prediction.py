import streamlit as st
import pandas as pd
import joblib

def load_pipeline(base_path):
    return joblib.load(base_path)

def page_patient_prediction_body():
    version = 'v1'
    model_path_reg = f'outputs/ml_pipeline/predict_severity/{version}/regressor_pipeline.pkl'
    model_pipeline_reg = load_pipeline(model_path_reg)

    input_data = get_user_input()
    st.write("Input Data:", input_data)

    if st.button("Run Predictive Analysis"):
        try:
            reg_prediction = model_pipeline_reg.predict(input_data)[0]

            if reg_prediction < 0.68:
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
    hypertension = st.selectbox("Hypertension", ["Yes", "No"])
    diabetes = st.selectbox("Diabetes", ["Yes", "No"])
    obesity = st.selectbox("Obesity", ["Yes", "No"])
    other_disease = st.selectbox("Other Disease", ["Yes", "No"])
    icu = st.selectbox("ICU", ["Yes", "No"])
    pneumonia = st.selectbox("Pneumonia", ["Yes", "No"])
    cardiovascular = st.selectbox("Cardiovascular", ["Yes", "No"])
    inmsupr = st.selectbox("Immunosuppressed", ["Yes", "No"])
    renal_chronic = st.selectbox("Renal Chronic", ["Yes", "No"])
    tobacco = st.selectbox("Tobacco", ["Yes", "No"])
    copd = st.selectbox("COPD", ["Yes", "No"])
    asthma = st.selectbox("Asthma", ["Yes", "No"])

    input_data = pd.DataFrame({
    'AGE': [age],
    'INTUBED': [0 if intubed == "Yes" else 1],
    'HIPERTENSION': [0 if hypertension == "Yes" else 1],
    'DIABETES': [0 if diabetes == "Yes" else 1],
    'OBESITY': [0 if obesity == "Yes" else 1],
    'OTHER_DISEASE': [0 if other_disease == "Yes" else 1],
    'ICU': [0 if icu == "Yes" else 1],
    'PNEUMONIA': [0 if pneumonia == "Yes" else 1],
    'CARDIOVASCULAR': [0 if cardiovascular == "Yes" else 1],
    'INMSUPR': [0 if inmsupr == "Yes" else 1],
    'RENAL_CHRONIC': [0 if renal_chronic == "Yes" else 1],
    'TOBACCO': [0 if tobacco == "Yes" else 1],
    'COPD': [0 if copd == "Yes" else 1],
    'ASTHMA': [0 if asthma == "Yes" else 1],
    'SEX': [0]
})

    return input_data