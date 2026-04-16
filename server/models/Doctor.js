const mongoose = require('mongoose');

const doctorSchema = new mongoose.Schema({
    name: {
        type: String,
        required: true
    },
    qualification: {
        type: String,
        required: true
    },
    specialization: {
        type: String,
        required: true
    },
    hospital_or_clinic_name: {
        type: String,
        required: true
    },
    address: {
        type: String,
        required: true
    },
    city: {
        type: String,
        required: true
    },
    phone: {
        type: String,
        required: true
    },
    consultation_fee: {
        type: Number,
        required: true
    },
    available_days: [{
        type: String, // e.g., 'Monday', 'Tuesday'
        required: true
    }],
    available_time_slots: [{
        type: String, // e.g., '10:00 AM - 10:30 AM'
        required: true
    }],
    is_active: {
        type: Boolean,
        default: true
    },
    distance: {
        type: Number, 
        default: 0
    },
    location: {
        lat: Number,
        lng: Number
    }
});

module.exports = mongoose.model('Doctor', doctorSchema);
