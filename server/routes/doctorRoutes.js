const express = require('express');
const router = express.Router();
const { recommendDoctors, seedDoctors, getDoctorAvailability, getDoctors, getDoctorById } = require('../controllers/doctorController');
const { protect } = require('../middleware/authMiddleware');

// Trigger seed on load (optional, or call manually)
// seedDoctors() is called from server.js

router.get('/', protect, getDoctors);
router.get('/recommend', protect, recommendDoctors);
router.get('/:id', protect, getDoctorById);
router.get('/:id/availability', protect, getDoctorAvailability);

module.exports = router;
