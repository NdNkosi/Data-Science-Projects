# Multivariate Imputation – Air Quality Dataset

**Tools:** Python, Pandas, Scikit-learn  
**Technique:** Multivariate Imputation by Chained Equations (MICE)  

## 🎯 Objective
To address missing values in an environmental air quality dataset while preserving underlying data patterns, particularly extreme pollution peaks, using **Multivariate Imputation by Chained Equations (MICE)**.

## 🛠 Key Steps
1. **Data Exploration**
   - Assessed missingness across pollutants: SO₂, NO₂, O₃, PM₂.₅, and PM₁₀.
   - Visualized missing data patterns.
2. **Data Preprocessing**
   - Removed duplicates.
   - Ensured consistent data types and formats.
3. **Multivariate Imputation**
   - Applied `IterativeImputer` from `scikit-learn` to predict missing values using other available features.
   - Maintained inter-variable relationships for realistic imputations.
4. **Post-Imputation Analysis**
   - Compared pre- and post-imputation pollutant trends.
   - Checked that extreme peaks were preserved.
5. **Reporting**
   - Documented methodology, findings, and implications in a detailed Word report.

## 📈 Results
- Achieved complete dataset with no missing values.
- Preserved overall trends and most extreme pollution events.
- Produced dataset suitable for downstream modeling and analysis.

## 📚 Skills Learned
- Understanding missing data mechanisms (MCAR, MAR, MNAR).
- Implementing MICE for realistic imputations.
- Evaluating imputation quality beyond missing value counts.
- Balancing data completeness with statistical integrity.

## 📂 Files in this Project
- `imputation_code.py` — Python script implementing the imputation.# Multivariate Imputation – Air Quality Dataset

**Tools:** Python, Pandas, Scikit-learn  
**Technique:** Multivariate Imputation by Chained Equations (MICE)  

## 🎯 Objective
To address missing values in an environmental air quality dataset while preserving underlying data patterns, particularly extreme pollution peaks, using **Multivariate Imputation by Chained Equations (MICE)**.

## 🛠 Key Steps
1. **Data Exploration**
   - Assessed missingness across pollutants: SO₂, NO₂, O₃, PM₂.₅, and PM₁₀.
   - Visualized missing data patterns.
2. **Data Preprocessing**
   - Removed duplicates.
   - Ensured consistent data types and formats.
3. **Multivariate Imputation**
   - Applied `IterativeImputer` from `scikit-learn` to predict missing values using other available features.
   - Maintained inter-variable relationships for realistic imputations.
4. **Post-Imputation Analysis**
   - Compared pre- and post-imputation pollutant trends.
   - Checked that extreme peaks were preserved.
5. **Reporting**
   - Documented methodology, findings, and implications in a detailed Word report.

## 📈 Results
- Achieved complete dataset with no missing values.
- Preserved overall trends and most extreme pollution events.
- Produced dataset suitable for downstream modeling and analysis.

## 📚 Skills Learned
- Understanding missing data mechanisms (MCAR, MAR, MNAR).
- Implementing MICE for realistic imputations.
- Evaluating imputation quality beyond missing value counts.
- Balancing data completeness with statistical integrity.

## 📂 Files in this Project
- `imputation_code.py` — Python script implementing the imputation.
- `imputed_dataset.csv` — Final cleaned dataset after imputation.
- `imputation_report.docx` — Full project report with methodology, evaluation, and discussion.
