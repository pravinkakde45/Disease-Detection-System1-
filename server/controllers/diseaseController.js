const DiseaseHistory = require('../models/DiseaseHistory');
const { HfInference } = require('@huggingface/inference');
const hf = new HfInference(process.env.HF_API_TOKEN);

// @desc    Save disease prediction result
// @route   POST /api/disease/save-result
// @access  Private
const saveDiseaseResult = async (req, res) => {
    const { predictedDisease, confidenceScore, symptomsProvided } = req.body;

    try {
        const diseaseHistory = await DiseaseHistory.create({
            userId: req.user.id,
            predictedDisease,
            confidenceScore,
            symptomsProvided
        });
        res.status(201).json(diseaseHistory);
    } catch (error) {
        res.status(500).json({ message: error.message });
    }
};

// @desc    Get disease history
// @route   GET /api/disease/history
// @access  Private
const getDiseaseHistory = async (req, res) => {
    try {
        const history = await DiseaseHistory.find({ userId: req.user.id }).sort({ createdAt: -1 });
        res.status(200).json(history);
    } catch (error) {
        res.status(500).json({ message: error.message });
    }
};

// @desc    Predict Disease using ML
// @route   POST /api/disease/predict
// @access  Private
const predictDisease = async (req, res) => {
    const { symptoms } = req.body; // Array of symptom codes

    if (!symptoms || symptoms.length === 0) {
        return res.status(400).json({ message: 'No symptoms provided' });
    }

    try {
        const systemPrompt = `You are an expert medical diagnostician algorithm. 
The patient has the following symptoms: ${symptoms.join(', ')}.
Analyze these symptoms and determine the most likely primary disease. Provide a confidence score between 0 and 100 representing how certain you are of this diagnosis based strictly on the symptoms.
Return ONLY a strictly valid JSON object matching this exact format:
{
  "primary_disease": "Name of Disease",
  "confidence": 85
}
Do not include any other text, markdown formatting, or code blocks.`;

        const response = await hf.chatCompletion({
            model: process.env.HF_MODEL_ID || 'google/gemma-3-27b-it',
            messages: [{ role: 'user', content: systemPrompt }],
            max_tokens: 200,
            temperature: 0.2
        });

        const rawText = response.choices[0].message.content.trim();
        let result;
        try {
            // Remove any markdown code blocks if the LLM hallucinated them
            const cleanedText = rawText.replace(/```json/g, '').replace(/```/g, '').trim();
            result = JSON.parse(cleanedText);
        } catch(e) {
             console.error("Failed to parse HF response:", rawText);
             return res.status(500).json({ message: "Invalid diagnosis format from AI", details: rawText });
        }

        const historyEntry = await DiseaseHistory.create({
            userId: req.user.id,
            predictedDisease: result.primary_disease || "Unknown Disease",
            confidenceScore: result.confidence || 0,
            symptomsProvided: symptoms
        });
        
        result.historyId = historyEntry._id;
        res.status(200).json(result);

    } catch (error) {
        console.error(error);
        res.status(500).json({ message: error.message });
    }
};

module.exports = {
    saveDiseaseResult,
    getDiseaseHistory,
    predictDisease
};
