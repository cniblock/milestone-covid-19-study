import streamlit as st
import pandas as pd
import joblib

def load_pipeline(base_path):
    return joblib.load(base_path)

def page_patient_prediction_body():
    st.header("Patient Risk Prediction")
    input_data = get_user_input()

    if st.button("Run Predictive Analysis"):
        try:
            model_path = 'outputs/ml_pipeline/predict_died/v1/clf_pipeline_model.pkl'
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
    sex = st.selectbox("Sex", ["Male", "Female"])
    pneumonia = st.selectbox("Pneumonia", ["Yes", "No"])
    intubed = st.selectbox("Intubed", ["Yes", "No"])
    hypertension = st.selectbox("Hypertension", ["Yes", "No"])
    diabetes = st.selectbox("Diabetes", ["Yes", "No"])
    copd = st.selectbox("COPD", ["Yes", "No"])
    asthma = st.selectbox("Asthma", ["Yes", "No"])
    inmsupr = st.selectbox("Immunosuppressed", ["Yes", "No"])
    other_disease = st.selectbox("Other Diseases", ["Yes", "No"])
    cardiovascular = st.selectbox("Cardiovascular Disease", ["Yes", "No"])
    obesity = st.selectbox("Obesity", ["Yes", "No"])
    renal_chronic = st.selectbox("Chronic Renal Disease", ["Yes", "No"])
    tobacco = st.selectbox("Tobacco Use", ["Yes", "No"])

    input_data = pd.DataFrame({
        'AGE': [age],
        'SEX': [1 if sex == "Male" else 0],
        'PNEUMONIA': [1 if pneumonia == "Yes" else 0],
        'INTUBED': [1 if intubed == "Yes" else 0],
        'HIPERTENSION': [1 if hypertension == "Yes" else 0],
        'DIABETES': [1 if diabetes == "Yes" else 0],
        'COPD': [1 if copd == "Yes" else 0],
        'ASTHMA': [1 if asthma == "Yes" else 0],
        'INMSUPR': [1 if inmsupr == "Yes" else 0],
        'OTHER_DISEASE': [1 if other_disease == "Yes" else 0],
        'CARDIOVASCULAR': [1 if cardiovascular == "Yes" else 0],
        'OBESITY': [1 if obesity == "Yes" else 0],
        'RENAL_CHRONIC': [1 if renal_chronic == "Yes" else 0],
        'TOBACCO': [1 if tobacco == "Yes" else 0]
    }, index=[0])

    return input_data