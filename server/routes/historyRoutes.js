const express = require('express');
const router = express.Router();
const { getCombinedHistory, deleteHistory, exportData } = require('../controllers/HistoryController');
const { protect } = require('../middleware/authMiddleware');

router.get('/', protect, getCombinedHistory);
router.delete('/', protect, deleteHistory);
router.get('/export', protect, exportData);

module.exports = router;
