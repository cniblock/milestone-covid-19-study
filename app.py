import streamlit as st
from app_pages.multipage import MultiPage

# Load page scripts
from app_pages.page_summary import page_summary_body
from app_pages.page_risk_analysis import page_risk_analysis_body
from app_pages.page_patient_prediction import page_patient_prediction_body
from app_pages.page_hypotheses_validation import page_hypotheses_validation_body
from app_pages.page_model_evaluation import page_model_evaluation_body

app = MultiPage(app_name="COVID-19 Risk Prediction Dashboard")

# Add your app pages here using .add_page()
app.add_page("Quick Project Summary", page_summary_body)
app.add_page("COVID-19 Risk Analysis", page_risk_analysis_body)
app.add_page("Patient Risk Prediction", page_patient_prediction_body)
app.add_page("Project Hypotheses and Validation", page_hypotheses_validation_body)
app.add_page("Model Evaluation and Feature Importance", page_model_evaluation_body)

app.run()  # Run the app