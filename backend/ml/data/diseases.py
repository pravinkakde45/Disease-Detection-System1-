# Disease Knowledge Base
# Format: {ID}: {name, category, severity, description}

diseases = {
    # Respiratory
    "D001": {"name": "Common Cold", "category": "Respiratory", "severity": "Low", "description": "Viral infection of your nose and throat."},
    "D002": {"name": "Influenza (Flu)", "category": "Respiratory", "severity": "Medium", "description": "Viral infection that attacks your respiratory system."},
    "D003": {"name": "Asthma", "category": "Respiratory", "severity": "Medium", "description": "Condition where airways narrow and swell and may produce extra mucus."},
    "D004": {"name": "Pneumonia", "category": "Respiratory", "severity": "High", "description": "Infection that inflames air sacs in one or both lungs."},
    "D005": {"name": "Chronic Obstructive Pulmonary Disease (COPD)", "category": "Respiratory", "severity": "High", "description": "Chronic inflammatory lung disease that causes obstructed airflow from the lungs."},
    "D006": {"name": "Tuberculosis", "category": "Respiratory", "severity": "High", "description": "Serious infectious bacterial disease that mainly affects the lungs."},
    "D007": {"name": "Bronchitis", "category": "Respiratory", "severity": "Medium", "description": "Inflammation of the lining of your bronchial tubes."},
    "D008": {"name": "Covid-19", "category": "Respiratory", "severity": "Variable", "description": "Disease caused by the coronavirus SARS-CoV-2."},

    # Cardiac
    "D009": {"name": "Hypertension", "category": "Cardiac", "severity": "Medium", "description": "High blood pressure."},
    "D010": {"name": "Coronary Artery Disease", "category": "Cardiac", "severity": "High", "description": "Narrowing or blockage of the coronary arteries."},
    "D011": {"name": "Myocardial Infarction (Heart Attack)", "category": "Cardiac", "severity": "Critical", "description": "Blockage of blood flow to the heart muscle."},
    "D012": {"name": "Arrhythmia", "category": "Cardiac", "severity": "Medium", "description": "Improper beating of the heart, whether too fast or too slow."},
    "D013": {"name": "Congestive Heart Failure", "category": "Cardiac", "severity": "High", "description": "Chronic condition in which the heart doesn't pump blood as well as it should."},

    # Digestive
    "D014": {"name": "Gastroenteritis", "category": "Digestive", "severity": "Low", "description": "Intestinal infection marked by diarrhea, cramps, nausea, vomiting, and fever."},
    "D015": {"name": "Gastroesophageal Reflux Disease (GERD)", "category": "Digestive", "severity": "Low", "description": "Digestive disease in which stomach acid or bile irritates the food pipe lining."},
    "D016": {"name": "Peptic Ulcer", "category": "Digestive", "severity": "Medium", "description": "Sore that develops on the lining of the esophagus, stomach, or small intestine."},
    "D017": {"name": "Irritable Bowel Syndrome (IBS)", "category": "Digestive", "severity": "Medium", "description": "An intestinal disorder causing pain in the belly, gas, diarrhea, and constipation."},
    "D018": {"name": "Celiac Disease", "category": "Digestive", "severity": "Medium", "description": "Immune reaction to eating gluten."},
    "D019": {"name": "Liver Cirrhosis", "category": "Digestive", "severity": "High", "description": "Chronic liver damage from a variety of causes leading to scarring and liver failure."},
    "D020": {"name": "Appendicitis", "category": "Digestive", "severity": "High", "description": "Inflammation of the appendix."},

    # Neurological
    "D021": {"name": "Migraine", "category": "Neurological", "severity": "Medium", "description": "Headache of varying intensity, often accompanied by nausea and sensitivity to light and sound."},
    "D022": {"name": "Stroke", "category": "Neurological", "severity": "Critical", "description": "Damage to the brain from interruption of its blood supply."},
    "D023": {"name": "Epilepsy", "category": "Neurological", "severity": "Medium", "description": "Central nervous system disorder in which brain activity becomes abnormal, causing seizures."},
    "D024": {"name": "Alzheimer's Disease", "category": "Neurological", "severity": "High", "description": "Progressive disease that destroys memory and other important mental functions."},
    "D025": {"name": "Parkinson's Disease", "category": "Neurological", "severity": "High", "description": "Disorder of the central nervous system that affects movement, often including tremors."},
    "D026": {"name": "Multiple Sclerosis", "category": "Neurological", "severity": "High", "description": "Disease in which the immune system eats away at the protective covering of nerves."},

    # Endocrine
    "D027": {"name": "Diabetes Mellitus Type 1", "category": "Endocrine", "severity": "High", "description": "Chronic condition in which the pancreas produces little or no insulin."},
    "D028": {"name": "Diabetes Mellitus Type 2", "category": "Endocrine", "severity": "High", "description": "Chronic condition that affects the way the body processes blood (sugar)."},
    "D029": {"name": "Hypothyroidism", "category": "Endocrine", "severity": "Medium", "description": "Condition in which the thyroid gland doesn't produce enough thyroid hormone."},
    "D030": {"name": "Hyperthyroidism", "category": "Endocrine", "severity": "Medium", "description": "Overproduction of a hormone by the butterfly-shaped gland in the neck (thyroid)."},

    # Infectious
    "D031": {"name": "Malaria", "category": "Infectious", "severity": "High", "description": "Disease caused by a plasmodium parasite, transmitted by the bite of infected mosquitoes."},
    "D032": {"name": "Dengue Fever", "category": "Infectious", "severity": "Medium", "description": "Mosquito-borne viral infection causing severe flu-like illness."},
    "D033": {"name": "Typhoid Fever", "category": "Infectious", "severity": "Medium", "description": "Bacterial infection that can lead to high fever, diarrhea, and vomiting."},
    "D034": {"name": "HIV/AIDS", "category": "Infectious", "severity": "Critical", "description": "HIV causes AIDS and interferes with the body's ability to fight infections."},
    "D035": {"name": "Chickenpox", "category": "Infectious", "severity": "Low", "description": "Highly contagious viral infection causing an itchy, blister-like rash on the skin."},
    
    # Skin
    "D036": {"name": "Eczema", "category": "Skin", "severity": "Low", "description": "Condition that makes your skin red and itchy."},
    "D037": {"name": "Psoriasis", "category": "Skin", "severity": "Medium", "description": "Condition that causes red, itchy scaly patches, most commonly on the knees, elbows, trunk and scalp."},
    "D038": {"name": "Acne Vulgaris", "category": "Skin", "severity": "Low", "description": "Common skin condition that happens when hair follicles under the skin become clogged."},
    "D039": {"name": "Melanoma", "category": "Skin", "severity": "Critical", "description": "The most serious type of skin cancer."},
    "D040": {"name": "Dermatitis", "category": "Skin", "severity": "Low", "description": "General term that describes a common skin irritation."},

    # Mental Health
    "D041": {"name": "Major Depressive Disorder", "category": "Mental", "severity": "High", "description": "Mental health disorder characterized by persistently depressed mood or loss of interest in activities."},
    "D042": {"name": "Generalized Anxiety Disorder", "category": "Mental", "severity": "Medium", "description": "Severe, ongoing anxiety that interferes with daily activities."},
    "D043": {"name": "Schizophrenia", "category": "Mental", "severity": "High", "description": "Disorder that affects a person's ability to think, feel, and behave clearly."},
    "D044": {"name": "Bipolar Disorder", "category": "Mental", "severity": "High", "description": "Disorder associated with episodes of mood swings ranging from depressive lows to manic highs."},
    "D045": {"name": "Panic Disorder", "category": "Mental", "severity": "Medium", "description": "Sudden episodes of intense fear or anxiety and physical symptoms, based on a perceived threat rather than imminent danger."},
    
    # Musculoskeletal
    "D046": {"name": "Osteoarthritis", "category": "Musculoskeletal", "severity": "Medium", "description": "Type of arthritis that occurs when flexible tissue at the ends of bones wears down."},
    "D047": {"name": "Rheumatoid Arthritis", "category": "Musculoskeletal", "severity": "High", "description": "Chronic inflammatory disorder affecting many joints, including those in the hands and feet."},
    "D048": {"name": "Osteoporosis", "category": "Musculoskeletal", "severity": "Medium", "description": "Condition in which bones become weak and brittle."},
    "D049": {"name": "Fibromyalgia", "category": "Musculoskeletal", "severity": "Medium", "description": "Widespread muscle pain and tenderness."},
    "D050": {"name": "Gout", "category": "Musculoskeletal", "severity": "Medium", "description": "Form of arthritis characterized by severe pain, redness, and tenderness in joints."},

    # Urinary
    "D051": {"name": "Urinary Tract Infection (UTI)", "category": "Urinary", "severity": "Low", "description": "Infection in any part of the urinary system, the kidneys, bladder, or urethra."},
    "D052": {"name": "Kidney Stones", "category": "Urinary", "severity": "High", "description": "Hard deposits made of minerals and salts that form inside your kidneys."},
    "D053": {"name": "Chronic Kidney Disease", "category": "Urinary", "severity": "Critical", "description": "Longstanding disease of the kidneys leading to renal failure."},
    
    # Others / Mixed
    "D054": {"name": "Anemia", "category": "Blood", "severity": "Medium", "description": "Condition in which you lack enough healthy red blood cells to carry adequate oxygen to your body's tissues."},
    "D055": {"name": "Allergies", "category": "Immune", "severity": "Low", "description": "Condition in which the immune system reacts abnormally to a foreign substance."},
    "D056": {"name": "Food Poisoning", "category": "Digestive", "severity": "Medium", "description": "Illness caused by bacteria or other toxins in food."},
    "D057": {"name": "Lyme Disease", "category": "Infectious", "severity": "Medium", "description": "Tick-borne illness caused by the bacterium Borrelia burgdorferi."},
    "D058": {"name": "Meningitis", "category": "Neurological", "severity": "Critical", "description": "Inflammation of brain and spinal cord membranes, typically caused by an infection."},
    "D059": {"name": "Glaucoma", "category": "Eye", "severity": "High", "description": "Group of eye conditions that damage the optic nerve."},
    "D060": {"name": "Conjunctivitis (Pink Eye)", "category": "Eye", "severity": "Low", "description": "Inflammation or infection of the outer membrane of the eyeball and the inner eyelid."},
    "D061": {"name": "Otitis Media", "category": "Ear", "severity": "Low", "description": "Infection of the middle ear."},
    "D062": {"name": "Tonsillitis", "category": "Respiratory", "severity": "Low", "description": "Inflammation of the two oval-shaped pads of tissue at the back of the throat."},
}
