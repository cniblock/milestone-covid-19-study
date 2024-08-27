import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
from src.data_management import load_pkl_file
from src.machine_learning.evaluate_clf import clf_performance


def page_model_evaluation_body():
    version = 'v1'
    risk_pipe = load_pkl_file(
        f"outputs/ml_pipeline/predict_severity/{version}/clf_pipeline.pkl")
    risk_feat_importance_1 = plt.imread(
        f"outputs/ml_pipeline/predict_severity/{version}/features_importance_1.png")
    risk_feat_importance_2 = plt.imread(
        f"outputs/ml_pipeline/predict_severity/{version}/features_importance_2.png")
    confusion_matrix_img = plt.imread(
        f"outputs/ml_pipeline/predict_severity/{version}/confusion_matrix.png")
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

    st.write("* The features the model was trained on and their importance.")
    st.write(X_train.columns.to_list())
    st.image(risk_feat_importance_1)
    st.image(risk_feat_importance_2)
    st.write("---")

    st.write("### Pipeline Performance")
    
    mae_train = mean_absolute_error(y_train, risk_pipe.predict(X_train))
    mae_test = mean_absolute_error(y_test, risk_pipe.predict(X_test))
    st.write(f"**Mean Absolute Error (Train):** {mae_train:.3f}")
    st.write(f"**Mean Absolute Error (Test):** {mae_test:.3f}")

    st.write(
        f"Mean Absolute Error (MAE) is a simple way to measure how far off the predictions are, on average. "
        f"The MAE for the training data is **{mae_train:.3f}**, which means that on average, the model's predictions "
        f"are off by this amount. The MAE for the test data is **{mae_test:.3f}**, which is slightly higher. "
        f"This suggests that the model doesn't perform as well on new, unseen data."
    )

    mse_train = mean_squared_error(y_train, risk_pipe.predict(X_train))
    mse_test = mean_squared_error(y_test, risk_pipe.predict(X_test))
    st.write(f"**Mean Squared Error (Train):** {mse_train:.3f}")
    st.write(f"**Mean Squared Error (Test):** {mse_test:.3f}")

    st.write(
        f"Mean Squared Error (MSE) is another way to measure how wrong the predictions are. It squares the errors, "
        f"so bigger mistakes are penalized more. The MSE for the training data is **{mse_train:.3f}**, and for the test data, it's **{mse_test:.3f}**. "
        f"The higher MSE on the test data shows there are a few large errors in the predictions."
    )

    rmse_train = np.sqrt(mse_train)
    rmse_test = np.sqrt(mse_test)
    st.write(f"**Root Mean Squared Error (Train):** {rmse_train:.3f}")
    st.write(f"**Root Mean Squared Error (Test):** {rmse_test:.3f}")

    st.write(
        f"Root Mean Squared Error (RMSE) is the square root of MSE, which puts it back in the same units as the original data. "
        f"The RMSE for the training data is **{rmse_train:.3f}**, and for the test data, it's **{rmse_test:.3f}**. "
        f"The RMSE is useful because it gives a sense of how large the errors are, in the same units as the target variable."
    )

    st.write("### Analysis")

    st.write(
        f"Based on these numbers, it looks like the model does a decent job on the training data but has slightly worse performance on the test data. "
        f"This could mean that the model is overfitting a bit, which means it's doing a bit too well on the training data but not generalizing "
        f"as well to new data. To improve this, we might need to tweak the model, use more data, or try different techniques."
    )

    st.write("### Confusion Matrix")
    st.image(confusion_matrix_img, caption='Confusion Matrix')
    st.write("---")

    st.write("### Analysis of Confusion Matrix")

    st.write(
    "The confusion matrix shows how well the model is doing by counting the correct and incorrect predictions. "
    "For the training set, the model correctly predicted 24,641 high-risk cases out of 28,761 (True Positives), but it also missed 4,120 cases (False Negatives). "
    "The test set has similar results, but the model missed a few more high-risk cases, which means it might need some improvements to do better on new data."
    )

    st.write(
        "The classification report gives us more details like precision, recall, and F1-score. "
        "Precision tells us how many of the positive predictions were actually correct, while recall shows how many actual positive cases were predicted correctly. "
        "F1-score is a mix of both. An accuracy of 0.67 on the test set means the model is okay, but there's still room for improvement, especially in predicting low-risk patients."
    )