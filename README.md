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

During the entire course of the pandemic, one of the main problems that healthcare providers have faced is the shortage of medical resources and a proper plan to efficiently distribute them. In these tough times, being able to predict what kind of resource an individual might require at the time of being tested positive or even before that will be of immense help to the authorities as they would be able to procure and arrange for the resources necessary to save the life of that patient.

## Business Requirements:

- 1 - Predicting Patient Severity: 
    - The primary business requirement is to build a machine learning model that, given a COVID-19 patient's current symptoms, status, and medical history, can predict whether the patient is at high risk of severe illness (requiring intensive care, intubation, etc.) or not.

- 2 - Resource Allocation:
    - Based on the predictions, provide actionable insights into how healthcare resources (such as ICU beds, ventilators, etc.) should be allocated to optimize patient outcomes and manage resource scarcity.

## Hypothesis and how to validate?

* List here your project hypothesis(es) and how you envision validating it (them).

## The rationale to map the business requirements to the Data Visualisations and ML tasks

* List your business requirements and a rationale to map them to the Data Visualisations and ML tasks.

## ML Business Case

* In the previous bullet, you potentially visualised an ML task to answer a business requirement. You should frame the business case using the method we covered in the course.

## Dashboard Design

* List all dashboard pages and their content, either blocks of information or widgets, like buttons, checkboxes, images, or any other items that your dashboard library supports.
* Eventually, during the project development, you may revisit your dashboard plan to update a given feature (for example, at the beginning of the project you were confident you would use a given plot to display an insight but eventually you needed to use another plot type)

## Unfixed Bugs

* You will need to mention unfixed bugs and why they were not fixed. This section should include shortcomings of the frameworks or technologies used. Although time can be a big variable to consider, paucity of time and difficulty understanding implementation is not valid reason to leave bugs unfixed.

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

* Here you should list the libraries you used in the project and provide example(s) of how you used these libraries.

## Credits

* In this section, you need to reference where you got your content, media and extra help from. It is common practice to use code from other repositories and tutorials, however, it is important to be very specific about these sources to avoid plagiarism.
* You can break the credits section up into Content and Media, depending on what you have included in your project.

### Content

* The text for the Home page was taken from Wikipedia Article A
* Instructions on how to implement form validation on the Sign-Up page was taken from [Specific YouTube Tutorial](https://www.youtube.com/)
* The icons in the footer were taken from [Font Awesome](https://fontawesome.com/)

### Media

* The photos used on the home and sign-up page are from This Open Source site
* The images used for the gallery page were taken from this other open-source site

## Acknowledgements (optional)


* In case you would like to thank the people that provided support through this project.

