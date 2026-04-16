const ChatHistory = require('../models/ChatHistory');
const DiseaseHistory = require('../models/DiseaseHistory');
const HealthRecord = require('../models/HealthRecord');

// @desc    Get all user history (chats, diseases, health records) sorted by date
// @route   GET /api/history
// @access  Private
const getCombinedHistory = async (req, res) => {
    try {
        const userId = req.user.id;

        const chats = await ChatHistory.find({ userId }).lean();
        const diseases = await DiseaseHistory.find({ userId }).lean();
        const records = await HealthRecord.find({ userId }).lean();

        const combined = [
            ...chats.map(item => ({ ...item, type: 'chat', date: item.timestamp })),
            ...diseases.map(item => ({ ...item, type: 'disease', date: item.createdAt })),
            ...records.map(item => ({ ...item, type: 'health_record', date: item.createdAt }))
        ];

        // Sort descending by date
        combined.sort((a, b) => new Date(b.date) - new Date(a.date));

        res.status(200).json(combined);
    } catch (error) {
        res.status(500).json({ message: error.message });
    }
};

// @desc    Delete all user history
// @route   DELETE /api/history
// @access  Private
const deleteHistory = async (req, res) => {
    try {
        const userId = req.user.id;

        await ChatHistory.deleteMany({ userId });
        await DiseaseHistory.deleteMany({ userId });
        await HealthRecord.deleteMany({ userId });

        res.status(200).json({ message: 'History deleted successfully' });
    } catch (error) {
        res.status(500).json({ message: error.message });
    }
};

// @desc    Export user data
// @route   GET /api/history/export
// @access  Private
const exportData = async (req, res) => {
    try {
        const userId = req.user.id;

        const chats = await ChatHistory.find({ userId }).lean();
        const diseases = await DiseaseHistory.find({ userId }).lean();
        const records = await HealthRecord.find({ userId }).lean();

        const data = {
            user: req.user,
            chats,
            diseases,
            healthRecords: records
        };

        res.status(200).json(data);
    } catch (error) {
        res.status(500).json({ message: error.message });
    }
};

module.exports = {
    getCombinedHistory,
    deleteHistory,
    exportData
};
