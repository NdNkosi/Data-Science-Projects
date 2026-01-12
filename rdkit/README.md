# Molecular Processing and Visualisation with RDKit

## 🧬 Project Overview
This project explores the use of **RDKit**, a cheminformatics library, to process, analyze, and visualize molecular structures. The assignment focuses on converting chemical representations into RDKit molecule objects, extracting molecular properties, and visualizing molecules using SMILES notation.

The **Delaney (ESOL) dataset**, previously used for solubility prediction, is reused in this assignment to demonstrate molecule drawing and layout customization.

---

## 📊 Dataset Description
- **Dataset:** Delaney (ESOL) Dataset
- **Format:** CSV file (`solubility.csv`)
- **Chemical Representation:** SMILES notation
- **Target Variable (from prior assignment):** Solubility (`logS`)

Each row represents a chemical compound, identified by a compound ID and described using SMILES strings.

---

## 🛠️ Tools & Libraries Used
This project was implemented in a **Jupyter Notebook** using:
- **RDKit**
- **NumPy**
- **Pandas**
- **Matplotlib**

RDKit was used for molecular creation, property extraction, and visualization.

---

## 🔍 Assignment Tasks & Methodology

### 1. Molecular Information Extraction
RDKit molecule objects were created for the following molecules obtained from **PubChem**:
- Propane
- Ethene
- Cyclohexane
- Buckminsterfullerene

For each molecule, the following properties were computed:

- **Total number of atoms**
- **Chemical symbol and atomic weight** of each atom  
  (implemented using a loop over atoms)
- **Number of aromatic bonds**

These tasks demonstrate the ability to navigate and extract information from RDKit molecular objects.

---

### 2. Molecular Visualisation
Using the Delaney dataset:
- The **first six molecules** were extracted from `solubility.csv`
- RDKit was used to draw molecular structures
- Molecules were displayed in a **grid layout**
- **Compound IDs** were used as labels for each molecule

Layout adjustments were applied to improve readability and presentation.

---

## 📈 Results & Observations
- RDKit successfully converted SMILES strings into molecular graph representations
- Atomic-level information such as symbols and weights can be easily accessed programmatically
- Aromaticity detection provides insight into molecular structure and bonding
- Grid-based visualization improves interpretability when displaying multiple molecules

---

## ⚠️ Challenges & Limitations
- Rendering large or complex molecules (e.g. Buckminsterfullerene) can be computationally intensive
- Visual layouts may require manual adjustment for optimal clarity
- RDKit visualizations are static and may be enhanced using interactive tools in future work

---

