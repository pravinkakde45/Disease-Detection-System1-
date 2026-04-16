# Master Symptom Knowledge Base
# Format: {symptom_code}: {name, category, severity, question_text, description}

symptoms = {
    # Respiratory
    "cough": {
        "name": "Cough",
        "category": "Respiratory",
        "severity": "mild",
        "question_text": "Do you have a cough?",
        "description": "Sudden, forceful hacking sound to release air."
    },
    "shortness_of_breath": {
        "name": "Shortness of Breath",
        "category": "Respiratory",
        "severity": "severe",
        "question_text": "Are you feeling short of breath or difficulty breathing?",
        "description": "Sensation of not being able to get enough air."
    },
    "wheezing": {
        "name": "Wheezing",
        "category": "Respiratory",
        "severity": "moderate",
        "question_text": "Do you hear a whistling sound when you breathe?",
        "description": "High-pitched whistling sound."
    },
    "sore_throat": {
        "name": "Sore Throat",
        "category": "Respiratory",
        "severity": "mild",
        "question_text": "Do you have a sore or scratchy throat?",
        "description": "Pain or irritation of the throat."
    },
    "runny_nose": {
        "name": "Runny Nose",
        "category": "Respiratory",
        "severity": "mild",
        "question_text": "Do you have a runny or stuffy nose?",
        "description": "Excess drainage from the nose."
    },
    "chest_tightness": {
        "name": "Chest Tightness",
        "category": "Respiratory",
        "severity": "moderate",
        "question_text": "Do you feel tightness or pressure in your chest?",
        "description": "Feeling of pressure in the chest."
    },
    "hemoptysis": {
        "name": "Coughing up Blood",
        "category": "Respiratory",
        "severity": "severe",
        "question_text": "Are you coughing up blood?",
        "description": "Coughing up blood or blood-stained mucus."
    },
    "sneezing": {
        "name": "Sneezing",
        "category": "Respiratory",
        "severity": "mild",
        "question_text": "Are you sneezing frequently?",
        "description": "Involuntary expulsion of air from nose/mouth."
    },

    # Cardiac
    "chest_pain": {
        "name": "Chest Pain",
        "category": "Cardiac",
        "severity": "severe",
        "question_text": "Are you experiencing pain or discomfort in your chest?",
        "description": "Discomfort in the chest area."
    },
    "palpitations": {
        "name": "Palpitations",
        "category": "Cardiac",
        "severity": "moderate",
        "question_text": "Do you feel like your heart is racing or pounding?",
        "description": "Rapid, strong, or irregular heartbeat."
    },
    "irregular_heartbeat": {
        "name": "Irregular Heartbeat",
        "category": "Cardiac",
        "severity": "moderate",
        "question_text": "Does your heartbeat feel irregular?",
        "description": "Heart beating too fast, too slow, or skipping beats."
    },
    "edema": {
        "name": "Leg Swelling (Edema)",
        "category": "Cardiac",
        "severity": "moderate",
        "question_text": "Do you have swelling in your legs or ankles?",
        "description": "Swelling caused by excess fluid."
    },

    # Neurological
    "headache": {
        "name": "Headache",
        "category": "Neurological",
        "severity": "moderate",
        "question_text": "Do you have a headache?",
        "description": "Pain in the head or upper neck."
    },
    "dizziness": {
        "name": "Dizziness",
        "category": "Neurological",
        "severity": "moderate",
        "question_text": "Do you feel dizzy or lightheaded?",
        "description": "Sensation of spinning or losing balance."
    },
    "seizures": {
        "name": "Seizures",
        "category": "Neurological",
        "severity": "severe",
        "question_text": "Have you experienced a seizure or convulsion?",
        "description": "Uncontrolled electrical disturbance in the brain."
    },
    "confusion": {
        "name": "Confusion",
        "category": "Neurological",
        "severity": "severe",
        "question_text": "Are you feeling confused or disoriented?",
        "description": "Lack of clarity in thought."
    },
    "memory_loss": {
        "name": "Memory Loss",
        "category": "Neurological",
        "severity": "moderate",
        "question_text": "Are you experiencing memory problems?",
        "description": "Unusual forgetfulness."
    },
    "tremors": {
        "name": "Tremors",
        "category": "Neurological",
        "severity": "moderate",
        "question_text": "Do you have shaking hands or tremors?",
        "description": "Involuntary shaking movements."
    },
    "slurred_speech": {
        "name": "Slurred Speech",
        "category": "Neurological",
        "severity": "severe",
        "question_text": "Is your speech slurred or difficult to understand?",
        "description": "Poor pronunciation or change in rhythm of speech."
    },
    "numbness": {
        "name": "Numbness",
        "category": "Neurological",
        "severity": "moderate",
        "question_text": "Do you have numbness or loss of sensation in any body part?",
        "description": "Loss of sensation."
    },
    "vision_changes": {
        "name": "Vision Changes",
        "category": "Neurological",
        "severity": "moderate",
        "question_text": "Have you noticed any changes in your vision?",
        "description": "Blurriness, double vision, or loss of vision."
    },
    "balance_problems": {
        "name": "Balance Problems",
        "category": "Neurological",
        "severity": "moderate",
        "question_text": "Are you having trouble keeping your balance?",
        "description": "Feeling unsteady."
    },

    # Digestive
    "nausea": {
        "name": "Nausea",
        "category": "Digestive",
        "severity": "moderate",
        "question_text": "Are you feeling nauseous?",
        "description": "Unease of the stomach."
    },
    "vomiting": {
        "name": "Vomiting",
        "category": "Digestive",
        "severity": "moderate",
        "question_text": "have you been vomiting?",
        "description": "Involuntary emptying of stomach."
    },
    "abdominal_pain": {
        "name": "Abdominal Pain",
        "category": "Digestive",
        "severity": "moderate",
        "question_text": "Do you have pain in your stomach or abdomen?",
        "description": "Pain between chest and pelvis."
    },
    "diarrhea": {
        "name": "Diarrhea",
        "category": "Digestive",
        "severity": "moderate",
        "question_text": "Do you have loose or watery stools?",
        "description": "Frequent loose stools."
    },
    "constipation": {
        "name": "Constipation",
        "category": "Digestive",
        "severity": "mild",
        "question_text": "Are you constipated or having trouble passing stool?",
        "description": "Infrequent bowel movements."
    },
    "heartburn": {
        "name": "Heartburn",
        "category": "Digestive",
        "severity": "mild",
        "question_text": "Do you feel a burning sensation in your chest after eating?",
        "description": "Burning pain in the chest."
    },
    "bloating": {
        "name": "Bloating",
        "category": "Digestive",
        "severity": "mild",
        "question_text": "Do you feel bloated or full?",
        "description": "Feeling of fullness in abdomen."
    },
    "blood_in_stool": {
        "name": "Blood in Stool",
        "category": "Digestive",
        "severity": "severe",
        "question_text": "Have you noticed blood in your stool?",
        "description": "Blood passed from the anus."
    },
    "jaundice": {
        "name": "Jaundice",
        "category": "Digestive",
        "severity": "severe",
        "question_text": "Is your skin or eyes yellowing?",
        "description": "Yellowing of skin and eyes."
    },

    # Systemic / General
    "fever": {
        "name": "Fever",
        "category": "General",
        "severity": "moderate",
        "question_text": "Do you have a fever or high temperature?",
        "description": "Increased body temperature."
    },
    "fatigue": {
        "name": "Fatigue",
        "category": "General",
        "severity": "moderate",
        "question_text": "Are you feeling unusually tired or weak?",
        "description": "Constant tiredness."
    },
    "chills": {
        "name": "Chills",
        "category": "General",
        "severity": "moderate",
        "question_text": "Do you have chills or shivering?",
        "description": "Feeling cold and shivering."
    },
    "night_sweats": {
        "name": "Night Sweats",
        "category": "General",
        "severity": "moderate",
        "question_text": "Do you sweat heavily at night?",
        "description": "Episodes of extreme perspiration."
    },
    "weight_loss": {
        "name": "Unexplained Weight Loss",
        "category": "General",
        "severity": "moderate",
        "question_text": "Have you lost weight without trying?",
        "description": "Involuntary decrease in weight."
    },
    "muscle_pain": {
        "name": "Muscle Pain",
        "category": "Musculoskeletal",
        "severity": "mild",
        "question_text": "Do you have aching muscles?",
        "description": "Pain in muscles."
    },
    "joint_pain": {
        "name": "Joint Pain",
        "category": "Musculoskeletal",
        "severity": "moderate",
        "question_text": "Do your joints hurt?",
        "description": "Discomfort in joints."
    },

    # Skin
    "rash": {
        "name": "Rash",
        "category": "Skin",
        "severity": "mild",
        "question_text": "Do you have a rash on your skin?",
        "description": "Change in skin texture or color."
    },
    "itching": {
        "name": "Itching",
        "category": "Skin",
        "severity": "mild",
        "question_text": "Is your skin itching?",
        "description": "Desire to scratch skin."
    },
    "dry_skin": {
        "name": "Dry Skin",
        "category": "Skin",
        "severity": "mild",
        "question_text": "Is your skin feeling dry or rough?",
        "description": "Rough, scaly skin."
    },
    "pallor": {
        "name": "Pale Skin",
        "category": "Skin",
        "severity": "moderate",
        "question_text": "Is your skin unusually pale?",
        "description": "Lightness of skin color."
    },
    "easy_bleeding": {
        "name": "Bleeding Easily",
        "category": "Skin",
        "severity": "moderate",
        "question_text": "Do you bleed or bruise easily?",
        "description": "Bleeding from minor cuts/gums."
    },
    "acne": {
        "name": "Acne",
        "category": "Skin",
        "severity": "mild",
        "question_text": "Do you have pimples or acne?",
        "description": "Plugged hair follicles."
    },

    # Mental
    "anxiety": {
        "name": "Anxiety",
        "category": "Mental",
        "severity": "moderate",
        "question_text": "Are you feeling anxious or worried?",
        "description": "Feeling of worry/nervousness."
    },
    "depressed_mood": {
        "name": "Depressed Mood",
        "category": "Mental",
        "severity": "moderate",
        "question_text": "Are you feeling down, depressed, or hopeless?",
        "description": "Sadness or loss of interest."
    },
    "mood_swings": {
        "name": "Mood Swings",
        "category": "Mental",
        "severity": "moderate",
        "question_text": "Are you experiencing rapid changes in your mood?",
        "description": "Rapid mood changes."
    },
    "insomnia": {
        "name": "Insomnia",
        "category": "Mental",
        "severity": "mild",
        "question_text": "Are you having trouble sleeping?",
        "description": "Habitual sleeplessness."
    },

    # Urinary / Endocrine
    "frequent_urination": {
        "name": "Frequent Urination",
        "category": "Urinary",
        "severity": "moderate",
        "question_text": "Are you urinating more often than usual?",
        "description": "Needing to urinate often."
    },
    "painful_urination": {
        "name": "Painful Urination",
        "category": "Urinary",
        "severity": "moderate",
        "question_text": "Does it hurt when you urinate?",
        "description": "Dysuria."
    },
    "excessive_thirst": {
        "name": "Excessive Thirst",
        "category": "Endocrine",
        "severity": "moderate",
        "question_text": "Are you feeling extremely thirsty?",
        "description": "Polydipsia."
    },
    "cold_intolerance": {
        "name": "Cold Intolerance",
        "category": "Endocrine",
        "severity": "moderate",
        "question_text": "Do you feel colder than others in the same room?",
        "description": "Sensitivity to cold."
    },
    "heat_intolerance": {
        "name": "Heat Intolerance",
        "category": "Endocrine",
        "severity": "moderate",
        "question_text": "Do you feel uncomfortably hot when others are fine?",
        "description": "Sensitivity to heat."
    },
    
    # Other
    "stiff_neck": {
        "name": "Stiff Neck",
        "category": "Musculoskeletal",
        "severity": "moderate",
        "question_text": "Is your neck stiff or painful to move?",
        "description": "Stiffness in neck muscles."
    },
    "joint_swelling": {
        "name": "Joint Swelling",
        "category": "Musculoskeletal",
        "severity": "moderate",
        "question_text": "Are your joints swollen?",
        "description": "Enlarged joints."
    },
    "back_pain": {
        "name": "Back Pain",
        "category": "Musculoskeletal",
        "severity": "moderate",
        "question_text": "Do you have pain in your back?",
        "description": "Discomfort in the back."
    },
    "loss_of_smell": {
        "name": "Loss of Smell/Taste",
        "category": "Sensory",
        "severity": "mild",
        "question_text": "Have you lost your sense of smell or taste?",
        "description": "Anosmia or ageusia."
    }
}

