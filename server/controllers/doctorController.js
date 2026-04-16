const Doctor = require('../models/Doctor');

// Mapping diseases to specializations
const diseaseSpecialistMap = {
    // Heart
    'heart attack': 'Cardiologist',
    'hypertension': 'Cardiologist',
    'stroke': 'Neurologist',
    
    // Brain/Neuro
    'migraine': 'Neurologist',
    'paralysis': 'Neurologist',
    
    // Skin
    'acne': 'Dermatologist',
    'fungal infection': 'Dermatologist',
    'psoriasis': 'Dermatologist',
    
    // Digestive
    'gerd': 'Gastroenterologist',
    'jaundice': 'Gastroenterologist',
    'peptic ulcer': 'Gastroenterologist',
    
    // General/Infection
    'malaria': 'General Physician',
    'dengue': 'General Physician',
    'typhoid': 'General Physician',
    'common cold': 'General Physician',
    'pneumonia': 'Pulmonologist',
    'tuberculosis': 'Pulmonologist',
    
    // Ortho
    'arthritis': 'Orthopedic',
    'osteosclerosis': 'Orthopedic',
    
    // Default
    'default': 'General Physician'
};

// Seed function to populate some dummy data if empty
const seedDoctors = async () => {
    await Doctor.deleteMany({});
    const Appointment = require('../models/Appointment');
    await Appointment.deleteMany({});
    
    const count = await Doctor.countDocuments();
    if (count === 0) {
        const doctors = [
            { 
                name: "Dr. Arvind Sharma", 
                qualification: "MD, DM (Cardiology)",
                specialization: "Cardiologist", 
                hospital_or_clinic_name: "Heart Care Clinic", 
                address: "Flat 102, Sunrise Apts, Bandra West", 
                city: "Mumbai", 
                phone: "022-26401234", 
                consultation_fee: 1500,
                available_days: ["Monday", "Wednesday", "Friday"],
                available_time_slots: ["10:00 AM - 10:30 AM", "10:30 AM - 11:00 AM", "11:00 AM - 11:30 AM", "04:00 PM - 04:30 PM", "04:30 PM - 05:00 PM"],
                is_active: true,
                location: { lat: 19.0544, lng: 72.8402 } 
            },
            { 
                name: "Dr. Sunita Verma", 
                qualification: "MBBS, MD (Neurology)",
                specialization: "Neurologist", 
                hospital_or_clinic_name: "Brain Health Center", 
                address: "45 Neuro Path, Colaba", 
                city: "Mumbai", 
                phone: "022-22025678", 
                consultation_fee: 1800,
                available_days: ["Tuesday", "Thursday", "Saturday"],
                available_time_slots: ["11:00 AM - 11:30 AM", "11:30 AM - 12:00 PM", "12:00 PM - 12:30 PM"],
                is_active: true,
                location: { lat: 18.9218, lng: 72.8335 } 
            },
            { 
                name: "Dr. Rajesh Gupta", 
                qualification: "MBBS, DDVL",
                specialization: "Dermatologist", 
                hospital_or_clinic_name: "Skin & Glow", 
                address: "78 Derma Road, Karol Bagh", 
                city: "Delhi", 
                phone: "011-25712345", 
                consultation_fee: 1200,
                available_days: ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
                available_time_slots: ["10:00 AM - 10:30 AM", "11:00 AM - 11:30 AM", "12:00 PM - 12:30 PM"],
                is_active: true,
                location: { lat: 28.6550, lng: 77.1888 } 
            },
            { 
                name: "Dr. Meera Singh", 
                qualification: "MBBS, MD (General Medicine)",
                specialization: "General Physician", 
                hospital_or_clinic_name: "City Hospital", 
                address: "101 City Center, MG Road", 
                city: "Bangalore", 
                phone: "080-25591010", 
                consultation_fee: 800,
                available_days: ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
                available_time_slots: ["09:00 AM - 09:30 AM", "10:00 AM - 10:30 AM", "11:00 AM - 11:30 AM", "12:00 PM - 12:30 PM"],
                is_active: true,
                location: { lat: 12.9767, lng: 77.5936 } 
            },
            { 
                name: "Dr. Vikram Seth", 
                qualification: "MBBS, MD, DM (Gastro)",
                specialization: "Gastroenterologist", 
                hospital_or_clinic_name: "Digestive Care", 
                address: "202 Belly Blvd, Salt Lake", 
                city: "Kolkata", 
                phone: "033-23351234", 
                consultation_fee: 1400,
                available_days: ["Wednesday", "Thursday", "Friday"],
                available_time_slots: ["02:00 PM - 02:30 PM", "03:00 PM - 03:30 PM", "04:00 PM - 04:30 PM"],
                is_active: true,
                location: { lat: 22.5830, lng: 88.4111 } 
            },
            { 
                name: "Dr. Anjali Rao", 
                qualification: "MBBS, DCH",
                specialization: "Pediatrician", 
                hospital_or_clinic_name: "Kids Clinic", 
                address: "12 Child Way, Jubilee Hills", 
                city: "Hyderabad", 
                phone: "040-23548901", 
                consultation_fee: 1000,
                available_days: ["Monday", "Wednesday", "Friday", "Saturday"],
                available_time_slots: ["10:00 AM - 10:30 AM", "11:00 AM - 11:30 AM", "12:00 PM - 12:30 PM"],
                is_active: true,
                location: { lat: 17.4325, lng: 78.4071 } 
            },
            { 
                name: "Dr. Karen Wilson", 
                qualification: "MBBS, MD (Chest)",
                specialization: "Pulmonologist", 
                hospital_or_clinic_name: "Breathe Easy Center", 
                address: "303 Oxygen Lane, Indiranagar", 
                city: "Bangalore", 
                phone: "080-25256789", 
                consultation_fee: 1300,
                available_days: ["Monday", "Tuesday", "Thursday", "Friday"],
                available_time_slots: ["11:00 AM - 11:30 AM", "12:00 PM - 12:30 PM", "01:00 PM - 01:30 PM"],
                is_active: true,
                location: { lat: 12.9719, lng: 77.6412 } 
            },
            { 
                name: "Dr. Sanjay Malhotra", 
                qualification: "MBBS, MS (Ortho)",
                specialization: "Orthopedic", 
                hospital_or_clinic_name: "Bone & Joint Center", 
                address: "55 Fracture Road, Sector 18", 
                city: "Noida", 
                phone: "0120-2512345", 
                consultation_fee: 1100,
                available_days: ["Tuesday", "Thursday", "Saturday"],
                available_time_slots: ["05:00 PM - 05:30 PM", "06:00 PM - 06:30 PM", "07:00 PM - 07:30 PM"],
                is_active: true,
                location: { lat: 28.5700, lng: 77.3200 } 
            },
            { 
                name: "Dr. Priya Das", 
                qualification: "MBBS, DGO, MS",
                specialization: "Gynecologist", 
                hospital_or_clinic_name: "Women's Wellness", 
                address: "88 Orchid Ave, T Nagar", 
                city: "Chennai", 
                phone: "044-24345678", 
                consultation_fee: 1200,
                available_days: ["Monday", "Wednesday", "Friday"],
                available_time_slots: ["11:00 AM - 11:30 AM", "12:00 PM - 12:30 PM", "01:00 PM - 01:30 PM"],
                is_active: true,
                location: { lat: 13.0418, lng: 80.2341 } 
            },
            { 
                name: "Dr. Rahul Kapoor", 
                qualification: "MBBS, MD, DM (Endo)",
                specialization: "Endocrinologist", 
                hospital_or_clinic_name: "Diabetes Care", 
                address: "22 Insulin Street, Pune Camp", 
                city: "Pune", 
                phone: "020-26123456", 
                consultation_fee: 1600,
                available_days: ["Tuesday", "Thursday", "Saturday"],
                available_time_slots: ["10:00 AM - 10:30 AM", "11:00 AM - 11:30 AM", "12:00 PM - 12:30 PM"],
                is_active: true,
                location: { lat: 18.5204, lng: 73.8567 } 
            },
            { 
                name: "Dr. Amit Trivedi", 
                qualification: "MD (Psychiatry)",
                specialization: "Psychiatrist", 
                hospital_or_clinic_name: "Mind Care Clinic", 
                address: "Flat 405, Peace Apts, Navrangpura", 
                city: "Ahmedabad", 
                phone: "079-26441234", 
                consultation_fee: 1400,
                available_days: ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
                available_time_slots: ["10:00 AM - 10:30 AM", "11:00 AM - 11:30 AM", "04:00 PM - 04:30 PM", "05:00 PM - 05:30 PM"],
                is_active: true,
                location: { lat: 23.0225, lng: 72.5714 } 
            },
            { 
                name: "Dr. Sneha Kulkarni", 
                qualification: "MBBS, MS (Ophthalmology)",
                specialization: "Ophthalmologist", 
                hospital_or_clinic_name: "Eye Sight Center", 
                address: "Shop 12, Vision Plaza, Kothrud", 
                city: "Pune", 
                phone: "020-25445678", 
                consultation_fee: 900,
                available_days: ["Monday", "Wednesday", "Friday", "Saturday"],
                available_time_slots: ["10:00 AM - 10:30 AM", "11:00 AM - 11:30 AM", "12:00 PM - 12:30 PM"],
                is_active: true,
                location: { lat: 18.5074, lng: 73.8077 } 
            },
            { 
                name: "Dr. Ritesh Deshmukh", 
                qualification: "MBBS, MS (ENT)",
                specialization: "ENT Specialist", 
                hospital_or_clinic_name: "Hearing & Care", 
                address: "202 Sound Tower, Andheri East", 
                city: "Mumbai", 
                phone: "022-26881234", 
                consultation_fee: 1100,
                available_days: ["Tuesday", "Thursday", "Saturday"],
                available_time_slots: ["05:00 PM - 05:30 PM", "06:00 PM - 06:30 PM", "07:00 PM - 07:30 PM"],
                is_active: true,
                location: { lat: 19.1136, lng: 72.8697 } 
            },
            { 
                name: "Dr. Kavita Nair", 
                qualification: "MBBS, MD (Endo)",
                specialization: "Endocrinologist", 
                hospital_or_clinic_name: "Hormone Health", 
                address: "Flat 101, Wellness Apts, MG Road", 
                city: "Kochi", 
                phone: "0484-2351234", 
                consultation_fee: 1300,
                available_days: ["Monday", "Tuesday", "Thursday", "Friday"],
                available_time_slots: ["11:00 AM - 11:30 AM", "12:00 PM - 12:30 PM", "01:00 PM - 01:30 PM"],
                is_active: true,
                location: { lat: 9.9312, lng: 76.2673 } 
            },
            { 
                name: "Dr. Manoj Bajpayee", 
                qualification: "MBBS, MD (Oncology)",
                specialization: "Oncologist", 
                hospital_or_clinic_name: "Cancer Cure Center", 
                address: "Flat 505, Hope Tower, Rohini", 
                city: "Delhi", 
                phone: "011-27005678", 
                consultation_fee: 2000,
                available_days: ["Monday", "Wednesday", "Friday"],
                available_time_slots: ["10:00 AM - 10:30 AM", "11:00 AM - 11:30 AM", "12:00 PM - 12:30 PM"],
                is_active: true,
                location: { lat: 28.7041, lng: 77.1025 } 
            }
        ];
        await Doctor.insertMany(doctors);
    }
};

