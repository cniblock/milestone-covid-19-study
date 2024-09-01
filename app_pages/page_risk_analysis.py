import plotly.express as px
import numpy as np
from feature_engine.discretisation import ArbitraryDiscretiser
import streamlit as st
from src.data_management import load_covid_data

import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style("whitegrid")

def page_risk_analysis_body():
    df = load_covid_data()

    vars_to_study = ['AGE', 'INTUBED', 'PNEUMONIA', 'ICU', 'DIABETES', 'HIPERTENSION']

    st.write("### COVID-19 Risk Analysis")
    st.info(
        "* This analysis aims to understand patterns in patient data "
        "to identify the most relevant variables correlated with severe COVID-19 outcomes."
    )

    if st.checkbox("Inspect COVID-19 Data"):
        st.write(
            f"The dataset contains {df.shape[0]} rows and {df.shape[1]} columns. "
            "Here are the first 10 rows of the data:"
        )
        st.dataframe(df.head(11))

    st.write("---")

    st.write(
        "A correlation study was conducted to understand how various factors "
        "are associated with COVID-19 severity levels.\n"
        f"The most correlated variables are: **{', '.join(vars_to_study)}**"
    )

    st.info(
        "Insights from the correlation study suggest:\n"
        "* Older age groups are more likely to experience severe outcomes.\n"
        "* Patients who are not intubated have a higher risk of severe illness or death.\n"
        "* The presence of pneumonia is a strong indicator of severe outcomes.\n"
        "* Conditions like hypertension and diabetes are associated with increased risk.\n"
        "* Admission to the ICU is often necessary for patients with severe disease progression and is a marker of high risk."
    )

    df_eda = df.filter(vars_to_study + ['DIED'])

    if st.checkbox("Show Risk Levels by Variable"):
        risk_level_per_variable(df_eda)

    if st.checkbox("Show Parallel Plot of Risk Factors"):
        st.write(
            "This parallel plot highlights the characteristics of patients with severe outcomes."
        )
        parallel_plot_risk(df_eda)

def risk_level_per_variable(df_eda):
    target_var = 'DIED'

    for col in df_eda.drop([target_var], axis=1).columns.to_list():
        if df_eda[col].dtype == 'object':
            plot_categorical(df_eda, col, target_var)
        else:
            plot_numerical(df_eda, col, target_var)

def plot_categorical(df, col, target_var):
    fig, axes = plt.subplots(figsize=(12, 5))
    sns.countplot(data=df, x=col, hue=target_var, order=df[col].value_counts().index)
    plt.xticks(rotation=90)
    plt.title(f"{col}", fontsize=20, y=1.05)
    st.pyplot(fig)

def plot_numerical(df, col, target_var):
    fig, axes = plt.subplots(figsize=(8, 5))
    sns.histplot(data=df, x=col, hue=target_var, kde=True, element="step")
    plt.title(f"{col}", fontsize=20, y=1.05)
    st.pyplot(fig)

def parallel_plot_risk(df_eda):
    age_map = [-np.Inf, 20, 40, 60, 80, np.Inf]
    disc = ArbitraryDiscretiser(binning_dict={'AGE': age_map})
    df_parallel = disc.fit_transform(df_eda)

    n_classes = len(age_map) - 1
    classes_ranges = disc.binner_dict_['AGE'][1:-1]
    labels_map = {}
    for n in range(0, n_classes):
        if n == 0:
            labels_map[n] = f"<{classes_ranges[0]}"
        elif n == n_classes-1:
            labels_map[n] = f"+{classes_ranges[-1]}"
        else:
            labels_map[n] = f"{classes_ranges[n-1]} to {classes_ranges[n]}"

    df_parallel['AGE'] = df_parallel['AGE'].replace(labels_map)
    df_parallel['DIED_Status_Num'] = df_parallel['DIED'].map({0: "Didn't die", 1: 'Died'})

    fig = px.parallel_categories(
        df_parallel,
        dimensions=['AGE', 'INTUBED', 'PNEUMONIA', 'ICU', 'DIABETES', 'HIPERTENSION', 'DIED_Status_Num'],
        color="DIED_Status_Num",
        color_continuous_scale=px.colors.sequential.Inferno
    )
    st.plotly_chart(fig)
