# Heart Failure Prediction using Decision Trees

## 📌 Project Overview
This project applies a **Decision Tree classifier** to predict mortality outcomes in patients with heart failure using the **Heart Failure Clinical Records Dataset** from the **UCI Machine Learning Repository**.

The primary objective of this assignment was not simply to achieve high predictive performance, but to demonstrate **clear reasoning**, **methodological justification**, and a strong understanding of **decision trees as information-theoretic models**.

This project was completed as part of a supervised learning assessment focused on **decision tree implementation, feature selection, overfitting, and pruning**.

---

## 📊 Dataset Description
The dataset contains clinical records of heart failure patients and is well-suited to decision tree modelling due to its mixture of numerical and binary features.

### Key Variables
- **age**: Age of the patient  
- **anaemia**: Decrease of red blood cells (boolean)  
- **creatinine_phosphokinase**: Level of CPK enzyme in the blood  
- **diabetes**: Whether the patient has diabetes  
- **ejection_fraction**: Percentage of blood leaving the heart at each contraction  
- **high_blood_pressure**: Presence of hypertension  
- **platelets**: Platelet count in the blood  
- **serum_creatinine**: Level of serum creatinine  
- **serum_sodium**: Level of serum sodium  
- **sex**: Gender of the patient  
- **smoking**: Smoking status  
- **time**: Follow-up period (days)  
- **DEATH_EVENT** *(target variable)*:  
  - 1 = death  
  - 0 = survival  

---

## 🔍 Exploratory Data Analysis
Before modelling, exploratory analysis was conducted to understand:
- Feature distributions
- Relationships between predictors and mortality outcomes
- Potential predictors of high importance (e.g., ejection fraction, serum creatinine)

EDA informed **feature selection decisions** and helped reduce unnecessary complexity in the model.

---

## 🌳 Decision Tree Model
A **Decision Tree classifier** was selected because:
- The target variable is binary
- Decision trees are interpretable and align well with clinical decision-making
- The model supports non-linear relationships and feature interactions

### Methodological Decisions
- Tree depth was controlled to prevent overfitting
- Feature importance was analysed to understand model behaviour
- Pruning strategies were explored and justified in the report
- Unnecessary techniques were intentionally excluded where they did not improve performance

These decisions are discussed in detail in the accompanying written report.

---

## 📈 Model Evaluation
The model was evaluated using:
- Classification accuracy
- Confusion matrix analysis
- Feature importance interpretation

Rather than optimising solely for accuracy, emphasis was placed on **interpretability**, **generalisation**, and **clarity of reasoning**.

---

## 🛠️ Technologies Used
- **Python**
- **NumPy**
- **Matplotlib**
- **Scikit-learn**

Additional libraries were used only where justified and documented in the report.

---

