const mongoose = require('mongoose');

const appointmentSchema = mongoose.Schema({
    user_id: {
        type: mongoose.Schema.Types.ObjectId,
        required: true,
        ref: 'User'
    },
    doctor_id: {
        type: mongoose.Schema.Types.ObjectId,
        required: true,
        ref: 'Doctor'
    },
    date: {
        type: Date,
        required: true
    },
    time_slot: {
        type: String,
        required: true
    },
    status: {
        type: String,
        required: true,
        enum: ['Booked', 'Completed', 'Cancelled'],
        default: 'Booked'
    },
    reason: {
        type: String,
        required: true
    }
}, {
    timestamps: true
});

module.exports = mongoose.model('Appointment', appointmentSchema);
