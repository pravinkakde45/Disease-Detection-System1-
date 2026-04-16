const mongoose = require('mongoose');

const healthRecordSchema = new mongoose.Schema({
    userId: {
        type: mongoose.Schema.Types.ObjectId,
        ref: 'User',
        required: true
    },
    diseaseName: {
        type: String,
        required: true
    },
    prescription: {
        type: String
    },
    notes: {
        type: String
    },
    reportFileUrl: {
        type: String
    },
    createdAt: {
        type: Date,
        default: Date.now
    }
});

module.exports = mongoose.model('HealthRecord', healthRecordSchema);