// @desc    Get all doctors
// @route   GET /api/doctors
// @access  Public
const getDoctors = async (req, res) => {
    try {
        const doctors = await Doctor.find({ is_active: true });
        res.status(200).json(doctors);
    } catch (error) {
        res.status(500).json({ message: error.message });
    }
};

// @desc    Get doctor by ID
// @route   GET /api/doctors/:id
// @access  Public
const getDoctorById = async (req, res) => {
    try {
        const doctor = await Doctor.findById(req.params.id);
        if (!doctor) {
            return res.status(404).json({ message: 'Doctor not found' });
        }
        res.status(200).json(doctor);
    } catch (error) {
        res.status(500).json({ message: error.message });
    }
};

// Haversine Formula to calculate distance between two points in km
const calculateDistance = (lat1, lon1, lat2, lon2) => {
    const toRad = (value) => (value * Math.PI) / 180;
    const R = 6371; // Radius of Earth in km
    const dLat = toRad(lat2 - lat1);
    const dLon = toRad(lon2 - lon1);
    const a = Math.sin(dLat / 2) * Math.sin(dLat / 2) +
              Math.cos(toRad(lat1)) * Math.cos(toRad(lat2)) *
              Math.sin(dLon / 2) * Math.sin(dLon / 2);
    const c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1 - a));
    return R * c; // Distance in km
};

