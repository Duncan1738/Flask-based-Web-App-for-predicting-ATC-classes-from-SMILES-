# Flask-based-Web-App-for-predicting-ATC-classes-from-SMILES-
🧪 Flask-based Web App for Predicting ATC Classes from SMILES
A Flask-based web application for predicting ATC classes from SMILES using pre-trained Graph Convolutional Network (GCN) models from DeepChem. This app accepts SMILES input, processes it using DeepChem’s MolGraphConvFeaturizer, and displays the predicted class probabilities along with a molecular structure image.

🌟 Features
Pre-trained GCN Models for predicting ATC classes (A, B, C, etc.).
Molecular Visualization using RDKit—converts the SMILES string into a molecule image.
Clear Error Handling and Logging for invalid SMILES or failed predictions.
Environment-based Configuration for flexible deployment with Flask-CORS support.

🚀 Technologies Used
Flask: Web framework for handling requests and rendering templates.
DeepChem: For molecular graph convolution feature extraction and model prediction.
RDKit: For SMILES parsing and molecule image generation.
Flask-CORS: For handling cross-origin requests.
Python: Core programming language for the backend.

🌐 Route Overview
Route	Description
/	Renders the home page (index.html).
/predict	Accepts a POST request with a SMILES string. Featurizes the molecule and returns predictions.
📖 Code Explanation
Model Loading
Loads pre-trained GCN models for each ATC class (A, B, C, etc.) from the directory last_final_atc_property_prediction_models/.
Uses DeepChem's GCNModel to load and predict molecular properties.
Models are stored in the atc_models dictionary for quick access.
Molecular Visualization
Converts the input SMILES string into an RDKit molecule object.
Generates a PNG image of the molecule and encodes it in base64 for rendering on the web.
Prediction Workflow
Accepts a SMILES string from the user.
Featurizes the molecule using DeepChem’s MolGraphConvFeaturizer.
Runs predictions on all loaded GCN models.
Returns class probabilities sorted in descending order.
📊 Example Input/Output
Input:
SMILES string (e.g., CCO)

Output:
Predicted class probabilities:
A: 85.5%
B: 12.4%
Molecular Structure Image (generated from SMILES)
🛠 Error Handling & Logging
Provides clear error messages for:
Invalid or malformed SMILES strings.
Failed model predictions.
Logs errors for easier debugging.
✨ Future Improvements
Add interactive visualizations for prediction results.
Support multiple molecule input for batch prediction.
Deploy the app on Heroku or Docker for easier sharing.
📜 License
This project is licensed under the MIT License.

📧 Contact
For questions or suggestions, feel free to reach out:
Duncan Kibet
GitHub Profile

