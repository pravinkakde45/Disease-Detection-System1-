const express = require('express');
const router = express.Router();
const { analyzePatterns } = require('../controllers/PatternController');
const { protect } = require('../middleware/authMiddleware');

router.get('/', protect, analyzePatterns);

module.exports = router;
