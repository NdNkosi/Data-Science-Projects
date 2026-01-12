# Wine Classification with Machine Learning

## 🍷 Project Overview
The objective of this project is to apply **machine learning classification techniques** to the **Wine dataset** in order to classify wines into their respective classes based on their chemical properties. This project demonstrates how numerical chemical features are handled in a supervised classification setting and how different models perform on the same dataset.

The project was completed using a **Jupyter Notebook**, combining explanations, code, and visualizations into a single, reproducible workflow.

---

## 📊 Dataset Description
- **Dataset:** Wine Dataset
- **Number of samples:** 178
- **Number of classes:** 3 wine types
- **Features:** Chemical properties such as alcohol, magnesium, flavanoids, color intensity, etc.
- **Target variable:** `Wine` (wine class)

The dataset contains no missing values and is well-suited for multi-class classification tasks.

---

## 🛠️ Tools & Libraries Used
The following libraries were used for this project:
- **NumPy**
- **Pandas**
- **Matplotlib**
- **scikit-learn**
- **Spark** (optional, where applicable)

Only libraries relevant to the task were used.

---

## 🔍 Task Breakdown & Methodology

### Task 1: Data Exploration
- Loaded the Wine dataset into a Jupyter Notebook
- Examined dataset shape, feature names, and summary statistics
- Visualized the data using:
  - Histograms
  - Scatter plots
  - Pair plots (where appropriate)
- Identified relationships and patterns among chemical properties

---

### Task 2: Data Preprocessing
- Checked for missing values
- Scaled numerical features to ensure fair model comparison
- Split the dataset into **training** and **testing** sets

---

### Task 3: Model Selection
At least two classification models were selected and trained, including:
- Decision Trees
- Support Vector Machines (SVM)
- k-Nearest Neighbors (k-NN)
- Naive Bayes
- Artificial Neural Networks (where applicable)

Each model was trained on the same training data to allow fair comparison.

---

### Task 4: Model Evaluation
Model performance was evaluated using:
- Accuracy
- Precision
- Recall
- F1-score

Visual evaluation included:
- Confusion matrices
- ROC curves (multi-class setting)

---

### Task 5: Model Comparison
- Compared all trained models based on quantitative metrics
- Discussed strengths and weaknesses of each model
- Identified the best-performing model(s) and justified the results
- Reflected on limitations such as:
  - Feature scaling sensitivity
  - Model interpretability
  - Overfitting risks

---

### Task 6: Interpretation
- Investigated **feature importance** for applicable models
- Identified which chemical properties contribute most to wine classification
- Interpreted results in the context of the underlying chemistry

---

## 📈 Results & Insights
- Certain chemical properties (e.g., alcohol content, flavanoids, color intensity) were strong predictors of wine class
- Tree-based and distance-based models performed particularly well on this dataset
- Proper preprocessing significantly improved model performance
- Feature importance analysis provided meaningful interpretability

---

