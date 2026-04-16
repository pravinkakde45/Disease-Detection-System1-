const mongoose = require('mongoose');

const userSchema = new mongoose.Schema({
    name: {
        type: String,
        required: true
    },
    email: {
        type: String,
        required: true,
        unique: true
    },
    password: {
        type: String,
        required: true
    },
    age: {
        type: Number,
        default: 0
    },
    gender: {
        type: String,
        default: 'Not Specified'
    },
    otp: {
        type: String
    },
    otpExpiry: {
        type: Date
    },
    createdAt: {
        type: Date,
        default: Date.now
    },
    preferences: {
        aiMemory: {
            type: Boolean,
            default: true
        }
    }
   

});

module.exports = mongoose.model('User', userSchema);
