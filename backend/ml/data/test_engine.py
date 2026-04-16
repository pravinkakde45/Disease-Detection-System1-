import sys
import os

# Ensure import path
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir)

from question_engine import QuestionEngine

def run_simulation(scenario_name, initial_symptoms):
    print(f"\n--- Simulation: {scenario_name} ---")
    engine = QuestionEngine()
    answered = initial_symptoms.copy()
    
    # Check immediate emergency
    emergency = engine.check_emergency(answered)
    if emergency['is_emergency']:
        print(f"🚨 ALERT: {emergency['message']}")
        return

    print(f"Initial Symptoms: {list(answered.keys())}")
    
    # Run 5 rounds of questions
    for i in range(5):
        # 1. Prediction
        preds = engine.calculate_probabilities(answered)
        top = preds[0]
        print(f"Current Top Diagnosis: {top[1]['name']} (Score: {top[1]['score']})")
        
        if top[1]['score'] > 0.85:
            print(f"✅ Diagnosis reached with high confidence: {top[1]['name']}")
            break
            
        # 2. Ask Next
        next_q = engine.get_next_question(answered)
        if not next_q:
            print("No more questions.")
            break
            
        print(f"🤖 AI Asks: {next_q['text']} ({next_q['symptom_code']})")
        
        # Simulate 'Yes' if it's a known symptom for the scenario (simple simulation logic)
        # In a real test we'd have a ground truth set of symptoms for the scenario
        val = input("   User Answer (y/n): ")
        answered[next_q['symptom_code']] = (val.lower() == 'y')

    print("--- End Simulation ---\n")

if __name__ == "__main__":
    print("Starting Engine Test...\n")
    
    # Scenarios defined by 'true' symptoms user has
    # We will simulate user input interactively for better verification
    
    print("Select Scenario to Test:")
    print("1. Flu (Fever, Muscle Pain)")
    print("2. Heart Attack (Chest Pain)")
    print("3. Cold Start (No unknown symptoms)")
    
    choice = input("Enter 1, 2, or 3: ")
    
    if choice == '1':
        # User starts with fever
        run_simulation("Flu Case", {"fever": True})
    elif choice == '2':
        run_simulation("Heart Attack Case", {"chest_pain": True})
    else:
        run_simulation("Unknown Case", {})
