const DiseaseHistory = require('../models/DiseaseHistory');

// @desc    Analyze health patterns based on history
// @route   GET /api/patterns
// @access  Private
const analyzePatterns = async (req, res) => {
    try {
        const userId = req.user.id;
        const history = await DiseaseHistory.find({ userId }).sort({ createdAt: -1 });

        if (history.length < 3) {
            return res.status(200).json({ patterns: [], message: 'Not enough data for pattern analysis' });
        }

        const symptomCounts = {};
        
        // rudimentary analysis: count symptom occurrences
        history.forEach(record => {
            record.symptomsProvided.forEach(symptom => {
                const s = symptom.toLowerCase().trim();
                symptomCounts[s] = (symptomCounts[s] || 0) + 1;
            });
        });

        const patterns = [];
        for (const [symptom, count] of Object.entries(symptomCounts)) {
            if (count >= 3) {
                patterns.push({
                    type: 'recurring_symptom',
                    symptom: symptom,
                    count: count,
                    message: `You have reported '${symptom}' ${count} times. Consider consulting a specialist.`
                });
            }
        }

        res.status(200).json({ patterns });
    } catch (error) {
        res.status(500).json({ message: error.message });
    }
};

module.exports = {
    analyzePatterns
};
