# Disease-Symptom Mappings
# Format: {DiseaseID}: [{symptom_code, probability, is_primary}, ...]

disease_symptom_mapping = {
    # Respiratory
    "D001": [ # Common Cold
        {"symptom_code": "S001", "probability": 0.9, "is_primary": True}, # Cough
        {"symptom_code": "S005", "probability": 0.9, "is_primary": True}, # Runny nose
        {"symptom_code": "S008", "probability": 0.8, "is_primary": False}, # Sneezing
        {"symptom_code": "S004", "probability": 0.7, "is_primary": True}, # Sore throat
        {"symptom_code": "S070", "probability": 0.3, "is_primary": False}, # Fever
        {"symptom_code": "S071", "probability": 0.5, "is_primary": False}, # Fatigue
    ],
    "D002": [ # Influenza
        {"symptom_code": "S070", "probability": 0.9, "is_primary": True}, # Fever
        {"symptom_code": "S072", "probability": 0.8, "is_primary": True}, # Chills
        {"symptom_code": "S075", "probability": 0.9, "is_primary": True}, # Muscle pain
        {"symptom_code": "S001", "probability": 0.8, "is_primary": True}, # Cough
        {"symptom_code": "S071", "probability": 0.9, "is_primary": True}, # Fatigue
        {"symptom_code": "S030", "probability": 0.7, "is_primary": False}, # Headache
    ],
    "D003": [ # Asthma
        {"symptom_code": "S003", "probability": 0.9, "is_primary": True}, # Wheezing
        {"symptom_code": "S002", "probability": 0.9, "is_primary": True}, # Shortness of breath
        {"symptom_code": "S006", "probability": 0.8, "is_primary": True}, # Chest tightness
        {"symptom_code": "S001", "probability": 0.7, "is_primary": False}, # Cough
    ],
    "D004": [ # Pneumonia
        {"symptom_code": "S001", "probability": 0.9, "is_primary": True}, # Cough
        {"symptom_code": "S070", "probability": 0.9, "is_primary": True}, # Fever
        {"symptom_code": "S002", "probability": 0.8, "is_primary": True}, # Shortness of breath
        {"symptom_code": "S072", "probability": 0.7, "is_primary": False}, # Chills
        {"symptom_code": "S020", "probability": 0.6, "is_primary": False}, # Chest pain
    ],
    "D005": [ # COPD
        {"symptom_code": "S002", "probability": 0.9, "is_primary": True}, # Shortness of breath
        {"symptom_code": "S003", "probability": 0.8, "is_primary": True}, # Wheezing
        {"symptom_code": "S001", "probability": 0.9, "is_primary": True}, # Cough
        {"symptom_code": "S006", "probability": 0.6, "is_primary": False}, # Chest tightness
    ],
    "D006": [ # Tuberculosis
        {"symptom_code": "S001", "probability": 0.9, "is_primary": True}, # Cough > 3 weeks
        {"symptom_code": "S007", "probability": 0.6, "is_primary": True}, # Hemoptysis
        {"symptom_code": "S073", "probability": 0.7, "is_primary": True}, # Night sweats
        {"symptom_code": "S074", "probability": 0.8, "is_primary": True}, # Weight loss
        {"symptom_code": "S070", "probability": 0.6, "is_primary": False}, # Fever
    ],
    "D007": [ # Bronchitis
        {"symptom_code": "S001", "probability": 0.9, "is_primary": True}, # Cough
        {"symptom_code": "S071", "probability": 0.6, "is_primary": False}, # Fatigue
        {"symptom_code": "S002", "probability": 0.5, "is_primary": False}, # Shortness of breath
        {"symptom_code": "S070", "probability": 0.4, "is_primary": False}, # Fever
    ],
    "D008": [ # Covid-19
        {"symptom_code": "S070", "probability": 0.8, "is_primary": True}, # Fever
        {"symptom_code": "S001", "probability": 0.8, "is_primary": True}, # Cough
        {"symptom_code": "S057", "probability": 0.7, "is_primary": True}, # Loss of taste/smell (using appetite as proxy/related)
        {"symptom_code": "S071", "probability": 0.7, "is_primary": True}, # Fatigue
        {"symptom_code": "S002", "probability": 0.5, "is_primary": False}, # Shortness of breath
    ],

    # Cardiac
    "D009": [ # Hypertension
        {"symptom_code": "S030", "probability": 0.4, "is_primary": False}, # Headache
        {"symptom_code": "S002", "probability": 0.3, "is_primary": False}, # Shortness of breath
        {"symptom_code": "S021", "probability": 0.3, "is_primary": False}, # Palpitations
         # Often asymptomatic
    ],
    "D010": [ # Coronary Artery Disease
        {"symptom_code": "S020", "probability": 0.8, "is_primary": True}, # Chest pain
        {"symptom_code": "S002", "probability": 0.6, "is_primary": True}, # Shortness of breath
        {"symptom_code": "S071", "probability": 0.5, "is_primary": False}, # Fatigue
    ],
    "D011": [ # Heart Attack
        {"symptom_code": "S020", "probability": 0.95, "is_primary": True}, # Chest pain
        {"symptom_code": "S002", "probability": 0.8, "is_primary": True}, # Shortness of breath
        {"symptom_code": "S050", "probability": 0.6, "is_primary": False}, # Nausea
        {"symptom_code": "S031", "probability": 0.5, "is_primary": False}, # Dizziness
        {"symptom_code": "S073", "probability": 0.6, "is_primary": True}, # Cold sweat (mapped to night sweats/chills proxy)
        {"symptom_code": "S037", "probability": 0.4, "is_primary": True}, # Numbness (arm)
    ],
    "D012": [ # Arrhythmia
        {"symptom_code": "S021", "probability": 0.9, "is_primary": True}, # Palpitations
        {"symptom_code": "S022", "probability": 0.9, "is_primary": True}, # Irregular heartbeat
        {"symptom_code": "S031", "probability": 0.5, "is_primary": False}, # Dizziness
        {"symptom_code": "S145", "probability": 0.3, "is_primary": False}, # Fainting
    ],
    "D013": [ # Congestive Heart Failure
        {"symptom_code": "S002", "probability": 0.9, "is_primary": True}, # Shortness of breath
        {"symptom_code": "S023", "probability": 0.8, "is_primary": True}, # Edema
        {"symptom_code": "S071", "probability": 0.7, "is_primary": True}, # Fatigue
    ],
    
    # Digestive
    "D014": [ # Gastroenteritis
        {"symptom_code": "S053", "probability": 0.9, "is_primary": True}, # Diarrhea
        {"symptom_code": "S051", "probability": 0.8, "is_primary": True}, # Vomiting
        {"symptom_code": "S050", "probability": 0.8, "is_primary": True}, # Nausea
        {"symptom_code": "S052", "probability": 0.7, "is_primary": True}, # Abdominal pain
        {"symptom_code": "S070", "probability": 0.5, "is_primary": False}, # Fever
    ],
    "D015": [ # GERD
        {"symptom_code": "S055", "probability": 0.9, "is_primary": True}, # Heartburn
        {"symptom_code": "S020", "probability": 0.4, "is_primary": False}, # Chest pain
        {"symptom_code": "S050", "probability": 0.3, "is_primary": False}, # Nausea
    ],
    "D016": [ # Peptic Ulcer
        {"symptom_code": "S052", "probability": 0.8, "is_primary": True}, # Abdominal pain
        {"symptom_code": "S055", "probability": 0.6, "is_primary": False}, # Heartburn
        {"symptom_code": "S050", "probability": 0.5, "is_primary": False}, # Nausea
    ],
    "D017": [ # IBS
        {"symptom_code": "S052", "probability": 0.8, "is_primary": True}, # Abdominal pain
        {"symptom_code": "S056", "probability": 0.7, "is_primary": True}, # Bloating
        {"symptom_code": "S053", "probability": 0.6, "is_primary": True}, # Diarrhea (or const)
        {"symptom_code": "S054", "probability": 0.6, "is_primary": True}, # Constipation
    ],
    "D018": [ # Celiac
        {"symptom_code": "S053", "probability": 0.7, "is_primary": True}, # Diarrhea
        {"symptom_code": "S056", "probability": 0.6, "is_primary": True}, # Bloating
        {"symptom_code": "S074", "probability": 0.5, "is_primary": False}, # Weight loss
        {"symptom_code": "S071", "probability": 0.5, "is_primary": False}, # Fatigue
    ],
    "D019": [ # Cirrhosis
        {"symptom_code": "S059", "probability": 0.8, "is_primary": True}, # Jaundice
        {"symptom_code": "S071", "probability": 0.7, "is_primary": True}, # Fatigue
        {"symptom_code": "S023", "probability": 0.6, "is_primary": True}, # Edema
        {"symptom_code": "S163", "probability": 0.5, "is_primary": False}, # Easy bleeding
    ],
    "D020": [ # Appendicitis
        {"symptom_code": "S052", "probability": 0.95, "is_primary": True}, # Abdominal pain (RLQ)
        {"symptom_code": "S050", "probability": 0.7, "is_primary": True}, # Nausea
        {"symptom_code": "S070", "probability": 0.6, "is_primary": False}, # Fever
        {"symptom_code": "S057", "probability": 0.5, "is_primary": False}, # Loss of appetite
    ],

    # Neurological
    "D021": [ # Migraine
        {"symptom_code": "S030", "probability": 0.95, "is_primary": True}, # Headache
        {"symptom_code": "S050", "probability": 0.8, "is_primary": True}, # Nausea
        {"symptom_code": "S038", "probability": 0.6, "is_primary": True}, # Vision changes
    ],
    "D022": [ # Stroke
        {"symptom_code": "S037", "probability": 0.9, "is_primary": True}, # Numbness/Weakness
        {"symptom_code": "S033", "probability": 0.8, "is_primary": True}, # Confusion
        {"symptom_code": "S036", "probability": 0.8, "is_primary": True}, # Slurred speech
        {"symptom_code": "S038", "probability": 0.6, "is_primary": False}, # Vision changes
        {"symptom_code": "S146", "probability": 0.7, "is_primary": True}, # Balance problems
    ],
    "D023": [ # Epilepsy
        {"symptom_code": "S032", "probability": 0.95, "is_primary": True}, # Seizures
        {"symptom_code": "S033", "probability": 0.6, "is_primary": False}, # Confusion (post-ictal)
    ],
    "D024": [ # Alzheimer's
        {"symptom_code": "S034", "probability": 0.95, "is_primary": True}, # Memory loss
        {"symptom_code": "S033", "probability": 0.8, "is_primary": True}, # Confusion
    ],
    "D025": [ # Parkinson's
        {"symptom_code": "S035", "probability": 0.9, "is_primary": True}, # Tremors
        {"symptom_code": "S164", "probability": 0.8, "is_primary": True}, # Stiffness
        {"symptom_code": "S146", "probability": 0.7, "is_primary": True}, # Balance problems
    ],
    "D026": [ # MS
        {"symptom_code": "S037", "probability": 0.8, "is_primary": True}, # Numbness
        {"symptom_code": "S165", "probability": 0.7, "is_primary": True}, # Weakness
        {"symptom_code": "S038", "probability": 0.6, "is_primary": False}, # Vision changes
        {"symptom_code": "S071", "probability": 0.7, "is_primary": False}, # Fatigue
    ],

    # Endocrine
    "D027": [ # Diabetes T1
        {"symptom_code": "S120", "probability": 0.9, "is_primary": True}, # Excessive thirst
        {"symptom_code": "S111", "probability": 0.9, "is_primary": True}, # Frequent urination
        {"symptom_code": "S161", "probability": 0.8, "is_primary": True}, # Excessive hunger
        {"symptom_code": "S074", "probability": 0.8, "is_primary": True}, # Weight loss
    ],
    "D028": [ # Diabetes T2
        {"symptom_code": "S120", "probability": 0.7, "is_primary": True}, # Excessive thirst
        {"symptom_code": "S111", "probability": 0.7, "is_primary": True}, # Frequent urination
        {"symptom_code": "S071", "probability": 0.6, "is_primary": False}, # Fatigue
        {"symptom_code": "S162", "probability": 0.5, "is_primary": False}, # Slow wound healing
    ],
    "D029": [ # Hypothyroidism
        {"symptom_code": "S071", "probability": 0.9, "is_primary": True}, # Fatigue
        {"symptom_code": "S121", "probability": 0.8, "is_primary": True}, # Cold intolerance
        {"symptom_code": "S143", "probability": 0.7, "is_primary": True}, # Dry skin
         # Weight gain (no code yet, proxy logic omitted for brevity)
    ],
    "D030": [ # Hyperthyroidism
        {"symptom_code": "S074", "probability": 0.8, "is_primary": True}, # Weight loss
        {"symptom_code": "S122", "probability": 0.8, "is_primary": True}, # Heat intolerance
        {"symptom_code": "S021", "probability": 0.7, "is_primary": True}, # Palpitations
        {"symptom_code": "S150", "probability": 0.6, "is_primary": False}, # Mood swings
    ],

    # Infectious
    "D031": [ # Malaria
        {"symptom_code": "S070", "probability": 0.95, "is_primary": True}, # Fever
        {"symptom_code": "S072", "probability": 0.9, "is_primary": True}, # Chills
        {"symptom_code": "S030", "probability": 0.8, "is_primary": False}, # Headache
        {"symptom_code": "S050", "probability": 0.6, "is_primary": False}, # Nausea
    ],
    "D032": [ # Dengue
        {"symptom_code": "S070", "probability": 0.95, "is_primary": True}, # Fever
        {"symptom_code": "S030", "probability": 0.9, "is_primary": True}, # Headache
        {"symptom_code": "S133", "probability": 0.8, "is_primary": True}, # Eye pain (retro-orbital)
        {"symptom_code": "S076", "probability": 0.9, "is_primary": True}, # Joint pain
        {"symptom_code": "S090", "probability": 0.6, "is_primary": False}, # Rash
    ],
    "D033": [ # Typhoid
        {"symptom_code": "S070", "probability": 0.95, "is_primary": True}, # Fever
        {"symptom_code": "S052", "probability": 0.7, "is_primary": True}, # Abdominal pain
        {"symptom_code": "S030", "probability": 0.7, "is_primary": False}, # Headache
    ],
    "D034": [ # HIV
        {"symptom_code": "S070", "probability": 0.6, "is_primary": False}, # Fever (Acute)
        {"symptom_code": "S071", "probability": 0.6, "is_primary": False}, # Fatigue
        {"symptom_code": "S077", "probability": 0.5, "is_primary": False}, # Swollen lymph nodes
         # Long latency
    ],
    "D035": [ # Chickenpox
        {"symptom_code": "S090", "probability": 0.95, "is_primary": True}, # Rash
        {"symptom_code": "S091", "probability": 0.95, "is_primary": True}, # Itching
        {"symptom_code": "S070", "probability": 0.7, "is_primary": True}, # Fever
    ],

    # Skin
    "D036": [ # Eczema
        {"symptom_code": "S091", "probability": 0.9, "is_primary": True}, # Itching
        {"symptom_code": "S090", "probability": 0.9, "is_primary": True}, # Rash
        {"symptom_code": "S143", "probability": 0.8, "is_primary": True}, # Dry skin
    ],
    "D037": [ # Psoriasis
        {"symptom_code": "S090", "probability": 0.9, "is_primary": True}, # Rash (Scaly)
        {"symptom_code": "S143", "probability": 0.7, "is_primary": True}, # Dry skin
    ],
    "D038": [ # Acne
        {"symptom_code": "S142", "probability": 0.95, "is_primary": True}, # Acne spots
    ],
    "D039": [ # Melanoma
        {"symptom_code": "S092", "probability": 0.9, "is_primary": True}, # Lesions (Mole changes)
    ],
    "D040": [ # Dermatitis
        {"symptom_code": "S090", "probability": 0.9, "is_primary": True}, # Rash
        {"symptom_code": "S091", "probability": 0.8, "is_primary": True}, # Itching
    ],

    # Mental
    "D041": [ # Depression
        {"symptom_code": "S101", "probability": 0.95, "is_primary": True}, # Depressed mood
        {"symptom_code": "S071", "probability": 0.8, "is_primary": True}, # Fatigue
        {"symptom_code": "S102", "probability": 0.7, "is_primary": True}, # Insomnia
        {"symptom_code": "S152", "probability": 0.4, "is_primary": False}, # Suicidal thoughts
    ],
    "D042": [ # GAD
        {"symptom_code": "S100", "probability": 0.95, "is_primary": True}, # Anxiety
        {"symptom_code": "S149", "probability": 0.7, "is_primary": True}, # Restlessness
        {"symptom_code": "S071", "probability": 0.6, "is_primary": False}, # Fatigue
    ],
    "D043": [ # Schizophrenia
        {"symptom_code": "S103", "probability": 0.9, "is_primary": True}, # Hallucinations
        {"symptom_code": "S151", "probability": 0.8, "is_primary": True}, # Paranoia
        {"symptom_code": "S033", "probability": 0.7, "is_primary": False}, # Confusion
    ],
    "D044": [ # Bipolar
        {"symptom_code": "S150", "probability": 0.95, "is_primary": True}, # Mood swings
        {"symptom_code": "S101", "probability": 0.8, "is_primary": True}, # Depressed mood
    ],
    "D045": [ # Panic Disorder
        {"symptom_code": "S153", "probability": 0.95, "is_primary": True}, # Panic attacks
        {"symptom_code": "S021", "probability": 0.8, "is_primary": True}, # Palpitations
        {"symptom_code": "S002", "probability": 0.7, "is_primary": False}, # Shortness of breath
    ],

    # Musculoskeletal
    "D046": [ # Osteoarthritis
        {"symptom_code": "S076", "probability": 0.9, "is_primary": True}, # Joint pain
        {"symptom_code": "S164", "probability": 0.8, "is_primary": True}, # Stiffness
        {"symptom_code": "S168", "probability": 0.7, "is_primary": True}, # Limited ROM
    ],
    "D047": [ # Rheumatoid Arthritis
        {"symptom_code": "S076", "probability": 0.9, "is_primary": True}, # Joint pain
        {"symptom_code": "S167", "probability": 0.8, "is_primary": True}, # Swollen joints
        {"symptom_code": "S164", "probability": 0.8, "is_primary": True}, # Stiffness (morning)
    ],
    "D048": [ # Osteoporosis
        {"symptom_code": "S130", "probability": 0.6, "is_primary": False}, # Back pain
         # Often asymptomatic until fracture
    ],
    "D049": [ # Fibromyalgia
        {"symptom_code": "S075", "probability": 0.9, "is_primary": True}, # Muscle pain
        {"symptom_code": "S071", "probability": 0.9, "is_primary": True}, # Fatigue
    ],
    "D050": [ # Gout
        {"symptom_code": "S076", "probability": 0.9, "is_primary": True}, # Joint pain
        {"symptom_code": "S167", "probability": 0.9, "is_primary": True}, # Swollen joints
    ],

    # Urinary
    "D051": [ # UTI
        {"symptom_code": "S110", "probability": 0.9, "is_primary": True}, # Dysuria
        {"symptom_code": "S111", "probability": 0.8, "is_primary": True}, # Frequent urination
    ],
    "D052": [ # Kidney Stones
        {"symptom_code": "S160", "probability": 0.9, "is_primary": True}, # Flank pain
        {"symptom_code": "S112", "probability": 0.7, "is_primary": True}, # Hematuria
        {"symptom_code": "S050", "probability": 0.6, "is_primary": False}, # Nausea
    ],
    "D053": [ # CKD
        {"symptom_code": "S071", "probability": 0.7, "is_primary": True}, # Fatigue
        {"symptom_code": "S023", "probability": 0.6, "is_primary": False}, # Edema
        {"symptom_code": "S111", "probability": 0.5, "is_primary": False}, # Frequent urination (or bubbles)
    ],

    # Others
    "D054": [ # Anemia
        {"symptom_code": "S071", "probability": 0.9, "is_primary": True}, # Fatigue
        {"symptom_code": "S093", "probability": 0.8, "is_primary": True}, # Pallor
        {"symptom_code": "S002", "probability": 0.6, "is_primary": False}, # Shortness of breath
    ],
    "D055": [ # Allergies
        {"symptom_code": "S008", "probability": 0.8, "is_primary": True}, # Sneezing
        {"symptom_code": "S005", "probability": 0.8, "is_primary": True}, # Runny nose
        {"symptom_code": "S091", "probability": 0.6, "is_primary": False}, # Itching
    ],
    "D056": [ # Food Poisoning
        {"symptom_code": "S051", "probability": 0.9, "is_primary": True}, # Vomiting
        {"symptom_code": "S053", "probability": 0.9, "is_primary": True}, # Diarrhea
        {"symptom_code": "S052", "probability": 0.8, "is_primary": True}, # Abdominal pain
    ],
    "D057": [ # Lyme
        {"symptom_code": "S090", "probability": 0.7, "is_primary": True}, # Rash (Bullseye)
        {"symptom_code": "S076", "probability": 0.6, "is_primary": False}, # Joint pain
        {"symptom_code": "S071", "probability": 0.6, "is_primary": False}, # Fatigue
    ],
    "D058": [ # Meningitis
        {"symptom_code": "S030", "probability": 0.9, "is_primary": True}, # Headache
        {"symptom_code": "S164", "probability": 0.8, "is_primary": True}, # Stiffness (Neck)
        {"symptom_code": "S070", "probability": 0.8, "is_primary": True}, # Fever
    ],
    "D059": [ # Glaucoma
        {"symptom_code": "S038", "probability": 0.6, "is_primary": True}, # Vision changes
        {"symptom_code": "S133", "probability": 0.5, "is_primary": False}, # Eye pain (acute)
    ],
    "D060": [ # Conjunctivitis
        {"symptom_code": "S134", "probability": 0.9, "is_primary": True}, # Red eye
        {"symptom_code": "S091", "probability": 0.7, "is_primary": False}, # Itching
    ],
    "D061": [ # Otitis Media
        {"symptom_code": "S132", "probability": 0.9, "is_primary": True}, # Ear pain
        {"symptom_code": "S070", "probability": 0.5, "is_primary": False}, # Fever
    ],
    "D062": [ # Tonsillitis
        {"symptom_code": "S004", "probability": 0.95, "is_primary": True}, # Sore throat
        {"symptom_code": "S070", "probability": 0.6, "is_primary": False}, # Fever
    ],
}
