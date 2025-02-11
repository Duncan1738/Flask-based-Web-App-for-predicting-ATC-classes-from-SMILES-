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

