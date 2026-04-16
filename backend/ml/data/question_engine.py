from symptoms import symptoms
from disease_symptom_map import disease_map

class QuestionEngine:
    def __init__(self):
        self.diseases = disease_map
        self.symptoms = symptoms
        self.emergency_symptoms = ["chest_pain", "shortness_of_breath", "seizures", "confusion", "hemoptysis"]

    def check_emergency(self, answered_symptoms):
        """
        Checks if any reported symptom is a critical emergency.
        """
        for sym in answered_symptoms:
            if sym in self.emergency_symptoms and answered_symptoms[sym] == True:
                return {
                    "is_emergency": True,
                    "message": f"WARNING: {self.symptoms[sym]['name']} is a serious symptom. Please seek medical attention immediately."
                }
        return {"is_emergency": False}

    def calculate_probabilities(self, answered_symptoms):
        """
        Scores each disease based on answered symptoms.
        Returns a sorted list of likely diseases.
        """
        scores = {}
        
        for d_id, d_data in self.diseases.items():
            score = 0.0
            total_weight = sum(d_data['symptom_weights'].values())
            matched_symptoms = 0
            
            for sym, response in answered_symptoms.items():
                if response == True: # specific match
                    if sym in d_data['symptom_weights']:
                        score += d_data['symptom_weights'][sym]
                        matched_symptoms += 1
                elif response == False: # specific mismatch
                    if sym in d_data['primary_symptoms']:
                        score -= 0.3 # Penalize if primary symptom missing
            
            if total_weight > 0:
                normalized_score = score / total_weight
            else:
                normalized_score = 0
                
            # Boost if all primary symptoms present
            primaries_present = [s for s in d_data['primary_symptoms'] if answered_symptoms.get(s) == True]
            if len(primaries_present) == len(d_data['primary_symptoms']):
                normalized_score += 0.2
                
            scores[d_id] = {
                "name": d_data['name'],
                "score": round(max(0, min(1.0, normalized_score)), 3),
                "matched": matched_symptoms
            }
            
        # Sort by score desc
        sorted_diseases = sorted(scores.items(), key=lambda x: x[1]['score'], reverse=True)
        return sorted_diseases

    def get_next_question(self, answered_symptoms):
        """
        Determines the best next symptom to ask about based on current top candidates.
        """
        # 1. Rank diseases
        ranked = self.calculate_probabilities(answered_symptoms)
        top_candidates = [item for item in ranked if item[1]['score'] > 0.0]
        
        if not top_candidates:
            # Cold start: Ask generalized high-frequency symptoms not yet answered
            starters = ["fever", "cough", "headache", "fatigue", "abdominal_pain"]
            for s in starters:
                if s not in answered_symptoms:
                    return {"symptom_code": s, "text": self.symptoms[s]['question_text']}
            return None # Exhausted starters
            
        # 2. Find best distinguishing symptom from Top 3 diseases
        candidate_ids = [x[0] for x in top_candidates[:3]]
        
        potential_symptoms = {}
        
        for d_id in candidate_ids:
            d_data = self.diseases[d_id]
            # Check primary then secondary
            for pool in [d_data['primary_symptoms'], d_data['secondary_symptoms']]:
                for sym in pool:
                    if sym not in answered_symptoms:
                        potential_symptoms[sym] = potential_symptoms.get(sym, 0) + d_data['symptom_weights'].get(sym, 0.1)
        
        # Sort by frequency/weight in top candidates
        if potential_symptoms:
            best_symptom = sorted(potential_symptoms.items(), key=lambda x: x[1], reverse=True)[0][0]
            return {"symptom_code": best_symptom, "text": self.symptoms[best_symptom]['question_text']}
            
        return None # No more relevant questions

