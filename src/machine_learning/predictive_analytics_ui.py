import streamlit as st
import numpy as np

def predict_risk_severity(X_live, risk_features, risk_pipeline_dc_fe, risk_pipeline_model, severity_labels_map):
    """
    Predict the severity of COVID-19 risk based on input features and display results.
    """

    # From live data, subset features related to this pipeline
    X_live_risk = X_live.filter(risk_features)

    # Apply data cleaning / feature engineering pipeline to live data
    X_live_risk_dc_fe = risk_pipeline_dc_fe.transform(X_live_risk)

    # Predict severity
    severity_prediction = risk_pipeline_model.predict(X_live_risk_dc_fe)
    severity_prediction_proba = risk_pipeline_model.predict_proba(X_live_risk_dc_fe)

    # Create a logic to display the results
    severity_prob = severity_prediction_proba[0, severity_prediction][0] * 100
    severity_level = severity_labels_map[severity_prediction[0]]

    statement = (
        f'### There is a {severity_prob.round(1)}% probability '
        f'that the patient is at **{severity_level} severity level**.'
    )
    
    st.write(statement)
    return severity_prediction

def predict_feature_impact(X_live, feature_impact_features, feature_impact_pipeline, feature_importance_map):
    """
    Analyze and display the impact of different features on risk severity prediction.
    """

    X_live_feature_impact = X_live.filter(feature_impact_features)

    feature_impact_scores = feature_impact_pipeline.feature_importances_

    sorted_indices = np.argsort(feature_impact_scores)[::-1]
    sorted_features = [feature_impact_features[i] for i in sorted_indices]
    sorted_importances = feature_impact_scores[sorted_indices]

    st.write("### Feature Impact Analysis")
    st.write("The following features have the most significant impact on the risk severity prediction:")

    for feature, importance in zip(sorted_features, sorted_importances):
        st.write(f"- {feature}: {importance:.2f}")

def show_patient_profile(X_live, severity_prediction, severity_profile_map):
    """
    Display the expected profile for the predicted severity level.
    """

    severity_profile = severity_profile_map[severity_prediction[0]]

    statement = (
        f"### The patient is expected to have the following profile based on the predicted severity level:"
    )
    st.write("---")
    st.write(statement)

    st.info(severity_profile)

    st.table(severity_profile)