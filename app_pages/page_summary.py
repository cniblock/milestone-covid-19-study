import streamlit as st

def page_summary_body():
    st.write("### Quick Project Summary")

    # "Dataset Content" section
    st.info(
        f"**Project Terms & Jargon**\n"
        f"* **COVID-19**: A novel coronavirus causing a global pandemic, primarily affecting the respiratory system.\n"
        f"* **Patient**: An individual whose health data is recorded in the dataset, particularly regarding COVID-19.\n"
        f"* **Risk Level**: A classification of a patient's likelihood of severe illness based on symptoms and health history.\n"
        f"* **Intubation**: A medical procedure where a tube is placed into the trachea to assist with breathing.\n"
        f"* **Hypertension**: A condition where the blood pressure in the arteries is persistently elevated.\n"
        f"* **Diabetes**: A group of diseases that result in high blood sugar levels over a prolonged period.\n\n"
        
        f"**Project Dataset**\n"
        f"* The dataset represents **patient information related to COVID-19** from a public health repository. "
        f"It includes anonymized patient records detailing demographic data, pre-existing conditions, "
        f"symptoms, and outcomes related to COVID-19.\n"
        f"* The dataset contains features such as age, gender, intubation status, and several chronic conditions "
        f"that may influence the severity of COVID-19 outcomes."
    )

    # Link to README file
    st.write(
        f"* For additional information, please visit and **read** the "
        f"[Project README file](https://github.com/cniblock/milestone-covid-19-study).")

    # "Business Requirements" section
    st.success(
        f"The project has 2 primary business requirements:\n"
        f"* 1 - The client is interested in predicting the severity of a COVID-19 patient's illness "
        f"based on their current symptoms and pre-existing health conditions. The goal is to assist healthcare "
        f"providers in prioritizing and allocating resources effectively.\n"
        f"* 2 - The client aims to provide actionable insights on healthcare resource allocation based on the predicted risk levels. "
        f"This includes optimizing the distribution of ICU beds, ventilators, and other critical care resources "
        f"to enhance patient outcomes and manage resource scarcity effectively."
    )