const express = require('express');
const router = express.Router();
const { registerUser, loginUser, getMe, forgotPassword, verifyOTP, resetPassword, updatePreferences } = require('../controllers/authController');
const { protect } = require('../middleware/authMiddleware');

router.post('/register', registerUser);
router.post('/login', loginUser);
router.get('/profile', protect, getMe);
router.post('/forgot-password', forgotPassword);
router.post('/verify-otp', verifyOTP);
router.post('/reset-password', resetPassword);
router.put('/preferences', protect, updatePreferences);

module.exports = router;
