const HealthRecord = require('../models/HealthRecord');

// @desc    Add health record
// @route   POST /api/health/add-record
// @access  Private
const addHealthRecord = async (req, res) => {
    const { diseaseName, prescription, notes, reportFileUrl } = req.body;

    try {
        const record = await HealthRecord.create({
            userId: req.user.id,
            diseaseName,
            prescription,
            notes,
            reportFileUrl
        });
        res.status(201).json(record);
    } catch (error) {
        res.status(500).json({ message: error.message });
    }
};

// @desc    Get my health records
// @route   GET /api/health/my-records
// @access  Private
const getMyRecords = async (req, res) => {
    try {
        const records = await HealthRecord.find({ userId: req.user.id }).sort({ createdAt: -1 });
        res.status(200).json(records);
    } catch (error) {
        res.status(500).json({ message: error.message });
    }
};

module.exports = {
    addHealthRecord,
    getMyRecords
};
