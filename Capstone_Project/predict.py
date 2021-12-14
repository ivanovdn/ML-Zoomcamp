import pickle
from flask import Flask, request
import numpy as np

with open('capstone_model.pkl', 'rb') as f:
    model = pickle.load(f)
    
app = Flask('predict')

@app.route('/predict', methods=['POST'])  
def predict():
    patient = request.get_json()
    patient = np.array(list(patient.values())).reshape(1, len(patient))
    y_pred = model.predict_proba(patient)[:, 1]
    diabet = y_pred >= 0.5 
    
    result = {
        'diabet_probability': float(y_pred),
        'diabet': bool(diabet)
    }
    return result
    

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=9696)    
