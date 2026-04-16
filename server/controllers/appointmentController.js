const Appointment = require('../models/Appointment');
const Doctor = require('../models/Doctor');

// @desc    Book new appointment
// @route   POST /api/appointments/book
// @access  Private
const bookAppointment = async (req, res) => {
    try {
        const { doctor_id, date, time_slot, reason } = req.body;
        
        const doctor = await Doctor.findById(doctor_id);
        if (!doctor) {
            return res.status(404).json({ message: 'Doctor not found' });
        }

        // Check if slot is already booked (collision prevention)
        const startOfDay = new Date(date);
        startOfDay.setHours(0, 0, 0, 0);
        const endOfDay = new Date(date);
        endOfDay.setHours(23, 59, 59, 999);

        const existingAppointment = await Appointment.findOne({
            doctor_id,
            date: { $gte: startOfDay, $lte: endOfDay },
            time_slot,
            status: { $ne: 'Cancelled' }
        });

        if (existingAppointment) {
            return res.status(400).json({ message: 'This time slot is already booked' });
        }

        const appointment = await Appointment.create({
            user_id: req.user._id,
            doctor_id,
            date,
            time_slot,
            reason
        });

        res.status(201).json(appointment);
    } catch (error) {
        res.status(500).json({ message: error.message });
    }
};

// @desc    Get appointments for a specific user
// @route   GET /api/appointments/user/:userId
// @access  Private
const getUserAppointments = async (req, res) => {
    try {
        const appointments = await Appointment.find({ user_id: req.params.userId })
            .populate('doctor_id')
            .sort({ date: 1 });
        res.status(200).json(appointments);
    } catch (error) {
        res.status(500).json({ message: error.message });
    }
};

// @desc    Get appointments for a specific doctor
// @route   GET /api/appointments/doctor/:doctorId
// @access  Private
const getDoctorAppointments = async (req, res) => {
    try {
        const appointments = await Appointment.find({ doctor_id: req.params.doctorId })
            .populate('user_id', 'name email')
            .sort({ date: 1 });
        res.status(200).json(appointments);
    } catch (error) {
        res.status(500).json({ message: error.message });
    }
};

module.exports = {
    bookAppointment,
    getUserAppointments,
    getDoctorAppointments
};
