const express = require('express');
const router = express.Router();
const { saveDiseaseResult, getDiseaseHistory, predictDisease } = require('../controllers/diseaseController');
const { protect } = require('../middleware/authMiddleware');

router.post('/save-result', protect, saveDiseaseResult);
router.get('/history', protect, getDiseaseHistory);
router.post('/predict', protect, predictDisease);

module.exports = router;
