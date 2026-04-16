const express = require('express');
const router = express.Router();
const { bookAppointment, getUserAppointments, getDoctorAppointments } = require('../controllers/appointmentController');
const { protect } = require('../middleware/authMiddleware');

router.post('/book', protect, bookAppointment);
router.get('/user/:userId', protect, getUserAppointments);
router.get('/doctor/:doctorId', protect, getDoctorAppointments);

module.exports = router;
