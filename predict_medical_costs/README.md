# 🏥  Medical Insurance Cost Prediction using Linear Regression
## 📌 Project Overview

This project applies linear regression techniques to predict individual medical insurance costs using the popular Insurance dataset. The objective is to explore how demographic and lifestyle factors influence medical charges, while carefully justifying modeling decisions rather than applying techniques mechanically.

The project was completed as part of a supervised learning assessment focusing on:

* Feature selection

* Functional form

* Optimization

* Regularization

* Model evaluation
* 
## 🔍 Exploratory Data Analysis (EDA)

The following analyses were conducted to understand the structure and relationships in the data:

1. Variable Distributions

* Distribution of age, gender, smoking status, and medical charges

* Visual comparison of medical costs between males and females

* Strong cost skew driven by smoking behavior

2. Correlation Analysis

* Correlation matrix used to identify linear relationships

* Smoking status shows the strongest association with medical charges

* Age and BMI exhibit moderate positive relationships with cost

3. Bivariate Analysis

* Regression line plotted between age and medical costs

*Clear upward trend, though variance increases with age

## 🧠 Modeling Approach
## Model Choice

A linear regression model was selected. Regularized variants were also explored to assess bias-variance trade-offs.

## Models Trained

* Ordinary Least Squares Linear Regression

* Ridge Regression (L2 regularization)

* Lasso Regression (L1 regularization)

* Elastic Net (combined L1 & L2)

## Data Preparation

* Categorical variables encoded appropriately

* Train/test split applied

* Feature scaling used where required for regularized models

## 🧪 Evaluation & Interpretation

* Linear and Ridge regression performed similarly, indicating limited overfitting in the base model

* Ridge regression marginally improved error metrics, suggesting mild multicollinearity

* Lasso and Elastic Net underperformed significantly, likely due to excessive coefficient shrinkage

* Smoking status emerged as the dominant predictor of medical costs

## ⚠️ Limitations

* Linear regression struggles to fully capture non-linear cost dynamics

* Heavy skew in medical charges affects prediction accuracy

* Interaction effects (e.g., age × smoker) could further improve performance

## 🚀 Key Takeaways

* Thoughtful feature exploration matters more than model complexity

* Regularization is not always beneficial and must be contextually justified

* Linear models remain interpretable and effective for structured tabular data
