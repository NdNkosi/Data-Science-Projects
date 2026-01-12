# Modelling Hydrocarbon Heat Dynamics with RDKit and Regression

## 🔥 Project Overview
This project combines **cheminformatics (RDKit)** and **machine learning regression** to model the **thermal properties of hydrocarbons**, specifically their **melting points** and **boiling points**.

Hydrocarbons are composed exclusively of carbon and hydrogen and are commonly used as fuels, making their thermal behaviour critically important. Due to the limited number of variables available in the raw dataset, this project demonstrates how **RDKit-derived molecular descriptors** can be used to enrich the dataset and improve predictive modelling.

---

## 📊 Dataset Description
- **Dataset:** Hydrocarbons dataset
- **Molecular Representation:** SMILES strings
- **Target Variables:**
  - Melting point
  - Boiling point

The dataset contains molecules composed only of carbon and hydrogen, along with experimentally measured thermal properties. The SMILES column enables molecular feature extraction using RDKit.

---

## 🛠️ Tools & Libraries Used
This project was implemented in a **Jupyter Notebook** using:
- **RDKit**
- **NumPy**
- **Pandas**
- **Matplotlib**
- **Scikit-learn**

RDKit was used for molecular feature extraction, while scikit-learn was used for regression modelling.

---

## 🧪 Methodology

### 1. Molecular Feature Extraction with RDKit
RDKit was used to convert SMILES strings into molecular objects and extract chemically meaningful descriptors. The following properties were computed:

- **Molecular (atomic) weight**
- **Number of aromatic rings**

These descriptors were selected due to their relevance to intermolecular forces and phase-change behaviour.

A new modelling dataset was constructed containing:
- Atomic weight
- Number of aromatic rings
- Melting point
- Boiling point

---

### 2. Regression Modelling
Two separate regression tasks were performed:

- **Melting point prediction**
- **Boiling point prediction**

Using the extracted RDKit features as inputs, regression models were trained to predict each thermal property. The modelling process highlights the challenges of learning from small and low-dimensional datasets and demonstrates how chemical domain knowledge can compensate for limited raw features.

---

## 📈 Results & Observations
- Molecular weight shows a strong relationship with boiling point
- Aromaticity contributes additional structural information relevant to heat dynamics
- RDKit descriptors significantly improve model expressiveness compared to using raw CSV variables alone
- Regression performance is constrained by dataset size and feature simplicity

---

## ⚠️ Challenges & Limitations
- Limited number of available molecular descriptors
- Hydrocarbon-only dataset restricts chemical diversity
- Linear models may not fully capture non-linear thermodynamic relationships
- Experimental noise in melting point measurements affects prediction accuracy

---

## 🔧 Potential Improvements
- Incorporate additional RDKit descriptors (e.g. molecular volume, surface area)
- Explore non-linear regression models
- Expand dataset to include a broader range of organic compounds
- Perform feature selection and regularization analysis

---

