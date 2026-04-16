import os
import sys

# Ensure we can import from the directory
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir)

from diseases import diseases
from symptoms import symptoms
from mappings import disease_symptom_mapping

def validate_data():
    print("Running Knowledge Base Validation...")
    print("-" * 40)

    # 1. Count checks
    print(f"Diseases count: {len(diseases)}")
    print(f"Symptoms count: {len(symptoms)}")
    
    if len(diseases) < 60:
        print("WARNING: Disease count is less than 60")
    if len(symptoms) < 100:
        print("WARNING: Symptom count is less than 100")

    # 2. Duplicate checks
    disease_ids = list(diseases.keys())
    symptom_codes = list(symptoms.keys())
    
    if len(disease_ids) != len(set(disease_ids)):
        print("ERROR: Duplicate Disease IDs found!")
    
    if len(symptom_codes) != len(set(symptom_codes)):
        print("ERROR: Duplicate Symptom Codes found!")

    # 3. Mapping Integrity
    invalid_mappings = 0
    missing_mappings = 0
    
    for d_id, d_maps in disease_symptom_mapping.items():
        if d_id not in diseases:
            print(f"ERROR: Mapping exists for unknown disease ID: {d_id}")
            invalid_mappings += 1
        
        for m in d_maps:
            if m['symptom_code'] not in symptoms:
                print(f"ERROR: Disease {d_id} maps to unknown symptom: {m['symptom_code']}")
                invalid_mappings += 1

    # Check if all diseases have mappings
    for d_id in diseases:
        if d_id not in disease_symptom_mapping:
            print(f"WARNING: Disease {d_id} ({diseases[d_id]['name']}) has no symptom mappings.")
            missing_mappings += 1

    print("-" * 40)
    if invalid_mappings == 0:
        print("SUCCESS: All mappings reference valid IDs.")
    else:
        print(f"FAILURE: Found {invalid_mappings} invalid mappings.")

    if missing_mappings > 0:
        print(f"NOTE: {missing_mappings} diseases have no mapped symptoms.")

    # 4. Demo One Disease
    demo_id = "D011" # Heart Attack
    if demo_id in diseases and demo_id in disease_symptom_mapping:
        print("-" * 40)
        print("DEMO: Displaying data for Heart Attack")
        d = diseases[demo_id]
        print(f"ID: {demo_id}")
        print(f"Name: {d['name']}")
        print(f"Category: {d['category']}")
        print(f"Severity: {d['severity']}")
        print("Symptoms:")
        for m in disease_symptom_mapping[demo_id]:
            s_code = m['symptom_code']
            s = symptoms[s_code]
            primary_str = "(Primary)" if m['is_primary'] else ""
            print(f"  - {s['name']} [{s_code}] {primary_str} (Prob: {m['probability']})")
            
if __name__ == "__main__":
    validate_data()
