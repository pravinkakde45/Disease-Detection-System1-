import sys
import json
import pickle
import numpy as np
import os

# Load Model
model_path = os.path.join(os.path.dirname(__file__), 'model.pkl')
index_path = os.path.join(os.path.dirname(__file__), 'symptom_index.pkl')

try:
    with open(model_path, 'rb') as f:
        model = pickle.load(f)
    with open(index_path, 'rb') as f:
        symptom_index = pickle.load(f)
except FileNotFoundError:
    print(json.dumps({"error": "Model not found. Please train first."}))
    sys.exit(1)

def predict():
    try:
        # Read input from stdin
        input_data = sys.stdin.read()
        if not input_data:
            return

        request = json.loads(input_data)
        user_symptoms = request.get('symptoms', []) # List of symptom codes e.g. ['fever', 'cough']
        
        # Create feature vector
        vector = [0] * len(symptom_index)
        for s in user_symptoms:
            if s in symptom_index:
                idx = symptom_index.index(s)
                vector[idx] = 1
        
        # Predict Probabilities
        probs = model.predict_proba([vector])[0]
        classes = model.classes_
        
        # Get Top 3
        top_indices = np.argsort(probs)[-3:][::-1]
        
        results = []
        for i in top_indices:
            if probs[i] > 0.01: # Filter very low probs
                results.append({
                    "name": classes[i],
                    "confidence": round(probs[i] * 100, 2)
                })
        
        response = {
            "primary_disease": results[0]['name'] if results else "Unknown",
            "confidence": results[0]['confidence'] if results else 0,
            "possible_diseases": results[1:],
            "recommendation": "Consult a physician if symptoms persist."
        }
        
        print(json.dumps(response))
        
    except Exception as e:
        print(json.dumps({"error": str(e)}))

if __name__ == "__main__":
    predict()
