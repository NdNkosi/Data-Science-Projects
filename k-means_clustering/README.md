# K-Means Clustering on Air Pollution Data
## 📌 Project Overview

This project applies **K-Means clustering** to the **Air Pollution (airpoll)** dataset in order to identify meaningful groupings of observations based on pollutant levels. The goal is to demonstrate a clear understanding of unsupervised learning, clustering methodology, and data-driven decision-making.

The project was completed as part of a machine learning assignment focused on **model reasoning, justification of choices, and interpretation of results**.

## 📊 Dataset

* **Dataset name**: Air Pollution (airpoll)

* **Type**: Environmental / Air quality data

* **Source**: Provided as part of the course materials

* **Variables**: Multiple air pollutant measurements recorded across different observations

## 🧠 Concepts Covered

This assignment draws on concepts from the lectures, including:

* Exploratory Data Analysis (EDA)

* Feature relationships and correlation

* Distance-based clustering

K-Means clustering algorithm

* Choosing the optimal number of clusters

* Model evaluation and interpretation

## 🛠️ Libraries Used

Only the following libraries were used, in accordance with the assignment requirements:

* NumPy

* Pandas

* Matplotlib

* Seaborn

* scikit-learn

No additional libraries were used.

## 🔍 Methodology
### 1. Descriptive Statistics

* Summary statistics (mean, median, standard deviation, etc.) were computed for all variables.

* This helped identify scale differences and potential preprocessing needs.

### 2. Correlation Analysis

* A correlation matrix and heatmap were used to examine relationships between pollutants.

* Highly correlated features were noted and discussed.

### 3. Distribution Analysis

* Individual distributions for each pollutant were visualized.

* This allowed inspection of skewness, outliers, and data spread.

### 4. Choosing the Number of Clusters

* To determine the optimal number of clusters:

* The Elbow Method was applied

* The trade-off between model simplicity and explained variance was evaluated

* The final value of k was chosen based on interpretability and performance

### 5. K-Means Clustering

* The K-Means algorithm was trained using the selected number of clusters

* Cluster labels were assigned to each observation

* Results were analyzed and interpreted in the context of air pollution patterns

### 6. Exporting Results

* Final clustering results were exported to an Excel file for further analysis and reporting

## 📈 Results & Discussion

* The clustering revealed distinct pollution profiles across observations

* Differences in pollutant concentration patterns were clearly observable between clusters

*The results were evaluated in terms of:

  * Cluster separation

  * Practical interpretability

  * Limitations of K-Means (e.g., sensitivity to scale and outliers)

## 📝 Report

A detailed 5-page report accompanies this project and includes:

* Step-by-step explanation of the implementation

* Justification for methodological choices

* Visualizations and interpretations

* Discussion of limitations and possible improvements

## 🚀 Key Takeaways

* K-Means clustering is effective for exploratory pattern discovery but requires careful preprocessing

* Choosing the correct number of clusters is crucial

* Clear reasoning and justification are as important as model performance
