import pandas as pd
import numpy as np
import pickle
import random
import os
import sys

# Add path to load data modules
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(current_dir, 'data'))
from disease_symptom_map import disease_map
from symptoms import symptoms

# Extract all unique symptoms from our master symptom list
ALL_SYMPTOMS = list(symptoms.keys())

def generate_synthetic_data():
    disease_ids = list(disease_map.keys())
    # Generate 15 samples per disease to ensure we don't hit MemoryError
    num_samples = max(5000, len(disease_ids) * 15)
    print(f"Generating {num_samples} Synthetic Patient Data for {len(disease_ids)} diseases...")
    
    data = []
    labels = []
    
    # Get disease keys from map
    disease_ids = list(disease_map.keys())
    
    for _ in range(num_samples):
        # Pick a random disease as the ground truth
        d_id = random.choice(disease_ids)
        d_info = disease_map[d_id]
        
        # Create a sample vector (all 0s initially)
        # Using a list comprehension to ensure order matches ALL_SYMPTOMS
        sample_vector = [0] * len(ALL_SYMPTOMS)
        
        # Helper to set symptom
        def activate_symptom(s_code, probability):
             if s_code in ALL_SYMPTOMS and random.random() < probability:
                 idx = ALL_SYMPTOMS.index(s_code)
                 sample_vector[idx] = 1

        # Primary symptoms (High probability ~90%)
        for s in d_info['primary_symptoms']:
             activate_symptom(s, 0.9)
        
        # Secondary symptoms (Medium probability ~60%)
        for s in d_info['secondary_symptoms']:
             activate_symptom(s, 0.6)

        # Rare symptoms (Low probability ~20%)
        for s in d_info['rare_symptoms']:
             activate_symptom(s, 0.2)
        
        # Random noise (user might click wrong symptom)
        noise_symptom = random.choice(ALL_SYMPTOMS)
        activate_symptom(noise_symptom, 0.05)

        data.append(sample_vector)
        labels.append(d_info['name'])
        
    return np.array(data), np.array(labels)

if __name__ == "__main__":
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.model_selection import train_test_split
    from sklearn.metrics import accuracy_score
    
    X, y = generate_synthetic_data()
    
    print(f"Dataset Shape: {X.shape}")
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    print("Training Random Forest Classifier...")
    clf = RandomForestClassifier(n_estimators=100, random_state=42)
    clf.fit(X_train, y_train)
    
    y_pred = clf.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    print(f"Model Accuracy on Synthetic Test Set: {acc * 100:.2f}%")
    
    # Save Model and Symptom List for persistence
    print("Saving Model...")
    with open(os.path.join(current_dir, 'model.pkl'), 'wb') as f:
        pickle.dump(clf, f)
        
    with open(os.path.join(current_dir, 'symptom_index.pkl'), 'wb') as f:
        pickle.dump(ALL_SYMPTOMS, f)
        
    print("Model Training Complete!")
