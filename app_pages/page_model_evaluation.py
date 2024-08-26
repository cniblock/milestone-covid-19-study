import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from src.data_management import load_covid_data, load_pkl_file
from src.machine_learning.evaluate_clf import clf_performance

def page_model_evaluation_body():
    version = 'v1'
    risk_pipe = load_pkl_file(
        f"outputs/ml_pipeline/predict_severity/{version}/regressor_pipeline.pkl")
    risk_feat_importance_1 = plt.imread(
        f"outputs/ml_pipeline/predict_severity/{version}/features_importance_1.png")
    risk_feat_importance_2 = plt.imread(
        f"outputs/ml_pipeline/predict_severity/{version}/features_importance_2.png")
    X_train = pd.read_csv(
        f"outputs/ml_pipeline/predict_severity/{version}/X_train.csv")
    X_test = pd.read_csv(
        f"outputs/ml_pipeline/predict_severity/{version}/X_test.csv")
    y_train = pd.read_csv(
        f"outputs/ml_pipeline/predict_severity/{version}/y_train.csv")
    y_test = pd.read_csv(
        f"outputs/ml_pipeline/predict_severity/{version}/y_test.csv")
    risk_labels_map = load_pkl_file(
        f"outputs/ml_pipeline/predict_severity/{version}/label_map.pkl")

    st.write("### ML Pipeline: Predict COVID-19 Risk")
    
    st.info(
        f"* The goal was to build a predictive model that could estimate the risk level of a COVID-19 patient "
        f"based on their health conditions and symptoms. The model's performance on the training and test sets "
        f"met the project's requirements for accuracy and recall, particularly in detecting high-risk patients.\n"
        f"* The model achieved a satisfactory level of performance, focusing on minimizing false negatives "
        f"to ensure that high-risk patients are correctly identified.\n"
        f"* The pipeline includes feature engineering steps that handle various patient attributes to optimize "
        f"the model's predictive capabilities.")
    st.write("---")

    st.write("* ML pipeline to predict COVID-19 risk levels based on patient data.")
    st.write(risk_pipe)
    st.write("---")

    st.write("* Features used for training the model and their importance.")
    st.write(X_train.columns.to_list())
    st.image(risk_feat_importance_1)
    st.image(risk_feat_importance_2)
    st.write("---")

    st.write("### Pipeline Performance")
    clf_performance(X_train=X_train, y_train=y_train,
                    X_test=X_test, y_test=y_test,
                    pipeline=risk_pipe,
                    label_map=risk_labels_map)