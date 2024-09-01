# COVID-19 Study

![COVID Banner](banner-coronavirus_0.webp)

## Dataset Content

The dataset is sourced from a public repository provided by the Mexican government and hosted on [Kaggle](https://www.kaggle.com/datasets/meirnizri/covid19-dataset). The original dataset contains anonymized patient-related information, including pre-existing conditions, symptoms, and outcomes related to COVID-19.
Each row represents a patient, and each column contains a patient attribute. The dataset includes information about:
- Medical Units and Patient Care.
- Demographics and Health Conditions.
- Pre-existing Conditions and Symptoms.
- Clinical Outcomes and Treatments.

|Variable|Meaning|Units|
|:----|:----|:----|
|USMER|Indicates whether the patient treated medical units of the first, second or third level|1: Yes; 2: No|
|MEDICAL_UNIT|Type of institution of the National Health System that provided the care|1-13 (Institution types)|
|SEX|Gender of the patient|1: Female; 2: Male|
|PATIENT_TYPE|Type of care the patient received in the unit|1: Returned home; 2: Hospitalization|
|DATE_DIED|Date of death, or '9999-99-99' if still alive|Date|
|INTUBED|Whether the patient was connected to the ventilator|1: Yes; 2: No|
|PNEUMONIA|Whether the patient already had air sacs inflammation|1: Yes; 2: No|
|AGE|Age of the patient|Numeric|
|PREGNANT|Whether the patient is pregnant|1: Yes; 2: No|
|DIABETES|Whether the patient has diabetes|1: Yes; 2: No|
|COPD|Whether the patient has chronic obstructive pulmonary disease|1: Yes; 2: No|
|ASTHMA|Whether the patient has asthma|1: Yes; 2: No|
|INMSUPR|Whether the patient is immunosuppressed|1: Yes; 2: No|
|HIPERTENSION|Whether the patient has hypertension|1: Yes; 2: No|
|OTHER_DISEASE|Whether the patient has other diseases|1: Yes; 2: No|
|CARDIOVASCULAR|Whether the patient has heart or blood vessel-related diseases|1: Yes; 2: No|
|OBESITY|Whether the patient is obese|1: Yes; 2: No|
|RENAL_CHRONIC|Whether the patient has chronic renal disease|1: Yes; 2: No|
|TOBACCO|Whether the patient is a tobacco user|1: Yes; 2: No|
|CLASIFFICATION_FINAL|COVID test results indicating the severity of the disease|1-3: Positive with different degrees; 4+: Negative or inconclusive|
|ICU|Whether the patient had been admitted to an Intensive Care Unit|1: Yes; 2: No|

## Business Case: Predicting COVID-19 Patient Severity

Coronavirus disease (COVID-19) is an infectious disease caused by a newly discovered coronavirus. Most people infected with COVID-19 virus will experience mild to moderate respiratory illness and recover without requiring special treatment. Older people and those with underlying medical problems like cardiovascular disease, diabetes, chronic respiratory disease, and cancer are more likely to develop serious illness.

During the entire course of the pandemic, one of the main problems that healthcare providers have faced is the shortage of medical resources and a proper plan to efficiently distribute them. In these challenging times, being able to predict what kind of resource an individual might require at the time of being tested positive or even before that will be of immense help to the authorities as they would be able to procure and arrange for the resources necessary to save the life of that patient.

## Business Requirements:

- ### 1 - Predicting Patient Severity: 
    - The primary business requirement is to build a machine learning model that, given a COVID-19 patient's current symptoms, status, and medical history, can predict whether the patient is at high risk of severe illness (requiring intensive care, intubation, etc.) or not.

- ### 2 - Resource Allocation:
    - Based on the predictions, provide actionable insights into how healthcare resources (such as ICU beds, ventilators, etc.) should be allocated to optimize patient outcomes and manage resource scarcity.

## Hypothesis and how to validate?

* 1 - Patients with pre-existing health conditions have a higher risk of severe COVID-19 outcomes.
    - Validation Method: Conduct a correlation study to identify relationships between pre-existing conditions (such as hypertension, diabetes, and COPD) and patient severity or mortality.

* 2 - Older patients are more likely to experience severe COVID-19 symptoms.
    - Validation Method: Use age as a variable in correlation and regression analyses to evaluate its predictive power for severe outcomes.

## The rationale to map the business requirements to the Data Visualisations and ML tasks

* #### Business Requirement 1: Data Visualization and Correlation Study

    - Objective: Understand the factors contributing to severe COVID-19 outcomes.
        - Inspect data related to patient demographics, health conditions, and outcomes.
        - Conduct a correlation study using Pearson and Spearman methods to explore relationships between variables and patient severity or mortality.
        - Visualize key variables against the severity or mortality outcomes to gain insights into potential risk factors.

* #### Business Requirement 2: Classification, Regression, and Data Analysis

    - Objective: Develop predictive models to assist in healthcare resource allocation and patient management.
        - Build a binary classifier to predict whether a patient is at high risk of severe illness, focusing on key factors identified in the correlation study.
        - Develop a regression model to estimate the risk level for a patient based on age and pre-existing conditions. If necessary, adjust the ML task to classification based on the regressor's performance.
        - Analyze model results to provide actionable insights for healthcare providers, including potential interventions to mitigate risk for vulnerable patient groups.

## ML Business Case

### Predicting COVID-19 Patient Severity

### Regression Model

The objective is to develop a machine learning model to predict the risk level for a COVID-19 patient based on their age and pre-existing health conditions. The model aims to assist healthcare providers in resource allocation and patient management during the pandemic.

* Target Variable: Patient mortality risk (0: No, 1: Yes).
* Type of Model: Regression model for predicting risk levels.

### Ideal Outcome

The model provides healthcare professionals with insights into the risk levels of COVID-19 patients, aiding in timely interventions and efficient resource allocation.

### Model Success Metrics

* Achieve an R² score of at least 0.7 on both train and test datasets.
* The model will be considered a failure if it predicts risk levels with more than 50% error in over 30% of the cases. For instance, if the model predicts a risk score of 10 for a patient who actually has a risk score of 2, this would be considered a failure.

### Output

* Prediction Type: Continuous value indicating the risk level of a patient.
* Usage: Predictions are made in real-time as new patient data becomes available, allowing healthcare providers to make informed decisions on the fly.

### Training Data

* Source: The dataset contains over 62,000 (trimmed from over 1 million) patient records sourced from a public repository provided by the Mexican government.
* Training Data Preparation: The training data is derived from the dataset, excluding the DIED column for features, and using DIED as the target variable.

## Dashboard Design (Streamlit App User Interface)

### Page 1: Quick Project Summary
- Quick project summary
  - Project Terms & Jargon
  - Describe Project Dataset
  - State Business Requirements

### Page 2: COVID-19 Risk Analysis
- Before the analysis, we knew we wanted this page to answer business requirement 1, but we couldn't know in advance which plots would need to be displayed.
- After data analysis, we agreed with stakeholders that the page will:
  - State business requirement 1
  - Checkbox: data inspection on the dataset (display the number of rows and columns in the data, and display the first ten rows of the data)
  - Display the most correlated variables to patient severity and the conclusions
  - Checkbox: Individual plots showing the severity levels for each correlated variable
  - Checkbox: Parallel plot using patient severity and correlated variables

### Page 3: Patient Risk Prediction
- State business requirement 2
- Set of widget inputs related to the patient profile. Each set of inputs is related to a given ML task to predict patient severity and resource needs.
- "Run predictive analysis" button that processes the patient data through our ML pipelines and predicts the risk level of severe illness. It also provides recommendations for resource allocation based on the predicted severity.

### Page 4: Project Hypotheses and Validation
- Before the analysis, we knew we wanted this page to describe each project hypothesis, the conclusions, and how we validated each. After the data analysis, we can report that:
- 1 - Older age groups are at higher risk of severe outcomes
  - Correct. The correlation study and regression analysis support this.
- 2 - Pre-existing conditions like pneumonia and hypertension increase severity risk.
  - Supported by data analysis. The insights will be taken to clinical teams for further discussions and investigations.

### Page 5: Model Evaluation and Feature Importance
- Considerations and conclusions after the pipeline is trained
- Present ML pipeline steps
- Feature importance
- Pipeline performance

## Unfixed Bugs

* On the prediction model, AGE does not seem to make as much of an impact of patient severity as expected. Addressing this would require further investigation, possibly involving more sophisticated feature engineering or alternative modeling approaches.Other than that, everything is functioning as expected and no significant issues were encountered.

## Deployment

### Heroku

* The App live link is: <https://YOUR_APP_NAME.herokuapp.com/>
* Set the runtime.txt Python version to a [Heroku-20](https://devcenter.heroku.com/articles/python-support#supported-runtimes) stack currently supported version.
* The project was deployed to Heroku using the following steps.

1. Log in to Heroku and create an App
2. At the Deploy tab, select GitHub as the deployment method.
3. Select your repository name and click Search. Once it is found, click Connect.
4. Select the branch you want to deploy, then click Deploy Branch.
5. The deployment process should happen smoothly if all deployment files are fully functional. Click the button Open App on the top of the page to access your App.
6. If the slug size is too large then add large files not required for the app to the .slugignore file.

## Main Data Analysis and Machine Learning Libraries

* **Pandas**: This library was used extensively for data manipulation and analysis, including tasks such as loading datasets, handling missing data, and performing DataFrame operations.

* **NumPy**: NumPy was utilized for various numerical computing tasks, providing support for array manipulations, mathematical operations, and efficient handling of numerical data.

* **Matplotlib & Seaborn**: These libraries were employed for data visualization, enabling the creation of plots, histograms, and heatmaps to help understand data distributions and relationships.

* **Scikit-Learn**: Scikit-Learn was leveraged for a range of machine learning tasks, including data preprocessing, model training, and evaluation. It provided tools for splitting data, applying machine learning algorithms, and assessing model performance.

* **XGBoost**: XGBoost was applied to build high-performance gradient boosting models, particularly suited for handling structured data in predictive modeling tasks.

* **Streamlit**: Streamlit was used to develop an interactive web application for the project, allowing users to input data and receive predictions based on the trained models.

* **Feature-Engine**: Utilized for feature engineering tasks, such as encoding categorical variables, handling outliers, and selecting important features.


## Credits

### Content

- **Dataset**: The COVID-19 dataset used in this project was sourced from a public repository provided by the Mexican government and hosted on Kaggle. The dataset includes anonymized patient-related information such as pre-existing conditions, symptoms, and outcomes related to COVID-19.

### Media

* The image used as a header on the README was taken from: ![COVID-19 Pandemic](https://www.paho.org/en/topics/coronavirus-infections/coronavirus-disease-covid-19-pandemic)

- **Streamlit App Layout Inspiration**: The layout and design of the Streamlit app were influenced by Code Institutes Walkthrough project.

## Acknowledgements (optional)

- **Mentor**: A special thank you to my mentor Precious Ljege who provided guidance and feedback throughout the project.

- **Online Communities**: I would also like to acknowledge the help from various online communities, including Slack, Stack Overflow and Code Institute alumni, for providing answers and solutions to challenges encountered during the development of this project.
