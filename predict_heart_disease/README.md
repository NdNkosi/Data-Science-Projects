# Heart Disease Prediction using Logistic Regression

## 📌 Project Overview
This project applies **logistic regression** to predict the presence of heart disease using the *Heart Attack Dataset*.  
The objective is not only to build a predictive model, but to demonstrate **clear analytical reasoning**, **exploratory data analysis**, and **model evaluation**, in line with supervised learning principles covered in class.

This project was completed with an accompanying written report explaining the full methodology and results.

---

## 📊 Dataset Description
The dataset contains clinical and demographic attributes commonly used in cardiovascular risk analysis.

### Variables
- **age**: Age of the individual  
- **sex**: Gender (1 = male, 0 = female)  
- **cp (chest pain type)**  
  - 0: Typical angina  
  - 1: Atypical angina  
  - 2: Non-anginal pain  
  - 3: Asymptomatic  
- **trestbps**: Resting blood pressure (mmHg)  
- **chol**: Serum cholesterol (mg/dL)  
- **fbs**: Fasting blood sugar > 120 mg/dL (1 = true, 0 = false)  
- **restecg**: Resting electrocardiogram results  
  - 0: Normal  
  - 1: ST-T wave abnormality  
  - 2: Left ventricular hypertrophy  
- **thalach**: Maximum heart rate achieved  
- **exang**: Exercise-induced angina (1 = yes, 0 = no)  
- **oldpeak**: ST depression induced by exercise relative to rest  
- **slope**: Slope of the peak exercise ST segment  
  - 0: Upsloping  
  - 1: Flat  
  - 2: Downsloping  
- **ca**: Number of major vessels colored by fluoroscopy (0–3)  
- **thal**: Thalassemia condition indicator  
- **target**: Presence of heart disease (1 = disease, 0 = no disease)

---

## 🔍 Exploratory Data Analysis (EDA)
The following analyses were performed to understand the dataset:

- Correlation analysis across all variables
- Distribution of **age** and **cholesterol** levels
- Distribution of heart disease cases by **gender**
- Distribution of heart disease cases by **resting ECG results**

These steps helped identify relationships between predictors and the target variable, guiding model interpretation.

---

## 🤖 Model Training
A **Logistic Regression** model was trained to predict the presence of heart disease.

### Key steps:
- Feature selection based on exploratory analysis
- Train-test split to evaluate generalisation
- Model training using `sklearn.linear_model.LogisticRegression`
- Evaluation using classification accuracy and performance metrics

Logistic regression was chosen because:
- The target variable is binary
- The model provides interpretability

---

## 📈 Model Evaluation
Model performance was evaluated on unseen test data using accuracy and classification metrics.  
The results demonstrate how well the model captures patterns associated with heart disease risk.

Visualisations and metrics are discussed in detail in the accompanying report.

---

## 🛠️ Technologies Used
- **Python**
- **NumPy**
- **Matplotlib**
- **Seaborn**
- **Scikit-learn**

---

