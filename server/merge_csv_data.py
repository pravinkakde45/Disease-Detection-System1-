import pandas as pd
import os
import sys

# Set up paths
current_dir = os.path.dirname(os.path.abspath(__file__))
# The python maps are in ../backend/ml/data
sys.path.append(os.path.join(current_dir, '../backend/ml/data'))
csv_path = os.path.join(current_dir, '../Disease and symptoms dataset.csv')

# Load existing maps
try:
    from disease_symptom_map import disease_map
except ImportError:
    print("Could not import disease_map")
    sys.exit(1)

try:
    from symptoms import symptoms
except ImportError:
    print("Could not import symptoms")
    sys.exit(1)

disease_map_file = os.path.join(current_dir, '../backend/ml/data', 'disease_symptom_map.py')
symptoms_file = os.path.join(current_dir, '../backend/ml/data', 'symptoms.py')

print(f"Loading dataset from: {csv_path}")
df = pd.read_csv(csv_path)

# Ensure "diseases" column exists
disease_col = 'diseases'
if disease_col not in df.columns:
    disease_col = df.columns[0] # Assuming first col is the target if not named precisely

# 1. Update Symptoms
existing_symptoms = [k.replace('_', ' ').lower() for k in symptoms.keys()]
new_symptoms_list = [c for c in df.columns if c != disease_col and c.replace('_', ' ').lower() not in existing_symptoms]

print(f"Found {len(new_symptoms_list)} new symptoms. Appending to symptoms.py...")

with open(symptoms_file, 'a', encoding='utf-8') as f:
    f.write("\n# --- Auto-merged from CSV ---\n")
    for s in new_symptoms_list:
        code = s.replace(' ', '_').replace('(', '').replace(')', '').replace('-', '_').lower()
        if code not in symptoms:
            name_clean = s.replace('"', '').title()
            f.write(f'symptoms["{code}"] = {{\n')
            f.write(f'    "name": "{name_clean}",\n')
            f.write(f'    "category": "CSV_Import",\n')
            f.write(f'    "severity": "moderate",\n')
            f.write(f'    "question_text": "Do you have {name_clean.lower()}?",\n')
            f.write(f'    "description": "Imported from CSV."\n')
            f.write('}\n')

# 2. Update Disease Map
existing_diseases_lower = [v['name'].lower() for v in disease_map.values()]
grouped = df.groupby(disease_col).mean()

new_disease_count = 0
print("Appending new diseases to disease_symptom_map.py...")

with open(disease_map_file, 'a', encoding='utf-8') as f:
    f.write("\n# --- Auto-merged from CSV ---\n")
    for disease_name in grouped.index:
        d_lower = str(disease_name).lower()
        
        # Avoid duplicate merging of same disease conceptually
        if any(d_lower in d for d in existing_diseases_lower) or any(d in d_lower for d in existing_diseases_lower):
            continue

        row = grouped.loc[disease_name]
        
        primary = [s.replace(' ', '_').replace('(', '').replace(')', '').replace('-', '_').lower() for s, v in row.items() if v >= 0.7]
        secondary = [s.replace(' ', '_').replace('(', '').replace(')', '').replace('-', '_').lower() for s, v in row.items() if 0.4 <= v < 0.7]
        rare = [s.replace(' ', '_').replace('(', '').replace(')', '').replace('-', '_').lower() for s, v in row.items() if 0.05 <= v < 0.4]
        weights = {s.replace(' ', '_').replace('(', '').replace(')', '').replace('-', '_').lower(): round(v, 2) for s,v in row.items() if v >= 0.05}

        if len(weights) == 0:
            continue

        new_disease_count += 1
        d_id = f"CSV_{new_disease_count:04d}"
        
        d_clean = str(disease_name).replace('"', '').title()
        
        f.write(f'disease_map["{d_id}"] = {{\n')
        f.write(f'    "name": "{d_clean}",\n')
        f.write(f'    "primary_symptoms": {primary},\n')
        f.write(f'    "secondary_symptoms": {secondary},\n')
        f.write(f'    "rare_symptoms": {rare},\n')
        f.write(f'    "symptom_weights": {weights}\n')
        f.write('}\n')

print(f"Added {new_disease_count} new diseases to disease_map.")
print("Merge script executed successfully!")
