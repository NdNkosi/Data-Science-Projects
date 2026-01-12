# Solubility Prediction with Machine Learning

## 🧪 Project Overview
This project applies **machine learning regression techniques** to predict the **aqueous solubility of chemical compounds** using molecular descriptors derived from chemical structure. The goal is to build and evaluate a predictive model capable of estimating solubility based on features extracted from chemical data.

The project uses the **Delaney (ESOL) dataset**, a well-known benchmark dataset for solubility prediction tasks in cheminformatics.

---

## 📊 Dataset Description
- **Dataset:** Delaney (ESOL) Dataset
- **Source:** UCI / ESOL Dataset
- **Target variable:** `logS` (logarithm of aqueous solubility)
- **Features:** Molecular descriptors derived from chemical structure
- **Representation:** Compounds described using **SMILES notation**

The dataset contains experimentally measured solubility values and is widely used for regression-based solubility prediction.

**Reference:**
> Delaney, J. S. (2004). *ESOL: Estimating Aqueous Solubility Directly from Molecular Structure*.  
> Journal of Chemical Information and Computer Sciences, 44(3), 1000–1005.

---

## 🛠️ Tools & Libraries Used
The project was implemented in a **Jupyter Notebook** using the following libraries:
- **NumPy**
- **Pandas**
- **Matplotlib**
- **scikit-learn**

Only libraries relevant to the task were used.

---

## 🔍 Assignment Tasks & Methodology

### 1. Data Preprocessing
- Loaded the processed Delaney dataset (`solubility.csv`)
- Explored the dataset to understand:
  - Feature types
  - Target distribution
  - Dataset size and structure
- Split the data into **training** and **testing** sets to enable model evaluation

---

### 2. Model Selection
A regression model was selected to predict solubility (`logS`), with consideration given to:
- Model interpretability
- Ability to handle non-linear relationships
- Suitability for chemical property prediction

Common regression models explored include:
- Linear Regression
- Random Forest Regression
- Support Vector Regression (SVR)

The chosen model was trained using the training dataset, with solubility values as the target variable.

---

### 3. Model Evaluation
Model performance was evaluated on the test dataset using standard regression metrics:
- **Mean Squared Error (MSE)**
- **Root Mean Squared Error (RMSE)**
- **Coefficient of Determination (R²)**

---

### 4. Visualization
To assess predictive performance:
- Scatter plots were created to compare **predicted vs. true solubility values**
- Regression plots were used to visualize model accuracy and error distribution

---

## 📈 Results & Discussion
- The model demonstrated reasonable predictive performance on unseen data
- Certain molecular descriptors showed stronger influence on solubility prediction
- Non-linear models generally performed better than simple linear approaches

---

## ⚠️ Limitations
- The dataset size is relatively small, which may limit generalization
- Molecular descriptors are simplified representations of complex chemical behavior
- Model performance could potentially improve with:
  - Additional chemical features
  - Hyperparameter tuning
  - Ensemble approaches

---

