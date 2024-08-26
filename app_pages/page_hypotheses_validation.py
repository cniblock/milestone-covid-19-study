import streamlit as st

def page_hypotheses_validation_body():
    st.write("### Project Hypotheses and Validation")

    st.success(
        f"* We suspect that older age groups are at higher risk of severe COVID-19 outcomes: "
        f"Correct. The correlation study and risk analysis confirm that age is a significant factor "
        f"in predicting severity and mortality. \n\n"
        
        f"* Patients with pre-existing conditions such as hypertension and diabetes are more likely to "
        f"experience severe outcomes: Correct. The analysis shows that these conditions are correlated with "
        f"increased severity in COVID-19 cases. \n\n"

        f"* Intubation is a critical intervention for patients at risk of severe respiratory distress: "
        f"Correct. The study indicates that intubated patients are often those with more severe symptoms, "
        f"highlighting the need for timely intervention. \n\n"

        f"* The presence of pneumonia in COVID-19 patients predicts higher risk: "
        f"Correct. Pneumonia is a common complication in severe cases, as supported by the data analysis. \n\n"

        f"* Admission to the ICU is a marker of severe disease progression: "
        f"Correct. Patients who require ICU care often have more severe symptoms and complications, indicating "
        f"a higher risk of poor outcomes. \n\n"
    )