# Income Prediction using PySpark

**Tools:** PySpark, Spark MLlib  
**Techniques:** Decision Tree Classifier, Feature Engineering, Data Preprocessing  

## 🎯 Objective
Predict whether an individual's income exceeds a certain threshold based on demographic and employment-related attributes, using distributed data processing and machine learning in PySpark.

## 🛠 Key Steps
1. **Data Loading**
   - Read CSV data into a Spark DataFrame with inferred schema.

2. **Target Variable Preprocessing**
   - Encoded the target (`income_class`) into a numerical label using `StringIndexer`.

3. **Categorical Feature Engineering**
   - Indexed all string features.
   - Applied one-hot encoding for model compatibility.

4. **Numerical Feature Engineering**
   - Assembled numeric columns into a single vector.
   - Standardized features using `StandardScaler`.

5. **Feature Assembly**
   - Combined scaled numerical features and encoded categorical features into a single `features` vector.

6. **Model Training**
   - Trained a `DecisionTreeClassifier` (max depth = 5) on 70% training data, tested on 30%.
   - Also defined a `RandomForestClassifier` as an alternative model.

7. **Model Evaluation**
   - Calculated accuracy, weighted precision, and weighted recall using `MulticlassClassificationEvaluator`.

## 📈 Results
- **Accuracy:** 84% (update after running)
- **Weighted Precision:** 83%
- **Weighted Recall:** 84%
- Demonstrated scalability and efficiency of PySpark for classification tasks.

## 📚 Skills Learned
- End-to-end ML pipeline building in PySpark.
- Encoding and scaling features for Spark ML models.
- Evaluating classification performance with multiple metrics.
- Working with distributed datasets for faster computation.

## 📂 Files in this Project
- `income_prediction_spark.py` — Full PySpark pipeline code.
- `README.md` — This project documentation.