// @desc    Recommend doctors based on disease and location
// @route   GET /api/doctors/recommend
// @access  Private
const recommendDoctors = async (req, res) => {
    try {
        const { disease, city, lat, lng, isCritical } = req.query;
        
        // 1. Determine Specialization
        const lowerDisease = (disease || '').toLowerCase();
        let specialization = 'General Physician';
        
        // Simple substring match for mapping
        for (const [key, value] of Object.entries(diseaseSpecialistMap)) {
            if (lowerDisease.includes(key)) {
                specialization = value;
                break;
            }
        }
        console.log(`Recommending ${specialization} for ${disease} (Critical: ${isCritical})`);

        // 2. Fetch ALL active doctors to ensure all 15 are available
        let allDoctors = await Doctor.find({ is_active: true }).lean();
        
        // 3. Score and Sort Doctors
        const userLat = parseFloat(lat);
        const userLng = parseFloat(lng);
        const hasLocation = !isNaN(userLat) && !isNaN(userLng);
        
        const scoredDoctors = allDoctors.map(doc => {
            // Calculate distance
            if (hasLocation && doc.location && doc.location.lat && doc.location.lng) {
                doc.distance = calculateDistance(userLat, userLng, doc.location.lat, doc.location.lng);
            } else {
                doc.distance = Infinity;
            }

            // Calculate relevance score (0 = specialst match, 1 = general match, 2 = other)
            let relevance = 2;
            if (doc.specialization === specialization) {
                relevance = 0;
            } else if (doc.specialization === 'General Physician') {
                relevance = 1;
            }
            
            doc.relevance = relevance;
            doc.distanceDisplay = (doc.distance !== Infinity && doc.distance < 1000) 
                ? `${doc.distance.toFixed(1)} km` 
                : 'Far';
                
            return doc;
        });

        // Sort by relevance first, then by distance
        scoredDoctors.sort((a, b) => {
            if (a.relevance !== b.relevance) {
                return a.relevance - b.relevance;
            }
            return a.distance - b.distance;
        });


        res.status(200).json({
            specialization,
            isCritical: isCritical === 'true',
            doctors: scoredDoctors
        });

    } catch (error) {
        console.error(error);
        res.status(500).json({ message: error.message });
    }
};

