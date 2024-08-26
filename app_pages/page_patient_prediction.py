import streamlit as st
import pandas as pd
import joblib

def load_pipeline(base_path):
    return joblib.load(base_path)

def page_patient_prediction_body():
    input_data = get_user_input()

    if st.button("Run Predictive Analysis"):
        try:
            model_path_clf = 'outputs/ml_pipeline/predict_severity/v1/clf_pipeline.pkl'
            model_pipeline_clf = load_pipeline(model_path_clf)
            clf_prediction = model_pipeline_clf.predict(input_data)[0]

            model_path_reg = 'outputs/ml_pipeline/predict_severity/v1/regressor_pipeline.pkl'
            model_pipeline_reg = load_pipeline(model_path_reg)
            reg_prediction = model_pipeline_reg.predict(input_data)[0]

            label_map = load_pipeline('outputs/ml_pipeline/predict_severity/v1/label_map.pkl')
            risk_level_clf = label_map[clf_prediction]

            if reg_prediction < 0.33:
                risk_level_reg = "Low Risk"
                risk_color_reg = "green"
            elif reg_prediction < 0.66:
                risk_level_reg = "Medium Risk"
                risk_color_reg = "orange"
            else:
                risk_level_reg = "High Risk"
                risk_color_reg = "red"

            st.markdown(f"**Classification Predicted Risk Level:** {risk_level_clf}")
            st.markdown(f"**Regression Predicted Risk Level:** <span style='color:{risk_color_reg};'>{risk_level_reg} ({reg_prediction:.2f})</span>", unsafe_allow_html=True)

        except Exception as e:
            st.error(f"An error occurred during prediction: {str(e)}")


def get_user_input():
    st.header("Patient Risk Prediction")

    age = st.slider("Age", min_value=0, max_value=120, value=50)
    intubed = st.selectbox("Intubed", ["Yes", "No"])
    icu = st.selectbox("ICU", ["Yes", "No"])
    hypertension = st.selectbox("Hypertension", ["Yes", "No"])
    diabetes = st.selectbox("Diabetes", ["Yes", "No"])
    obesity = st.selectbox("Obesity", ["Yes", "No"])

    input_data = pd.DataFrame({
        'AGE': [age],
        'INTUBED': [1 if intubed == "Yes" else 0],
        'ICU': [1 if icu == "Yes" else 0],
        'HIPERTENSION': [1 if hypertension == "Yes" else 0],
        'DIABETES': [1 if diabetes == "Yes" else 0],
        'OBESITY': [1 if obesity == "Yes" else 0],
        'SEX': [0],
        'PNEUMONIA': [0],
        'COPD': [0],
        'ASTHMA': [0],
        'INMSUPR': [0],
        'OTHER_DISEASE': [0],
        'CARDIOVASCULAR': [0],
        'RENAL_CHRONIC': [0],
        'TOBACCO': [0]
    })

    return input_data
