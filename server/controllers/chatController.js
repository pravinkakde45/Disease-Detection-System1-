const dns = require('dns');
try { dns.setDefaultResultOrder('ipv4first'); } catch (e) { }
const ChatHistory = require('../models/ChatHistory');
const User = require('../models/User');
const DiseaseHistory = require('../models/DiseaseHistory');
const { HfInference } = require('@huggingface/inference');

const hf = new HfInference(process.env.HF_API_TOKEN);


// @desc    Save chat message
// @route   POST /api/chat/save
// @access  Private
const saveChatMessage = async (req, res) => {
    const { message, sender } = req.body;

    try {
        const chat = await ChatHistory.create({
            userId: req.user.id,
            message,
            sender
        });
        res.status(201).json(chat);
    } catch (error) {
        res.status(500).json({ message: error.message });
    }
};

// @desc    Get chat history
// @route   GET /api/chat/history
// @access  Private
const getChatHistory = async (req, res) => {
    try {
        const history = await ChatHistory.find({ userId: req.user.id }).sort({ timestamp: 1 });
        res.status(200).json(history);
    } catch (error) {
        res.status(500).json({ message: error.message });
    }
};

// @desc    Generate AI response with context
// @route   POST /api/chat/ask
// @access  Private
const generateAIResponse = async (req, res) => {
    const { message } = req.body;
    const userId = req.user.id; // Extract userId
    try {
        // Check User Preferences for AI Memory
        const user = await User.findById(userId);
        let historyContext = [];
        let diseaseHistory = []; // Keep for simulated response compatibility

        if (user && user.preferences && user.preferences.aiMemory !== false) {
             const chats = await ChatHistory.find({ userId }).sort({ timestamp: -1 }).limit(5).lean();
             const diseases = await DiseaseHistory.find({ userId }).sort({ createdAt: -1 }).limit(3).lean();
             
             historyContext = [
                ...chats.map(c => `User asked: ${c.userMessage}\nAI answered: ${c.aiResponse}`),
                ...diseases.map(d => `User was predicted with ${d.predictedDisease} (Confidence: ${d.confidenceScore}%) based on symptoms: ${d.symptomsProvided ? d.symptomsProvided.join(', ') : 'N/A'}`)
            ];
            diseaseHistory = diseases; // Re-assign for simulated response compatibility
        }

        // Construct Prompt
        const systemPrompt = `You are a medical assistant AI. 
        Context from previous interactions (User History):
        ${historyContext.join('\n')}
        
        Current User Question: ${message}
        
        Provide a helpful, safe, and concise medical response. Always advise consulting a doctor for serious issues.`;

        // Call Hugging Face API
        let aiResponse = "I'm sorry, I couldn't process your request at the moment.";
        
        try {
             const response = await hf.chatCompletion({
                model: process.env.HF_MODEL_ID || 'google/gemma-3-27b-it',
                messages: [
                    { role: 'user', content: systemPrompt }
                ],
                max_tokens: 500,
                temperature: 0.7
            });
            aiResponse = response.choices[0].message.content;
        } catch (apiError) {
             console.error("Hugging Face API Error:", apiError);
             aiResponse = "I am having trouble connecting to my medical brain right now. Please try again later.";
        }


        // Save user message
        await ChatHistory.create({
            userId: req.user.id,
            message,
            sender: 'user'
        });

        // Save AI response
        const chat = await ChatHistory.create({
            userId: req.user.id,
            message: aiResponse,
            sender: 'system'
        });

        res.status(200).json(chat);
    } catch (error) {
        res.status(500).json({ message: error.message });
    }
};

module.exports = {
    saveChatMessage,
    getChatHistory,
    generateAIResponse
};
