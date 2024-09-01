import streamlit as st

def page_summary_body():
    st.write("### Quick Project Summary")

    # "Project Terms & Jargon" section
    st.info(
        "**Project Terms & Jargon**\n\n"
        "* **COVID-19**: A novel coronavirus responsible for a global pandemic, primarily affecting the respiratory system.\n"
        "* **Patient**: An individual whose health data is recorded in the dataset, particularly regarding COVID-19.\n"
        "* **Risk Level**: A classification of a patient's likelihood of severe illness based on symptoms and health history.\n"
        "* **Intubation**: A medical procedure where a tube is placed into the trachea to assist with breathing.\n"
        "* **Pneumonia**: An infection that inflames the air sacs in one or both lungs, which may fill with fluid or pus, causing cough with phlegm or pus, fever, chills, and difficulty breathing.\n"
        "* **ICU**: Intensive Care Unit, a specialized hospital department where critically ill patients receive close monitoring and intensive care.\n"
        "* **Hypertension**: A condition where the blood pressure in the arteries is persistently elevated.\n"
        "* **Diabetes**: A group of diseases that result in high blood sugar levels over a prolonged period.\n"
    )

    # "Project Dataset" section
    st.info(
        "**Project Dataset**\n\n"
        "* The dataset comprises **patient information related to COVID-19** from a public health repository. "
        "It includes anonymized patient records detailing demographic data, pre-existing conditions, "
        "symptoms, and outcomes related to COVID-19.\n"
        "* Features in the dataset include age, gender, intubation status, and several chronic conditions "
        "that may influence the severity of COVID-19 outcomes."
    )

    # Link to README file
    st.write(
        "* For more details, please visit and **read** the "
        "[Project README file](https://github.com/cniblock/milestone-covid-19-study)."
    )

    # "Business Requirements" section
    st.success(
        "**Business Requirements**\n\n"
        "The project has two primary business requirements:\n"
        "1. **Severity Prediction:** The client is interested in predicting the severity of a COVID-19 patient's illness "
        "based on their current symptoms and pre-existing health conditions. The goal is to assist healthcare "
        "providers in prioritizing and allocating resources effectively.\n"
        "2. **Resource Allocation Insights:** The client aims to provide actionable insights on healthcare resource allocation based on the predicted risk levels. "
        "This includes optimizing the distribution of ICU beds, ventilators, and other critical care resources "
        "to enhance patient outcomes and manage resource scarcity effectively."
    )
