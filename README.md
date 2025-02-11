# Flask-based-Web-App-for-predicting-ATC-classes-from-SMILES-
Flask-based Web App for predicting ATC classes from SMILES using pre-trained GCN models from DeepChem. Supports Graph Convolution Networks (GCN) for molecular property prediction.
Accepts SMILES input and displays the predicted class probabilities along with a molecular structure image.
Code Explanation
Model Loading:

Loads pre-trained GCN models for each ATC class (A, B, C, etc.) from the directory last_final_atc_property_prediction_models/.
Uses DeepChem's GCNModel to load and predict molecular properties.
Models are loaded into a dictionary atc_models for quick access.
Molecular Visualization:

Converts the SMILES string into an RDKit molecule object.
Generates a PNG image of the molecule and encodes it in base64 format for rendering on the web.
Routes:

/: Renders the home page (index.html).
/predict: Accepts a POST request with a SMILES string.
Featurizes the molecule using DeepChem's MolGraphConvFeaturizer.
Runs predictions on all loaded models.
Returns class probabilities sorted in descending order.
Error Handling & Logging:

Catches errors during model loading, featurization, and prediction.
Provides clear error messages for invalid SMILES or prediction failures.
Flask Configuration:

Uses Flask-CORS for handling cross-origin requests.
Supports environment-based debug mode and dynamic port configuration.
Example Input/Output
Input: SMILES string (e.g., CCO)
Output:
Predicted class probabilities (A: 85.5%, B: 12.4%, etc.)
Image of the molecule structure

