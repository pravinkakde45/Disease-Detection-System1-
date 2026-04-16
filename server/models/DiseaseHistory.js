const mongoose = require('mongoose');

const diseaseHistorySchema = new mongoose.Schema({
    userId: {
        type: mongoose.Schema.Types.ObjectId,
        ref: 'User',
        required: true
    },
    predictedDisease: {
        type: String,
        required: true
    },
    confidenceScore: {
        type: Number,
        required: true
    },
    symptomsProvided: {
        type: [String],
        required: true
    },
    createdAt: {
        type: Date,
        default: Date.now
    }
});

module.exports = mongoose.model('DiseaseHistory', diseaseHistorySchema);
