# Disease Symptom Mappings (Advanced)
# Maps diseases to their symptom profile for the question engine.

disease_map = {
    "D001": { # Common Cold
        "name": "Common Cold",
        "primary_symptoms": ["cough", "runny_nose", "sore_throat"],
        "secondary_symptoms": ["sneezing", "fever", "fatigue"],
        "rare_symptoms": ["headache"],
        "symptom_weights": {
            "runny_nose": 0.9, "cough": 0.8, "sore_throat": 0.8, "sneezing": 0.7,
            "fever": 0.3, "fatigue": 0.4
        }
    },
    "D002": { # Influenza
        "name": "Influenza (Flu)",
        "primary_symptoms": ["fever", "chills", "muscle_pain", "fatigue"],
        "secondary_symptoms": ["cough", "headache", "sore_throat"],
        "rare_symptoms": ["vomiting"],
        "symptom_weights": {
            "fever": 0.9, "muscle_pain": 0.9, "fatigue": 0.9, "chills": 0.8,
            "cough": 0.7, "headache": 0.6
        }
    },
    "D003": { # Asthma
        "name": "Asthma",
        "primary_symptoms": ["wheezing", "shortness_of_breath", "chest_tightness"],
        "secondary_symptoms": ["cough"],
        "rare_symptoms": ["anxiety"],
        "symptom_weights": {
            "wheezing": 0.95, "shortness_of_breath": 0.9, "chest_tightness": 0.8,
            "cough": 0.6
        }
    },
    "D004": { # Pneumonia
        "name": "Pneumonia",
        "primary_symptoms": ["cough", "fever", "shortness_of_breath", "chest_pain"],
        "secondary_symptoms": ["chills", "fatigue", "nausea"],
        "rare_symptoms": ["confusion"],
        "symptom_weights": {
            "cough": 0.9, "fever": 0.9, "shortness_of_breath": 0.85, "chest_pain": 0.7,
            "chills": 0.6
        }
    },
    "D008": { # Covid-19
        "name": "Covid-19",
        "primary_symptoms": ["fever", "cough", "loss_of_smell", "fatigue"],
        "secondary_symptoms": ["shortness_of_breath", "sore_throat", "headache", "muscle_pain"],
        "rare_symptoms": ["diarrhea", "rash"],
        "symptom_weights": {
            "loss_of_smell": 0.95, "fever": 0.8, "cough": 0.8, "fatigue": 0.7,
            "shortness_of_breath": 0.6
        }
    },
    "D011": { # Heart Attack
        "name": "Heart Attack",
        "primary_symptoms": ["chest_pain", "shortness_of_breath", "nausea", "cold_intolerance"], # using cold_intol as night_sweat/cold_sweat proxy for now
        "secondary_symptoms": ["dizziness", "fatigue", "anxiety"],
        "rare_symptoms": ["vomiting"],
        "symptom_weights": {
            "chest_pain": 0.98, "shortness_of_breath": 0.85, "nausea": 0.6,
            "dizziness": 0.5
        }
    },
    "D014": { # Gastroenteritis
        "name": "Gastroenteritis",
        "primary_symptoms": ["diarrhea", "vomiting", "nausea", "abdominal_pain"],
        "secondary_symptoms": ["fever", "headache", "muscle_pain"],
        "rare_symptoms": ["dehydration"],
        "symptom_weights": {
            "diarrhea": 0.9, "vomiting": 0.9, "nausea": 0.8, "abdominal_pain": 0.7,
            "fever": 0.5
        }
    },
    "D021": { # Migraine
        "name": "Migraine",
        "primary_symptoms": ["headache", "nausea", "vision_changes"],
        "secondary_symptoms": ["vomiting", "dizziness"],
        "rare_symptoms": ["confusion"],
        "symptom_weights": {
            "headache": 0.95, "nausea": 0.8, "vision_changes": 0.7,
            "vomiting": 0.6
        }
    },
    "D027": { # Diabetes Type 1
        "name": "Diabetes Type 1",
        "primary_symptoms": ["excessive_thirst", "frequent_urination", "weight_loss"],
        "secondary_symptoms": ["fatigue", "blurred_vision"],
        "rare_symptoms": ["nausea"],
        "symptom_weights": {
            "excessive_thirst": 0.9, "frequent_urination": 0.9, "weight_loss": 0.8,
            "fatigue": 0.5
        }
    },
    "D041": { # Depression
        "name": "Major Depressive Disorder",
        "primary_symptoms": ["depressed_mood", "fatigue", "insomnia"],
        "secondary_symptoms": ["weight_loss", "anxiety"],
        "rare_symptoms": ["headache"],
        "symptom_weights": {
            "depressed_mood": 0.95, "fatigue": 0.8, "insomnia": 0.7,
            "weight_loss": 0.5
        }
    },
    "D051": { # UTI
        "name": "Urinary Tract Infection",
        "primary_symptoms": ["painful_urination", "frequent_urination"],
        "secondary_symptoms": ["abdominal_pain", "fever"],
        "rare_symptoms": ["blood_in_urine"],
        "symptom_weights": {
            "painful_urination": 0.9, "frequent_urination": 0.85, "abdominal_pain": 0.5,
            "fever": 0.4
        }
    },
    "D058": { # Meningitis
        "name": "Meningitis",
        "primary_symptoms": ["headache", "stiff_neck", "fever", "confusion"],
        "secondary_symptoms": ["nausea", "vomiting", "sensitivity_to_light"],
        "rare_symptoms": ["seizures"],
        "symptom_weights": {
            "stiff_neck": 0.95, "headache": 0.9, "fever": 0.85, "confusion": 0.7,
            "nausea": 0.6
        }
    }
}

# --- Auto-merged from CSV ---
disease_map["CSV_0001"] = {
    "name": "Abdominal Aortic Aneurysm",
    "primary_symptoms": ['shortness_of_breath', 'palpitations', 'arm_swelling', 'burning_abdominal_pain'],
    "secondary_symptoms": ['sharp_abdominal_pain', 'back_pain'],
    "rare_symptoms": [],
    "symptom_weights": {'shortness_of_breath': 0.76, 'palpitations': 0.8, 'sharp_abdominal_pain': 0.57, 'arm_swelling': 0.76, 'back_pain': 0.47, 'burning_abdominal_pain': 0.79}
}
disease_map["CSV_0002"] = {
    "name": "Abdominal Hernia",
    "primary_symptoms": ['symptoms_of_the_scrotum_and_testes', 'lower_abdominal_pain'],
    "secondary_symptoms": ['groin_mass', 'sharp_abdominal_pain', 'regurgitation', 'ache_all_over', 'upper_abdominal_pain', 'swollen_abdomen', 'regurgitation.1', 'irregular_belly_button'],
    "rare_symptoms": [],
    "symptom_weights": {'groin_mass': 0.53, 'symptoms_of_the_scrotum_and_testes': 0.75, 'sharp_abdominal_pain': 0.59, 'lower_abdominal_pain': 0.71, 'regurgitation': 0.52, 'ache_all_over': 0.54, 'upper_abdominal_pain': 0.56, 'swollen_abdomen': 0.54, 'regurgitation.1': 0.52, 'irregular_belly_button': 0.57}
}
disease_map["CSV_0003"] = {
    "name": "Abscess Of Nose",
    "primary_symptoms": ['irritable_infant', 'vomiting'],
    "secondary_symptoms": ['sore_throat', 'cough', 'nasal_congestion', 'fever', 'coryza', 'sinus_congestion'],
    "rare_symptoms": [],
    "symptom_weights": {'sore_throat': 0.53, 'cough': 0.5, 'nasal_congestion': 0.53, 'irritable_infant': 0.78, 'vomiting': 0.81, 'fever': 0.5, 'coryza': 0.52, 'sinus_congestion': 0.51}
}
disease_map["CSV_0004"] = {
    "name": "Abscess Of The Lung",
    "primary_symptoms": ['shortness_of_breath', 'depressive_or_psychotic_symptoms', 'itchy_eyelid'],
    "secondary_symptoms": ['cough'],
    "rare_symptoms": [],
    "symptom_weights": {'shortness_of_breath': 0.89, 'depressive_or_psychotic_symptoms': 1.0, 'cough': 0.42, 'itchy_eyelid': 0.79}
}
disease_map["CSV_0005"] = {
    "name": "Abscess Of The Pharynx",
    "primary_symptoms": ['sharp_chest_pain', 'headache'],
    "secondary_symptoms": ['sore_throat', 'cough', 'nasal_congestion', 'throat_swelling', 'difficulty_in_swallowing', 'fever'],
    "rare_symptoms": [],
    "symptom_weights": {'sharp_chest_pain': 0.78, 'sore_throat': 0.53, 'cough': 0.49, 'nasal_congestion': 0.49, 'throat_swelling': 0.7, 'difficulty_in_swallowing': 0.5, 'headache': 0.73, 'fever': 0.51}
}
disease_map["CSV_0006"] = {
    "name": "Acanthosis Nigricans",
    "primary_symptoms": ['acne_or_pimples', 'skin_growth'],
    "secondary_symptoms": ['skin_lesion', 'weight_gain'],
    "rare_symptoms": [],
    "symptom_weights": {'skin_lesion': 0.63, 'acne_or_pimples': 0.83, 'skin_growth': 0.87, 'weight_gain': 0.63}
}
disease_map["CSV_0007"] = {
    "name": "Acariasis",
    "primary_symptoms": ['emotional_symptoms', 'swelling_of_scrotum'],
    "secondary_symptoms": ['itching_of_skin', 'skin_rash'],
    "rare_symptoms": [],
    "symptom_weights": {'emotional_symptoms': 0.92, 'swelling_of_scrotum': 0.72, 'itching_of_skin': 0.47, 'skin_rash': 0.47}
}
disease_map["CSV_0008"] = {
    "name": "Achalasia",
    "primary_symptoms": ['chest_tightness', 'cough'],
    "secondary_symptoms": ['sharp_chest_pain', 'throat_feels_tight', 'difficulty_in_swallowing'],
    "rare_symptoms": [],
    "symptom_weights": {'sharp_chest_pain': 0.5, 'chest_tightness': 0.85, 'cough': 0.77, 'throat_feels_tight': 0.68, 'difficulty_in_swallowing': 0.52}
}
disease_map["CSV_0009"] = {
    "name": "Acne",
    "primary_symptoms": [],
    "secondary_symptoms": ['skin_swelling', 'abnormal_appearing_skin', 'acne_or_pimples', 'skin_growth', 'irregular_appearing_scalp', 'skin_moles', 'long_menstrual_periods', 'skin_dryness,_peeling,_scaliness,_or_roughness', 'skin_rash'],
    "rare_symptoms": [],
    "symptom_weights": {'skin_swelling': 0.5, 'abnormal_appearing_skin': 0.55, 'acne_or_pimples': 0.51, 'skin_growth': 0.5, 'irregular_appearing_scalp': 0.69, 'skin_moles': 0.51, 'long_menstrual_periods': 0.67, 'skin_dryness,_peeling,_scaliness,_or_roughness': 0.68, 'skin_rash': 0.53}
}
disease_map["CSV_0010"] = {
    "name": "Actinic Keratosis",
    "primary_symptoms": [],
    "secondary_symptoms": ['skin_swelling', 'abnormal_appearing_skin', 'skin_lesion', 'skin_growth', 'irregular_appearing_scalp', 'skin_moles', 'symptoms_of_the_face', 'itching_of_skin', 'skin_dryness,_peeling,_scaliness,_or_roughness', 'skin_irritation', 'skin_rash'],
    "rare_symptoms": [],
    "symptom_weights": {'skin_swelling': 0.5, 'abnormal_appearing_skin': 0.5, 'skin_lesion': 0.49, 'skin_growth': 0.5, 'irregular_appearing_scalp': 0.53, 'skin_moles': 0.52, 'symptoms_of_the_face': 0.7, 'itching_of_skin': 0.51, 'skin_dryness,_peeling,_scaliness,_or_roughness': 0.52, 'skin_irritation': 0.5, 'skin_rash': 0.5}
}
disease_map["CSV_0011"] = {
    "name": "Acute Bronchiolitis",
    "primary_symptoms": [],
    "secondary_symptoms": ['shortness_of_breath', 'cough', 'nasal_congestion', 'irritable_infant', 'vomiting', 'wheezing', 'decreased_appetite', 'fever', 'difficulty_breathing', 'coryza', 'pulling_at_ears', 'hurts_to_breath'],
    "rare_symptoms": [],
    "symptom_weights": {'shortness_of_breath': 0.48, 'cough': 0.51, 'nasal_congestion': 0.52, 'irritable_infant': 0.49, 'vomiting': 0.52, 'wheezing': 0.52, 'decreased_appetite': 0.51, 'fever': 0.52, 'difficulty_breathing': 0.5, 'coryza': 0.48, 'pulling_at_ears': 0.49, 'hurts_to_breath': 0.51}
}
disease_map["CSV_0012"] = {
    "name": "Acute Bronchitis",
    "primary_symptoms": [],
    "secondary_symptoms": ['shortness_of_breath', 'sharp_chest_pain', 'sore_throat', 'cough', 'nasal_congestion', 'headache', 'wheezing', 'fever', 'difficulty_breathing', 'coughing_up_sputum', 'coryza', 'congestion_in_chest'],
    "rare_symptoms": [],
    "symptom_weights": {'shortness_of_breath': 0.49, 'sharp_chest_pain': 0.5, 'sore_throat': 0.51, 'cough': 0.52, 'nasal_congestion': 0.52, 'headache': 0.52, 'wheezing': 0.5, 'fever': 0.52, 'difficulty_breathing': 0.49, 'coughing_up_sputum': 0.5, 'coryza': 0.52, 'congestion_in_chest': 0.5}
}
disease_map["CSV_0013"] = {
    "name": "Acute Bronchospasm",
    "primary_symptoms": [],
    "secondary_symptoms": ['shortness_of_breath', 'sharp_chest_pain', 'chest_tightness', 'sore_throat', 'cough', 'nasal_congestion', 'vomiting', 'wheezing', 'fever', 'difficulty_breathing', 'coryza'],
    "rare_symptoms": [],
    "symptom_weights": {'shortness_of_breath': 0.49, 'sharp_chest_pain': 0.51, 'chest_tightness': 0.49, 'sore_throat': 0.52, 'cough': 0.53, 'nasal_congestion': 0.51, 'vomiting': 0.69, 'wheezing': 0.52, 'fever': 0.5, 'difficulty_breathing': 0.52, 'coryza': 0.49}
}
disease_map["CSV_0014"] = {
    "name": "Acute Fatty Liver Of Pregnancy (Aflp)",
    "primary_symptoms": ['emotional_symptoms', 'sharp_abdominal_pain'],
    "secondary_symptoms": [],
    "rare_symptoms": [],
    "symptom_weights": {'emotional_symptoms': 1.0, 'sharp_abdominal_pain': 0.89}
}
disease_map["CSV_0015"] = {
    "name": "Acute Glaucoma",
    "primary_symptoms": ['double_vision'],
    "secondary_symptoms": ['diminished_vision', 'symptoms_of_eye', 'pain_in_eye', 'foreign_body_sensation_in_eye', 'spots_or_clouds_in_vision', 'eye_redness', 'blindness'],
    "rare_symptoms": [],
    "symptom_weights": {'diminished_vision': 0.57, 'double_vision': 0.73, 'symptoms_of_eye': 0.54, 'pain_in_eye': 0.57, 'foreign_body_sensation_in_eye': 0.7, 'spots_or_clouds_in_vision': 0.47, 'eye_redness': 0.5, 'blindness': 0.49}
}
disease_map["CSV_0016"] = {
    "name": "Acute Kidney Injury",
    "primary_symptoms": [],
    "secondary_symptoms": ['shortness_of_breath', 'sharp_chest_pain', 'dizziness', 'retention_of_urine', 'sharp_abdominal_pain', 'vomiting', 'nausea', 'peripheral_edema', 'weakness', 'kidney_mass', 'symptoms_of_the_kidneys'],
    "rare_symptoms": [],
    "symptom_weights": {'shortness_of_breath': 0.5, 'sharp_chest_pain': 0.5, 'dizziness': 0.49, 'retention_of_urine': 0.68, 'sharp_abdominal_pain': 0.5, 'vomiting': 0.53, 'nausea': 0.52, 'peripheral_edema': 0.5, 'weakness': 0.54, 'kidney_mass': 0.5, 'symptoms_of_the_kidneys': 0.48}
}
disease_map["CSV_0017"] = {
    "name": "Acute Otitis Media",
    "primary_symptoms": [],
    "secondary_symptoms": ['sore_throat', 'cough', 'nasal_congestion', 'diminished_hearing', 'ear_pain', 'plugged_feeling_in_ear', 'fluid_in_ear', 'fever', 'coryza', 'redness_in_ear'],
    "rare_symptoms": [],
    "symptom_weights": {'sore_throat': 0.49, 'cough': 0.5, 'nasal_congestion': 0.5, 'diminished_hearing': 0.66, 'ear_pain': 0.5, 'plugged_feeling_in_ear': 0.53, 'fluid_in_ear': 0.49, 'fever': 0.52, 'coryza': 0.65, 'redness_in_ear': 0.52}
}
disease_map["CSV_0018"] = {
    "name": "Acute Pancreatitis",
    "primary_symptoms": [],
    "secondary_symptoms": ['sharp_chest_pain', 'abusing_alcohol', 'sharp_abdominal_pain', 'vomiting', 'nausea', 'diarrhea', 'back_pain', 'burning_abdominal_pain', 'side_pain', 'lower_body_pain', 'upper_abdominal_pain', 'hemoptysis'],
    "rare_symptoms": [],
    "symptom_weights": {'sharp_chest_pain': 0.49, 'abusing_alcohol': 0.51, 'sharp_abdominal_pain': 0.5, 'vomiting': 0.51, 'nausea': 0.52, 'diarrhea': 0.51, 'back_pain': 0.5, 'burning_abdominal_pain': 0.53, 'side_pain': 0.49, 'lower_body_pain': 0.5, 'upper_abdominal_pain': 0.5, 'hemoptysis': 0.51}
}
disease_map["CSV_0019"] = {
    "name": "Acute Respiratory Distress Syndrome (Ards)",
    "primary_symptoms": ['chills'],
    "secondary_symptoms": ['shortness_of_breath', 'depressive_or_psychotic_symptoms', 'sharp_chest_pain', 'chest_tightness', 'cough', 'wheezing', 'fever', 'difficulty_breathing'],
    "rare_symptoms": [],
    "symptom_weights": {'shortness_of_breath': 0.49, 'depressive_or_psychotic_symptoms': 0.51, 'sharp_chest_pain': 0.52, 'chest_tightness': 0.65, 'cough': 0.51, 'wheezing': 0.52, 'fever': 0.52, 'difficulty_breathing': 0.52, 'chills': 0.75}
}
disease_map["CSV_0020"] = {
    "name": "Acute Sinusitis",
    "primary_symptoms": [],
    "secondary_symptoms": ['sore_throat', 'cough', 'nasal_congestion', 'facial_pain', 'ear_pain', 'frontal_headache', 'fever', 'coughing_up_sputum', 'coryza', 'sinus_congestion', 'painful_sinuses'],
    "rare_symptoms": [],
    "symptom_weights": {'sore_throat': 0.66, 'cough': 0.51, 'nasal_congestion': 0.49, 'facial_pain': 0.51, 'ear_pain': 0.53, 'frontal_headache': 0.52, 'fever': 0.5, 'coughing_up_sputum': 0.5, 'coryza': 0.54, 'sinus_congestion': 0.53, 'painful_sinuses': 0.47}
}
disease_map["CSV_0021"] = {
    "name": "Acute Stress Reaction",
    "primary_symptoms": [],
    "secondary_symptoms": ['anxiety_and_nervousness', 'depression', 'shortness_of_breath', 'depressive_or_psychotic_symptoms', 'sharp_chest_pain', 'dizziness', 'insomnia', 'abnormal_involuntary_movements', 'headache', 'burning_abdominal_pain', 'fatigue'],
    "rare_symptoms": [],
    "symptom_weights": {'anxiety_and_nervousness': 0.49, 'depression': 0.5, 'shortness_of_breath': 0.49, 'depressive_or_psychotic_symptoms': 0.51, 'sharp_chest_pain': 0.53, 'dizziness': 0.51, 'insomnia': 0.5, 'abnormal_involuntary_movements': 0.67, 'headache': 0.52, 'burning_abdominal_pain': 0.51, 'fatigue': 0.51}
}
disease_map["CSV_0022"] = {
    "name": "Adhesive Capsulitis Of The Shoulder",
    "primary_symptoms": ['arm_pain', 'muscle_pain'],
    "secondary_symptoms": ['neck_pain', 'shoulder_pain', 'shoulder_stiffness_or_tightness', 'ache_all_over'],
    "rare_symptoms": [],
    "symptom_weights": {'arm_pain': 0.75, 'neck_pain': 0.53, 'muscle_pain': 0.89, 'shoulder_pain': 0.51, 'shoulder_stiffness_or_tightness': 0.59, 'ache_all_over': 0.52}
}
disease_map["CSV_0023"] = {
    "name": "Adjustment Reaction",
    "primary_symptoms": ['delusions_or_hallucinations'],
    "secondary_symptoms": ['anxiety_and_nervousness', 'depression', 'insomnia', 'hostile_behavior', 'restlessness', 'excessive_anger', 'fears_and_phobias', 'nightmares'],
    "rare_symptoms": [],
    "symptom_weights": {'anxiety_and_nervousness': 0.5, 'depression': 0.67, 'insomnia': 0.69, 'hostile_behavior': 0.53, 'restlessness': 0.5, 'excessive_anger': 0.5, 'delusions_or_hallucinations': 0.7, 'fears_and_phobias': 0.51, 'nightmares': 0.49}
}
disease_map["CSV_0024"] = {
    "name": "Adrenal Adenoma",
    "primary_symptoms": ['anxiety_and_nervousness', 'shortness_of_breath', 'back_weakness'],
    "secondary_symptoms": ['sharp_abdominal_pain'],
    "rare_symptoms": [],
    "symptom_weights": {'anxiety_and_nervousness': 0.86, 'shortness_of_breath': 0.91, 'back_weakness': 0.83, 'sharp_abdominal_pain': 0.57}
}
disease_map["CSV_0025"] = {
    "name": "Adrenal Cancer",
    "primary_symptoms": ['dizziness', 'diminished_hearing'],
    "secondary_symptoms": [],
    "rare_symptoms": [],
    "symptom_weights": {'dizziness': 1.0, 'diminished_hearing': 1.0}
}
disease_map["CSV_0026"] = {
    "name": "Alcohol Abuse",
    "primary_symptoms": [],
    "secondary_symptoms": ['anxiety_and_nervousness', 'depression', 'depressive_or_psychotic_symptoms', 'abusing_alcohol', 'hostile_behavior', 'drug_abuse', 'vomiting_blood', 'smoking_problems', 'low_self_esteem'],
    "rare_symptoms": [],
    "symptom_weights": {'anxiety_and_nervousness': 0.47, 'depression': 0.53, 'depressive_or_psychotic_symptoms': 0.48, 'abusing_alcohol': 0.49, 'hostile_behavior': 0.68, 'drug_abuse': 0.51, 'vomiting_blood': 0.68, 'smoking_problems': 0.68, 'low_self_esteem': 0.51}
}
disease_map["CSV_0027"] = {
    "name": "Alcohol Intoxication",
    "primary_symptoms": ['anxiety_and_nervousness', 'abnormal_involuntary_movements'],
    "secondary_symptoms": ['depression', 'depressive_or_psychotic_symptoms', 'sharp_chest_pain', 'abusing_alcohol', 'vomiting', 'problems_with_movement'],
    "rare_symptoms": [],
    "symptom_weights": {'anxiety_and_nervousness': 0.7, 'depression': 0.52, 'depressive_or_psychotic_symptoms': 0.56, 'sharp_chest_pain': 0.7, 'abnormal_involuntary_movements': 0.71, 'abusing_alcohol': 0.55, 'vomiting': 0.55, 'problems_with_movement': 0.69}
}
disease_map["CSV_0028"] = {
    "name": "Alcohol Withdrawal",
    "primary_symptoms": [],
    "secondary_symptoms": ['depressive_or_psychotic_symptoms', 'sharp_chest_pain', 'dizziness', 'abnormal_involuntary_movements', 'abusing_alcohol', 'fainting', 'vomiting', 'seizures', 'delusions_or_hallucinations', 'antisocial_behavior'],
    "rare_symptoms": [],
    "symptom_weights": {'depressive_or_psychotic_symptoms': 0.65, 'sharp_chest_pain': 0.51, 'dizziness': 0.67, 'abnormal_involuntary_movements': 0.51, 'abusing_alcohol': 0.52, 'fainting': 0.51, 'vomiting': 0.53, 'seizures': 0.53, 'delusions_or_hallucinations': 0.48, 'antisocial_behavior': 0.52}
}
disease_map["CSV_0029"] = {
    "name": "Alcoholic Liver Disease",
    "primary_symptoms": ['abnormal_involuntary_movements'],
    "secondary_symptoms": ['abusing_alcohol', 'sharp_abdominal_pain', 'diarrhea', 'peripheral_edema', 'weight_gain', 'stomach_bloating'],
    "rare_symptoms": [],
    "symptom_weights": {'abnormal_involuntary_movements': 0.78, 'abusing_alcohol': 0.51, 'sharp_abdominal_pain': 0.54, 'diarrhea': 0.65, 'peripheral_edema': 0.52, 'weight_gain': 0.68, 'stomach_bloating': 0.67}
}
disease_map["CSV_0030"] = {
    "name": "Allergy",
    "primary_symptoms": [],
    "secondary_symptoms": ['cough', 'skin_swelling', 'lip_swelling', 'abnormal_appearing_skin', 'peripheral_edema', 'itchiness_of_eye', 'allergic_reaction', 'fluid_retention', 'swollen_eye', 'itching_of_skin', 'skin_rash'],
    "rare_symptoms": [],
    "symptom_weights": {'cough': 0.48, 'skin_swelling': 0.52, 'lip_swelling': 0.49, 'abnormal_appearing_skin': 0.51, 'peripheral_edema': 0.52, 'itchiness_of_eye': 0.5, 'allergic_reaction': 0.52, 'fluid_retention': 0.67, 'swollen_eye': 0.48, 'itching_of_skin': 0.51, 'skin_rash': 0.5}
}
disease_map["CSV_0031"] = {
    "name": "Allergy To Animals",
    "primary_symptoms": ['sore_throat', 'cough', 'cross_eyed'],
    "secondary_symptoms": ['nasal_congestion', 'allergic_reaction'],
    "rare_symptoms": [],
    "symptom_weights": {'sore_throat': 0.97, 'cough': 0.79, 'nasal_congestion': 0.67, 'cross_eyed': 0.77, 'allergic_reaction': 0.67}
}
disease_map["CSV_0032"] = {
    "name": "Alopecia",
    "primary_symptoms": ['skin_swelling', 'itching_of_skin'],
    "secondary_symptoms": ['feeling_ill', 'acne_or_pimples', 'skin_growth', 'irregular_appearing_scalp', 'too_little_hair', 'skin_rash'],
    "rare_symptoms": [],
    "symptom_weights": {'skin_swelling': 0.72, 'feeling_ill': 0.51, 'acne_or_pimples': 0.69, 'skin_growth': 0.51, 'irregular_appearing_scalp': 0.53, 'itching_of_skin': 0.72, 'too_little_hair': 0.47, 'skin_rash': 0.53}
}
disease_map["CSV_0033"] = {
    "name": "Alzheimer Disease",
    "primary_symptoms": ['eye_burns_or_stings'],
    "secondary_symptoms": ['depression', 'depressive_or_psychotic_symptoms', 'difficulty_speaking', 'hostile_behavior', 'irregular_appearing_scalp', 'disturbance_of_memory', 'delusions_or_hallucinations'],
    "rare_symptoms": [],
    "symptom_weights": {'depression': 0.51, 'depressive_or_psychotic_symptoms': 0.55, 'difficulty_speaking': 0.54, 'hostile_behavior': 0.68, 'irregular_appearing_scalp': 0.68, 'eye_burns_or_stings': 0.75, 'disturbance_of_memory': 0.53, 'delusions_or_hallucinations': 0.54}
}
disease_map["CSV_0034"] = {
    "name": "Amblyopia",
    "primary_symptoms": ['pus_draining_from_ear', 'cross_eyed'],
    "secondary_symptoms": ['eye_deviation', 'diminished_vision', 'pain_in_eye'],
    "rare_symptoms": [],
    "symptom_weights": {'pus_draining_from_ear': 0.87, 'eye_deviation': 0.66, 'diminished_vision': 0.66, 'cross_eyed': 0.77, 'pain_in_eye': 0.53}
}
disease_map["CSV_0035"] = {
    "name": "Amyloidosis",
    "primary_symptoms": ['anxiety_and_nervousness', 'shortness_of_breath', 'wrist_weakness'],
    "secondary_symptoms": [],
    "rare_symptoms": [],
    "symptom_weights": {'anxiety_and_nervousness': 1.0, 'shortness_of_breath': 0.75, 'wrist_weakness': 1.0}
}
disease_map["CSV_0036"] = {
    "name": "Amyotrophic Lateral Sclerosis (Als)",
    "primary_symptoms": ['abnormal_involuntary_movements', 'difficulty_speaking', 'difficulty_in_swallowing', 'weakness', 'leg_cramps_or_spasms'],
    "secondary_symptoms": [],
    "rare_symptoms": [],
    "symptom_weights": {'abnormal_involuntary_movements': 0.9, 'difficulty_speaking': 0.82, 'difficulty_in_swallowing': 0.87, 'weakness': 0.7, 'leg_cramps_or_spasms': 0.73}
}
disease_map["CSV_0037"] = {
    "name": "Anal Fissure",
    "primary_symptoms": ['vaginal_dryness'],
    "secondary_symptoms": ['blood_in_stool', 'sharp_abdominal_pain', 'pain_of_the_anus', 'lower_body_pain', 'changes_in_stool_appearance', 'rectal_bleeding', 'constipation'],
    "rare_symptoms": [],
    "symptom_weights": {'blood_in_stool': 0.49, 'sharp_abdominal_pain': 0.54, 'vaginal_dryness': 0.84, 'pain_of_the_anus': 0.51, 'lower_body_pain': 0.5, 'changes_in_stool_appearance': 0.53, 'rectal_bleeding': 0.5, 'constipation': 0.48}
}
disease_map["CSV_0038"] = {
    "name": "Anal Fistula",
    "primary_symptoms": ['blood_in_stool', 'mass_in_scrotum'],
    "secondary_symptoms": ['pain_of_the_anus', 'rectal_bleeding'],
    "rare_symptoms": [],
    "symptom_weights": {'blood_in_stool': 0.85, 'mass_in_scrotum': 0.9, 'pain_of_the_anus': 0.55, 'rectal_bleeding': 0.65}
}
disease_map["CSV_0039"] = {
    "name": "Anemia",
    "primary_symptoms": ['changes_in_stool_appearance'],
    "secondary_symptoms": ['shortness_of_breath', 'dizziness', 'vomiting_blood', 'weakness', 'fatigue', 'melena', 'nosebleed'],
    "rare_symptoms": [],
    "symptom_weights": {'shortness_of_breath': 0.53, 'dizziness': 0.56, 'vomiting_blood': 0.68, 'weakness': 0.56, 'changes_in_stool_appearance': 0.77, 'fatigue': 0.49, 'melena': 0.56, 'nosebleed': 0.68}
}
disease_map["CSV_0040"] = {
    "name": "Anemia Due To Chronic Kidney Disease",
    "primary_symptoms": ['recent_weight_loss'],
    "secondary_symptoms": ['shortness_of_breath', 'peripheral_edema', 'weakness', 'fatigue', 'ankle_swelling'],
    "rare_symptoms": [],
    "symptom_weights": {'shortness_of_breath': 0.56, 'peripheral_edema': 0.54, 'recent_weight_loss': 0.84, 'weakness': 0.66, 'fatigue': 0.5, 'ankle_swelling': 0.48}
}
disease_map["CSV_0041"] = {
    "name": "Anemia Due To Malignancy",
    "primary_symptoms": ['flatulence', 'fatigue'],
    "secondary_symptoms": ['shortness_of_breath', 'difficulty_in_swallowing'],
    "rare_symptoms": [],
    "symptom_weights": {'shortness_of_breath': 0.67, 'difficulty_in_swallowing': 0.58, 'flatulence': 0.92, 'fatigue': 0.75}
}
disease_map["CSV_0042"] = {
    "name": "Anemia Of Chronic Disease",
    "primary_symptoms": ['dizziness', 'feeling_ill'],
    "secondary_symptoms": ['emotional_symptoms', 'weakness'],
    "rare_symptoms": [],
    "symptom_weights": {'dizziness': 0.93, 'emotional_symptoms': 0.62, 'feeling_ill': 0.95, 'weakness': 0.5}
}
disease_map["CSV_0043"] = {
    "name": "Angina",
    "primary_symptoms": [],
    "secondary_symptoms": ['shortness_of_breath', 'sharp_chest_pain', 'dizziness', 'chest_tightness', 'palpitations', 'irregular_heartbeat', 'hot_flashes', 'arm_pain', 'increased_heart_rate', 'lower_body_pain', 'sweating'],
    "rare_symptoms": [],
    "symptom_weights": {'shortness_of_breath': 0.49, 'sharp_chest_pain': 0.52, 'dizziness': 0.49, 'chest_tightness': 0.51, 'palpitations': 0.53, 'irregular_heartbeat': 0.51, 'hot_flashes': 0.68, 'arm_pain': 0.5, 'increased_heart_rate': 0.5, 'lower_body_pain': 0.51, 'sweating': 0.5}
}
disease_map["CSV_0044"] = {
    "name": "Ankylosing Spondylitis",
    "primary_symptoms": ['paresthesia'],
    "secondary_symptoms": ['leg_pain', 'hip_pain', 'back_pain', 'low_back_pain', 'knee_pain', 'elbow_pain', 'ache_all_over', 'lower_body_pain', 'stiffness_all_over'],
    "rare_symptoms": [],
    "symptom_weights": {'leg_pain': 0.47, 'hip_pain': 0.47, 'back_pain': 0.48, 'low_back_pain': 0.51, 'knee_pain': 0.5, 'elbow_pain': 0.52, 'paresthesia': 0.74, 'ache_all_over': 0.51, 'lower_body_pain': 0.49, 'stiffness_all_over': 0.5}
}
disease_map["CSV_0045"] = {
    "name": "Anxiety",
    "primary_symptoms": [],
    "secondary_symptoms": ['anxiety_and_nervousness', 'depression', 'shortness_of_breath', 'depressive_or_psychotic_symptoms', 'sharp_chest_pain', 'insomnia', 'abnormal_involuntary_movements', 'palpitations', 'irregular_heartbeat', 'headache', 'increased_heart_rate', 'fears_and_phobias'],
    "rare_symptoms": [],
    "symptom_weights": {'anxiety_and_nervousness': 0.49, 'depression': 0.51, 'shortness_of_breath': 0.51, 'depressive_or_psychotic_symptoms': 0.52, 'sharp_chest_pain': 0.53, 'insomnia': 0.52, 'abnormal_involuntary_movements': 0.51, 'palpitations': 0.5, 'irregular_heartbeat': 0.51, 'headache': 0.51, 'increased_heart_rate': 0.49, 'fears_and_phobias': 0.51}
}
disease_map["CSV_0046"] = {
    "name": "Aortic Valve Disease",
    "primary_symptoms": ['irregular_heartbeat'],
    "secondary_symptoms": ['shortness_of_breath', 'sharp_chest_pain', 'palpitations', 'groin_mass', 'fainting', 'peripheral_edema', 'difficulty_breathing', 'lymphedema'],
    "rare_symptoms": [],
    "symptom_weights": {'shortness_of_breath': 0.49, 'sharp_chest_pain': 0.68, 'palpitations': 0.53, 'irregular_heartbeat': 0.77, 'groin_mass': 0.45, 'fainting': 0.53, 'peripheral_edema': 0.49, 'difficulty_breathing': 0.54, 'lymphedema': 0.52}
}
disease_map["CSV_0047"] = {
    "name": "Aphakia",
    "primary_symptoms": ['diminished_vision', 'symptoms_of_eye', 'eye_burns_or_stings'],
    "secondary_symptoms": ['spots_or_clouds_in_vision'],
    "rare_symptoms": [],
    "symptom_weights": {'diminished_vision': 0.78, 'symptoms_of_eye': 1.0, 'spots_or_clouds_in_vision': 0.56, 'eye_burns_or_stings': 0.78}
}
disease_map["CSV_0048"] = {
    "name": "Aphthous Ulcer",
    "primary_symptoms": ['headache'],
    "secondary_symptoms": ['sore_throat', 'cough', 'toothache', 'mouth_ulcer', 'fever', 'tongue_lesions', 'mouth_pain'],
    "rare_symptoms": [],
    "symptom_weights": {'sore_throat': 0.54, 'cough': 0.67, 'headache': 0.86, 'toothache': 0.5, 'mouth_ulcer': 0.56, 'fever': 0.55, 'tongue_lesions': 0.53, 'mouth_pain': 0.57}
}
disease_map["CSV_0049"] = {
    "name": "Aplastic Anemia",
    "primary_symptoms": ['lack_of_growth'],
    "secondary_symptoms": ['nausea', 'weakness', 'slurring_words', 'fever', 'fatigue'],
    "rare_symptoms": [],
    "symptom_weights": {'lack_of_growth': 0.91, 'nausea': 0.51, 'weakness': 0.57, 'slurring_words': 0.59, 'fever': 0.43, 'fatigue': 0.5}
}
disease_map["CSV_0050"] = {
    "name": "Appendicitis",
    "primary_symptoms": [],
    "secondary_symptoms": ['sharp_abdominal_pain', 'vomiting', 'nausea', 'diarrhea', 'lower_abdominal_pain', 'burning_abdominal_pain', 'decreased_appetite', 'side_pain', 'fever', 'upper_abdominal_pain', 'stomach_bloating'],
    "rare_symptoms": [],
    "symptom_weights": {'sharp_abdominal_pain': 0.48, 'vomiting': 0.51, 'nausea': 0.51, 'diarrhea': 0.5, 'lower_abdominal_pain': 0.52, 'burning_abdominal_pain': 0.53, 'decreased_appetite': 0.66, 'side_pain': 0.51, 'fever': 0.5, 'upper_abdominal_pain': 0.5, 'stomach_bloating': 0.51}
}
disease_map["CSV_0051"] = {
    "name": "Arrhythmia",
    "primary_symptoms": ['shortness_of_breath', 'dizziness', 'fainting'],
    "secondary_symptoms": ['sharp_chest_pain', 'chest_tightness', 'palpitations', 'leg_cramps_or_spasms', 'fatigue'],
    "rare_symptoms": [],
    "symptom_weights": {'shortness_of_breath': 0.72, 'sharp_chest_pain': 0.56, 'dizziness': 0.78, 'chest_tightness': 0.54, 'palpitations': 0.6, 'fainting': 0.83, 'leg_cramps_or_spasms': 0.47, 'fatigue': 0.56}
}
disease_map["CSV_0052"] = {
    "name": "Arthritis Of The Hip",
    "primary_symptoms": [],
    "secondary_symptoms": ['leg_pain', 'hip_pain', 'back_pain', 'low_back_pain', 'pelvic_pain', 'knee_pain', 'problems_with_movement', 'ache_all_over', 'lower_body_pain', 'joint_pain', 'groin_pain', 'hip_stiffness_or_tightness'],
    "rare_symptoms": [],
    "symptom_weights": {'leg_pain': 0.49, 'hip_pain': 0.5, 'back_pain': 0.5, 'low_back_pain': 0.5, 'pelvic_pain': 0.53, 'knee_pain': 0.51, 'problems_with_movement': 0.5, 'ache_all_over': 0.51, 'lower_body_pain': 0.5, 'joint_pain': 0.49, 'groin_pain': 0.51, 'hip_stiffness_or_tightness': 0.51}
}
disease_map["CSV_0053"] = {
    "name": "Ascending Cholangitis",
    "primary_symptoms": ['shortness_of_breath', 'retention_of_urine', 'jaundice'],
    "secondary_symptoms": ['sharp_abdominal_pain', 'fever'],
    "rare_symptoms": [],
    "symptom_weights": {'shortness_of_breath': 0.89, 'retention_of_urine': 0.83, 'jaundice': 0.75, 'sharp_abdominal_pain': 0.6, 'fever': 0.53}
}
disease_map["CSV_0054"] = {
    "name": "Asperger Syndrome",
    "primary_symptoms": ['excessive_anger'],
    "secondary_symptoms": ['anxiety_and_nervousness', 'depression', 'depressive_or_psychotic_symptoms', 'lack_of_growth', 'fainting', 'hostile_behavior', 'antisocial_behavior'],
    "rare_symptoms": [],
    "symptom_weights": {'anxiety_and_nervousness': 0.51, 'depression': 0.52, 'depressive_or_psychotic_symptoms': 0.56, 'lack_of_growth': 0.67, 'fainting': 0.51, 'hostile_behavior': 0.67, 'excessive_anger': 0.75, 'antisocial_behavior': 0.54}
}
disease_map["CSV_0055"] = {
    "name": "Aspergillosis",
    "primary_symptoms": ['shortness_of_breath', 'knee_lump_or_mass'],
    "secondary_symptoms": [],
    "rare_symptoms": [],
    "symptom_weights": {'shortness_of_breath': 1.0, 'knee_lump_or_mass': 1.0}
}
disease_map["CSV_0056"] = {
    "name": "Astigmatism",
    "primary_symptoms": ['pain_in_eye'],
    "secondary_symptoms": ['eye_deviation', 'diminished_vision', 'double_vision', 'symptoms_of_eye', 'foreign_body_sensation_in_eye', 'spots_or_clouds_in_vision', 'lacrimation'],
    "rare_symptoms": [],
    "symptom_weights": {'eye_deviation': 0.67, 'diminished_vision': 0.52, 'double_vision': 0.66, 'symptoms_of_eye': 0.52, 'pain_in_eye': 0.78, 'foreign_body_sensation_in_eye': 0.5, 'spots_or_clouds_in_vision': 0.52, 'lacrimation': 0.51}
}
disease_map["CSV_0057"] = {
    "name": "Atelectasis",
    "primary_symptoms": ['dizziness', 'sore_throat', 'headache'],
    "secondary_symptoms": ['shortness_of_breath', 'sharp_chest_pain', 'cough'],
    "rare_symptoms": [],
    "symptom_weights": {'shortness_of_breath': 0.63, 'sharp_chest_pain': 0.6, 'dizziness': 0.83, 'sore_throat': 0.71, 'cough': 0.62, 'headache': 0.86}
}
disease_map["CSV_0058"] = {
    "name": "Athlete'S Foot",
    "primary_symptoms": [],
    "secondary_symptoms": ['skin_swelling', 'abnormal_appearing_skin', 'skin_lesion', 'foot_or_toe_pain', 'foot_or_toe_swelling', 'irregular_appearing_nails', 'skin_dryness,_peeling,_scaliness,_or_roughness', 'skin_rash'],
    "rare_symptoms": [],
    "symptom_weights": {'skin_swelling': 0.66, 'abnormal_appearing_skin': 0.68, 'skin_lesion': 0.7, 'foot_or_toe_pain': 0.51, 'foot_or_toe_swelling': 0.52, 'irregular_appearing_nails': 0.68, 'skin_dryness,_peeling,_scaliness,_or_roughness': 0.51, 'skin_rash': 0.48}
}
disease_map["CSV_0059"] = {
    "name": "Atonic Bladder",
    "primary_symptoms": ['retention_of_urine', 'suprapubic_pain', 'emotional_symptoms'],
    "secondary_symptoms": ['impotence', 'symptoms_of_bladder'],
    "rare_symptoms": [],
    "symptom_weights": {'retention_of_urine': 0.77, 'suprapubic_pain': 0.9, 'emotional_symptoms': 0.8, 'impotence': 0.63, 'symptoms_of_bladder': 0.54}
}
disease_map["CSV_0060"] = {
    "name": "Atrial Fibrillation",
    "primary_symptoms": [],
    "secondary_symptoms": ['shortness_of_breath', 'sharp_chest_pain', 'dizziness', 'palpitations', 'irregular_heartbeat', 'decreased_heart_rate', 'increased_heart_rate', 'fatigue'],
    "rare_symptoms": [],
    "symptom_weights": {'shortness_of_breath': 0.59, 'sharp_chest_pain': 0.54, 'dizziness': 0.62, 'palpitations': 0.65, 'irregular_heartbeat': 0.49, 'decreased_heart_rate': 0.53, 'increased_heart_rate': 0.6, 'fatigue': 0.53}
}
disease_map["CSV_0061"] = {
    "name": "Atrial Flutter",
    "primary_symptoms": ['sharp_chest_pain'],
    "secondary_symptoms": ['shortness_of_breath', 'chest_tightness', 'palpitations', 'irregular_heartbeat', 'frequent_urination', 'swollen_lymph_nodes', 'increased_heart_rate'],
    "rare_symptoms": [],
    "symptom_weights": {'shortness_of_breath': 0.53, 'sharp_chest_pain': 0.84, 'chest_tightness': 0.5, 'palpitations': 0.56, 'irregular_heartbeat': 0.6, 'frequent_urination': 0.55, 'swollen_lymph_nodes': 0.69, 'increased_heart_rate': 0.57}
}
disease_map["CSV_0062"] = {
    "name": "Atrophic Skin Condition",
    "primary_symptoms": ['acne_or_pimples'],
    "secondary_symptoms": ['skin_swelling', 'lip_swelling', 'abnormal_appearing_skin', 'skin_lesion', 'skin_growth', 'skin_moles', 'skin_irritation', 'wrinkles_on_skin'],
    "rare_symptoms": [],
    "symptom_weights": {'skin_swelling': 0.49, 'lip_swelling': 0.67, 'abnormal_appearing_skin': 0.53, 'skin_lesion': 0.54, 'acne_or_pimples': 0.77, 'skin_growth': 0.54, 'skin_moles': 0.52, 'skin_irritation': 0.54, 'wrinkles_on_skin': 0.47}
}
disease_map["CSV_0063"] = {
    "name": "Atrophic Vaginitis",
    "primary_symptoms": ['vaginal_itching', 'blood_in_urine'],
    "secondary_symptoms": ['suprapubic_pain', 'painful_urination', 'involuntary_urination', 'pain_during_intercourse', 'frequent_urination', 'vaginal_discharge'],
    "rare_symptoms": [],
    "symptom_weights": {'suprapubic_pain': 0.68, 'vaginal_itching': 0.72, 'painful_urination': 0.53, 'involuntary_urination': 0.51, 'pain_during_intercourse': 0.54, 'frequent_urination': 0.52, 'vaginal_discharge': 0.49, 'blood_in_urine': 0.78}
}
disease_map["CSV_0064"] = {
    "name": "Atrophy Of The Corpus Cavernosum",
    "primary_symptoms": ['frequent_urination', 'impotence', 'bumps_on_penis'],
    "secondary_symptoms": ['abnormal_appearing_skin', 'skin_growth'],
    "rare_symptoms": [],
    "symptom_weights": {'frequent_urination': 0.94, 'abnormal_appearing_skin': 0.6, 'skin_growth': 0.57, 'impotence': 0.77, 'bumps_on_penis': 0.83}
}
disease_map["CSV_0065"] = {
    "name": "Attention Deficit Hyperactivity Disorder (Adhd)",
    "primary_symptoms": [],
    "secondary_symptoms": ['anxiety_and_nervousness', 'depression', 'depressive_or_psychotic_symptoms', 'lack_of_growth', 'hostile_behavior', 'drug_abuse', 'restlessness', 'temper_problems', 'antisocial_behavior'],
    "rare_symptoms": [],
    "symptom_weights": {'anxiety_and_nervousness': 0.49, 'depression': 0.52, 'depressive_or_psychotic_symptoms': 0.49, 'lack_of_growth': 0.66, 'hostile_behavior': 0.69, 'drug_abuse': 0.64, 'restlessness': 0.49, 'temper_problems': 0.52, 'antisocial_behavior': 0.52}
}
disease_map["CSV_0066"] = {
    "name": "Autism",
    "primary_symptoms": ['long_menstrual_periods'],
    "secondary_symptoms": ['depressive_or_psychotic_symptoms', 'difficulty_speaking', 'lack_of_growth', 'hostile_behavior', 'seizures', 'constipation', 'temper_problems', 'antisocial_behavior'],
    "rare_symptoms": [],
    "symptom_weights": {'depressive_or_psychotic_symptoms': 0.5, 'difficulty_speaking': 0.66, 'lack_of_growth': 0.5, 'hostile_behavior': 0.51, 'seizures': 0.5, 'constipation': 0.49, 'temper_problems': 0.49, 'long_menstrual_periods': 0.72, 'antisocial_behavior': 0.51}
}
disease_map["CSV_0067"] = {
    "name": "Autonomic Nervous System Disorder",
    "primary_symptoms": ['dizziness', 'headache'],
    "secondary_symptoms": ['difficulty_in_swallowing', 'leg_pain', 'decreased_appetite'],
    "rare_symptoms": [],
    "symptom_weights": {'dizziness': 0.83, 'difficulty_in_swallowing': 0.61, 'leg_pain': 0.56, 'headache': 0.88, 'decreased_appetite': 0.65}
}
disease_map["CSV_0068"] = {
    "name": "Avascular Necrosis",
    "primary_symptoms": ['drug_abuse', 'shoulder_pain'],
    "secondary_symptoms": ['hip_pain', 'knee_pain'],
    "rare_symptoms": [],
    "symptom_weights": {'hip_pain': 0.4, 'drug_abuse': 1.0, 'knee_pain': 0.6, 'shoulder_pain': 0.7}
}
disease_map["CSV_0069"] = {
    "name": "Balanitis",
    "primary_symptoms": ['suprapubic_pain'],
    "secondary_symptoms": ['cough', 'painful_urination', 'abnormal_appearing_skin', 'itching_of_skin', 'skin_rash', 'penis_pain', 'penis_redness', 'diaper_rash'],
    "rare_symptoms": [],
    "symptom_weights": {'cough': 0.5, 'suprapubic_pain': 0.76, 'painful_urination': 0.66, 'abnormal_appearing_skin': 0.49, 'itching_of_skin': 0.48, 'skin_rash': 0.5, 'penis_pain': 0.45, 'penis_redness': 0.49, 'diaper_rash': 0.5}
}
disease_map["CSV_0070"] = {
    "name": "Bell Palsy",
    "primary_symptoms": [],
    "secondary_symptoms": ['abnormal_involuntary_movements', 'headache', 'facial_pain', 'diminished_vision', 'symptoms_of_eye', 'peripheral_edema', 'weakness', 'loss_of_sensation', 'focal_weakness', 'symptoms_of_the_face'],
    "rare_symptoms": [],
    "symptom_weights": {'abnormal_involuntary_movements': 0.64, 'headache': 0.49, 'facial_pain': 0.5, 'diminished_vision': 0.66, 'symptoms_of_eye': 0.52, 'peripheral_edema': 0.52, 'weakness': 0.49, 'loss_of_sensation': 0.48, 'focal_weakness': 0.52, 'symptoms_of_the_face': 0.51}
}
disease_map["CSV_0071"] = {
    "name": "Benign Kidney Cyst",
    "primary_symptoms": ['impotence'],
    "secondary_symptoms": ['sharp_abdominal_pain', 'vomiting', 'involuntary_urination', 'blood_in_urine', 'low_back_pain', 'side_pain'],
    "rare_symptoms": [],
    "symptom_weights": {'sharp_abdominal_pain': 0.53, 'vomiting': 0.68, 'involuntary_urination': 0.67, 'blood_in_urine': 0.57, 'low_back_pain': 0.47, 'impotence': 0.74, 'side_pain': 0.49}
}
disease_map["CSV_0072"] = {
    "name": "Benign Paroxysmal Positional Vertical (Bppv)",
    "primary_symptoms": ['irregular_heartbeat'],
    "secondary_symptoms": ['dizziness', 'fainting', 'vomiting', 'headache', 'nausea', 'problems_with_movement', 'weakness', 'frontal_headache'],
    "rare_symptoms": [],
    "symptom_weights": {'dizziness': 0.52, 'irregular_heartbeat': 0.77, 'fainting': 0.68, 'vomiting': 0.52, 'headache': 0.54, 'nausea': 0.52, 'problems_with_movement': 0.51, 'weakness': 0.5, 'frontal_headache': 0.5}
}
disease_map["CSV_0073"] = {
    "name": "Benign Prostatic Hyperplasia (Bph)",
    "primary_symptoms": [],
    "secondary_symptoms": ['retention_of_urine', 'swelling_of_scrotum', 'pain_in_testicles', 'involuntary_urination', 'frequent_urination', 'blood_in_urine', 'impotence', 'symptoms_of_prostate', 'excessive_urination_at_night', 'symptoms_of_bladder', 'hesitancy', 'low_urine_output'],
    "rare_symptoms": [],
    "symptom_weights": {'retention_of_urine': 0.5, 'swelling_of_scrotum': 0.5, 'pain_in_testicles': 0.5, 'involuntary_urination': 0.5, 'frequent_urination': 0.52, 'blood_in_urine': 0.51, 'impotence': 0.5, 'symptoms_of_prostate': 0.52, 'excessive_urination_at_night': 0.49, 'symptoms_of_bladder': 0.5, 'hesitancy': 0.5, 'low_urine_output': 0.5}
}
disease_map["CSV_0074"] = {
    "name": "Benign Vaginal Discharge (Leukorrhea)",
    "primary_symptoms": [],
    "secondary_symptoms": ['suprapubic_pain', 'sharp_abdominal_pain', 'vaginal_itching', 'painful_urination', 'frequent_urination', 'vaginal_discharge', 'pain_during_pregnancy', 'burning_abdominal_pain', 'vaginal_redness', 'problems_during_pregnancy'],
    "rare_symptoms": [],
    "symptom_weights": {'suprapubic_pain': 0.66, 'sharp_abdominal_pain': 0.48, 'vaginal_itching': 0.51, 'painful_urination': 0.68, 'frequent_urination': 0.51, 'vaginal_discharge': 0.53, 'pain_during_pregnancy': 0.52, 'burning_abdominal_pain': 0.49, 'vaginal_redness': 0.52, 'problems_during_pregnancy': 0.5}
}
disease_map["CSV_0075"] = {
    "name": "Bipolar Disorder",
    "primary_symptoms": [],
    "secondary_symptoms": ['anxiety_and_nervousness', 'depression', 'depressive_or_psychotic_symptoms', 'insomnia', 'abusing_alcohol', 'excessive_anger', 'delusions_or_hallucinations', 'temper_problems', 'fears_and_phobias', 'obsessions_and_compulsions'],
    "rare_symptoms": [],
    "symptom_weights": {'anxiety_and_nervousness': 0.49, 'depression': 0.52, 'depressive_or_psychotic_symptoms': 0.51, 'insomnia': 0.67, 'abusing_alcohol': 0.65, 'excessive_anger': 0.51, 'delusions_or_hallucinations': 0.52, 'temper_problems': 0.48, 'fears_and_phobias': 0.51, 'obsessions_and_compulsions': 0.51}
}
disease_map["CSV_0076"] = {
    "name": "Birth Trauma",
    "primary_symptoms": ['depressive_or_psychotic_symptoms', 'emotional_symptoms', 'arm_stiffness_or_tightness'],
    "secondary_symptoms": [],
    "rare_symptoms": [],
    "symptom_weights": {'depressive_or_psychotic_symptoms': 1.0, 'emotional_symptoms': 0.91, 'arm_stiffness_or_tightness': 0.91}
}
disease_map["CSV_0077"] = {
    "name": "Bladder Cancer",
    "primary_symptoms": ['mass_in_scrotum'],
    "secondary_symptoms": ['retention_of_urine', 'groin_mass', 'blood_in_urine', 'excessive_urination_at_night', 'symptoms_of_bladder', 'bladder_mass'],
    "rare_symptoms": [],
    "symptom_weights": {'retention_of_urine': 0.6, 'groin_mass': 0.55, 'mass_in_scrotum': 0.91, 'blood_in_urine': 0.54, 'excessive_urination_at_night': 0.53, 'symptoms_of_bladder': 0.5, 'bladder_mass': 0.54}
}
disease_map["CSV_0078"] = {
    "name": "Bladder Disorder",
    "primary_symptoms": ['painful_urination'],
    "secondary_symptoms": ['retention_of_urine', 'suprapubic_pain', 'sharp_abdominal_pain', 'involuntary_urination', 'frequent_urination', 'lower_abdominal_pain', 'blood_in_urine', 'symptoms_of_bladder'],
    "rare_symptoms": [],
    "symptom_weights": {'retention_of_urine': 0.49, 'suprapubic_pain': 0.51, 'sharp_abdominal_pain': 0.51, 'painful_urination': 0.73, 'involuntary_urination': 0.49, 'frequent_urination': 0.53, 'lower_abdominal_pain': 0.66, 'blood_in_urine': 0.49, 'symptoms_of_bladder': 0.5}
}
disease_map["CSV_0079"] = {
    "name": "Bladder Obstruction",
    "primary_symptoms": ['involuntary_urination'],
    "secondary_symptoms": ['retention_of_urine', 'suprapubic_pain', 'frequent_urination', 'impotence', 'symptoms_of_bladder', 'bedwetting', 'hesitancy'],
    "rare_symptoms": [],
    "symptom_weights": {'retention_of_urine': 0.51, 'suprapubic_pain': 0.68, 'involuntary_urination': 0.78, 'frequent_urination': 0.69, 'impotence': 0.53, 'symptoms_of_bladder': 0.51, 'bedwetting': 0.5, 'hesitancy': 0.53}
}
disease_map["CSV_0080"] = {
    "name": "Blepharitis",
    "primary_symptoms": [],
    "secondary_symptoms": ['white_discharge_from_eye', 'diminished_vision', 'symptoms_of_eye', 'pain_in_eye', 'spots_or_clouds_in_vision', 'eye_redness', 'lacrimation', 'itchiness_of_eye', 'eye_burns_or_stings', 'swollen_eye', 'eyelid_swelling'],
    "rare_symptoms": [],
    "symptom_weights": {'white_discharge_from_eye': 0.48, 'diminished_vision': 0.51, 'symptoms_of_eye': 0.48, 'pain_in_eye': 0.51, 'spots_or_clouds_in_vision': 0.52, 'eye_redness': 0.51, 'lacrimation': 0.52, 'itchiness_of_eye': 0.5, 'eye_burns_or_stings': 0.67, 'swollen_eye': 0.5, 'eyelid_swelling': 0.53}
}
disease_map["CSV_0081"] = {
    "name": "Blepharospasm",
    "primary_symptoms": ['headache', 'abnormal_movement_of_eyelid', 'low_back_weakness'],
    "secondary_symptoms": ['diminished_vision'],
    "rare_symptoms": [],
    "symptom_weights": {'headache': 1.0, 'diminished_vision': 0.5, 'abnormal_movement_of_eyelid': 0.83, 'low_back_weakness': 0.83}
}
disease_map["CSV_0082"] = {
    "name": "Bone Cancer",
    "primary_symptoms": ['leg_pain', 'problems_with_movement'],
    "secondary_symptoms": ['low_back_pain', 'peripheral_edema', 'fatigue'],
    "rare_symptoms": [],
    "symptom_weights": {'leg_pain': 0.72, 'low_back_pain': 0.52, 'peripheral_edema': 0.64, 'problems_with_movement': 0.87, 'fatigue': 0.43}
}
disease_map["CSV_0083"] = {
    "name": "Bone Disorder",
    "primary_symptoms": ['difficulty_speaking', 'leg_cramps_or_spasms'],
    "secondary_symptoms": ['leg_pain', 'back_pain', 'knee_pain', 'bones_are_painful', 'muscle_stiffness_or_tightness'],
    "rare_symptoms": [],
    "symptom_weights": {'difficulty_speaking': 0.76, 'leg_pain': 0.69, 'back_pain': 0.5, 'knee_pain': 0.54, 'bones_are_painful': 0.52, 'leg_cramps_or_spasms': 0.72, 'muscle_stiffness_or_tightness': 0.69}
}
disease_map["CSV_0084"] = {
    "name": "Bone Spur Of The Calcaneous",
    "primary_symptoms": ['foot_or_toe_pain', 'elbow_pain'],
    "secondary_symptoms": ['leg_pain', 'ankle_pain', 'foot_or_toe_swelling'],
    "rare_symptoms": [],
    "symptom_weights": {'leg_pain': 0.48, 'foot_or_toe_pain': 0.81, 'ankle_pain': 0.61, 'elbow_pain': 0.97, 'foot_or_toe_swelling': 0.52}
}
disease_map["CSV_0085"] = {
    "name": "Brachial Neuritis",
    "primary_symptoms": [],
    "secondary_symptoms": ['headache', 'hand_or_finger_pain', 'arm_pain', 'back_pain', 'neck_pain', 'low_back_pain', 'elbow_pain', 'loss_of_sensation', 'paresthesia', 'shoulder_pain', 'hand_or_finger_weakness'],
    "rare_symptoms": [],
    "symptom_weights": {'headache': 0.49, 'hand_or_finger_pain': 0.5, 'arm_pain': 0.49, 'back_pain': 0.52, 'neck_pain': 0.53, 'low_back_pain': 0.52, 'elbow_pain': 0.68, 'loss_of_sensation': 0.49, 'paresthesia': 0.52, 'shoulder_pain': 0.51, 'hand_or_finger_weakness': 0.5}
}
disease_map["CSV_0086"] = {
    "name": "Brain Cancer",
    "primary_symptoms": ['difficulty_speaking'],
    "secondary_symptoms": ['headache', 'weakness', 'decreased_appetite', 'focal_weakness', 'slurring_words', 'disturbance_of_memory', 'seizures'],
    "rare_symptoms": [],
    "symptom_weights": {'difficulty_speaking': 0.86, 'headache': 0.48, 'weakness': 0.48, 'decreased_appetite': 0.55, 'focal_weakness': 0.57, 'slurring_words': 0.55, 'disturbance_of_memory': 0.48, 'seizures': 0.51}
}
disease_map["CSV_0087"] = {
    "name": "Breast Cancer",
    "primary_symptoms": ['lump_or_mass_of_breast'],
    "secondary_symptoms": ['hot_flashes', 'bleeding_or_discharge_from_nipple', 'pain_or_soreness_of_breast'],
    "rare_symptoms": [],
    "symptom_weights": {'hot_flashes': 0.5, 'bleeding_or_discharge_from_nipple': 0.67, 'pain_or_soreness_of_breast': 0.67, 'lump_or_mass_of_breast': 0.83}
}
disease_map["CSV_0088"] = {
    "name": "Breast Cyst",
    "primary_symptoms": ['vaginal_dryness'],
    "secondary_symptoms": ['skin_growth', 'pain_or_soreness_of_breast', 'lump_or_mass_of_breast'],
    "rare_symptoms": [],
    "symptom_weights": {'vaginal_dryness': 0.91, 'skin_growth': 0.64, 'pain_or_soreness_of_breast': 0.55, 'lump_or_mass_of_breast': 0.5}
}
disease_map["CSV_0089"] = {
    "name": "Breast Infection (Mastitis)",
    "primary_symptoms": [],
    "secondary_symptoms": ['abnormal_appearing_skin', 'skin_growth', 'mouth_dryness', 'bleeding_or_discharge_from_nipple', 'fever', 'chills', 'pain_or_soreness_of_breast', 'lump_or_mass_of_breast', 'postpartum_problems_of_the_breast'],
    "rare_symptoms": [],
    "symptom_weights": {'abnormal_appearing_skin': 0.5, 'skin_growth': 0.67, 'mouth_dryness': 0.66, 'bleeding_or_discharge_from_nipple': 0.5, 'fever': 0.5, 'chills': 0.67, 'pain_or_soreness_of_breast': 0.52, 'lump_or_mass_of_breast': 0.51, 'postpartum_problems_of_the_breast': 0.5}
}
disease_map["CSV_0090"] = {
    "name": "Broken Tooth",
    "primary_symptoms": ['lip_swelling', 'dry_lips'],
    "secondary_symptoms": ['toothache', 'facial_pain', 'difficulty_eating', 'gum_pain', 'bleeding_gums'],
    "rare_symptoms": [],
    "symptom_weights": {'lip_swelling': 0.82, 'toothache': 0.6, 'dry_lips': 0.75, 'facial_pain': 0.52, 'difficulty_eating': 0.5, 'gum_pain': 0.5, 'bleeding_gums': 0.52}
}
disease_map["CSV_0091"] = {
    "name": "Bunion",
    "primary_symptoms": ['skin_growth', 'foot_or_toe_pain', 'skin_moles'],
    "secondary_symptoms": ['knee_pain', 'foot_or_toe_lump_or_mass'],
    "rare_symptoms": [],
    "symptom_weights": {'skin_growth': 0.95, 'knee_pain': 0.53, 'foot_or_toe_pain': 0.84, 'skin_moles': 0.87, 'foot_or_toe_lump_or_mass': 0.53}
}
disease_map["CSV_0092"] = {
    "name": "Burn",
    "primary_symptoms": ['wrist_pain', 'wrist_swelling', 'skin_irritation'],
    "secondary_symptoms": ['headache', 'hand_or_finger_pain', 'knee_pain'],
    "rare_symptoms": [],
    "symptom_weights": {'headache': 0.54, 'hand_or_finger_pain': 0.56, 'wrist_pain': 0.72, 'wrist_swelling': 0.74, 'knee_pain': 0.54, 'skin_irritation': 0.77}
}
disease_map["CSV_0093"] = {
    "name": "Bursitis",
    "primary_symptoms": [],
    "secondary_symptoms": ['leg_pain', 'hip_pain', 'arm_pain', 'arm_stiffness_or_tightness', 'arm_swelling', 'knee_pain', 'elbow_pain', 'knee_swelling', 'leg_swelling', 'shoulder_pain', 'shoulder_stiffness_or_tightness', 'elbow_swelling'],
    "rare_symptoms": [],
    "symptom_weights": {'leg_pain': 0.49, 'hip_pain': 0.51, 'arm_pain': 0.51, 'arm_stiffness_or_tightness': 0.51, 'arm_swelling': 0.51, 'knee_pain': 0.52, 'elbow_pain': 0.51, 'knee_swelling': 0.5, 'leg_swelling': 0.49, 'shoulder_pain': 0.49, 'shoulder_stiffness_or_tightness': 0.49, 'elbow_swelling': 0.53}
}
disease_map["CSV_0094"] = {
    "name": "Callus",
    "primary_symptoms": [],
    "secondary_symptoms": ['skin_swelling', 'abnormal_appearing_skin', 'skin_lesion', 'acne_or_pimples', 'skin_growth', 'foot_or_toe_pain', 'foot_or_toe_swelling', 'irregular_appearing_nails', 'skin_rash'],
    "rare_symptoms": [],
    "symptom_weights": {'skin_swelling': 0.65, 'abnormal_appearing_skin': 0.49, 'skin_lesion': 0.5, 'acne_or_pimples': 0.68, 'skin_growth': 0.55, 'foot_or_toe_pain': 0.51, 'foot_or_toe_swelling': 0.65, 'irregular_appearing_nails': 0.5, 'skin_rash': 0.49}
}
disease_map["CSV_0095"] = {
    "name": "Carbon Monoxide Poisoning",
    "primary_symptoms": ['depressive_or_psychotic_symptoms', 'emotional_symptoms'],
    "secondary_symptoms": ['dizziness', 'vomiting', 'headache', 'nausea'],
    "rare_symptoms": [],
    "symptom_weights": {'depressive_or_psychotic_symptoms': 0.86, 'dizziness': 0.52, 'emotional_symptoms': 0.72, 'vomiting': 0.52, 'headache': 0.58, 'nausea': 0.58}
}
disease_map["CSV_0096"] = {
    "name": "Carcinoid Syndrome",
    "primary_symptoms": ['involuntary_urination', 'knee_lump_or_mass'],
    "secondary_symptoms": [],
    "rare_symptoms": [],
    "symptom_weights": {'involuntary_urination': 1.0, 'knee_lump_or_mass': 1.0}
}
disease_map["CSV_0097"] = {
    "name": "Cardiac Arrest",
    "primary_symptoms": ['palpitations', 'irregular_heartbeat', 'arm_swelling'],
    "secondary_symptoms": ['shortness_of_breath', 'sharp_chest_pain', 'weakness', 'decreased_heart_rate', 'difficulty_breathing'],
    "rare_symptoms": [],
    "symptom_weights": {'shortness_of_breath': 0.56, 'sharp_chest_pain': 0.54, 'palpitations': 0.72, 'irregular_heartbeat': 0.71, 'arm_swelling': 0.71, 'weakness': 0.56, 'decreased_heart_rate': 0.67, 'difficulty_breathing': 0.51}
}
disease_map["CSV_0098"] = {
    "name": "Cardiomyopathy",
    "primary_symptoms": ['decreased_heart_rate'],
    "secondary_symptoms": ['shortness_of_breath', 'sharp_chest_pain', 'chest_tightness', 'irregular_heartbeat', 'peripheral_edema', 'heartburn', 'fatigue'],
    "rare_symptoms": [],
    "symptom_weights": {'shortness_of_breath': 0.53, 'sharp_chest_pain': 0.56, 'chest_tightness': 0.69, 'irregular_heartbeat': 0.68, 'peripheral_edema': 0.46, 'heartburn': 0.5, 'decreased_heart_rate': 0.74, 'fatigue': 0.59}
}
disease_map["CSV_0099"] = {
    "name": "Carpal Tunnel Syndrome",
    "primary_symptoms": [],
    "secondary_symptoms": ['hand_or_finger_pain', 'wrist_pain', 'hand_or_finger_swelling', 'arm_pain', 'wrist_swelling', 'hand_or_finger_stiffness_or_tightness', 'neck_pain', 'elbow_pain', 'loss_of_sensation', 'paresthesia', 'arm_weakness'],
    "rare_symptoms": [],
    "symptom_weights": {'hand_or_finger_pain': 0.5, 'wrist_pain': 0.52, 'hand_or_finger_swelling': 0.49, 'arm_pain': 0.5, 'wrist_swelling': 0.53, 'hand_or_finger_stiffness_or_tightness': 0.51, 'neck_pain': 0.52, 'elbow_pain': 0.68, 'loss_of_sensation': 0.52, 'paresthesia': 0.52, 'arm_weakness': 0.5}
}
disease_map["CSV_0100"] = {
    "name": "Cat Scratch Disease",
    "primary_symptoms": ['skin_swelling', 'groin_mass'],
    "secondary_symptoms": ['itchy_eyelid'],
    "rare_symptoms": [],
    "symptom_weights": {'skin_swelling': 1.0, 'groin_mass': 1.0, 'itchy_eyelid': 0.67}
}
disease_map["CSV_0101"] = {
    "name": "Cataract",
    "primary_symptoms": ['double_vision'],
    "secondary_symptoms": ['diminished_vision', 'symptoms_of_eye', 'pain_in_eye', 'abnormal_movement_of_eyelid', 'spots_or_clouds_in_vision', 'lacrimation', 'itchiness_of_eye', 'blindness', 'cloudy_eye'],
    "rare_symptoms": [],
    "symptom_weights": {'diminished_vision': 0.46, 'double_vision': 0.72, 'symptoms_of_eye': 0.52, 'pain_in_eye': 0.5, 'abnormal_movement_of_eyelid': 0.49, 'spots_or_clouds_in_vision': 0.49, 'lacrimation': 0.51, 'itchiness_of_eye': 0.47, 'blindness': 0.52, 'cloudy_eye': 0.51}
}
disease_map["CSV_0102"] = {
    "name": "Celiac Disease",
    "primary_symptoms": ['sharp_chest_pain', 'sharp_abdominal_pain', 'peripheral_edema'],
    "secondary_symptoms": ['vomiting', 'nausea', 'regurgitation.1'],
    "rare_symptoms": [],
    "symptom_weights": {'sharp_chest_pain': 0.75, 'sharp_abdominal_pain': 0.72, 'vomiting': 0.7, 'nausea': 0.5, 'peripheral_edema': 0.81, 'regurgitation.1': 0.52}
}
disease_map["CSV_0103"] = {
    "name": "Cellulitis Or Abscess Of Mouth",
    "primary_symptoms": ['throat_swelling', 'abnormal_appearing_skin'],
    "secondary_symptoms": ['sore_throat', 'difficulty_in_swallowing', 'lip_swelling', 'toothache', 'skin_growth'],
    "rare_symptoms": [],
    "symptom_weights": {'sore_throat': 0.64, 'throat_swelling': 0.9, 'difficulty_in_swallowing': 0.47, 'lip_swelling': 0.62, 'toothache': 0.52, 'abnormal_appearing_skin': 0.78, 'skin_growth': 0.57}
}
disease_map["CSV_0104"] = {
    "name": "Central Atherosclerosis",
    "primary_symptoms": ['shortness_of_breath', 'irregular_heartbeat', 'blood_in_urine'],
    "secondary_symptoms": ['fatigue'],
    "rare_symptoms": [],
    "symptom_weights": {'shortness_of_breath': 0.72, 'irregular_heartbeat': 0.94, 'blood_in_urine': 0.72, 'fatigue': 0.67}
}
disease_map["CSV_0105"] = {
    "name": "Central Retinal Artery Or Vein Occlusion",
    "primary_symptoms": ['irregular_heartbeat', 'symptoms_of_eye'],
    "secondary_symptoms": ['diminished_vision', 'pain_in_eye', 'foreign_body_sensation_in_eye', 'blindness'],
    "rare_symptoms": [],
    "symptom_weights": {'irregular_heartbeat': 0.8, 'diminished_vision': 0.51, 'symptoms_of_eye': 0.71, 'pain_in_eye': 0.58, 'foreign_body_sensation_in_eye': 0.48, 'blindness': 0.51}
}
disease_map["CSV_0106"] = {
    "name": "Cerebral Edema",
    "primary_symptoms": ['dizziness', 'vomiting'],
    "secondary_symptoms": ['headache', 'arm_pain', 'neck_pain', 'focal_weakness'],
    "rare_symptoms": [],
    "symptom_weights": {'dizziness': 0.9, 'vomiting': 0.74, 'headache': 0.57, 'arm_pain': 0.68, 'neck_pain': 0.57, 'focal_weakness': 0.52}
}
disease_map["CSV_0107"] = {
    "name": "Cerebral Palsy",
    "primary_symptoms": ['lack_of_growth', 'infant_feeding_problem', 'blindness'],
    "secondary_symptoms": ['problems_with_movement', 'cramps_and_spasms', 'seizures'],
    "rare_symptoms": [],
    "symptom_weights": {'lack_of_growth': 0.73, 'problems_with_movement': 0.51, 'infant_feeding_problem': 0.81, 'blindness': 0.75, 'cramps_and_spasms': 0.53, 'seizures': 0.51}
}
disease_map["CSV_0108"] = {
    "name": "Cervical Cancer",
    "primary_symptoms": ['jaundice', 'vaginal_itching'],
    "secondary_symptoms": ['vaginal_discharge', 'pelvic_pain', 'vulvar_irritation', 'heavy_menstrual_flow'],
    "rare_symptoms": [],
    "symptom_weights": {'jaundice': 0.87, 'vaginal_itching': 0.91, 'vaginal_discharge': 0.54, 'pelvic_pain': 0.63, 'vulvar_irritation': 0.53, 'heavy_menstrual_flow': 0.59}
}
disease_map["CSV_0109"] = {
    "name": "Cervical Disorder",
    "primary_symptoms": ['sharp_abdominal_pain', 'vaginal_itching', 'pain_during_intercourse'],
    "secondary_symptoms": [],
    "rare_symptoms": ['pelvic_pain'],
    "symptom_weights": {'sharp_abdominal_pain': 0.72, 'vaginal_itching': 0.88, 'pain_during_intercourse': 0.79, 'pelvic_pain': 0.4}
}
disease_map["CSV_0110"] = {
    "name": "Cervicitis",
    "primary_symptoms": ['painful_urination'],
    "secondary_symptoms": ['suprapubic_pain', 'sharp_abdominal_pain', 'nausea', 'vaginal_itching', 'vaginal_discharge', 'pain_during_pregnancy', 'pelvic_pain'],
    "rare_symptoms": [],
    "symptom_weights": {'suprapubic_pain': 0.48, 'sharp_abdominal_pain': 0.53, 'nausea': 0.67, 'vaginal_itching': 0.66, 'painful_urination': 0.71, 'vaginal_discharge': 0.5, 'pain_during_pregnancy': 0.66, 'pelvic_pain': 0.53}
}
disease_map["CSV_0111"] = {
    "name": "Chalazion",
    "primary_symptoms": [],
    "secondary_symptoms": ['skin_growth', 'diminished_vision', 'symptoms_of_eye', 'pain_in_eye', 'foreign_body_sensation_in_eye', 'eye_redness', 'lacrimation', 'mass_on_eyelid', 'swollen_eye', 'eyelid_swelling'],
    "rare_symptoms": [],
    "symptom_weights": {'skin_growth': 0.48, 'diminished_vision': 0.68, 'symptoms_of_eye': 0.5, 'pain_in_eye': 0.5, 'foreign_body_sensation_in_eye': 0.51, 'eye_redness': 0.51, 'lacrimation': 0.52, 'mass_on_eyelid': 0.52, 'swollen_eye': 0.51, 'eyelid_swelling': 0.68}
}
disease_map["CSV_0112"] = {
    "name": "Chickenpox",
    "primary_symptoms": ['cough', 'pain_in_testicles'],
    "secondary_symptoms": ['abnormal_appearing_skin', 'fever', 'itching_of_skin', 'skin_rash'],
    "rare_symptoms": [],
    "symptom_weights": {'cough': 0.84, 'pain_in_testicles': 0.86, 'abnormal_appearing_skin': 0.5, 'fever': 0.58, 'itching_of_skin': 0.59, 'skin_rash': 0.56}
}
disease_map["CSV_0113"] = {
    "name": "Chlamydia",
    "primary_symptoms": ['vaginal_itching', 'pelvic_pain'],
    "secondary_symptoms": ['sharp_abdominal_pain', 'lower_abdominal_pain', 'vaginal_discharge', 'vaginal_pain'],
    "rare_symptoms": [],
    "symptom_weights": {'sharp_abdominal_pain': 0.68, 'vaginal_itching': 0.78, 'lower_abdominal_pain': 0.56, 'vaginal_discharge': 0.65, 'pelvic_pain': 0.81, 'vaginal_pain': 0.53}
}
disease_map["CSV_0114"] = {
    "name": "Cholecystitis",
    "primary_symptoms": [],
    "secondary_symptoms": ['sharp_chest_pain', 'sharp_abdominal_pain', 'vomiting', 'nausea', 'back_pain', 'burning_abdominal_pain', 'side_pain', 'lower_body_pain', 'upper_abdominal_pain', 'stomach_bloating', 'regurgitation.1', 'symptoms_of_the_kidneys'],
    "rare_symptoms": [],
    "symptom_weights": {'sharp_chest_pain': 0.48, 'sharp_abdominal_pain': 0.51, 'vomiting': 0.52, 'nausea': 0.5, 'back_pain': 0.52, 'burning_abdominal_pain': 0.51, 'side_pain': 0.52, 'lower_body_pain': 0.5, 'upper_abdominal_pain': 0.49, 'stomach_bloating': 0.48, 'regurgitation.1': 0.51, 'symptoms_of_the_kidneys': 0.51}
}
disease_map["CSV_0115"] = {
    "name": "Choledocholithiasis",
    "primary_symptoms": ['jaundice'],
    "secondary_symptoms": ['sharp_chest_pain', 'sharp_abdominal_pain', 'vomiting', 'nausea', 'decreased_appetite', 'side_pain', 'upper_abdominal_pain', 'chills'],
    "rare_symptoms": [],
    "symptom_weights": {'sharp_chest_pain': 0.5, 'jaundice': 0.78, 'sharp_abdominal_pain': 0.54, 'vomiting': 0.52, 'nausea': 0.5, 'decreased_appetite': 0.68, 'side_pain': 0.53, 'upper_abdominal_pain': 0.47, 'chills': 0.52}
}
disease_map["CSV_0116"] = {
    "name": "Cholesteatoma",
    "primary_symptoms": ['nasal_congestion', 'diminished_hearing', 'pus_draining_from_ear'],
    "secondary_symptoms": ['muscle_swelling'],
    "rare_symptoms": [],
    "symptom_weights": {'nasal_congestion': 1.0, 'diminished_hearing': 0.94, 'pus_draining_from_ear': 0.77, 'muscle_swelling': 0.52}
}
disease_map["CSV_0117"] = {
    "name": "Chondromalacia Of The Patella",
    "primary_symptoms": ['knee_weakness'],
    "secondary_symptoms": ['leg_pain', 'knee_pain', 'bones_are_painful', 'knee_swelling', 'problems_with_movement'],
    "rare_symptoms": [],
    "symptom_weights": {'leg_pain': 0.49, 'knee_pain': 0.57, 'bones_are_painful': 0.47, 'knee_weakness': 0.79, 'knee_swelling': 0.49, 'problems_with_movement': 0.68}
}
disease_map["CSV_0118"] = {
    "name": "Chorioretinitis",
    "primary_symptoms": ['double_vision', 'pain_in_eye', 'muscle_swelling'],
    "secondary_symptoms": ['diminished_vision', 'spots_or_clouds_in_vision'],
    "rare_symptoms": [],
    "symptom_weights": {'diminished_vision': 0.59, 'double_vision': 0.8, 'pain_in_eye': 0.72, 'spots_or_clouds_in_vision': 0.55, 'muscle_swelling': 0.8}
}
disease_map["CSV_0119"] = {
    "name": "Chronic Back Pain",
    "primary_symptoms": [],
    "secondary_symptoms": ['leg_pain', 'hip_pain', 'back_pain', 'neck_pain', 'low_back_pain', 'loss_of_sensation', 'side_pain', 'lower_body_pain', 'groin_pain', 'back_cramps_or_spasms', 'back_stiffness_or_tightness'],
    "rare_symptoms": [],
    "symptom_weights": {'leg_pain': 0.48, 'hip_pain': 0.51, 'back_pain': 0.5, 'neck_pain': 0.51, 'low_back_pain': 0.52, 'loss_of_sensation': 0.5, 'side_pain': 0.53, 'lower_body_pain': 0.5, 'groin_pain': 0.5, 'back_cramps_or_spasms': 0.68, 'back_stiffness_or_tightness': 0.51}
}
disease_map["CSV_0120"] = {
    "name": "Chronic Constipation",
    "primary_symptoms": [],
    "secondary_symptoms": ['retention_of_urine', 'blood_in_stool', 'sharp_abdominal_pain', 'vomiting', 'nausea', 'lower_abdominal_pain', 'pain_of_the_anus', 'burning_abdominal_pain', 'changes_in_stool_appearance', 'rectal_bleeding', 'constipation'],
    "rare_symptoms": [],
    "symptom_weights": {'retention_of_urine': 0.65, 'blood_in_stool': 0.5, 'sharp_abdominal_pain': 0.49, 'vomiting': 0.52, 'nausea': 0.5, 'lower_abdominal_pain': 0.53, 'pain_of_the_anus': 0.51, 'burning_abdominal_pain': 0.5, 'changes_in_stool_appearance': 0.5, 'rectal_bleeding': 0.51, 'constipation': 0.52}
}
disease_map["CSV_0121"] = {
    "name": "Chronic Glaucoma",
    "primary_symptoms": [],
    "secondary_symptoms": ['white_discharge_from_eye', 'diminished_vision', 'symptoms_of_eye', 'pain_in_eye', 'foreign_body_sensation_in_eye', 'spots_or_clouds_in_vision', 'lacrimation', 'itchiness_of_eye', 'eye_burns_or_stings', 'mass_on_eyelid'],
    "rare_symptoms": [],
    "symptom_weights": {'white_discharge_from_eye': 0.65, 'diminished_vision': 0.5, 'symptoms_of_eye': 0.5, 'pain_in_eye': 0.51, 'foreign_body_sensation_in_eye': 0.48, 'spots_or_clouds_in_vision': 0.52, 'lacrimation': 0.49, 'itchiness_of_eye': 0.68, 'eye_burns_or_stings': 0.49, 'mass_on_eyelid': 0.49}
}
disease_map["CSV_0122"] = {
    "name": "Chronic Inflammatory Demyelinating Polyneuropathy (Cidp)",
    "primary_symptoms": ['dizziness', 'problems_with_movement'],
    "secondary_symptoms": ['weakness', 'loss_of_sensation'],
    "rare_symptoms": [],
    "symptom_weights": {'dizziness': 1.0, 'problems_with_movement': 0.83, 'weakness': 0.61, 'loss_of_sensation': 0.61}
}
disease_map["CSV_0123"] = {
    "name": "Chronic Kidney Disease",
    "primary_symptoms": ['feeling_cold', 'fatigue'],
    "secondary_symptoms": ['shortness_of_breath', 'peripheral_edema', 'symptoms_of_the_kidneys'],
    "rare_symptoms": [],
    "symptom_weights": {'shortness_of_breath': 0.4, 'peripheral_edema': 0.6, 'feeling_cold': 0.7, 'fatigue': 0.8, 'symptoms_of_the_kidneys': 0.5}
}
disease_map["CSV_0124"] = {
    "name": "Chronic Knee Pain",
    "primary_symptoms": [],
    "secondary_symptoms": ['leg_pain', 'hip_pain', 'back_pain', 'knee_pain', 'knee_weakness', 'knee_swelling', 'knee_stiffness_or_tightness', 'leg_swelling', 'joint_pain'],
    "rare_symptoms": [],
    "symptom_weights": {'leg_pain': 0.56, 'hip_pain': 0.47, 'back_pain': 0.56, 'knee_pain': 0.57, 'knee_weakness': 0.52, 'knee_swelling': 0.53, 'knee_stiffness_or_tightness': 0.48, 'leg_swelling': 0.51, 'joint_pain': 0.43}
}
disease_map["CSV_0125"] = {
    "name": "Chronic Obstructive Pulmonary Disease (Copd)",
    "primary_symptoms": [],
    "secondary_symptoms": ['shortness_of_breath', 'sharp_chest_pain', 'chest_tightness', 'sore_throat', 'cough', 'nasal_congestion', 'wheezing', 'fever', 'coughing_up_sputum', 'coryza', 'congestion_in_chest'],
    "rare_symptoms": [],
    "symptom_weights": {'shortness_of_breath': 0.49, 'sharp_chest_pain': 0.69, 'chest_tightness': 0.48, 'sore_throat': 0.5, 'cough': 0.53, 'nasal_congestion': 0.52, 'wheezing': 0.52, 'fever': 0.5, 'coughing_up_sputum': 0.53, 'coryza': 0.53, 'congestion_in_chest': 0.5}
}
disease_map["CSV_0126"] = {
    "name": "Chronic Otitis Media",
    "primary_symptoms": [],
    "secondary_symptoms": ['cough', 'nasal_congestion', 'ear_pain', 'plugged_feeling_in_ear', 'fluid_in_ear', 'fever', 'allergic_reaction', 'pulling_at_ears', 'redness_in_ear', 'painful_sinuses'],
    "rare_symptoms": [],
    "symptom_weights": {'cough': 0.66, 'nasal_congestion': 0.51, 'ear_pain': 0.5, 'plugged_feeling_in_ear': 0.5, 'fluid_in_ear': 0.49, 'fever': 0.54, 'allergic_reaction': 0.5, 'pulling_at_ears': 0.51, 'redness_in_ear': 0.5, 'painful_sinuses': 0.65}
}
disease_map["CSV_0127"] = {
    "name": "Chronic Pain Disorder",
    "primary_symptoms": [],
    "secondary_symptoms": ['leg_pain', 'hip_pain', 'sharp_abdominal_pain', 'headache', 'back_pain', 'low_back_pain', 'pelvic_pain', 'knee_pain', 'shoulder_pain', 'ache_all_over'],
    "rare_symptoms": [],
    "symptom_weights": {'leg_pain': 0.66, 'hip_pain': 0.49, 'sharp_abdominal_pain': 0.49, 'headache': 0.5, 'back_pain': 0.52, 'low_back_pain': 0.54, 'pelvic_pain': 0.67, 'knee_pain': 0.51, 'shoulder_pain': 0.48, 'ache_all_over': 0.53}
}
disease_map["CSV_0128"] = {
    "name": "Chronic Pancreatitis",
    "primary_symptoms": ['diarrhea', 'skin_growth', 'back_pain'],
    "secondary_symptoms": ['abusing_alcohol', 'sharp_abdominal_pain', 'vomiting', 'nausea', 'ache_all_over'],
    "rare_symptoms": [],
    "symptom_weights": {'abusing_alcohol': 0.55, 'sharp_abdominal_pain': 0.53, 'vomiting': 0.56, 'nausea': 0.59, 'diarrhea': 0.71, 'skin_growth': 0.74, 'back_pain': 0.72, 'ache_all_over': 0.53}
}
disease_map["CSV_0129"] = {
    "name": "Chronic Rheumatic Fever",
    "primary_symptoms": ['throat_feels_tight'],
    "secondary_symptoms": ['shortness_of_breath', 'sharp_chest_pain', 'dizziness', 'chest_tightness', 'palpitations', 'increased_heart_rate'],
    "rare_symptoms": [],
    "symptom_weights": {'shortness_of_breath': 0.47, 'sharp_chest_pain': 0.5, 'dizziness': 0.67, 'chest_tightness': 0.55, 'palpitations': 0.51, 'throat_feels_tight': 0.87, 'increased_heart_rate': 0.5}
}
disease_map["CSV_0130"] = {
    "name": "Chronic Sinusitis",
    "primary_symptoms": [],
    "secondary_symptoms": ['sore_throat', 'cough', 'headache', 'facial_pain', 'ear_pain', 'frontal_headache', 'fever', 'congestion_in_chest', 'sinus_congestion', 'painful_sinuses'],
    "rare_symptoms": [],
    "symptom_weights": {'sore_throat': 0.51, 'cough': 0.7, 'headache': 0.52, 'facial_pain': 0.5, 'ear_pain': 0.66, 'frontal_headache': 0.51, 'fever': 0.49, 'congestion_in_chest': 0.52, 'sinus_congestion': 0.51, 'painful_sinuses': 0.52}
}
disease_map["CSV_0131"] = {
    "name": "Chronic Ulcer",
    "primary_symptoms": ['skin_lesion', 'skin_pain'],
    "secondary_symptoms": [],
    "rare_symptoms": [],
    "symptom_weights": {'skin_lesion': 1.0, 'skin_pain': 1.0}
}
disease_map["CSV_0132"] = {
    "name": "Cirrhosis",
    "primary_symptoms": ['blood_in_stool', 'vomiting_blood'],
    "secondary_symptoms": ['shortness_of_breath', 'sharp_abdominal_pain', 'regurgitation', 'peripheral_edema', 'upper_abdominal_pain', 'abdominal_distention', 'regurgitation.1'],
    "rare_symptoms": [],
    "symptom_weights": {'shortness_of_breath': 0.55, 'blood_in_stool': 0.71, 'sharp_abdominal_pain': 0.5, 'vomiting_blood': 0.77, 'regurgitation': 0.52, 'peripheral_edema': 0.55, 'upper_abdominal_pain': 0.69, 'abdominal_distention': 0.55, 'regurgitation.1': 0.52}
}
disease_map["CSV_0133"] = {
    "name": "Coagulation (Bleeding) Disorder",
    "primary_symptoms": ['blood_in_urine', 'knee_swelling', 'melena'],
    "secondary_symptoms": ['leg_pain', 'eye_redness'],
    "rare_symptoms": [],
    "symptom_weights": {'leg_pain': 0.5, 'blood_in_urine': 0.8, 'knee_swelling': 0.71, 'eye_redness': 0.48, 'melena': 0.73}
}
disease_map["CSV_0134"] = {
    "name": "Cold Sore",
    "primary_symptoms": ['skin_swelling', 'lip_swelling', 'mouth_ulcer'],
    "secondary_symptoms": ['sore_throat', 'vaginal_itching', 'skin_rash', 'lip_sore'],
    "rare_symptoms": [],
    "symptom_weights": {'sore_throat': 0.55, 'skin_swelling': 0.84, 'vaginal_itching': 0.48, 'lip_swelling': 0.72, 'mouth_ulcer': 0.72, 'skin_rash': 0.55, 'lip_sore': 0.51}
}
disease_map["CSV_0135"] = {
    "name": "Colonic Polyp",
    "primary_symptoms": ['flatulence'],
    "secondary_symptoms": ['blood_in_stool', 'sharp_abdominal_pain', 'diarrhea', 'pain_of_the_anus', 'heartburn', 'upper_abdominal_pain', 'rectal_bleeding'],
    "rare_symptoms": [],
    "symptom_weights": {'blood_in_stool': 0.52, 'flatulence': 0.79, 'sharp_abdominal_pain': 0.7, 'diarrhea': 0.52, 'pain_of_the_anus': 0.66, 'heartburn': 0.51, 'upper_abdominal_pain': 0.47, 'rectal_bleeding': 0.51}
}
disease_map["CSV_0136"] = {
    "name": "Colorectal Cancer",
    "primary_symptoms": ['rectal_bleeding'],
    "secondary_symptoms": ['blood_in_stool', 'sharp_abdominal_pain', 'pain_of_the_anus', 'mass_or_swelling_around_the_anus'],
    "rare_symptoms": ['drainage_in_throat'],
    "symptom_weights": {'blood_in_stool': 0.6, 'sharp_abdominal_pain': 0.53, 'pain_of_the_anus': 0.47, 'rectal_bleeding': 0.73, 'mass_or_swelling_around_the_anus': 0.47, 'drainage_in_throat': 0.27}
}
disease_map["CSV_0137"] = {
    "name": "Complex Regional Pain Syndrome",
    "primary_symptoms": [],
    "secondary_symptoms": ['abnormal_involuntary_movements', 'leg_pain', 'hand_or_finger_pain', 'arm_pain', 'back_pain', 'neck_pain', 'low_back_pain', 'foot_or_toe_pain', 'problems_with_movement', 'loss_of_sensation', 'paresthesia', 'ache_all_over'],
    "rare_symptoms": [],
    "symptom_weights": {'abnormal_involuntary_movements': 0.49, 'leg_pain': 0.51, 'hand_or_finger_pain': 0.5, 'arm_pain': 0.51, 'back_pain': 0.53, 'neck_pain': 0.52, 'low_back_pain': 0.49, 'foot_or_toe_pain': 0.52, 'problems_with_movement': 0.48, 'loss_of_sensation': 0.49, 'paresthesia': 0.5, 'ache_all_over': 0.49}
}
disease_map["CSV_0138"] = {
    "name": "Concussion",
    "primary_symptoms": [],
    "secondary_symptoms": ['dizziness', 'difficulty_speaking', 'vomiting', 'headache', 'nausea', 'facial_pain', 'double_vision', 'back_pain', 'neck_pain', 'disturbance_of_memory', 'rib_pain', 'sleepiness'],
    "rare_symptoms": [],
    "symptom_weights": {'dizziness': 0.5, 'difficulty_speaking': 0.5, 'vomiting': 0.5, 'headache': 0.52, 'nausea': 0.53, 'facial_pain': 0.51, 'double_vision': 0.51, 'back_pain': 0.51, 'neck_pain': 0.5, 'disturbance_of_memory': 0.51, 'rib_pain': 0.5, 'sleepiness': 0.51}
}
disease_map["CSV_0139"] = {
    "name": "Conduct Disorder",
    "primary_symptoms": [],
    "secondary_symptoms": ['depression', 'depressive_or_psychotic_symptoms', 'lack_of_growth', 'abusing_alcohol', 'fainting', 'hostile_behavior', 'excessive_anger', 'seizures', 'temper_problems', 'hysterical_behavior'],
    "rare_symptoms": [],
    "symptom_weights": {'depression': 0.49, 'depressive_or_psychotic_symptoms': 0.51, 'lack_of_growth': 0.66, 'abusing_alcohol': 0.68, 'fainting': 0.47, 'hostile_behavior': 0.53, 'excessive_anger': 0.51, 'seizures': 0.51, 'temper_problems': 0.52, 'hysterical_behavior': 0.48}
}
disease_map["CSV_0140"] = {
    "name": "Conductive Hearing Loss",
    "primary_symptoms": ['hoarse_voice'],
    "secondary_symptoms": ['dizziness', 'difficulty_speaking', 'diminished_hearing', 'ear_pain', 'ringing_in_ear', 'plugged_feeling_in_ear', 'fluid_in_ear', 'redness_in_ear', 'low_self_esteem'],
    "rare_symptoms": [],
    "symptom_weights": {'dizziness': 0.46, 'hoarse_voice': 0.73, 'difficulty_speaking': 0.51, 'diminished_hearing': 0.51, 'ear_pain': 0.53, 'ringing_in_ear': 0.49, 'plugged_feeling_in_ear': 0.53, 'fluid_in_ear': 0.49, 'redness_in_ear': 0.5, 'low_self_esteem': 0.52}
}
disease_map["CSV_0141"] = {
    "name": "Congenital Heart Defect",
    "primary_symptoms": ['lack_of_growth', 'arm_swelling', 'hand_or_finger_stiffness_or_tightness'],
    "secondary_symptoms": ['sharp_chest_pain'],
    "rare_symptoms": [],
    "symptom_weights": {'sharp_chest_pain': 0.56, 'lack_of_growth': 0.72, 'arm_swelling': 0.78, 'hand_or_finger_stiffness_or_tightness': 0.92}
}
disease_map["CSV_0142"] = {
    "name": "Congenital Malformation Syndrome",
    "primary_symptoms": ['diminished_hearing', 'seizures'],
    "secondary_symptoms": ['lack_of_growth'],
    "rare_symptoms": ['gum_pain'],
    "symptom_weights": {'diminished_hearing': 1.0, 'lack_of_growth': 0.62, 'seizures': 0.77, 'gum_pain': 0.38}
}
disease_map["CSV_0143"] = {
    "name": "Conjunctivitis",
    "primary_symptoms": [],
    "secondary_symptoms": ['sore_throat', 'cough', 'nasal_congestion', 'white_discharge_from_eye', 'pain_in_eye', 'eye_redness', 'lacrimation', 'itchiness_of_eye', 'fever', 'coryza', 'swollen_eye'],
    "rare_symptoms": [],
    "symptom_weights": {'sore_throat': 0.66, 'cough': 0.51, 'nasal_congestion': 0.5, 'white_discharge_from_eye': 0.5, 'pain_in_eye': 0.54, 'eye_redness': 0.52, 'lacrimation': 0.5, 'itchiness_of_eye': 0.51, 'fever': 0.5, 'coryza': 0.53, 'swollen_eye': 0.53}
}
disease_map["CSV_0144"] = {
    "name": "Conjunctivitis Due To Allergy",
    "primary_symptoms": [],
    "secondary_symptoms": ['cough', 'nasal_congestion', 'diminished_vision', 'symptoms_of_eye', 'pain_in_eye', 'eye_redness', 'lacrimation', 'itchiness_of_eye', 'eye_burns_or_stings', 'allergic_reaction', 'swollen_eye', 'sneezing'],
    "rare_symptoms": [],
    "symptom_weights": {'cough': 0.47, 'nasal_congestion': 0.51, 'diminished_vision': 0.49, 'symptoms_of_eye': 0.51, 'pain_in_eye': 0.51, 'eye_redness': 0.52, 'lacrimation': 0.51, 'itchiness_of_eye': 0.52, 'eye_burns_or_stings': 0.48, 'allergic_reaction': 0.5, 'swollen_eye': 0.5, 'sneezing': 0.52}
}
disease_map["CSV_0145"] = {
    "name": "Conjunctivitis Due To Bacteria",
    "primary_symptoms": ['sore_throat', 'cough', 'nasal_congestion', 'abnormal_appearing_skin'],
    "secondary_symptoms": ['eye_redness', 'fever'],
    "rare_symptoms": [],
    "symptom_weights": {'sore_throat': 0.73, 'cough': 0.74, 'nasal_congestion': 0.77, 'abnormal_appearing_skin': 0.8, 'eye_redness': 0.55, 'fever': 0.52}
}
disease_map["CSV_0146"] = {
    "name": "Conjunctivitis Due To Virus",
    "primary_symptoms": [],
    "secondary_symptoms": ['cough', 'nasal_congestion', 'white_discharge_from_eye', 'diminished_vision', 'pain_in_eye', 'eye_redness', 'lacrimation', 'itchiness_of_eye', 'fever', 'swollen_eye'],
    "rare_symptoms": [],
    "symptom_weights": {'cough': 0.48, 'nasal_congestion': 0.51, 'white_discharge_from_eye': 0.5, 'diminished_vision': 0.68, 'pain_in_eye': 0.51, 'eye_redness': 0.5, 'lacrimation': 0.68, 'itchiness_of_eye': 0.5, 'fever': 0.49, 'swollen_eye': 0.51}
}
disease_map["CSV_0147"] = {
    "name": "Connective Tissue Disorder",
    "primary_symptoms": ['difficulty_in_swallowing', 'feeling_ill'],
    "secondary_symptoms": ['joint_pain'],
    "rare_symptoms": [],
    "symptom_weights": {'difficulty_in_swallowing': 1.0, 'feeling_ill': 1.0, 'joint_pain': 0.67}
}
disease_map["CSV_0148"] = {
    "name": "Contact Dermatitis",
    "primary_symptoms": [],
    "secondary_symptoms": ['skin_swelling', 'abnormal_appearing_skin', 'skin_lesion', 'acne_or_pimples', 'skin_moles', 'allergic_reaction', 'swollen_eye', 'itching_of_skin', 'skin_dryness,_peeling,_scaliness,_or_roughness', 'skin_irritation', 'skin_rash'],
    "rare_symptoms": [],
    "symptom_weights": {'skin_swelling': 0.5, 'abnormal_appearing_skin': 0.5, 'skin_lesion': 0.49, 'acne_or_pimples': 0.49, 'skin_moles': 0.68, 'allergic_reaction': 0.54, 'swollen_eye': 0.5, 'itching_of_skin': 0.51, 'skin_dryness,_peeling,_scaliness,_or_roughness': 0.51, 'skin_irritation': 0.51, 'skin_rash': 0.5}
}
disease_map["CSV_0149"] = {
    "name": "Conversion Disorder",
    "primary_symptoms": ['anxiety_and_nervousness', 'cough'],
    "secondary_symptoms": ['depression', 'seizures'],
    "rare_symptoms": [],
    "symptom_weights": {'anxiety_and_nervousness': 1.0, 'depression': 0.6, 'cough': 0.85, 'seizures': 0.6}
}
disease_map["CSV_0150"] = {
    "name": "Cornea Infection",
    "primary_symptoms": [],
    "secondary_symptoms": ['lip_swelling', 'diminished_vision', 'symptoms_of_eye', 'pain_in_eye', 'foreign_body_sensation_in_eye', 'spots_or_clouds_in_vision', 'eye_redness', 'lacrimation', 'itchiness_of_eye', 'eye_burns_or_stings', 'swollen_eye'],
    "rare_symptoms": [],
    "symptom_weights": {'lip_swelling': 0.65, 'diminished_vision': 0.52, 'symptoms_of_eye': 0.5, 'pain_in_eye': 0.52, 'foreign_body_sensation_in_eye': 0.5, 'spots_or_clouds_in_vision': 0.54, 'eye_redness': 0.51, 'lacrimation': 0.51, 'itchiness_of_eye': 0.5, 'eye_burns_or_stings': 0.51, 'swollen_eye': 0.48}
}
disease_map["CSV_0151"] = {
    "name": "Corneal Abrasion",
    "primary_symptoms": [],
    "secondary_symptoms": ['white_discharge_from_eye', 'diminished_vision', 'symptoms_of_eye', 'pain_in_eye', 'foreign_body_sensation_in_eye', 'eye_redness', 'lacrimation', 'itchiness_of_eye', 'eyelid_swelling'],
    "rare_symptoms": [],
    "symptom_weights": {'white_discharge_from_eye': 0.66, 'diminished_vision': 0.69, 'symptoms_of_eye': 0.53, 'pain_in_eye': 0.52, 'foreign_body_sensation_in_eye': 0.52, 'eye_redness': 0.49, 'lacrimation': 0.52, 'itchiness_of_eye': 0.67, 'eyelid_swelling': 0.47}
}
disease_map["CSV_0152"] = {
    "name": "Corneal Disorder",
    "primary_symptoms": [],
    "secondary_symptoms": ['white_discharge_from_eye', 'diminished_vision', 'double_vision', 'symptoms_of_eye', 'pain_in_eye', 'foreign_body_sensation_in_eye', 'spots_or_clouds_in_vision', 'eye_redness', 'lacrimation', 'itchiness_of_eye'],
    "rare_symptoms": [],
    "symptom_weights": {'white_discharge_from_eye': 0.64, 'diminished_vision': 0.52, 'double_vision': 0.68, 'symptoms_of_eye': 0.48, 'pain_in_eye': 0.51, 'foreign_body_sensation_in_eye': 0.52, 'spots_or_clouds_in_vision': 0.54, 'eye_redness': 0.49, 'lacrimation': 0.49, 'itchiness_of_eye': 0.53}
}
disease_map["CSV_0153"] = {
    "name": "Coronary Atherosclerosis",
    "primary_symptoms": ['irregular_heartbeat'],
    "secondary_symptoms": ['shortness_of_breath', 'sharp_chest_pain', 'chest_tightness', 'palpitations', 'leg_cramps_or_spasms', 'fatigue', 'burning_chest_pain'],
    "rare_symptoms": [],
    "symptom_weights": {'shortness_of_breath': 0.49, 'sharp_chest_pain': 0.5, 'chest_tightness': 0.46, 'palpitations': 0.54, 'irregular_heartbeat': 0.76, 'leg_cramps_or_spasms': 0.49, 'fatigue': 0.5, 'burning_chest_pain': 0.54}
}
disease_map["CSV_0154"] = {
    "name": "Cranial Nerve Palsy",
    "primary_symptoms": ['difficulty_speaking', 'facial_pain'],
    "secondary_symptoms": ['abnormal_involuntary_movements', 'headache', 'diminished_vision', 'double_vision', 'abnormal_movement_of_eyelid', 'symptoms_of_the_face'],
    "rare_symptoms": [],
    "symptom_weights": {'abnormal_involuntary_movements': 0.52, 'difficulty_speaking': 0.7, 'headache': 0.54, 'facial_pain': 0.77, 'diminished_vision': 0.51, 'double_vision': 0.52, 'abnormal_movement_of_eyelid': 0.69, 'symptoms_of_the_face': 0.49}
}
disease_map["CSV_0155"] = {
    "name": "Crohn Disease",
    "primary_symptoms": ['pain_of_the_anus'],
    "secondary_symptoms": ['blood_in_stool', 'sharp_abdominal_pain', 'vomiting', 'nausea', 'diarrhea', 'regurgitation', 'burning_abdominal_pain', 'regurgitation.1', 'rectal_bleeding'],
    "rare_symptoms": [],
    "symptom_weights": {'blood_in_stool': 0.49, 'sharp_abdominal_pain': 0.53, 'vomiting': 0.5, 'nausea': 0.54, 'diarrhea': 0.49, 'pain_of_the_anus': 0.78, 'regurgitation': 0.5, 'burning_abdominal_pain': 0.49, 'regurgitation.1': 0.5, 'rectal_bleeding': 0.45}
}
disease_map["CSV_0156"] = {
    "name": "Croup",
    "primary_symptoms": [],
    "secondary_symptoms": ['shortness_of_breath', 'hoarse_voice', 'sore_throat', 'cough', 'nasal_congestion', 'vomiting', 'wheezing', 'fever', 'coryza', 'abnormal_breathing_sounds', 'pulling_at_ears'],
    "rare_symptoms": [],
    "symptom_weights": {'shortness_of_breath': 0.48, 'hoarse_voice': 0.5, 'sore_throat': 0.49, 'cough': 0.52, 'nasal_congestion': 0.69, 'vomiting': 0.55, 'wheezing': 0.5, 'fever': 0.5, 'coryza': 0.49, 'abnormal_breathing_sounds': 0.51, 'pulling_at_ears': 0.52}
}
disease_map["CSV_0157"] = {
    "name": "Crushing Injury",
    "primary_symptoms": ['hand_or_finger_swelling', 'neck_swelling'],
    "secondary_symptoms": ['hand_or_finger_pain', 'hand_or_finger_stiffness_or_tightness', 'foot_or_toe_pain', 'knee_swelling'],
    "rare_symptoms": [],
    "symptom_weights": {'hand_or_finger_pain': 0.52, 'hand_or_finger_swelling': 0.71, 'hand_or_finger_stiffness_or_tightness': 0.57, 'neck_swelling': 0.76, 'foot_or_toe_pain': 0.57, 'knee_swelling': 0.63}
}
disease_map["CSV_0158"] = {
    "name": "Cryptococcosis",
    "primary_symptoms": ['depressive_or_psychotic_symptoms', 'cross_eyed'],
    "secondary_symptoms": [],
    "rare_symptoms": [],
    "symptom_weights": {'depressive_or_psychotic_symptoms': 1.0, 'cross_eyed': 1.0}
}
disease_map["CSV_0159"] = {
    "name": "Cryptorchidism",
    "primary_symptoms": ['lack_of_growth', 'symptoms_of_the_scrotum_and_testes', 'swelling_of_scrotum'],
    "secondary_symptoms": [],
    "rare_symptoms": [],
    "symptom_weights": {'lack_of_growth': 1.0, 'symptoms_of_the_scrotum_and_testes': 0.8, 'swelling_of_scrotum': 0.8}
}
disease_map["CSV_0160"] = {
    "name": "Cushing Syndrome",
    "primary_symptoms": ['emotional_symptoms', 'weight_gain'],
    "secondary_symptoms": [],
    "rare_symptoms": [],
    "symptom_weights": {'emotional_symptoms': 1.0, 'weight_gain': 0.89}
}
disease_map["CSV_0161"] = {
    "name": "Cyst Of The Eyelid",
    "primary_symptoms": ['skin_growth', 'diminished_vision', 'abnormal_movement_of_eyelid', 'muscle_swelling', 'mass_on_eyelid'],
    "secondary_symptoms": [],
    "rare_symptoms": [],
    "symptom_weights": {'skin_growth': 0.72, 'diminished_vision': 1.0, 'abnormal_movement_of_eyelid': 0.94, 'muscle_swelling': 0.72, 'mass_on_eyelid': 0.72}
}
disease_map["CSV_0162"] = {
    "name": "Cystic Fibrosis",
    "primary_symptoms": ['cough', 'intermenstrual_bleeding'],
    "secondary_symptoms": ['feeling_ill', 'decreased_appetite'],
    "rare_symptoms": [],
    "symptom_weights": {'cough': 0.73, 'feeling_ill': 0.53, 'intermenstrual_bleeding': 0.87, 'decreased_appetite': 0.67}
}
disease_map["CSV_0163"] = {
    "name": "Cysticercosis",
    "primary_symptoms": ['shortness_of_breath', 'elbow_weakness'],
    "secondary_symptoms": ['headache', 'seizures'],
    "rare_symptoms": [],
    "symptom_weights": {'shortness_of_breath': 0.83, 'elbow_weakness': 0.83, 'headache': 0.5, 'seizures': 0.53}
}
disease_map["CSV_0164"] = {
    "name": "Cystitis",
    "primary_symptoms": [],
    "secondary_symptoms": ['retention_of_urine', 'suprapubic_pain', 'sharp_abdominal_pain', 'painful_urination', 'involuntary_urination', 'frequent_urination', 'lower_abdominal_pain', 'blood_in_urine', 'back_pain', 'pelvic_pain', 'side_pain', 'symptoms_of_bladder'],
    "rare_symptoms": [],
    "symptom_weights": {'retention_of_urine': 0.48, 'suprapubic_pain': 0.5, 'sharp_abdominal_pain': 0.5, 'painful_urination': 0.49, 'involuntary_urination': 0.52, 'frequent_urination': 0.51, 'lower_abdominal_pain': 0.5, 'blood_in_urine': 0.5, 'back_pain': 0.48, 'pelvic_pain': 0.47, 'side_pain': 0.52, 'symptoms_of_bladder': 0.52}
}
disease_map["CSV_0165"] = {
    "name": "De Quervain Disease",
    "primary_symptoms": ['abnormal_involuntary_movements'],
    "secondary_symptoms": ['hand_or_finger_pain', 'wrist_pain', 'hand_or_finger_swelling', 'arm_pain', 'wrist_swelling', 'shoulder_pain'],
    "rare_symptoms": [],
    "symptom_weights": {'abnormal_involuntary_movements': 0.78, 'hand_or_finger_pain': 0.52, 'wrist_pain': 0.52, 'hand_or_finger_swelling': 0.49, 'arm_pain': 0.57, 'wrist_swelling': 0.59, 'shoulder_pain': 0.49}
}
disease_map["CSV_0166"] = {
    "name": "Decubitus Ulcer",
    "primary_symptoms": ['incontinence_of_stool'],
    "secondary_symptoms": ['difficulty_speaking', 'skin_lesion', 'skin_on_leg_or_foot_looks_infected'],
    "rare_symptoms": [],
    "symptom_weights": {'difficulty_speaking': 0.4, 'skin_lesion': 0.6, 'skin_on_leg_or_foot_looks_infected': 0.6, 'incontinence_of_stool': 0.9}
}
disease_map["CSV_0167"] = {
    "name": "Deep Vein Thrombosis (Dvt)",
    "primary_symptoms": ['leg_cramps_or_spasms'],
    "secondary_symptoms": ['leg_pain', 'arm_swelling', 'abnormal_appearing_skin', 'leg_swelling', 'foot_or_toe_swelling', 'leg_stiffness_or_tightness'],
    "rare_symptoms": [],
    "symptom_weights": {'leg_pain': 0.53, 'arm_swelling': 0.68, 'abnormal_appearing_skin': 0.69, 'leg_swelling': 0.53, 'foot_or_toe_swelling': 0.51, 'leg_cramps_or_spasms': 0.77, 'leg_stiffness_or_tightness': 0.68}
}
disease_map["CSV_0168"] = {
    "name": "Degenerative Disc Disease",
    "primary_symptoms": [],
    "secondary_symptoms": ['leg_pain', 'hip_pain', 'arm_pain', 'back_pain', 'neck_pain', 'low_back_pain', 'loss_of_sensation', 'paresthesia', 'shoulder_pain', 'lower_body_pain', 'joint_pain'],
    "rare_symptoms": [],
    "symptom_weights": {'leg_pain': 0.5, 'hip_pain': 0.5, 'arm_pain': 0.49, 'back_pain': 0.5, 'neck_pain': 0.53, 'low_back_pain': 0.52, 'loss_of_sensation': 0.52, 'paresthesia': 0.51, 'shoulder_pain': 0.68, 'lower_body_pain': 0.51, 'joint_pain': 0.52}
}
disease_map["CSV_0169"] = {
    "name": "Delirium",
    "primary_symptoms": ['slurring_words'],
    "secondary_symptoms": ['depression', 'depressive_or_psychotic_symptoms', 'abnormal_involuntary_movements', 'difficulty_speaking', 'hostile_behavior', 'problems_with_movement', 'focal_weakness', 'disturbance_of_memory', 'delusions_or_hallucinations'],
    "rare_symptoms": [],
    "symptom_weights": {'depression': 0.47, 'depressive_or_psychotic_symptoms': 0.5, 'abnormal_involuntary_movements': 0.5, 'difficulty_speaking': 0.5, 'hostile_behavior': 0.51, 'problems_with_movement': 0.53, 'focal_weakness': 0.5, 'slurring_words': 0.76, 'disturbance_of_memory': 0.5, 'delusions_or_hallucinations': 0.51}
}
disease_map["CSV_0170"] = {
    "name": "Dementia",
    "primary_symptoms": ['insomnia'],
    "secondary_symptoms": ['depressive_or_psychotic_symptoms', 'abnormal_involuntary_movements', 'hostile_behavior', 'problems_with_movement', 'focal_weakness', 'disturbance_of_memory', 'delusions_or_hallucinations'],
    "rare_symptoms": [],
    "symptom_weights": {'depressive_or_psychotic_symptoms': 0.69, 'insomnia': 0.77, 'abnormal_involuntary_movements': 0.47, 'hostile_behavior': 0.67, 'problems_with_movement': 0.47, 'focal_weakness': 0.52, 'disturbance_of_memory': 0.5, 'delusions_or_hallucinations': 0.52}
}
disease_map["CSV_0171"] = {
    "name": "Dengue Fever",
    "primary_symptoms": ['sore_throat', 'wrist_pain'],
    "secondary_symptoms": [],
    "rare_symptoms": [],
    "symptom_weights": {'sore_throat': 1.0, 'wrist_pain': 1.0}
}
disease_map["CSV_0172"] = {
    "name": "Dental Caries",
    "primary_symptoms": [],
    "secondary_symptoms": ['skin_swelling', 'toothache', 'facial_pain', 'restlessness', 'peripheral_edema', 'ear_pain', 'jaw_swelling', 'neck_swelling', 'gum_pain', 'skin_irritation', 'mouth_pain', 'pain_in_gums'],
    "rare_symptoms": [],
    "symptom_weights": {'skin_swelling': 0.48, 'toothache': 0.51, 'facial_pain': 0.52, 'restlessness': 0.52, 'peripheral_edema': 0.52, 'ear_pain': 0.51, 'jaw_swelling': 0.5, 'neck_swelling': 0.5, 'gum_pain': 0.52, 'skin_irritation': 0.49, 'mouth_pain': 0.51, 'pain_in_gums': 0.51}
}
disease_map["CSV_0173"] = {
    "name": "Depression",
    "primary_symptoms": [],
    "secondary_symptoms": ['anxiety_and_nervousness', 'depression', 'depressive_or_psychotic_symptoms', 'insomnia', 'abusing_alcohol', 'hostile_behavior', 'drug_abuse', 'excessive_anger', 'disturbance_of_memory', 'delusions_or_hallucinations', 'temper_problems'],
    "rare_symptoms": [],
    "symptom_weights": {'anxiety_and_nervousness': 0.49, 'depression': 0.5, 'depressive_or_psychotic_symptoms': 0.49, 'insomnia': 0.5, 'abusing_alcohol': 0.52, 'hostile_behavior': 0.52, 'drug_abuse': 0.51, 'excessive_anger': 0.5, 'disturbance_of_memory': 0.65, 'delusions_or_hallucinations': 0.51, 'temper_problems': 0.52}
}
disease_map["CSV_0174"] = {
    "name": "Dermatitis Due To Sun Exposure",
    "primary_symptoms": ['lack_of_growth'],
    "secondary_symptoms": ['skin_swelling', 'abnormal_appearing_skin', 'skin_lesion', 'acne_or_pimples', 'irregular_appearing_scalp', 'skin_moles', 'skin_dryness,_peeling,_scaliness,_or_roughness', 'skin_rash'],
    "rare_symptoms": [],
    "symptom_weights": {'skin_swelling': 0.5, 'lack_of_growth': 0.77, 'abnormal_appearing_skin': 0.51, 'skin_lesion': 0.51, 'acne_or_pimples': 0.67, 'irregular_appearing_scalp': 0.51, 'skin_moles': 0.52, 'skin_dryness,_peeling,_scaliness,_or_roughness': 0.53, 'skin_rash': 0.53}
}
disease_map["CSV_0175"] = {
    "name": "Developmental Disability",
    "primary_symptoms": [],
    "secondary_symptoms": ['depressive_or_psychotic_symptoms', 'difficulty_speaking', 'lack_of_growth', 'hostile_behavior', 'restlessness', 'seizures', 'delusions_or_hallucinations', 'temper_problems', 'fears_and_phobias', 'obsessions_and_compulsions', 'antisocial_behavior'],
    "rare_symptoms": [],
    "symptom_weights": {'depressive_or_psychotic_symptoms': 0.49, 'difficulty_speaking': 0.5, 'lack_of_growth': 0.49, 'hostile_behavior': 0.51, 'restlessness': 0.68, 'seizures': 0.51, 'delusions_or_hallucinations': 0.51, 'temper_problems': 0.52, 'fears_and_phobias': 0.51, 'obsessions_and_compulsions': 0.51, 'antisocial_behavior': 0.5}
}
disease_map["CSV_0176"] = {
    "name": "Deviated Nasal Septum",
    "primary_symptoms": ['facial_pain'],
    "secondary_symptoms": ['sore_throat', 'nasal_congestion', 'headache', 'difficulty_breathing', 'allergic_reaction', 'apnea', 'abnormal_breathing_sounds', 'painful_sinuses', 'nosebleed'],
    "rare_symptoms": [],
    "symptom_weights": {'sore_throat': 0.45, 'nasal_congestion': 0.49, 'headache': 0.51, 'facial_pain': 0.74, 'difficulty_breathing': 0.51, 'allergic_reaction': 0.5, 'apnea': 0.49, 'abnormal_breathing_sounds': 0.51, 'painful_sinuses': 0.52, 'nosebleed': 0.53}
}
disease_map["CSV_0177"] = {
    "name": "Diabetes Insipidus",
    "primary_symptoms": ['dizziness', 'emotional_symptoms'],
    "secondary_symptoms": [],
    "rare_symptoms": [],
    "symptom_weights": {'dizziness': 1.0, 'emotional_symptoms': 0.83}
}
disease_map["CSV_0178"] = {
    "name": "Diabetic Ketoacidosis",
    "primary_symptoms": [],
    "secondary_symptoms": ['depressive_or_psychotic_symptoms', 'sharp_chest_pain', 'sharp_abdominal_pain', 'vomiting', 'nausea', 'diarrhea', 'frequent_urination', 'weakness', 'decreased_appetite', 'fluid_retention'],
    "rare_symptoms": [],
    "symptom_weights": {'depressive_or_psychotic_symptoms': 0.49, 'sharp_chest_pain': 0.51, 'sharp_abdominal_pain': 0.51, 'vomiting': 0.51, 'nausea': 0.54, 'diarrhea': 0.51, 'frequent_urination': 0.68, 'weakness': 0.49, 'decreased_appetite': 0.67, 'fluid_retention': 0.51}
}
disease_map["CSV_0179"] = {
    "name": "Diabetic Kidney Disease",
    "primary_symptoms": ['blood_in_stool', 'impotence'],
    "secondary_symptoms": [],
    "rare_symptoms": [],
    "symptom_weights": {'blood_in_stool': 1.0, 'impotence': 1.0}
}
disease_map["CSV_0180"] = {
    "name": "Diabetic Peripheral Neuropathy",
    "primary_symptoms": ['lymphedema'],
    "secondary_symptoms": ['leg_pain', 'skin_lesion', 'foot_or_toe_pain', 'problems_with_movement', 'foot_or_toe_swelling', 'loss_of_sensation', 'paresthesia', 'foot_or_toe_stiffness_or_tightness'],
    "rare_symptoms": [],
    "symptom_weights": {'leg_pain': 0.5, 'skin_lesion': 0.51, 'foot_or_toe_pain': 0.5, 'problems_with_movement': 0.48, 'foot_or_toe_swelling': 0.5, 'loss_of_sensation': 0.48, 'paresthesia': 0.5, 'lymphedema': 0.78, 'foot_or_toe_stiffness_or_tightness': 0.68}
}
disease_map["CSV_0181"] = {
    "name": "Diabetic Retinopathy",
    "primary_symptoms": ['abnormal_movement_of_eyelid', 'foreign_body_sensation_in_eye'],
    "secondary_symptoms": ['diminished_vision', 'double_vision', 'symptoms_of_eye', 'pain_in_eye', 'spots_or_clouds_in_vision', 'lacrimation', 'itchiness_of_eye'],
    "rare_symptoms": [],
    "symptom_weights": {'diminished_vision': 0.5, 'double_vision': 0.51, 'symptoms_of_eye': 0.5, 'pain_in_eye': 0.48, 'abnormal_movement_of_eyelid': 0.75, 'foreign_body_sensation_in_eye': 0.71, 'spots_or_clouds_in_vision': 0.5, 'lacrimation': 0.49, 'itchiness_of_eye': 0.5}
}
disease_map["CSV_0182"] = {
    "name": "Diaper Rash",
    "primary_symptoms": [],
    "secondary_symptoms": ['cough', 'nasal_congestion', 'blood_in_stool', 'irritable_infant', 'vomiting', 'diarrhea', 'fever', 'temper_problems', 'pulling_at_ears', 'skin_rash', 'diaper_rash'],
    "rare_symptoms": [],
    "symptom_weights": {'cough': 0.49, 'nasal_congestion': 0.52, 'blood_in_stool': 0.5, 'irritable_infant': 0.49, 'vomiting': 0.51, 'diarrhea': 0.53, 'fever': 0.52, 'temper_problems': 0.67, 'pulling_at_ears': 0.51, 'skin_rash': 0.54, 'diaper_rash': 0.52}
}
disease_map["CSV_0183"] = {
    "name": "Dislocation Of The Ankle",
    "primary_symptoms": ['emotional_symptoms'],
    "secondary_symptoms": ['foot_or_toe_pain', 'ankle_pain', 'ankle_swelling'],
    "rare_symptoms": [],
    "symptom_weights": {'emotional_symptoms': 0.95, 'foot_or_toe_pain': 0.52, 'ankle_pain': 0.43, 'ankle_swelling': 0.62}
}
disease_map["CSV_0184"] = {
    "name": "Dislocation Of The Elbow",
    "primary_symptoms": [],
    "secondary_symptoms": ['depression', 'irritable_infant', 'wrist_pain', 'arm_pain', 'arm_stiffness_or_tightness', 'elbow_pain', 'elbow_swelling'],
    "rare_symptoms": [],
    "symptom_weights": {'depression': 0.48, 'irritable_infant': 0.63, 'wrist_pain': 0.51, 'arm_pain': 0.51, 'arm_stiffness_or_tightness': 0.62, 'elbow_pain': 0.42, 'elbow_swelling': 0.64}
}
disease_map["CSV_0185"] = {
    "name": "Dislocation Of The Finger",
    "primary_symptoms": ['difficulty_speaking'],
    "secondary_symptoms": ['hand_or_finger_pain', 'hand_or_finger_swelling', 'hand_or_finger_stiffness_or_tightness'],
    "rare_symptoms": ['wrist_pain'],
    "symptom_weights": {'difficulty_speaking': 0.78, 'hand_or_finger_pain': 0.56, 'wrist_pain': 0.39, 'hand_or_finger_swelling': 0.44, 'hand_or_finger_stiffness_or_tightness': 0.67}
}
disease_map["CSV_0186"] = {
    "name": "Dislocation Of The Foot",
    "primary_symptoms": ['elbow_weakness', 'vomiting'],
    "secondary_symptoms": ['foot_or_toe_pain'],
    "rare_symptoms": [],
    "symptom_weights": {'elbow_weakness': 0.95, 'vomiting': 1.0, 'foot_or_toe_pain': 0.47}
}
disease_map["CSV_0187"] = {
    "name": "Dislocation Of The Hip",
    "primary_symptoms": ['leg_pain', 'abusing_alcohol'],
    "secondary_symptoms": ['hip_pain'],
    "rare_symptoms": [],
    "symptom_weights": {'leg_pain': 0.83, 'hip_pain': 0.67, 'abusing_alcohol': 1.0}
}
disease_map["CSV_0188"] = {
    "name": "Dislocation Of The Knee",
    "primary_symptoms": ['knee_pain'],
    "secondary_symptoms": ['knee_swelling', 'knee_stiffness_or_tightness'],
    "rare_symptoms": [],
    "symptom_weights": {'knee_pain': 1.0, 'knee_swelling': 0.67, 'knee_stiffness_or_tightness': 0.67}
}
disease_map["CSV_0189"] = {
    "name": "Dislocation Of The Patella",
    "primary_symptoms": ['knee_pain', 'knee_stiffness_or_tightness'],
    "secondary_symptoms": ['knee_swelling'],
    "rare_symptoms": [],
    "symptom_weights": {'knee_pain': 1.0, 'knee_swelling': 0.67, 'knee_stiffness_or_tightness': 1.0}
}
disease_map["CSV_0190"] = {
    "name": "Dislocation Of The Shoulder",
    "primary_symptoms": ['neck_mass'],
    "secondary_symptoms": ['wrist_pain', 'arm_pain', 'arm_stiffness_or_tightness', 'arm_swelling', 'shoulder_pain'],
    "rare_symptoms": [],
    "symptom_weights": {'wrist_pain': 0.55, 'arm_pain': 0.58, 'arm_stiffness_or_tightness': 0.69, 'arm_swelling': 0.61, 'neck_mass': 0.77, 'shoulder_pain': 0.52}
}
disease_map["CSV_0191"] = {
    "name": "Dislocation Of The Vertebra",
    "primary_symptoms": ['leg_pain', 'elbow_weakness', 'neck_pain'],
    "secondary_symptoms": ['back_pain', 'low_back_pain'],
    "rare_symptoms": [],
    "symptom_weights": {'leg_pain': 0.97, 'elbow_weakness': 0.89, 'back_pain': 0.61, 'neck_pain': 0.74, 'low_back_pain': 0.61}
}
disease_map["CSV_0192"] = {
    "name": "Dislocation Of The Wrist",
    "primary_symptoms": ['depression', 'elbow_weakness', 'hand_or_finger_pain'],
    "secondary_symptoms": ['arm_pain'],
    "rare_symptoms": [],
    "symptom_weights": {'depression': 0.73, 'elbow_weakness': 0.84, 'hand_or_finger_pain': 0.84, 'arm_pain': 0.6}
}
disease_map["CSV_0193"] = {
    "name": "Dissociative Disorder",
    "primary_symptoms": ['back_weakness', 'excessive_anger', 'disturbance_of_memory'],
    "secondary_symptoms": ['anxiety_and_nervousness', 'depressive_or_psychotic_symptoms'],
    "rare_symptoms": [],
    "symptom_weights": {'anxiety_and_nervousness': 0.67, 'depressive_or_psychotic_symptoms': 0.55, 'back_weakness': 0.85, 'excessive_anger': 0.73, 'disturbance_of_memory': 0.77}
}
disease_map["CSV_0194"] = {
    "name": "Diverticulitis",
    "primary_symptoms": [],
    "secondary_symptoms": ['blood_in_stool', 'sharp_abdominal_pain', 'vomiting', 'nausea', 'diarrhea', 'lower_abdominal_pain', 'burning_abdominal_pain', 'side_pain', 'fever', 'upper_abdominal_pain', 'chills', 'constipation'],
    "rare_symptoms": [],
    "symptom_weights": {'blood_in_stool': 0.47, 'sharp_abdominal_pain': 0.52, 'vomiting': 0.5, 'nausea': 0.51, 'diarrhea': 0.51, 'lower_abdominal_pain': 0.51, 'burning_abdominal_pain': 0.49, 'side_pain': 0.5, 'fever': 0.49, 'upper_abdominal_pain': 0.47, 'chills': 0.5, 'constipation': 0.53}
}
disease_map["CSV_0195"] = {
    "name": "Diverticulosis",
    "primary_symptoms": [],
    "secondary_symptoms": ['blood_in_stool', 'sharp_abdominal_pain', 'vomiting', 'nausea', 'diarrhea', 'lower_abdominal_pain', 'heartburn', 'upper_abdominal_pain', 'melena', 'rectal_bleeding'],
    "rare_symptoms": [],
    "symptom_weights": {'blood_in_stool': 0.48, 'sharp_abdominal_pain': 0.51, 'vomiting': 0.49, 'nausea': 0.68, 'diarrhea': 0.5, 'lower_abdominal_pain': 0.5, 'heartburn': 0.5, 'upper_abdominal_pain': 0.51, 'melena': 0.49, 'rectal_bleeding': 0.67}
}
disease_map["CSV_0196"] = {
    "name": "Down Syndrome",
    "primary_symptoms": ['difficulty_speaking', 'nasal_congestion'],
    "secondary_symptoms": ['cough', 'lack_of_growth', 'decreased_appetite', 'seizures'],
    "rare_symptoms": [],
    "symptom_weights": {'difficulty_speaking': 0.91, 'cough': 0.52, 'nasal_congestion': 0.72, 'lack_of_growth': 0.6, 'decreased_appetite': 0.53, 'seizures': 0.51}
}
disease_map["CSV_0197"] = {
    "name": "Drug Abuse",
    "primary_symptoms": ['smoking_problems'],
    "secondary_symptoms": ['anxiety_and_nervousness', 'depression', 'depressive_or_psychotic_symptoms', 'abusing_alcohol', 'hostile_behavior', 'drug_abuse', 'delusions_or_hallucinations', 'sweating', 'antisocial_behavior'],
    "rare_symptoms": [],
    "symptom_weights": {'anxiety_and_nervousness': 0.48, 'depression': 0.5, 'depressive_or_psychotic_symptoms': 0.47, 'abusing_alcohol': 0.52, 'hostile_behavior': 0.49, 'drug_abuse': 0.54, 'smoking_problems': 0.75, 'delusions_or_hallucinations': 0.49, 'sweating': 0.51, 'antisocial_behavior': 0.55}
}
disease_map["CSV_0198"] = {
    "name": "Drug Abuse (Barbiturates)",
    "primary_symptoms": ['anxiety_and_nervousness', 'depression'],
    "secondary_symptoms": ['abnormal_involuntary_movements', 'hostile_behavior', 'drug_abuse', 'delusions_or_hallucinations'],
    "rare_symptoms": [],
    "symptom_weights": {'anxiety_and_nervousness': 0.77, 'depression': 0.87, 'abnormal_involuntary_movements': 0.58, 'hostile_behavior': 0.65, 'drug_abuse': 0.58, 'delusions_or_hallucinations': 0.47}
}
disease_map["CSV_0199"] = {
    "name": "Drug Abuse (Cocaine)",
    "primary_symptoms": ['fears_and_phobias'],
    "secondary_symptoms": ['depression', 'depressive_or_psychotic_symptoms', 'sharp_chest_pain', 'abusing_alcohol', 'hostile_behavior', 'drug_abuse', 'excessive_anger', 'delusions_or_hallucinations'],
    "rare_symptoms": [],
    "symptom_weights": {'depression': 0.54, 'depressive_or_psychotic_symptoms': 0.52, 'sharp_chest_pain': 0.51, 'abusing_alcohol': 0.56, 'hostile_behavior': 0.48, 'drug_abuse': 0.54, 'excessive_anger': 0.55, 'delusions_or_hallucinations': 0.53, 'fears_and_phobias': 0.79}
}
disease_map["CSV_0200"] = {
    "name": "Drug Abuse (Methamphetamine)",
    "primary_symptoms": ['anxiety_and_nervousness', 'hostile_behavior'],
    "secondary_symptoms": ['shortness_of_breath', 'depressive_or_psychotic_symptoms', 'palpitations', 'abusing_alcohol', 'drug_abuse', 'feeling_ill'],
    "rare_symptoms": [],
    "symptom_weights": {'anxiety_and_nervousness': 0.72, 'shortness_of_breath': 0.55, 'depressive_or_psychotic_symptoms': 0.53, 'palpitations': 0.54, 'abusing_alcohol': 0.52, 'hostile_behavior': 0.76, 'drug_abuse': 0.53, 'feeling_ill': 0.68}
}
disease_map["CSV_0201"] = {
    "name": "Drug Abuse (Opioids)",
    "primary_symptoms": ['restlessness'],
    "secondary_symptoms": ['anxiety_and_nervousness', 'depression', 'depressive_or_psychotic_symptoms', 'insomnia', 'abusing_alcohol', 'drug_abuse', 'excessive_anger', 'delusions_or_hallucinations', 'temper_problems'],
    "rare_symptoms": [],
    "symptom_weights": {'anxiety_and_nervousness': 0.49, 'depression': 0.49, 'depressive_or_psychotic_symptoms': 0.47, 'insomnia': 0.52, 'abusing_alcohol': 0.5, 'drug_abuse': 0.53, 'restlessness': 0.73, 'excessive_anger': 0.49, 'delusions_or_hallucinations': 0.49, 'temper_problems': 0.54}
}
disease_map["CSV_0202"] = {
    "name": "Drug Poisoning Due To Medication",
    "primary_symptoms": ['abusing_alcohol', 'lip_swelling'],
    "secondary_symptoms": ['depression', 'depressive_or_psychotic_symptoms', 'drug_abuse', 'slurring_words', 'sleepiness'],
    "rare_symptoms": [],
    "symptom_weights": {'depression': 0.5, 'depressive_or_psychotic_symptoms': 0.52, 'abusing_alcohol': 0.71, 'drug_abuse': 0.54, 'lip_swelling': 0.78, 'slurring_words': 0.65, 'sleepiness': 0.52}
}
disease_map["CSV_0203"] = {
    "name": "Drug Reaction",
    "primary_symptoms": [],
    "secondary_symptoms": ['shortness_of_breath', 'dizziness', 'throat_swelling', 'vomiting', 'headache', 'nausea', 'abnormal_appearing_skin', 'peripheral_edema', 'allergic_reaction', 'itching_of_skin', 'skin_rash'],
    "rare_symptoms": [],
    "symptom_weights": {'shortness_of_breath': 0.5, 'dizziness': 0.51, 'throat_swelling': 0.48, 'vomiting': 0.51, 'headache': 0.52, 'nausea': 0.69, 'abnormal_appearing_skin': 0.5, 'peripheral_edema': 0.52, 'allergic_reaction': 0.52, 'itching_of_skin': 0.5, 'skin_rash': 0.53}
}
disease_map["CSV_0204"] = {
    "name": "Drug Withdrawal",
    "primary_symptoms": ['anxiety_and_nervousness', 'depression', 'sharp_abdominal_pain'],
    "secondary_symptoms": ['dizziness', 'vomiting', 'nausea', 'chills'],
    "rare_symptoms": [],
    "symptom_weights": {'anxiety_and_nervousness': 0.7, 'depression': 0.76, 'dizziness': 0.65, 'sharp_abdominal_pain': 0.71, 'vomiting': 0.54, 'nausea': 0.49, 'chills': 0.51}
}
disease_map["CSV_0205"] = {
    "name": "Dry Eye Of Unknown Cause",
    "primary_symptoms": [],
    "secondary_symptoms": ['white_discharge_from_eye', 'diminished_vision', 'double_vision', 'symptoms_of_eye', 'pain_in_eye', 'abnormal_movement_of_eyelid', 'foreign_body_sensation_in_eye', 'spots_or_clouds_in_vision', 'eye_redness', 'lacrimation', 'itchiness_of_eye'],
    "rare_symptoms": [],
    "symptom_weights": {'white_discharge_from_eye': 0.48, 'diminished_vision': 0.54, 'double_vision': 0.49, 'symptoms_of_eye': 0.52, 'pain_in_eye': 0.54, 'abnormal_movement_of_eyelid': 0.51, 'foreign_body_sensation_in_eye': 0.68, 'spots_or_clouds_in_vision': 0.51, 'eye_redness': 0.53, 'lacrimation': 0.53, 'itchiness_of_eye': 0.5}
}
disease_map["CSV_0206"] = {
    "name": "Dumping Syndrome",
    "primary_symptoms": ['vomiting', 'nausea', 'knee_lump_or_mass'],
    "secondary_symptoms": [],
    "rare_symptoms": [],
    "symptom_weights": {'vomiting': 1.0, 'nausea': 0.75, 'knee_lump_or_mass': 0.75}
}
disease_map["CSV_0207"] = {
    "name": "Dyshidrosis",
    "primary_symptoms": ['frequent_urination'],
    "secondary_symptoms": ['abnormal_appearing_skin', 'skin_lesion', 'acne_or_pimples', 'skin_rash'],
    "rare_symptoms": [],
    "symptom_weights": {'frequent_urination': 0.84, 'abnormal_appearing_skin': 0.7, 'skin_lesion': 0.55, 'acne_or_pimples': 0.64, 'skin_rash': 0.59}
}
disease_map["CSV_0208"] = {
    "name": "Dysthymic Disorder",
    "primary_symptoms": [],
    "secondary_symptoms": ['anxiety_and_nervousness', 'depression', 'depressive_or_psychotic_symptoms', 'insomnia', 'excessive_anger', 'slurring_words', 'disturbance_of_memory', 'temper_problems', 'loss_of_sex_drive'],
    "rare_symptoms": [],
    "symptom_weights": {'anxiety_and_nervousness': 0.52, 'depression': 0.53, 'depressive_or_psychotic_symptoms': 0.51, 'insomnia': 0.52, 'excessive_anger': 0.69, 'slurring_words': 0.5, 'disturbance_of_memory': 0.52, 'temper_problems': 0.66, 'loss_of_sex_drive': 0.67}
}
disease_map["CSV_0209"] = {
    "name": "Ear Drum Damage",
    "primary_symptoms": [],
    "secondary_symptoms": ['cough', 'nasal_congestion', 'diminished_hearing', 'pus_draining_from_ear', 'ear_pain', 'ringing_in_ear', 'plugged_feeling_in_ear', 'fluid_in_ear', 'pulling_at_ears', 'redness_in_ear', 'bleeding_from_ear'],
    "rare_symptoms": [],
    "symptom_weights": {'cough': 0.5, 'nasal_congestion': 0.49, 'diminished_hearing': 0.49, 'pus_draining_from_ear': 0.67, 'ear_pain': 0.5, 'ringing_in_ear': 0.53, 'plugged_feeling_in_ear': 0.51, 'fluid_in_ear': 0.5, 'pulling_at_ears': 0.52, 'redness_in_ear': 0.52, 'bleeding_from_ear': 0.48}
}
disease_map["CSV_0210"] = {
    "name": "Ear Wax Impaction",
    "primary_symptoms": [],
    "secondary_symptoms": ['cough', 'nasal_congestion', 'diminished_hearing', 'ear_pain', 'ringing_in_ear', 'plugged_feeling_in_ear', 'fluid_in_ear', 'fever', 'pulling_at_ears', 'sinus_congestion'],
    "rare_symptoms": [],
    "symptom_weights": {'cough': 0.48, 'nasal_congestion': 0.5, 'diminished_hearing': 0.5, 'ear_pain': 0.49, 'ringing_in_ear': 0.52, 'plugged_feeling_in_ear': 0.52, 'fluid_in_ear': 0.69, 'fever': 0.5, 'pulling_at_ears': 0.5, 'sinus_congestion': 0.65}
}
disease_map["CSV_0211"] = {
    "name": "Eating Disorder",
    "primary_symptoms": ['abusing_alcohol'],
    "secondary_symptoms": ['anxiety_and_nervousness', 'depression', 'depressive_or_psychotic_symptoms', 'insomnia', 'acne_or_pimples', 'weight_gain', 'difficulty_eating', 'decreased_appetite'],
    "rare_symptoms": [],
    "symptom_weights": {'anxiety_and_nervousness': 0.52, 'depression': 0.54, 'depressive_or_psychotic_symptoms': 0.51, 'insomnia': 0.69, 'abusing_alcohol': 0.71, 'acne_or_pimples': 0.68, 'weight_gain': 0.48, 'difficulty_eating': 0.53, 'decreased_appetite': 0.5}
}
disease_map["CSV_0212"] = {
    "name": "Ectopic Pregnancy",
    "primary_symptoms": ['intermenstrual_bleeding'],
    "secondary_symptoms": ['dizziness', 'sharp_abdominal_pain', 'nausea', 'lower_abdominal_pain', 'vaginal_discharge', 'pain_during_pregnancy', 'pelvic_pain'],
    "rare_symptoms": [],
    "symptom_weights": {'dizziness': 0.52, 'sharp_abdominal_pain': 0.53, 'nausea': 0.53, 'lower_abdominal_pain': 0.68, 'vaginal_discharge': 0.65, 'intermenstrual_bleeding': 0.75, 'pain_during_pregnancy': 0.47, 'pelvic_pain': 0.49}
}
disease_map["CSV_0213"] = {
    "name": "Ectropion",
    "primary_symptoms": ['white_discharge_from_eye', 'symptoms_of_eye'],
    "secondary_symptoms": ['pain_in_eye', 'eye_redness', 'lacrimation'],
    "rare_symptoms": [],
    "symptom_weights": {'white_discharge_from_eye': 0.97, 'symptoms_of_eye': 0.79, 'pain_in_eye': 0.55, 'eye_redness': 0.61, 'lacrimation': 0.5}
}
disease_map["CSV_0214"] = {
    "name": "Eczema",
    "primary_symptoms": [],
    "secondary_symptoms": ['cough', 'skin_swelling', 'abnormal_appearing_skin', 'skin_lesion', 'acne_or_pimples', 'irregular_appearing_scalp', 'allergic_reaction', 'itching_of_skin', 'skin_dryness,_peeling,_scaliness,_or_roughness', 'skin_irritation', 'warts', 'skin_rash'],
    "rare_symptoms": [],
    "symptom_weights": {'cough': 0.49, 'skin_swelling': 0.51, 'abnormal_appearing_skin': 0.5, 'skin_lesion': 0.51, 'acne_or_pimples': 0.51, 'irregular_appearing_scalp': 0.5, 'allergic_reaction': 0.5, 'itching_of_skin': 0.52, 'skin_dryness,_peeling,_scaliness,_or_roughness': 0.49, 'skin_irritation': 0.5, 'warts': 0.51, 'skin_rash': 0.51}
}
disease_map["CSV_0215"] = {
    "name": "Edward Syndrome",
    "primary_symptoms": ['suprapubic_pain', 'cross_eyed'],
    "secondary_symptoms": [],
    "rare_symptoms": [],
    "symptom_weights": {'suprapubic_pain': 1.0, 'cross_eyed': 0.83}
}
disease_map["CSV_0216"] = {
    "name": "Emphysema",
    "primary_symptoms": ['shortness_of_breath', 'cough', 'emotional_symptoms'],
    "secondary_symptoms": ['sharp_chest_pain'],
    "rare_symptoms": [],
    "symptom_weights": {'shortness_of_breath': 0.97, 'sharp_chest_pain': 0.45, 'cough': 0.97, 'emotional_symptoms': 0.81}
}
disease_map["CSV_0217"] = {
    "name": "Empyema",
    "primary_symptoms": ['shortness_of_breath', 'sharp_chest_pain', 'leg_pain'],
    "secondary_symptoms": ['cough'],
    "rare_symptoms": [],
    "symptom_weights": {'shortness_of_breath': 0.83, 'sharp_chest_pain': 1.0, 'cough': 0.67, 'leg_pain': 1.0}
}
disease_map["CSV_0218"] = {
    "name": "Encephalitis",
    "primary_symptoms": ['insomnia', 'disturbance_of_memory'],
    "secondary_symptoms": ['dizziness', 'headache', 'loss_of_sensation'],
    "rare_symptoms": [],
    "symptom_weights": {'dizziness': 0.65, 'insomnia': 0.85, 'headache': 0.5, 'loss_of_sensation': 0.63, 'disturbance_of_memory': 0.71}
}
disease_map["CSV_0219"] = {
    "name": "Endocarditis",
    "primary_symptoms": ['palpitations', 'irregular_heartbeat'],
    "secondary_symptoms": ['shortness_of_breath', 'sharp_chest_pain', 'dizziness', 'increased_heart_rate'],
    "rare_symptoms": [],
    "symptom_weights": {'shortness_of_breath': 0.59, 'sharp_chest_pain': 0.58, 'dizziness': 0.52, 'palpitations': 0.84, 'irregular_heartbeat': 0.86, 'increased_heart_rate': 0.48}
}
disease_map["CSV_0220"] = {
    "name": "Endometrial Cancer",
    "primary_symptoms": ['vaginal_itching', 'hot_flashes', 'absence_of_menstruation'],
    "secondary_symptoms": ['intermenstrual_bleeding', 'vaginal_bleeding_after_menopause'],
    "rare_symptoms": [],
    "symptom_weights": {'vaginal_itching': 0.74, 'hot_flashes': 0.75, 'intermenstrual_bleeding': 0.51, 'absence_of_menstruation': 0.8, 'vaginal_bleeding_after_menopause': 0.6}
}
disease_map["CSV_0221"] = {
    "name": "Endometrial Hyperplasia",
    "primary_symptoms": ['back_weakness', 'involuntary_urination'],
    "secondary_symptoms": ['heavy_menstrual_flow', 'vaginal_bleeding_after_menopause'],
    "rare_symptoms": ['unpredictable_menstruation'],
    "symptom_weights": {'back_weakness': 0.84, 'involuntary_urination': 0.96, 'heavy_menstrual_flow': 0.59, 'unpredictable_menstruation': 0.39, 'vaginal_bleeding_after_menopause': 0.67}
}
disease_map["CSV_0222"] = {
    "name": "Endometriosis",
    "primary_symptoms": ['hot_flashes'],
    "secondary_symptoms": ['sharp_abdominal_pain', 'lower_abdominal_pain', 'intermenstrual_bleeding', 'pelvic_pain', 'burning_abdominal_pain', 'heavy_menstrual_flow', 'painful_menstruation', 'infertility'],
    "rare_symptoms": [],
    "symptom_weights": {'sharp_abdominal_pain': 0.5, 'lower_abdominal_pain': 0.54, 'hot_flashes': 0.8, 'intermenstrual_bleeding': 0.52, 'pelvic_pain': 0.51, 'burning_abdominal_pain': 0.53, 'heavy_menstrual_flow': 0.49, 'painful_menstruation': 0.51, 'infertility': 0.52}
}
disease_map["CSV_0223"] = {
    "name": "Endophthalmitis",
    "primary_symptoms": ['painful_urination'],
    "secondary_symptoms": ['diminished_vision', 'pain_in_eye', 'eye_redness', 'itchiness_of_eye', 'swollen_eye'],
    "rare_symptoms": [],
    "symptom_weights": {'painful_urination': 0.89, 'diminished_vision': 0.62, 'pain_in_eye': 0.57, 'eye_redness': 0.56, 'itchiness_of_eye': 0.43, 'swollen_eye': 0.52}
}
disease_map["CSV_0224"] = {
    "name": "Envenomation From Spider Or Animal Bite",
    "primary_symptoms": ['arm_swelling'],
    "secondary_symptoms": ['skin_swelling', 'hand_or_finger_swelling', 'abnormal_appearing_skin', 'foot_or_toe_swelling', 'paresthesia', 'allergic_reaction', 'fluid_retention', 'itching_of_skin'],
    "rare_symptoms": [],
    "symptom_weights": {'skin_swelling': 0.49, 'hand_or_finger_swelling': 0.52, 'arm_swelling': 0.75, 'abnormal_appearing_skin': 0.49, 'foot_or_toe_swelling': 0.48, 'paresthesia': 0.52, 'allergic_reaction': 0.51, 'fluid_retention': 0.51, 'itching_of_skin': 0.68}
}
disease_map["CSV_0225"] = {
    "name": "Ependymoma",
    "primary_symptoms": ['emotional_symptoms', 'headache', 'diminished_vision'],
    "secondary_symptoms": ['pain_in_eye'],
    "rare_symptoms": [],
    "symptom_weights": {'emotional_symptoms': 0.89, 'headache': 1.0, 'diminished_vision': 0.74, 'pain_in_eye': 0.63}
}
disease_map["CSV_0226"] = {
    "name": "Epididymitis",
    "primary_symptoms": [],
    "secondary_symptoms": ['retention_of_urine', 'swelling_of_scrotum', 'pain_in_testicles', 'mass_in_scrotum', 'sharp_abdominal_pain', 'painful_urination', 'side_pain', 'lower_body_pain', 'groin_pain'],
    "rare_symptoms": [],
    "symptom_weights": {'retention_of_urine': 0.64, 'swelling_of_scrotum': 0.5, 'pain_in_testicles': 0.51, 'mass_in_scrotum': 0.69, 'sharp_abdominal_pain': 0.53, 'painful_urination': 0.66, 'side_pain': 0.5, 'lower_body_pain': 0.49, 'groin_pain': 0.53}
}
disease_map["CSV_0227"] = {
    "name": "Epidural Hemorrhage",
    "primary_symptoms": ['depressive_or_psychotic_symptoms', 'dizziness', 'emotional_symptoms'],
    "secondary_symptoms": [],
    "rare_symptoms": [],
    "symptom_weights": {'depressive_or_psychotic_symptoms': 1.0, 'dizziness': 1.0, 'emotional_symptoms': 0.7}
}
disease_map["CSV_0228"] = {
    "name": "Epilepsy",
    "primary_symptoms": ['lack_of_growth'],
    "secondary_symptoms": ['abnormal_involuntary_movements', 'difficulty_speaking', 'headache', 'disturbance_of_memory', 'seizures', 'muscle_weakness'],
    "rare_symptoms": [],
    "symptom_weights": {'abnormal_involuntary_movements': 0.53, 'difficulty_speaking': 0.45, 'lack_of_growth': 0.8, 'headache': 0.43, 'disturbance_of_memory': 0.53, 'seizures': 0.51, 'muscle_weakness': 0.45}
}
disease_map["CSV_0229"] = {
    "name": "Erectile Dysfunction",
    "primary_symptoms": ['involuntary_urination'],
    "secondary_symptoms": ['retention_of_urine', 'pain_in_testicles', 'pain_during_intercourse', 'frequent_urination', 'blood_in_urine', 'impotence', 'symptoms_of_prostate', 'excessive_urination_at_night', 'loss_of_sex_drive'],
    "rare_symptoms": [],
    "symptom_weights": {'retention_of_urine': 0.47, 'pain_in_testicles': 0.48, 'involuntary_urination': 0.76, 'pain_during_intercourse': 0.49, 'frequent_urination': 0.52, 'blood_in_urine': 0.51, 'impotence': 0.51, 'symptoms_of_prostate': 0.52, 'excessive_urination_at_night': 0.51, 'loss_of_sex_drive': 0.54}
}
disease_map["CSV_0230"] = {
    "name": "Erythema Multiforme",
    "primary_symptoms": ['difficulty_in_swallowing', 'vomiting', 'skin_rash'],
    "secondary_symptoms": ['mouth_ulcer', 'fever'],
    "rare_symptoms": [],
    "symptom_weights": {'difficulty_in_swallowing': 0.88, 'vomiting': 0.84, 'mouth_ulcer': 0.49, 'fever': 0.53, 'skin_rash': 0.77}
}
disease_map["CSV_0231"] = {
    "name": "Esophageal Cancer",
    "primary_symptoms": ['shortness_of_breath', 'sharp_abdominal_pain', 'stomach_bloating'],
    "secondary_symptoms": ['hoarse_voice', 'decreased_appetite'],
    "rare_symptoms": [],
    "symptom_weights": {'shortness_of_breath': 0.73, 'hoarse_voice': 0.53, 'sharp_abdominal_pain': 0.9, 'decreased_appetite': 0.6, 'stomach_bloating': 0.77}
}
disease_map["CSV_0232"] = {
    "name": "Esophageal Varices",
    "primary_symptoms": ['dizziness', 'nausea'],
    "secondary_symptoms": [],
    "rare_symptoms": [],
    "symptom_weights": {'dizziness': 1.0, 'nausea': 1.0}
}
disease_map["CSV_0233"] = {
    "name": "Esophagitis",
    "primary_symptoms": [],
    "secondary_symptoms": ['shortness_of_breath', 'sharp_chest_pain', 'chest_tightness', 'sore_throat', 'cough', 'difficulty_in_swallowing', 'sharp_abdominal_pain', 'vomiting', 'nausea', 'burning_abdominal_pain', 'heartburn', 'upper_abdominal_pain'],
    "rare_symptoms": [],
    "symptom_weights": {'shortness_of_breath': 0.47, 'sharp_chest_pain': 0.5, 'chest_tightness': 0.5, 'sore_throat': 0.51, 'cough': 0.5, 'difficulty_in_swallowing': 0.53, 'sharp_abdominal_pain': 0.49, 'vomiting': 0.52, 'nausea': 0.5, 'burning_abdominal_pain': 0.47, 'heartburn': 0.5, 'upper_abdominal_pain': 0.52}
}
disease_map["CSV_0234"] = {
    "name": "Essential Tremor",
    "primary_symptoms": ['dizziness', 'hoarse_voice'],
    "secondary_symptoms": ['abnormal_involuntary_movements', 'problems_with_movement', 'muscle_pain', 'loss_of_sensation', 'disturbance_of_memory'],
    "rare_symptoms": [],
    "symptom_weights": {'dizziness': 0.73, 'abnormal_involuntary_movements': 0.57, 'hoarse_voice': 0.86, 'problems_with_movement': 0.51, 'muscle_pain': 0.5, 'loss_of_sensation': 0.68, 'disturbance_of_memory': 0.44}
}
disease_map["CSV_0235"] = {
    "name": "Eustachian Tube Dysfunction (Ear Disorder)",
    "primary_symptoms": [],
    "secondary_symptoms": ['dizziness', 'sore_throat', 'nasal_congestion', 'diminished_hearing', 'ear_pain', 'ringing_in_ear', 'plugged_feeling_in_ear', 'allergic_reaction', 'abnormal_breathing_sounds', 'redness_in_ear', 'swollen_or_red_tonsils'],
    "rare_symptoms": [],
    "symptom_weights": {'dizziness': 0.5, 'sore_throat': 0.66, 'nasal_congestion': 0.49, 'diminished_hearing': 0.5, 'ear_pain': 0.52, 'ringing_in_ear': 0.53, 'plugged_feeling_in_ear': 0.49, 'allergic_reaction': 0.5, 'abnormal_breathing_sounds': 0.54, 'redness_in_ear': 0.5, 'swollen_or_red_tonsils': 0.5}
}
disease_map["CSV_0236"] = {
    "name": "Extrapyramidal Effect Of Drugs",
    "primary_symptoms": ['headache', 'restlessness'],
    "secondary_symptoms": ['anxiety_and_nervousness', 'abnormal_involuntary_movements', 'arm_stiffness_or_tightness', 'seizures'],
    "rare_symptoms": [],
    "symptom_weights": {'anxiety_and_nervousness': 0.54, 'abnormal_involuntary_movements': 0.63, 'headache': 0.89, 'arm_stiffness_or_tightness': 0.53, 'restlessness': 0.83, 'seizures': 0.55}
}
disease_map["CSV_0237"] = {
    "name": "Eye Alignment Disorder",
    "primary_symptoms": ['lack_of_growth'],
    "secondary_symptoms": ['eye_deviation', 'diminished_vision', 'double_vision', 'cross_eyed', 'symptoms_of_eye', 'pain_in_eye', 'eye_moves_abnormally', 'irregular_appearing_scalp'],
    "rare_symptoms": [],
    "symptom_weights": {'lack_of_growth': 0.75, 'eye_deviation': 0.51, 'diminished_vision': 0.47, 'double_vision': 0.54, 'cross_eyed': 0.51, 'symptoms_of_eye': 0.53, 'pain_in_eye': 0.48, 'eye_moves_abnormally': 0.53, 'irregular_appearing_scalp': 0.69}
}
disease_map["CSV_0238"] = {
    "name": "Factitious Disorder",
    "primary_symptoms": ['depression', 'depressive_or_psychotic_symptoms', 'elbow_weakness', 'disturbance_of_memory'],
    "secondary_symptoms": [],
    "rare_symptoms": [],
    "symptom_weights": {'depression': 1.0, 'depressive_or_psychotic_symptoms': 0.77, 'elbow_weakness': 0.85, 'disturbance_of_memory': 0.77}
}
disease_map["CSV_0239"] = {
    "name": "Female Genitalia Infection",
    "primary_symptoms": ['skin_swelling', 'vaginal_discharge'],
    "secondary_symptoms": ['skin_lesion', 'vaginal_pain', 'vulvar_irritation', 'groin_pain', 'vulvar_sore'],
    "rare_symptoms": [],
    "symptom_weights": {'skin_swelling': 0.86, 'vaginal_discharge': 0.7, 'skin_lesion': 0.68, 'vaginal_pain': 0.52, 'vulvar_irritation': 0.54, 'groin_pain': 0.45, 'vulvar_sore': 0.49}
}
disease_map["CSV_0240"] = {
    "name": "Female Infertility Of Unknown Cause",
    "primary_symptoms": ['pain_during_intercourse'],
    "secondary_symptoms": ['scanty_menstrual_flow', 'long_menstrual_periods', 'unpredictable_menstruation', 'infertility'],
    "rare_symptoms": [],
    "symptom_weights": {'pain_during_intercourse': 0.89, 'scanty_menstrual_flow': 0.43, 'long_menstrual_periods': 0.64, 'unpredictable_menstruation': 0.54, 'infertility': 0.64}
}
disease_map["CSV_0241"] = {
    "name": "Fetal Alcohol Syndrome",
    "primary_symptoms": ['depressive_or_psychotic_symptoms', 'emotional_symptoms', 'excessive_anger'],
    "secondary_symptoms": [],
    "rare_symptoms": [],
    "symptom_weights": {'depressive_or_psychotic_symptoms': 1.0, 'emotional_symptoms': 0.86, 'excessive_anger': 0.71}
}
disease_map["CSV_0242"] = {
    "name": "Fibroadenoma",
    "primary_symptoms": ['vaginal_dryness', 'hot_flashes'],
    "secondary_symptoms": ['bones_are_painful', 'bleeding_or_discharge_from_nipple', 'pain_or_soreness_of_breast', 'lump_or_mass_of_breast'],
    "rare_symptoms": [],
    "symptom_weights": {'vaginal_dryness': 0.82, 'hot_flashes': 0.7, 'bones_are_painful': 0.69, 'bleeding_or_discharge_from_nipple': 0.57, 'pain_or_soreness_of_breast': 0.62, 'lump_or_mass_of_breast': 0.48}
}
disease_map["CSV_0243"] = {
    "name": "Fibrocystic Breast Disease",
    "primary_symptoms": ['intermenstrual_bleeding', 'bleeding_or_discharge_from_nipple', 'pain_or_soreness_of_breast'],
    "secondary_symptoms": ['lump_or_mass_of_breast'],
    "rare_symptoms": [],
    "symptom_weights": {'intermenstrual_bleeding': 0.93, 'bleeding_or_discharge_from_nipple': 0.71, 'pain_or_soreness_of_breast': 0.71, 'lump_or_mass_of_breast': 0.57}
}
disease_map["CSV_0244"] = {
    "name": "Fibromyalgia",
    "primary_symptoms": ['low_back_pain'],
    "secondary_symptoms": ['sharp_chest_pain', 'leg_pain', 'hip_pain', 'headache', 'arm_pain', 'back_pain', 'neck_pain', 'muscle_pain', 'ache_all_over'],
    "rare_symptoms": [],
    "symptom_weights": {'sharp_chest_pain': 0.5, 'leg_pain': 0.51, 'hip_pain': 0.67, 'headache': 0.5, 'arm_pain': 0.51, 'back_pain': 0.48, 'neck_pain': 0.51, 'low_back_pain': 0.71, 'muscle_pain': 0.51, 'ache_all_over': 0.5}
}
disease_map["CSV_0245"] = {
    "name": "Flat Feet",
    "primary_symptoms": ['skin_swelling', 'foot_or_toe_pain', 'problems_with_movement'],
    "secondary_symptoms": ['knee_pain', 'ankle_pain'],
    "rare_symptoms": [],
    "symptom_weights": {'skin_swelling': 0.97, 'knee_pain': 0.61, 'foot_or_toe_pain': 0.73, 'ankle_pain': 0.67, 'problems_with_movement': 0.82}
}
disease_map["CSV_0246"] = {
    "name": "Floaters",
    "primary_symptoms": ['symptoms_of_eye'],
    "secondary_symptoms": ['diminished_vision', 'foreign_body_sensation_in_eye', 'spots_or_clouds_in_vision', 'lacrimation'],
    "rare_symptoms": [],
    "symptom_weights": {'diminished_vision': 0.54, 'symptoms_of_eye': 0.79, 'foreign_body_sensation_in_eye': 0.67, 'spots_or_clouds_in_vision': 0.46, 'lacrimation': 0.67}
}
disease_map["CSV_0247"] = {
    "name": "Fluid Overload",
    "primary_symptoms": ['nausea'],
    "secondary_symptoms": ['shortness_of_breath', 'sharp_chest_pain', 'sharp_abdominal_pain', 'vomiting', 'hand_or_finger_swelling', 'peripheral_edema', 'fluid_retention'],
    "rare_symptoms": [],
    "symptom_weights": {'shortness_of_breath': 0.54, 'sharp_chest_pain': 0.68, 'sharp_abdominal_pain': 0.5, 'vomiting': 0.69, 'nausea': 0.76, 'hand_or_finger_swelling': 0.53, 'peripheral_edema': 0.51, 'fluid_retention': 0.48}
}
disease_map["CSV_0248"] = {
    "name": "Folate Deficiency",
    "primary_symptoms": ['sharp_abdominal_pain', 'vomiting_blood', 'difficulty_breathing'],
    "secondary_symptoms": ['shortness_of_breath', 'sharp_chest_pain'],
    "rare_symptoms": [],
    "symptom_weights": {'shortness_of_breath': 0.57, 'sharp_chest_pain': 0.48, 'sharp_abdominal_pain': 0.91, 'vomiting_blood': 0.86, 'difficulty_breathing': 0.84}
}
disease_map["CSV_0249"] = {
    "name": "Food Allergy",
    "primary_symptoms": ['lip_swelling'],
    "secondary_symptoms": ['cough', 'nasal_congestion', 'vomiting', 'hand_or_finger_swelling', 'abnormal_appearing_skin', 'allergic_reaction', 'itching_of_skin', 'skin_rash'],
    "rare_symptoms": [],
    "symptom_weights": {'cough': 0.69, 'nasal_congestion': 0.49, 'vomiting': 0.49, 'hand_or_finger_swelling': 0.51, 'lip_swelling': 0.74, 'abnormal_appearing_skin': 0.52, 'allergic_reaction': 0.53, 'itching_of_skin': 0.51, 'skin_rash': 0.49}
}
disease_map["CSV_0250"] = {
    "name": "Foreign Body In The Ear",
    "primary_symptoms": ['throat_feels_tight'],
    "secondary_symptoms": ['diminished_hearing', 'ear_pain', 'fluid_in_ear', 'bleeding_from_ear'],
    "rare_symptoms": [],
    "symptom_weights": {'diminished_hearing': 0.4, 'throat_feels_tight': 0.88, 'ear_pain': 0.52, 'fluid_in_ear': 0.4, 'bleeding_from_ear': 0.52}
}
disease_map["CSV_0251"] = {
    "name": "Foreign Body In The Eye",
    "primary_symptoms": ['white_discharge_from_eye'],
    "secondary_symptoms": ['symptoms_of_eye', 'pain_in_eye', 'foreign_body_sensation_in_eye', 'eye_redness', 'lacrimation', 'itchiness_of_eye', 'eye_burns_or_stings'],
    "rare_symptoms": [],
    "symptom_weights": {'white_discharge_from_eye': 0.82, 'symptoms_of_eye': 0.68, 'pain_in_eye': 0.5, 'foreign_body_sensation_in_eye': 0.5, 'eye_redness': 0.53, 'lacrimation': 0.46, 'itchiness_of_eye': 0.52, 'eye_burns_or_stings': 0.52}
}
disease_map["CSV_0252"] = {
    "name": "Foreign Body In The Gastrointestinal Tract",
    "primary_symptoms": ['lump_in_throat', 'recent_weight_loss'],
    "secondary_symptoms": ['difficulty_in_swallowing', 'sharp_abdominal_pain', 'vomiting', 'vomiting_blood'],
    "rare_symptoms": [],
    "symptom_weights": {'lump_in_throat': 0.78, 'difficulty_in_swallowing': 0.56, 'sharp_abdominal_pain': 0.46, 'vomiting': 0.52, 'vomiting_blood': 0.64, 'recent_weight_loss': 0.82}
}
disease_map["CSV_0253"] = {
    "name": "Foreign Body In The Nose",
    "primary_symptoms": ['nasal_congestion', 'regurgitation.1'],
    "secondary_symptoms": [],
    "rare_symptoms": [],
    "symptom_weights": {'nasal_congestion': 1.0, 'regurgitation.1': 1.0}
}
disease_map["CSV_0254"] = {
    "name": "Foreign Body In The Throat",
    "primary_symptoms": ['shortness_of_breath', 'throat_swelling'],
    "secondary_symptoms": ['sore_throat', 'cough', 'difficulty_in_swallowing', 'vomiting', 'infant_spitting_up'],
    "rare_symptoms": [],
    "symptom_weights": {'shortness_of_breath': 0.73, 'sore_throat': 0.55, 'cough': 0.51, 'throat_swelling': 0.88, 'difficulty_in_swallowing': 0.54, 'vomiting': 0.52, 'infant_spitting_up': 0.51}
}
disease_map["CSV_0255"] = {
    "name": "Foreign Body In The Vagina",
    "primary_symptoms": ['emotional_symptoms', 'painful_urination'],
    "secondary_symptoms": ['vaginal_discharge'],
    "rare_symptoms": [],
    "symptom_weights": {'emotional_symptoms': 0.9, 'painful_urination': 0.86, 'vaginal_discharge': 0.48}
}
disease_map["CSV_0256"] = {
    "name": "Fracture Of The Ankle",
    "primary_symptoms": [],
    "secondary_symptoms": ['leg_pain', 'foot_or_toe_pain', 'ankle_pain', 'knee_weakness', 'ankle_swelling', 'ankle_weakness'],
    "rare_symptoms": ['foot_or_toe_swelling'],
    "symptom_weights": {'leg_pain': 0.47, 'foot_or_toe_pain': 0.61, 'ankle_pain': 0.5, 'knee_weakness': 0.53, 'foot_or_toe_swelling': 0.36, 'ankle_swelling': 0.53, 'ankle_weakness': 0.5}
}
disease_map["CSV_0257"] = {
    "name": "Fracture Of The Arm",
    "primary_symptoms": [],
    "secondary_symptoms": ['wrist_pain', 'arm_pain', 'wrist_swelling', 'arm_stiffness_or_tightness', 'arm_swelling', 'wrist_stiffness_or_tightness', 'elbow_pain', 'shoulder_pain', 'shoulder_stiffness_or_tightness', 'elbow_swelling'],
    "rare_symptoms": [],
    "symptom_weights": {'wrist_pain': 0.5, 'arm_pain': 0.54, 'wrist_swelling': 0.56, 'arm_stiffness_or_tightness': 0.49, 'arm_swelling': 0.5, 'wrist_stiffness_or_tightness': 0.45, 'elbow_pain': 0.53, 'shoulder_pain': 0.51, 'shoulder_stiffness_or_tightness': 0.69, 'elbow_swelling': 0.52}
}
disease_map["CSV_0258"] = {
    "name": "Fracture Of The Facial Bones",
    "primary_symptoms": ['lip_swelling'],
    "secondary_symptoms": ['abusing_alcohol', 'headache', 'facial_pain', 'double_vision', 'pain_in_eye', 'peripheral_edema', 'swollen_eye', 'redness_in_or_around_nose'],
    "rare_symptoms": [],
    "symptom_weights": {'abusing_alcohol': 0.49, 'headache': 0.51, 'lip_swelling': 0.76, 'facial_pain': 0.52, 'double_vision': 0.52, 'pain_in_eye': 0.69, 'peripheral_edema': 0.51, 'swollen_eye': 0.5, 'redness_in_or_around_nose': 0.51}
}
disease_map["CSV_0259"] = {
    "name": "Fracture Of The Finger",
    "primary_symptoms": ['foot_or_toe_pain'],
    "secondary_symptoms": ['hand_or_finger_pain', 'hand_or_finger_swelling', 'hand_or_finger_stiffness_or_tightness'],
    "rare_symptoms": ['foot_or_toe_swelling'],
    "symptom_weights": {'hand_or_finger_pain': 0.5, 'hand_or_finger_swelling': 0.62, 'hand_or_finger_stiffness_or_tightness': 0.5, 'foot_or_toe_pain': 0.75, 'foot_or_toe_swelling': 0.38}
}
disease_map["CSV_0260"] = {
    "name": "Fracture Of The Foot",
    "primary_symptoms": ['foot_or_toe_pain'],
    "secondary_symptoms": ['ankle_pain', 'foot_or_toe_swelling', 'ankle_swelling', 'foot_or_toe_stiffness_or_tightness', 'foot_or_toe_weakness'],
    "rare_symptoms": [],
    "symptom_weights": {'foot_or_toe_pain': 0.79, 'ankle_pain': 0.57, 'foot_or_toe_swelling': 0.57, 'ankle_swelling': 0.57, 'foot_or_toe_stiffness_or_tightness': 0.5, 'foot_or_toe_weakness': 0.64}
}
disease_map["CSV_0261"] = {
    "name": "Fracture Of The Hand",
    "primary_symptoms": [],
    "secondary_symptoms": ['hand_or_finger_pain', 'wrist_pain', 'hand_or_finger_swelling', 'arm_pain', 'wrist_swelling', 'arm_stiffness_or_tightness', 'hand_or_finger_stiffness_or_tightness', 'wrist_stiffness_or_tightness'],
    "rare_symptoms": [],
    "symptom_weights": {'hand_or_finger_pain': 0.51, 'wrist_pain': 0.51, 'hand_or_finger_swelling': 0.5, 'arm_pain': 0.52, 'wrist_swelling': 0.59, 'arm_stiffness_or_tightness': 0.62, 'hand_or_finger_stiffness_or_tightness': 0.49, 'wrist_stiffness_or_tightness': 0.52}
}
disease_map["CSV_0262"] = {
    "name": "Fracture Of The Jaw",
    "primary_symptoms": ['pain_in_eye', 'bones_are_painful'],
    "secondary_symptoms": ['facial_pain', 'peripheral_edema', 'jaw_swelling', 'mouth_pain'],
    "rare_symptoms": [],
    "symptom_weights": {'facial_pain': 0.65, 'pain_in_eye': 0.76, 'peripheral_edema': 0.59, 'jaw_swelling': 0.55, 'bones_are_painful': 0.85, 'mouth_pain': 0.48}
}
disease_map["CSV_0263"] = {
    "name": "Fracture Of The Leg",
    "primary_symptoms": [],
    "secondary_symptoms": ['leg_pain', 'hip_pain', 'knee_pain', 'ankle_pain', 'knee_weakness', 'knee_swelling', 'problems_with_movement', 'leg_swelling', 'leg_stiffness_or_tightness', 'ankle_swelling'],
    "rare_symptoms": [],
    "symptom_weights": {'leg_pain': 0.49, 'hip_pain': 0.51, 'knee_pain': 0.49, 'ankle_pain': 0.48, 'knee_weakness': 0.66, 'knee_swelling': 0.51, 'problems_with_movement': 0.51, 'leg_swelling': 0.5, 'leg_stiffness_or_tightness': 0.64, 'ankle_swelling': 0.52}
}
disease_map["CSV_0264"] = {
    "name": "Fracture Of The Neck",
    "primary_symptoms": ['elbow_pain', 'lower_body_pain'],
    "secondary_symptoms": ['leg_pain', 'hip_pain', 'low_back_pain'],
    "rare_symptoms": [],
    "symptom_weights": {'leg_pain': 0.54, 'hip_pain': 0.54, 'low_back_pain': 0.44, 'elbow_pain': 0.71, 'lower_body_pain': 0.76}
}
disease_map["CSV_0265"] = {
    "name": "Fracture Of The Patella",
    "primary_symptoms": ['hip_pain', 'bones_are_painful'],
    "secondary_symptoms": ['leg_pain', 'knee_pain', 'knee_swelling', 'leg_weakness'],
    "rare_symptoms": [],
    "symptom_weights": {'leg_pain': 0.56, 'hip_pain': 0.73, 'knee_pain': 0.61, 'bones_are_painful': 0.87, 'knee_swelling': 0.57, 'leg_weakness': 0.59}
}
disease_map["CSV_0266"] = {
    "name": "Fracture Of The Pelvis",
    "primary_symptoms": ['difficulty_speaking', 'knee_pain'],
    "secondary_symptoms": ['leg_pain', 'hip_pain', 'back_pain', 'ache_all_over', 'groin_pain'],
    "rare_symptoms": [],
    "symptom_weights": {'difficulty_speaking': 0.82, 'leg_pain': 0.48, 'hip_pain': 0.49, 'back_pain': 0.53, 'knee_pain': 0.75, 'ache_all_over': 0.54, 'groin_pain': 0.47}
}
disease_map["CSV_0267"] = {
    "name": "Fracture Of The Rib",
    "primary_symptoms": [],
    "secondary_symptoms": ['shortness_of_breath', 'sharp_chest_pain', 'hip_pain', 'back_pain', 'bones_are_painful', 'side_pain', 'shoulder_pain', 'ache_all_over', 'rib_pain', 'back_mass_or_lump', 'hurts_to_breath'],
    "rare_symptoms": [],
    "symptom_weights": {'shortness_of_breath': 0.66, 'sharp_chest_pain': 0.52, 'hip_pain': 0.5, 'back_pain': 0.53, 'bones_are_painful': 0.52, 'side_pain': 0.52, 'shoulder_pain': 0.5, 'ache_all_over': 0.51, 'rib_pain': 0.53, 'back_mass_or_lump': 0.52, 'hurts_to_breath': 0.52}
}
disease_map["CSV_0268"] = {
    "name": "Fracture Of The Shoulder",
    "primary_symptoms": ['neck_swelling'],
    "secondary_symptoms": ['arm_pain', 'arm_stiffness_or_tightness', 'bones_are_painful', 'shoulder_pain', 'shoulder_stiffness_or_tightness', 'shoulder_swelling'],
    "rare_symptoms": [],
    "symptom_weights": {'arm_pain': 0.51, 'arm_stiffness_or_tightness': 0.51, 'neck_swelling': 0.83, 'bones_are_painful': 0.53, 'shoulder_pain': 0.54, 'shoulder_stiffness_or_tightness': 0.46, 'shoulder_swelling': 0.65}
}
disease_map["CSV_0269"] = {
    "name": "Fracture Of The Skull",
    "primary_symptoms": ['depressive_or_psychotic_symptoms', 'drug_abuse', 'vomiting'],
    "secondary_symptoms": ['diminished_hearing', 'headache'],
    "rare_symptoms": [],
    "symptom_weights": {'depressive_or_psychotic_symptoms': 0.91, 'diminished_hearing': 0.6, 'drug_abuse': 0.78, 'vomiting': 0.78, 'headache': 0.55}
}
disease_map["CSV_0270"] = {
    "name": "Fracture Of The Vertebra",
    "primary_symptoms": ['hand_or_finger_stiffness_or_tightness'],
    "secondary_symptoms": ['hip_pain', 'back_pain', 'neck_pain', 'low_back_pain', 'pelvic_pain', 'bones_are_painful', 'leg_stiffness_or_tightness'],
    "rare_symptoms": [],
    "symptom_weights": {'hip_pain': 0.49, 'hand_or_finger_stiffness_or_tightness': 0.79, 'back_pain': 0.53, 'neck_pain': 0.56, 'low_back_pain': 0.57, 'pelvic_pain': 0.51, 'bones_are_painful': 0.7, 'leg_stiffness_or_tightness': 0.45}
}
disease_map["CSV_0271"] = {
    "name": "Friedrich Ataxia",
    "primary_symptoms": ['cough', 'knee_lump_or_mass'],
    "secondary_symptoms": ['ear_pain'],
    "rare_symptoms": [],
    "symptom_weights": {'cough': 1.0, 'ear_pain': 0.6, 'knee_lump_or_mass': 1.0}
}
disease_map["CSV_0272"] = {
    "name": "Frostbite",
    "primary_symptoms": ['sharp_chest_pain', 'elbow_weakness', 'foot_or_toe_pain'],
    "secondary_symptoms": [],
    "rare_symptoms": [],
    "symptom_weights": {'sharp_chest_pain': 1.0, 'elbow_weakness': 0.92, 'foot_or_toe_pain': 0.83}
}
disease_map["CSV_0273"] = {
    "name": "Fungal Infection Of The Hair",
    "primary_symptoms": [],
    "secondary_symptoms": ['skin_swelling', 'abnormal_appearing_skin', 'skin_lesion', 'acne_or_pimples', 'skin_growth', 'irregular_appearing_scalp', 'pelvic_pain', 'itching_of_skin', 'skin_dryness,_peeling,_scaliness,_or_roughness', 'skin_irritation', 'itchy_scalp', 'skin_rash'],
    "rare_symptoms": [],
    "symptom_weights": {'skin_swelling': 0.49, 'abnormal_appearing_skin': 0.5, 'skin_lesion': 0.51, 'acne_or_pimples': 0.5, 'skin_growth': 0.52, 'irregular_appearing_scalp': 0.51, 'pelvic_pain': 0.51, 'itching_of_skin': 0.5, 'skin_dryness,_peeling,_scaliness,_or_roughness': 0.48, 'skin_irritation': 0.49, 'itchy_scalp': 0.5, 'skin_rash': 0.51}
}
disease_map["CSV_0274"] = {
    "name": "Fungal Infection Of The Skin",
    "primary_symptoms": [],
    "secondary_symptoms": ['skin_swelling', 'abnormal_appearing_skin', 'skin_lesion', 'acne_or_pimples', 'irregular_appearing_scalp', 'itching_of_skin', 'skin_dryness,_peeling,_scaliness,_or_roughness', 'itchy_scalp', 'too_little_hair', 'skin_rash'],
    "rare_symptoms": [],
    "symptom_weights": {'skin_swelling': 0.47, 'abnormal_appearing_skin': 0.5, 'skin_lesion': 0.52, 'acne_or_pimples': 0.67, 'irregular_appearing_scalp': 0.51, 'itching_of_skin': 0.52, 'skin_dryness,_peeling,_scaliness,_or_roughness': 0.49, 'itchy_scalp': 0.64, 'too_little_hair': 0.51, 'skin_rash': 0.52}
}
disease_map["CSV_0275"] = {
    "name": "G6Pd Enzyme Deficiency",
    "primary_symptoms": ['cough', 'emotional_symptoms'],
    "secondary_symptoms": [],
    "rare_symptoms": [],
    "symptom_weights": {'cough': 1.0, 'emotional_symptoms': 1.0}
}
disease_map["CSV_0276"] = {
    "name": "Galactorrhea Of Unknown Cause",
    "primary_symptoms": ['anxiety_and_nervousness'],
    "secondary_symptoms": ['emotional_symptoms', 'bleeding_or_discharge_from_nipple', 'pain_or_soreness_of_breast'],
    "rare_symptoms": [],
    "symptom_weights": {'anxiety_and_nervousness': 1.0, 'emotional_symptoms': 0.45, 'bleeding_or_discharge_from_nipple': 0.55, 'pain_or_soreness_of_breast': 0.55}
}
disease_map["CSV_0277"] = {
    "name": "Gallstone",
    "primary_symptoms": [],
    "secondary_symptoms": ['sharp_chest_pain', 'sharp_abdominal_pain', 'vomiting', 'nausea', 'back_pain', 'burning_abdominal_pain', 'heartburn', 'side_pain', 'lower_body_pain', 'upper_abdominal_pain', 'regurgitation.1'],
    "rare_symptoms": [],
    "symptom_weights": {'sharp_chest_pain': 0.48, 'sharp_abdominal_pain': 0.51, 'vomiting': 0.49, 'nausea': 0.52, 'back_pain': 0.53, 'burning_abdominal_pain': 0.52, 'heartburn': 0.5, 'side_pain': 0.51, 'lower_body_pain': 0.51, 'upper_abdominal_pain': 0.52, 'regurgitation.1': 0.67}
}
disease_map["CSV_0278"] = {
    "name": "Ganglion Cyst",
    "primary_symptoms": [],
    "secondary_symptoms": ['leg_pain', 'hand_or_finger_pain', 'wrist_swelling', 'skin_growth', 'knee_pain', 'foot_or_toe_pain', 'knee_swelling', 'knee_lump_or_mass', 'hand_or_finger_lump_or_mass', 'wrist_lump_or_mass'],
    "rare_symptoms": [],
    "symptom_weights": {'leg_pain': 0.65, 'hand_or_finger_pain': 0.51, 'wrist_swelling': 0.5, 'skin_growth': 0.52, 'knee_pain': 0.5, 'foot_or_toe_pain': 0.52, 'knee_swelling': 0.51, 'knee_lump_or_mass': 0.66, 'hand_or_finger_lump_or_mass': 0.49, 'wrist_lump_or_mass': 0.5}
}
disease_map["CSV_0279"] = {
    "name": "Gas Gangrene",
    "primary_symptoms": ['sharp_abdominal_pain', 'wrist_pain'],
    "secondary_symptoms": [],
    "rare_symptoms": [],
    "symptom_weights": {'sharp_abdominal_pain': 1.0, 'wrist_pain': 1.0}
}
disease_map["CSV_0280"] = {
    "name": "Gastritis",
    "primary_symptoms": [],
    "secondary_symptoms": ['sharp_chest_pain', 'sharp_abdominal_pain', 'vomiting', 'headache', 'nausea', 'diarrhea', 'vomiting_blood', 'burning_abdominal_pain', 'fever', 'regurgitation.1'],
    "rare_symptoms": [],
    "symptom_weights": {'sharp_chest_pain': 0.48, 'sharp_abdominal_pain': 0.51, 'vomiting': 0.49, 'headache': 0.68, 'nausea': 0.5, 'diarrhea': 0.67, 'vomiting_blood': 0.49, 'burning_abdominal_pain': 0.48, 'fever': 0.49, 'regurgitation.1': 0.5}
}
disease_map["CSV_0281"] = {
    "name": "Gastroduodenal Ulcer",
    "primary_symptoms": [],
    "secondary_symptoms": ['sharp_chest_pain', 'blood_in_stool', 'sharp_abdominal_pain', 'vomiting', 'nausea', 'vomiting_blood', 'burning_abdominal_pain', 'heartburn', 'upper_abdominal_pain', 'changes_in_stool_appearance'],
    "rare_symptoms": [],
    "symptom_weights": {'sharp_chest_pain': 0.49, 'blood_in_stool': 0.65, 'sharp_abdominal_pain': 0.51, 'vomiting': 0.52, 'nausea': 0.51, 'vomiting_blood': 0.53, 'burning_abdominal_pain': 0.47, 'heartburn': 0.51, 'upper_abdominal_pain': 0.52, 'changes_in_stool_appearance': 0.67}
}
disease_map["CSV_0282"] = {
    "name": "Gastroesophageal Reflux Disease (Gerd)",
    "primary_symptoms": ['cough'],
    "secondary_symptoms": ['sharp_chest_pain', 'chest_tightness', 'hoarse_voice', 'difficulty_in_swallowing', 'sharp_abdominal_pain', 'nausea', 'regurgitation', 'burning_abdominal_pain', 'regurgitation.1'],
    "rare_symptoms": [],
    "symptom_weights": {'sharp_chest_pain': 0.51, 'chest_tightness': 0.52, 'hoarse_voice': 0.5, 'cough': 0.75, 'difficulty_in_swallowing': 0.65, 'sharp_abdominal_pain': 0.55, 'nausea': 0.47, 'regurgitation': 0.52, 'burning_abdominal_pain': 0.49, 'regurgitation.1': 0.52}
}
disease_map["CSV_0283"] = {
    "name": "Gastrointestinal Hemorrhage",
    "primary_symptoms": [],
    "secondary_symptoms": ['dizziness', 'blood_in_stool', 'fainting', 'sharp_abdominal_pain', 'vomiting', 'nausea', 'diarrhea', 'vomiting_blood', 'weakness', 'changes_in_stool_appearance', 'melena', 'rectal_bleeding'],
    "rare_symptoms": [],
    "symptom_weights": {'dizziness': 0.47, 'blood_in_stool': 0.52, 'fainting': 0.5, 'sharp_abdominal_pain': 0.51, 'vomiting': 0.51, 'nausea': 0.51, 'diarrhea': 0.49, 'vomiting_blood': 0.5, 'weakness': 0.48, 'changes_in_stool_appearance': 0.49, 'melena': 0.49, 'rectal_bleeding': 0.51}
}
disease_map["CSV_0284"] = {
    "name": "Gastroparesis",
    "primary_symptoms": ['burning_abdominal_pain'],
    "secondary_symptoms": ['sharp_chest_pain', 'sharp_abdominal_pain', 'vomiting', 'nausea', 'regurgitation', 'upper_abdominal_pain', 'regurgitation.1'],
    "rare_symptoms": [],
    "symptom_weights": {'sharp_chest_pain': 0.69, 'sharp_abdominal_pain': 0.61, 'vomiting': 0.59, 'nausea': 0.54, 'regurgitation': 0.56, 'burning_abdominal_pain': 0.77, 'upper_abdominal_pain': 0.69, 'regurgitation.1': 0.56}
}
disease_map["CSV_0285"] = {
    "name": "Genital Herpes",
    "primary_symptoms": ['suprapubic_pain', 'vaginal_itching', 'vaginal_discharge', 'skin_lesion'],
    "secondary_symptoms": ['painful_urination', 'recent_pregnancy', 'skin_rash'],
    "rare_symptoms": [],
    "symptom_weights": {'suprapubic_pain': 0.71, 'vaginal_itching': 0.72, 'painful_urination': 0.55, 'vaginal_discharge': 0.71, 'skin_lesion': 0.74, 'recent_pregnancy': 0.69, 'skin_rash': 0.56}
}
disease_map["CSV_0286"] = {
    "name": "Gestational Diabetes",
    "primary_symptoms": ['vaginal_redness'],
    "secondary_symptoms": ['pain_during_pregnancy', 'problems_during_pregnancy', 'uterine_contractions', 'pelvic_pressure'],
    "rare_symptoms": [],
    "symptom_weights": {'pain_during_pregnancy': 0.54, 'vaginal_redness': 0.81, 'problems_during_pregnancy': 0.54, 'uterine_contractions': 0.54, 'pelvic_pressure': 0.58}
}
disease_map["CSV_0287"] = {
    "name": "Glaucoma",
    "primary_symptoms": [],
    "secondary_symptoms": ['diminished_vision', 'symptoms_of_eye', 'pain_in_eye', 'foreign_body_sensation_in_eye', 'spots_or_clouds_in_vision', 'eye_redness', 'lacrimation', 'itchiness_of_eye', 'itchy_eyelid'],
    "rare_symptoms": [],
    "symptom_weights": {'diminished_vision': 0.52, 'symptoms_of_eye': 0.53, 'pain_in_eye': 0.51, 'foreign_body_sensation_in_eye': 0.67, 'spots_or_clouds_in_vision': 0.53, 'eye_redness': 0.52, 'lacrimation': 0.53, 'itchiness_of_eye': 0.66, 'itchy_eyelid': 0.64}
}
disease_map["CSV_0288"] = {
    "name": "Glucocorticoid Deficiency",
    "primary_symptoms": ['shortness_of_breath', 'lack_of_growth', 'diarrhea'],
    "secondary_symptoms": [],
    "rare_symptoms": [],
    "symptom_weights": {'shortness_of_breath': 0.82, 'lack_of_growth': 0.94, 'diarrhea': 0.76}
}
disease_map["CSV_0289"] = {
    "name": "Goiter",
    "primary_symptoms": ['lump_in_throat', 'difficulty_in_swallowing', 'hot_flashes'],
    "secondary_symptoms": ['weight_gain', 'fatigue'],
    "rare_symptoms": [],
    "symptom_weights": {'lump_in_throat': 0.83, 'difficulty_in_swallowing': 0.77, 'hot_flashes': 0.81, 'weight_gain': 0.56, 'fatigue': 0.64}
}
disease_map["CSV_0290"] = {
    "name": "Gonorrhea",
    "primary_symptoms": ['problems_with_movement', 'vaginal_pain'],
    "secondary_symptoms": ['sharp_abdominal_pain', 'vaginal_itching', 'vaginal_discharge', 'penile_discharge'],
    "rare_symptoms": [],
    "symptom_weights": {'sharp_abdominal_pain': 0.6, 'vaginal_itching': 0.69, 'vaginal_discharge': 0.5, 'problems_with_movement': 0.86, 'vaginal_pain': 0.73, 'penile_discharge': 0.56}
}
disease_map["CSV_0291"] = {
    "name": "Gout",
    "primary_symptoms": [],
    "secondary_symptoms": ['hand_or_finger_pain', 'wrist_pain', 'hand_or_finger_swelling', 'wrist_swelling', 'knee_pain', 'foot_or_toe_pain', 'ankle_pain', 'knee_swelling', 'leg_swelling', 'foot_or_toe_swelling', 'joint_pain', 'ankle_swelling'],
    "rare_symptoms": [],
    "symptom_weights": {'hand_or_finger_pain': 0.48, 'wrist_pain': 0.5, 'hand_or_finger_swelling': 0.5, 'wrist_swelling': 0.51, 'knee_pain': 0.53, 'foot_or_toe_pain': 0.52, 'ankle_pain': 0.51, 'knee_swelling': 0.52, 'leg_swelling': 0.47, 'foot_or_toe_swelling': 0.52, 'joint_pain': 0.5, 'ankle_swelling': 0.51}
}
disease_map["CSV_0292"] = {
    "name": "Granuloma Inguinale",
    "primary_symptoms": ['sharp_chest_pain', 'knee_lump_or_mass'],
    "secondary_symptoms": [],
    "rare_symptoms": [],
    "symptom_weights": {'sharp_chest_pain': 1.0, 'knee_lump_or_mass': 0.8}
}
disease_map["CSV_0293"] = {
    "name": "Graves Disease",
    "primary_symptoms": ['irregular_heartbeat'],
    "secondary_symptoms": ['dizziness', 'abnormal_involuntary_movements', 'palpitations', 'involuntary_urination', 'hemoptysis', 'sweating'],
    "rare_symptoms": [],
    "symptom_weights": {'dizziness': 0.68, 'abnormal_involuntary_movements': 0.49, 'palpitations': 0.54, 'irregular_heartbeat': 0.77, 'involuntary_urination': 0.67, 'hemoptysis': 0.65, 'sweating': 0.51}
}
disease_map["CSV_0294"] = {
    "name": "Guillain Barre Syndrome",
    "primary_symptoms": ['dizziness', 'difficulty_speaking', 'leg_pain', 'hand_or_finger_pain'],
    "secondary_symptoms": ['loss_of_sensation'],
    "rare_symptoms": [],
    "symptom_weights": {'dizziness': 0.88, 'difficulty_speaking': 0.74, 'leg_pain': 0.84, 'hand_or_finger_pain': 0.88, 'loss_of_sensation': 0.68}
}
disease_map["CSV_0295"] = {
    "name": "Gum Disease",
    "primary_symptoms": [],
    "secondary_symptoms": ['lip_swelling', 'toothache', 'facial_pain', 'mouth_ulcer', 'peripheral_edema', 'ear_pain', 'jaw_swelling', 'fever', 'gum_pain', 'bleeding_gums', 'pain_in_gums'],
    "rare_symptoms": [],
    "symptom_weights": {'lip_swelling': 0.48, 'toothache': 0.53, 'facial_pain': 0.51, 'mouth_ulcer': 0.7, 'peripheral_edema': 0.51, 'ear_pain': 0.53, 'jaw_swelling': 0.51, 'fever': 0.5, 'gum_pain': 0.52, 'bleeding_gums': 0.5, 'pain_in_gums': 0.48}
}
disease_map["CSV_0296"] = {
    "name": "Gynecomastia",
    "primary_symptoms": [],
    "secondary_symptoms": ['skin_swelling', 'back_pain', 'neck_pain', 'bones_are_painful', 'problems_with_shape_or_size_of_breast', 'pain_or_soreness_of_breast', 'lump_or_mass_of_breast'],
    "rare_symptoms": [],
    "symptom_weights": {'skin_swelling': 0.6, 'back_pain': 0.58, 'neck_pain': 0.53, 'bones_are_painful': 0.63, 'problems_with_shape_or_size_of_breast': 0.57, 'pain_or_soreness_of_breast': 0.43, 'lump_or_mass_of_breast': 0.59}
}
disease_map["CSV_0297"] = {
    "name": "Hammer Toe",
    "primary_symptoms": ['skin_growth'],
    "secondary_symptoms": ['skin_lesion', 'foot_or_toe_pain', 'loss_of_sensation'],
    "rare_symptoms": [],
    "symptom_weights": {'skin_lesion': 0.67, 'skin_growth': 0.89, 'foot_or_toe_pain': 0.56, 'loss_of_sensation': 0.44}
}
disease_map["CSV_0298"] = {
    "name": "Hashimoto Thyroiditis",
    "primary_symptoms": ['abnormal_involuntary_movements', 'weight_gain'],
    "secondary_symptoms": [],
    "rare_symptoms": [],
    "symptom_weights": {'abnormal_involuntary_movements': 1.0, 'weight_gain': 1.0}
}
disease_map["CSV_0299"] = {
    "name": "Head And Neck Cancer",
    "primary_symptoms": ['hoarse_voice', 'hemoptysis'],
    "secondary_symptoms": ['sore_throat', 'throat_feels_tight', 'difficulty_in_swallowing', 'neck_mass', 'plugged_feeling_in_ear', 'mouth_pain'],
    "rare_symptoms": [],
    "symptom_weights": {'hoarse_voice': 0.71, 'sore_throat': 0.54, 'throat_feels_tight': 0.53, 'difficulty_in_swallowing': 0.54, 'neck_mass': 0.54, 'plugged_feeling_in_ear': 0.67, 'hemoptysis': 0.73, 'mouth_pain': 0.49}
}
disease_map["CSV_0300"] = {
    "name": "Head Injury",
    "primary_symptoms": [],
    "secondary_symptoms": ['dizziness', 'fainting', 'headache', 'lip_swelling', 'facial_pain', 'double_vision', 'back_pain', 'neck_pain'],
    "rare_symptoms": [],
    "symptom_weights": {'dizziness': 0.49, 'fainting': 0.5, 'headache': 0.5, 'lip_swelling': 0.63, 'facial_pain': 0.55, 'double_vision': 0.64, 'back_pain': 0.54, 'neck_pain': 0.52}
}
disease_map["CSV_0301"] = {
    "name": "Headache After Lumbar Puncture",
    "primary_symptoms": ['painful_urination'],
    "secondary_symptoms": ['dizziness', 'vomiting', 'headache', 'nausea', 'neck_pain', 'low_back_pain'],
    "rare_symptoms": [],
    "symptom_weights": {'dizziness': 0.47, 'vomiting': 0.5, 'headache': 0.53, 'nausea': 0.69, 'painful_urination': 0.83, 'neck_pain': 0.5, 'low_back_pain': 0.5}
}
disease_map["CSV_0302"] = {
    "name": "Heart Block",
    "primary_symptoms": ['weight_gain'],
    "secondary_symptoms": ['shortness_of_breath', 'sharp_chest_pain', 'dizziness', 'chest_tightness', 'palpitations', 'irregular_heartbeat', 'fainting', 'peripheral_edema', 'weakness'],
    "rare_symptoms": [],
    "symptom_weights": {'shortness_of_breath': 0.47, 'sharp_chest_pain': 0.47, 'dizziness': 0.48, 'chest_tightness': 0.5, 'palpitations': 0.51, 'irregular_heartbeat': 0.52, 'fainting': 0.5, 'peripheral_edema': 0.49, 'weight_gain': 0.75, 'weakness': 0.55}
}
disease_map["CSV_0303"] = {
    "name": "Heart Contusion",
    "primary_symptoms": ['depression', 'elbow_weakness'],
    "secondary_symptoms": [],
    "rare_symptoms": [],
    "symptom_weights": {'depression': 1.0, 'elbow_weakness': 0.82}
}
disease_map["CSV_0304"] = {
    "name": "Heart Failure",
    "primary_symptoms": [],
    "secondary_symptoms": ['shortness_of_breath', 'sharp_chest_pain', 'chest_tightness', 'palpitations', 'cough', 'weight_gain', 'leg_swelling', 'weakness', 'difficulty_breathing', 'fluid_retention', 'hurts_to_breath'],
    "rare_symptoms": [],
    "symptom_weights": {'shortness_of_breath': 0.49, 'sharp_chest_pain': 0.51, 'chest_tightness': 0.49, 'palpitations': 0.52, 'cough': 0.68, 'weight_gain': 0.51, 'leg_swelling': 0.5, 'weakness': 0.49, 'difficulty_breathing': 0.52, 'fluid_retention': 0.5, 'hurts_to_breath': 0.51}
}
disease_map["CSV_0305"] = {
    "name": "Heat Exhaustion",
    "primary_symptoms": ['shortness_of_breath', 'vomiting'],
    "secondary_symptoms": ['sharp_chest_pain', 'dizziness', 'fainting', 'headache', 'weakness', 'fluid_retention'],
    "rare_symptoms": [],
    "symptom_weights": {'shortness_of_breath': 0.84, 'sharp_chest_pain': 0.5, 'dizziness': 0.5, 'fainting': 0.51, 'vomiting': 0.71, 'headache': 0.48, 'weakness': 0.53, 'fluid_retention': 0.5}
}
disease_map["CSV_0306"] = {
    "name": "Heat Stroke",
    "primary_symptoms": ['dizziness', 'feeling_hot'],
    "secondary_symptoms": [],
    "rare_symptoms": [],
    "symptom_weights": {'dizziness': 1.0, 'feeling_hot': 1.0}
}
disease_map["CSV_0307"] = {
    "name": "Hemangioma",
    "primary_symptoms": [],
    "secondary_symptoms": ['skin_swelling', 'lip_swelling', 'abnormal_appearing_skin', 'skin_lesion', 'skin_growth', 'irregular_appearing_scalp', 'skin_moles', 'lymphedema', 'irregular_appearing_nails', 'skin_dryness,_peeling,_scaliness,_or_roughness'],
    "rare_symptoms": [],
    "symptom_weights": {'skin_swelling': 0.48, 'lip_swelling': 0.67, 'abnormal_appearing_skin': 0.5, 'skin_lesion': 0.51, 'skin_growth': 0.51, 'irregular_appearing_scalp': 0.67, 'skin_moles': 0.51, 'lymphedema': 0.5, 'irregular_appearing_nails': 0.48, 'skin_dryness,_peeling,_scaliness,_or_roughness': 0.5}
}
disease_map["CSV_0308"] = {
    "name": "Hemarthrosis",
    "primary_symptoms": ['elbow_weakness', 'frequent_urination', 'knee_pain'],
    "secondary_symptoms": [],
    "rare_symptoms": ['knee_swelling'],
    "symptom_weights": {'elbow_weakness': 0.78, 'frequent_urination': 1.0, 'knee_pain': 0.78, 'knee_swelling': 0.33}
}
disease_map["CSV_0309"] = {
    "name": "Hematoma",
    "primary_symptoms": ['skin_swelling', 'swelling_of_scrotum', 'arm_swelling', 'ache_all_over'],
    "secondary_symptoms": ['sharp_abdominal_pain'],
    "rare_symptoms": [],
    "symptom_weights": {'skin_swelling': 0.73, 'swelling_of_scrotum': 0.72, 'sharp_abdominal_pain': 0.68, 'arm_swelling': 0.97, 'ache_all_over': 0.78}
}
disease_map["CSV_0310"] = {
    "name": "Hemiplegia",
    "primary_symptoms": [],
    "secondary_symptoms": ['abnormal_involuntary_movements', 'difficulty_speaking', 'headache', 'arm_stiffness_or_tightness', 'problems_with_movement', 'weakness', 'loss_of_sensation', 'slurring_words', 'seizures'],
    "rare_symptoms": [],
    "symptom_weights": {'abnormal_involuntary_movements': 0.5, 'difficulty_speaking': 0.66, 'headache': 0.51, 'arm_stiffness_or_tightness': 0.55, 'problems_with_movement': 0.51, 'weakness': 0.7, 'loss_of_sensation': 0.5, 'slurring_words': 0.67, 'seizures': 0.52}
}
disease_map["CSV_0311"] = {
    "name": "Hemochromatosis",
    "primary_symptoms": ['difficulty_speaking'],
    "secondary_symptoms": ['abnormal_appearing_skin', 'ache_all_over'],
    "rare_symptoms": [],
    "symptom_weights": {'difficulty_speaking': 1.0, 'abnormal_appearing_skin': 0.67, 'ache_all_over': 0.67}
}
disease_map["CSV_0312"] = {
    "name": "Hemolytic Anemia",
    "primary_symptoms": ['nausea', 'skin_growth'],
    "secondary_symptoms": ['cough', 'fatigue'],
    "rare_symptoms": [],
    "symptom_weights": {'cough': 0.59, 'nausea': 0.78, 'skin_growth': 0.93, 'fatigue': 0.67}
}
disease_map["CSV_0313"] = {
    "name": "Hemophilia",
    "primary_symptoms": ['cough', 'frontal_headache'],
    "secondary_symptoms": ['leg_pain', 'bleeding_gums'],
    "rare_symptoms": [],
    "symptom_weights": {'cough': 0.9, 'leg_pain': 0.52, 'frontal_headache': 0.9, 'bleeding_gums': 0.62}
}
disease_map["CSV_0314"] = {
    "name": "Hemorrhoids",
    "primary_symptoms": [],
    "secondary_symptoms": ['blood_in_stool', 'sharp_abdominal_pain', 'pain_of_the_anus', 'heartburn', 'lower_body_pain', 'changes_in_stool_appearance', 'melena', 'rectal_bleeding', 'constipation', 'mass_or_swelling_around_the_anus', 'itching_of_the_anus'],
    "rare_symptoms": [],
    "symptom_weights": {'blood_in_stool': 0.5, 'sharp_abdominal_pain': 0.49, 'pain_of_the_anus': 0.49, 'heartburn': 0.69, 'lower_body_pain': 0.52, 'changes_in_stool_appearance': 0.51, 'melena': 0.5, 'rectal_bleeding': 0.52, 'constipation': 0.52, 'mass_or_swelling_around_the_anus': 0.5, 'itching_of_the_anus': 0.5}
}
disease_map["CSV_0315"] = {
    "name": "Hepatic Encephalopathy",
    "primary_symptoms": ['depressive_or_psychotic_symptoms', 'abusing_alcohol', 'fainting'],
    "secondary_symptoms": ['shortness_of_breath', 'sharp_abdominal_pain', 'fluid_retention'],
    "rare_symptoms": [],
    "symptom_weights": {'shortness_of_breath': 0.56, 'depressive_or_psychotic_symptoms': 0.76, 'abusing_alcohol': 0.96, 'fainting': 0.91, 'sharp_abdominal_pain': 0.56, 'fluid_retention': 0.56}
}
disease_map["CSV_0316"] = {
    "name": "Hepatitis Due To A Toxin",
    "primary_symptoms": ['depression', 'nausea'],
    "secondary_symptoms": ['jaundice', 'sharp_abdominal_pain', 'feeling_ill', 'vomiting', 'rectal_bleeding', 'itching_of_skin'],
    "rare_symptoms": [],
    "symptom_weights": {'depression': 0.71, 'jaundice': 0.52, 'sharp_abdominal_pain': 0.54, 'feeling_ill': 0.68, 'vomiting': 0.53, 'nausea': 0.73, 'rectal_bleeding': 0.69, 'itching_of_skin': 0.52}
}
disease_map["CSV_0317"] = {
    "name": "Herniated Disk",
    "primary_symptoms": [],
    "secondary_symptoms": ['leg_pain', 'hip_pain', 'arm_pain', 'back_pain', 'neck_pain', 'low_back_pain', 'loss_of_sensation', 'paresthesia', 'shoulder_pain', 'arm_weakness', 'leg_weakness'],
    "rare_symptoms": [],
    "symptom_weights": {'leg_pain': 0.5, 'hip_pain': 0.5, 'arm_pain': 0.66, 'back_pain': 0.52, 'neck_pain': 0.51, 'low_back_pain': 0.53, 'loss_of_sensation': 0.51, 'paresthesia': 0.52, 'shoulder_pain': 0.49, 'arm_weakness': 0.48, 'leg_weakness': 0.49}
}
disease_map["CSV_0318"] = {
    "name": "Herpangina",
    "primary_symptoms": ['swollen_lymph_nodes'],
    "secondary_symptoms": ['insomnia', 'sore_throat', 'cough', 'vomiting', 'mouth_ulcer', 'decreased_appetite', 'fever', 'skin_rash'],
    "rare_symptoms": [],
    "symptom_weights": {'insomnia': 0.68, 'sore_throat': 0.49, 'cough': 0.52, 'vomiting': 0.52, 'mouth_ulcer': 0.51, 'swollen_lymph_nodes': 0.73, 'decreased_appetite': 0.53, 'fever': 0.51, 'skin_rash': 0.51}
}
disease_map["CSV_0319"] = {
    "name": "Hiatal Hernia",
    "primary_symptoms": [],
    "secondary_symptoms": ['sharp_chest_pain', 'dizziness', 'difficulty_in_swallowing', 'sharp_abdominal_pain', 'nausea', 'back_pain', 'vomiting_blood', 'regurgitation', 'burning_abdominal_pain', 'heartburn', 'upper_abdominal_pain', 'regurgitation.1'],
    "rare_symptoms": [],
    "symptom_weights": {'sharp_chest_pain': 0.49, 'dizziness': 0.51, 'difficulty_in_swallowing': 0.68, 'sharp_abdominal_pain': 0.53, 'nausea': 0.53, 'back_pain': 0.51, 'vomiting_blood': 0.5, 'regurgitation': 0.51, 'burning_abdominal_pain': 0.51, 'heartburn': 0.51, 'upper_abdominal_pain': 0.53, 'regurgitation.1': 0.51}
}
disease_map["CSV_0320"] = {
    "name": "Hidradenitis Suppurativa",
    "primary_symptoms": ['skin_swelling', 'groin_mass', 'arm_pain', 'skin_lesion'],
    "secondary_symptoms": ['skin_growth', 'skin_rash'],
    "rare_symptoms": [],
    "symptom_weights": {'skin_swelling': 0.77, 'groin_mass': 0.85, 'arm_pain': 0.76, 'skin_lesion': 0.77, 'skin_growth': 0.55, 'skin_rash': 0.49}
}
disease_map["CSV_0321"] = {
    "name": "High Blood Pressure",
    "primary_symptoms": ['sharp_chest_pain', 'headache'],
    "secondary_symptoms": [],
    "rare_symptoms": [],
    "symptom_weights": {'sharp_chest_pain': 1.0, 'headache': 1.0}
}
disease_map["CSV_0322"] = {
    "name": "Hirschsprung Disease",
    "primary_symptoms": ['emotional_symptoms', 'sharp_abdominal_pain'],
    "secondary_symptoms": ['constipation'],
    "rare_symptoms": [],
    "symptom_weights": {'emotional_symptoms': 0.95, 'sharp_abdominal_pain': 0.84, 'constipation': 0.63}
}
disease_map["CSV_0323"] = {
    "name": "Hirsutism",
    "primary_symptoms": ['abnormal_appearing_skin', 'acne_or_pimples', 'apnea', 'unwanted_hair'],
    "secondary_symptoms": [],
    "rare_symptoms": [],
    "symptom_weights": {'abnormal_appearing_skin': 0.97, 'acne_or_pimples': 0.84, 'apnea': 0.77, 'unwanted_hair': 0.71}
}
disease_map["CSV_0324"] = {
    "name": "Histoplasmosis",
    "primary_symptoms": ['cough', 'elbow_weakness'],
    "secondary_symptoms": ['lacrimation'],
    "rare_symptoms": [],
    "symptom_weights": {'cough': 1.0, 'elbow_weakness': 1.0, 'lacrimation': 0.6}
}
disease_map["CSV_0325"] = {
    "name": "Hormone Disorder",
    "primary_symptoms": ['lack_of_growth', 'headache', 'hot_flashes', 'acne_or_pimples'],
    "secondary_symptoms": ['excessive_growth'],
    "rare_symptoms": [],
    "symptom_weights": {'lack_of_growth': 0.71, 'headache': 0.85, 'hot_flashes': 0.89, 'acne_or_pimples': 0.95, 'excessive_growth': 0.65}
}
disease_map["CSV_0326"] = {
    "name": "Hpv",
    "primary_symptoms": ['vaginal_itching', 'involuntary_urination'],
    "secondary_symptoms": ['warts'],
    "rare_symptoms": [],
    "symptom_weights": {'vaginal_itching': 0.92, 'involuntary_urination': 1.0, 'warts': 0.54}
}
disease_map["CSV_0327"] = {
    "name": "Human Immunodeficiency Virus Infection (Hiv)",
    "primary_symptoms": ['drug_abuse', 'fears_and_phobias', 'nightmares'],
    "secondary_symptoms": [],
    "rare_symptoms": [],
    "symptom_weights": {'drug_abuse': 1.0, 'fears_and_phobias': 1.0, 'nightmares': 1.0}
}
disease_map["CSV_0328"] = {
    "name": "Huntington Disease",
    "primary_symptoms": ['anxiety_and_nervousness', 'elbow_weakness'],
    "secondary_symptoms": [],
    "rare_symptoms": [],
    "symptom_weights": {'anxiety_and_nervousness': 1.0, 'elbow_weakness': 1.0}
}
disease_map["CSV_0329"] = {
    "name": "Hydatidiform Mole",
    "primary_symptoms": ['dizziness', 'sharp_abdominal_pain', 'diminished_vision'],
    "secondary_symptoms": ['pain_during_pregnancy', 'spotting_or_bleeding_during_pregnancy'],
    "rare_symptoms": [],
    "symptom_weights": {'dizziness': 0.94, 'sharp_abdominal_pain': 0.82, 'diminished_vision': 0.79, 'pain_during_pregnancy': 0.53, 'spotting_or_bleeding_during_pregnancy': 0.53}
}
disease_map["CSV_0330"] = {
    "name": "Hydrocele Of The Testicle",
    "primary_symptoms": ['symptoms_of_the_scrotum_and_testes'],
    "secondary_symptoms": ['retention_of_urine', 'groin_mass', 'swelling_of_scrotum', 'pain_in_testicles', 'mass_in_scrotum', 'lower_abdominal_pain', 'groin_pain'],
    "rare_symptoms": [],
    "symptom_weights": {'retention_of_urine': 0.48, 'groin_mass': 0.53, 'symptoms_of_the_scrotum_and_testes': 0.85, 'swelling_of_scrotum': 0.52, 'pain_in_testicles': 0.5, 'mass_in_scrotum': 0.51, 'lower_abdominal_pain': 0.5, 'groin_pain': 0.49}
}
disease_map["CSV_0331"] = {
    "name": "Hydrocephalus",
    "primary_symptoms": ['abnormal_involuntary_movements'],
    "secondary_symptoms": ['depressive_or_psychotic_symptoms', 'lack_of_growth', 'vomiting', 'headache', 'problems_with_movement', 'seizures'],
    "rare_symptoms": [],
    "symptom_weights": {'depressive_or_psychotic_symptoms': 0.54, 'abnormal_involuntary_movements': 0.9, 'lack_of_growth': 0.63, 'vomiting': 0.55, 'headache': 0.6, 'problems_with_movement': 0.51, 'seizures': 0.46}
}
disease_map["CSV_0332"] = {
    "name": "Hydronephrosis",
    "primary_symptoms": ['suprapubic_pain', 'pain_in_testicles'],
    "secondary_symptoms": ['sharp_abdominal_pain', 'vomiting', 'nausea', 'lower_abdominal_pain', 'back_pain', 'side_pain'],
    "rare_symptoms": [],
    "symptom_weights": {'suprapubic_pain': 0.72, 'pain_in_testicles': 0.76, 'sharp_abdominal_pain': 0.49, 'vomiting': 0.55, 'nausea': 0.48, 'lower_abdominal_pain': 0.69, 'back_pain': 0.5, 'side_pain': 0.51}
}
disease_map["CSV_0333"] = {
    "name": "Hypercalcemia",
    "primary_symptoms": ['retention_of_urine', 'weakness'],
    "secondary_symptoms": ['dizziness', 'loss_of_sensation'],
    "rare_symptoms": [],
    "symptom_weights": {'dizziness': 0.5, 'retention_of_urine': 1.0, 'weakness': 0.8, 'loss_of_sensation': 0.5}
}
disease_map["CSV_0334"] = {
    "name": "Hypercholesterolemia",
    "primary_symptoms": ['weight_gain'],
    "secondary_symptoms": ['sharp_chest_pain', 'palpitations', 'hand_or_finger_stiffness_or_tightness'],
    "rare_symptoms": ['excessive_urination_at_night'],
    "symptom_weights": {'sharp_chest_pain': 0.5, 'palpitations': 0.62, 'hand_or_finger_stiffness_or_tightness': 0.5, 'weight_gain': 0.75, 'excessive_urination_at_night': 0.38}
}
disease_map["CSV_0335"] = {
    "name": "Hyperemesis Gravidarum",
    "primary_symptoms": [],
    "secondary_symptoms": ['dizziness', 'sharp_abdominal_pain', 'vomiting', 'headache', 'nausea', 'diarrhea', 'pain_during_pregnancy', 'vomiting_blood', 'burning_abdominal_pain', 'weakness', 'problems_during_pregnancy'],
    "rare_symptoms": [],
    "symptom_weights": {'dizziness': 0.49, 'sharp_abdominal_pain': 0.5, 'vomiting': 0.49, 'headache': 0.5, 'nausea': 0.52, 'diarrhea': 0.51, 'pain_during_pregnancy': 0.52, 'vomiting_blood': 0.67, 'burning_abdominal_pain': 0.53, 'weakness': 0.51, 'problems_during_pregnancy': 0.5}
}
disease_map["CSV_0336"] = {
    "name": "Hypergammaglobulinemia",
    "primary_symptoms": ['blood_in_stool', 'fatigue'],
    "secondary_symptoms": [],
    "rare_symptoms": [],
    "symptom_weights": {'blood_in_stool': 1.0, 'fatigue': 1.0}
}
disease_map["CSV_0337"] = {
    "name": "Hyperhidrosis",
    "primary_symptoms": ['cough', 'warts'],
    "secondary_symptoms": ['acne_or_pimples', 'fever', 'sweating'],
    "rare_symptoms": [],
    "symptom_weights": {'cough': 1.0, 'acne_or_pimples': 0.46, 'fever': 0.62, 'sweating': 0.5, 'warts': 0.75}
}
disease_map["CSV_0338"] = {
    "name": "Hyperkalemia",
    "primary_symptoms": [],
    "secondary_symptoms": ['shortness_of_breath', 'depressive_or_psychotic_symptoms', 'sharp_chest_pain', 'dizziness', 'difficulty_in_swallowing', 'feeling_ill', 'vomiting', 'nausea', 'weakness', 'decreased_heart_rate'],
    "rare_symptoms": [],
    "symptom_weights": {'shortness_of_breath': 0.51, 'depressive_or_psychotic_symptoms': 0.69, 'sharp_chest_pain': 0.51, 'dizziness': 0.52, 'difficulty_in_swallowing': 0.48, 'feeling_ill': 0.53, 'vomiting': 0.5, 'nausea': 0.52, 'weakness': 0.53, 'decreased_heart_rate': 0.7}
}
disease_map["CSV_0339"] = {
    "name": "Hyperlipidemia",
    "primary_symptoms": ['sharp_chest_pain', 'smoking_problems'],
    "secondary_symptoms": [],
    "rare_symptoms": ['weight_gain'],
    "symptom_weights": {'sharp_chest_pain': 1.0, 'weight_gain': 0.33, 'smoking_problems': 1.0}
}
disease_map["CSV_0340"] = {
    "name": "Hypernatremia",
    "primary_symptoms": ['shortness_of_breath', 'fainting', 'fever'],
    "secondary_symptoms": ['weakness', 'difficulty_breathing'],
    "rare_symptoms": [],
    "symptom_weights": {'shortness_of_breath': 0.91, 'fainting': 0.86, 'weakness': 0.58, 'fever': 0.84, 'difficulty_breathing': 0.47}
}
disease_map["CSV_0341"] = {
    "name": "Hyperopia",
    "primary_symptoms": ['difficulty_speaking', 'eye_deviation', 'symptoms_of_eye'],
    "secondary_symptoms": ['diminished_vision', 'spots_or_clouds_in_vision', 'eye_redness'],
    "rare_symptoms": [],
    "symptom_weights": {'difficulty_speaking': 0.84, 'eye_deviation': 0.85, 'diminished_vision': 0.56, 'symptoms_of_eye': 0.74, 'spots_or_clouds_in_vision': 0.56, 'eye_redness': 0.53}
}
disease_map["CSV_0342"] = {
    "name": "Hyperosmotic Hyperketotic State",
    "primary_symptoms": ['cough', 'weakness'],
    "secondary_symptoms": ['frequent_urination'],
    "rare_symptoms": [],
    "symptom_weights": {'cough': 1.0, 'frequent_urination': 0.6, 'weakness': 0.8}
}
disease_map["CSV_0343"] = {
    "name": "Hypertension Of Pregnancy",
    "primary_symptoms": ['heartburn'],
    "secondary_symptoms": ['headache', 'pain_during_pregnancy', 'problems_during_pregnancy', 'spotting_or_bleeding_during_pregnancy', 'uterine_contractions'],
    "rare_symptoms": [],
    "symptom_weights": {'headache': 0.57, 'pain_during_pregnancy': 0.55, 'heartburn': 0.86, 'problems_during_pregnancy': 0.61, 'spotting_or_bleeding_during_pregnancy': 0.55, 'uterine_contractions': 0.55}
}
disease_map["CSV_0344"] = {
    "name": "Hypertensive Heart Disease",
    "primary_symptoms": [],
    "secondary_symptoms": ['shortness_of_breath', 'sharp_chest_pain', 'insomnia', 'chest_tightness', 'palpitations', 'leg_swelling', 'heartburn', 'weakness', 'difficulty_breathing', 'fatigue', 'recent_pregnancy'],
    "rare_symptoms": [],
    "symptom_weights": {'shortness_of_breath': 0.48, 'sharp_chest_pain': 0.51, 'insomnia': 0.49, 'chest_tightness': 0.51, 'palpitations': 0.55, 'leg_swelling': 0.68, 'heartburn': 0.49, 'weakness': 0.48, 'difficulty_breathing': 0.52, 'fatigue': 0.52, 'recent_pregnancy': 0.5}
}
disease_map["CSV_0345"] = {
    "name": "Hypertrophic Obstructive Cardiomyopathy (Hocm)",
    "primary_symptoms": ['anxiety_and_nervousness'],
    "secondary_symptoms": ['sharp_chest_pain', 'emotional_symptoms'],
    "rare_symptoms": [],
    "symptom_weights": {'anxiety_and_nervousness': 1.0, 'sharp_chest_pain': 0.67, 'emotional_symptoms': 0.67}
}
disease_map["CSV_0346"] = {
    "name": "Hypocalcemia",
    "primary_symptoms": ['shortness_of_breath', 'sharp_chest_pain', 'abnormal_involuntary_movements'],
    "secondary_symptoms": ['constipation', 'leg_weakness'],
    "rare_symptoms": [],
    "symptom_weights": {'shortness_of_breath': 0.72, 'sharp_chest_pain': 1.0, 'abnormal_involuntary_movements': 0.8, 'constipation': 0.5, 'leg_weakness': 0.46}
}
disease_map["CSV_0347"] = {
    "name": "Hypoglycemia",
    "primary_symptoms": [],
    "secondary_symptoms": ['depressive_or_psychotic_symptoms', 'dizziness', 'abnormal_involuntary_movements', 'fainting', 'feeling_ill', 'nausea', 'problems_with_movement', 'weakness', 'decreased_appetite', 'seizures', 'sleepiness', 'sweating'],
    "rare_symptoms": [],
    "symptom_weights": {'depressive_or_psychotic_symptoms': 0.48, 'dizziness': 0.5, 'abnormal_involuntary_movements': 0.5, 'fainting': 0.51, 'feeling_ill': 0.51, 'nausea': 0.51, 'problems_with_movement': 0.5, 'weakness': 0.5, 'decreased_appetite': 0.48, 'seizures': 0.51, 'sleepiness': 0.5, 'sweating': 0.51}
}
disease_map["CSV_0348"] = {
    "name": "Hypokalemia",
    "primary_symptoms": ['sharp_chest_pain'],
    "secondary_symptoms": ['shortness_of_breath', 'fainting', 'sharp_abdominal_pain', 'vomiting', 'headache', 'nausea', 'diarrhea', 'loss_of_sensation', 'fever'],
    "rare_symptoms": [],
    "symptom_weights": {'shortness_of_breath': 0.55, 'sharp_chest_pain': 0.82, 'fainting': 0.58, 'sharp_abdominal_pain': 0.56, 'vomiting': 0.56, 'headache': 0.51, 'nausea': 0.59, 'diarrhea': 0.6, 'loss_of_sensation': 0.53, 'fever': 0.54}
}
disease_map["CSV_0349"] = {
    "name": "Hyponatremia",
    "primary_symptoms": [],
    "secondary_symptoms": ['shortness_of_breath', 'sharp_chest_pain', 'fainting', 'sharp_abdominal_pain', 'vomiting', 'nausea', 'back_pain', 'weakness', 'seizures'],
    "rare_symptoms": [],
    "symptom_weights": {'shortness_of_breath': 0.69, 'sharp_chest_pain': 0.66, 'fainting': 0.52, 'sharp_abdominal_pain': 0.53, 'vomiting': 0.55, 'nausea': 0.54, 'back_pain': 0.67, 'weakness': 0.55, 'seizures': 0.51}
}
disease_map["CSV_0350"] = {
    "name": "Hypothermia",
    "primary_symptoms": ['emotional_symptoms', 'fainting'],
    "secondary_symptoms": ['depressive_or_psychotic_symptoms', 'weakness'],
    "rare_symptoms": [],
    "symptom_weights": {'depressive_or_psychotic_symptoms': 0.69, 'emotional_symptoms': 0.85, 'fainting': 1.0, 'weakness': 0.62}
}
disease_map["CSV_0351"] = {
    "name": "Hypothyroidism",
    "primary_symptoms": ['hot_flashes', 'wrist_swelling'],
    "secondary_symptoms": ['weight_gain', 'muscle_pain', 'fatigue', 'too_little_hair'],
    "rare_symptoms": [],
    "symptom_weights": {'hot_flashes': 0.72, 'wrist_swelling': 0.88, 'weight_gain': 0.57, 'muscle_pain': 0.47, 'fatigue': 0.58, 'too_little_hair': 0.54}
}
disease_map["CSV_0352"] = {
    "name": "Hypovolemia",
    "primary_symptoms": ['fainting'],
    "secondary_symptoms": ['dizziness', 'sharp_abdominal_pain', 'feeling_ill', 'vomiting', 'nausea', 'diarrhea', 'decreased_appetite', 'fever'],
    "rare_symptoms": [],
    "symptom_weights": {'dizziness': 0.69, 'fainting': 0.76, 'sharp_abdominal_pain': 0.52, 'feeling_ill': 0.53, 'vomiting': 0.54, 'nausea': 0.5, 'diarrhea': 0.56, 'decreased_appetite': 0.48, 'fever': 0.52}
}
disease_map["CSV_0353"] = {
    "name": "Idiopathic Absence Of Menstruation",
    "primary_symptoms": ['vaginal_itching'],
    "secondary_symptoms": ['sharp_abdominal_pain', 'nausea', 'lower_abdominal_pain', 'pelvic_pain', 'heartburn', 'pain_or_soreness_of_breast', 'absence_of_menstruation', 'long_menstrual_periods'],
    "rare_symptoms": [],
    "symptom_weights": {'sharp_abdominal_pain': 0.7, 'nausea': 0.5, 'vaginal_itching': 0.7, 'lower_abdominal_pain': 0.68, 'pelvic_pain': 0.52, 'heartburn': 0.52, 'pain_or_soreness_of_breast': 0.5, 'absence_of_menstruation': 0.53, 'long_menstrual_periods': 0.5}
}
disease_map["CSV_0354"] = {
    "name": "Idiopathic Excessive Menstruation",
    "primary_symptoms": [],
    "secondary_symptoms": ['sharp_abdominal_pain', 'involuntary_urination', 'vaginal_discharge', 'intermenstrual_bleeding', 'cramps_and_spasms', 'blood_clots_during_menstrual_periods', 'long_menstrual_periods', 'heavy_menstrual_flow', 'unpredictable_menstruation', 'painful_menstruation', 'frequent_menstruation'],
    "rare_symptoms": [],
    "symptom_weights": {'sharp_abdominal_pain': 0.66, 'involuntary_urination': 0.5, 'vaginal_discharge': 0.49, 'intermenstrual_bleeding': 0.5, 'cramps_and_spasms': 0.54, 'blood_clots_during_menstrual_periods': 0.51, 'long_menstrual_periods': 0.51, 'heavy_menstrual_flow': 0.5, 'unpredictable_menstruation': 0.53, 'painful_menstruation': 0.53, 'frequent_menstruation': 0.54}
}
disease_map["CSV_0355"] = {
    "name": "Idiopathic Infrequent Menstruation",
    "primary_symptoms": ['retention_of_urine', 'sharp_abdominal_pain', 'nausea'],
    "secondary_symptoms": ['unpredictable_menstruation'],
    "rare_symptoms": [],
    "symptom_weights": {'retention_of_urine': 0.74, 'sharp_abdominal_pain': 0.96, 'nausea': 0.88, 'unpredictable_menstruation': 0.46}
}
disease_map["CSV_0356"] = {
    "name": "Idiopathic Irregular Menstrual Cycle",
    "primary_symptoms": [],
    "secondary_symptoms": ['sharp_abdominal_pain', 'lower_abdominal_pain', 'intermenstrual_bleeding', 'pelvic_pain', 'cramps_and_spasms', 'long_menstrual_periods', 'heavy_menstrual_flow', 'unpredictable_menstruation', 'painful_menstruation', 'infertility', 'frequent_menstruation'],
    "rare_symptoms": [],
    "symptom_weights": {'sharp_abdominal_pain': 0.5, 'lower_abdominal_pain': 0.5, 'intermenstrual_bleeding': 0.49, 'pelvic_pain': 0.51, 'cramps_and_spasms': 0.67, 'long_menstrual_periods': 0.51, 'heavy_menstrual_flow': 0.52, 'unpredictable_menstruation': 0.52, 'painful_menstruation': 0.51, 'infertility': 0.49, 'frequent_menstruation': 0.51}
}
disease_map["CSV_0357"] = {
    "name": "Idiopathic Nonmenstrual Bleeding",
    "primary_symptoms": ['sharp_abdominal_pain', 'painful_urination', 'vaginal_discharge'],
    "secondary_symptoms": ['intermenstrual_bleeding', 'long_menstrual_periods', 'unpredictable_menstruation'],
    "rare_symptoms": [],
    "symptom_weights": {'sharp_abdominal_pain': 0.88, 'painful_urination': 0.92, 'vaginal_discharge': 0.74, 'intermenstrual_bleeding': 0.62, 'long_menstrual_periods': 0.67, 'unpredictable_menstruation': 0.56}
}
disease_map["CSV_0358"] = {
    "name": "Idiopathic Painful Menstruation",
    "primary_symptoms": [],
    "secondary_symptoms": ['sharp_abdominal_pain', 'vaginal_itching', 'lower_abdominal_pain', 'vaginal_discharge', 'pelvic_pain', 'cramps_and_spasms', 'blood_clots_during_menstrual_periods', 'long_menstrual_periods', 'heavy_menstrual_flow', 'unpredictable_menstruation', 'painful_menstruation'],
    "rare_symptoms": [],
    "symptom_weights": {'sharp_abdominal_pain': 0.49, 'vaginal_itching': 0.51, 'lower_abdominal_pain': 0.49, 'vaginal_discharge': 0.66, 'pelvic_pain': 0.53, 'cramps_and_spasms': 0.53, 'blood_clots_during_menstrual_periods': 0.5, 'long_menstrual_periods': 0.51, 'heavy_menstrual_flow': 0.52, 'unpredictable_menstruation': 0.5, 'painful_menstruation': 0.5}
}
disease_map["CSV_0359"] = {
    "name": "Ileus",
    "primary_symptoms": ['lower_abdominal_pain'],
    "secondary_symptoms": ['sharp_abdominal_pain', 'vomiting', 'headache', 'nausea', 'diarrhea', 'pain_of_the_anus', 'burning_abdominal_pain', 'constipation'],
    "rare_symptoms": [],
    "symptom_weights": {'sharp_abdominal_pain': 0.5, 'vomiting': 0.51, 'headache': 0.68, 'nausea': 0.5, 'diarrhea': 0.53, 'lower_abdominal_pain': 0.78, 'pain_of_the_anus': 0.5, 'burning_abdominal_pain': 0.5, 'constipation': 0.5}
}
disease_map["CSV_0360"] = {
    "name": "Impetigo",
    "primary_symptoms": [],
    "secondary_symptoms": ['cough', 'nasal_congestion', 'skin_swelling', 'abnormal_appearing_skin', 'skin_lesion', 'mouth_ulcer', 'fever', 'itching_of_skin', 'skin_rash', 'sore_in_nose'],
    "rare_symptoms": [],
    "symptom_weights": {'cough': 0.49, 'nasal_congestion': 0.49, 'skin_swelling': 0.66, 'abnormal_appearing_skin': 0.5, 'skin_lesion': 0.51, 'mouth_ulcer': 0.68, 'fever': 0.49, 'itching_of_skin': 0.48, 'skin_rash': 0.5, 'sore_in_nose': 0.5}
}
disease_map["CSV_0361"] = {
    "name": "Impulse Control Disorder",
    "primary_symptoms": ['anxiety_and_nervousness', 'excessive_appetite', 'delusions_or_hallucinations'],
    "secondary_symptoms": ['depression', 'depressive_or_psychotic_symptoms', 'insomnia', 'excessive_anger', 'temper_problems'],
    "rare_symptoms": [],
    "symptom_weights": {'anxiety_and_nervousness': 0.71, 'depression': 0.52, 'depressive_or_psychotic_symptoms': 0.52, 'insomnia': 0.51, 'excessive_appetite': 0.73, 'excessive_anger': 0.52, 'delusions_or_hallucinations': 0.71, 'temper_problems': 0.56}
}
disease_map["CSV_0362"] = {
    "name": "Indigestion",
    "primary_symptoms": ['stomach_bloating'],
    "secondary_symptoms": ['sharp_chest_pain', 'sharp_abdominal_pain', 'vomiting', 'nausea', 'diarrhea', 'burning_abdominal_pain', 'heartburn', 'decreased_appetite'],
    "rare_symptoms": [],
    "symptom_weights": {'sharp_chest_pain': 0.5, 'sharp_abdominal_pain': 0.52, 'vomiting': 0.5, 'nausea': 0.5, 'diarrhea': 0.52, 'burning_abdominal_pain': 0.49, 'heartburn': 0.69, 'decreased_appetite': 0.5, 'stomach_bloating': 0.74}
}
disease_map["CSV_0363"] = {
    "name": "Induced Abortion",
    "primary_symptoms": ['intermenstrual_bleeding', 'groin_pain'],
    "secondary_symptoms": ['sharp_abdominal_pain', 'lower_abdominal_pain', 'vaginal_discharge', 'pain_during_pregnancy', 'spotting_or_bleeding_during_pregnancy', 'cramps_and_spasms'],
    "rare_symptoms": [],
    "symptom_weights": {'sharp_abdominal_pain': 0.55, 'lower_abdominal_pain': 0.49, 'vaginal_discharge': 0.5, 'intermenstrual_bleeding': 0.79, 'pain_during_pregnancy': 0.55, 'spotting_or_bleeding_during_pregnancy': 0.53, 'cramps_and_spasms': 0.5, 'groin_pain': 0.77}
}
disease_map["CSV_0364"] = {
    "name": "Infection Of Open Wound",
    "primary_symptoms": ['insomnia', 'leg_pain', 'hand_or_finger_swelling'],
    "secondary_symptoms": ['abnormal_appearing_skin'],
    "rare_symptoms": [],
    "symptom_weights": {'insomnia': 0.89, 'leg_pain': 0.8, 'hand_or_finger_swelling': 1.0, 'abnormal_appearing_skin': 0.46}
}
disease_map["CSV_0365"] = {
    "name": "Ingrown Toe Nail",
    "primary_symptoms": ['neck_swelling'],
    "secondary_symptoms": ['abnormal_appearing_skin', 'skin_growth', 'foot_or_toe_pain', 'foot_or_toe_swelling', 'skin_on_leg_or_foot_looks_infected', 'swollen_eye', 'irregular_appearing_nails', 'skin_dryness,_peeling,_scaliness,_or_roughness', 'skin_on_arm_or_hand_looks_infected'],
    "rare_symptoms": [],
    "symptom_weights": {'abnormal_appearing_skin': 0.49, 'skin_growth': 0.48, 'neck_swelling': 0.76, 'foot_or_toe_pain': 0.48, 'foot_or_toe_swelling': 0.51, 'skin_on_leg_or_foot_looks_infected': 0.5, 'swollen_eye': 0.51, 'irregular_appearing_nails': 0.52, 'skin_dryness,_peeling,_scaliness,_or_roughness': 0.49, 'skin_on_arm_or_hand_looks_infected': 0.48}
}
disease_map["CSV_0366"] = {
    "name": "Inguinal Hernia",
    "primary_symptoms": [],
    "secondary_symptoms": ['groin_mass', 'symptoms_of_the_scrotum_and_testes', 'swelling_of_scrotum', 'pain_in_testicles', 'mass_in_scrotum', 'sharp_abdominal_pain', 'lower_abdominal_pain', 'ache_all_over', 'swollen_abdomen', 'groin_pain'],
    "rare_symptoms": [],
    "symptom_weights": {'groin_mass': 0.55, 'symptoms_of_the_scrotum_and_testes': 0.65, 'swelling_of_scrotum': 0.52, 'pain_in_testicles': 0.52, 'mass_in_scrotum': 0.51, 'sharp_abdominal_pain': 0.53, 'lower_abdominal_pain': 0.58, 'ache_all_over': 0.55, 'swollen_abdomen': 0.54, 'groin_pain': 0.56}
}
disease_map["CSV_0367"] = {
    "name": "Injury Of The Ankle",
    "primary_symptoms": ['wrist_swelling'],
    "secondary_symptoms": ['leg_pain', 'foot_or_toe_pain', 'ankle_pain', 'foot_or_toe_swelling', 'joint_pain', 'ankle_swelling', 'foot_or_toe_weakness'],
    "rare_symptoms": [],
    "symptom_weights": {'leg_pain': 0.51, 'wrist_swelling': 0.8, 'foot_or_toe_pain': 0.46, 'ankle_pain': 0.55, 'foot_or_toe_swelling': 0.54, 'joint_pain': 0.54, 'ankle_swelling': 0.52, 'foot_or_toe_weakness': 0.54}
}
disease_map["CSV_0368"] = {
    "name": "Injury To Internal Organ",
    "primary_symptoms": ['sharp_chest_pain', 'retention_of_urine', 'frequent_urination'],
    "secondary_symptoms": ['sharp_abdominal_pain', 'back_pain', 'side_pain'],
    "rare_symptoms": [],
    "symptom_weights": {'sharp_chest_pain': 0.79, 'retention_of_urine': 0.76, 'sharp_abdominal_pain': 0.56, 'frequent_urination': 0.85, 'back_pain': 0.68, 'side_pain': 0.62}
}
disease_map["CSV_0369"] = {
    "name": "Injury To The Abdomen",
    "primary_symptoms": ['leg_pain', 'blood_in_urine', 'back_pain'],
    "secondary_symptoms": ['sharp_chest_pain', 'sharp_abdominal_pain'],
    "rare_symptoms": [],
    "symptom_weights": {'sharp_chest_pain': 0.56, 'leg_pain': 0.95, 'sharp_abdominal_pain': 0.59, 'blood_in_urine': 0.73, 'back_pain': 0.89}
}
disease_map["CSV_0370"] = {
    "name": "Injury To The Arm",
    "primary_symptoms": [],
    "secondary_symptoms": ['hand_or_finger_pain', 'wrist_pain', 'hand_or_finger_swelling', 'arm_pain', 'wrist_swelling', 'arm_stiffness_or_tightness', 'arm_swelling', 'bones_are_painful', 'elbow_pain', 'loss_of_sensation', 'joint_pain', 'elbow_swelling'],
    "rare_symptoms": [],
    "symptom_weights": {'hand_or_finger_pain': 0.49, 'wrist_pain': 0.5, 'hand_or_finger_swelling': 0.49, 'arm_pain': 0.5, 'wrist_swelling': 0.52, 'arm_stiffness_or_tightness': 0.5, 'arm_swelling': 0.5, 'bones_are_painful': 0.5, 'elbow_pain': 0.5, 'loss_of_sensation': 0.51, 'joint_pain': 0.5, 'elbow_swelling': 0.51}
}
disease_map["CSV_0371"] = {
    "name": "Injury To The Face",
    "primary_symptoms": ['diminished_hearing'],
    "secondary_symptoms": ['headache', 'facial_pain', 'neck_pain', 'ear_pain', 'neck_stiffness_or_tightness', 'nosebleed', 'bleeding_from_ear', 'mouth_pain'],
    "rare_symptoms": [],
    "symptom_weights": {'diminished_hearing': 0.78, 'headache': 0.48, 'facial_pain': 0.45, 'neck_pain': 0.55, 'ear_pain': 0.51, 'neck_stiffness_or_tightness': 0.69, 'nosebleed': 0.54, 'bleeding_from_ear': 0.49, 'mouth_pain': 0.51}
}
disease_map["CSV_0372"] = {
    "name": "Injury To The Finger",
    "primary_symptoms": ['swelling_of_scrotum'],
    "secondary_symptoms": ['hand_or_finger_pain', 'hand_or_finger_swelling'],
    "rare_symptoms": ['hand_or_finger_stiffness_or_tightness'],
    "symptom_weights": {'swelling_of_scrotum': 0.86, 'hand_or_finger_pain': 0.57, 'hand_or_finger_swelling': 0.57, 'hand_or_finger_stiffness_or_tightness': 0.29}
}
disease_map["CSV_0373"] = {
    "name": "Injury To The Hand",
    "primary_symptoms": ['wrist_swelling'],
    "secondary_symptoms": ['hand_or_finger_pain', 'wrist_pain', 'hand_or_finger_swelling', 'hand_or_finger_stiffness_or_tightness', 'skin_growth', 'joint_pain'],
    "rare_symptoms": [],
    "symptom_weights": {'hand_or_finger_pain': 0.58, 'wrist_pain': 0.55, 'hand_or_finger_swelling': 0.59, 'wrist_swelling': 0.89, 'hand_or_finger_stiffness_or_tightness': 0.52, 'skin_growth': 0.48, 'joint_pain': 0.57}
}
disease_map["CSV_0374"] = {
    "name": "Injury To The Hip",
    "primary_symptoms": ['hand_or_finger_swelling', 'neck_pain'],
    "secondary_symptoms": ['leg_pain', 'hip_pain'],
    "rare_symptoms": [],
    "symptom_weights": {'leg_pain': 0.5, 'hip_pain': 0.44, 'hand_or_finger_swelling': 0.94, 'neck_pain': 0.75}
}
disease_map["CSV_0375"] = {
    "name": "Injury To The Knee",
    "primary_symptoms": ['foot_or_toe_swelling'],
    "secondary_symptoms": ['leg_pain', 'knee_pain', 'knee_weakness'],
    "rare_symptoms": ['problems_with_movement'],
    "symptom_weights": {'leg_pain': 0.7, 'knee_pain': 0.57, 'knee_weakness': 0.68, 'problems_with_movement': 0.36, 'foot_or_toe_swelling': 0.72}
}
disease_map["CSV_0376"] = {
    "name": "Injury To The Leg",
    "primary_symptoms": [],
    "secondary_symptoms": ['leg_pain', 'knee_pain', 'foot_or_toe_pain', 'ankle_pain', 'knee_swelling', 'problems_with_movement', 'knee_stiffness_or_tightness', 'leg_swelling', 'foot_or_toe_swelling', 'infant_feeding_problem', 'irregular_appearing_nails', 'ankle_swelling'],
    "rare_symptoms": [],
    "symptom_weights": {'leg_pain': 0.5, 'knee_pain': 0.51, 'foot_or_toe_pain': 0.51, 'ankle_pain': 0.5, 'knee_swelling': 0.52, 'problems_with_movement': 0.52, 'knee_stiffness_or_tightness': 0.49, 'leg_swelling': 0.52, 'foot_or_toe_swelling': 0.51, 'infant_feeding_problem': 0.49, 'irregular_appearing_nails': 0.5, 'ankle_swelling': 0.51}
}
disease_map["CSV_0377"] = {
    "name": "Injury To The Shoulder",
    "primary_symptoms": [],
    "secondary_symptoms": ['arm_pain', 'arm_stiffness_or_tightness', 'back_pain', 'neck_pain', 'bones_are_painful', 'elbow_pain', 'shoulder_pain', 'shoulder_stiffness_or_tightness', 'muscle_cramps,_contractures,_or_spasms'],
    "rare_symptoms": [],
    "symptom_weights": {'arm_pain': 0.47, 'arm_stiffness_or_tightness': 0.53, 'back_pain': 0.48, 'neck_pain': 0.48, 'bones_are_painful': 0.68, 'elbow_pain': 0.51, 'shoulder_pain': 0.51, 'shoulder_stiffness_or_tightness': 0.68, 'muscle_cramps,_contractures,_or_spasms': 0.67}
}
disease_map["CSV_0378"] = {
    "name": "Injury To The Spinal Cord",
    "primary_symptoms": ['retention_of_urine', 'headache'],
    "secondary_symptoms": ['back_pain', 'neck_pain'],
    "rare_symptoms": [],
    "symptom_weights": {'retention_of_urine': 0.97, 'headache': 0.79, 'back_pain': 0.69, 'neck_pain': 0.59}
}
disease_map["CSV_0379"] = {
    "name": "Injury To The Trunk",
    "primary_symptoms": [],
    "secondary_symptoms": ['sharp_chest_pain', 'symptoms_of_the_scrotum_and_testes', 'headache', 'wrist_pain', 'back_pain', 'neck_pain', 'low_back_pain', 'bones_are_painful', 'shoulder_pain', 'lower_body_pain', 'rib_pain'],
    "rare_symptoms": [],
    "symptom_weights": {'sharp_chest_pain': 0.49, 'symptoms_of_the_scrotum_and_testes': 0.68, 'headache': 0.49, 'wrist_pain': 0.49, 'back_pain': 0.52, 'neck_pain': 0.54, 'low_back_pain': 0.51, 'bones_are_painful': 0.48, 'shoulder_pain': 0.52, 'lower_body_pain': 0.51, 'rib_pain': 0.51}
}
disease_map["CSV_0380"] = {
    "name": "Insect Bite",
    "primary_symptoms": [],
    "secondary_symptoms": ['skin_swelling', 'hand_or_finger_swelling', 'lip_swelling', 'abnormal_appearing_skin', 'skin_lesion', 'peripheral_edema', 'leg_swelling', 'fluid_retention', 'itching_of_skin', 'skin_rash'],
    "rare_symptoms": [],
    "symptom_weights": {'skin_swelling': 0.49, 'hand_or_finger_swelling': 0.68, 'lip_swelling': 0.48, 'abnormal_appearing_skin': 0.52, 'skin_lesion': 0.51, 'peripheral_edema': 0.52, 'leg_swelling': 0.69, 'fluid_retention': 0.49, 'itching_of_skin': 0.51, 'skin_rash': 0.54}
}
disease_map["CSV_0381"] = {
    "name": "Insulin Overdose",
    "primary_symptoms": ['depressive_or_psychotic_symptoms', 'emotional_symptoms'],
    "secondary_symptoms": [],
    "rare_symptoms": [],
    "symptom_weights": {'depressive_or_psychotic_symptoms': 1.0, 'emotional_symptoms': 1.0}
}
disease_map["CSV_0382"] = {
    "name": "Interstitial Lung Disease",
    "primary_symptoms": [],
    "secondary_symptoms": ['shortness_of_breath', 'sore_throat', 'cough', 'nasal_congestion', 'headache', 'wheezing', 'fever', 'sleepiness', 'abnormal_breathing_sounds'],
    "rare_symptoms": [],
    "symptom_weights": {'shortness_of_breath': 0.64, 'sore_throat': 0.66, 'cough': 0.53, 'nasal_congestion': 0.52, 'headache': 0.51, 'wheezing': 0.64, 'fever': 0.52, 'sleepiness': 0.5, 'abnormal_breathing_sounds': 0.48}
}
disease_map["CSV_0383"] = {
    "name": "Intertrigo (Skin Condition)",
    "primary_symptoms": ['skin_lesion', 'acne_or_pimples'],
    "secondary_symptoms": ['skin_swelling', 'abnormal_appearing_skin', 'skin_dryness,_peeling,_scaliness,_or_roughness', 'skin_rash'],
    "rare_symptoms": [],
    "symptom_weights": {'skin_swelling': 0.56, 'abnormal_appearing_skin': 0.55, 'skin_lesion': 0.79, 'acne_or_pimples': 0.85, 'skin_dryness,_peeling,_scaliness,_or_roughness': 0.5, 'skin_rash': 0.59}
}
disease_map["CSV_0384"] = {
    "name": "Intestinal Cancer",
    "primary_symptoms": ['throat_feels_tight', 'sharp_abdominal_pain', 'neck_mass', 'foot_or_toe_swelling'],
    "secondary_symptoms": ['diarrhea'],
    "rare_symptoms": [],
    "symptom_weights": {'throat_feels_tight': 0.94, 'sharp_abdominal_pain': 0.71, 'diarrhea': 0.51, 'neck_mass': 0.73, 'foot_or_toe_swelling': 0.76}
}
disease_map["CSV_0385"] = {
    "name": "Intestinal Disease",
    "primary_symptoms": ['fainting'],
    "secondary_symptoms": ['sharp_chest_pain', 'sharp_abdominal_pain', 'vomiting', 'nausea', 'diarrhea', 'regurgitation', 'burning_abdominal_pain', 'regurgitation.1'],
    "rare_symptoms": [],
    "symptom_weights": {'sharp_chest_pain': 0.5, 'fainting': 0.7, 'sharp_abdominal_pain': 0.49, 'vomiting': 0.52, 'nausea': 0.66, 'diarrhea': 0.49, 'regurgitation': 0.67, 'burning_abdominal_pain': 0.68, 'regurgitation.1': 0.67}
}
disease_map["CSV_0386"] = {
    "name": "Intestinal Malabsorption",
    "primary_symptoms": ['cough', 'flatulence'],
    "secondary_symptoms": ['nasal_congestion', 'sharp_abdominal_pain', 'vomiting', 'diarrhea', 'allergic_reaction'],
    "rare_symptoms": [],
    "symptom_weights": {'cough': 0.84, 'nasal_congestion': 0.53, 'flatulence': 0.84, 'sharp_abdominal_pain': 0.5, 'vomiting': 0.58, 'diarrhea': 0.57, 'allergic_reaction': 0.51}
}
disease_map["CSV_0387"] = {
    "name": "Intestinal Obstruction",
    "primary_symptoms": ['vaginal_itching'],
    "secondary_symptoms": ['retention_of_urine', 'sharp_abdominal_pain', 'vomiting', 'nausea', 'pain_of_the_anus', 'burning_abdominal_pain', 'stomach_bloating', 'constipation'],
    "rare_symptoms": [],
    "symptom_weights": {'retention_of_urine': 0.51, 'sharp_abdominal_pain': 0.52, 'vomiting': 0.51, 'nausea': 0.66, 'vaginal_itching': 0.77, 'pain_of_the_anus': 0.5, 'burning_abdominal_pain': 0.5, 'stomach_bloating': 0.53, 'constipation': 0.5}
}
disease_map["CSV_0388"] = {
    "name": "Intracerebral Hemorrhage",
    "primary_symptoms": ['diminished_vision'],
    "secondary_symptoms": ['depressive_or_psychotic_symptoms', 'dizziness', 'vomiting', 'headache', 'nausea', 'weakness', 'blindness', 'focal_weakness', 'seizures'],
    "rare_symptoms": [],
    "symptom_weights": {'depressive_or_psychotic_symptoms': 0.48, 'dizziness': 0.49, 'vomiting': 0.47, 'headache': 0.5, 'nausea': 0.5, 'diminished_vision': 0.78, 'weakness': 0.5, 'blindness': 0.49, 'focal_weakness': 0.52, 'seizures': 0.5}
}
disease_map["CSV_0389"] = {
    "name": "Intracranial Abscess",
    "primary_symptoms": ['depressive_or_psychotic_symptoms', 'headache'],
    "secondary_symptoms": ['seizures'],
    "rare_symptoms": [],
    "symptom_weights": {'depressive_or_psychotic_symptoms': 0.92, 'headache': 1.0, 'seizures': 0.67}
}
disease_map["CSV_0390"] = {
    "name": "Intracranial Hemorrhage",
    "primary_symptoms": ['depressive_or_psychotic_symptoms', 'abnormal_involuntary_movements', 'vomiting'],
    "secondary_symptoms": ['dizziness', 'difficulty_speaking', 'headache', 'diminished_vision', 'seizures'],
    "rare_symptoms": [],
    "symptom_weights": {'depressive_or_psychotic_symptoms': 0.79, 'dizziness': 0.52, 'abnormal_involuntary_movements': 0.71, 'difficulty_speaking': 0.53, 'vomiting': 0.71, 'headache': 0.57, 'diminished_vision': 0.48, 'seizures': 0.51}
}
disease_map["CSV_0391"] = {
    "name": "Intussusception",
    "primary_symptoms": ['blood_in_stool', 'emotional_symptoms', 'sharp_abdominal_pain'],
    "secondary_symptoms": [],
    "rare_symptoms": [],
    "symptom_weights": {'blood_in_stool': 1.0, 'emotional_symptoms': 0.75, 'sharp_abdominal_pain': 0.75}
}
disease_map["CSV_0392"] = {
    "name": "Iridocyclitis",
    "primary_symptoms": [],
    "secondary_symptoms": ['headache', 'diminished_vision', 'symptoms_of_eye', 'pain_in_eye', 'foreign_body_sensation_in_eye', 'eye_redness', 'lacrimation', 'eye_burns_or_stings', 'cloudy_eye'],
    "rare_symptoms": [],
    "symptom_weights": {'headache': 0.69, 'diminished_vision': 0.49, 'symptoms_of_eye': 0.49, 'pain_in_eye': 0.55, 'foreign_body_sensation_in_eye': 0.68, 'eye_redness': 0.53, 'lacrimation': 0.67, 'eye_burns_or_stings': 0.5, 'cloudy_eye': 0.48}
}
disease_map["CSV_0393"] = {
    "name": "Iron Deficiency Anemia",
    "primary_symptoms": [],
    "secondary_symptoms": ['dizziness', 'blood_in_stool', 'intermenstrual_bleeding', 'regurgitation', 'weight_gain', 'heartburn', 'weakness', 'fatigue', 'regurgitation.1', 'rectal_bleeding', 'heavy_menstrual_flow'],
    "rare_symptoms": [],
    "symptom_weights": {'dizziness': 0.49, 'blood_in_stool': 0.5, 'intermenstrual_bleeding': 0.66, 'regurgitation': 0.49, 'weight_gain': 0.49, 'heartburn': 0.66, 'weakness': 0.52, 'fatigue': 0.51, 'regurgitation.1': 0.49, 'rectal_bleeding': 0.52, 'heavy_menstrual_flow': 0.52}
}
disease_map["CSV_0394"] = {
    "name": "Irritable Bowel Syndrome",
    "primary_symptoms": [],
    "secondary_symptoms": ['anxiety_and_nervousness', 'insomnia', 'flatulence', 'sharp_abdominal_pain', 'nausea', 'diarrhea', 'lower_abdominal_pain', 'burning_abdominal_pain', 'upper_abdominal_pain'],
    "rare_symptoms": [],
    "symptom_weights": {'anxiety_and_nervousness': 0.47, 'insomnia': 0.67, 'flatulence': 0.68, 'sharp_abdominal_pain': 0.5, 'nausea': 0.66, 'diarrhea': 0.48, 'lower_abdominal_pain': 0.51, 'burning_abdominal_pain': 0.48, 'upper_abdominal_pain': 0.5}
}
disease_map["CSV_0395"] = {
    "name": "Ischemia Of The Bowel",
    "primary_symptoms": [],
    "secondary_symptoms": ['retention_of_urine', 'blood_in_stool', 'sharp_abdominal_pain', 'vomiting', 'nausea', 'burning_abdominal_pain', 'constipation'],
    "rare_symptoms": [],
    "symptom_weights": {'retention_of_urine': 0.67, 'blood_in_stool': 0.69, 'sharp_abdominal_pain': 0.52, 'vomiting': 0.64, 'nausea': 0.7, 'burning_abdominal_pain': 0.67, 'constipation': 0.49}
}
disease_map["CSV_0396"] = {
    "name": "Ischemic Heart Disease",
    "primary_symptoms": [],
    "secondary_symptoms": ['shortness_of_breath', 'sharp_chest_pain', 'dizziness', 'chest_tightness', 'palpitations', 'throat_feels_tight', 'peripheral_edema', 'muscle_pain', 'difficulty_breathing', 'fatigue', 'lymphedema'],
    "rare_symptoms": [],
    "symptom_weights": {'shortness_of_breath': 0.49, 'sharp_chest_pain': 0.54, 'dizziness': 0.51, 'chest_tightness': 0.52, 'palpitations': 0.51, 'throat_feels_tight': 0.5, 'peripheral_edema': 0.53, 'muscle_pain': 0.64, 'difficulty_breathing': 0.51, 'fatigue': 0.52, 'lymphedema': 0.5}
}
disease_map["CSV_0397"] = {
    "name": "Itching Of Unknown Cause",
    "primary_symptoms": [],
    "secondary_symptoms": ['vaginal_itching', 'abnormal_appearing_skin', 'problems_during_pregnancy', 'allergic_reaction', 'fluid_retention', 'itching_of_skin', 'skin_dryness,_peeling,_scaliness,_or_roughness', 'itchy_scalp', 'skin_rash'],
    "rare_symptoms": [],
    "symptom_weights": {'vaginal_itching': 0.66, 'abnormal_appearing_skin': 0.5, 'problems_during_pregnancy': 0.68, 'allergic_reaction': 0.54, 'fluid_retention': 0.67, 'itching_of_skin': 0.5, 'skin_dryness,_peeling,_scaliness,_or_roughness': 0.48, 'itchy_scalp': 0.52, 'skin_rash': 0.48}
}
disease_map["CSV_0398"] = {
    "name": "Jaw Disorder",
    "primary_symptoms": ['difficulty_in_swallowing'],
    "secondary_symptoms": ['headache', 'toothache', 'facial_pain', 'peripheral_edema', 'neck_mass', 'jaw_swelling', 'mouth_pain'],
    "rare_symptoms": [],
    "symptom_weights": {'difficulty_in_swallowing': 0.76, 'headache': 0.54, 'toothache': 0.51, 'facial_pain': 0.49, 'peripheral_edema': 0.51, 'neck_mass': 0.68, 'jaw_swelling': 0.66, 'mouth_pain': 0.5}
}
disease_map["CSV_0399"] = {
    "name": "Joint Effusion",
    "primary_symptoms": ['wrist_pain'],
    "secondary_symptoms": ['wrist_swelling', 'knee_pain', 'ankle_pain', 'elbow_pain', 'knee_swelling', 'problems_with_movement', 'knee_stiffness_or_tightness', 'ankle_swelling'],
    "rare_symptoms": [],
    "symptom_weights": {'wrist_pain': 0.76, 'wrist_swelling': 0.51, 'knee_pain': 0.51, 'ankle_pain': 0.53, 'elbow_pain': 0.48, 'knee_swelling': 0.54, 'problems_with_movement': 0.51, 'knee_stiffness_or_tightness': 0.7, 'ankle_swelling': 0.54}
}
disease_map["CSV_0400"] = {
    "name": "Juvenile Rheumatoid Arthritis",
    "primary_symptoms": ['hand_or_finger_pain', 'wrist_swelling'],
    "secondary_symptoms": ['back_pain', 'knee_pain', 'joint_pain'],
    "rare_symptoms": [],
    "symptom_weights": {'hand_or_finger_pain': 0.91, 'wrist_swelling': 0.94, 'back_pain': 0.61, 'knee_pain': 0.61, 'joint_pain': 0.67}
}
disease_map["CSV_0401"] = {
    "name": "Kaposi Sarcoma",
    "primary_symptoms": ['depression', 'elbow_weakness'],
    "secondary_symptoms": [],
    "rare_symptoms": [],
    "symptom_weights": {'depression': 1.0, 'elbow_weakness': 1.0}
}
disease_map["CSV_0402"] = {
    "name": "Kidney Cancer",
    "primary_symptoms": ['groin_mass', 'involuntary_urination'],
    "secondary_symptoms": ['retention_of_urine', 'blood_in_urine', 'kidney_mass'],
    "rare_symptoms": [],
    "symptom_weights": {'retention_of_urine': 0.51, 'groin_mass': 0.79, 'involuntary_urination': 0.79, 'blood_in_urine': 0.61, 'kidney_mass': 0.54}
}
disease_map["CSV_0403"] = {
    "name": "Kidney Disease Due To Longstanding Hypertension",
    "primary_symptoms": ['feeling_cold'],
    "secondary_symptoms": ['shortness_of_breath', 'difficulty_speaking', 'symptoms_of_the_kidneys'],
    "rare_symptoms": [],
    "symptom_weights": {'shortness_of_breath': 0.65, 'difficulty_speaking': 0.41, 'feeling_cold': 0.94, 'symptoms_of_the_kidneys': 0.65}
}
disease_map["CSV_0404"] = {
    "name": "Kidney Failure",
    "primary_symptoms": ['swollen_abdomen'],
    "secondary_symptoms": ['shortness_of_breath', 'sharp_chest_pain', 'vomiting', 'nausea', 'arm_swelling', 'leg_swelling', 'symptoms_of_the_kidneys'],
    "rare_symptoms": [],
    "symptom_weights": {'shortness_of_breath': 0.5, 'sharp_chest_pain': 0.69, 'vomiting': 0.51, 'nausea': 0.54, 'arm_swelling': 0.51, 'leg_swelling': 0.49, 'swollen_abdomen': 0.77, 'symptoms_of_the_kidneys': 0.5}
}
disease_map["CSV_0405"] = {
    "name": "Kidney Stone",
    "primary_symptoms": ['vomiting'],
    "secondary_symptoms": ['retention_of_urine', 'suprapubic_pain', 'sharp_abdominal_pain', 'painful_urination', 'frequent_urination', 'lower_abdominal_pain', 'blood_in_urine', 'back_pain', 'low_back_pain', 'side_pain'],
    "rare_symptoms": [],
    "symptom_weights": {'retention_of_urine': 0.48, 'suprapubic_pain': 0.5, 'sharp_abdominal_pain': 0.49, 'vomiting': 0.71, 'painful_urination': 0.51, 'frequent_urination': 0.51, 'lower_abdominal_pain': 0.49, 'blood_in_urine': 0.48, 'back_pain': 0.53, 'low_back_pain': 0.51, 'side_pain': 0.52}
}
disease_map["CSV_0406"] = {
    "name": "Knee Ligament Or Meniscus Tear",
    "primary_symptoms": ['knee_lump_or_mass'],
    "secondary_symptoms": ['knee_pain', 'knee_weakness', 'knee_swelling', 'knee_stiffness_or_tightness', 'leg_stiffness_or_tightness', 'leg_weakness'],
    "rare_symptoms": [],
    "symptom_weights": {'knee_pain': 0.51, 'knee_weakness': 0.56, 'knee_swelling': 0.53, 'knee_lump_or_mass': 0.87, 'knee_stiffness_or_tightness': 0.57, 'leg_stiffness_or_tightness': 0.46, 'leg_weakness': 0.57}
}
disease_map["CSV_0407"] = {
    "name": "Labyrinthitis",
    "primary_symptoms": [],
    "secondary_symptoms": ['dizziness', 'diminished_hearing', 'vomiting', 'headache', 'nausea', 'ear_pain', 'plugged_feeling_in_ear', 'spots_or_clouds_in_vision', 'loss_of_sensation', 'sweating'],
    "rare_symptoms": [],
    "symptom_weights": {'dizziness': 0.5, 'diminished_hearing': 0.67, 'vomiting': 0.54, 'headache': 0.52, 'nausea': 0.5, 'ear_pain': 0.7, 'plugged_feeling_in_ear': 0.49, 'spots_or_clouds_in_vision': 0.5, 'loss_of_sensation': 0.53, 'sweating': 0.52}
}
disease_map["CSV_0408"] = {
    "name": "Lactose Intolerance",
    "primary_symptoms": ['nasal_congestion', 'flatulence', 'impotence'],
    "secondary_symptoms": ['shortness_of_breath', 'diarrhea', 'burning_abdominal_pain'],
    "rare_symptoms": [],
    "symptom_weights": {'shortness_of_breath': 0.55, 'nasal_congestion': 0.85, 'flatulence': 0.74, 'diarrhea': 0.51, 'impotence': 0.74, 'burning_abdominal_pain': 0.57}
}
disease_map["CSV_0409"] = {
    "name": "Laryngitis",
    "primary_symptoms": [],
    "secondary_symptoms": ['hoarse_voice', 'sore_throat', 'difficulty_speaking', 'cough', 'nasal_congestion', 'throat_feels_tight', 'difficulty_in_swallowing', 'ear_pain', 'fever', 'coryza'],
    "rare_symptoms": [],
    "symptom_weights": {'hoarse_voice': 0.48, 'sore_throat': 0.52, 'difficulty_speaking': 0.66, 'cough': 0.51, 'nasal_congestion': 0.51, 'throat_feels_tight': 0.69, 'difficulty_in_swallowing': 0.5, 'ear_pain': 0.51, 'fever': 0.51, 'coryza': 0.5}
}
disease_map["CSV_0410"] = {
    "name": "Lateral Epicondylitis (Tennis Elbow)",
    "primary_symptoms": ['joint_pain'],
    "secondary_symptoms": ['hand_or_finger_pain', 'wrist_pain', 'arm_pain', 'hand_or_finger_stiffness_or_tightness', 'elbow_pain', 'loss_of_sensation', 'shoulder_pain'],
    "rare_symptoms": [],
    "symptom_weights": {'hand_or_finger_pain': 0.67, 'wrist_pain': 0.52, 'arm_pain': 0.54, 'hand_or_finger_stiffness_or_tightness': 0.69, 'elbow_pain': 0.53, 'loss_of_sensation': 0.52, 'shoulder_pain': 0.47, 'joint_pain': 0.74}
}
disease_map["CSV_0411"] = {
    "name": "Leukemia",
    "primary_symptoms": ['muscle_stiffness_or_tightness'],
    "secondary_symptoms": ['fever', 'fatigue', 'mouth_pain'],
    "rare_symptoms": [],
    "symptom_weights": {'fever': 0.4, 'muscle_stiffness_or_tightness': 1.0, 'fatigue': 0.5, 'mouth_pain': 0.6}
}
disease_map["CSV_0412"] = {
    "name": "Lewy Body Dementia",
    "primary_symptoms": ['depressive_or_psychotic_symptoms', 'hostile_behavior'],
    "secondary_symptoms": ['abnormal_involuntary_movements', 'disturbance_of_memory', 'delusions_or_hallucinations'],
    "rare_symptoms": [],
    "symptom_weights": {'depressive_or_psychotic_symptoms': 0.73, 'abnormal_involuntary_movements': 0.63, 'hostile_behavior': 0.84, 'disturbance_of_memory': 0.53, 'delusions_or_hallucinations': 0.48}
}
disease_map["CSV_0413"] = {
    "name": "Lice",
    "primary_symptoms": ['nasal_congestion', 'itchy_scalp', 'leg_lump_or_mass'],
    "secondary_symptoms": ['cough', 'itching_of_skin'],
    "rare_symptoms": [],
    "symptom_weights": {'cough': 0.58, 'nasal_congestion': 0.94, 'itching_of_skin': 0.58, 'itchy_scalp': 0.82, 'leg_lump_or_mass': 0.85}
}
disease_map["CSV_0414"] = {
    "name": "Lichen Planus",
    "primary_symptoms": ['difficulty_speaking', 'abnormal_appearing_skin', 'skin_growth'],
    "secondary_symptoms": [],
    "rare_symptoms": [],
    "symptom_weights": {'difficulty_speaking': 1.0, 'abnormal_appearing_skin': 1.0, 'skin_growth': 1.0}
}
disease_map["CSV_0415"] = {
    "name": "Lichen Simplex",
    "primary_symptoms": ['difficulty_speaking', 'vaginal_itching'],
    "secondary_symptoms": ['skin_lesion', 'itching_of_skin', 'skin_rash'],
    "rare_symptoms": [],
    "symptom_weights": {'difficulty_speaking': 0.81, 'vaginal_itching': 0.93, 'skin_lesion': 0.56, 'itching_of_skin': 0.61, 'skin_rash': 0.54}
}
disease_map["CSV_0416"] = {
    "name": "Lipoma",
    "primary_symptoms": [],
    "secondary_symptoms": ['skin_swelling', 'groin_mass', 'abnormal_appearing_skin', 'skin_lesion', 'skin_growth', 'neck_mass', 'bones_are_painful', 'back_mass_or_lump', 'shoulder_lump_or_mass', 'arm_lump_or_mass'],
    "rare_symptoms": [],
    "symptom_weights": {'skin_swelling': 0.47, 'groin_mass': 0.66, 'abnormal_appearing_skin': 0.52, 'skin_lesion': 0.5, 'skin_growth': 0.5, 'neck_mass': 0.51, 'bones_are_painful': 0.68, 'back_mass_or_lump': 0.49, 'shoulder_lump_or_mass': 0.51, 'arm_lump_or_mass': 0.52}
}
disease_map["CSV_0417"] = {
    "name": "Liver Cancer",
    "primary_symptoms": ['groin_mass'],
    "secondary_symptoms": ['sharp_abdominal_pain', 'decreased_appetite', 'upper_abdominal_pain', 'stomach_bloating'],
    "rare_symptoms": [],
    "symptom_weights": {'groin_mass': 0.94, 'sharp_abdominal_pain': 0.57, 'decreased_appetite': 0.65, 'upper_abdominal_pain': 0.49, 'stomach_bloating': 0.57}
}
disease_map["CSV_0418"] = {
    "name": "Liver Disease",
    "primary_symptoms": [],
    "secondary_symptoms": ['shortness_of_breath', 'blood_in_stool', 'jaundice', 'sharp_abdominal_pain', 'nausea', 'diarrhea', 'peripheral_edema', 'heartburn', 'weakness', 'side_pain', 'upper_abdominal_pain', 'unusual_color_or_odor_to_urine'],
    "rare_symptoms": [],
    "symptom_weights": {'shortness_of_breath': 0.48, 'blood_in_stool': 0.51, 'jaundice': 0.51, 'sharp_abdominal_pain': 0.51, 'nausea': 0.52, 'diarrhea': 0.5, 'peripheral_edema': 0.51, 'heartburn': 0.5, 'weakness': 0.5, 'side_pain': 0.5, 'upper_abdominal_pain': 0.52, 'unusual_color_or_odor_to_urine': 0.5}
}
disease_map["CSV_0419"] = {
    "name": "Lumbago",
    "primary_symptoms": ['hip_pain', 'side_pain'],
    "secondary_symptoms": ['leg_pain', 'back_pain', 'low_back_pain', 'muscle_pain', 'low_back_cramps_or_spasms'],
    "rare_symptoms": [],
    "symptom_weights": {'leg_pain': 0.56, 'hip_pain': 0.76, 'back_pain': 0.6, 'low_back_pain': 0.6, 'muscle_pain': 0.68, 'side_pain': 0.74, 'low_back_cramps_or_spasms': 0.66}
}
disease_map["CSV_0420"] = {
    "name": "Lung Cancer",
    "primary_symptoms": [],
    "secondary_symptoms": ['shortness_of_breath', 'cough', 'smoking_problems', 'decreased_appetite', 'fatigue', 'hemoptysis', 'leg_weakness'],
    "rare_symptoms": [],
    "symptom_weights": {'shortness_of_breath': 0.53, 'cough': 0.57, 'smoking_problems': 0.51, 'decreased_appetite': 0.51, 'fatigue': 0.59, 'hemoptysis': 0.67, 'leg_weakness': 0.51}
}
disease_map["CSV_0421"] = {
    "name": "Lung Contusion",
    "primary_symptoms": ['shortness_of_breath', 'sharp_chest_pain', 'ache_all_over'],
    "secondary_symptoms": ['back_pain'],
    "rare_symptoms": [],
    "symptom_weights": {'shortness_of_breath': 1.0, 'sharp_chest_pain': 0.8, 'back_pain': 0.6, 'ache_all_over': 0.73}
}
disease_map["CSV_0422"] = {
    "name": "Lyme Disease",
    "primary_symptoms": ['hip_pain'],
    "secondary_symptoms": ['depressive_or_psychotic_symptoms', 'headache', 'abnormal_appearing_skin', 'symptoms_of_the_face', 'fever', 'fatigue'],
    "rare_symptoms": [],
    "symptom_weights": {'depressive_or_psychotic_symptoms': 0.69, 'hip_pain': 0.83, 'headache': 0.68, 'abnormal_appearing_skin': 0.52, 'symptoms_of_the_face': 0.5, 'fever': 0.55, 'fatigue': 0.51}
}
disease_map["CSV_0423"] = {
    "name": "Lymphadenitis",
    "primary_symptoms": ['cough'],
    "secondary_symptoms": ['sore_throat', 'skin_swelling', 'sharp_abdominal_pain', 'neck_pain', 'neck_mass', 'ear_pain', 'neck_swelling', 'fever'],
    "rare_symptoms": [],
    "symptom_weights": {'sore_throat': 0.5, 'cough': 0.77, 'skin_swelling': 0.49, 'sharp_abdominal_pain': 0.65, 'neck_pain': 0.51, 'neck_mass': 0.5, 'ear_pain': 0.5, 'neck_swelling': 0.54, 'fever': 0.53}
}
disease_map["CSV_0424"] = {
    "name": "Lymphangitis",
    "primary_symptoms": ['arm_pain', 'neck_swelling'],
    "secondary_symptoms": [],
    "rare_symptoms": [],
    "symptom_weights": {'arm_pain': 1.0, 'neck_swelling': 1.0}
}
disease_map["CSV_0425"] = {
    "name": "Lymphedema",
    "primary_symptoms": [],
    "secondary_symptoms": ['throat_swelling', 'leg_pain', 'abnormal_appearing_skin', 'skin_lesion', 'peripheral_edema', 'leg_swelling', 'foot_or_toe_swelling', 'lymphedema', 'fluid_retention'],
    "rare_symptoms": [],
    "symptom_weights": {'throat_swelling': 0.67, 'leg_pain': 0.5, 'abnormal_appearing_skin': 0.52, 'skin_lesion': 0.53, 'peripheral_edema': 0.5, 'leg_swelling': 0.51, 'foot_or_toe_swelling': 0.67, 'lymphedema': 0.65, 'fluid_retention': 0.53}
}
disease_map["CSV_0426"] = {
    "name": "Lymphogranuloma Venereum",
    "primary_symptoms": ['ear_pain', 'knee_lump_or_mass'],
    "secondary_symptoms": ['sore_throat'],
    "rare_symptoms": [],
    "symptom_weights": {'sore_throat': 0.55, 'ear_pain': 0.95, 'knee_lump_or_mass': 0.85}
}
disease_map["CSV_0427"] = {
    "name": "Lymphoma",
    "primary_symptoms": ['hoarse_voice', 'groin_mass', 'itchy_ears'],
    "secondary_symptoms": ['regurgitation', 'neck_mass', 'fatigue', 'regurgitation.1'],
    "rare_symptoms": [],
    "symptom_weights": {'hoarse_voice': 0.75, 'groin_mass': 0.83, 'regurgitation': 0.58, 'neck_mass': 0.58, 'itchy_ears': 0.74, 'fatigue': 0.47, 'regurgitation.1': 0.58}
}
disease_map["CSV_0428"] = {
    "name": "Macular Degeneration",
    "primary_symptoms": [],
    "secondary_symptoms": ['diminished_vision', 'double_vision', 'symptoms_of_eye', 'pain_in_eye', 'abnormal_movement_of_eyelid', 'foreign_body_sensation_in_eye', 'spots_or_clouds_in_vision', 'lacrimation', 'itchiness_of_eye', 'blindness', 'bleeding_from_eye'],
    "rare_symptoms": [],
    "symptom_weights": {'diminished_vision': 0.5, 'double_vision': 0.67, 'symptoms_of_eye': 0.49, 'pain_in_eye': 0.5, 'abnormal_movement_of_eyelid': 0.51, 'foreign_body_sensation_in_eye': 0.54, 'spots_or_clouds_in_vision': 0.5, 'lacrimation': 0.51, 'itchiness_of_eye': 0.49, 'blindness': 0.52, 'bleeding_from_eye': 0.5}
}
disease_map["CSV_0429"] = {
    "name": "Magnesium Deficiency",
    "primary_symptoms": ['shortness_of_breath', 'sharp_chest_pain', 'dizziness'],
    "secondary_symptoms": ['leg_pain'],
    "rare_symptoms": [],
    "symptom_weights": {'shortness_of_breath': 0.89, 'sharp_chest_pain': 1.0, 'dizziness': 0.74, 'leg_pain': 0.51}
}
disease_map["CSV_0430"] = {
    "name": "Malaria",
    "primary_symptoms": ['fainting', 'headache', 'knee_lump_or_mass'],
    "secondary_symptoms": ['fever'],
    "rare_symptoms": [],
    "symptom_weights": {'fainting': 1.0, 'headache': 0.87, 'knee_lump_or_mass': 0.8, 'fever': 0.67}
}
disease_map["CSV_0431"] = {
    "name": "Male Genitalia Infection",
    "primary_symptoms": ['swelling_of_scrotum', 'irritable_infant'],
    "secondary_symptoms": ['pain_in_testicles', 'mass_in_scrotum', 'abnormal_appearing_skin', 'bumps_on_penis'],
    "rare_symptoms": [],
    "symptom_weights": {'swelling_of_scrotum': 0.78, 'pain_in_testicles': 0.62, 'mass_in_scrotum': 0.57, 'irritable_infant': 0.83, 'abnormal_appearing_skin': 0.68, 'bumps_on_penis': 0.66}
}
disease_map["CSV_0432"] = {
    "name": "Malignant Hypertension",
    "primary_symptoms": ['depressive_or_psychotic_symptoms', 'insomnia'],
    "secondary_symptoms": ['shortness_of_breath', 'sharp_chest_pain', 'vomiting', 'headache', 'lower_body_pain'],
    "rare_symptoms": [],
    "symptom_weights": {'shortness_of_breath': 0.5, 'depressive_or_psychotic_symptoms': 0.77, 'sharp_chest_pain': 0.47, 'insomnia': 0.82, 'vomiting': 0.54, 'headache': 0.55, 'lower_body_pain': 0.52}
}
disease_map["CSV_0433"] = {
    "name": "Marijuana Abuse",
    "primary_symptoms": [],
    "secondary_symptoms": ['anxiety_and_nervousness', 'depression', 'depressive_or_psychotic_symptoms', 'difficulty_speaking', 'abusing_alcohol', 'hostile_behavior', 'drug_abuse', 'excessive_anger', 'delusions_or_hallucinations', 'temper_problems', 'fears_and_phobias', 'low_self_esteem'],
    "rare_symptoms": [],
    "symptom_weights": {'anxiety_and_nervousness': 0.49, 'depression': 0.5, 'depressive_or_psychotic_symptoms': 0.5, 'difficulty_speaking': 0.49, 'abusing_alcohol': 0.53, 'hostile_behavior': 0.52, 'drug_abuse': 0.51, 'excessive_anger': 0.52, 'delusions_or_hallucinations': 0.5, 'temper_problems': 0.49, 'fears_and_phobias': 0.51, 'low_self_esteem': 0.52}
}
disease_map["CSV_0434"] = {
    "name": "Mastectomy",
    "primary_symptoms": ['skin_swelling', 'arm_stiffness_or_tightness', 'pain_or_soreness_of_breast'],
    "secondary_symptoms": [],
    "rare_symptoms": [],
    "symptom_weights": {'skin_swelling': 0.71, 'arm_stiffness_or_tightness': 0.94, 'pain_or_soreness_of_breast': 0.94}
}
disease_map["CSV_0435"] = {
    "name": "Mastoiditis",
    "primary_symptoms": ['cough', 'nasal_congestion', 'diminished_hearing'],
    "secondary_symptoms": ['dizziness', 'facial_pain', 'ear_pain'],
    "rare_symptoms": [],
    "symptom_weights": {'dizziness': 0.56, 'cough': 0.75, 'nasal_congestion': 0.78, 'diminished_hearing': 0.79, 'facial_pain': 0.47, 'ear_pain': 0.52}
}
disease_map["CSV_0436"] = {
    "name": "Meckel Diverticulum",
    "primary_symptoms": ['lower_abdominal_pain', 'knee_lump_or_mass'],
    "secondary_symptoms": [],
    "rare_symptoms": [],
    "symptom_weights": {'lower_abdominal_pain': 1.0, 'knee_lump_or_mass': 1.0}
}
disease_map["CSV_0437"] = {
    "name": "Melanoma",
    "primary_symptoms": ['swollen_lymph_nodes'],
    "secondary_symptoms": ['skin_swelling', 'abnormal_appearing_skin', 'skin_lesion', 'skin_growth', 'irregular_appearing_scalp', 'skin_moles', 'itchy_eyelid'],
    "rare_symptoms": [],
    "symptom_weights": {'skin_swelling': 0.5, 'abnormal_appearing_skin': 0.52, 'skin_lesion': 0.53, 'skin_growth': 0.54, 'irregular_appearing_scalp': 0.54, 'swollen_lymph_nodes': 0.79, 'skin_moles': 0.51, 'itchy_eyelid': 0.65}
}
disease_map["CSV_0438"] = {
    "name": "Meniere Disease",
    "primary_symptoms": ['facial_pain'],
    "secondary_symptoms": ['dizziness', 'diminished_hearing', 'headache', 'nausea', 'ear_pain', 'ringing_in_ear', 'allergic_reaction'],
    "rare_symptoms": [],
    "symptom_weights": {'dizziness': 0.51, 'diminished_hearing': 0.51, 'headache': 0.5, 'nausea': 0.52, 'facial_pain': 0.78, 'ear_pain': 0.67, 'ringing_in_ear': 0.52, 'allergic_reaction': 0.49}
}
disease_map["CSV_0439"] = {
    "name": "Meningioma",
    "primary_symptoms": ['depressive_or_psychotic_symptoms', 'dizziness', 'headache', 'weakness', 'disturbance_of_memory'],
    "secondary_symptoms": [],
    "rare_symptoms": [],
    "symptom_weights": {'depressive_or_psychotic_symptoms': 0.94, 'dizziness': 1.0, 'headache': 0.72, 'weakness': 0.72, 'disturbance_of_memory': 0.72}
}
disease_map["CSV_0440"] = {
    "name": "Menopause",
    "primary_symptoms": ['vaginal_itching', 'involuntary_urination', 'hot_flashes'],
    "secondary_symptoms": ['absence_of_menstruation', 'sweating'],
    "rare_symptoms": ['unpredictable_menstruation'],
    "symptom_weights": {'vaginal_itching': 0.87, 'involuntary_urination': 0.83, 'hot_flashes': 0.75, 'absence_of_menstruation': 0.45, 'unpredictable_menstruation': 0.39, 'sweating': 0.58}
}
disease_map["CSV_0441"] = {
    "name": "Metabolic Disorder",
    "primary_symptoms": ['jaundice', 'arm_stiffness_or_tightness'],
    "secondary_symptoms": ['smoking_problems'],
    "rare_symptoms": ['weight_gain'],
    "symptom_weights": {'jaundice': 0.97, 'arm_stiffness_or_tightness': 0.82, 'weight_gain': 0.35, 'smoking_problems': 0.47}
}
disease_map["CSV_0442"] = {
    "name": "Metastatic Cancer",
    "primary_symptoms": ['vaginal_dryness'],
    "secondary_symptoms": ['neck_mass', 'decreased_appetite', 'focal_weakness', 'fatigue'],
    "rare_symptoms": [],
    "symptom_weights": {'vaginal_dryness': 0.85, 'neck_mass': 0.56, 'decreased_appetite': 0.52, 'focal_weakness': 0.56, 'fatigue': 0.56}
}
disease_map["CSV_0443"] = {
    "name": "Missed Abortion",
    "primary_symptoms": ['blood_in_stool'],
    "secondary_symptoms": ['sharp_abdominal_pain', 'lower_abdominal_pain', 'intermenstrual_bleeding', 'pain_during_pregnancy', 'problems_during_pregnancy', 'spotting_or_bleeding_during_pregnancy', 'cramps_and_spasms', 'blood_clots_during_menstrual_periods'],
    "rare_symptoms": [],
    "symptom_weights": {'blood_in_stool': 0.82, 'sharp_abdominal_pain': 0.5, 'lower_abdominal_pain': 0.49, 'intermenstrual_bleeding': 0.54, 'pain_during_pregnancy': 0.5, 'problems_during_pregnancy': 0.55, 'spotting_or_bleeding_during_pregnancy': 0.53, 'cramps_and_spasms': 0.5, 'blood_clots_during_menstrual_periods': 0.46}
}
disease_map["CSV_0444"] = {
    "name": "Mitral Valve Disease",
    "primary_symptoms": [],
    "secondary_symptoms": ['shortness_of_breath', 'sharp_chest_pain', 'dizziness', 'chest_tightness', 'irregular_heartbeat', 'increased_heart_rate', 'fatigue', 'sweating', 'nightmares'],
    "rare_symptoms": [],
    "symptom_weights": {'shortness_of_breath': 0.68, 'sharp_chest_pain': 0.5, 'dizziness': 0.52, 'chest_tightness': 0.55, 'irregular_heartbeat': 0.66, 'increased_heart_rate': 0.47, 'fatigue': 0.5, 'sweating': 0.69, 'nightmares': 0.53}
}
disease_map["CSV_0445"] = {
    "name": "Mittelschmerz",
    "primary_symptoms": ['diarrhea'],
    "secondary_symptoms": ['sharp_abdominal_pain', 'vomiting', 'lower_abdominal_pain', 'pelvic_pain', 'painful_menstruation'],
    "rare_symptoms": [],
    "symptom_weights": {'sharp_abdominal_pain': 0.55, 'vomiting': 0.58, 'diarrhea': 0.96, 'lower_abdominal_pain': 0.57, 'pelvic_pain': 0.57, 'painful_menstruation': 0.58}
}
disease_map["CSV_0446"] = {
    "name": "Molluscum Contagiosum",
    "primary_symptoms": ['acne_or_pimples'],
    "secondary_symptoms": ['skin_swelling', 'abnormal_appearing_skin', 'skin_lesion', 'knee_lump_or_mass', 'itching_of_skin', 'skin_dryness,_peeling,_scaliness,_or_roughness', 'warts', 'skin_rash'],
    "rare_symptoms": [],
    "symptom_weights": {'skin_swelling': 0.47, 'abnormal_appearing_skin': 0.68, 'skin_lesion': 0.5, 'acne_or_pimples': 0.7, 'knee_lump_or_mass': 0.66, 'itching_of_skin': 0.52, 'skin_dryness,_peeling,_scaliness,_or_roughness': 0.47, 'warts': 0.51, 'skin_rash': 0.49}
}
disease_map["CSV_0447"] = {
    "name": "Mononeuritis",
    "primary_symptoms": [],
    "secondary_symptoms": ['leg_pain', 'hand_or_finger_pain', 'wrist_pain', 'arm_pain', 'foot_or_toe_pain', 'ankle_pain', 'elbow_pain', 'loss_of_sensation', 'shoulder_pain', 'hand_or_finger_weakness'],
    "rare_symptoms": [],
    "symptom_weights": {'leg_pain': 0.66, 'hand_or_finger_pain': 0.66, 'wrist_pain': 0.53, 'arm_pain': 0.51, 'foot_or_toe_pain': 0.49, 'ankle_pain': 0.52, 'elbow_pain': 0.5, 'loss_of_sensation': 0.51, 'shoulder_pain': 0.49, 'hand_or_finger_weakness': 0.53}
}
disease_map["CSV_0448"] = {
    "name": "Mononucleosis",
    "primary_symptoms": ['cough', 'swollen_lymph_nodes'],
    "secondary_symptoms": ['sore_throat', 'nasal_congestion', 'feeling_ill', 'headache', 'fever', 'skin_rash'],
    "rare_symptoms": [],
    "symptom_weights": {'sore_throat': 0.55, 'cough': 0.79, 'nasal_congestion': 0.49, 'feeling_ill': 0.69, 'headache': 0.52, 'swollen_lymph_nodes': 0.72, 'fever': 0.53, 'skin_rash': 0.51}
}
disease_map["CSV_0449"] = {
    "name": "Moyamoya Disease",
    "primary_symptoms": ['depressive_or_psychotic_symptoms', 'elbow_weakness'],
    "secondary_symptoms": [],
    "rare_symptoms": [],
    "symptom_weights": {'depressive_or_psychotic_symptoms': 1.0, 'elbow_weakness': 0.92}
}
disease_map["CSV_0450"] = {
    "name": "Mucositis",
    "primary_symptoms": ['difficulty_in_swallowing', 'irritable_infant'],
    "secondary_symptoms": ['sore_throat', 'mouth_ulcer', 'decreased_appetite', 'fever', 'tongue_lesions', 'mouth_pain'],
    "rare_symptoms": [],
    "symptom_weights": {'sore_throat': 0.54, 'difficulty_in_swallowing': 0.74, 'irritable_infant': 0.75, 'mouth_ulcer': 0.57, 'decreased_appetite': 0.52, 'fever': 0.48, 'tongue_lesions': 0.54, 'mouth_pain': 0.55}
}
disease_map["CSV_0451"] = {
    "name": "Multiple Myeloma",
    "primary_symptoms": ['lip_swelling'],
    "secondary_symptoms": ['problems_with_movement', 'weakness', 'disturbance_of_memory', 'fatigue'],
    "rare_symptoms": [],
    "symptom_weights": {'lip_swelling': 0.92, 'problems_with_movement': 0.63, 'weakness': 0.45, 'disturbance_of_memory': 0.55, 'fatigue': 0.57}
}
disease_map["CSV_0452"] = {
    "name": "Multiple Sclerosis",
    "primary_symptoms": [],
    "secondary_symptoms": ['dizziness', 'abnormal_involuntary_movements', 'headache', 'problems_with_movement', 'weakness', 'loss_of_sensation', 'focal_weakness', 'disturbance_of_memory', 'paresthesia', 'fatigue', 'leg_weakness'],
    "rare_symptoms": [],
    "symptom_weights": {'dizziness': 0.49, 'abnormal_involuntary_movements': 0.67, 'headache': 0.49, 'problems_with_movement': 0.51, 'weakness': 0.51, 'loss_of_sensation': 0.54, 'focal_weakness': 0.48, 'disturbance_of_memory': 0.51, 'paresthesia': 0.5, 'fatigue': 0.52, 'leg_weakness': 0.54}
}
disease_map["CSV_0453"] = {
    "name": "Mumps",
    "primary_symptoms": ['swollen_lymph_nodes', 'ear_pain', 'shoulder_swelling'],
    "secondary_symptoms": ['sore_throat'],
    "rare_symptoms": [],
    "symptom_weights": {'sore_throat': 0.69, 'swollen_lymph_nodes': 0.91, 'ear_pain': 0.8, 'shoulder_swelling': 0.82}
}
disease_map["CSV_0454"] = {
    "name": "Muscle Spasm",
    "primary_symptoms": [],
    "secondary_symptoms": ['sharp_chest_pain', 'abnormal_involuntary_movements', 'leg_pain', 'headache', 'arm_pain', 'back_pain', 'neck_pain', 'low_back_pain', 'loss_of_sensation', 'muscle_cramps,_contractures,_or_spasms'],
    "rare_symptoms": [],
    "symptom_weights": {'sharp_chest_pain': 0.48, 'abnormal_involuntary_movements': 0.49, 'leg_pain': 0.67, 'headache': 0.53, 'arm_pain': 0.52, 'back_pain': 0.5, 'neck_pain': 0.52, 'low_back_pain': 0.68, 'loss_of_sensation': 0.52, 'muscle_cramps,_contractures,_or_spasms': 0.5}
}
disease_map["CSV_0455"] = {
    "name": "Muscular Dystrophy",
    "primary_symptoms": ['cough', 'hip_pain', 'fatigue'],
    "secondary_symptoms": ['nasal_congestion'],
    "rare_symptoms": ['feeling_cold'],
    "symptom_weights": {'cough': 0.93, 'nasal_congestion': 0.69, 'hip_pain': 0.93, 'feeling_cold': 0.38, 'fatigue': 0.71}
}
disease_map["CSV_0456"] = {
    "name": "Myasthenia Gravis",
    "primary_symptoms": ['shortness_of_breath', 'dizziness'],
    "secondary_symptoms": ['double_vision', 'weakness', 'slurring_words', 'fatigue', 'coughing_up_sputum'],
    "rare_symptoms": [],
    "symptom_weights": {'shortness_of_breath': 0.91, 'dizziness': 0.9, 'double_vision': 0.61, 'weakness': 0.6, 'slurring_words': 0.51, 'fatigue': 0.58, 'coughing_up_sputum': 0.68}
}
disease_map["CSV_0457"] = {
    "name": "Myelodysplastic Syndrome",
    "primary_symptoms": ['difficulty_speaking'],
    "secondary_symptoms": ['chills'],
    "rare_symptoms": ['fatigue'],
    "symptom_weights": {'difficulty_speaking': 1.0, 'chills': 0.67, 'fatigue': 0.33}
}
disease_map["CSV_0458"] = {
    "name": "Myocarditis",
    "primary_symptoms": ['sharp_chest_pain', 'dizziness', 'palpitations'],
    "secondary_symptoms": [],
    "rare_symptoms": [],
    "symptom_weights": {'sharp_chest_pain': 1.0, 'dizziness': 1.0, 'palpitations': 1.0}
}
disease_map["CSV_0459"] = {
    "name": "Myoclonus",
    "primary_symptoms": ['insomnia', 'muscle_swelling'],
    "secondary_symptoms": ['abnormal_involuntary_movements', 'seizures'],
    "rare_symptoms": [],
    "symptom_weights": {'insomnia': 1.0, 'abnormal_involuntary_movements': 0.55, 'seizures': 0.64, 'muscle_swelling': 0.73}
}
disease_map["CSV_0460"] = {
    "name": "Myopia",
    "primary_symptoms": ['foreign_body_sensation_in_eye'],
    "secondary_symptoms": ['eye_deviation', 'diminished_vision', 'symptoms_of_eye', 'pain_in_eye', 'eye_moves_abnormally', 'spots_or_clouds_in_vision', 'eye_redness', 'blindness'],
    "rare_symptoms": [],
    "symptom_weights": {'eye_deviation': 0.65, 'diminished_vision': 0.52, 'symptoms_of_eye': 0.51, 'pain_in_eye': 0.52, 'eye_moves_abnormally': 0.51, 'foreign_body_sensation_in_eye': 0.78, 'spots_or_clouds_in_vision': 0.5, 'eye_redness': 0.53, 'blindness': 0.51}
}
disease_map["CSV_0461"] = {
    "name": "Myositis",
    "primary_symptoms": ['hip_pain', 'headache', 'problems_with_movement'],
    "secondary_symptoms": ['leg_pain', 'knee_pain', 'loss_of_sensation'],
    "rare_symptoms": [],
    "symptom_weights": {'leg_pain': 0.58, 'hip_pain': 0.82, 'headache': 0.74, 'knee_pain': 0.54, 'problems_with_movement': 0.77, 'loss_of_sensation': 0.47}
}
disease_map["CSV_0462"] = {
    "name": "Narcolepsy",
    "primary_symptoms": ['shortness_of_breath', 'insomnia', 'disturbance_of_memory'],
    "secondary_symptoms": ['headache', 'fatigue', 'sleepiness', 'apnea'],
    "rare_symptoms": [],
    "symptom_weights": {'shortness_of_breath': 0.7, 'insomnia': 0.8, 'headache': 0.55, 'disturbance_of_memory': 0.76, 'fatigue': 0.53, 'sleepiness': 0.62, 'apnea': 0.56}
}
disease_map["CSV_0463"] = {
    "name": "Nasal Polyp",
    "primary_symptoms": ['frontal_headache', 'painful_sinuses'],
    "secondary_symptoms": ['hoarse_voice', 'cough', 'nasal_congestion', 'headache', 'facial_pain', 'allergic_reaction'],
    "rare_symptoms": [],
    "symptom_weights": {'hoarse_voice': 0.68, 'cough': 0.68, 'nasal_congestion': 0.55, 'headache': 0.57, 'facial_pain': 0.5, 'frontal_headache': 0.71, 'allergic_reaction': 0.53, 'painful_sinuses': 0.71}
}
disease_map["CSV_0464"] = {
    "name": "Necrotizing Fasciitis",
    "primary_symptoms": ['leg_pain', 'hip_pain'],
    "secondary_symptoms": ['elbow_weakness'],
    "rare_symptoms": [],
    "symptom_weights": {'leg_pain': 1.0, 'hip_pain': 1.0, 'elbow_weakness': 0.67}
}
disease_map["CSV_0465"] = {
    "name": "Neonatal Jaundice",
    "primary_symptoms": ['lack_of_growth'],
    "secondary_symptoms": ['jaundice', 'irritable_infant', 'infant_feeding_problem', 'changes_in_stool_appearance'],
    "rare_symptoms": [],
    "symptom_weights": {'lack_of_growth': 0.94, 'jaundice': 0.56, 'irritable_infant': 0.44, 'infant_feeding_problem': 0.62, 'changes_in_stool_appearance': 0.53}
}
disease_map["CSV_0466"] = {
    "name": "Nerve Impingement Near The Shoulder",
    "primary_symptoms": ['hand_or_finger_stiffness_or_tightness'],
    "secondary_symptoms": ['arm_pain', 'neck_pain', 'elbow_pain', 'problems_with_movement', 'shoulder_pain', 'shoulder_stiffness_or_tightness', 'shoulder_weakness'],
    "rare_symptoms": [],
    "symptom_weights": {'arm_pain': 0.5, 'hand_or_finger_stiffness_or_tightness': 0.81, 'neck_pain': 0.68, 'elbow_pain': 0.51, 'problems_with_movement': 0.54, 'shoulder_pain': 0.54, 'shoulder_stiffness_or_tightness': 0.51, 'shoulder_weakness': 0.49}
}
disease_map["CSV_0467"] = {
    "name": "Neuralgia",
    "primary_symptoms": [],
    "secondary_symptoms": ['leg_pain', 'hip_pain', 'headache', 'arm_pain', 'back_pain', 'neck_pain', 'low_back_pain', 'loss_of_sensation', 'shoulder_pain', 'ache_all_over'],
    "rare_symptoms": [],
    "symptom_weights": {'leg_pain': 0.47, 'hip_pain': 0.66, 'headache': 0.68, 'arm_pain': 0.5, 'back_pain': 0.52, 'neck_pain': 0.51, 'low_back_pain': 0.5, 'loss_of_sensation': 0.52, 'shoulder_pain': 0.51, 'ache_all_over': 0.5}
}
disease_map["CSV_0468"] = {
    "name": "Neurofibromatosis",
    "primary_symptoms": ['abnormal_involuntary_movements', 'groin_mass'],
    "secondary_symptoms": ['headache', 'abnormal_appearing_skin'],
    "rare_symptoms": [],
    "symptom_weights": {'abnormal_involuntary_movements': 0.9, 'groin_mass': 0.83, 'headache': 0.57, 'abnormal_appearing_skin': 0.53}
}
disease_map["CSV_0469"] = {
    "name": "Neuropathy Due To Drugs",
    "primary_symptoms": ['cough', 'vomiting', 'foot_or_toe_pain'],
    "secondary_symptoms": ['problems_with_movement', 'loss_of_sensation'],
    "rare_symptoms": [],
    "symptom_weights": {'cough': 0.75, 'vomiting': 0.95, 'foot_or_toe_pain': 0.82, 'problems_with_movement': 0.6, 'loss_of_sensation': 0.55}
}
disease_map["CSV_0470"] = {
    "name": "Neurosis",
    "primary_symptoms": [],
    "secondary_symptoms": ['anxiety_and_nervousness', 'depression', 'depressive_or_psychotic_symptoms', 'insomnia', 'hostile_behavior', 'drug_abuse', 'headache', 'smoking_problems', 'excessive_anger', 'delusions_or_hallucinations', 'obsessions_and_compulsions'],
    "rare_symptoms": [],
    "symptom_weights": {'anxiety_and_nervousness': 0.49, 'depression': 0.51, 'depressive_or_psychotic_symptoms': 0.5, 'insomnia': 0.51, 'hostile_behavior': 0.52, 'drug_abuse': 0.51, 'headache': 0.51, 'smoking_problems': 0.66, 'excessive_anger': 0.51, 'delusions_or_hallucinations': 0.49, 'obsessions_and_compulsions': 0.51}
}
disease_map["CSV_0471"] = {
    "name": "Nonalcoholic Liver Disease (Nash)",
    "primary_symptoms": ['dizziness', 'sharp_abdominal_pain', 'mouth_ulcer'],
    "secondary_symptoms": ['nausea', 'weight_gain'],
    "rare_symptoms": [],
    "symptom_weights": {'dizziness': 0.73, 'sharp_abdominal_pain': 0.84, 'nausea': 0.55, 'mouth_ulcer': 0.87, 'weight_gain': 0.44}
}
disease_map["CSV_0472"] = {
    "name": "Normal Pressure Hydrocephalus",
    "primary_symptoms": ['depressive_or_psychotic_symptoms', 'palpitations'],
    "secondary_symptoms": ['headache', 'problems_with_movement'],
    "rare_symptoms": [],
    "symptom_weights": {'depressive_or_psychotic_symptoms': 0.88, 'palpitations': 1.0, 'headache': 0.46, 'problems_with_movement': 0.69}
}
disease_map["CSV_0473"] = {
    "name": "Nose Disorder",
    "primary_symptoms": [],
    "secondary_symptoms": ['sore_throat', 'cough', 'nasal_congestion', 'headache', 'facial_pain', 'ear_pain', 'fever', 'difficulty_breathing', 'coryza', 'sinus_congestion', 'painful_sinuses', 'nosebleed'],
    "rare_symptoms": [],
    "symptom_weights": {'sore_throat': 0.48, 'cough': 0.51, 'nasal_congestion': 0.5, 'headache': 0.5, 'facial_pain': 0.51, 'ear_pain': 0.52, 'fever': 0.5, 'difficulty_breathing': 0.51, 'coryza': 0.49, 'sinus_congestion': 0.5, 'painful_sinuses': 0.51, 'nosebleed': 0.52}
}
disease_map["CSV_0474"] = {
    "name": "Obesity",
    "primary_symptoms": ['weight_gain', 'sleepiness'],
    "secondary_symptoms": ['excessive_appetite'],
    "rare_symptoms": [],
    "symptom_weights": {'weight_gain': 1.0, 'excessive_appetite': 0.67, 'sleepiness': 1.0}
}
disease_map["CSV_0475"] = {
    "name": "Obsessive Compulsive Disorder (Ocd)",
    "primary_symptoms": ['feeling_ill'],
    "secondary_symptoms": ['anxiety_and_nervousness', 'depression', 'depressive_or_psychotic_symptoms', 'lack_of_growth', 'hostile_behavior', 'temper_problems', 'low_self_esteem', 'obsessions_and_compulsions'],
    "rare_symptoms": [],
    "symptom_weights": {'anxiety_and_nervousness': 0.51, 'depression': 0.5, 'depressive_or_psychotic_symptoms': 0.5, 'lack_of_growth': 0.66, 'hostile_behavior': 0.5, 'feeling_ill': 0.79, 'temper_problems': 0.49, 'low_self_esteem': 0.51, 'obsessions_and_compulsions': 0.48}
}
disease_map["CSV_0476"] = {
    "name": "Obstructive Sleep Apnea (Osa)",
    "primary_symptoms": [],
    "secondary_symptoms": ['shortness_of_breath', 'insomnia', 'abnormal_involuntary_movements', 'difficulty_in_swallowing', 'mouth_dryness', 'weight_gain', 'difficulty_breathing', 'fatigue', 'sleepiness', 'apnea', 'abnormal_breathing_sounds', 'sweating'],
    "rare_symptoms": [],
    "symptom_weights": {'shortness_of_breath': 0.48, 'insomnia': 0.5, 'abnormal_involuntary_movements': 0.51, 'difficulty_in_swallowing': 0.5, 'mouth_dryness': 0.53, 'weight_gain': 0.51, 'difficulty_breathing': 0.51, 'fatigue': 0.52, 'sleepiness': 0.5, 'apnea': 0.51, 'abnormal_breathing_sounds': 0.51, 'sweating': 0.52}
}
disease_map["CSV_0477"] = {
    "name": "Omphalitis",
    "primary_symptoms": ['emotional_symptoms', 'flatulence', 'irregular_belly_button'],
    "secondary_symptoms": [],
    "rare_symptoms": [],
    "symptom_weights": {'emotional_symptoms': 1.0, 'flatulence': 1.0, 'irregular_belly_button': 1.0}
}
disease_map["CSV_0478"] = {
    "name": "Onychomycosis",
    "primary_symptoms": [],
    "secondary_symptoms": ['skin_swelling', 'abnormal_appearing_skin', 'skin_growth', 'foot_or_toe_pain', 'skin_on_leg_or_foot_looks_infected', 'irregular_appearing_nails', 'skin_dryness,_peeling,_scaliness,_or_roughness', 'too_little_hair', 'skin_rash'],
    "rare_symptoms": [],
    "symptom_weights": {'skin_swelling': 0.65, 'abnormal_appearing_skin': 0.68, 'skin_growth': 0.69, 'foot_or_toe_pain': 0.51, 'skin_on_leg_or_foot_looks_infected': 0.53, 'irregular_appearing_nails': 0.5, 'skin_dryness,_peeling,_scaliness,_or_roughness': 0.52, 'too_little_hair': 0.52, 'skin_rash': 0.52}
}
disease_map["CSV_0479"] = {
    "name": "Open Wound Due To Trauma",
    "primary_symptoms": ['wrist_swelling', 'skin_on_arm_or_hand_looks_infected'],
    "secondary_symptoms": [],
    "rare_symptoms": [],
    "symptom_weights": {'wrist_swelling': 1.0, 'skin_on_arm_or_hand_looks_infected': 1.0}
}
disease_map["CSV_0480"] = {
    "name": "Open Wound From Surgical Incision",
    "primary_symptoms": ['skin_swelling', 'flatulence'],
    "secondary_symptoms": ['skin_lesion'],
    "rare_symptoms": [],
    "symptom_weights": {'skin_swelling': 0.86, 'flatulence': 0.86, 'skin_lesion': 0.57}
}
disease_map["CSV_0481"] = {
    "name": "Open Wound Of The Abdomen",
    "primary_symptoms": ['sharp_abdominal_pain'],
    "secondary_symptoms": ['blindness'],
    "rare_symptoms": ['irregular_belly_button'],
    "symptom_weights": {'sharp_abdominal_pain': 1.0, 'blindness': 0.67, 'irregular_belly_button': 0.33}
}
disease_map["CSV_0482"] = {
    "name": "Open Wound Of The Arm",
    "primary_symptoms": ['arm_pain', 'knee_weakness'],
    "secondary_symptoms": ['redness_in_or_around_nose'],
    "rare_symptoms": ['elbow_pain'],
    "symptom_weights": {'arm_pain': 0.7, 'knee_weakness': 0.9, 'elbow_pain': 0.3, 'redness_in_or_around_nose': 0.4}
}
disease_map["CSV_0483"] = {
    "name": "Open Wound Of The Back",
    "primary_symptoms": ['irregular_heartbeat', 'weight_gain'],
    "secondary_symptoms": ['skin_lesion', 'lower_body_pain'],
    "rare_symptoms": [],
    "symptom_weights": {'irregular_heartbeat': 0.89, 'skin_lesion': 0.67, 'weight_gain': 0.78, 'lower_body_pain': 0.56}
}
disease_map["CSV_0484"] = {
    "name": "Open Wound Of The Cheek",
    "primary_symptoms": ['wrist_pain', 'facial_pain'],
    "secondary_symptoms": [],
    "rare_symptoms": [],
    "symptom_weights": {'wrist_pain': 1.0, 'facial_pain': 1.0}
}
disease_map["CSV_0485"] = {
    "name": "Open Wound Of The Chest",
    "primary_symptoms": ['sharp_chest_pain', 'drug_abuse'],
    "secondary_symptoms": [],
    "rare_symptoms": [],
    "symptom_weights": {'sharp_chest_pain': 1.0, 'drug_abuse': 1.0}
}
disease_map["CSV_0486"] = {
    "name": "Open Wound Of The Ear",
    "primary_symptoms": ['dry_lips'],
    "secondary_symptoms": ['facial_pain', 'ear_pain', 'fluid_in_ear', 'bleeding_from_ear'],
    "rare_symptoms": [],
    "symptom_weights": {'dry_lips': 0.94, 'facial_pain': 0.58, 'ear_pain': 0.55, 'fluid_in_ear': 0.45, 'bleeding_from_ear': 0.55}
}
disease_map["CSV_0487"] = {
    "name": "Open Wound Of The Eye",
    "primary_symptoms": ['white_discharge_from_eye', 'pain_in_eye'],
    "secondary_symptoms": ['diminished_vision', 'symptoms_of_eye', 'spots_or_clouds_in_vision'],
    "rare_symptoms": [],
    "symptom_weights": {'white_discharge_from_eye': 0.94, 'diminished_vision': 0.47, 'symptoms_of_eye': 0.53, 'pain_in_eye': 0.72, 'spots_or_clouds_in_vision': 0.59}
}
disease_map["CSV_0488"] = {
    "name": "Open Wound Of The Face",
    "primary_symptoms": ['wrist_swelling', 'facial_pain'],
    "secondary_symptoms": [],
    "rare_symptoms": [],
    "symptom_weights": {'wrist_swelling': 1.0, 'facial_pain': 1.0}
}
disease_map["CSV_0489"] = {
    "name": "Open Wound Of The Finger",
    "primary_symptoms": ['hand_or_finger_pain'],
    "secondary_symptoms": ['hand_or_finger_swelling', 'hand_or_finger_stiffness_or_tightness', 'skin_on_arm_or_hand_looks_infected'],
    "rare_symptoms": [],
    "symptom_weights": {'hand_or_finger_pain': 0.75, 'hand_or_finger_swelling': 0.5, 'hand_or_finger_stiffness_or_tightness': 0.5, 'skin_on_arm_or_hand_looks_infected': 0.5}
}
disease_map["CSV_0490"] = {
    "name": "Open Wound Of The Foot",
    "primary_symptoms": [],
    "secondary_symptoms": ['skin_lesion', 'foot_or_toe_pain', 'foot_or_toe_swelling', 'skin_on_leg_or_foot_looks_infected', 'irregular_appearing_nails', 'foot_or_toe_lump_or_mass'],
    "rare_symptoms": [],
    "symptom_weights": {'skin_lesion': 0.48, 'foot_or_toe_pain': 0.59, 'foot_or_toe_swelling': 0.48, 'skin_on_leg_or_foot_looks_infected': 0.56, 'irregular_appearing_nails': 0.52, 'foot_or_toe_lump_or_mass': 0.59}
}
disease_map["CSV_0491"] = {
    "name": "Open Wound Of The Hand",
    "primary_symptoms": ['hand_or_finger_pain'],
    "secondary_symptoms": ['hand_or_finger_swelling', 'hand_or_finger_stiffness_or_tightness', 'skin_on_arm_or_hand_looks_infected'],
    "rare_symptoms": [],
    "symptom_weights": {'hand_or_finger_pain': 0.75, 'hand_or_finger_swelling': 0.5, 'hand_or_finger_stiffness_or_tightness': 0.5, 'skin_on_arm_or_hand_looks_infected': 0.5}
}
disease_map["CSV_0492"] = {
    "name": "Open Wound Of The Head",
    "primary_symptoms": ['abusing_alcohol', 'headache'],
    "secondary_symptoms": [],
    "rare_symptoms": [],
    "symptom_weights": {'abusing_alcohol': 1.0, 'headache': 1.0}
}
disease_map["CSV_0493"] = {
    "name": "Open Wound Of The Jaw",
    "primary_symptoms": ['wrist_swelling', 'lip_swelling'],
    "secondary_symptoms": [],
    "rare_symptoms": [],
    "symptom_weights": {'wrist_swelling': 1.0, 'lip_swelling': 1.0}
}
disease_map["CSV_0494"] = {
    "name": "Open Wound Of The Knee",
    "primary_symptoms": ['leg_pain', 'leg_swelling'],
    "secondary_symptoms": [],
    "rare_symptoms": [],
    "symptom_weights": {'leg_pain': 1.0, 'leg_swelling': 1.0}
}
disease_map["CSV_0495"] = {
    "name": "Open Wound Of The Lip",
    "primary_symptoms": ['mouth_ulcer'],
    "secondary_symptoms": ['lip_swelling', 'dry_lips', 'mouth_pain'],
    "rare_symptoms": ['facial_pain'],
    "symptom_weights": {'lip_swelling': 0.54, 'dry_lips': 0.46, 'facial_pain': 0.31, 'mouth_ulcer': 1.0, 'mouth_pain': 0.5}
}
disease_map["CSV_0496"] = {
    "name": "Open Wound Of The Mouth",
    "primary_symptoms": ['lip_swelling', 'mouth_ulcer'],
    "secondary_symptoms": ['toothache', 'peripheral_edema', 'tongue_lesions', 'seizures'],
    "rare_symptoms": [],
    "symptom_weights": {'lip_swelling': 0.87, 'toothache': 0.61, 'mouth_ulcer': 0.88, 'peripheral_edema': 0.66, 'tongue_lesions': 0.6, 'seizures': 0.65}
}
disease_map["CSV_0497"] = {
    "name": "Open Wound Of The Neck",
    "primary_symptoms": ['skin_swelling'],
    "secondary_symptoms": ['abnormal_appearing_skin', 'skin_lesion', 'peripheral_edema', 'ache_all_over'],
    "rare_symptoms": [],
    "symptom_weights": {'skin_swelling': 0.94, 'abnormal_appearing_skin': 0.53, 'skin_lesion': 0.62, 'peripheral_edema': 0.59, 'ache_all_over': 0.66}
}
disease_map["CSV_0498"] = {
    "name": "Open Wound Of The Nose",
    "primary_symptoms": ['diminished_hearing'],
    "secondary_symptoms": ['facial_pain', 'nosebleed'],
    "rare_symptoms": ['headache'],
    "symptom_weights": {'diminished_hearing': 1.0, 'headache': 0.36, 'facial_pain': 0.55, 'nosebleed': 0.64}
}
disease_map["CSV_0499"] = {
    "name": "Open Wound Of The Shoulder",
    "primary_symptoms": ['abusing_alcohol', 'shoulder_pain'],
    "secondary_symptoms": [],
    "rare_symptoms": ['arm_pain'],
    "symptom_weights": {'abusing_alcohol': 1.0, 'arm_pain': 0.25, 'shoulder_pain': 1.0}
}
disease_map["CSV_0500"] = {
    "name": "Oppositional Disorder",
    "primary_symptoms": [],
    "secondary_symptoms": ['depressive_or_psychotic_symptoms', 'fainting', 'hostile_behavior', 'restlessness', 'excessive_anger', 'temper_problems', 'low_self_esteem', 'obsessions_and_compulsions', 'antisocial_behavior', 'low_urine_output'],
    "rare_symptoms": [],
    "symptom_weights": {'depressive_or_psychotic_symptoms': 0.49, 'fainting': 0.54, 'hostile_behavior': 0.56, 'restlessness': 0.53, 'excessive_anger': 0.54, 'temper_problems': 0.47, 'low_self_esteem': 0.67, 'obsessions_and_compulsions': 0.51, 'antisocial_behavior': 0.5, 'low_urine_output': 0.52}
}
disease_map["CSV_0501"] = {
    "name": "Optic Neuritis",
    "primary_symptoms": ['retention_of_urine', 'headache', 'diminished_vision'],
    "secondary_symptoms": ['blindness'],
    "rare_symptoms": [],
    "symptom_weights": {'retention_of_urine': 0.8, 'headache': 1.0, 'diminished_vision': 0.7, 'blindness': 0.6}
}
disease_map["CSV_0502"] = {
    "name": "Oral Leukoplakia",
    "primary_symptoms": ['skin_swelling', 'elbow_weakness', 'tongue_lesions'],
    "secondary_symptoms": [],
    "rare_symptoms": [],
    "symptom_weights": {'skin_swelling': 1.0, 'elbow_weakness': 0.75, 'tongue_lesions': 1.0}
}
disease_map["CSV_0503"] = {
    "name": "Oral Mucosal Lesion",
    "primary_symptoms": ['cough'],
    "secondary_symptoms": ['sore_throat', 'lip_swelling', 'toothache', 'facial_pain', 'mouth_ulcer', 'fever', 'tongue_lesions', 'gum_pain', 'mouth_pain'],
    "rare_symptoms": [],
    "symptom_weights": {'sore_throat': 0.47, 'cough': 0.73, 'lip_swelling': 0.51, 'toothache': 0.5, 'facial_pain': 0.5, 'mouth_ulcer': 0.49, 'fever': 0.5, 'tongue_lesions': 0.49, 'gum_pain': 0.5, 'mouth_pain': 0.5}
}
disease_map["CSV_0504"] = {
    "name": "Oral Thrush (Yeast Infection)",
    "primary_symptoms": [],
    "secondary_symptoms": ['sore_throat', 'cough', 'nasal_congestion', 'irritable_infant', 'mouth_ulcer', 'fever', 'tongue_lesions', 'constipation', 'skin_rash', 'mouth_pain'],
    "rare_symptoms": [],
    "symptom_weights": {'sore_throat': 0.48, 'cough': 0.51, 'nasal_congestion': 0.51, 'irritable_infant': 0.69, 'mouth_ulcer': 0.5, 'fever': 0.49, 'tongue_lesions': 0.52, 'constipation': 0.67, 'skin_rash': 0.49, 'mouth_pain': 0.51}
}
disease_map["CSV_0505"] = {
    "name": "Orbital Cellulitis",
    "primary_symptoms": ['diminished_hearing', 'peripheral_edema'],
    "secondary_symptoms": ['symptoms_of_eye', 'pain_in_eye', 'eye_redness', 'fever', 'swollen_eye'],
    "rare_symptoms": [],
    "symptom_weights": {'diminished_hearing': 0.82, 'symptoms_of_eye': 0.49, 'pain_in_eye': 0.55, 'peripheral_edema': 0.7, 'eye_redness': 0.54, 'fever': 0.48, 'swollen_eye': 0.52}
}
disease_map["CSV_0506"] = {
    "name": "Orthostatic Hypotension",
    "primary_symptoms": ['abnormal_involuntary_movements', 'feeling_ill'],
    "secondary_symptoms": ['sharp_chest_pain', 'dizziness', 'irregular_heartbeat', 'fainting', 'headache', 'weakness'],
    "rare_symptoms": [],
    "symptom_weights": {'sharp_chest_pain': 0.5, 'dizziness': 0.51, 'abnormal_involuntary_movements': 0.83, 'irregular_heartbeat': 0.5, 'fainting': 0.52, 'feeling_ill': 0.73, 'headache': 0.55, 'weakness': 0.47}
}
disease_map["CSV_0507"] = {
    "name": "Osteoarthritis",
    "primary_symptoms": [],
    "secondary_symptoms": ['leg_pain', 'hip_pain', 'hand_or_finger_pain', 'back_pain', 'knee_pain', 'ankle_pain', 'knee_weakness', 'elbow_pain', 'knee_swelling', 'muscle_pain', 'joint_pain'],
    "rare_symptoms": [],
    "symptom_weights": {'leg_pain': 0.5, 'hip_pain': 0.69, 'hand_or_finger_pain': 0.5, 'back_pain': 0.5, 'knee_pain': 0.52, 'ankle_pain': 0.52, 'knee_weakness': 0.52, 'elbow_pain': 0.51, 'knee_swelling': 0.51, 'muscle_pain': 0.51, 'joint_pain': 0.49}
}
disease_map["CSV_0508"] = {
    "name": "Osteochondroma",
    "primary_symptoms": ['lower_abdominal_pain'],
    "secondary_symptoms": ['lip_swelling', 'abnormal_appearing_skin', 'skin_lesion', 'skin_growth', 'knee_pain', 'foot_or_toe_pain'],
    "rare_symptoms": [],
    "symptom_weights": {'lower_abdominal_pain': 0.83, 'lip_swelling': 0.46, 'abnormal_appearing_skin': 0.54, 'skin_lesion': 0.66, 'skin_growth': 0.69, 'knee_pain': 0.51, 'foot_or_toe_pain': 0.51}
}
disease_map["CSV_0509"] = {
    "name": "Osteochondrosis",
    "primary_symptoms": ['hand_or_finger_pain', 'elbow_pain'],
    "secondary_symptoms": ['knee_pain', 'foot_or_toe_pain', 'bowlegged_or_knock_kneed', 'ankle_pain'],
    "rare_symptoms": [],
    "symptom_weights": {'hand_or_finger_pain': 0.77, 'knee_pain': 0.51, 'foot_or_toe_pain': 0.49, 'bowlegged_or_knock_kneed': 0.56, 'ankle_pain': 0.53, 'elbow_pain': 0.87}
}
disease_map["CSV_0510"] = {
    "name": "Osteomyelitis",
    "primary_symptoms": ['difficulty_speaking', 'bones_are_painful'],
    "secondary_symptoms": ['hand_or_finger_pain', 'hand_or_finger_swelling', 'arm_swelling', 'skin_lesion', 'skin_on_leg_or_foot_looks_infected'],
    "rare_symptoms": [],
    "symptom_weights": {'difficulty_speaking': 0.72, 'hand_or_finger_pain': 0.54, 'hand_or_finger_swelling': 0.51, 'arm_swelling': 0.65, 'skin_lesion': 0.59, 'bones_are_painful': 0.86, 'skin_on_leg_or_foot_looks_infected': 0.55}
}
disease_map["CSV_0511"] = {
    "name": "Osteoporosis",
    "primary_symptoms": ['leg_cramps_or_spasms'],
    "secondary_symptoms": ['hip_pain', 'back_pain', 'bones_are_painful', 'disturbance_of_memory', 'stomach_bloating', 'joint_pain', 'muscle_cramps,_contractures,_or_spasms', 'early_or_late_onset_of_menopause'],
    "rare_symptoms": [],
    "symptom_weights": {'hip_pain': 0.49, 'back_pain': 0.53, 'bones_are_painful': 0.51, 'disturbance_of_memory': 0.55, 'leg_cramps_or_spasms': 0.78, 'stomach_bloating': 0.48, 'joint_pain': 0.49, 'muscle_cramps,_contractures,_or_spasms': 0.47, 'early_or_late_onset_of_menopause': 0.54}
}
disease_map["CSV_0512"] = {
    "name": "Otitis Externa (Swimmer'S Ear)",
    "primary_symptoms": [],
    "secondary_symptoms": ['sore_throat', 'cough', 'diminished_hearing', 'facial_pain', 'ear_pain', 'ringing_in_ear', 'plugged_feeling_in_ear', 'itchy_ears', 'fluid_in_ear', 'fever', 'redness_in_ear'],
    "rare_symptoms": [],
    "symptom_weights": {'sore_throat': 0.48, 'cough': 0.52, 'diminished_hearing': 0.5, 'facial_pain': 0.51, 'ear_pain': 0.53, 'ringing_in_ear': 0.51, 'plugged_feeling_in_ear': 0.53, 'itchy_ears': 0.66, 'fluid_in_ear': 0.51, 'fever': 0.54, 'redness_in_ear': 0.52}
}
disease_map["CSV_0513"] = {
    "name": "Otitis Media",
    "primary_symptoms": [],
    "secondary_symptoms": ['sore_throat', 'cough', 'nasal_congestion', 'diminished_hearing', 'vomiting', 'ear_pain', 'plugged_feeling_in_ear', 'fluid_in_ear', 'fever', 'coryza', 'pulling_at_ears'],
    "rare_symptoms": [],
    "symptom_weights": {'sore_throat': 0.49, 'cough': 0.5, 'nasal_congestion': 0.49, 'diminished_hearing': 0.51, 'vomiting': 0.68, 'ear_pain': 0.54, 'plugged_feeling_in_ear': 0.49, 'fluid_in_ear': 0.5, 'fever': 0.5, 'coryza': 0.53, 'pulling_at_ears': 0.5}
}
disease_map["CSV_0514"] = {
    "name": "Otosclerosis",
    "primary_symptoms": ['dizziness', 'emotional_symptoms'],
    "secondary_symptoms": ['diminished_hearing'],
    "rare_symptoms": [],
    "symptom_weights": {'dizziness': 0.95, 'diminished_hearing': 0.53, 'emotional_symptoms': 1.0}
}
disease_map["CSV_0515"] = {
    "name": "Ovarian Cancer",
    "primary_symptoms": ['groin_mass', 'stomach_bloating'],
    "secondary_symptoms": ['sharp_abdominal_pain', 'decreased_appetite'],
    "rare_symptoms": [],
    "symptom_weights": {'groin_mass': 0.84, 'sharp_abdominal_pain': 0.63, 'decreased_appetite': 0.42, 'stomach_bloating': 0.74}
}
disease_map["CSV_0516"] = {
    "name": "Ovarian Cyst",
    "primary_symptoms": [],
    "secondary_symptoms": ['sharp_abdominal_pain', 'vomiting', 'nausea', 'lower_abdominal_pain', 'vaginal_discharge', 'intermenstrual_bleeding', 'pelvic_pain', 'burning_abdominal_pain', 'painful_menstruation'],
    "rare_symptoms": [],
    "symptom_weights": {'sharp_abdominal_pain': 0.52, 'vomiting': 0.67, 'nausea': 0.52, 'lower_abdominal_pain': 0.57, 'vaginal_discharge': 0.68, 'intermenstrual_bleeding': 0.69, 'pelvic_pain': 0.47, 'burning_abdominal_pain': 0.48, 'painful_menstruation': 0.51}
}
disease_map["CSV_0517"] = {
    "name": "Ovarian Torsion",
    "primary_symptoms": ['skin_swelling'],
    "secondary_symptoms": ['groin_mass', 'sharp_abdominal_pain', 'lower_abdominal_pain', 'pelvic_pain', 'ache_all_over'],
    "rare_symptoms": [],
    "symptom_weights": {'skin_swelling': 0.94, 'groin_mass': 0.55, 'sharp_abdominal_pain': 0.57, 'lower_abdominal_pain': 0.57, 'pelvic_pain': 0.52, 'ache_all_over': 0.49}
}
disease_map["CSV_0518"] = {
    "name": "Overflow Incontinence",
    "primary_symptoms": ['suprapubic_pain', 'hand_or_finger_stiffness_or_tightness', 'impotence'],
    "secondary_symptoms": ['retention_of_urine', 'involuntary_urination', 'blood_in_urine', 'symptoms_of_bladder'],
    "rare_symptoms": [],
    "symptom_weights": {'retention_of_urine': 0.54, 'suprapubic_pain': 0.71, 'involuntary_urination': 0.53, 'blood_in_urine': 0.48, 'hand_or_finger_stiffness_or_tightness': 0.8, 'impotence': 0.77, 'symptoms_of_bladder': 0.5}
}
disease_map["CSV_0519"] = {
    "name": "Pain After An Operation",
    "primary_symptoms": [],
    "secondary_symptoms": ['sharp_chest_pain', 'leg_pain', 'sharp_abdominal_pain', 'vomiting', 'headache', 'nausea', 'lower_abdominal_pain', 'back_pain', 'neck_pain', 'low_back_pain', 'side_pain'],
    "rare_symptoms": [],
    "symptom_weights": {'sharp_chest_pain': 0.5, 'leg_pain': 0.68, 'sharp_abdominal_pain': 0.48, 'vomiting': 0.51, 'headache': 0.52, 'nausea': 0.53, 'lower_abdominal_pain': 0.5, 'back_pain': 0.51, 'neck_pain': 0.52, 'low_back_pain': 0.53, 'side_pain': 0.5}
}
disease_map["CSV_0520"] = {
    "name": "Pain Disorder Affecting The Neck",
    "primary_symptoms": ['neck_stiffness_or_tightness'],
    "secondary_symptoms": ['dizziness', 'insomnia', 'headache', 'arm_pain', 'back_pain', 'neck_pain', 'low_back_pain', 'disturbance_of_memory'],
    "rare_symptoms": [],
    "symptom_weights": {'dizziness': 0.5, 'insomnia': 0.5, 'headache': 0.59, 'arm_pain': 0.69, 'back_pain': 0.52, 'neck_pain': 0.58, 'low_back_pain': 0.52, 'neck_stiffness_or_tightness': 0.76, 'disturbance_of_memory': 0.51}
}
disease_map["CSV_0521"] = {
    "name": "Pancreatic Cancer",
    "primary_symptoms": ['arm_swelling', 'ache_all_over'],
    "secondary_symptoms": ['jaundice', 'sharp_abdominal_pain', 'nausea', 'diarrhea', 'stomach_bloating'],
    "rare_symptoms": [],
    "symptom_weights": {'jaundice': 0.53, 'sharp_abdominal_pain': 0.5, 'nausea': 0.59, 'diarrhea': 0.52, 'arm_swelling': 0.79, 'ache_all_over': 0.72, 'stomach_bloating': 0.68}
}
disease_map["CSV_0522"] = {
    "name": "Panic Attack",
    "primary_symptoms": ['anxiety_and_nervousness', 'sharp_chest_pain', 'chest_tightness', 'irregular_heartbeat'],
    "secondary_symptoms": ['shortness_of_breath', 'weakness', 'loss_of_sensation'],
    "rare_symptoms": [],
    "symptom_weights": {'anxiety_and_nervousness': 0.79, 'shortness_of_breath': 0.56, 'sharp_chest_pain': 0.76, 'chest_tightness': 0.79, 'irregular_heartbeat': 0.73, 'weakness': 0.57, 'loss_of_sensation': 0.55}
}
disease_map["CSV_0523"] = {
    "name": "Panic Disorder",
    "primary_symptoms": [],
    "secondary_symptoms": ['anxiety_and_nervousness', 'depression', 'shortness_of_breath', 'depressive_or_psychotic_symptoms', 'dizziness', 'insomnia', 'abnormal_involuntary_movements', 'chest_tightness', 'palpitations', 'irregular_heartbeat', 'breathing_fast'],
    "rare_symptoms": [],
    "symptom_weights": {'anxiety_and_nervousness': 0.5, 'depression': 0.5, 'shortness_of_breath': 0.49, 'depressive_or_psychotic_symptoms': 0.68, 'dizziness': 0.53, 'insomnia': 0.52, 'abnormal_involuntary_movements': 0.52, 'chest_tightness': 0.51, 'palpitations': 0.5, 'irregular_heartbeat': 0.5, 'breathing_fast': 0.51}
}
disease_map["CSV_0524"] = {
    "name": "Parasitic Disease",
    "primary_symptoms": ['cough', 'retention_of_urine'],
    "secondary_symptoms": ['sharp_abdominal_pain', 'hand_or_finger_swelling', 'abnormal_appearing_skin', 'skin_rash'],
    "rare_symptoms": [],
    "symptom_weights": {'cough': 0.8, 'retention_of_urine': 0.92, 'sharp_abdominal_pain': 0.59, 'hand_or_finger_swelling': 0.62, 'abnormal_appearing_skin': 0.55, 'skin_rash': 0.51}
}
disease_map["CSV_0525"] = {
    "name": "Parathyroid Adenoma",
    "primary_symptoms": ['anxiety_and_nervousness', 'throat_feels_tight'],
    "secondary_symptoms": ['disturbance_of_memory', 'shoulder_pain'],
    "rare_symptoms": [],
    "symptom_weights": {'anxiety_and_nervousness': 0.78, 'throat_feels_tight': 1.0, 'disturbance_of_memory': 0.44, 'shoulder_pain': 0.56}
}
disease_map["CSV_0526"] = {
    "name": "Parkinson Disease",
    "primary_symptoms": [],
    "secondary_symptoms": ['dizziness', 'abnormal_involuntary_movements', 'difficulty_speaking', 'problems_with_movement', 'weakness', 'focal_weakness', 'disturbance_of_memory', 'leg_stiffness_or_tightness', 'stiffness_all_over'],
    "rare_symptoms": [],
    "symptom_weights": {'dizziness': 0.48, 'abnormal_involuntary_movements': 0.52, 'difficulty_speaking': 0.49, 'problems_with_movement': 0.45, 'weakness': 0.51, 'focal_weakness': 0.68, 'disturbance_of_memory': 0.47, 'leg_stiffness_or_tightness': 0.67, 'stiffness_all_over': 0.67}
}
disease_map["CSV_0527"] = {
    "name": "Paronychia",
    "primary_symptoms": ['sinus_congestion'],
    "secondary_symptoms": ['hand_or_finger_pain', 'hand_or_finger_swelling', 'abnormal_appearing_skin', 'foot_or_toe_pain', 'foot_or_toe_swelling', 'hand_or_finger_lump_or_mass', 'skin_on_leg_or_foot_looks_infected', 'skin_on_arm_or_hand_looks_infected'],
    "rare_symptoms": [],
    "symptom_weights": {'hand_or_finger_pain': 0.5, 'hand_or_finger_swelling': 0.69, 'abnormal_appearing_skin': 0.55, 'foot_or_toe_pain': 0.52, 'foot_or_toe_swelling': 0.55, 'hand_or_finger_lump_or_mass': 0.48, 'skin_on_leg_or_foot_looks_infected': 0.51, 'sinus_congestion': 0.76, 'skin_on_arm_or_hand_looks_infected': 0.46}
}
disease_map["CSV_0528"] = {
    "name": "Paroxysmal Supraventricular Tachycardia",
    "primary_symptoms": ['involuntary_urination'],
    "secondary_symptoms": ['shortness_of_breath', 'sharp_chest_pain', 'dizziness', 'chest_tightness', 'palpitations', 'irregular_heartbeat', 'weakness', 'increased_heart_rate'],
    "rare_symptoms": [],
    "symptom_weights": {'shortness_of_breath': 0.5, 'sharp_chest_pain': 0.54, 'dizziness': 0.5, 'chest_tightness': 0.51, 'palpitations': 0.5, 'irregular_heartbeat': 0.51, 'involuntary_urination': 0.8, 'weakness': 0.51, 'increased_heart_rate': 0.53}
}
disease_map["CSV_0529"] = {
    "name": "Paroxysmal Ventricular Tachycardia",
    "primary_symptoms": [],
    "secondary_symptoms": ['shortness_of_breath', 'sharp_chest_pain', 'dizziness', 'chest_tightness', 'irregular_heartbeat', 'fainting', 'weight_gain', 'decreased_heart_rate', 'increased_heart_rate', 'fatigue'],
    "rare_symptoms": [],
    "symptom_weights": {'shortness_of_breath': 0.48, 'sharp_chest_pain': 0.51, 'dizziness': 0.69, 'chest_tightness': 0.52, 'irregular_heartbeat': 0.48, 'fainting': 0.56, 'weight_gain': 0.49, 'decreased_heart_rate': 0.67, 'increased_heart_rate': 0.51, 'fatigue': 0.49}
}
disease_map["CSV_0530"] = {
    "name": "Pelvic Fistula",
    "primary_symptoms": ['dizziness', 'elbow_weakness'],
    "secondary_symptoms": ['vaginal_discharge'],
    "rare_symptoms": [],
    "symptom_weights": {'dizziness': 1.0, 'elbow_weakness': 1.0, 'vaginal_discharge': 0.6}
}
disease_map["CSV_0531"] = {
    "name": "Pelvic Inflammatory Disease",
    "primary_symptoms": [],
    "secondary_symptoms": ['suprapubic_pain', 'sharp_abdominal_pain', 'vomiting', 'nausea', 'painful_urination', 'lower_abdominal_pain', 'vaginal_discharge', 'intermenstrual_bleeding', 'back_pain', 'pelvic_pain', 'burning_abdominal_pain'],
    "rare_symptoms": [],
    "symptom_weights": {'suprapubic_pain': 0.49, 'sharp_abdominal_pain': 0.5, 'vomiting': 0.5, 'nausea': 0.51, 'painful_urination': 0.52, 'lower_abdominal_pain': 0.51, 'vaginal_discharge': 0.51, 'intermenstrual_bleeding': 0.52, 'back_pain': 0.51, 'pelvic_pain': 0.5, 'burning_abdominal_pain': 0.68}
}
disease_map["CSV_0532"] = {
    "name": "Pelvic Organ Prolapse",
    "primary_symptoms": ['blood_in_urine'],
    "secondary_symptoms": ['retention_of_urine', 'suprapubic_pain', 'involuntary_urination', 'frequent_urination', 'vaginal_discharge', 'intermenstrual_bleeding', 'vaginal_pain', 'symptoms_of_bladder'],
    "rare_symptoms": [],
    "symptom_weights": {'retention_of_urine': 0.5, 'suprapubic_pain': 0.52, 'involuntary_urination': 0.53, 'frequent_urination': 0.53, 'vaginal_discharge': 0.48, 'blood_in_urine': 0.75, 'intermenstrual_bleeding': 0.63, 'vaginal_pain': 0.52, 'symptoms_of_bladder': 0.5}
}
disease_map["CSV_0533"] = {
    "name": "Pemphigus",
    "primary_symptoms": ['hand_or_finger_pain', 'skin_lesion'],
    "secondary_symptoms": ['abnormal_appearing_skin'],
    "rare_symptoms": [],
    "symptom_weights": {'hand_or_finger_pain': 1.0, 'abnormal_appearing_skin': 0.57, 'skin_lesion': 1.0}
}
disease_map["CSV_0534"] = {
    "name": "Pericarditis",
    "primary_symptoms": ['chest_tightness', 'palpitations', 'sharp_abdominal_pain', 'lower_body_pain'],
    "secondary_symptoms": ['shortness_of_breath', 'sharp_chest_pain'],
    "rare_symptoms": [],
    "symptom_weights": {'shortness_of_breath': 0.63, 'sharp_chest_pain': 0.54, 'chest_tightness': 0.75, 'palpitations': 0.8, 'sharp_abdominal_pain': 0.7, 'lower_body_pain': 0.76}
}
disease_map["CSV_0535"] = {
    "name": "Peripheral Arterial Disease",
    "primary_symptoms": [],
    "secondary_symptoms": ['leg_pain', 'skin_lesion', 'foot_or_toe_pain', 'feeling_cold', 'leg_cramps_or_spasms', 'symptoms_of_the_kidneys', 'lymphedema', 'poor_circulation'],
    "rare_symptoms": [],
    "symptom_weights": {'leg_pain': 0.51, 'skin_lesion': 0.56, 'foot_or_toe_pain': 0.47, 'feeling_cold': 0.53, 'leg_cramps_or_spasms': 0.58, 'symptoms_of_the_kidneys': 0.65, 'lymphedema': 0.52, 'poor_circulation': 0.5}
}
disease_map["CSV_0536"] = {
    "name": "Peripheral Arterial Embolism",
    "primary_symptoms": ['knee_swelling', 'paresthesia'],
    "secondary_symptoms": ['leg_pain', 'abnormal_appearing_skin', 'leg_swelling', 'loss_of_sensation'],
    "rare_symptoms": [],
    "symptom_weights": {'leg_pain': 0.59, 'abnormal_appearing_skin': 0.7, 'knee_swelling': 0.73, 'leg_swelling': 0.56, 'loss_of_sensation': 0.59, 'paresthesia': 0.82}
}
disease_map["CSV_0537"] = {
    "name": "Peripheral Nerve Disorder",
    "primary_symptoms": [],
    "secondary_symptoms": ['dizziness', 'abnormal_involuntary_movements', 'leg_pain', 'arm_pain', 'back_pain', 'foot_or_toe_pain', 'problems_with_movement', 'loss_of_sensation', 'disturbance_of_memory', 'paresthesia', 'arm_weakness', 'leg_weakness'],
    "rare_symptoms": [],
    "symptom_weights": {'dizziness': 0.48, 'abnormal_involuntary_movements': 0.5, 'leg_pain': 0.5, 'arm_pain': 0.51, 'back_pain': 0.51, 'foot_or_toe_pain': 0.51, 'problems_with_movement': 0.49, 'loss_of_sensation': 0.51, 'disturbance_of_memory': 0.48, 'paresthesia': 0.5, 'arm_weakness': 0.5, 'leg_weakness': 0.52}
}
disease_map["CSV_0538"] = {
    "name": "Perirectal Infection",
    "primary_symptoms": ['skin_swelling', 'pain_in_testicles', 'skin_lesion'],
    "secondary_symptoms": ['swelling_of_scrotum', 'abnormal_appearing_skin', 'pain_of_the_anus'],
    "rare_symptoms": [],
    "symptom_weights": {'skin_swelling': 0.83, 'swelling_of_scrotum': 0.56, 'pain_in_testicles': 0.73, 'abnormal_appearing_skin': 0.53, 'skin_lesion': 0.78, 'pain_of_the_anus': 0.62}
}
disease_map["CSV_0539"] = {
    "name": "Peritonitis",
    "primary_symptoms": [],
    "secondary_symptoms": ['shortness_of_breath', 'groin_mass', 'sharp_abdominal_pain', 'vomiting', 'nausea', 'intermenstrual_bleeding', 'back_pain', 'side_pain'],
    "rare_symptoms": [],
    "symptom_weights": {'shortness_of_breath': 0.67, 'groin_mass': 0.52, 'sharp_abdominal_pain': 0.5, 'vomiting': 0.51, 'nausea': 0.48, 'intermenstrual_bleeding': 0.65, 'back_pain': 0.7, 'side_pain': 0.69}
}
disease_map["CSV_0540"] = {
    "name": "Peritonsillar Abscess",
    "primary_symptoms": ['headache', 'swollen_lymph_nodes', 'ear_pain'],
    "secondary_symptoms": ['sore_throat', 'throat_swelling', 'throat_feels_tight', 'difficulty_in_swallowing'],
    "rare_symptoms": [],
    "symptom_weights": {'sore_throat': 0.53, 'throat_swelling': 0.66, 'throat_feels_tight': 0.47, 'difficulty_in_swallowing': 0.52, 'headache': 0.71, 'swollen_lymph_nodes': 0.73, 'ear_pain': 0.76}
}
disease_map["CSV_0541"] = {
    "name": "Persistent Vomiting Of Unknown Cause",
    "primary_symptoms": ['dizziness', 'abnormal_involuntary_movements'],
    "secondary_symptoms": ['sharp_abdominal_pain', 'vomiting', 'nausea', 'diarrhea', 'fever'],
    "rare_symptoms": [],
    "symptom_weights": {'dizziness': 0.74, 'abnormal_involuntary_movements': 0.81, 'sharp_abdominal_pain': 0.52, 'vomiting': 0.47, 'nausea': 0.53, 'diarrhea': 0.47, 'fever': 0.53}
}
disease_map["CSV_0542"] = {
    "name": "Personality Disorder",
    "primary_symptoms": [],
    "secondary_symptoms": ['anxiety_and_nervousness', 'depression', 'depressive_or_psychotic_symptoms', 'insomnia', 'hostile_behavior', 'drug_abuse', 'excessive_anger', 'delusions_or_hallucinations', 'temper_problems', 'fears_and_phobias', 'low_self_esteem'],
    "rare_symptoms": [],
    "symptom_weights": {'anxiety_and_nervousness': 0.49, 'depression': 0.5, 'depressive_or_psychotic_symptoms': 0.49, 'insomnia': 0.51, 'hostile_behavior': 0.54, 'drug_abuse': 0.5, 'excessive_anger': 0.5, 'delusions_or_hallucinations': 0.52, 'temper_problems': 0.66, 'fears_and_phobias': 0.5, 'low_self_esteem': 0.51}
}
disease_map["CSV_0543"] = {
    "name": "Peyronie Disease",
    "primary_symptoms": ['mass_in_scrotum', 'impotence'],
    "secondary_symptoms": ['symptoms_of_prostate', 'penis_pain'],
    "rare_symptoms": ['emotional_symptoms'],
    "symptom_weights": {'emotional_symptoms': 0.38, 'mass_in_scrotum': 1.0, 'impotence': 0.76, 'symptoms_of_prostate': 0.43, 'penis_pain': 0.62}
}
disease_map["CSV_0544"] = {
    "name": "Pharyngitis",
    "primary_symptoms": ['hoarse_voice', 'cough', 'wheezing'],
    "secondary_symptoms": ['sore_throat', 'fever'],
    "rare_symptoms": [],
    "symptom_weights": {'hoarse_voice': 1.0, 'sore_throat': 0.58, 'cough': 0.74, 'wheezing': 0.79, 'fever': 0.47}
}
disease_map["CSV_0545"] = {
    "name": "Phimosis",
    "primary_symptoms": ['symptoms_of_the_scrotum_and_testes'],
    "secondary_symptoms": ['retention_of_urine', 'painful_urination', 'blood_in_urine', 'penis_pain', 'penis_redness'],
    "rare_symptoms": [],
    "symptom_weights": {'retention_of_urine': 0.53, 'symptoms_of_the_scrotum_and_testes': 0.85, 'painful_urination': 0.58, 'blood_in_urine': 0.58, 'penis_pain': 0.48, 'penis_redness': 0.47}
}
disease_map["CSV_0546"] = {
    "name": "Pilonidal Cyst",
    "primary_symptoms": ['irregular_appearing_scalp', 'pelvic_pain'],
    "secondary_symptoms": ['skin_swelling', 'skin_growth', 'pain_of_the_anus', 'bones_are_painful', 'ache_all_over', 'lower_body_pain'],
    "rare_symptoms": [],
    "symptom_weights": {'skin_swelling': 0.52, 'skin_growth': 0.54, 'irregular_appearing_scalp': 0.71, 'pain_of_the_anus': 0.51, 'pelvic_pain': 0.76, 'bones_are_painful': 0.68, 'ache_all_over': 0.51, 'lower_body_pain': 0.5}
}
disease_map["CSV_0547"] = {
    "name": "Pinguecula",
    "primary_symptoms": ['headache'],
    "secondary_symptoms": ['symptoms_of_eye', 'lacrimation', 'itching_of_scrotum'],
    "rare_symptoms": [],
    "symptom_weights": {'headache': 1.0, 'symptoms_of_eye': 0.67, 'lacrimation': 0.5, 'itching_of_scrotum': 0.67}
}
disease_map["CSV_0548"] = {
    "name": "Pinworm Infection",
    "primary_symptoms": ['retention_of_urine', 'constipation'],
    "secondary_symptoms": ['sharp_abdominal_pain', 'painful_urination', 'pain_of_the_anus', 'itching_of_the_anus'],
    "rare_symptoms": [],
    "symptom_weights": {'retention_of_urine': 0.84, 'sharp_abdominal_pain': 0.54, 'painful_urination': 0.55, 'pain_of_the_anus': 0.57, 'constipation': 0.85, 'itching_of_the_anus': 0.62}
}
disease_map["CSV_0549"] = {
    "name": "Pituitary Adenoma",
    "primary_symptoms": ['nausea', 'pain_in_eye'],
    "secondary_symptoms": ['headache', 'muscle_swelling'],
    "rare_symptoms": [],
    "symptom_weights": {'headache': 0.55, 'nausea': 0.9, 'pain_in_eye': 0.9, 'muscle_swelling': 0.52}
}
disease_map["CSV_0550"] = {
    "name": "Pituitary Disorder",
    "primary_symptoms": ['hot_flashes', 'pain_in_eye'],
    "secondary_symptoms": ['lack_of_growth', 'headache'],
    "rare_symptoms": [],
    "symptom_weights": {'lack_of_growth': 0.67, 'headache': 0.57, 'hot_flashes': 0.9, 'pain_in_eye': 0.83}
}
disease_map["CSV_0551"] = {
    "name": "Pityriasis Rosea",
    "primary_symptoms": ['vaginal_itching'],
    "secondary_symptoms": ['skin_swelling', 'abnormal_appearing_skin', 'itching_of_skin', 'warts', 'skin_rash'],
    "rare_symptoms": [],
    "symptom_weights": {'skin_swelling': 0.56, 'vaginal_itching': 0.85, 'abnormal_appearing_skin': 0.55, 'itching_of_skin': 0.55, 'warts': 0.52, 'skin_rash': 0.51}
}
disease_map["CSV_0552"] = {
    "name": "Placenta Previa",
    "primary_symptoms": ['involuntary_urination', 'pain_during_pregnancy', 'spotting_or_bleeding_during_pregnancy'],
    "secondary_symptoms": ['cramps_and_spasms'],
    "rare_symptoms": [],
    "symptom_weights": {'involuntary_urination': 0.89, 'pain_during_pregnancy': 0.78, 'spotting_or_bleeding_during_pregnancy': 0.89, 'cramps_and_spasms': 0.44}
}
disease_map["CSV_0553"] = {
    "name": "Placental Abruption",
    "primary_symptoms": ['emotional_symptoms', 'nausea', 'spotting_or_bleeding_during_pregnancy'],
    "secondary_symptoms": ['uterine_contractions'],
    "rare_symptoms": [],
    "symptom_weights": {'emotional_symptoms': 0.93, 'nausea': 1.0, 'spotting_or_bleeding_during_pregnancy': 0.79, 'uterine_contractions': 0.5}
}
disease_map["CSV_0554"] = {
    "name": "Plantar Fasciitis",
    "primary_symptoms": ['muscle_pain'],
    "secondary_symptoms": ['knee_pain', 'foot_or_toe_pain', 'ankle_pain', 'bones_are_painful', 'problems_with_movement', 'ankle_swelling'],
    "rare_symptoms": [],
    "symptom_weights": {'knee_pain': 0.57, 'foot_or_toe_pain': 0.57, 'ankle_pain': 0.52, 'bones_are_painful': 0.66, 'problems_with_movement': 0.67, 'muscle_pain': 0.78, 'ankle_swelling': 0.49}
}
disease_map["CSV_0555"] = {
    "name": "Pleural Effusion",
    "primary_symptoms": ['sharp_abdominal_pain'],
    "secondary_symptoms": ['shortness_of_breath', 'sharp_chest_pain', 'cough', 'back_pain', 'weakness', 'side_pain', 'difficulty_breathing', 'rib_pain', 'hurts_to_breath'],
    "rare_symptoms": [],
    "symptom_weights": {'shortness_of_breath': 0.46, 'sharp_chest_pain': 0.49, 'cough': 0.48, 'sharp_abdominal_pain': 0.76, 'back_pain': 0.51, 'weakness': 0.54, 'side_pain': 0.49, 'difficulty_breathing': 0.48, 'rib_pain': 0.53, 'hurts_to_breath': 0.52}
}
disease_map["CSV_0556"] = {
    "name": "Pneumoconiosis",
    "primary_symptoms": ['shortness_of_breath', 'dizziness'],
    "secondary_symptoms": ['cough', 'fever'],
    "rare_symptoms": [],
    "symptom_weights": {'shortness_of_breath': 0.86, 'dizziness': 1.0, 'cough': 0.57, 'fever': 0.57}
}
disease_map["CSV_0557"] = {
    "name": "Pneumothorax",
    "primary_symptoms": ['drug_abuse', 'shoulder_pain'],
    "secondary_symptoms": ['shortness_of_breath', 'sharp_chest_pain', 'cough', 'back_pain', 'side_pain', 'hurts_to_breath'],
    "rare_symptoms": [],
    "symptom_weights": {'shortness_of_breath': 0.55, 'sharp_chest_pain': 0.49, 'cough': 0.51, 'drug_abuse': 0.74, 'back_pain': 0.53, 'side_pain': 0.56, 'shoulder_pain': 0.74, 'hurts_to_breath': 0.53}
}
disease_map["CSV_0558"] = {
    "name": "Poisoning Due To Analgesics",
    "primary_symptoms": ['skin_swelling'],
    "secondary_symptoms": ['depression', 'depressive_or_psychotic_symptoms', 'abusing_alcohol', 'vomiting', 'problems_during_pregnancy'],
    "rare_symptoms": [],
    "symptom_weights": {'depression': 0.61, 'depressive_or_psychotic_symptoms': 0.55, 'skin_swelling': 0.88, 'abusing_alcohol': 0.56, 'vomiting': 0.55, 'problems_during_pregnancy': 0.48}
}
disease_map["CSV_0559"] = {
    "name": "Poisoning Due To Anticonvulsants",
    "primary_symptoms": ['depression', 'difficulty_speaking'],
    "secondary_symptoms": ['dizziness', 'problems_with_movement'],
    "rare_symptoms": [],
    "symptom_weights": {'depression': 0.83, 'dizziness': 0.59, 'difficulty_speaking': 0.85, 'problems_with_movement': 0.68}
}
disease_map["CSV_0560"] = {
    "name": "Poisoning Due To Antidepressants",
    "primary_symptoms": ['abusing_alcohol', 'drug_abuse'],
    "secondary_symptoms": ['depression', 'emotional_symptoms'],
    "rare_symptoms": [],
    "symptom_weights": {'depression': 0.62, 'emotional_symptoms': 0.62, 'abusing_alcohol': 0.93, 'drug_abuse': 0.9}
}
disease_map["CSV_0561"] = {
    "name": "Poisoning Due To Antihypertensives",
    "primary_symptoms": ['depressive_or_psychotic_symptoms', 'sharp_abdominal_pain', 'weakness'],
    "secondary_symptoms": [],
    "rare_symptoms": [],
    "symptom_weights": {'depressive_or_psychotic_symptoms': 0.82, 'sharp_abdominal_pain': 1.0, 'weakness': 0.82}
}
disease_map["CSV_0562"] = {
    "name": "Poisoning Due To Antimicrobial Drugs",
    "primary_symptoms": ['shortness_of_breath', 'abnormal_involuntary_movements'],
    "secondary_symptoms": ['peripheral_edema', 'problems_with_movement', 'allergic_reaction', 'skin_rash'],
    "rare_symptoms": [],
    "symptom_weights": {'shortness_of_breath': 0.88, 'abnormal_involuntary_movements': 0.88, 'peripheral_edema': 0.53, 'problems_with_movement': 0.55, 'allergic_reaction': 0.47, 'skin_rash': 0.59}
}
disease_map["CSV_0563"] = {
    "name": "Poisoning Due To Antipsychotics",
    "primary_symptoms": ['anxiety_and_nervousness', 'sharp_chest_pain'],
    "secondary_symptoms": ['delusions_or_hallucinations'],
    "rare_symptoms": [],
    "symptom_weights": {'anxiety_and_nervousness': 1.0, 'sharp_chest_pain': 1.0, 'delusions_or_hallucinations': 0.6}
}
disease_map["CSV_0564"] = {
    "name": "Poisoning Due To Ethylene Glycol",
    "primary_symptoms": ['depression', 'depressive_or_psychotic_symptoms'],
    "secondary_symptoms": ['abusing_alcohol', 'fainting'],
    "rare_symptoms": [],
    "symptom_weights": {'depression': 1.0, 'depressive_or_psychotic_symptoms': 0.88, 'abusing_alcohol': 0.42, 'fainting': 0.54}
}
disease_map["CSV_0565"] = {
    "name": "Poisoning Due To Gas",
    "primary_symptoms": ['sharp_chest_pain', 'dizziness', 'headache'],
    "secondary_symptoms": ['shortness_of_breath', 'cough', 'wheezing', 'drainage_in_throat'],
    "rare_symptoms": [],
    "symptom_weights": {'shortness_of_breath': 0.58, 'sharp_chest_pain': 0.77, 'dizziness': 0.85, 'cough': 0.56, 'headache': 0.77, 'wheezing': 0.66, 'drainage_in_throat': 0.49}
}
disease_map["CSV_0566"] = {
    "name": "Poisoning Due To Opioids",
    "primary_symptoms": ['depressive_or_psychotic_symptoms', 'dizziness', 'difficulty_speaking', 'drug_abuse'],
    "secondary_symptoms": [],
    "rare_symptoms": [],
    "symptom_weights": {'depressive_or_psychotic_symptoms': 0.78, 'dizziness': 1.0, 'difficulty_speaking': 1.0, 'drug_abuse': 0.78}
}
disease_map["CSV_0567"] = {
    "name": "Poisoning Due To Sedatives",
    "primary_symptoms": ['hostile_behavior'],
    "secondary_symptoms": ['depression', 'depressive_or_psychotic_symptoms', 'insomnia', 'drug_abuse', 'sleepiness'],
    "rare_symptoms": [],
    "symptom_weights": {'depression': 0.6, 'depressive_or_psychotic_symptoms': 0.54, 'insomnia': 0.7, 'hostile_behavior': 0.81, 'drug_abuse': 0.68, 'sleepiness': 0.47}
}
disease_map["CSV_0568"] = {
    "name": "Polycystic Kidney Disease",
    "primary_symptoms": ['retention_of_urine'],
    "secondary_symptoms": ['sharp_abdominal_pain', 'blood_in_urine', 'skin_growth', 'back_pain', 'low_back_pain', 'side_pain', 'kidney_mass'],
    "rare_symptoms": [],
    "symptom_weights": {'retention_of_urine': 0.9, 'sharp_abdominal_pain': 0.55, 'blood_in_urine': 0.55, 'skin_growth': 0.49, 'back_pain': 0.58, 'low_back_pain': 0.54, 'side_pain': 0.61, 'kidney_mass': 0.53}
}
disease_map["CSV_0569"] = {
    "name": "Polycystic Ovarian Syndrome (Pcos)",
    "primary_symptoms": ['hot_flashes'],
    "secondary_symptoms": ['intermenstrual_bleeding', 'pelvic_pain', 'weight_gain', 'absence_of_menstruation', 'long_menstrual_periods', 'unpredictable_menstruation', 'infertility'],
    "rare_symptoms": [],
    "symptom_weights": {'hot_flashes': 0.83, 'intermenstrual_bleeding': 0.49, 'pelvic_pain': 0.5, 'weight_gain': 0.53, 'absence_of_menstruation': 0.7, 'long_menstrual_periods': 0.54, 'unpredictable_menstruation': 0.54, 'infertility': 0.53}
}
disease_map["CSV_0570"] = {
    "name": "Polycythemia Vera",
    "primary_symptoms": ['dizziness', 'symptoms_of_eye', 'weight_gain'],
    "secondary_symptoms": ['headache', 'fatigue'],
    "rare_symptoms": [],
    "symptom_weights": {'dizziness': 0.84, 'headache': 0.59, 'symptoms_of_eye': 0.8, 'weight_gain': 0.88, 'fatigue': 0.61}
}
disease_map["CSV_0571"] = {
    "name": "Polymyalgia Rheumatica",
    "primary_symptoms": ['irregular_heartbeat', 'difficulty_in_swallowing', 'leg_pain'],
    "secondary_symptoms": ['sharp_chest_pain', 'shoulder_pain', 'fatigue'],
    "rare_symptoms": [],
    "symptom_weights": {'sharp_chest_pain': 0.58, 'irregular_heartbeat': 0.77, 'difficulty_in_swallowing': 0.77, 'leg_pain': 0.74, 'shoulder_pain': 0.53, 'fatigue': 0.52}
}
disease_map["CSV_0572"] = {
    "name": "Post-Traumatic Stress Disorder (Ptsd)",
    "primary_symptoms": ['hostile_behavior'],
    "secondary_symptoms": ['anxiety_and_nervousness', 'depression', 'depressive_or_psychotic_symptoms', 'insomnia', 'abusing_alcohol', 'drug_abuse', 'excessive_anger', 'delusions_or_hallucinations', 'temper_problems'],
    "rare_symptoms": [],
    "symptom_weights": {'anxiety_and_nervousness': 0.46, 'depression': 0.49, 'depressive_or_psychotic_symptoms': 0.48, 'insomnia': 0.52, 'abusing_alcohol': 0.5, 'hostile_behavior': 0.76, 'drug_abuse': 0.5, 'excessive_anger': 0.49, 'delusions_or_hallucinations': 0.5, 'temper_problems': 0.53}
}
disease_map["CSV_0573"] = {
    "name": "Postoperative Infection",
    "primary_symptoms": ['skin_swelling', 'jaw_swelling'],
    "secondary_symptoms": ['sharp_abdominal_pain', 'abnormal_appearing_skin', 'fever', 'skin_on_leg_or_foot_looks_infected'],
    "rare_symptoms": [],
    "symptom_weights": {'skin_swelling': 0.78, 'sharp_abdominal_pain': 0.48, 'abnormal_appearing_skin': 0.52, 'jaw_swelling': 0.85, 'fever': 0.53, 'skin_on_leg_or_foot_looks_infected': 0.55}
}
disease_map["CSV_0574"] = {
    "name": "Postpartum Depression",
    "primary_symptoms": [],
    "secondary_symptoms": ['anxiety_and_nervousness', 'depression', 'depressive_or_psychotic_symptoms', 'drug_abuse', 'intermenstrual_bleeding', 'pain_during_pregnancy', 'excessive_anger', 'problems_during_pregnancy', 'delusions_or_hallucinations'],
    "rare_symptoms": [],
    "symptom_weights": {'anxiety_and_nervousness': 0.51, 'depression': 0.54, 'depressive_or_psychotic_symptoms': 0.51, 'drug_abuse': 0.68, 'intermenstrual_bleeding': 0.51, 'pain_during_pregnancy': 0.53, 'excessive_anger': 0.49, 'problems_during_pregnancy': 0.68, 'delusions_or_hallucinations': 0.67}
}
disease_map["CSV_0575"] = {
    "name": "Preeclampsia",
    "primary_symptoms": [],
    "secondary_symptoms": ['sharp_abdominal_pain', 'headache', 'lower_abdominal_pain', 'pain_during_pregnancy', 'vaginal_redness', 'spots_or_clouds_in_vision', 'problems_during_pregnancy', 'recent_pregnancy', 'uterine_contractions'],
    "rare_symptoms": [],
    "symptom_weights": {'sharp_abdominal_pain': 0.53, 'headache': 0.53, 'lower_abdominal_pain': 0.5, 'pain_during_pregnancy': 0.58, 'vaginal_redness': 0.67, 'spots_or_clouds_in_vision': 0.5, 'problems_during_pregnancy': 0.53, 'recent_pregnancy': 0.47, 'uterine_contractions': 0.53}
}
disease_map["CSV_0576"] = {
    "name": "Pregnancy",
    "primary_symptoms": [],
    "secondary_symptoms": ['pain_during_pregnancy', 'problems_during_pregnancy', 'spotting_or_bleeding_during_pregnancy', 'cramps_and_spasms', 'uterine_contractions'],
    "rare_symptoms": ['pelvic_pressure'],
    "symptom_weights": {'pain_during_pregnancy': 0.62, 'problems_during_pregnancy': 0.69, 'spotting_or_bleeding_during_pregnancy': 0.62, 'cramps_and_spasms': 0.69, 'uterine_contractions': 0.62, 'pelvic_pressure': 0.38}
}
disease_map["CSV_0577"] = {
    "name": "Premature Atrial Contractions (Pacs)",
    "primary_symptoms": ['shortness_of_breath', 'dizziness', 'fainting'],
    "secondary_symptoms": ['palpitations', 'irregular_heartbeat', 'fatigue', 'muscle_swelling'],
    "rare_symptoms": [],
    "symptom_weights": {'shortness_of_breath': 0.75, 'dizziness': 0.73, 'palpitations': 0.57, 'irregular_heartbeat': 0.53, 'fainting': 0.73, 'fatigue': 0.52, 'muscle_swelling': 0.67}
}
disease_map["CSV_0578"] = {
    "name": "Premature Ovarian Failure",
    "primary_symptoms": ['lack_of_growth', 'absence_of_menstruation'],
    "secondary_symptoms": ['pelvic_pain', 'weight_gain', 'infertility'],
    "rare_symptoms": [],
    "symptom_weights": {'lack_of_growth': 0.94, 'pelvic_pain': 0.46, 'weight_gain': 0.65, 'absence_of_menstruation': 0.71, 'infertility': 0.56}
}
disease_map["CSV_0579"] = {
    "name": "Premature Rupture Of Amniotic Membrane",
    "primary_symptoms": ['elbow_weakness', 'sharp_abdominal_pain', 'uterine_contractions'],
    "secondary_symptoms": [],
    "rare_symptoms": [],
    "symptom_weights": {'elbow_weakness': 0.89, 'sharp_abdominal_pain': 1.0, 'uterine_contractions': 1.0}
}
disease_map["CSV_0580"] = {
    "name": "Premature Ventricular Contractions (Pvcs)",
    "primary_symptoms": ['shortness_of_breath'],
    "secondary_symptoms": ['sharp_chest_pain', 'chest_tightness', 'palpitations', 'irregular_heartbeat', 'fainting', 'impotence', 'sleepiness'],
    "rare_symptoms": [],
    "symptom_weights": {'shortness_of_breath': 0.78, 'sharp_chest_pain': 0.54, 'chest_tightness': 0.55, 'palpitations': 0.55, 'irregular_heartbeat': 0.54, 'fainting': 0.52, 'impotence': 0.68, 'sleepiness': 0.67}
}
disease_map["CSV_0581"] = {
    "name": "Premenstrual Tension Syndrome",
    "primary_symptoms": ['depressive_or_psychotic_symptoms', 'lower_abdominal_pain', 'back_pain'],
    "secondary_symptoms": ['headache', 'unpredictable_menstruation', 'premenstrual_tension_or_irritability'],
    "rare_symptoms": [],
    "symptom_weights": {'depressive_or_psychotic_symptoms': 0.79, 'headache': 0.54, 'lower_abdominal_pain': 0.84, 'back_pain': 0.72, 'unpredictable_menstruation': 0.53, 'premenstrual_tension_or_irritability': 0.45}
}
disease_map["CSV_0582"] = {
    "name": "Presbyacusis",
    "primary_symptoms": ['emotional_symptoms'],
    "secondary_symptoms": ['dizziness', 'diminished_hearing', 'ear_pain', 'ringing_in_ear'],
    "rare_symptoms": [],
    "symptom_weights": {'dizziness': 0.55, 'diminished_hearing': 0.51, 'emotional_symptoms': 0.87, 'ear_pain': 0.67, 'ringing_in_ear': 0.47}
}
disease_map["CSV_0583"] = {
    "name": "Presbyopia",
    "primary_symptoms": ['pain_in_eye', 'abnormal_movement_of_eyelid', 'foreign_body_sensation_in_eye'],
    "secondary_symptoms": ['difficulty_speaking', 'diminished_vision', 'symptoms_of_eye', 'spots_or_clouds_in_vision'],
    "rare_symptoms": [],
    "symptom_weights": {'difficulty_speaking': 0.68, 'diminished_vision': 0.59, 'symptoms_of_eye': 0.61, 'pain_in_eye': 0.82, 'abnormal_movement_of_eyelid': 0.75, 'foreign_body_sensation_in_eye': 0.71, 'spots_or_clouds_in_vision': 0.6}
}
disease_map["CSV_0584"] = {
    "name": "Priapism",
    "primary_symptoms": ['abusing_alcohol', 'penis_pain'],
    "secondary_symptoms": ['elbow_weakness', 'painful_urination'],
    "rare_symptoms": [],
    "symptom_weights": {'elbow_weakness': 0.5, 'abusing_alcohol': 1.0, 'painful_urination': 0.67, 'penis_pain': 0.83}
}
disease_map["CSV_0585"] = {
    "name": "Primary Immunodeficiency",
    "primary_symptoms": ['arm_stiffness_or_tightness', 'decreased_appetite', 'fatigue'],
    "secondary_symptoms": ['cough', 'frontal_headache'],
    "rare_symptoms": [],
    "symptom_weights": {'cough': 0.64, 'arm_stiffness_or_tightness': 0.86, 'frontal_headache': 0.64, 'decreased_appetite': 0.86, 'fatigue': 0.75}
}
disease_map["CSV_0586"] = {
    "name": "Primary Insomnia",
    "primary_symptoms": ['anxiety_and_nervousness', 'sleepiness'],
    "secondary_symptoms": ['insomnia', 'abnormal_involuntary_movements', 'fatigue', 'delusions_or_hallucinations', 'abnormal_breathing_sounds'],
    "rare_symptoms": [],
    "symptom_weights": {'anxiety_and_nervousness': 0.87, 'insomnia': 0.56, 'abnormal_involuntary_movements': 0.69, 'fatigue': 0.51, 'delusions_or_hallucinations': 0.51, 'sleepiness': 0.7, 'abnormal_breathing_sounds': 0.55}
}
disease_map["CSV_0587"] = {
    "name": "Primary Kidney Disease",
    "primary_symptoms": ['lack_of_growth'],
    "secondary_symptoms": ['blood_in_urine', 'impotence', 'peripheral_edema', 'symptoms_of_the_kidneys'],
    "rare_symptoms": [],
    "symptom_weights": {'lack_of_growth': 0.97, 'blood_in_urine': 0.5, 'impotence': 0.53, 'peripheral_edema': 0.65, 'symptoms_of_the_kidneys': 0.5}
}
disease_map["CSV_0588"] = {
    "name": "Primary Thrombocythemia",
    "primary_symptoms": ['dizziness', 'flatulence', 'fatigue'],
    "secondary_symptoms": [],
    "rare_symptoms": [],
    "symptom_weights": {'dizziness': 1.0, 'flatulence': 1.0, 'fatigue': 1.0}
}
disease_map["CSV_0589"] = {
    "name": "Problem During Pregnancy",
    "primary_symptoms": [],
    "secondary_symptoms": ['sharp_abdominal_pain', 'vomiting', 'headache', 'nausea', 'lower_abdominal_pain', 'back_pain', 'pain_during_pregnancy', 'pelvic_pain', 'problems_during_pregnancy', 'spotting_or_bleeding_during_pregnancy', 'cramps_and_spasms'],
    "rare_symptoms": [],
    "symptom_weights": {'sharp_abdominal_pain': 0.49, 'vomiting': 0.5, 'headache': 0.49, 'nausea': 0.51, 'lower_abdominal_pain': 0.53, 'back_pain': 0.52, 'pain_during_pregnancy': 0.51, 'pelvic_pain': 0.66, 'problems_during_pregnancy': 0.53, 'spotting_or_bleeding_during_pregnancy': 0.52, 'cramps_and_spasms': 0.5}
}
disease_map["CSV_0590"] = {
    "name": "Prostate Cancer",
    "primary_symptoms": ['involuntary_urination'],
    "secondary_symptoms": ['retention_of_urine', 'pain_during_intercourse', 'blood_in_urine', 'impotence', 'symptoms_of_prostate', 'flushing', 'excessive_urination_at_night'],
    "rare_symptoms": [],
    "symptom_weights": {'retention_of_urine': 0.67, 'involuntary_urination': 0.73, 'pain_during_intercourse': 0.52, 'blood_in_urine': 0.56, 'impotence': 0.61, 'symptoms_of_prostate': 0.52, 'flushing': 0.68, 'excessive_urination_at_night': 0.51}
}
disease_map["CSV_0591"] = {
    "name": "Prostatitis",
    "primary_symptoms": [],
    "secondary_symptoms": ['retention_of_urine', 'sharp_abdominal_pain', 'painful_urination', 'frequent_urination', 'lower_abdominal_pain', 'blood_in_urine', 'back_pain', 'impotence', 'fever', 'chills'],
    "rare_symptoms": [],
    "symptom_weights": {'retention_of_urine': 0.66, 'sharp_abdominal_pain': 0.67, 'painful_urination': 0.5, 'frequent_urination': 0.52, 'lower_abdominal_pain': 0.51, 'blood_in_urine': 0.54, 'back_pain': 0.48, 'impotence': 0.55, 'fever': 0.51, 'chills': 0.51}
}
disease_map["CSV_0592"] = {
    "name": "Protein Deficiency",
    "primary_symptoms": ['depression', 'vomiting', 'smoking_problems'],
    "secondary_symptoms": ['nausea', 'weakness'],
    "rare_symptoms": [],
    "symptom_weights": {'depression': 0.91, 'vomiting': 0.81, 'nausea': 0.59, 'smoking_problems': 0.75, 'weakness': 0.67}
}
disease_map["CSV_0593"] = {
    "name": "Pseudohypoparathyroidism",
    "primary_symptoms": ['leg_pain', 'wrist_pain'],
    "secondary_symptoms": ['elbow_weakness', 'knee_pain'],
    "rare_symptoms": [],
    "symptom_weights": {'leg_pain': 1.0, 'elbow_weakness': 0.5, 'wrist_pain': 0.83, 'knee_pain': 0.67}
}
disease_map["CSV_0594"] = {
    "name": "Pseudotumor Cerebri",
    "primary_symptoms": ['abnormal_involuntary_movements', 'pain_in_eye'],
    "secondary_symptoms": ['dizziness', 'headache', 'diminished_vision'],
    "rare_symptoms": [],
    "symptom_weights": {'dizziness': 0.52, 'abnormal_involuntary_movements': 0.96, 'headache': 0.52, 'diminished_vision': 0.6, 'pain_in_eye': 0.77}
}
disease_map["CSV_0595"] = {
    "name": "Psoriasis",
    "primary_symptoms": [],
    "secondary_symptoms": ['skin_swelling', 'abnormal_appearing_skin', 'skin_lesion', 'skin_growth', 'irregular_appearing_scalp', 'skin_moles', 'joint_pain', 'itching_of_skin', 'skin_dryness,_peeling,_scaliness,_or_roughness', 'itchy_scalp', 'skin_rash'],
    "rare_symptoms": [],
    "symptom_weights": {'skin_swelling': 0.65, 'abnormal_appearing_skin': 0.5, 'skin_lesion': 0.49, 'skin_growth': 0.51, 'irregular_appearing_scalp': 0.54, 'skin_moles': 0.51, 'joint_pain': 0.49, 'itching_of_skin': 0.5, 'skin_dryness,_peeling,_scaliness,_or_roughness': 0.5, 'itchy_scalp': 0.51, 'skin_rash': 0.55}
}
disease_map["CSV_0596"] = {
    "name": "Psychosexual Disorder",
    "primary_symptoms": ['involuntary_urination'],
    "secondary_symptoms": ['depression', 'pain_during_intercourse', 'impotence', 'fatigue', 'loss_of_sex_drive', 'premature_ejaculation'],
    "rare_symptoms": [],
    "symptom_weights": {'depression': 0.62, 'involuntary_urination': 0.83, 'pain_during_intercourse': 0.49, 'impotence': 0.49, 'fatigue': 0.51, 'loss_of_sex_drive': 0.5, 'premature_ejaculation': 0.52}
}
disease_map["CSV_0597"] = {
    "name": "Psychotic Disorder",
    "primary_symptoms": [],
    "secondary_symptoms": ['anxiety_and_nervousness', 'depression', 'depressive_or_psychotic_symptoms', 'insomnia', 'abusing_alcohol', 'hostile_behavior', 'excessive_anger', 'delusions_or_hallucinations', 'temper_problems', 'fears_and_phobias', 'hysterical_behavior'],
    "rare_symptoms": [],
    "symptom_weights": {'anxiety_and_nervousness': 0.48, 'depression': 0.51, 'depressive_or_psychotic_symptoms': 0.5, 'insomnia': 0.69, 'abusing_alcohol': 0.5, 'hostile_behavior': 0.54, 'excessive_anger': 0.5, 'delusions_or_hallucinations': 0.52, 'temper_problems': 0.51, 'fears_and_phobias': 0.52, 'hysterical_behavior': 0.5}
}
disease_map["CSV_0598"] = {
    "name": "Pterygium",
    "primary_symptoms": ['acne_or_pimples', 'symptoms_of_eye', 'lacrimation'],
    "secondary_symptoms": ['diminished_vision', 'foreign_body_sensation_in_eye', 'spots_or_clouds_in_vision', 'eye_redness'],
    "rare_symptoms": [],
    "symptom_weights": {'acne_or_pimples': 0.78, 'diminished_vision': 0.52, 'symptoms_of_eye': 0.79, 'foreign_body_sensation_in_eye': 0.7, 'spots_or_clouds_in_vision': 0.56, 'eye_redness': 0.57, 'lacrimation': 0.73}
}
disease_map["CSV_0599"] = {
    "name": "Pulmonary Congestion",
    "primary_symptoms": ['cough'],
    "secondary_symptoms": ['shortness_of_breath', 'sharp_chest_pain', 'chest_tightness', 'nasal_congestion', 'leg_swelling', 'weakness', 'decreased_heart_rate', 'fever'],
    "rare_symptoms": [],
    "symptom_weights": {'shortness_of_breath': 0.51, 'sharp_chest_pain': 0.54, 'chest_tightness': 0.68, 'cough': 0.71, 'nasal_congestion': 0.53, 'leg_swelling': 0.68, 'weakness': 0.49, 'decreased_heart_rate': 0.48, 'fever': 0.48}
}
disease_map["CSV_0600"] = {
    "name": "Pulmonary Embolism",
    "primary_symptoms": [],
    "secondary_symptoms": ['shortness_of_breath', 'sharp_chest_pain', 'chest_tightness', 'cough', 'leg_pain', 'leg_swelling', 'weakness', 'side_pain', 'difficulty_breathing', 'hemoptysis', 'sweating'],
    "rare_symptoms": [],
    "symptom_weights": {'shortness_of_breath': 0.51, 'sharp_chest_pain': 0.53, 'chest_tightness': 0.49, 'cough': 0.52, 'leg_pain': 0.69, 'leg_swelling': 0.51, 'weakness': 0.5, 'side_pain': 0.51, 'difficulty_breathing': 0.51, 'hemoptysis': 0.5, 'sweating': 0.51}
}
disease_map["CSV_0601"] = {
    "name": "Pulmonary Eosinophilia",
    "primary_symptoms": ['dizziness', 'paresthesia'],
    "secondary_symptoms": ['shortness_of_breath', 'sharp_chest_pain', 'cough', 'nasal_congestion', 'fever'],
    "rare_symptoms": [],
    "symptom_weights": {'shortness_of_breath': 0.5, 'sharp_chest_pain': 0.51, 'dizziness': 0.76, 'cough': 0.56, 'nasal_congestion': 0.52, 'paresthesia': 0.82, 'fever': 0.5}
}
disease_map["CSV_0602"] = {
    "name": "Pulmonary Fibrosis",
    "primary_symptoms": ['chest_tightness'],
    "secondary_symptoms": ['shortness_of_breath', 'sharp_chest_pain', 'cough', 'fainting', 'fever', 'difficulty_breathing'],
    "rare_symptoms": [],
    "symptom_weights": {'shortness_of_breath': 0.57, 'sharp_chest_pain': 0.57, 'chest_tightness': 0.86, 'cough': 0.54, 'fainting': 0.56, 'fever': 0.58, 'difficulty_breathing': 0.49}
}
disease_map["CSV_0603"] = {
    "name": "Pulmonary Hypertension",
    "primary_symptoms": ['feeling_ill'],
    "secondary_symptoms": ['shortness_of_breath', 'sharp_chest_pain', 'palpitations', 'cough', 'difficulty_breathing', 'fatigue', 'hemoptysis', 'apnea'],
    "rare_symptoms": [],
    "symptom_weights": {'shortness_of_breath': 0.52, 'sharp_chest_pain': 0.52, 'palpitations': 0.52, 'cough': 0.49, 'feeling_ill': 0.76, 'difficulty_breathing': 0.52, 'fatigue': 0.51, 'hemoptysis': 0.5, 'apnea': 0.66}
}
disease_map["CSV_0604"] = {
    "name": "Pulmonic Valve Disease",
    "primary_symptoms": ['shortness_of_breath', 'emotional_symptoms'],
    "secondary_symptoms": [],
    "rare_symptoms": [],
    "symptom_weights": {'shortness_of_breath': 1.0, 'emotional_symptoms': 1.0}
}
disease_map["CSV_0605"] = {
    "name": "Pyelonephritis",
    "primary_symptoms": [],
    "secondary_symptoms": ['suprapubic_pain', 'sharp_abdominal_pain', 'vomiting', 'nausea', 'painful_urination', 'frequent_urination', 'lower_abdominal_pain', 'blood_in_urine', 'back_pain', 'low_back_pain', 'side_pain'],
    "rare_symptoms": [],
    "symptom_weights": {'suprapubic_pain': 0.48, 'sharp_abdominal_pain': 0.68, 'vomiting': 0.5, 'nausea': 0.51, 'painful_urination': 0.51, 'frequent_urination': 0.52, 'lower_abdominal_pain': 0.51, 'blood_in_urine': 0.5, 'back_pain': 0.47, 'low_back_pain': 0.52, 'side_pain': 0.52}
}
disease_map["CSV_0606"] = {
    "name": "Pyloric Stenosis",
    "primary_symptoms": ['cough', 'arm_stiffness_or_tightness'],
    "secondary_symptoms": ['vomiting'],
    "rare_symptoms": [],
    "symptom_weights": {'cough': 0.75, 'vomiting': 0.69, 'arm_stiffness_or_tightness': 0.94}
}
disease_map["CSV_0607"] = {
    "name": "Pyogenic Skin Infection",
    "primary_symptoms": [],
    "secondary_symptoms": ['skin_swelling', 'leg_pain', 'hand_or_finger_pain', 'hand_or_finger_swelling', 'abnormal_appearing_skin', 'skin_lesion', 'peripheral_edema', 'foot_or_toe_pain', 'leg_swelling', 'foot_or_toe_swelling', 'skin_rash'],
    "rare_symptoms": [],
    "symptom_weights": {'skin_swelling': 0.49, 'leg_pain': 0.5, 'hand_or_finger_pain': 0.49, 'hand_or_finger_swelling': 0.51, 'abnormal_appearing_skin': 0.53, 'skin_lesion': 0.49, 'peripheral_edema': 0.52, 'foot_or_toe_pain': 0.66, 'leg_swelling': 0.52, 'foot_or_toe_swelling': 0.5, 'skin_rash': 0.51}
}
disease_map["CSV_0608"] = {
    "name": "Raynaud Disease",
    "primary_symptoms": ['hand_or_finger_pain', 'hand_or_finger_swelling'],
    "secondary_symptoms": ['loss_of_sensation'],
    "rare_symptoms": [],
    "symptom_weights": {'hand_or_finger_pain': 1.0, 'hand_or_finger_swelling': 0.92, 'loss_of_sensation': 0.58}
}
disease_map["CSV_0609"] = {
    "name": "Reactive Arthritis",
    "primary_symptoms": ['hip_pain', 'knee_lump_or_mass'],
    "secondary_symptoms": [],
    "rare_symptoms": [],
    "symptom_weights": {'hip_pain': 1.0, 'knee_lump_or_mass': 1.0}
}
disease_map["CSV_0610"] = {
    "name": "Rectal Disorder",
    "primary_symptoms": [],
    "secondary_symptoms": ['blood_in_stool', 'sharp_abdominal_pain', 'diarrhea', 'pain_of_the_anus', 'burning_abdominal_pain', 'heartburn', 'cramps_and_spasms', 'melena', 'rectal_bleeding', 'constipation', 'itching_of_the_anus'],
    "rare_symptoms": [],
    "symptom_weights": {'blood_in_stool': 0.49, 'sharp_abdominal_pain': 0.52, 'diarrhea': 0.49, 'pain_of_the_anus': 0.53, 'burning_abdominal_pain': 0.52, 'heartburn': 0.67, 'cramps_and_spasms': 0.5, 'melena': 0.48, 'rectal_bleeding': 0.51, 'constipation': 0.52, 'itching_of_the_anus': 0.47}
}
disease_map["CSV_0611"] = {
    "name": "Restless Leg Syndrome",
    "primary_symptoms": ['insomnia'],
    "secondary_symptoms": ['depression', 'abnormal_involuntary_movements', 'leg_pain', 'headache', 'fatigue', 'sleepiness', 'apnea'],
    "rare_symptoms": [],
    "symptom_weights": {'depression': 0.5, 'insomnia': 0.81, 'abnormal_involuntary_movements': 0.51, 'leg_pain': 0.5, 'headache': 0.53, 'fatigue': 0.67, 'sleepiness': 0.5, 'apnea': 0.48}
}
disease_map["CSV_0612"] = {
    "name": "Retinal Detachment",
    "primary_symptoms": ['double_vision'],
    "secondary_symptoms": ['diminished_vision', 'symptoms_of_eye', 'pain_in_eye', 'spots_or_clouds_in_vision', 'lacrimation', 'itchiness_of_eye', 'blindness'],
    "rare_symptoms": [],
    "symptom_weights": {'diminished_vision': 0.5, 'double_vision': 0.81, 'symptoms_of_eye': 0.5, 'pain_in_eye': 0.53, 'spots_or_clouds_in_vision': 0.52, 'lacrimation': 0.68, 'itchiness_of_eye': 0.56, 'blindness': 0.5}
}
disease_map["CSV_0613"] = {
    "name": "Retinopathy Due To High Blood Pressure",
    "primary_symptoms": ['pus_draining_from_ear', 'foreign_body_sensation_in_eye'],
    "secondary_symptoms": ['diminished_vision', 'symptoms_of_eye', 'pain_in_eye', 'spots_or_clouds_in_vision'],
    "rare_symptoms": [],
    "symptom_weights": {'pus_draining_from_ear': 0.85, 'diminished_vision': 0.56, 'symptoms_of_eye': 0.55, 'pain_in_eye': 0.63, 'foreign_body_sensation_in_eye': 0.71, 'spots_or_clouds_in_vision': 0.5}
}
disease_map["CSV_0614"] = {
    "name": "Rhabdomyolysis",
    "primary_symptoms": ['leg_pain'],
    "secondary_symptoms": ['depressive_or_psychotic_symptoms', 'sharp_chest_pain', 'arm_pain'],
    "rare_symptoms": ['hoarse_voice'],
    "symptom_weights": {'depressive_or_psychotic_symptoms': 0.56, 'sharp_chest_pain': 0.5, 'hoarse_voice': 0.38, 'leg_pain': 1.0, 'arm_pain': 0.62}
}
disease_map["CSV_0615"] = {
    "name": "Rheumatic Fever",
    "primary_symptoms": ['knee_lump_or_mass', 'itchiness_of_eye'],
    "secondary_symptoms": [],
    "rare_symptoms": [],
    "symptom_weights": {'knee_lump_or_mass': 1.0, 'itchiness_of_eye': 1.0}
}
disease_map["CSV_0616"] = {
    "name": "Rheumatoid Arthritis",
    "primary_symptoms": [],
    "secondary_symptoms": ['hand_or_finger_pain', 'wrist_pain', 'hand_or_finger_swelling', 'wrist_swelling', 'peripheral_edema', 'knee_pain', 'ache_all_over', 'joint_pain', 'elbow_swelling', 'joint_swelling'],
    "rare_symptoms": [],
    "symptom_weights": {'hand_or_finger_pain': 0.47, 'wrist_pain': 0.51, 'hand_or_finger_swelling': 0.49, 'wrist_swelling': 0.68, 'peripheral_edema': 0.49, 'knee_pain': 0.5, 'ache_all_over': 0.52, 'joint_pain': 0.5, 'elbow_swelling': 0.67, 'joint_swelling': 0.5}
}
disease_map["CSV_0617"] = {
    "name": "Rocky Mountain Spotted Fever",
    "primary_symptoms": ['headache', 'wrist_pain'],
    "secondary_symptoms": [],
    "rare_symptoms": [],
    "symptom_weights": {'headache': 1.0, 'wrist_pain': 1.0}
}
disease_map["CSV_0618"] = {
    "name": "Rosacea",
    "primary_symptoms": [],
    "secondary_symptoms": ['skin_swelling', 'abnormal_appearing_skin', 'skin_lesion', 'acne_or_pimples', 'skin_growth', 'symptoms_of_eye', 'skin_moles', 'lymphedema', 'itching_of_skin', 'skin_dryness,_peeling,_scaliness,_or_roughness'],
    "rare_symptoms": [],
    "symptom_weights": {'skin_swelling': 0.48, 'abnormal_appearing_skin': 0.67, 'skin_lesion': 0.5, 'acne_or_pimples': 0.51, 'skin_growth': 0.52, 'symptoms_of_eye': 0.67, 'skin_moles': 0.5, 'lymphedema': 0.47, 'itching_of_skin': 0.47, 'skin_dryness,_peeling,_scaliness,_or_roughness': 0.51}
}
disease_map["CSV_0619"] = {
    "name": "Rotator Cuff Injury",
    "primary_symptoms": ['arm_stiffness_or_tightness', 'hand_or_finger_stiffness_or_tightness'],
    "secondary_symptoms": ['arm_pain', 'shoulder_pain', 'shoulder_stiffness_or_tightness', 'shoulder_weakness'],
    "rare_symptoms": [],
    "symptom_weights": {'arm_pain': 0.5, 'arm_stiffness_or_tightness': 0.77, 'hand_or_finger_stiffness_or_tightness': 0.87, 'shoulder_pain': 0.52, 'shoulder_stiffness_or_tightness': 0.5, 'shoulder_weakness': 0.51}
}
disease_map["CSV_0620"] = {
    "name": "Salivary Gland Disorder",
    "primary_symptoms": ['sore_throat', 'cough', 'throat_feels_tight', 'swollen_lymph_nodes'],
    "secondary_symptoms": [],
    "rare_symptoms": [],
    "symptom_weights": {'sore_throat': 0.76, 'cough': 0.84, 'throat_feels_tight': 0.79, 'swollen_lymph_nodes': 0.73}
}
disease_map["CSV_0621"] = {
    "name": "Sarcoidosis",
    "primary_symptoms": ['sharp_chest_pain', 'facial_pain'],
    "secondary_symptoms": ['shortness_of_breath', 'chest_tightness', 'cough', 'headache', 'pain_in_eye', 'peripheral_edema'],
    "rare_symptoms": [],
    "symptom_weights": {'shortness_of_breath': 0.52, 'sharp_chest_pain': 0.72, 'chest_tightness': 0.51, 'cough': 0.54, 'headache': 0.54, 'facial_pain': 0.75, 'pain_in_eye': 0.69, 'peripheral_edema': 0.57}
}
disease_map["CSV_0622"] = {
    "name": "Scabies",
    "primary_symptoms": ['foot_or_toe_swelling', 'unpredictable_menstruation'],
    "secondary_symptoms": ['skin_swelling', 'abnormal_appearing_skin', 'problems_during_pregnancy', 'itching_of_skin', 'skin_rash'],
    "rare_symptoms": [],
    "symptom_weights": {'skin_swelling': 0.53, 'abnormal_appearing_skin': 0.49, 'foot_or_toe_swelling': 0.73, 'problems_during_pregnancy': 0.52, 'unpredictable_menstruation': 0.83, 'itching_of_skin': 0.51, 'skin_rash': 0.48}
}
disease_map["CSV_0623"] = {
    "name": "Scar",
    "primary_symptoms": ['skin_swelling', 'skin_moles'],
    "secondary_symptoms": ['lip_swelling', 'abnormal_appearing_skin', 'skin_lesion', 'skin_growth', 'itching_of_skin'],
    "rare_symptoms": [],
    "symptom_weights": {'skin_swelling': 0.75, 'lip_swelling': 0.68, 'abnormal_appearing_skin': 0.53, 'skin_lesion': 0.65, 'skin_growth': 0.46, 'skin_moles': 0.72, 'itching_of_skin': 0.5}
}
disease_map["CSV_0624"] = {
    "name": "Scarlet Fever",
    "primary_symptoms": ['throat_swelling', 'skin_swelling'],
    "secondary_symptoms": ['sore_throat', 'cough', 'fever', 'skin_rash'],
    "rare_symptoms": [],
    "symptom_weights": {'sore_throat': 0.49, 'cough': 0.44, 'throat_swelling': 0.86, 'skin_swelling': 0.7, 'fever': 0.61, 'skin_rash': 0.52}
}
disease_map["CSV_0625"] = {
    "name": "Schizophrenia",
    "primary_symptoms": [],
    "secondary_symptoms": ['anxiety_and_nervousness', 'depression', 'depressive_or_psychotic_symptoms', 'insomnia', 'hostile_behavior', 'excessive_anger', 'delusions_or_hallucinations', 'temper_problems', 'fears_and_phobias', 'low_self_esteem', 'hysterical_behavior'],
    "rare_symptoms": [],
    "symptom_weights": {'anxiety_and_nervousness': 0.49, 'depression': 0.53, 'depressive_or_psychotic_symptoms': 0.51, 'insomnia': 0.67, 'hostile_behavior': 0.49, 'excessive_anger': 0.52, 'delusions_or_hallucinations': 0.5, 'temper_problems': 0.51, 'fears_and_phobias': 0.52, 'low_self_esteem': 0.5, 'hysterical_behavior': 0.52}
}
disease_map["CSV_0626"] = {
    "name": "Sciatica",
    "primary_symptoms": [],
    "secondary_symptoms": ['leg_pain', 'hip_pain', 'low_back_pain', 'problems_with_movement', 'loss_of_sensation', 'leg_cramps_or_spasms', 'lower_body_pain', 'unusual_color_or_odor_to_urine', 'back_cramps_or_spasms', 'leg_weakness'],
    "rare_symptoms": [],
    "symptom_weights": {'leg_pain': 0.67, 'hip_pain': 0.5, 'low_back_pain': 0.53, 'problems_with_movement': 0.67, 'loss_of_sensation': 0.52, 'leg_cramps_or_spasms': 0.47, 'lower_body_pain': 0.53, 'unusual_color_or_odor_to_urine': 0.48, 'back_cramps_or_spasms': 0.49, 'leg_weakness': 0.52}
}
disease_map["CSV_0627"] = {
    "name": "Scleritis",
    "primary_symptoms": ['abnormal_involuntary_movements', 'headache'],
    "secondary_symptoms": ['pain_in_eye', 'spots_or_clouds_in_vision', 'eye_redness'],
    "rare_symptoms": [],
    "symptom_weights": {'abnormal_involuntary_movements': 0.93, 'headache': 0.72, 'pain_in_eye': 0.52, 'spots_or_clouds_in_vision': 0.57, 'eye_redness': 0.65}
}
disease_map["CSV_0628"] = {
    "name": "Scleroderma",
    "primary_symptoms": ['feeling_ill'],
    "secondary_symptoms": ['lip_swelling', 'abnormal_appearing_skin', 'skin_lesion', 'skin_growth', 'itching_of_skin', 'skin_dryness,_peeling,_scaliness,_or_roughness', 'skin_irritation'],
    "rare_symptoms": [],
    "symptom_weights": {'feeling_ill': 0.77, 'lip_swelling': 0.52, 'abnormal_appearing_skin': 0.51, 'skin_lesion': 0.66, 'skin_growth': 0.51, 'itching_of_skin': 0.46, 'skin_dryness,_peeling,_scaliness,_or_roughness': 0.49, 'skin_irritation': 0.62}
}
disease_map["CSV_0629"] = {
    "name": "Scoliosis",
    "primary_symptoms": ['knee_stiffness_or_tightness'],
    "secondary_symptoms": ['leg_pain', 'back_pain', 'low_back_pain', 'knee_swelling', 'problems_with_movement', 'lower_body_pain'],
    "rare_symptoms": [],
    "symptom_weights": {'leg_pain': 0.48, 'back_pain': 0.47, 'low_back_pain': 0.51, 'knee_swelling': 0.67, 'problems_with_movement': 0.5, 'knee_stiffness_or_tightness': 0.83, 'lower_body_pain': 0.5}
}
disease_map["CSV_0630"] = {
    "name": "Scurvy",
    "primary_symptoms": ['sharp_abdominal_pain', 'knee_lump_or_mass'],
    "secondary_symptoms": [],
    "rare_symptoms": [],
    "symptom_weights": {'sharp_abdominal_pain': 1.0, 'knee_lump_or_mass': 1.0}
}
disease_map["CSV_0631"] = {
    "name": "Seasonal Allergies (Hay Fever)",
    "primary_symptoms": [],
    "secondary_symptoms": ['sore_throat', 'cough', 'nasal_congestion', 'headache', 'ear_pain', 'frontal_headache', 'lacrimation', 'itchiness_of_eye', 'coryza', 'allergic_reaction', 'sneezing'],
    "rare_symptoms": [],
    "symptom_weights": {'sore_throat': 0.49, 'cough': 0.5, 'nasal_congestion': 0.49, 'headache': 0.51, 'ear_pain': 0.53, 'frontal_headache': 0.52, 'lacrimation': 0.68, 'itchiness_of_eye': 0.49, 'coryza': 0.51, 'allergic_reaction': 0.51, 'sneezing': 0.51}
}
disease_map["CSV_0632"] = {
    "name": "Sebaceous Cyst",
    "primary_symptoms": [],
    "secondary_symptoms": ['skin_swelling', 'abnormal_appearing_skin', 'skin_lesion', 'acne_or_pimples', 'skin_growth', 'irregular_appearing_scalp', 'neck_mass', 'skin_moles', 'hand_or_finger_lump_or_mass', 'back_mass_or_lump', 'arm_lump_or_mass'],
    "rare_symptoms": [],
    "symptom_weights": {'skin_swelling': 0.49, 'abnormal_appearing_skin': 0.5, 'skin_lesion': 0.49, 'acne_or_pimples': 0.5, 'skin_growth': 0.53, 'irregular_appearing_scalp': 0.51, 'neck_mass': 0.52, 'skin_moles': 0.67, 'hand_or_finger_lump_or_mass': 0.52, 'back_mass_or_lump': 0.49, 'arm_lump_or_mass': 0.48}
}
disease_map["CSV_0633"] = {
    "name": "Seborrheic Dermatitis",
    "primary_symptoms": [],
    "secondary_symptoms": ['abnormal_appearing_skin', 'skin_lesion', 'acne_or_pimples', 'skin_growth', 'irregular_appearing_scalp', 'symptoms_of_the_face', 'itching_of_skin', 'skin_dryness,_peeling,_scaliness,_or_roughness', 'too_little_hair', 'skin_rash', 'dry_or_flaky_scalp'],
    "rare_symptoms": [],
    "symptom_weights": {'abnormal_appearing_skin': 0.5, 'skin_lesion': 0.52, 'acne_or_pimples': 0.66, 'skin_growth': 0.51, 'irregular_appearing_scalp': 0.52, 'symptoms_of_the_face': 0.51, 'itching_of_skin': 0.51, 'skin_dryness,_peeling,_scaliness,_or_roughness': 0.53, 'too_little_hair': 0.5, 'skin_rash': 0.51, 'dry_or_flaky_scalp': 0.52}
}
disease_map["CSV_0634"] = {
    "name": "Seborrheic Keratosis",
    "primary_symptoms": [],
    "secondary_symptoms": ['skin_swelling', 'abnormal_appearing_skin', 'skin_lesion', 'acne_or_pimples', 'skin_growth', 'irregular_appearing_scalp', 'skin_moles', 'itching_of_skin', 'skin_irritation', 'warts', 'skin_rash'],
    "rare_symptoms": [],
    "symptom_weights": {'skin_swelling': 0.48, 'abnormal_appearing_skin': 0.54, 'skin_lesion': 0.51, 'acne_or_pimples': 0.5, 'skin_growth': 0.54, 'irregular_appearing_scalp': 0.51, 'skin_moles': 0.55, 'itching_of_skin': 0.66, 'skin_irritation': 0.52, 'warts': 0.51, 'skin_rash': 0.52}
}
disease_map["CSV_0635"] = {
    "name": "Sensorineural Hearing Loss",
    "primary_symptoms": [],
    "secondary_symptoms": ['dizziness', 'hoarse_voice', 'nasal_congestion', 'diminished_hearing', 'throat_feels_tight', 'ear_pain', 'ringing_in_ear', 'plugged_feeling_in_ear', 'itchy_ears', 'fluid_in_ear'],
    "rare_symptoms": [],
    "symptom_weights": {'dizziness': 0.48, 'hoarse_voice': 0.67, 'nasal_congestion': 0.52, 'diminished_hearing': 0.5, 'throat_feels_tight': 0.65, 'ear_pain': 0.53, 'ringing_in_ear': 0.49, 'plugged_feeling_in_ear': 0.5, 'itchy_ears': 0.49, 'fluid_in_ear': 0.49}
}
disease_map["CSV_0636"] = {
    "name": "Sepsis",
    "primary_symptoms": [],
    "secondary_symptoms": ['shortness_of_breath', 'cough', 'suprapubic_pain', 'sharp_abdominal_pain', 'feeling_ill', 'vomiting', 'weakness', 'decreased_appetite', 'fever', 'difficulty_breathing', 'chills'],
    "rare_symptoms": [],
    "symptom_weights": {'shortness_of_breath': 0.66, 'cough': 0.51, 'suprapubic_pain': 0.5, 'sharp_abdominal_pain': 0.5, 'feeling_ill': 0.53, 'vomiting': 0.51, 'weakness': 0.51, 'decreased_appetite': 0.5, 'fever': 0.54, 'difficulty_breathing': 0.51, 'chills': 0.5}
}
disease_map["CSV_0637"] = {
    "name": "Septic Arthritis",
    "primary_symptoms": ['leg_pain', 'hip_pain'],
    "secondary_symptoms": ['knee_pain', 'knee_swelling', 'fever'],
    "rare_symptoms": [],
    "symptom_weights": {'leg_pain': 0.89, 'hip_pain': 0.87, 'knee_pain': 0.53, 'knee_swelling': 0.58, 'fever': 0.48}
}
disease_map["CSV_0638"] = {
    "name": "Shingles (Herpes Zoster)",
    "primary_symptoms": ['sharp_chest_pain', 'headache'],
    "secondary_symptoms": ['abnormal_appearing_skin', 'skin_lesion', 'facial_pain', 'pain_in_eye', 'back_pain', 'itching_of_skin', 'skin_rash'],
    "rare_symptoms": [],
    "symptom_weights": {'sharp_chest_pain': 0.81, 'headache': 0.73, 'abnormal_appearing_skin': 0.54, 'skin_lesion': 0.59, 'facial_pain': 0.53, 'pain_in_eye': 0.53, 'back_pain': 0.54, 'itching_of_skin': 0.54, 'skin_rash': 0.59}
}
disease_map["CSV_0639"] = {
    "name": "Sialoadenitis",
    "primary_symptoms": [],
    "secondary_symptoms": ['sore_throat', 'cough', 'nasal_congestion', 'facial_pain', 'swollen_lymph_nodes', 'peripheral_edema', 'neck_mass', 'jaw_swelling', 'neck_swelling'],
    "rare_symptoms": [],
    "symptom_weights": {'sore_throat': 0.65, 'cough': 0.65, 'nasal_congestion': 0.51, 'facial_pain': 0.53, 'swollen_lymph_nodes': 0.69, 'peripheral_edema': 0.52, 'neck_mass': 0.49, 'jaw_swelling': 0.5, 'neck_swelling': 0.5}
}
disease_map["CSV_0640"] = {
    "name": "Sick Sinus Syndrome",
    "primary_symptoms": ['shortness_of_breath'],
    "secondary_symptoms": ['dizziness', 'palpitations', 'irregular_heartbeat', 'fainting', 'weakness', 'decreased_heart_rate', 'increased_heart_rate'],
    "rare_symptoms": [],
    "symptom_weights": {'shortness_of_breath': 0.74, 'dizziness': 0.54, 'palpitations': 0.51, 'irregular_heartbeat': 0.58, 'fainting': 0.53, 'weakness': 0.45, 'decreased_heart_rate': 0.47, 'increased_heart_rate': 0.66}
}
disease_map["CSV_0641"] = {
    "name": "Sickle Cell Anemia",
    "primary_symptoms": ['dry_lips'],
    "secondary_symptoms": ['leg_pain', 'back_pain', 'fever', 'ache_all_over', 'joint_pain', 'temper_problems', 'pulling_at_ears'],
    "rare_symptoms": [],
    "symptom_weights": {'leg_pain': 0.46, 'dry_lips': 0.88, 'back_pain': 0.51, 'fever': 0.5, 'ache_all_over': 0.54, 'joint_pain': 0.49, 'temper_problems': 0.51, 'pulling_at_ears': 0.51}
}
disease_map["CSV_0642"] = {
    "name": "Sickle Cell Crisis",
    "primary_symptoms": [],
    "secondary_symptoms": ['sharp_chest_pain', 'leg_pain', 'hip_pain', 'sharp_abdominal_pain', 'vomiting', 'arm_pain', 'back_pain', 'low_back_pain', 'burning_abdominal_pain', 'knee_pain', 'ache_all_over'],
    "rare_symptoms": [],
    "symptom_weights": {'sharp_chest_pain': 0.49, 'leg_pain': 0.5, 'hip_pain': 0.49, 'sharp_abdominal_pain': 0.51, 'vomiting': 0.68, 'arm_pain': 0.54, 'back_pain': 0.5, 'low_back_pain': 0.49, 'burning_abdominal_pain': 0.5, 'knee_pain': 0.5, 'ache_all_over': 0.49}
}
disease_map["CSV_0643"] = {
    "name": "Sinus Bradycardia",
    "primary_symptoms": [],
    "secondary_symptoms": ['shortness_of_breath', 'sharp_chest_pain', 'dizziness', 'chest_tightness', 'palpitations', 'irregular_heartbeat', 'fainting', 'feeling_ill', 'weakness', 'decreased_heart_rate', 'increased_heart_rate'],
    "rare_symptoms": [],
    "symptom_weights": {'shortness_of_breath': 0.5, 'sharp_chest_pain': 0.5, 'dizziness': 0.49, 'chest_tightness': 0.68, 'palpitations': 0.5, 'irregular_heartbeat': 0.54, 'fainting': 0.52, 'feeling_ill': 0.5, 'weakness': 0.5, 'decreased_heart_rate': 0.52, 'increased_heart_rate': 0.51}
}
disease_map["CSV_0644"] = {
    "name": "Sjogren Syndrome",
    "primary_symptoms": ['difficulty_in_swallowing', 'pain_in_eye'],
    "secondary_symptoms": ['diminished_vision', 'symptoms_of_eye', 'ache_all_over', 'joint_pain'],
    "rare_symptoms": [],
    "symptom_weights": {'difficulty_in_swallowing': 0.79, 'diminished_vision': 0.58, 'symptoms_of_eye': 0.51, 'pain_in_eye': 0.93, 'ache_all_over': 0.5, 'joint_pain': 0.45}
}
disease_map["CSV_0645"] = {
    "name": "Skin Cancer",
    "primary_symptoms": [],
    "secondary_symptoms": ['skin_swelling', 'lip_swelling', 'abnormal_appearing_skin', 'skin_lesion', 'skin_growth', 'irregular_appearing_scalp', 'skin_moles', 'skin_dryness,_peeling,_scaliness,_or_roughness', 'skin_irritation', 'warts'],
    "rare_symptoms": [],
    "symptom_weights": {'skin_swelling': 0.48, 'lip_swelling': 0.67, 'abnormal_appearing_skin': 0.49, 'skin_lesion': 0.52, 'skin_growth': 0.51, 'irregular_appearing_scalp': 0.68, 'skin_moles': 0.51, 'skin_dryness,_peeling,_scaliness,_or_roughness': 0.49, 'skin_irritation': 0.5, 'warts': 0.51}
}
disease_map["CSV_0646"] = {
    "name": "Skin Disorder",
    "primary_symptoms": [],
    "secondary_symptoms": ['skin_swelling', 'abnormal_appearing_skin', 'skin_lesion', 'acne_or_pimples', 'skin_growth', 'irregular_appearing_scalp', 'skin_moles', 'itching_of_skin', 'skin_dryness,_peeling,_scaliness,_or_roughness', 'skin_irritation'],
    "rare_symptoms": [],
    "symptom_weights": {'skin_swelling': 0.47, 'abnormal_appearing_skin': 0.69, 'skin_lesion': 0.53, 'acne_or_pimples': 0.51, 'skin_growth': 0.51, 'irregular_appearing_scalp': 0.48, 'skin_moles': 0.53, 'itching_of_skin': 0.51, 'skin_dryness,_peeling,_scaliness,_or_roughness': 0.52, 'skin_irritation': 0.67}
}
disease_map["CSV_0647"] = {
    "name": "Skin Pigmentation Disorder",
    "primary_symptoms": [],
    "secondary_symptoms": ['skin_swelling', 'abnormal_appearing_skin', 'skin_lesion', 'acne_or_pimples', 'skin_growth', 'irregular_appearing_scalp', 'skin_moles', 'itching_of_skin', 'skin_dryness,_peeling,_scaliness,_or_roughness', 'warts', 'skin_rash'],
    "rare_symptoms": [],
    "symptom_weights": {'skin_swelling': 0.5, 'abnormal_appearing_skin': 0.5, 'skin_lesion': 0.49, 'acne_or_pimples': 0.51, 'skin_growth': 0.53, 'irregular_appearing_scalp': 0.69, 'skin_moles': 0.52, 'itching_of_skin': 0.5, 'skin_dryness,_peeling,_scaliness,_or_roughness': 0.51, 'warts': 0.55, 'skin_rash': 0.5}
}
disease_map["CSV_0648"] = {
    "name": "Skin Polyp",
    "primary_symptoms": [],
    "secondary_symptoms": ['skin_swelling', 'abnormal_appearing_skin', 'skin_lesion', 'acne_or_pimples', 'skin_growth', 'irregular_appearing_scalp', 'skin_moles', 'itching_of_skin', 'skin_dryness,_peeling,_scaliness,_or_roughness', 'skin_irritation', 'warts'],
    "rare_symptoms": [],
    "symptom_weights": {'skin_swelling': 0.67, 'abnormal_appearing_skin': 0.51, 'skin_lesion': 0.49, 'acne_or_pimples': 0.51, 'skin_growth': 0.51, 'irregular_appearing_scalp': 0.53, 'skin_moles': 0.55, 'itching_of_skin': 0.49, 'skin_dryness,_peeling,_scaliness,_or_roughness': 0.51, 'skin_irritation': 0.49, 'warts': 0.54}
}
disease_map["CSV_0649"] = {
    "name": "Smoking Or Tobacco Addiction",
    "primary_symptoms": [],
    "secondary_symptoms": ['shortness_of_breath', 'sharp_chest_pain', 'cough', 'abusing_alcohol', 'drug_abuse', 'headache', 'smoking_problems', 'excessive_anger', 'coughing_up_sputum', 'hemoptysis', 'hurts_to_breath'],
    "rare_symptoms": [],
    "symptom_weights": {'shortness_of_breath': 0.5, 'sharp_chest_pain': 0.53, 'cough': 0.51, 'abusing_alcohol': 0.51, 'drug_abuse': 0.53, 'headache': 0.5, 'smoking_problems': 0.54, 'excessive_anger': 0.66, 'coughing_up_sputum': 0.52, 'hemoptysis': 0.5, 'hurts_to_breath': 0.53}
}
disease_map["CSV_0650"] = {
    "name": "Social Phobia",
    "primary_symptoms": [],
    "secondary_symptoms": ['anxiety_and_nervousness', 'depression', 'depressive_or_psychotic_symptoms', 'insomnia', 'abusing_alcohol', 'excessive_appetite', 'excessive_anger', 'delusions_or_hallucinations', 'fears_and_phobias'],
    "rare_symptoms": [],
    "symptom_weights": {'anxiety_and_nervousness': 0.49, 'depression': 0.51, 'depressive_or_psychotic_symptoms': 0.47, 'insomnia': 0.49, 'abusing_alcohol': 0.68, 'excessive_appetite': 0.68, 'excessive_anger': 0.68, 'delusions_or_hallucinations': 0.48, 'fears_and_phobias': 0.5}
}
disease_map["CSV_0651"] = {
    "name": "Soft Tissue Sarcoma",
    "primary_symptoms": ['groin_mass'],
    "secondary_symptoms": ['abnormal_appearing_skin', 'skin_lesion', 'skin_growth', 'skin_moles', 'itching_of_skin', 'skin_dryness,_peeling,_scaliness,_or_roughness'],
    "rare_symptoms": [],
    "symptom_weights": {'groin_mass': 0.81, 'abnormal_appearing_skin': 0.49, 'skin_lesion': 0.5, 'skin_growth': 0.49, 'skin_moles': 0.53, 'itching_of_skin': 0.53, 'skin_dryness,_peeling,_scaliness,_or_roughness': 0.66}
}
disease_map["CSV_0652"] = {
    "name": "Somatization Disorder",
    "primary_symptoms": ['dizziness', 'fainting'],
    "secondary_symptoms": ['anxiety_and_nervousness', 'depression', 'ache_all_over'],
    "rare_symptoms": [],
    "symptom_weights": {'anxiety_and_nervousness': 0.57, 'depression': 0.61, 'dizziness': 0.81, 'fainting': 0.89, 'ache_all_over': 0.52}
}
disease_map["CSV_0653"] = {
    "name": "Spermatocele",
    "primary_symptoms": ['retention_of_urine', 'elbow_weakness', 'frequent_urination'],
    "secondary_symptoms": ['pain_in_testicles', 'mass_in_scrotum'],
    "rare_symptoms": [],
    "symptom_weights": {'retention_of_urine': 0.78, 'elbow_weakness': 0.72, 'pain_in_testicles': 0.54, 'mass_in_scrotum': 0.57, 'frequent_urination': 0.91}
}
disease_map["CSV_0654"] = {
    "name": "Spherocytosis",
    "primary_symptoms": ['cough', 'elbow_weakness', 'skin_rash'],
    "secondary_symptoms": [],
    "rare_symptoms": [],
    "symptom_weights": {'cough': 1.0, 'elbow_weakness': 1.0, 'skin_rash': 0.8}
}
disease_map["CSV_0655"] = {
    "name": "Spina Bifida",
    "primary_symptoms": ['eye_moves_abnormally'],
    "secondary_symptoms": ['headache', 'involuntary_urination', 'skin_lesion', 'back_pain', 'disturbance_of_memory'],
    "rare_symptoms": [],
    "symptom_weights": {'headache': 0.55, 'involuntary_urination': 0.51, 'skin_lesion': 0.57, 'eye_moves_abnormally': 0.89, 'back_pain': 0.56, 'disturbance_of_memory': 0.7}
}
disease_map["CSV_0656"] = {
    "name": "Spinal Stenosis",
    "primary_symptoms": [],
    "secondary_symptoms": ['leg_pain', 'hip_pain', 'headache', 'arm_pain', 'back_pain', 'neck_pain', 'low_back_pain', 'problems_with_movement', 'loss_of_sensation', 'paresthesia', 'shoulder_pain', 'lower_body_pain'],
    "rare_symptoms": [],
    "symptom_weights": {'leg_pain': 0.49, 'hip_pain': 0.51, 'headache': 0.5, 'arm_pain': 0.51, 'back_pain': 0.52, 'neck_pain': 0.51, 'low_back_pain': 0.51, 'problems_with_movement': 0.51, 'loss_of_sensation': 0.49, 'paresthesia': 0.5, 'shoulder_pain': 0.49, 'lower_body_pain': 0.51}
}
disease_map["CSV_0657"] = {
    "name": "Spinocerebellar Ataxia",
    "primary_symptoms": ['anxiety_and_nervousness', 'abnormal_involuntary_movements'],
    "secondary_symptoms": ['dizziness'],
    "rare_symptoms": ['problems_with_movement'],
    "symptom_weights": {'anxiety_and_nervousness': 1.0, 'dizziness': 0.62, 'abnormal_involuntary_movements': 0.75, 'problems_with_movement': 0.38}
}
disease_map["CSV_0658"] = {
    "name": "Spondylitis",
    "primary_symptoms": ['stiffness_all_over'],
    "secondary_symptoms": ['leg_pain', 'hip_pain', 'back_pain', 'neck_pain', 'low_back_pain', 'side_pain', 'lower_body_pain', 'back_mass_or_lump'],
    "rare_symptoms": [],
    "symptom_weights": {'leg_pain': 0.5, 'hip_pain': 0.5, 'back_pain': 0.51, 'neck_pain': 0.48, 'low_back_pain': 0.53, 'side_pain': 0.66, 'lower_body_pain': 0.5, 'stiffness_all_over': 0.74, 'back_mass_or_lump': 0.51}
}
disease_map["CSV_0659"] = {
    "name": "Spondylolisthesis",
    "primary_symptoms": [],
    "secondary_symptoms": ['leg_pain', 'hip_pain', 'back_pain', 'neck_pain', 'low_back_pain', 'problems_with_movement', 'loss_of_sensation', 'paresthesia', 'leg_cramps_or_spasms', 'leg_weakness'],
    "rare_symptoms": [],
    "symptom_weights": {'leg_pain': 0.49, 'hip_pain': 0.66, 'back_pain': 0.52, 'neck_pain': 0.51, 'low_back_pain': 0.52, 'problems_with_movement': 0.48, 'loss_of_sensation': 0.5, 'paresthesia': 0.51, 'leg_cramps_or_spasms': 0.67, 'leg_weakness': 0.49}
}
disease_map["CSV_0660"] = {
    "name": "Spondylosis",
    "primary_symptoms": [],
    "secondary_symptoms": ['leg_pain', 'hip_pain', 'arm_pain', 'back_pain', 'neck_pain', 'low_back_pain', 'knee_pain', 'loss_of_sensation', 'paresthesia', 'shoulder_pain', 'ache_all_over', 'lower_body_pain'],
    "rare_symptoms": [],
    "symptom_weights": {'leg_pain': 0.48, 'hip_pain': 0.5, 'arm_pain': 0.51, 'back_pain': 0.51, 'neck_pain': 0.52, 'low_back_pain': 0.52, 'knee_pain': 0.5, 'loss_of_sensation': 0.51, 'paresthesia': 0.48, 'shoulder_pain': 0.49, 'ache_all_over': 0.52, 'lower_body_pain': 0.5}
}
disease_map["CSV_0661"] = {
    "name": "Spontaneous Abortion",
    "primary_symptoms": [],
    "secondary_symptoms": ['sharp_abdominal_pain', 'lower_abdominal_pain', 'intermenstrual_bleeding', 'pain_during_pregnancy', 'pelvic_pain', 'burning_abdominal_pain', 'problems_during_pregnancy', 'spotting_or_bleeding_during_pregnancy', 'cramps_and_spasms', 'blood_clots_during_menstrual_periods', 'uterine_contractions', 'heavy_menstrual_flow'],
    "rare_symptoms": [],
    "symptom_weights": {'sharp_abdominal_pain': 0.49, 'lower_abdominal_pain': 0.5, 'intermenstrual_bleeding': 0.5, 'pain_during_pregnancy': 0.51, 'pelvic_pain': 0.51, 'burning_abdominal_pain': 0.52, 'problems_during_pregnancy': 0.5, 'spotting_or_bleeding_during_pregnancy': 0.5, 'cramps_and_spasms': 0.49, 'blood_clots_during_menstrual_periods': 0.48, 'uterine_contractions': 0.52, 'heavy_menstrual_flow': 0.5}
}
disease_map["CSV_0662"] = {
    "name": "Sporotrichosis",
    "primary_symptoms": ['wrist_pain', 'knee_pain'],
    "secondary_symptoms": [],
    "rare_symptoms": [],
    "symptom_weights": {'wrist_pain': 1.0, 'knee_pain': 1.0}
}
disease_map["CSV_0663"] = {
    "name": "Sprain Or Strain",
    "primary_symptoms": [],
    "secondary_symptoms": ['leg_pain', 'headache', 'hand_or_finger_pain', 'wrist_pain', 'arm_pain', 'back_pain', 'neck_pain', 'low_back_pain', 'knee_pain', 'foot_or_toe_pain', 'ankle_pain', 'shoulder_pain'],
    "rare_symptoms": [],
    "symptom_weights": {'leg_pain': 0.48, 'headache': 0.5, 'hand_or_finger_pain': 0.5, 'wrist_pain': 0.51, 'arm_pain': 0.51, 'back_pain': 0.52, 'neck_pain': 0.5, 'low_back_pain': 0.51, 'knee_pain': 0.5, 'foot_or_toe_pain': 0.51, 'ankle_pain': 0.5, 'shoulder_pain': 0.5}
}
disease_map["CSV_0664"] = {
    "name": "Stenosis Of The Tear Duct",
    "primary_symptoms": ['white_discharge_from_eye', 'abnormal_movement_of_eyelid'],
    "secondary_symptoms": ['cough', 'symptoms_of_eye', 'lacrimation'],
    "rare_symptoms": [],
    "symptom_weights": {'cough': 0.7, 'white_discharge_from_eye': 0.82, 'symptoms_of_eye': 0.65, 'abnormal_movement_of_eyelid': 0.75, 'lacrimation': 0.47}
}
disease_map["CSV_0665"] = {
    "name": "Stomach Cancer",
    "primary_symptoms": ['difficulty_in_swallowing', 'diarrhea'],
    "secondary_symptoms": ['sharp_abdominal_pain', 'vomiting', 'nausea', 'burning_abdominal_pain', 'heartburn'],
    "rare_symptoms": [],
    "symptom_weights": {'difficulty_in_swallowing': 0.85, 'sharp_abdominal_pain': 0.63, 'vomiting': 0.51, 'nausea': 0.56, 'diarrhea': 0.85, 'burning_abdominal_pain': 0.56, 'heartburn': 0.51}
}
disease_map["CSV_0666"] = {
    "name": "Strep Throat",
    "primary_symptoms": [],
    "secondary_symptoms": ['sore_throat', 'cough', 'nasal_congestion', 'difficulty_in_swallowing', 'vomiting', 'headache', 'ear_pain', 'decreased_appetite', 'fever', 'ache_all_over', 'chills', 'skin_rash'],
    "rare_symptoms": [],
    "symptom_weights": {'sore_throat': 0.49, 'cough': 0.5, 'nasal_congestion': 0.5, 'difficulty_in_swallowing': 0.49, 'vomiting': 0.53, 'headache': 0.52, 'ear_pain': 0.52, 'decreased_appetite': 0.51, 'fever': 0.5, 'ache_all_over': 0.5, 'chills': 0.51, 'skin_rash': 0.52}
}
disease_map["CSV_0667"] = {
    "name": "Stress Incontinence",
    "primary_symptoms": ['hot_flashes', 'intermenstrual_bleeding'],
    "secondary_symptoms": ['retention_of_urine', 'painful_urination', 'involuntary_urination', 'frequent_urination', 'blood_in_urine'],
    "rare_symptoms": [],
    "symptom_weights": {'retention_of_urine': 0.69, 'painful_urination': 0.69, 'involuntary_urination': 0.53, 'frequent_urination': 0.56, 'blood_in_urine': 0.5, 'hot_flashes': 0.81, 'intermenstrual_bleeding': 0.7}
}
disease_map["CSV_0668"] = {
    "name": "Stricture Of The Esophagus",
    "primary_symptoms": ['sharp_chest_pain', 'difficulty_in_swallowing', 'problems_with_movement', 'heartburn'],
    "secondary_symptoms": ['vomiting', 'regurgitation.1'],
    "rare_symptoms": [],
    "symptom_weights": {'sharp_chest_pain': 0.78, 'difficulty_in_swallowing': 0.71, 'vomiting': 0.69, 'problems_with_movement': 0.71, 'heartburn': 0.83, 'regurgitation.1': 0.55}
}
disease_map["CSV_0669"] = {
    "name": "Stroke",
    "primary_symptoms": ['headache'],
    "secondary_symptoms": ['depressive_or_psychotic_symptoms', 'dizziness', 'abnormal_involuntary_movements', 'difficulty_speaking', 'problems_with_movement', 'focal_weakness', 'slurring_words', 'disturbance_of_memory', 'seizures'],
    "rare_symptoms": [],
    "symptom_weights": {'depressive_or_psychotic_symptoms': 0.5, 'dizziness': 0.52, 'abnormal_involuntary_movements': 0.51, 'difficulty_speaking': 0.5, 'headache': 0.74, 'problems_with_movement': 0.69, 'focal_weakness': 0.53, 'slurring_words': 0.52, 'disturbance_of_memory': 0.5, 'seizures': 0.51}
}
disease_map["CSV_0670"] = {
    "name": "Stye",
    "primary_symptoms": [],
    "secondary_symptoms": ['skin_swelling', 'abnormal_appearing_skin', 'symptoms_of_eye', 'pain_in_eye', 'eye_redness', 'itchiness_of_eye', 'eye_burns_or_stings', 'mass_on_eyelid', 'swollen_eye', 'eyelid_swelling', 'eyelid_lesion_or_rash'],
    "rare_symptoms": [],
    "symptom_weights": {'skin_swelling': 0.65, 'abnormal_appearing_skin': 0.5, 'symptoms_of_eye': 0.5, 'pain_in_eye': 0.51, 'eye_redness': 0.49, 'itchiness_of_eye': 0.51, 'eye_burns_or_stings': 0.51, 'mass_on_eyelid': 0.51, 'swollen_eye': 0.53, 'eyelid_swelling': 0.52, 'eyelid_lesion_or_rash': 0.54}
}
disease_map["CSV_0671"] = {
    "name": "Subacute Thyroiditis",
    "primary_symptoms": ['palpitations', 'blood_in_stool', 'problems_during_pregnancy'],
    "secondary_symptoms": ['pain_during_pregnancy', 'uterine_contractions'],
    "rare_symptoms": [],
    "symptom_weights": {'palpitations': 0.83, 'blood_in_stool': 0.97, 'pain_during_pregnancy': 0.6, 'problems_during_pregnancy': 0.8, 'uterine_contractions': 0.6}
}
disease_map["CSV_0672"] = {
    "name": "Subarachnoid Hemorrhage",
    "primary_symptoms": ['vomiting', 'symptoms_of_eye'],
    "secondary_symptoms": ['dizziness', 'fainting', 'headache', 'loss_of_sensation'],
    "rare_symptoms": [],
    "symptom_weights": {'dizziness': 0.61, 'fainting': 0.67, 'vomiting': 0.72, 'headache': 0.57, 'symptoms_of_eye': 0.84, 'loss_of_sensation': 0.64}
}
disease_map["CSV_0673"] = {
    "name": "Subconjunctival Hemorrhage",
    "primary_symptoms": ['headache', 'foreign_body_sensation_in_eye'],
    "secondary_symptoms": ['facial_pain', 'diminished_vision', 'symptoms_of_eye', 'pain_in_eye', 'eye_redness', 'bleeding_from_eye'],
    "rare_symptoms": [],
    "symptom_weights": {'headache': 0.71, 'facial_pain': 0.49, 'diminished_vision': 0.54, 'symptoms_of_eye': 0.51, 'pain_in_eye': 0.59, 'foreign_body_sensation_in_eye': 0.8, 'eye_redness': 0.55, 'bleeding_from_eye': 0.57}
}
disease_map["CSV_0674"] = {
    "name": "Subdural Hemorrhage",
    "primary_symptoms": ['dizziness', 'irritable_infant', 'vomiting'],
    "secondary_symptoms": ['depressive_or_psychotic_symptoms', 'headache', 'facial_pain'],
    "rare_symptoms": [],
    "symptom_weights": {'depressive_or_psychotic_symptoms': 0.61, 'dizziness': 0.73, 'irritable_infant': 0.78, 'vomiting': 0.73, 'headache': 0.52, 'facial_pain': 0.68}
}
disease_map["CSV_0675"] = {
    "name": "Substance-Related Mental Disorder",
    "primary_symptoms": ['hostile_behavior'],
    "secondary_symptoms": ['anxiety_and_nervousness', 'depressive_or_psychotic_symptoms', 'insomnia', 'drug_abuse', 'feeling_ill', 'delusions_or_hallucinations'],
    "rare_symptoms": [],
    "symptom_weights": {'anxiety_and_nervousness': 0.68, 'depressive_or_psychotic_symptoms': 0.54, 'insomnia': 0.69, 'hostile_behavior': 0.8, 'drug_abuse': 0.5, 'feeling_ill': 0.54, 'delusions_or_hallucinations': 0.51}
}
disease_map["CSV_0676"] = {
    "name": "Syndrome Of Inappropriate Secretion Of Adh (Siadh)",
    "primary_symptoms": ['dizziness', 'feeling_ill', 'cross_eyed'],
    "secondary_symptoms": [],
    "rare_symptoms": [],
    "symptom_weights": {'dizziness': 0.75, 'feeling_ill': 1.0, 'cross_eyed': 0.75}
}
disease_map["CSV_0677"] = {
    "name": "Syphilis",
    "primary_symptoms": ['vaginal_discharge', 'muscle_pain'],
    "secondary_symptoms": ['headache', 'skin_rash'],
    "rare_symptoms": [],
    "symptom_weights": {'headache': 0.57, 'vaginal_discharge': 0.8, 'muscle_pain': 0.97, 'skin_rash': 0.63}
}
disease_map["CSV_0678"] = {
    "name": "Syringomyelia",
    "primary_symptoms": ['fainting', 'headache'],
    "secondary_symptoms": ['back_pain', 'shoulder_pain'],
    "rare_symptoms": [],
    "symptom_weights": {'fainting': 1.0, 'headache': 0.86, 'back_pain': 0.57, 'shoulder_pain': 0.64}
}
disease_map["CSV_0679"] = {
    "name": "Systemic Lupus Erythematosis (Sle)",
    "primary_symptoms": ['hand_or_finger_stiffness_or_tightness', 'bones_are_painful'],
    "secondary_symptoms": ['sharp_chest_pain', 'knee_pain', 'leg_swelling', 'ache_all_over'],
    "rare_symptoms": [],
    "symptom_weights": {'sharp_chest_pain': 0.56, 'hand_or_finger_stiffness_or_tightness': 0.77, 'knee_pain': 0.69, 'bones_are_painful': 0.77, 'leg_swelling': 0.67, 'ache_all_over': 0.55}
}
disease_map["CSV_0680"] = {
    "name": "Teething Syndrome",
    "primary_symptoms": ['cough'],
    "secondary_symptoms": ['nasal_congestion', 'diarrhea', 'symptoms_of_infants', 'ear_pain', 'decreased_appetite', 'fever', 'temper_problems', 'redness_in_ear'],
    "rare_symptoms": [],
    "symptom_weights": {'cough': 0.78, 'nasal_congestion': 0.5, 'diarrhea': 0.52, 'symptoms_of_infants': 0.54, 'ear_pain': 0.63, 'decreased_appetite': 0.5, 'fever': 0.52, 'temper_problems': 0.49, 'redness_in_ear': 0.53}
}
disease_map["CSV_0681"] = {
    "name": "Temporary Or Benign Blood In Urine",
    "primary_symptoms": [],
    "secondary_symptoms": ['retention_of_urine', 'suprapubic_pain', 'sharp_abdominal_pain', 'painful_urination', 'involuntary_urination', 'frequent_urination', 'lower_abdominal_pain', 'blood_in_urine', 'back_pain', 'regurgitation', 'regurgitation.1', 'symptoms_of_bladder'],
    "rare_symptoms": [],
    "symptom_weights": {'retention_of_urine': 0.49, 'suprapubic_pain': 0.52, 'sharp_abdominal_pain': 0.49, 'painful_urination': 0.69, 'involuntary_urination': 0.5, 'frequent_urination': 0.52, 'lower_abdominal_pain': 0.52, 'blood_in_urine': 0.51, 'back_pain': 0.51, 'regurgitation': 0.51, 'regurgitation.1': 0.51, 'symptoms_of_bladder': 0.49}
}
disease_map["CSV_0682"] = {
    "name": "Temporomandibular Joint Disorder",
    "primary_symptoms": ['pain_in_eye'],
    "secondary_symptoms": ['sore_throat', 'nasal_congestion', 'diminished_hearing', 'headache', 'facial_pain', 'neck_pain', 'ear_pain'],
    "rare_symptoms": [],
    "symptom_weights": {'sore_throat': 0.7, 'nasal_congestion': 0.52, 'diminished_hearing': 0.67, 'headache': 0.52, 'facial_pain': 0.54, 'pain_in_eye': 0.73, 'neck_pain': 0.43, 'ear_pain': 0.48}
}
disease_map["CSV_0683"] = {
    "name": "Tendinitis",
    "primary_symptoms": [],
    "secondary_symptoms": ['leg_pain', 'hip_pain', 'hand_or_finger_pain', 'wrist_pain', 'hand_or_finger_swelling', 'arm_pain', 'knee_pain', 'foot_or_toe_pain', 'ankle_pain', 'shoulder_pain'],
    "rare_symptoms": [],
    "symptom_weights": {'leg_pain': 0.47, 'hip_pain': 0.51, 'hand_or_finger_pain': 0.5, 'wrist_pain': 0.5, 'hand_or_finger_swelling': 0.68, 'arm_pain': 0.53, 'knee_pain': 0.52, 'foot_or_toe_pain': 0.52, 'ankle_pain': 0.66, 'shoulder_pain': 0.52}
}
disease_map["CSV_0684"] = {
    "name": "Tension Headache",
    "primary_symptoms": ['neck_stiffness_or_tightness'],
    "secondary_symptoms": ['anxiety_and_nervousness', 'dizziness', 'headache', 'nausea', 'neck_pain', 'chills', 'back_cramps_or_spasms'],
    "rare_symptoms": [],
    "symptom_weights": {'anxiety_and_nervousness': 0.51, 'dizziness': 0.51, 'headache': 0.51, 'nausea': 0.55, 'neck_pain': 0.52, 'neck_stiffness_or_tightness': 0.78, 'chills': 0.48, 'back_cramps_or_spasms': 0.68}
}
disease_map["CSV_0685"] = {
    "name": "Testicular Cancer",
    "primary_symptoms": ['anxiety_and_nervousness', 'diminished_hearing'],
    "secondary_symptoms": ['mass_in_scrotum'],
    "rare_symptoms": [],
    "symptom_weights": {'anxiety_and_nervousness': 1.0, 'diminished_hearing': 1.0, 'mass_in_scrotum': 0.6}
}
disease_map["CSV_0686"] = {
    "name": "Testicular Disorder",
    "primary_symptoms": ['hoarse_voice', 'symptoms_of_the_scrotum_and_testes'],
    "secondary_symptoms": ['impotence', 'fatigue', 'loss_of_sex_drive'],
    "rare_symptoms": [],
    "symptom_weights": {'hoarse_voice': 0.87, 'symptoms_of_the_scrotum_and_testes': 0.9, 'impotence': 0.59, 'fatigue': 0.49, 'loss_of_sex_drive': 0.66}
}
disease_map["CSV_0687"] = {
    "name": "Testicular Torsion",
    "primary_symptoms": ['emotional_symptoms', 'back_pain'],
    "secondary_symptoms": ['symptoms_of_the_scrotum_and_testes', 'swelling_of_scrotum', 'pain_in_testicles', 'sharp_abdominal_pain'],
    "rare_symptoms": [],
    "symptom_weights": {'emotional_symptoms': 0.83, 'symptoms_of_the_scrotum_and_testes': 0.53, 'swelling_of_scrotum': 0.57, 'pain_in_testicles': 0.52, 'sharp_abdominal_pain': 0.62, 'back_pain': 0.73}
}
disease_map["CSV_0688"] = {
    "name": "Thalassemia",
    "primary_symptoms": ['insomnia', 'elbow_weakness'],
    "secondary_symptoms": [],
    "rare_symptoms": [],
    "symptom_weights": {'insomnia': 1.0, 'elbow_weakness': 1.0}
}
disease_map["CSV_0689"] = {
    "name": "Thoracic Aortic Aneurysm",
    "primary_symptoms": ['jaundice'],
    "secondary_symptoms": ['shortness_of_breath', 'sharp_chest_pain', 'dizziness', 'chest_tightness', 'sharp_abdominal_pain', 'fatigue'],
    "rare_symptoms": [],
    "symptom_weights": {'shortness_of_breath': 0.62, 'sharp_chest_pain': 0.52, 'dizziness': 0.47, 'chest_tightness': 0.48, 'jaundice': 0.84, 'sharp_abdominal_pain': 0.52, 'fatigue': 0.52}
}
disease_map["CSV_0690"] = {
    "name": "Thoracic Outlet Syndrome",
    "primary_symptoms": ['sharp_chest_pain', 'loss_of_sensation'],
    "secondary_symptoms": ['hand_or_finger_pain', 'arm_pain', 'decreased_appetite', 'shoulder_pain'],
    "rare_symptoms": [],
    "symptom_weights": {'sharp_chest_pain': 0.78, 'hand_or_finger_pain': 0.69, 'arm_pain': 0.66, 'decreased_appetite': 0.63, 'loss_of_sensation': 0.73, 'shoulder_pain': 0.52}
}
disease_map["CSV_0691"] = {
    "name": "Threatened Pregnancy",
    "primary_symptoms": [],
    "secondary_symptoms": ['sharp_abdominal_pain', 'lower_abdominal_pain', 'vaginal_discharge', 'intermenstrual_bleeding', 'back_pain', 'pelvic_pain', 'problems_during_pregnancy', 'spotting_or_bleeding_during_pregnancy', 'cramps_and_spasms', 'blood_clots_during_menstrual_periods', 'uterine_contractions'],
    "rare_symptoms": [],
    "symptom_weights": {'sharp_abdominal_pain': 0.66, 'lower_abdominal_pain': 0.51, 'vaginal_discharge': 0.46, 'intermenstrual_bleeding': 0.51, 'back_pain': 0.5, 'pelvic_pain': 0.51, 'problems_during_pregnancy': 0.51, 'spotting_or_bleeding_during_pregnancy': 0.5, 'cramps_and_spasms': 0.53, 'blood_clots_during_menstrual_periods': 0.47, 'uterine_contractions': 0.49}
}
disease_map["CSV_0692"] = {
    "name": "Thrombocytopenia",
    "primary_symptoms": ['irregular_appearing_scalp'],
    "secondary_symptoms": ['sharp_chest_pain', 'blood_in_stool', 'blood_in_urine', 'fatigue', 'nosebleed', 'bleeding_gums'],
    "rare_symptoms": [],
    "symptom_weights": {'sharp_chest_pain': 0.58, 'blood_in_stool': 0.53, 'blood_in_urine': 0.59, 'irregular_appearing_scalp': 0.89, 'fatigue': 0.56, 'nosebleed': 0.53, 'bleeding_gums': 0.52}
}
disease_map["CSV_0693"] = {
    "name": "Thrombophlebitis",
    "primary_symptoms": ['skin_swelling'],
    "secondary_symptoms": ['leg_pain', 'arm_pain', 'arm_swelling', 'foot_or_toe_pain', 'leg_swelling', 'ache_all_over', 'lymphedema', 'skin_on_leg_or_foot_looks_infected'],
    "rare_symptoms": [],
    "symptom_weights": {'skin_swelling': 0.75, 'leg_pain': 0.51, 'arm_pain': 0.54, 'arm_swelling': 0.65, 'foot_or_toe_pain': 0.52, 'leg_swelling': 0.49, 'ache_all_over': 0.51, 'lymphedema': 0.51, 'skin_on_leg_or_foot_looks_infected': 0.5}
}
disease_map["CSV_0694"] = {
    "name": "Thyroid Cancer",
    "primary_symptoms": ['difficulty_in_swallowing', 'swollen_lymph_nodes'],
    "secondary_symptoms": ['neck_mass', 'fatigue'],
    "rare_symptoms": [],
    "symptom_weights": {'difficulty_in_swallowing': 0.78, 'swollen_lymph_nodes': 0.89, 'neck_mass': 0.56, 'fatigue': 0.67}
}
disease_map["CSV_0695"] = {
    "name": "Thyroid Disease",
    "primary_symptoms": ['lump_in_throat', 'throat_feels_tight', 'neck_mass'],
    "secondary_symptoms": ['difficulty_in_swallowing'],
    "rare_symptoms": [],
    "symptom_weights": {'lump_in_throat': 0.94, 'throat_feels_tight': 0.88, 'difficulty_in_swallowing': 0.65, 'neck_mass': 0.82}
}
disease_map["CSV_0696"] = {
    "name": "Thyroid Nodule",
    "primary_symptoms": ['hoarse_voice', 'diminished_hearing'],
    "secondary_symptoms": ['throat_feels_tight', 'difficulty_in_swallowing', 'back_weakness', 'neck_mass', 'fatigue'],
    "rare_symptoms": [],
    "symptom_weights": {'hoarse_voice': 0.79, 'diminished_hearing': 0.8, 'throat_feels_tight': 0.51, 'difficulty_in_swallowing': 0.57, 'back_weakness': 0.69, 'neck_mass': 0.54, 'fatigue': 0.56}
}
disease_map["CSV_0697"] = {
    "name": "Tic (Movement) Disorder",
    "primary_symptoms": ['problems_with_movement'],
    "secondary_symptoms": ['depressive_or_psychotic_symptoms', 'abnormal_involuntary_movements', 'headache', 'symptoms_of_eye', 'abnormal_movement_of_eyelid'],
    "rare_symptoms": [],
    "symptom_weights": {'depressive_or_psychotic_symptoms': 0.63, 'abnormal_involuntary_movements': 0.57, 'headache': 0.61, 'symptoms_of_eye': 0.49, 'abnormal_movement_of_eyelid': 0.59, 'problems_with_movement': 0.89}
}
disease_map["CSV_0698"] = {
    "name": "Tietze Syndrome",
    "primary_symptoms": ['difficulty_breathing'],
    "secondary_symptoms": ['shortness_of_breath', 'sharp_chest_pain', 'chest_tightness', 'cough', 'nausea', 'loss_of_sensation', 'rib_pain'],
    "rare_symptoms": [],
    "symptom_weights": {'shortness_of_breath': 0.51, 'sharp_chest_pain': 0.55, 'chest_tightness': 0.53, 'cough': 0.7, 'nausea': 0.68, 'loss_of_sensation': 0.5, 'difficulty_breathing': 0.74, 'rib_pain': 0.51}
}
disease_map["CSV_0699"] = {
    "name": "Tinnitus Of Unknown Cause",
    "primary_symptoms": ['hoarse_voice'],
    "secondary_symptoms": ['dizziness', 'diminished_hearing', 'headache', 'ear_pain', 'ringing_in_ear', 'plugged_feeling_in_ear', 'itchy_ears'],
    "rare_symptoms": [],
    "symptom_weights": {'dizziness': 0.53, 'hoarse_voice': 0.78, 'diminished_hearing': 0.53, 'headache': 0.51, 'ear_pain': 0.48, 'ringing_in_ear': 0.54, 'plugged_feeling_in_ear': 0.53, 'itchy_ears': 0.65}
}
disease_map["CSV_0700"] = {
    "name": "Tonsillar Hypertrophy",
    "primary_symptoms": ['difficulty_in_swallowing'],
    "secondary_symptoms": ['sore_throat', 'cough', 'nasal_congestion', 'fever', 'apnea', 'abnormal_breathing_sounds', 'redness_in_ear'],
    "rare_symptoms": [],
    "symptom_weights": {'sore_throat': 0.52, 'cough': 0.54, 'nasal_congestion': 0.56, 'difficulty_in_swallowing': 0.75, 'fever': 0.66, 'apnea': 0.48, 'abnormal_breathing_sounds': 0.68, 'redness_in_ear': 0.53}
}
disease_map["CSV_0701"] = {
    "name": "Tonsillitis",
    "primary_symptoms": ['lump_in_throat'],
    "secondary_symptoms": ['sore_throat', 'nasal_congestion', 'diminished_hearing', 'throat_feels_tight', 'abnormal_breathing_sounds', 'redness_in_ear', 'swollen_or_red_tonsils', 'throat_redness'],
    "rare_symptoms": [],
    "symptom_weights": {'sore_throat': 0.5, 'nasal_congestion': 0.52, 'diminished_hearing': 0.67, 'lump_in_throat': 0.77, 'throat_feels_tight': 0.51, 'abnormal_breathing_sounds': 0.55, 'redness_in_ear': 0.5, 'swollen_or_red_tonsils': 0.51, 'throat_redness': 0.52}
}
disease_map["CSV_0702"] = {
    "name": "Tooth Abscess",
    "primary_symptoms": [],
    "secondary_symptoms": ['skin_swelling', 'lip_swelling', 'toothache', 'facial_pain', 'peripheral_edema', 'jaw_swelling', 'neck_swelling', 'gum_pain', 'mouth_pain', 'pain_in_gums'],
    "rare_symptoms": [],
    "symptom_weights": {'skin_swelling': 0.64, 'lip_swelling': 0.5, 'toothache': 0.51, 'facial_pain': 0.49, 'peripheral_edema': 0.51, 'jaw_swelling': 0.51, 'neck_swelling': 0.67, 'gum_pain': 0.52, 'mouth_pain': 0.51, 'pain_in_gums': 0.53}
}
disease_map["CSV_0703"] = {
    "name": "Tooth Disorder",
    "primary_symptoms": [],
    "secondary_symptoms": ['headache', 'toothache', 'facial_pain', 'mouth_ulcer', 'peripheral_edema', 'ear_pain', 'jaw_swelling', 'gum_pain', 'bleeding_gums', 'pain_in_gums'],
    "rare_symptoms": [],
    "symptom_weights": {'headache': 0.48, 'toothache': 0.5, 'facial_pain': 0.5, 'mouth_ulcer': 0.66, 'peripheral_edema': 0.68, 'ear_pain': 0.54, 'jaw_swelling': 0.5, 'gum_pain': 0.49, 'bleeding_gums': 0.5, 'pain_in_gums': 0.48}
}
disease_map["CSV_0704"] = {
    "name": "Torticollis",
    "primary_symptoms": ['throat_swelling'],
    "secondary_symptoms": ['abnormal_involuntary_movements', 'headache', 'arm_pain', 'neck_pain', 'neck_stiffness_or_tightness', 'shoulder_pain', 'neck_cramps_or_spasms'],
    "rare_symptoms": [],
    "symptom_weights": {'abnormal_involuntary_movements': 0.52, 'throat_swelling': 0.8, 'headache': 0.52, 'arm_pain': 0.67, 'neck_pain': 0.47, 'neck_stiffness_or_tightness': 0.52, 'shoulder_pain': 0.49, 'neck_cramps_or_spasms': 0.48}
}
disease_map["CSV_0705"] = {
    "name": "Tourette Syndrome",
    "primary_symptoms": ['abnormal_involuntary_movements', 'drug_abuse'],
    "secondary_symptoms": ['depressive_or_psychotic_symptoms', 'headache', 'allergic_reaction'],
    "rare_symptoms": [],
    "symptom_weights": {'depressive_or_psychotic_symptoms': 0.52, 'abnormal_involuntary_movements': 0.77, 'drug_abuse': 0.97, 'headache': 0.55, 'allergic_reaction': 0.61}
}
disease_map["CSV_0706"] = {
    "name": "Toxic Multinodular Goiter",
    "primary_symptoms": ['irregular_heartbeat', 'involuntary_urination'],
    "secondary_symptoms": ['abnormal_involuntary_movements', 'double_vision', 'fatigue'],
    "rare_symptoms": [],
    "symptom_weights": {'abnormal_involuntary_movements': 0.57, 'irregular_heartbeat': 0.78, 'involuntary_urination': 0.78, 'double_vision': 0.62, 'fatigue': 0.59}
}
disease_map["CSV_0707"] = {
    "name": "Toxoplasmosis",
    "primary_symptoms": ['emotional_symptoms', 'diminished_vision'],
    "secondary_symptoms": [],
    "rare_symptoms": [],
    "symptom_weights": {'emotional_symptoms': 0.92, 'diminished_vision': 0.92}
}
disease_map["CSV_0708"] = {
    "name": "Tracheitis",
    "primary_symptoms": ['hoarse_voice', 'nasal_congestion'],
    "secondary_symptoms": ['shortness_of_breath', 'sore_throat', 'cough', 'fever', 'sneezing'],
    "rare_symptoms": [],
    "symptom_weights": {'shortness_of_breath': 0.69, 'hoarse_voice': 0.71, 'sore_throat': 0.53, 'cough': 0.57, 'nasal_congestion': 0.87, 'fever': 0.53, 'sneezing': 0.53}
}
disease_map["CSV_0709"] = {
    "name": "Transient Ischemic Attack",
    "primary_symptoms": [],
    "secondary_symptoms": ['depressive_or_psychotic_symptoms', 'dizziness', 'difficulty_speaking', 'headache', 'weakness', 'loss_of_sensation', 'focal_weakness', 'symptoms_of_the_face', 'disturbance_of_memory', 'paresthesia'],
    "rare_symptoms": [],
    "symptom_weights": {'depressive_or_psychotic_symptoms': 0.64, 'dizziness': 0.54, 'difficulty_speaking': 0.51, 'headache': 0.54, 'weakness': 0.48, 'loss_of_sensation': 0.53, 'focal_weakness': 0.68, 'symptoms_of_the_face': 0.5, 'disturbance_of_memory': 0.48, 'paresthesia': 0.49}
}
disease_map["CSV_0710"] = {
    "name": "Trichiasis",
    "primary_symptoms": ['emotional_symptoms', 'diminished_vision', 'foreign_body_sensation_in_eye'],
    "secondary_symptoms": ['eye_redness', 'eyelid_lesion_or_rash'],
    "rare_symptoms": [],
    "symptom_weights": {'emotional_symptoms': 0.83, 'diminished_vision': 1.0, 'foreign_body_sensation_in_eye': 0.7, 'eye_redness': 0.67, 'eyelid_lesion_or_rash': 0.67}
}
disease_map["CSV_0711"] = {
    "name": "Trichinosis",
    "primary_symptoms": ['nasal_congestion', 'knee_lump_or_mass'],
    "secondary_symptoms": [],
    "rare_symptoms": [],
    "symptom_weights": {'nasal_congestion': 1.0, 'knee_lump_or_mass': 1.0}
}
disease_map["CSV_0712"] = {
    "name": "Trichomonas Infection",
    "primary_symptoms": ['vomiting'],
    "secondary_symptoms": ['sharp_abdominal_pain', 'nausea', 'vaginal_itching', 'lower_abdominal_pain', 'vaginal_discharge', 'pain_during_pregnancy', 'unpredictable_menstruation'],
    "rare_symptoms": [],
    "symptom_weights": {'sharp_abdominal_pain': 0.51, 'vomiting': 0.8, 'nausea': 0.53, 'vaginal_itching': 0.67, 'lower_abdominal_pain': 0.5, 'vaginal_discharge': 0.48, 'pain_during_pregnancy': 0.65, 'unpredictable_menstruation': 0.5}
}
disease_map["CSV_0713"] = {
    "name": "Tricuspid Valve Disease",
    "primary_symptoms": ['anxiety_and_nervousness', 'emotional_symptoms'],
    "secondary_symptoms": [],
    "rare_symptoms": [],
    "symptom_weights": {'anxiety_and_nervousness': 1.0, 'emotional_symptoms': 1.0}
}
disease_map["CSV_0714"] = {
    "name": "Trigeminal Neuralgia",
    "primary_symptoms": ['abnormal_involuntary_movements', 'symptoms_of_the_face'],
    "secondary_symptoms": ['dizziness', 'headache', 'toothache', 'facial_pain', 'pain_in_eye'],
    "rare_symptoms": [],
    "symptom_weights": {'dizziness': 0.7, 'abnormal_involuntary_movements': 0.87, 'headache': 0.56, 'toothache': 0.46, 'facial_pain': 0.52, 'pain_in_eye': 0.5, 'symptoms_of_the_face': 0.7}
}
disease_map["CSV_0715"] = {
    "name": "Trigger Finger (Finger Disorder)",
    "primary_symptoms": ['bones_are_painful'],
    "secondary_symptoms": ['hand_or_finger_pain', 'wrist_pain', 'hand_or_finger_swelling', 'hand_or_finger_stiffness_or_tightness', 'hand_or_finger_cramps_or_spasms'],
    "rare_symptoms": [],
    "symptom_weights": {'hand_or_finger_pain': 0.54, 'wrist_pain': 0.53, 'hand_or_finger_swelling': 0.63, 'hand_or_finger_stiffness_or_tightness': 0.55, 'bones_are_painful': 0.85, 'hand_or_finger_cramps_or_spasms': 0.54}
}
disease_map["CSV_0716"] = {
    "name": "Tuberculosis",
    "primary_symptoms": ['vaginal_itching'],
    "secondary_symptoms": ['shortness_of_breath', 'cough', 'congestion_in_chest'],
    "rare_symptoms": [],
    "symptom_weights": {'shortness_of_breath': 0.48, 'cough': 0.65, 'vaginal_itching': 0.87, 'congestion_in_chest': 0.65}
}
disease_map["CSV_0717"] = {
    "name": "Tuberous Sclerosis",
    "primary_symptoms": ['depressive_or_psychotic_symptoms', 'elbow_weakness'],
    "secondary_symptoms": ['seizures'],
    "rare_symptoms": [],
    "symptom_weights": {'depressive_or_psychotic_symptoms': 1.0, 'elbow_weakness': 0.83, 'seizures': 0.67}
}
disease_map["CSV_0718"] = {
    "name": "Turner Syndrome",
    "primary_symptoms": ['depression', 'emotional_symptoms'],
    "secondary_symptoms": [],
    "rare_symptoms": [],
    "symptom_weights": {'depression': 1.0, 'emotional_symptoms': 1.0}
}
disease_map["CSV_0719"] = {
    "name": "Typhoid Fever",
    "primary_symptoms": ['wrist_pain', 'fever'],
    "secondary_symptoms": [],
    "rare_symptoms": [],
    "symptom_weights": {'wrist_pain': 1.0, 'fever': 1.0}
}
disease_map["CSV_0720"] = {
    "name": "Ulcerative Colitis",
    "primary_symptoms": ['swollen_lymph_nodes'],
    "secondary_symptoms": ['blood_in_stool', 'sharp_abdominal_pain', 'vomiting', 'nausea', 'diarrhea', 'lower_abdominal_pain', 'burning_abdominal_pain', 'rectal_bleeding'],
    "rare_symptoms": [],
    "symptom_weights": {'blood_in_stool': 0.5, 'sharp_abdominal_pain': 0.52, 'vomiting': 0.52, 'nausea': 0.53, 'diarrhea': 0.47, 'lower_abdominal_pain': 0.5, 'swollen_lymph_nodes': 0.8, 'burning_abdominal_pain': 0.46, 'rectal_bleeding': 0.48}
}
disease_map["CSV_0721"] = {
    "name": "Urethral Disorder",
    "primary_symptoms": ['sharp_abdominal_pain', 'vomiting'],
    "secondary_symptoms": ['retention_of_urine', 'suprapubic_pain', 'abusing_alcohol', 'painful_urination', 'involuntary_urination', 'side_pain'],
    "rare_symptoms": [],
    "symptom_weights": {'retention_of_urine': 0.49, 'suprapubic_pain': 0.5, 'abusing_alcohol': 0.5, 'sharp_abdominal_pain': 0.75, 'vomiting': 0.83, 'painful_urination': 0.53, 'involuntary_urination': 0.55, 'side_pain': 0.68}
}
disease_map["CSV_0722"] = {
    "name": "Urethral Stricture",
    "primary_symptoms": ['symptoms_of_the_scrotum_and_testes'],
    "secondary_symptoms": ['retention_of_urine', 'suprapubic_pain', 'painful_urination', 'involuntary_urination', 'blood_in_urine', 'symptoms_of_prostate', 'symptoms_of_bladder'],
    "rare_symptoms": [],
    "symptom_weights": {'retention_of_urine': 0.53, 'suprapubic_pain': 0.65, 'symptoms_of_the_scrotum_and_testes': 0.81, 'painful_urination': 0.53, 'involuntary_urination': 0.51, 'blood_in_urine': 0.54, 'symptoms_of_prostate': 0.49, 'symptoms_of_bladder': 0.52}
}
disease_map["CSV_0723"] = {
    "name": "Urethral Valves",
    "primary_symptoms": ['suprapubic_pain', 'elbow_weakness'],
    "secondary_symptoms": ['sharp_abdominal_pain', 'lower_abdominal_pain', 'side_pain'],
    "rare_symptoms": [],
    "symptom_weights": {'suprapubic_pain': 0.97, 'elbow_weakness': 0.77, 'sharp_abdominal_pain': 0.63, 'lower_abdominal_pain': 0.66, 'side_pain': 0.66}
}
disease_map["CSV_0724"] = {
    "name": "Urethritis",
    "primary_symptoms": ['vaginal_itching'],
    "secondary_symptoms": ['retention_of_urine', 'suprapubic_pain', 'sharp_abdominal_pain', 'painful_urination', 'frequent_urination', 'blood_in_urine', 'penis_pain', 'penile_discharge'],
    "rare_symptoms": [],
    "symptom_weights": {'retention_of_urine': 0.5, 'suprapubic_pain': 0.66, 'sharp_abdominal_pain': 0.48, 'vaginal_itching': 0.75, 'painful_urination': 0.53, 'frequent_urination': 0.47, 'blood_in_urine': 0.51, 'penis_pain': 0.49, 'penile_discharge': 0.51}
}
disease_map["CSV_0725"] = {
    "name": "Urge Incontinence",
    "primary_symptoms": [],
    "secondary_symptoms": ['retention_of_urine', 'vaginal_itching', 'painful_urination', 'involuntary_urination', 'frequent_urination', 'blood_in_urine', 'excessive_urination_at_night', 'constipation', 'symptoms_of_bladder'],
    "rare_symptoms": [],
    "symptom_weights": {'retention_of_urine': 0.7, 'vaginal_itching': 0.69, 'painful_urination': 0.51, 'involuntary_urination': 0.52, 'frequent_urination': 0.54, 'blood_in_urine': 0.68, 'excessive_urination_at_night': 0.51, 'constipation': 0.48, 'symptoms_of_bladder': 0.52}
}
disease_map["CSV_0726"] = {
    "name": "Urinary Tract Obstruction",
    "primary_symptoms": [],
    "secondary_symptoms": ['retention_of_urine', 'suprapubic_pain', 'sharp_abdominal_pain', 'painful_urination', 'frequent_urination', 'blood_in_urine', 'back_pain', 'side_pain', 'symptoms_of_prostate', 'excessive_urination_at_night'],
    "rare_symptoms": [],
    "symptom_weights": {'retention_of_urine': 0.49, 'suprapubic_pain': 0.49, 'sharp_abdominal_pain': 0.49, 'painful_urination': 0.67, 'frequent_urination': 0.5, 'blood_in_urine': 0.54, 'back_pain': 0.49, 'side_pain': 0.49, 'symptoms_of_prostate': 0.5, 'excessive_urination_at_night': 0.66}
}
disease_map["CSV_0727"] = {
    "name": "Uterine Atony",
    "primary_symptoms": ['back_cramps_or_spasms'],
    "secondary_symptoms": ['sharp_abdominal_pain', 'lower_abdominal_pain', 'blood_in_urine', 'intermenstrual_bleeding', 'pain_during_pregnancy', 'problems_during_pregnancy', 'spotting_or_bleeding_during_pregnancy', 'uterine_contractions'],
    "rare_symptoms": [],
    "symptom_weights": {'sharp_abdominal_pain': 0.54, 'lower_abdominal_pain': 0.52, 'blood_in_urine': 0.5, 'intermenstrual_bleeding': 0.55, 'pain_during_pregnancy': 0.54, 'problems_during_pregnancy': 0.46, 'spotting_or_bleeding_during_pregnancy': 0.55, 'uterine_contractions': 0.49, 'back_cramps_or_spasms': 0.71}
}
disease_map["CSV_0728"] = {
    "name": "Uterine Cancer",
    "primary_symptoms": ['groin_mass', 'pelvic_pain', 'vaginal_bleeding_after_menopause'],
    "secondary_symptoms": [],
    "rare_symptoms": [],
    "symptom_weights": {'groin_mass': 1.0, 'pelvic_pain': 0.8, 'vaginal_bleeding_after_menopause': 1.0}
}
disease_map["CSV_0729"] = {
    "name": "Uterine Fibroids",
    "primary_symptoms": ['involuntary_urination'],
    "secondary_symptoms": ['sharp_abdominal_pain', 'lower_abdominal_pain', 'intermenstrual_bleeding', 'pelvic_pain', 'cramps_and_spasms', 'heavy_menstrual_flow', 'unpredictable_menstruation', 'painful_menstruation'],
    "rare_symptoms": [],
    "symptom_weights": {'sharp_abdominal_pain': 0.49, 'involuntary_urination': 0.77, 'lower_abdominal_pain': 0.5, 'intermenstrual_bleeding': 0.67, 'pelvic_pain': 0.5, 'cramps_and_spasms': 0.53, 'heavy_menstrual_flow': 0.49, 'unpredictable_menstruation': 0.53, 'painful_menstruation': 0.53}
}
disease_map["CSV_0730"] = {
    "name": "Uveitis",
    "primary_symptoms": ['elbow_weakness', 'symptoms_of_eye'],
    "secondary_symptoms": ['diminished_vision'],
    "rare_symptoms": [],
    "symptom_weights": {'elbow_weakness': 0.95, 'diminished_vision': 0.63, 'symptoms_of_eye': 0.89}
}
disease_map["CSV_0731"] = {
    "name": "Vacterl Syndrome",
    "primary_symptoms": ['suprapubic_pain', 'emotional_symptoms'],
    "secondary_symptoms": [],
    "rare_symptoms": [],
    "symptom_weights": {'suprapubic_pain': 1.0, 'emotional_symptoms': 1.0}
}
disease_map["CSV_0732"] = {
    "name": "Vaginal Cyst",
    "primary_symptoms": [],
    "secondary_symptoms": ['sharp_abdominal_pain', 'lower_abdominal_pain', 'vaginal_discharge', 'intermenstrual_bleeding', 'pain_during_pregnancy', 'pelvic_pain', 'vaginal_pain', 'problems_during_pregnancy', 'spotting_or_bleeding_during_pregnancy', 'cramps_and_spasms', 'blood_clots_during_menstrual_periods', 'heavy_menstrual_flow'],
    "rare_symptoms": [],
    "symptom_weights": {'sharp_abdominal_pain': 0.48, 'lower_abdominal_pain': 0.51, 'vaginal_discharge': 0.5, 'intermenstrual_bleeding': 0.51, 'pain_during_pregnancy': 0.51, 'pelvic_pain': 0.52, 'vaginal_pain': 0.5, 'problems_during_pregnancy': 0.49, 'spotting_or_bleeding_during_pregnancy': 0.49, 'cramps_and_spasms': 0.5, 'blood_clots_during_menstrual_periods': 0.5, 'heavy_menstrual_flow': 0.52}
}
disease_map["CSV_0733"] = {
    "name": "Vaginal Yeast Infection",
    "primary_symptoms": ['suprapubic_pain'],
    "secondary_symptoms": ['sharp_abdominal_pain', 'vaginal_itching', 'painful_urination', 'lower_abdominal_pain', 'vaginal_discharge', 'vaginal_pain', 'vaginal_redness', 'vulvar_irritation', 'itching_of_skin'],
    "rare_symptoms": [],
    "symptom_weights": {'suprapubic_pain': 0.72, 'sharp_abdominal_pain': 0.46, 'vaginal_itching': 0.51, 'painful_urination': 0.48, 'lower_abdominal_pain': 0.5, 'vaginal_discharge': 0.48, 'vaginal_pain': 0.51, 'vaginal_redness': 0.47, 'vulvar_irritation': 0.5, 'itching_of_skin': 0.52}
}
disease_map["CSV_0734"] = {
    "name": "Vaginismus",
    "primary_symptoms": ['suprapubic_pain', 'sharp_abdominal_pain'],
    "secondary_symptoms": ['pain_during_intercourse', 'lower_abdominal_pain', 'pelvic_pain', 'vaginal_pain'],
    "rare_symptoms": [],
    "symptom_weights": {'suprapubic_pain': 0.94, 'sharp_abdominal_pain': 0.71, 'pain_during_intercourse': 0.55, 'lower_abdominal_pain': 0.55, 'pelvic_pain': 0.69, 'vaginal_pain': 0.56}
}
disease_map["CSV_0735"] = {
    "name": "Vaginitis",
    "primary_symptoms": [],
    "secondary_symptoms": ['suprapubic_pain', 'sharp_abdominal_pain', 'vaginal_itching', 'painful_urination', 'pain_during_intercourse', 'lower_abdominal_pain', 'vaginal_discharge', 'pain_during_pregnancy', 'pelvic_pain', 'vaginal_pain', 'vaginal_redness'],
    "rare_symptoms": [],
    "symptom_weights": {'suprapubic_pain': 0.5, 'sharp_abdominal_pain': 0.51, 'vaginal_itching': 0.49, 'painful_urination': 0.5, 'pain_during_intercourse': 0.67, 'lower_abdominal_pain': 0.55, 'vaginal_discharge': 0.52, 'pain_during_pregnancy': 0.5, 'pelvic_pain': 0.51, 'vaginal_pain': 0.54, 'vaginal_redness': 0.51}
}
disease_map["CSV_0736"] = {
    "name": "Valley Fever",
    "primary_symptoms": ['shortness_of_breath', 'hand_or_finger_pain'],
    "secondary_symptoms": ['fever', 'shoulder_swelling'],
    "rare_symptoms": [],
    "symptom_weights": {'shortness_of_breath': 0.78, 'hand_or_finger_pain': 1.0, 'fever': 0.67, 'shoulder_swelling': 0.44}
}
disease_map["CSV_0737"] = {
    "name": "Varicocele Of The Testicles",
    "primary_symptoms": [],
    "secondary_symptoms": ['symptoms_of_the_scrotum_and_testes', 'swelling_of_scrotum', 'pain_in_testicles', 'mass_in_scrotum', 'involuntary_urination', 'lower_abdominal_pain', 'skin_growth', 'pain_of_the_anus', 'groin_pain', 'infertility'],
    "rare_symptoms": [],
    "symptom_weights": {'symptoms_of_the_scrotum_and_testes': 0.49, 'swelling_of_scrotum': 0.5, 'pain_in_testicles': 0.52, 'mass_in_scrotum': 0.49, 'involuntary_urination': 0.68, 'lower_abdominal_pain': 0.51, 'skin_growth': 0.51, 'pain_of_the_anus': 0.67, 'groin_pain': 0.51, 'infertility': 0.53}
}
disease_map["CSV_0738"] = {
    "name": "Varicose Veins",
    "primary_symptoms": ['leg_cramps_or_spasms'],
    "secondary_symptoms": ['leg_pain', 'skin_lesion', 'peripheral_edema', 'leg_swelling', 'ache_all_over', 'lymphedema', 'leg_lump_or_mass'],
    "rare_symptoms": [],
    "symptom_weights": {'leg_pain': 0.5, 'skin_lesion': 0.52, 'peripheral_edema': 0.47, 'leg_swelling': 0.53, 'leg_cramps_or_spasms': 0.74, 'ache_all_over': 0.54, 'lymphedema': 0.44, 'leg_lump_or_mass': 0.5}
}
disease_map["CSV_0739"] = {
    "name": "Vasculitis",
    "primary_symptoms": ['foot_or_toe_swelling', 'leg_stiffness_or_tightness'],
    "secondary_symptoms": ['dizziness', 'leg_pain', 'headache', 'skin_lesion', 'lymphedema', 'skin_rash'],
    "rare_symptoms": [],
    "symptom_weights": {'dizziness': 0.53, 'leg_pain': 0.49, 'headache': 0.52, 'skin_lesion': 0.52, 'foot_or_toe_swelling': 0.77, 'leg_stiffness_or_tightness': 0.75, 'lymphedema': 0.51, 'skin_rash': 0.48}
}
disease_map["CSV_0740"] = {
    "name": "Venous Insufficiency",
    "primary_symptoms": ['leg_pain', 'skin_on_leg_or_foot_looks_infected'],
    "secondary_symptoms": ['abnormal_appearing_skin', 'skin_lesion', 'leg_cramps_or_spasms', 'lymphedema', 'fluid_retention', 'burning_chest_pain'],
    "rare_symptoms": [],
    "symptom_weights": {'leg_pain': 0.77, 'abnormal_appearing_skin': 0.55, 'skin_lesion': 0.52, 'leg_cramps_or_spasms': 0.48, 'lymphedema': 0.53, 'skin_on_leg_or_foot_looks_infected': 0.7, 'fluid_retention': 0.46, 'burning_chest_pain': 0.68}
}
disease_map["CSV_0741"] = {
    "name": "Vertebrobasilar Insufficiency",
    "primary_symptoms": ['sharp_chest_pain', 'leg_pain', 'back_pain'],
    "secondary_symptoms": ['dizziness'],
    "rare_symptoms": [],
    "symptom_weights": {'sharp_chest_pain': 0.96, 'dizziness': 0.52, 'leg_pain': 0.78, 'back_pain': 1.0}
}
disease_map["CSV_0742"] = {
    "name": "Vesicoureteral Reflux",
    "primary_symptoms": ['suprapubic_pain', 'involuntary_urination', 'blood_in_urine'],
    "secondary_symptoms": ['fever'],
    "rare_symptoms": [],
    "symptom_weights": {'suprapubic_pain': 0.7, 'involuntary_urination': 0.8, 'blood_in_urine': 0.8, 'fever': 0.6}
}
disease_map["CSV_0743"] = {
    "name": "Viral Exanthem",
    "primary_symptoms": ['skin_swelling'],
    "secondary_symptoms": ['cough', 'nasal_congestion', 'vomiting', 'abnormal_appearing_skin', 'decreased_appetite', 'fever', 'pulling_at_ears', 'itching_of_skin', 'skin_rash'],
    "rare_symptoms": [],
    "symptom_weights": {'cough': 0.47, 'nasal_congestion': 0.48, 'skin_swelling': 0.74, 'vomiting': 0.48, 'abnormal_appearing_skin': 0.52, 'decreased_appetite': 0.49, 'fever': 0.52, 'pulling_at_ears': 0.51, 'itching_of_skin': 0.5, 'skin_rash': 0.51}
}
disease_map["CSV_0744"] = {
    "name": "Viral Hepatitis",
    "primary_symptoms": ['abusing_alcohol', 'hand_or_finger_stiffness_or_tightness'],
    "secondary_symptoms": ['sharp_abdominal_pain', 'stomach_bloating', 'melena'],
    "rare_symptoms": [],
    "symptom_weights": {'abusing_alcohol': 0.71, 'sharp_abdominal_pain': 0.54, 'hand_or_finger_stiffness_or_tightness': 0.8, 'stomach_bloating': 0.51, 'melena': 0.57}
}
disease_map["CSV_0745"] = {
    "name": "Viral Warts",
    "primary_symptoms": ['lip_swelling'],
    "secondary_symptoms": ['skin_swelling', 'abnormal_appearing_skin', 'skin_lesion', 'acne_or_pimples', 'skin_growth', 'skin_moles', 'warts', 'bumps_on_penis'],
    "rare_symptoms": [],
    "symptom_weights": {'skin_swelling': 0.68, 'lip_swelling': 0.75, 'abnormal_appearing_skin': 0.49, 'skin_lesion': 0.51, 'acne_or_pimples': 0.47, 'skin_growth': 0.51, 'skin_moles': 0.49, 'warts': 0.52, 'bumps_on_penis': 0.47}
}
disease_map["CSV_0746"] = {
    "name": "Vitamin A Deficiency",
    "primary_symptoms": ['hand_or_finger_pain', 'knee_lump_or_mass'],
    "secondary_symptoms": [],
    "rare_symptoms": [],
    "symptom_weights": {'hand_or_finger_pain': 1.0, 'knee_lump_or_mass': 1.0}
}
disease_map["CSV_0747"] = {
    "name": "Vitamin B12 Deficiency",
    "primary_symptoms": ['hot_flashes', 'knee_stiffness_or_tightness', 'disturbance_of_memory'],
    "secondary_symptoms": ['problems_with_movement', 'fatigue'],
    "rare_symptoms": [],
    "symptom_weights": {'hot_flashes': 0.76, 'problems_with_movement': 0.53, 'knee_stiffness_or_tightness': 0.8, 'disturbance_of_memory': 0.72, 'fatigue': 0.53}
}
disease_map["CSV_0748"] = {
    "name": "Vitamin D Deficiency",
    "primary_symptoms": ['hot_flashes', 'arm_stiffness_or_tightness'],
    "secondary_symptoms": ['fatigue'],
    "rare_symptoms": [],
    "symptom_weights": {'hot_flashes': 0.82, 'arm_stiffness_or_tightness': 0.94, 'fatigue': 0.65}
}
disease_map["CSV_0749"] = {
    "name": "Vitreous Degeneration",
    "primary_symptoms": ['double_vision'],
    "secondary_symptoms": ['diminished_vision', 'symptoms_of_eye', 'pain_in_eye', 'foreign_body_sensation_in_eye', 'spots_or_clouds_in_vision', 'eye_redness', 'lacrimation'],
    "rare_symptoms": [],
    "symptom_weights": {'diminished_vision': 0.52, 'double_vision': 0.78, 'symptoms_of_eye': 0.53, 'pain_in_eye': 0.48, 'foreign_body_sensation_in_eye': 0.69, 'spots_or_clouds_in_vision': 0.51, 'eye_redness': 0.7, 'lacrimation': 0.53}
}
disease_map["CSV_0750"] = {
    "name": "Vitreous Hemorrhage",
    "primary_symptoms": ['pain_in_eye'],
    "secondary_symptoms": ['diminished_vision', 'symptoms_of_eye', 'spots_or_clouds_in_vision', 'lacrimation', 'blindness'],
    "rare_symptoms": [],
    "symptom_weights": {'diminished_vision': 0.44, 'symptoms_of_eye': 0.56, 'pain_in_eye': 0.7, 'spots_or_clouds_in_vision': 0.63, 'lacrimation': 0.48, 'blindness': 0.41}
}
disease_map["CSV_0751"] = {
    "name": "Vocal Cord Polyp",
    "primary_symptoms": ['difficulty_speaking', 'throat_swelling', 'throat_feels_tight'],
    "secondary_symptoms": ['hoarse_voice', 'sore_throat'],
    "rare_symptoms": [],
    "symptom_weights": {'hoarse_voice': 0.5, 'sore_throat': 0.49, 'difficulty_speaking': 0.77, 'throat_swelling': 0.81, 'throat_feels_tight': 0.79}
}
disease_map["CSV_0752"] = {
    "name": "Volvulus",
    "primary_symptoms": ['depressive_or_psychotic_symptoms', 'vomiting'],
    "secondary_symptoms": ['elbow_weakness', 'sharp_abdominal_pain'],
    "rare_symptoms": [],
    "symptom_weights": {'depressive_or_psychotic_symptoms': 1.0, 'elbow_weakness': 0.64, 'sharp_abdominal_pain': 0.64, 'vomiting': 0.82}
}
disease_map["CSV_0753"] = {
    "name": "Von Willebrand Disease",
    "primary_symptoms": ['blood_in_stool', 'muscle_swelling'],
    "secondary_symptoms": ['nosebleed'],
    "rare_symptoms": [],
    "symptom_weights": {'blood_in_stool': 1.0, 'muscle_swelling': 1.0, 'nosebleed': 0.4}
}
disease_map["CSV_0754"] = {
    "name": "Vulvar Cancer",
    "primary_symptoms": ['insomnia', 'back_pain'],
    "secondary_symptoms": ['emotional_symptoms'],
    "rare_symptoms": [],
    "symptom_weights": {'insomnia': 1.0, 'emotional_symptoms': 0.67, 'back_pain': 0.83}
}
disease_map["CSV_0755"] = {
    "name": "Vulvar Disorder",
    "primary_symptoms": ['vaginal_itching', 'pain_during_intercourse'],
    "secondary_symptoms": ['vaginal_discharge', 'vaginal_pain', 'vulvar_irritation', 'skin_dryness,_peeling,_scaliness,_or_roughness'],
    "rare_symptoms": [],
    "symptom_weights": {'vaginal_itching': 0.77, 'pain_during_intercourse': 0.78, 'vaginal_discharge': 0.68, 'vaginal_pain': 0.69, 'vulvar_irritation': 0.5, 'skin_dryness,_peeling,_scaliness,_or_roughness': 0.51}
}
disease_map["CSV_0756"] = {
    "name": "Vulvodynia",
    "primary_symptoms": [],
    "secondary_symptoms": ['sharp_abdominal_pain', 'nausea', 'painful_urination', 'lower_abdominal_pain', 'vaginal_discharge', 'back_pain', 'pain_during_pregnancy', 'pelvic_pain', 'burning_abdominal_pain', 'vaginal_pain', 'side_pain', 'cramps_and_spasms'],
    "rare_symptoms": [],
    "symptom_weights": {'sharp_abdominal_pain': 0.49, 'nausea': 0.5, 'painful_urination': 0.5, 'lower_abdominal_pain': 0.51, 'vaginal_discharge': 0.51, 'back_pain': 0.52, 'pain_during_pregnancy': 0.5, 'pelvic_pain': 0.5, 'burning_abdominal_pain': 0.49, 'vaginal_pain': 0.48, 'side_pain': 0.49, 'cramps_and_spasms': 0.49}
}
disease_map["CSV_0757"] = {
    "name": "Wernicke Korsakoff Syndrome",
    "primary_symptoms": ['anxiety_and_nervousness', 'abusing_alcohol'],
    "secondary_symptoms": ['depressive_or_psychotic_symptoms'],
    "rare_symptoms": [],
    "symptom_weights": {'anxiety_and_nervousness': 1.0, 'depressive_or_psychotic_symptoms': 0.5, 'abusing_alcohol': 0.83}
}
disease_map["CSV_0758"] = {
    "name": "White Blood Cell Disease",
    "primary_symptoms": [],
    "secondary_symptoms": ['cough', 'sharp_abdominal_pain', 'vomiting', 'nausea', 'diarrhea', 'heartburn', 'fever', 'chills', 'fatigue'],
    "rare_symptoms": [],
    "symptom_weights": {'cough': 0.5, 'sharp_abdominal_pain': 0.53, 'vomiting': 0.49, 'nausea': 0.51, 'diarrhea': 0.66, 'heartburn': 0.66, 'fever': 0.53, 'chills': 0.67, 'fatigue': 0.5}
}
disease_map["CSV_0759"] = {
    "name": "Whooping Cough",
    "primary_symptoms": ['shortness_of_breath', 'sore_throat', 'nasal_congestion'],
    "secondary_symptoms": ['cough', 'vomiting'],
    "rare_symptoms": [],
    "symptom_weights": {'shortness_of_breath': 0.72, 'sore_throat': 0.84, 'cough': 0.6, 'nasal_congestion': 0.93, 'vomiting': 0.7}
}
disease_map["CSV_0760"] = {
    "name": "Wilson Disease",
    "primary_symptoms": ['insomnia', 'cough'],
    "secondary_symptoms": ['sleepiness'],
    "rare_symptoms": [],
    "symptom_weights": {'insomnia': 1.0, 'cough': 0.93, 'sleepiness': 0.64}
}
disease_map["CSV_0761"] = {
    "name": "Yeast Infection",
    "primary_symptoms": ['suprapubic_pain'],
    "secondary_symptoms": ['sharp_abdominal_pain', 'vaginal_itching', 'frequent_urination', 'vaginal_discharge', 'pelvic_pain', 'vaginal_pain', 'skin_rash', 'diaper_rash'],
    "rare_symptoms": [],
    "symptom_weights": {'suprapubic_pain': 0.72, 'sharp_abdominal_pain': 0.66, 'vaginal_itching': 0.54, 'frequent_urination': 0.67, 'vaginal_discharge': 0.54, 'pelvic_pain': 0.51, 'vaginal_pain': 0.52, 'skin_rash': 0.53, 'diaper_rash': 0.52}
}
disease_map["CSV_0762"] = {
    "name": "Zenker Diverticulum",
    "primary_symptoms": ['sharp_chest_pain', 'sore_throat', 'elbow_weakness'],
    "secondary_symptoms": [],
    "rare_symptoms": [],
    "symptom_weights": {'sharp_chest_pain': 0.82, 'sore_throat': 1.0, 'elbow_weakness': 0.91}
}
