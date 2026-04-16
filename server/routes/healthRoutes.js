const express = require('express');
const router = express.Router();
const { addHealthRecord, getMyRecords } = require('../controllers/healthController');
const { protect } = require('../middleware/authMiddleware');

router.post('/add-record', protect, addHealthRecord);
router.get('/my-records', protect, getMyRecords);

module.exports = router;