# --- Auto-merged from CSV ---
symptoms["anxiety_and_nervousness"] = {
    "name": "Anxiety And Nervousness",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have anxiety and nervousness?",
    "description": "Imported from CSV."
}
symptoms["depression"] = {
    "name": "Depression",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have depression?",
    "description": "Imported from CSV."
}
symptoms["depressive_or_psychotic_symptoms"] = {
    "name": "Depressive Or Psychotic Symptoms",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have depressive or psychotic symptoms?",
    "description": "Imported from CSV."
}
symptoms["sharp_chest_pain"] = {
    "name": "Sharp Chest Pain",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have sharp chest pain?",
    "description": "Imported from CSV."
}
symptoms["abnormal_involuntary_movements"] = {
    "name": "Abnormal Involuntary Movements",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have abnormal involuntary movements?",
    "description": "Imported from CSV."
}
symptoms["breathing_fast"] = {
    "name": "Breathing Fast",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have breathing fast?",
    "description": "Imported from CSV."
}
symptoms["hoarse_voice"] = {
    "name": "Hoarse Voice",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have hoarse voice?",
    "description": "Imported from CSV."
}
symptoms["difficulty_speaking"] = {
    "name": "Difficulty Speaking",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have difficulty speaking?",
    "description": "Imported from CSV."
}
symptoms["nasal_congestion"] = {
    "name": "Nasal Congestion",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have nasal congestion?",
    "description": "Imported from CSV."
}
symptoms["throat_swelling"] = {
    "name": "Throat Swelling",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have throat swelling?",
    "description": "Imported from CSV."
}
symptoms["diminished_hearing"] = {
    "name": "Diminished Hearing",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have diminished hearing?",
    "description": "Imported from CSV."
}
symptoms["lump_in_throat"] = {
    "name": "Lump In Throat",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have lump in throat?",
    "description": "Imported from CSV."
}
symptoms["throat_feels_tight"] = {
    "name": "Throat Feels Tight",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have throat feels tight?",
    "description": "Imported from CSV."
}
symptoms["difficulty_in_swallowing"] = {
    "name": "Difficulty In Swallowing",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have difficulty in swallowing?",
    "description": "Imported from CSV."
}
symptoms["skin_swelling"] = {
    "name": "Skin Swelling",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have skin swelling?",
    "description": "Imported from CSV."
}
symptoms["retention_of_urine"] = {
    "name": "Retention Of Urine",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have retention of urine?",
    "description": "Imported from CSV."
}
symptoms["groin_mass"] = {
    "name": "Groin Mass",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have groin mass?",
    "description": "Imported from CSV."
}
symptoms["leg_pain"] = {
    "name": "Leg Pain",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have leg pain?",
    "description": "Imported from CSV."
}
symptoms["hip_pain"] = {
    "name": "Hip Pain",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have hip pain?",
    "description": "Imported from CSV."
}
symptoms["suprapubic_pain"] = {
    "name": "Suprapubic Pain",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have suprapubic pain?",
    "description": "Imported from CSV."
}
symptoms["lack_of_growth"] = {
    "name": "Lack Of Growth",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have lack of growth?",
    "description": "Imported from CSV."
}
symptoms["emotional_symptoms"] = {
    "name": "Emotional Symptoms",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have emotional symptoms?",
    "description": "Imported from CSV."
}
symptoms["elbow_weakness"] = {
    "name": "Elbow Weakness",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have elbow weakness?",
    "description": "Imported from CSV."
}
symptoms["back_weakness"] = {
    "name": "Back Weakness",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have back weakness?",
    "description": "Imported from CSV."
}
symptoms["pus_in_sputum"] = {
    "name": "Pus In Sputum",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have pus in sputum?",
    "description": "Imported from CSV."
}
symptoms["symptoms_of_the_scrotum_and_testes"] = {
    "name": "Symptoms Of The Scrotum And Testes",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have symptoms of the scrotum and testes?",
    "description": "Imported from CSV."
}
symptoms["swelling_of_scrotum"] = {
    "name": "Swelling Of Scrotum",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have swelling of scrotum?",
    "description": "Imported from CSV."
}
symptoms["pain_in_testicles"] = {
    "name": "Pain In Testicles",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have pain in testicles?",
    "description": "Imported from CSV."
}
symptoms["flatulence"] = {
    "name": "Flatulence",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have flatulence?",
    "description": "Imported from CSV."
}
symptoms["pus_draining_from_ear"] = {
    "name": "Pus Draining From Ear",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have pus draining from ear?",
    "description": "Imported from CSV."
}
symptoms["mass_in_scrotum"] = {
    "name": "Mass In Scrotum",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have mass in scrotum?",
    "description": "Imported from CSV."
}
symptoms["white_discharge_from_eye"] = {
    "name": "White Discharge From Eye",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have white discharge from eye?",
    "description": "Imported from CSV."
}
symptoms["irritable_infant"] = {
    "name": "Irritable Infant",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have irritable infant?",
    "description": "Imported from CSV."
}
symptoms["abusing_alcohol"] = {
    "name": "Abusing Alcohol",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have abusing alcohol?",
    "description": "Imported from CSV."
}
symptoms["fainting"] = {
    "name": "Fainting",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have fainting?",
    "description": "Imported from CSV."
}
symptoms["hostile_behavior"] = {
    "name": "Hostile Behavior",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have hostile behavior?",
    "description": "Imported from CSV."
}
symptoms["drug_abuse"] = {
    "name": "Drug Abuse",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have drug abuse?",
    "description": "Imported from CSV."
}
symptoms["sharp_abdominal_pain"] = {
    "name": "Sharp Abdominal Pain",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have sharp abdominal pain?",
    "description": "Imported from CSV."
}
symptoms["feeling_ill"] = {
    "name": "Feeling Ill",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have feeling ill?",
    "description": "Imported from CSV."
}
symptoms["vaginal_itching"] = {
    "name": "Vaginal Itching",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have vaginal itching?",
    "description": "Imported from CSV."
}
symptoms["vaginal_dryness"] = {
    "name": "Vaginal Dryness",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have vaginal dryness?",
    "description": "Imported from CSV."
}
symptoms["involuntary_urination"] = {
    "name": "Involuntary Urination",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have involuntary urination?",
    "description": "Imported from CSV."
}
symptoms["pain_during_intercourse"] = {
    "name": "Pain During Intercourse",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have pain during intercourse?",
    "description": "Imported from CSV."
}
symptoms["lower_abdominal_pain"] = {
    "name": "Lower Abdominal Pain",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have lower abdominal pain?",
    "description": "Imported from CSV."
}
symptoms["vaginal_discharge"] = {
    "name": "Vaginal Discharge",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have vaginal discharge?",
    "description": "Imported from CSV."
}
symptoms["blood_in_urine"] = {
    "name": "Blood In Urine",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have blood in urine?",
    "description": "Imported from CSV."
}
symptoms["hot_flashes"] = {
    "name": "Hot Flashes",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have hot flashes?",
    "description": "Imported from CSV."
}
symptoms["intermenstrual_bleeding"] = {
    "name": "Intermenstrual Bleeding",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have intermenstrual bleeding?",
    "description": "Imported from CSV."
}
symptoms["hand_or_finger_pain"] = {
    "name": "Hand Or Finger Pain",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have hand or finger pain?",
    "description": "Imported from CSV."
}
symptoms["wrist_pain"] = {
    "name": "Wrist Pain",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have wrist pain?",
    "description": "Imported from CSV."
}
symptoms["hand_or_finger_swelling"] = {
    "name": "Hand Or Finger Swelling",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have hand or finger swelling?",
    "description": "Imported from CSV."
}
symptoms["arm_pain"] = {
    "name": "Arm Pain",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have arm pain?",
    "description": "Imported from CSV."
}
symptoms["wrist_swelling"] = {
    "name": "Wrist Swelling",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have wrist swelling?",
    "description": "Imported from CSV."
}
symptoms["arm_stiffness_or_tightness"] = {
    "name": "Arm Stiffness Or Tightness",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have arm stiffness or tightness?",
    "description": "Imported from CSV."
}
symptoms["arm_swelling"] = {
    "name": "Arm Swelling",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have arm swelling?",
    "description": "Imported from CSV."
}
symptoms["hand_or_finger_stiffness_or_tightness"] = {
    "name": "Hand Or Finger Stiffness Or Tightness",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have hand or finger stiffness or tightness?",
    "description": "Imported from CSV."
}
symptoms["wrist_stiffness_or_tightness"] = {
    "name": "Wrist Stiffness Or Tightness",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have wrist stiffness or tightness?",
    "description": "Imported from CSV."
}
symptoms["lip_swelling"] = {
    "name": "Lip Swelling",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have lip swelling?",
    "description": "Imported from CSV."
}
symptoms["toothache"] = {
    "name": "Toothache",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have toothache?",
    "description": "Imported from CSV."
}
symptoms["abnormal_appearing_skin"] = {
    "name": "Abnormal Appearing Skin",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have abnormal appearing skin?",
    "description": "Imported from CSV."
}
symptoms["skin_lesion"] = {
    "name": "Skin Lesion",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have skin lesion?",
    "description": "Imported from CSV."
}
symptoms["acne_or_pimples"] = {
    "name": "Acne Or Pimples",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have acne or pimples?",
    "description": "Imported from CSV."
}
symptoms["dry_lips"] = {
    "name": "Dry Lips",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have dry lips?",
    "description": "Imported from CSV."
}
symptoms["facial_pain"] = {
    "name": "Facial Pain",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have facial pain?",
    "description": "Imported from CSV."
}
symptoms["mouth_ulcer"] = {
    "name": "Mouth Ulcer",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have mouth ulcer?",
    "description": "Imported from CSV."
}
symptoms["skin_growth"] = {
    "name": "Skin Growth",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have skin growth?",
    "description": "Imported from CSV."
}
symptoms["eye_deviation"] = {
    "name": "Eye Deviation",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have eye deviation?",
    "description": "Imported from CSV."
}
symptoms["diminished_vision"] = {
    "name": "Diminished Vision",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have diminished vision?",
    "description": "Imported from CSV."
}
symptoms["double_vision"] = {
    "name": "Double Vision",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have double vision?",
    "description": "Imported from CSV."
}
symptoms["cross_eyed"] = {
    "name": "Cross-Eyed",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have cross-eyed?",
    "description": "Imported from CSV."
}
symptoms["symptoms_of_eye"] = {
    "name": "Symptoms Of Eye",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have symptoms of eye?",
    "description": "Imported from CSV."
}
symptoms["pain_in_eye"] = {
    "name": "Pain In Eye",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have pain in eye?",
    "description": "Imported from CSV."
}
symptoms["eye_moves_abnormally"] = {
    "name": "Eye Moves Abnormally",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have eye moves abnormally?",
    "description": "Imported from CSV."
}
symptoms["abnormal_movement_of_eyelid"] = {
    "name": "Abnormal Movement Of Eyelid",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have abnormal movement of eyelid?",
    "description": "Imported from CSV."
}
symptoms["foreign_body_sensation_in_eye"] = {
    "name": "Foreign Body Sensation In Eye",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have foreign body sensation in eye?",
    "description": "Imported from CSV."
}
symptoms["irregular_appearing_scalp"] = {
    "name": "Irregular Appearing Scalp",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have irregular appearing scalp?",
    "description": "Imported from CSV."
}
symptoms["swollen_lymph_nodes"] = {
    "name": "Swollen Lymph Nodes",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have swollen lymph nodes?",
    "description": "Imported from CSV."
}
symptoms["neck_pain"] = {
    "name": "Neck Pain",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have neck pain?",
    "description": "Imported from CSV."
}
symptoms["low_back_pain"] = {
    "name": "Low Back Pain",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have low back pain?",
    "description": "Imported from CSV."
}
symptoms["pain_of_the_anus"] = {
    "name": "Pain Of The Anus",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have pain of the anus?",
    "description": "Imported from CSV."
}
symptoms["pain_during_pregnancy"] = {
    "name": "Pain During Pregnancy",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have pain during pregnancy?",
    "description": "Imported from CSV."
}
symptoms["pelvic_pain"] = {
    "name": "Pelvic Pain",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have pelvic pain?",
    "description": "Imported from CSV."
}
symptoms["impotence"] = {
    "name": "Impotence",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have impotence?",
    "description": "Imported from CSV."
}
symptoms["infant_spitting_up"] = {
    "name": "Infant Spitting Up",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have infant spitting up?",
    "description": "Imported from CSV."
}
symptoms["vomiting_blood"] = {
    "name": "Vomiting Blood",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have vomiting blood?",
    "description": "Imported from CSV."
}
symptoms["regurgitation"] = {
    "name": "Regurgitation",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have regurgitation?",
    "description": "Imported from CSV."
}
symptoms["burning_abdominal_pain"] = {
    "name": "Burning Abdominal Pain",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have burning abdominal pain?",
    "description": "Imported from CSV."
}
symptoms["restlessness"] = {
    "name": "Restlessness",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have restlessness?",
    "description": "Imported from CSV."
}
symptoms["symptoms_of_infants"] = {
    "name": "Symptoms Of Infants",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have symptoms of infants?",
    "description": "Imported from CSV."
}
symptoms["peripheral_edema"] = {
    "name": "Peripheral Edema",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have peripheral edema?",
    "description": "Imported from CSV."
}
symptoms["neck_mass"] = {
    "name": "Neck Mass",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have neck mass?",
    "description": "Imported from CSV."
}
symptoms["ear_pain"] = {
    "name": "Ear Pain",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have ear pain?",
    "description": "Imported from CSV."
}
symptoms["jaw_swelling"] = {
    "name": "Jaw Swelling",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have jaw swelling?",
    "description": "Imported from CSV."
}
symptoms["mouth_dryness"] = {
    "name": "Mouth Dryness",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have mouth dryness?",
    "description": "Imported from CSV."
}
symptoms["neck_swelling"] = {
    "name": "Neck Swelling",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have neck swelling?",
    "description": "Imported from CSV."
}
symptoms["knee_pain"] = {
    "name": "Knee Pain",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have knee pain?",
    "description": "Imported from CSV."
}
symptoms["foot_or_toe_pain"] = {
    "name": "Foot Or Toe Pain",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have foot or toe pain?",
    "description": "Imported from CSV."
}
symptoms["bowlegged_or_knock_kneed"] = {
    "name": "Bowlegged Or Knock-Kneed",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have bowlegged or knock-kneed?",
    "description": "Imported from CSV."
}
symptoms["ankle_pain"] = {
    "name": "Ankle Pain",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have ankle pain?",
    "description": "Imported from CSV."
}
symptoms["bones_are_painful"] = {
    "name": "Bones Are Painful",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have bones are painful?",
    "description": "Imported from CSV."
}
symptoms["knee_weakness"] = {
    "name": "Knee Weakness",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have knee weakness?",
    "description": "Imported from CSV."
}
symptoms["elbow_pain"] = {
    "name": "Elbow Pain",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have elbow pain?",
    "description": "Imported from CSV."
}
symptoms["knee_swelling"] = {
    "name": "Knee Swelling",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have knee swelling?",
    "description": "Imported from CSV."
}
symptoms["skin_moles"] = {
    "name": "Skin Moles",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have skin moles?",
    "description": "Imported from CSV."
}
symptoms["knee_lump_or_mass"] = {
    "name": "Knee Lump Or Mass",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have knee lump or mass?",
    "description": "Imported from CSV."
}
symptoms["weight_gain"] = {
    "name": "Weight Gain",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have weight gain?",
    "description": "Imported from CSV."
}
symptoms["problems_with_movement"] = {
    "name": "Problems With Movement",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have problems with movement?",
    "description": "Imported from CSV."
}
symptoms["knee_stiffness_or_tightness"] = {
    "name": "Knee Stiffness Or Tightness",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have knee stiffness or tightness?",
    "description": "Imported from CSV."
}
symptoms["leg_swelling"] = {
    "name": "Leg Swelling",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have leg swelling?",
    "description": "Imported from CSV."
}
symptoms["foot_or_toe_swelling"] = {
    "name": "Foot Or Toe Swelling",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have foot or toe swelling?",
    "description": "Imported from CSV."
}
symptoms["smoking_problems"] = {
    "name": "Smoking Problems",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have smoking problems?",
    "description": "Imported from CSV."
}
symptoms["infant_feeding_problem"] = {
    "name": "Infant Feeding Problem",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have infant feeding problem?",
    "description": "Imported from CSV."
}
symptoms["recent_weight_loss"] = {
    "name": "Recent Weight Loss",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have recent weight loss?",
    "description": "Imported from CSV."
}
symptoms["problems_with_shape_or_size_of_breast"] = {
    "name": "Problems With Shape Or Size Of Breast",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have problems with shape or size of breast?",
    "description": "Imported from CSV."
}
symptoms["underweight"] = {
    "name": "Underweight",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have underweight?",
    "description": "Imported from CSV."
}
symptoms["difficulty_eating"] = {
    "name": "Difficulty Eating",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have difficulty eating?",
    "description": "Imported from CSV."
}
symptoms["scanty_menstrual_flow"] = {
    "name": "Scanty Menstrual Flow",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have scanty menstrual flow?",
    "description": "Imported from CSV."
}
symptoms["vaginal_pain"] = {
    "name": "Vaginal Pain",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have vaginal pain?",
    "description": "Imported from CSV."
}
symptoms["vaginal_redness"] = {
    "name": "Vaginal Redness",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have vaginal redness?",
    "description": "Imported from CSV."
}
symptoms["vulvar_irritation"] = {
    "name": "Vulvar Irritation",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have vulvar irritation?",
    "description": "Imported from CSV."
}
symptoms["weakness"] = {
    "name": "Weakness",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have weakness?",
    "description": "Imported from CSV."
}
symptoms["decreased_heart_rate"] = {
    "name": "Decreased Heart Rate",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have decreased heart rate?",
    "description": "Imported from CSV."
}
symptoms["increased_heart_rate"] = {
    "name": "Increased Heart Rate",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have increased heart rate?",
    "description": "Imported from CSV."
}
symptoms["bleeding_or_discharge_from_nipple"] = {
    "name": "Bleeding Or Discharge From Nipple",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have bleeding or discharge from nipple?",
    "description": "Imported from CSV."
}
symptoms["ringing_in_ear"] = {
    "name": "Ringing In Ear",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have ringing in ear?",
    "description": "Imported from CSV."
}
symptoms["plugged_feeling_in_ear"] = {
    "name": "Plugged Feeling In Ear",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have plugged feeling in ear?",
    "description": "Imported from CSV."
}
symptoms["itchy_ears"] = {
    "name": "Itchy Ear(S)",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have itchy ear(s)?",
    "description": "Imported from CSV."
}
symptoms["frontal_headache"] = {
    "name": "Frontal Headache",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have frontal headache?",
    "description": "Imported from CSV."
}
symptoms["fluid_in_ear"] = {
    "name": "Fluid In Ear",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have fluid in ear?",
    "description": "Imported from CSV."
}
symptoms["neck_stiffness_or_tightness"] = {
    "name": "Neck Stiffness Or Tightness",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have neck stiffness or tightness?",
    "description": "Imported from CSV."
}
symptoms["spots_or_clouds_in_vision"] = {
    "name": "Spots Or Clouds In Vision",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have spots or clouds in vision?",
    "description": "Imported from CSV."
}
symptoms["eye_redness"] = {
    "name": "Eye Redness",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have eye redness?",
    "description": "Imported from CSV."
}
symptoms["lacrimation"] = {
    "name": "Lacrimation",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have lacrimation?",
    "description": "Imported from CSV."
}
symptoms["itchiness_of_eye"] = {
    "name": "Itchiness Of Eye",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have itchiness of eye?",
    "description": "Imported from CSV."
}
symptoms["blindness"] = {
    "name": "Blindness",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have blindness?",
    "description": "Imported from CSV."
}
symptoms["eye_burns_or_stings"] = {
    "name": "Eye Burns Or Stings",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have eye burns or stings?",
    "description": "Imported from CSV."
}
symptoms["itchy_eyelid"] = {
    "name": "Itchy Eyelid",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have itchy eyelid?",
    "description": "Imported from CSV."
}
symptoms["feeling_cold"] = {
    "name": "Feeling Cold",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have feeling cold?",
    "description": "Imported from CSV."
}
symptoms["decreased_appetite"] = {
    "name": "Decreased Appetite",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have decreased appetite?",
    "description": "Imported from CSV."
}
symptoms["excessive_appetite"] = {
    "name": "Excessive Appetite",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have excessive appetite?",
    "description": "Imported from CSV."
}
symptoms["excessive_anger"] = {
    "name": "Excessive Anger",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have excessive anger?",
    "description": "Imported from CSV."
}
symptoms["loss_of_sensation"] = {
    "name": "Loss Of Sensation",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have loss of sensation?",
    "description": "Imported from CSV."
}
symptoms["focal_weakness"] = {
    "name": "Focal Weakness",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have focal weakness?",
    "description": "Imported from CSV."
}
symptoms["slurring_words"] = {
    "name": "Slurring Words",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have slurring words?",
    "description": "Imported from CSV."
}
symptoms["symptoms_of_the_face"] = {
    "name": "Symptoms Of The Face",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have symptoms of the face?",
    "description": "Imported from CSV."
}
symptoms["disturbance_of_memory"] = {
    "name": "Disturbance Of Memory",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have disturbance of memory?",
    "description": "Imported from CSV."
}
symptoms["paresthesia"] = {
    "name": "Paresthesia",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have paresthesia?",
    "description": "Imported from CSV."
}
symptoms["side_pain"] = {
    "name": "Side Pain",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have side pain?",
    "description": "Imported from CSV."
}
symptoms["shoulder_pain"] = {
    "name": "Shoulder Pain",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have shoulder pain?",
    "description": "Imported from CSV."
}
symptoms["shoulder_stiffness_or_tightness"] = {
    "name": "Shoulder Stiffness Or Tightness",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have shoulder stiffness or tightness?",
    "description": "Imported from CSV."
}
symptoms["shoulder_weakness"] = {
    "name": "Shoulder Weakness",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have shoulder weakness?",
    "description": "Imported from CSV."
}
symptoms["arm_cramps_or_spasms"] = {
    "name": "Arm Cramps Or Spasms",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have arm cramps or spasms?",
    "description": "Imported from CSV."
}
symptoms["shoulder_swelling"] = {
    "name": "Shoulder Swelling",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have shoulder swelling?",
    "description": "Imported from CSV."
}
symptoms["tongue_lesions"] = {
    "name": "Tongue Lesions",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have tongue lesions?",
    "description": "Imported from CSV."
}
symptoms["leg_cramps_or_spasms"] = {
    "name": "Leg Cramps Or Spasms",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have leg cramps or spasms?",
    "description": "Imported from CSV."
}
symptoms["abnormal_appearing_tongue"] = {
    "name": "Abnormal Appearing Tongue",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have abnormal appearing tongue?",
    "description": "Imported from CSV."
}
symptoms["ache_all_over"] = {
    "name": "Ache All Over",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have ache all over?",
    "description": "Imported from CSV."
}
symptoms["lower_body_pain"] = {
    "name": "Lower Body Pain",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have lower body pain?",
    "description": "Imported from CSV."
}
symptoms["problems_during_pregnancy"] = {
    "name": "Problems During Pregnancy",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have problems during pregnancy?",
    "description": "Imported from CSV."
}
symptoms["spotting_or_bleeding_during_pregnancy"] = {
    "name": "Spotting Or Bleeding During Pregnancy",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have spotting or bleeding during pregnancy?",
    "description": "Imported from CSV."
}
symptoms["cramps_and_spasms"] = {
    "name": "Cramps And Spasms",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have cramps and spasms?",
    "description": "Imported from CSV."
}
symptoms["upper_abdominal_pain"] = {
    "name": "Upper Abdominal Pain",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have upper abdominal pain?",
    "description": "Imported from CSV."
}
symptoms["stomach_bloating"] = {
    "name": "Stomach Bloating",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have stomach bloating?",
    "description": "Imported from CSV."
}
symptoms["changes_in_stool_appearance"] = {
    "name": "Changes In Stool Appearance",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have changes in stool appearance?",
    "description": "Imported from CSV."
}
symptoms["unusual_color_or_odor_to_urine"] = {
    "name": "Unusual Color Or Odor To Urine",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have unusual color or odor to urine?",
    "description": "Imported from CSV."
}
symptoms["kidney_mass"] = {
    "name": "Kidney Mass",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have kidney mass?",
    "description": "Imported from CSV."
}
symptoms["swollen_abdomen"] = {
    "name": "Swollen Abdomen",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have swollen abdomen?",
    "description": "Imported from CSV."
}
symptoms["symptoms_of_prostate"] = {
    "name": "Symptoms Of Prostate",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have symptoms of prostate?",
    "description": "Imported from CSV."
}
symptoms["leg_stiffness_or_tightness"] = {
    "name": "Leg Stiffness Or Tightness",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have leg stiffness or tightness?",
    "description": "Imported from CSV."
}
symptoms["difficulty_breathing"] = {
    "name": "Difficulty Breathing",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have difficulty breathing?",
    "description": "Imported from CSV."
}
symptoms["rib_pain"] = {
    "name": "Rib Pain",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have rib pain?",
    "description": "Imported from CSV."
}
symptoms["muscle_stiffness_or_tightness"] = {
    "name": "Muscle Stiffness Or Tightness",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have muscle stiffness or tightness?",
    "description": "Imported from CSV."
}
symptoms["hand_or_finger_lump_or_mass"] = {
    "name": "Hand Or Finger Lump Or Mass",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have hand or finger lump or mass?",
    "description": "Imported from CSV."
}
symptoms["groin_pain"] = {
    "name": "Groin Pain",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have groin pain?",
    "description": "Imported from CSV."
}
symptoms["abdominal_distention"] = {
    "name": "Abdominal Distention",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have abdominal distention?",
    "description": "Imported from CSV."
}
symptoms["regurgitation.1"] = {
    "name": "Regurgitation.1",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have regurgitation.1?",
    "description": "Imported from CSV."
}
symptoms["symptoms_of_the_kidneys"] = {
    "name": "Symptoms Of The Kidneys",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have symptoms of the kidneys?",
    "description": "Imported from CSV."
}
symptoms["melena"] = {
    "name": "Melena",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have melena?",
    "description": "Imported from CSV."
}
symptoms["flushing"] = {
    "name": "Flushing",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have flushing?",
    "description": "Imported from CSV."
}
symptoms["coughing_up_sputum"] = {
    "name": "Coughing Up Sputum",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have coughing up sputum?",
    "description": "Imported from CSV."
}
symptoms["delusions_or_hallucinations"] = {
    "name": "Delusions Or Hallucinations",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have delusions or hallucinations?",
    "description": "Imported from CSV."
}
symptoms["shoulder_cramps_or_spasms"] = {
    "name": "Shoulder Cramps Or Spasms",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have shoulder cramps or spasms?",
    "description": "Imported from CSV."
}
symptoms["joint_stiffness_or_tightness"] = {
    "name": "Joint Stiffness Or Tightness",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have joint stiffness or tightness?",
    "description": "Imported from CSV."
}
symptoms["pain_or_soreness_of_breast"] = {
    "name": "Pain Or Soreness Of Breast",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have pain or soreness of breast?",
    "description": "Imported from CSV."
}
symptoms["excessive_urination_at_night"] = {
    "name": "Excessive Urination At Night",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have excessive urination at night?",
    "description": "Imported from CSV."
}
symptoms["bleeding_from_eye"] = {
    "name": "Bleeding From Eye",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have bleeding from eye?",
    "description": "Imported from CSV."
}
symptoms["rectal_bleeding"] = {
    "name": "Rectal Bleeding",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have rectal bleeding?",
    "description": "Imported from CSV."
}
symptoms["temper_problems"] = {
    "name": "Temper Problems",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have temper problems?",
    "description": "Imported from CSV."
}
symptoms["coryza"] = {
    "name": "Coryza",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have coryza?",
    "description": "Imported from CSV."
}
symptoms["wrist_weakness"] = {
    "name": "Wrist Weakness",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have wrist weakness?",
    "description": "Imported from CSV."
}
symptoms["eye_strain"] = {
    "name": "Eye Strain",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have eye strain?",
    "description": "Imported from CSV."
}
symptoms["lymphedema"] = {
    "name": "Lymphedema",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have lymphedema?",
    "description": "Imported from CSV."
}
symptoms["skin_on_leg_or_foot_looks_infected"] = {
    "name": "Skin On Leg Or Foot Looks Infected",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have skin on leg or foot looks infected?",
    "description": "Imported from CSV."
}
symptoms["allergic_reaction"] = {
    "name": "Allergic Reaction",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have allergic reaction?",
    "description": "Imported from CSV."
}
symptoms["congestion_in_chest"] = {
    "name": "Congestion In Chest",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have congestion in chest?",
    "description": "Imported from CSV."
}
symptoms["muscle_swelling"] = {
    "name": "Muscle Swelling",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have muscle swelling?",
    "description": "Imported from CSV."
}
symptoms["pus_in_urine"] = {
    "name": "Pus In Urine",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have pus in urine?",
    "description": "Imported from CSV."
}
symptoms["abnormal_size_or_shape_of_ear"] = {
    "name": "Abnormal Size Or Shape Of Ear",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have abnormal size or shape of ear?",
    "description": "Imported from CSV."
}
symptoms["low_back_weakness"] = {
    "name": "Low Back Weakness",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have low back weakness?",
    "description": "Imported from CSV."
}
symptoms["sleepiness"] = {
    "name": "Sleepiness",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have sleepiness?",
    "description": "Imported from CSV."
}
symptoms["apnea"] = {
    "name": "Apnea",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have apnea?",
    "description": "Imported from CSV."
}
symptoms["abnormal_breathing_sounds"] = {
    "name": "Abnormal Breathing Sounds",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have abnormal breathing sounds?",
    "description": "Imported from CSV."
}
symptoms["excessive_growth"] = {
    "name": "Excessive Growth",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have excessive growth?",
    "description": "Imported from CSV."
}
symptoms["elbow_cramps_or_spasms"] = {
    "name": "Elbow Cramps Or Spasms",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have elbow cramps or spasms?",
    "description": "Imported from CSV."
}
symptoms["feeling_hot_and_cold"] = {
    "name": "Feeling Hot And Cold",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have feeling hot and cold?",
    "description": "Imported from CSV."
}
symptoms["blood_clots_during_menstrual_periods"] = {
    "name": "Blood Clots During Menstrual Periods",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have blood clots during menstrual periods?",
    "description": "Imported from CSV."
}
symptoms["absence_of_menstruation"] = {
    "name": "Absence Of Menstruation",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have absence of menstruation?",
    "description": "Imported from CSV."
}
symptoms["pulling_at_ears"] = {
    "name": "Pulling At Ears",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have pulling at ears?",
    "description": "Imported from CSV."
}
symptoms["gum_pain"] = {
    "name": "Gum Pain",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have gum pain?",
    "description": "Imported from CSV."
}
symptoms["redness_in_ear"] = {
    "name": "Redness In Ear",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have redness in ear?",
    "description": "Imported from CSV."
}
symptoms["fluid_retention"] = {
    "name": "Fluid Retention",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have fluid retention?",
    "description": "Imported from CSV."
}
symptoms["flu_like_syndrome"] = {
    "name": "Flu-Like Syndrome",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have flu-like syndrome?",
    "description": "Imported from CSV."
}
symptoms["sinus_congestion"] = {
    "name": "Sinus Congestion",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have sinus congestion?",
    "description": "Imported from CSV."
}
symptoms["painful_sinuses"] = {
    "name": "Painful Sinuses",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have painful sinuses?",
    "description": "Imported from CSV."
}
symptoms["fears_and_phobias"] = {
    "name": "Fears And Phobias",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have fears and phobias?",
    "description": "Imported from CSV."
}
symptoms["recent_pregnancy"] = {
    "name": "Recent Pregnancy",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have recent pregnancy?",
    "description": "Imported from CSV."
}
symptoms["uterine_contractions"] = {
    "name": "Uterine Contractions",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have uterine contractions?",
    "description": "Imported from CSV."
}
symptoms["burning_chest_pain"] = {
    "name": "Burning Chest Pain",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have burning chest pain?",
    "description": "Imported from CSV."
}
symptoms["back_cramps_or_spasms"] = {
    "name": "Back Cramps Or Spasms",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have back cramps or spasms?",
    "description": "Imported from CSV."
}
symptoms["stiffness_all_over"] = {
    "name": "Stiffness All Over",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have stiffness all over?",
    "description": "Imported from CSV."
}
symptoms["muscle_cramps,_contractures,_or_spasms"] = {
    "name": "Muscle Cramps, Contractures, Or Spasms",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have muscle cramps, contractures, or spasms?",
    "description": "Imported from CSV."
}
symptoms["low_back_cramps_or_spasms"] = {
    "name": "Low Back Cramps Or Spasms",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have low back cramps or spasms?",
    "description": "Imported from CSV."
}
symptoms["back_mass_or_lump"] = {
    "name": "Back Mass Or Lump",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have back mass or lump?",
    "description": "Imported from CSV."
}
symptoms["nosebleed"] = {
    "name": "Nosebleed",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have nosebleed?",
    "description": "Imported from CSV."
}
symptoms["long_menstrual_periods"] = {
    "name": "Long Menstrual Periods",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have long menstrual periods?",
    "description": "Imported from CSV."
}
symptoms["heavy_menstrual_flow"] = {
    "name": "Heavy Menstrual Flow",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have heavy menstrual flow?",
    "description": "Imported from CSV."
}
symptoms["unpredictable_menstruation"] = {
    "name": "Unpredictable Menstruation",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have unpredictable menstruation?",
    "description": "Imported from CSV."
}
symptoms["painful_menstruation"] = {
    "name": "Painful Menstruation",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have painful menstruation?",
    "description": "Imported from CSV."
}
symptoms["infertility"] = {
    "name": "Infertility",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have infertility?",
    "description": "Imported from CSV."
}
symptoms["frequent_menstruation"] = {
    "name": "Frequent Menstruation",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have frequent menstruation?",
    "description": "Imported from CSV."
}
symptoms["sweating"] = {
    "name": "Sweating",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have sweating?",
    "description": "Imported from CSV."
}
symptoms["mass_on_eyelid"] = {
    "name": "Mass On Eyelid",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have mass on eyelid?",
    "description": "Imported from CSV."
}
symptoms["swollen_eye"] = {
    "name": "Swollen Eye",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have swollen eye?",
    "description": "Imported from CSV."
}
symptoms["eyelid_swelling"] = {
    "name": "Eyelid Swelling",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have eyelid swelling?",
    "description": "Imported from CSV."
}
symptoms["eyelid_lesion_or_rash"] = {
    "name": "Eyelid Lesion Or Rash",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have eyelid lesion or rash?",
    "description": "Imported from CSV."
}
symptoms["unwanted_hair"] = {
    "name": "Unwanted Hair",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have unwanted hair?",
    "description": "Imported from CSV."
}
symptoms["symptoms_of_bladder"] = {
    "name": "Symptoms Of Bladder",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have symptoms of bladder?",
    "description": "Imported from CSV."
}
symptoms["irregular_appearing_nails"] = {
    "name": "Irregular Appearing Nails",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have irregular appearing nails?",
    "description": "Imported from CSV."
}
symptoms["itching_of_skin"] = {
    "name": "Itching Of Skin",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have itching of skin?",
    "description": "Imported from CSV."
}
symptoms["hurts_to_breath"] = {
    "name": "Hurts To Breath",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have hurts to breath?",
    "description": "Imported from CSV."
}
symptoms["nailbiting"] = {
    "name": "Nailbiting",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have nailbiting?",
    "description": "Imported from CSV."
}
symptoms["skin_dryness,_peeling,_scaliness,_or_roughness"] = {
    "name": "Skin Dryness, Peeling, Scaliness, Or Roughness",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have skin dryness, peeling, scaliness, or roughness?",
    "description": "Imported from CSV."
}
symptoms["skin_on_arm_or_hand_looks_infected"] = {
    "name": "Skin On Arm Or Hand Looks Infected",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have skin on arm or hand looks infected?",
    "description": "Imported from CSV."
}
symptoms["skin_irritation"] = {
    "name": "Skin Irritation",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have skin irritation?",
    "description": "Imported from CSV."
}
symptoms["itchy_scalp"] = {
    "name": "Itchy Scalp",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have itchy scalp?",
    "description": "Imported from CSV."
}
symptoms["hip_swelling"] = {
    "name": "Hip Swelling",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have hip swelling?",
    "description": "Imported from CSV."
}
symptoms["incontinence_of_stool"] = {
    "name": "Incontinence Of Stool",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have incontinence of stool?",
    "description": "Imported from CSV."
}
symptoms["foot_or_toe_cramps_or_spasms"] = {
    "name": "Foot Or Toe Cramps Or Spasms",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have foot or toe cramps or spasms?",
    "description": "Imported from CSV."
}
symptoms["warts"] = {
    "name": "Warts",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have warts?",
    "description": "Imported from CSV."
}
symptoms["bumps_on_penis"] = {
    "name": "Bumps On Penis",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have bumps on penis?",
    "description": "Imported from CSV."
}
symptoms["too_little_hair"] = {
    "name": "Too Little Hair",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have too little hair?",
    "description": "Imported from CSV."
}
symptoms["foot_or_toe_lump_or_mass"] = {
    "name": "Foot Or Toe Lump Or Mass",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have foot or toe lump or mass?",
    "description": "Imported from CSV."
}
symptoms["skin_rash"] = {
    "name": "Skin Rash",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have skin rash?",
    "description": "Imported from CSV."
}
symptoms["mass_or_swelling_around_the_anus"] = {
    "name": "Mass Or Swelling Around The Anus",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have mass or swelling around the anus?",
    "description": "Imported from CSV."
}
symptoms["low_back_swelling"] = {
    "name": "Low Back Swelling",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have low back swelling?",
    "description": "Imported from CSV."
}
symptoms["ankle_swelling"] = {
    "name": "Ankle Swelling",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have ankle swelling?",
    "description": "Imported from CSV."
}
symptoms["hip_lump_or_mass"] = {
    "name": "Hip Lump Or Mass",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have hip lump or mass?",
    "description": "Imported from CSV."
}
symptoms["drainage_in_throat"] = {
    "name": "Drainage In Throat",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have drainage in throat?",
    "description": "Imported from CSV."
}
symptoms["dry_or_flaky_scalp"] = {
    "name": "Dry Or Flaky Scalp",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have dry or flaky scalp?",
    "description": "Imported from CSV."
}
symptoms["premenstrual_tension_or_irritability"] = {
    "name": "Premenstrual Tension Or Irritability",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have premenstrual tension or irritability?",
    "description": "Imported from CSV."
}
symptoms["feeling_hot"] = {
    "name": "Feeling Hot",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have feeling hot?",
    "description": "Imported from CSV."
}
symptoms["feet_turned_in"] = {
    "name": "Feet Turned In",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have feet turned in?",
    "description": "Imported from CSV."
}
symptoms["foot_or_toe_stiffness_or_tightness"] = {
    "name": "Foot Or Toe Stiffness Or Tightness",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have foot or toe stiffness or tightness?",
    "description": "Imported from CSV."
}
symptoms["pelvic_pressure"] = {
    "name": "Pelvic Pressure",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have pelvic pressure?",
    "description": "Imported from CSV."
}
symptoms["elbow_swelling"] = {
    "name": "Elbow Swelling",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have elbow swelling?",
    "description": "Imported from CSV."
}
symptoms["elbow_stiffness_or_tightness"] = {
    "name": "Elbow Stiffness Or Tightness",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have elbow stiffness or tightness?",
    "description": "Imported from CSV."
}
symptoms["early_or_late_onset_of_menopause"] = {
    "name": "Early Or Late Onset Of Menopause",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have early or late onset of menopause?",
    "description": "Imported from CSV."
}
symptoms["mass_on_ear"] = {
    "name": "Mass On Ear",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have mass on ear?",
    "description": "Imported from CSV."
}
symptoms["bleeding_from_ear"] = {
    "name": "Bleeding From Ear",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have bleeding from ear?",
    "description": "Imported from CSV."
}
symptoms["hand_or_finger_weakness"] = {
    "name": "Hand Or Finger Weakness",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have hand or finger weakness?",
    "description": "Imported from CSV."
}
symptoms["low_self_esteem"] = {
    "name": "Low Self-Esteem",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have low self-esteem?",
    "description": "Imported from CSV."
}
symptoms["throat_irritation"] = {
    "name": "Throat Irritation",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have throat irritation?",
    "description": "Imported from CSV."
}
symptoms["itching_of_the_anus"] = {
    "name": "Itching Of The Anus",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have itching of the anus?",
    "description": "Imported from CSV."
}
symptoms["swollen_or_red_tonsils"] = {
    "name": "Swollen Or Red Tonsils",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have swollen or red tonsils?",
    "description": "Imported from CSV."
}
symptoms["irregular_belly_button"] = {
    "name": "Irregular Belly Button",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have irregular belly button?",
    "description": "Imported from CSV."
}
symptoms["swollen_tongue"] = {
    "name": "Swollen Tongue",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have swollen tongue?",
    "description": "Imported from CSV."
}
symptoms["lip_sore"] = {
    "name": "Lip Sore",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have lip sore?",
    "description": "Imported from CSV."
}
symptoms["vulvar_sore"] = {
    "name": "Vulvar Sore",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have vulvar sore?",
    "description": "Imported from CSV."
}
symptoms["hip_stiffness_or_tightness"] = {
    "name": "Hip Stiffness Or Tightness",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have hip stiffness or tightness?",
    "description": "Imported from CSV."
}
symptoms["mouth_pain"] = {
    "name": "Mouth Pain",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have mouth pain?",
    "description": "Imported from CSV."
}
symptoms["arm_weakness"] = {
    "name": "Arm Weakness",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have arm weakness?",
    "description": "Imported from CSV."
}
symptoms["leg_lump_or_mass"] = {
    "name": "Leg Lump Or Mass",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have leg lump or mass?",
    "description": "Imported from CSV."
}
symptoms["disturbance_of_smell_or_taste"] = {
    "name": "Disturbance Of Smell Or Taste",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have disturbance of smell or taste?",
    "description": "Imported from CSV."
}
symptoms["discharge_in_stools"] = {
    "name": "Discharge In Stools",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have discharge in stools?",
    "description": "Imported from CSV."
}
symptoms["penis_pain"] = {
    "name": "Penis Pain",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have penis pain?",
    "description": "Imported from CSV."
}
symptoms["loss_of_sex_drive"] = {
    "name": "Loss Of Sex Drive",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have loss of sex drive?",
    "description": "Imported from CSV."
}
symptoms["obsessions_and_compulsions"] = {
    "name": "Obsessions And Compulsions",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have obsessions and compulsions?",
    "description": "Imported from CSV."
}
symptoms["antisocial_behavior"] = {
    "name": "Antisocial Behavior",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have antisocial behavior?",
    "description": "Imported from CSV."
}
symptoms["neck_cramps_or_spasms"] = {
    "name": "Neck Cramps Or Spasms",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have neck cramps or spasms?",
    "description": "Imported from CSV."
}
symptoms["pupils_unequal"] = {
    "name": "Pupils Unequal",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have pupils unequal?",
    "description": "Imported from CSV."
}
symptoms["poor_circulation"] = {
    "name": "Poor Circulation",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have poor circulation?",
    "description": "Imported from CSV."
}
symptoms["thirst"] = {
    "name": "Thirst",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have thirst?",
    "description": "Imported from CSV."
}
symptoms["sleepwalking"] = {
    "name": "Sleepwalking",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have sleepwalking?",
    "description": "Imported from CSV."
}
symptoms["skin_oiliness"] = {
    "name": "Skin Oiliness",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have skin oiliness?",
    "description": "Imported from CSV."
}
symptoms["bladder_mass"] = {
    "name": "Bladder Mass",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have bladder mass?",
    "description": "Imported from CSV."
}
symptoms["knee_cramps_or_spasms"] = {
    "name": "Knee Cramps Or Spasms",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have knee cramps or spasms?",
    "description": "Imported from CSV."
}
symptoms["premature_ejaculation"] = {
    "name": "Premature Ejaculation",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have premature ejaculation?",
    "description": "Imported from CSV."
}
symptoms["leg_weakness"] = {
    "name": "Leg Weakness",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have leg weakness?",
    "description": "Imported from CSV."
}
symptoms["posture_problems"] = {
    "name": "Posture Problems",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have posture problems?",
    "description": "Imported from CSV."
}
symptoms["bleeding_in_mouth"] = {
    "name": "Bleeding In Mouth",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have bleeding in mouth?",
    "description": "Imported from CSV."
}
symptoms["tongue_bleeding"] = {
    "name": "Tongue Bleeding",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have tongue bleeding?",
    "description": "Imported from CSV."
}
symptoms["change_in_skin_mole_size_or_color"] = {
    "name": "Change In Skin Mole Size Or Color",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have change in skin mole size or color?",
    "description": "Imported from CSV."
}
symptoms["penis_redness"] = {
    "name": "Penis Redness",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have penis redness?",
    "description": "Imported from CSV."
}
symptoms["penile_discharge"] = {
    "name": "Penile Discharge",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have penile discharge?",
    "description": "Imported from CSV."
}
symptoms["shoulder_lump_or_mass"] = {
    "name": "Shoulder Lump Or Mass",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have shoulder lump or mass?",
    "description": "Imported from CSV."
}
symptoms["polyuria"] = {
    "name": "Polyuria",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have polyuria?",
    "description": "Imported from CSV."
}
symptoms["cloudy_eye"] = {
    "name": "Cloudy Eye",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have cloudy eye?",
    "description": "Imported from CSV."
}
symptoms["hysterical_behavior"] = {
    "name": "Hysterical Behavior",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have hysterical behavior?",
    "description": "Imported from CSV."
}
symptoms["arm_lump_or_mass"] = {
    "name": "Arm Lump Or Mass",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have arm lump or mass?",
    "description": "Imported from CSV."
}
symptoms["nightmares"] = {
    "name": "Nightmares",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have nightmares?",
    "description": "Imported from CSV."
}
symptoms["bleeding_gums"] = {
    "name": "Bleeding Gums",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have bleeding gums?",
    "description": "Imported from CSV."
}
symptoms["pain_in_gums"] = {
    "name": "Pain In Gums",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have pain in gums?",
    "description": "Imported from CSV."
}
symptoms["bedwetting"] = {
    "name": "Bedwetting",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have bedwetting?",
    "description": "Imported from CSV."
}
symptoms["diaper_rash"] = {
    "name": "Diaper Rash",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have diaper rash?",
    "description": "Imported from CSV."
}
symptoms["lump_or_mass_of_breast"] = {
    "name": "Lump Or Mass Of Breast",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have lump or mass of breast?",
    "description": "Imported from CSV."
}
symptoms["vaginal_bleeding_after_menopause"] = {
    "name": "Vaginal Bleeding After Menopause",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have vaginal bleeding after menopause?",
    "description": "Imported from CSV."
}
symptoms["infrequent_menstruation"] = {
    "name": "Infrequent Menstruation",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have infrequent menstruation?",
    "description": "Imported from CSV."
}
symptoms["mass_on_vulva"] = {
    "name": "Mass On Vulva",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have mass on vulva?",
    "description": "Imported from CSV."
}
symptoms["jaw_pain"] = {
    "name": "Jaw Pain",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have jaw pain?",
    "description": "Imported from CSV."
}
symptoms["itching_of_scrotum"] = {
    "name": "Itching Of Scrotum",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have itching of scrotum?",
    "description": "Imported from CSV."
}
symptoms["postpartum_problems_of_the_breast"] = {
    "name": "Postpartum Problems Of The Breast",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have postpartum problems of the breast?",
    "description": "Imported from CSV."
}
symptoms["eyelid_retracted"] = {
    "name": "Eyelid Retracted",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have eyelid retracted?",
    "description": "Imported from CSV."
}
symptoms["hesitancy"] = {
    "name": "Hesitancy",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have hesitancy?",
    "description": "Imported from CSV."
}
symptoms["elbow_lump_or_mass"] = {
    "name": "Elbow Lump Or Mass",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have elbow lump or mass?",
    "description": "Imported from CSV."
}
symptoms["muscle_weakness"] = {
    "name": "Muscle Weakness",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have muscle weakness?",
    "description": "Imported from CSV."
}
symptoms["throat_redness"] = {
    "name": "Throat Redness",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have throat redness?",
    "description": "Imported from CSV."
}
symptoms["tongue_pain"] = {
    "name": "Tongue Pain",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have tongue pain?",
    "description": "Imported from CSV."
}
symptoms["redness_in_or_around_nose"] = {
    "name": "Redness In Or Around Nose",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have redness in or around nose?",
    "description": "Imported from CSV."
}
symptoms["wrinkles_on_skin"] = {
    "name": "Wrinkles On Skin",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have wrinkles on skin?",
    "description": "Imported from CSV."
}
symptoms["foot_or_toe_weakness"] = {
    "name": "Foot Or Toe Weakness",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have foot or toe weakness?",
    "description": "Imported from CSV."
}
symptoms["hand_or_finger_cramps_or_spasms"] = {
    "name": "Hand Or Finger Cramps Or Spasms",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have hand or finger cramps or spasms?",
    "description": "Imported from CSV."
}
symptoms["back_stiffness_or_tightness"] = {
    "name": "Back Stiffness Or Tightness",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have back stiffness or tightness?",
    "description": "Imported from CSV."
}
symptoms["wrist_lump_or_mass"] = {
    "name": "Wrist Lump Or Mass",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have wrist lump or mass?",
    "description": "Imported from CSV."
}
symptoms["skin_pain"] = {
    "name": "Skin Pain",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have skin pain?",
    "description": "Imported from CSV."
}
symptoms["low_back_stiffness_or_tightness"] = {
    "name": "Low Back Stiffness Or Tightness",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have low back stiffness or tightness?",
    "description": "Imported from CSV."
}
symptoms["low_urine_output"] = {
    "name": "Low Urine Output",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have low urine output?",
    "description": "Imported from CSV."
}
symptoms["skin_on_head_or_neck_looks_infected"] = {
    "name": "Skin On Head Or Neck Looks Infected",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have skin on head or neck looks infected?",
    "description": "Imported from CSV."
}
symptoms["stuttering_or_stammering"] = {
    "name": "Stuttering Or Stammering",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have stuttering or stammering?",
    "description": "Imported from CSV."
}
symptoms["problems_with_orgasm"] = {
    "name": "Problems With Orgasm",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have problems with orgasm?",
    "description": "Imported from CSV."
}
symptoms["nose_deformity"] = {
    "name": "Nose Deformity",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have nose deformity?",
    "description": "Imported from CSV."
}
symptoms["lump_over_jaw"] = {
    "name": "Lump Over Jaw",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have lump over jaw?",
    "description": "Imported from CSV."
}
symptoms["sore_in_nose"] = {
    "name": "Sore In Nose",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have sore in nose?",
    "description": "Imported from CSV."
}
symptoms["hip_weakness"] = {
    "name": "Hip Weakness",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have hip weakness?",
    "description": "Imported from CSV."
}
symptoms["back_swelling"] = {
    "name": "Back Swelling",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have back swelling?",
    "description": "Imported from CSV."
}
symptoms["ankle_stiffness_or_tightness"] = {
    "name": "Ankle Stiffness Or Tightness",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have ankle stiffness or tightness?",
    "description": "Imported from CSV."
}
symptoms["ankle_weakness"] = {
    "name": "Ankle Weakness",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have ankle weakness?",
    "description": "Imported from CSV."
}
symptoms["neck_weakness"] = {
    "name": "Neck Weakness",
    "category": "CSV_Import",
    "severity": "moderate",
    "question_text": "Do you have neck weakness?",
    "description": "Imported from CSV."
}
