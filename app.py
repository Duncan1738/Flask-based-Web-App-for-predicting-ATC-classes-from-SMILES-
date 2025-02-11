from flask import Flask, request, jsonify, render_template
import torch
from dotenv import load_dotenv
import numpy as np
from rdkit import Chem
from rdkit.Chem import Draw
import base64
from io import BytesIO
import deepchem as dc
import os
from flask_cors import CORS

load_dotenv()

app = Flask(__name__)
CORS(app)

app.config['DEBUG'] = os.environ.get('FLASK_DEBUG', 'False') == 'True'
classes = ['A', 'B', 'C', 'D', 'G', 'H', 'J', 'L', 'M', 'N', 'P', 'R', 'S', 'V']
model_dir = 'last_final_atc_property_prediction_models/'
atc_models = {}

for cls in classes:
    model_path = os.path.join(model_dir, f'model_gcn_{cls}.pt')
    try:
        model = dc.models.GCNModel(mode='classification', n_tasks=1, batch_size=64, learning_rate=0.001)
        model.model.load_state_dict(torch.load(model_path, map_location=torch.device('cpu')))
        atc_models[cls] = model
        print(f"Model for class {cls} loaded successfully from {model_path}")
    except Exception as e:
        print(f"Error loading model weights for class {cls}: {e}")

def draw_smiles(smiles):
    mol = Chem.MolFromSmiles(smiles)
    if mol is None:
        return None
    img = Draw.MolToImage(mol)
    buffered = BytesIO()
    img.save(buffered, format="PNG")
    img_str = base64.b64encode(buffered.getvalue()).decode('utf-8')
    return img_str

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    smiles = request.form['smiles']
    if not smiles:
        return jsonify({'error': 'No SMILES provided'}), 400

    smiles_img = draw_smiles(smiles)
    if smiles_img is None:
        return jsonify({'error': 'Invalid SMILES string'}), 400

    mol = Chem.MolFromSmiles(smiles)
    if mol is None:
        return jsonify({'error': 'Invalid SMILES string'}), 400

    featurizer = dc.feat.MolGraphConvFeaturizer()
    new_features = featurizer.featurize([mol])

    if new_features is None:
        return jsonify({'error': 'Invalid molecule for prediction'}), 400
    
    results = []
    for cls, model in atc_models.items():
        try:
            new_dataset = dc.data.NumpyDataset(X=new_features)
            prob = model.predict(new_dataset)
            percentage_prob = prob[0][0] * 100
            results.append({'class': cls, 'probability': round(percentage_prob, 2)})
        except Exception as e:
            print(f"Error with class {cls}: {str(e)}")
            continue

    results = sorted(results, key=lambda x: x['probability'], reverse=True)
    return render_template('results.html', smiles=smiles, smiles_img=smiles_img, results=results)

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
