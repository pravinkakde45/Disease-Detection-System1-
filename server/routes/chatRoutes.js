const express = require('express');
const router = express.Router();
const { saveChatMessage, getChatHistory, generateAIResponse } = require('../controllers/chatController');
const { protect } = require('../middleware/authMiddleware');

router.post('/save', protect, saveChatMessage);
router.post('/ask', protect, generateAIResponse);
router.get('/history', protect, getChatHistory);

module.exports = router;