// @desc    Get doctor availability for a specific date
// @route   GET /api/doctors/:id/availability
// @access  Private
const getDoctorAvailability = async (req, res) => {
    try {
        const { date } = req.query;
        const doctorId = req.params.id;

        if (!date) {
            return res.status(400).json({ message: 'Date is required' });
        }

        const doctor = await Doctor.findById(doctorId);
        if (!doctor) {
            return res.status(404).json({ message: 'Doctor not found' });
        }

        const selectedDate = new Date(date);
        const days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'];
        const dayName = days[selectedDate.getDay()];

        // Find availability for that day
        const isDayAvailable = doctor.available_days.includes(dayName);
        if (!isDayAvailable) {
            return res.status(200).json({ availableSlots: [] });
        }

        // Find already booked appointments for this doctor on this date
        const startOfDay = new Date(selectedDate.setHours(0, 0, 0, 0));
        const endOfDay = new Date(selectedDate.setHours(23, 59, 59, 999));

        const Appointment = require('../models/Appointment'); // Lazy load to avoid circular dep
        const bookedAppointments = await Appointment.find({
            doctor: doctorId,
            date: { $gte: startOfDay, $lte: endOfDay },
            status: { $ne: 'Cancelled' }
        });

        const bookedSlots = bookedAppointments.map(appt => appt.timeSlot);
        const availableSlots = doctor.available_time_slots.filter(slot => !bookedSlots.includes(slot));

        res.status(200).json({ availableSlots });

    } catch (error) {
        console.error(error);
        res.status(500).json({ message: error.message });
    }
};

module.exports = {
    recommendDoctors,
    seedDoctors,
    getDoctorAvailability,
    getDoctors,
    getDoctorById
};
