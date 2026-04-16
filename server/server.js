const express = require('express');
const dotenv = require('dotenv').config();
const cors = require('cors');
const connectDB = require('./config/db');

// Connect to database
// Connect to database
connectDB();
const { seedDoctors } = require('./controllers/doctorController');
seedDoctors();

const app = express();

// Middleware
app.use(express.json());
app.use(express.urlencoded({ extended: false }));
app.use(cors());

// Routes
app.use('/api/auth', require('./routes/authRoutes'));
app.use('/api/user', require('./routes/authRoutes')); // Profile is under authRoutes but mapped to /user/profile in prompt spec, so we can alias or restructure. The prompt asked for GET /api/user/profile. My authRoutes has GET /profile so mounting at /api/auth makes it /api/auth/profile. I will mount it at /api/user as well for compliance or adjust route.
// Adjusting: The prompt asked for GET /api/user/profile. 
// My authRoutes: router.get('/profile', ...).
// So mounting authRoutes at /api/user gives /api/user/profile.
// But authRoutes also has /register, so that would be /api/user/register.
// Better to split or just dual mount for simplicity in this artifact.
app.use('/api/disease', require('./routes/diseaseRoutes'));
app.use('/api/chat', require('./routes/chatRoutes'));
app.use('/api/health', require('./routes/healthRoutes'));
app.use('/api/history', require('./routes/historyRoutes'));
app.use('/api/patterns', require('./routes/patternRoutes'));
app.use('/api/doctors', require('./routes/doctorRoutes'));
app.use('/api/recommendations', require('./routes/recommendationRoutes'));
app.use('/api/appointments', require('./routes/appointmentRoutes'));


const port = process.env.PORT || 5000;

app.listen(port, '0.0.0.0', () => console.log(`Server started on port ${port}`));
