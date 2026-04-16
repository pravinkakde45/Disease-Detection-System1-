const DiseaseHistory = require('../models/DiseaseHistory');
const { spawn } = require('child_process');
const path = require('path');

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
        // Path to python script
        const scriptPath = path.join(__dirname, '../../backend/ml/predict_disease.py');

        const pythonProcess = spawn('python', [scriptPath]);

        let dataString = '';
        let errorString = '';

        // Send data to python script
        pythonProcess.stdin.write(JSON.stringify({ symptoms }));
        pythonProcess.stdin.end();

        pythonProcess.stdout.on('data', (data) => {
            dataString += data.toString();
        });

        pythonProcess.stderr.on('data', (data) => {
            console.error(`Python Error: ${data}`);
            errorString += data.toString();
        });

        pythonProcess.on('close', async (code) => {
            if (code !== 0) {
                console.error('Python script failed', errorString);
                return res.status(500).json({ message: 'Prediction failed', error: errorString });
            }

            try {
                const result = JSON.parse(dataString);

                if (result.error) {
                    return res.status(500).json({ message: result.error });
                }

                // Save to Database
                const historyEntry = await DiseaseHistory.create({
                    userId: req.user.id,
                    predictedDisease: result.primary_disease || "Unknown",
                    confidenceScore: result.confidence || 0,
                    symptomsProvided: symptoms
                });

                // Attach ID to result if needed (optional)
                result.historyId = historyEntry._id;

                res.status(200).json(result);

            } catch (e) {
                console.error("JSON Parse Error", e, dataString);
                res.status(500).json({ message: 'Invalid response from model', details: dataString });
            }
        });

    } catch (error) {
        res.status(500).json({ message: error.message });
    }
};

module.exports = {
    saveDiseaseResult,
    getDiseaseHistory,
    predictDisease
};
