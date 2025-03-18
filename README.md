
# 🧪 Flask-Based Web App for Predicting ATC Classes from SMILES

This **Flask-based web application** predicts **Anatomical Therapeutic Chemical (ATC) classes** for input **SMILES strings** using **Graph Convolutional Networks (GCN)** from **DeepChem**.  
The app **processes molecular structures**, **extracts features**, and **displays prediction results** along with a **molecular visualization**.

---

## 🌟 Features
✅ **Pre-trained GCN Models** – Predicts **ATC classes (A, B, C, etc.)**.  
✅ **Molecular Visualization** – Uses **RDKit** to generate a **molecule image from SMILES**.  
✅ **Clear Error Handling** – Detects **invalid SMILES and prediction failures**, logging errors.  
✅ **Environment-Based Configuration** – Supports **Flask-CORS** for flexible deployment.  

---

## 🚀 Technologies Used
- **Flask** – Web framework for handling HTTP requests and rendering templates.
- **DeepChem** – Feature extraction and **GCN-based molecular property prediction**.
- **RDKit** – **SMILES parsing and molecule visualization**.
- **Flask-CORS** – Cross-origin request handling for flexible deployment.
- **Python** – Core backend programming language.

---

## 🌐 Route Overview

| Route        | Description |
|-------------|------------|
| `/`         | Renders the **home page** (`index.html`). |
| `/predict`  | Accepts a **POST request** with a **SMILES string**, **featurizes the molecule**, and **returns predictions**. |

---

## 📖 Code Explanation

### **1️⃣ Model Loading**
- Loads **pre-trained GCN models** for each **ATC class (A, B, C, etc.)** from the directory:  
  📁 **`last_final_atc_property_prediction_models/`**
- Uses **DeepChem’s GCNModel** to **load and predict molecular properties**.
- Stores models in the **`atc_models` dictionary** for **quick access**.

### **2️⃣ Molecular Visualization**
- Converts the input **SMILES string** into an **RDKit molecule object**.
- Generates a **PNG image** of the molecule.
- Encodes the **image in base64** for rendering in the web UI.

### **3️⃣ Prediction Workflow**
1️⃣ **Accepts a SMILES string** from the user.  
2️⃣ **Featurizes the molecule** using **DeepChem’s `MolGraphConvFeaturizer`**.  
3️⃣ **Runs predictions** on all **loaded GCN models**.  
4️⃣ **Returns class probabilities**, **sorted in descending order**.  

---

## 📊 Example Input/Output
**🔹 Input:**  
```json
{
    "smiles": "CCO"
}
🔹output
- molecular structure generated from smiles and percentage probabilities according to each class.

