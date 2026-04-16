const axios = require('axios');
const jwt = require('jsonwebtoken');

const BASE_URL = 'http://localhost:5000/api/doctors/recommend';
const JWT_SECRET = 'supersecretkey12345'; // Hardcoded from .env for test

// Mumbai Coordinates
const MY_LAT = 19.0760;
const MY_LNG = 72.8777;

const validObjectId = '507f1f77bcf86cd799439011'; // Valid 24 hex char ID
const token = jwt.sign({ id: validObjectId }, JWT_SECRET, { expiresIn: '1h' });
const headers = { Authorization: `Bearer ${token}` };

const mongoose = require('mongoose');
const Doctor = require('./models/Doctor'); // Assuming this path is correct relative to CWD
require('dotenv').config();

async function testLocationLogic() {
    console.log("--- Testing Location-Based Recommendations ---");

    try {
        console.log('Connecting to:', process.env.MONGO_URI);
        await mongoose.connect(process.env.MONGO_URI);
        const count = await Doctor.countDocuments();
        console.log(`[Direct DB] Doctor count: ${count}`);
        const allDocs = await Doctor.find({});
        console.log(`[Direct DB] All docs:`, allDocs.map(d => `${d.name} - ${d.specialization}`));

        // Debug: Check what doctors exist via API
        // ...
        console.log("--- Debug: Checking Database ---");
        const debugRes = await axios.get(`${BASE_URL}?disease=default`, { headers });
        console.log("Total doctors returned:", debugRes.data.doctors.length);
        if (debugRes.data.doctors.length > 0) {
             console.log("Sample Doctor:", JSON.stringify(debugRes.data.doctors[0], null, 2));
        }

        // Test 1: Normal Disease (Acne) - User in Mumbai
        console.log("\nTest 1: Normal Disease (Acne) - User in Mumbai");
        // Dr. C. Gupta is in Delhi (Far), others in Mumbai (Near)
        const res1 = await axios.get(`${BASE_URL}?disease=acne&lat=${MY_LAT}&lng=${MY_LNG}&isCritical=false`, { headers });
        console.log("Doctors found:", res1.data.doctors.length);
        res1.data.doctors.forEach(d => console.log(`- ${d.name} (${d.distanceDisplay})`));
        
        // Test 2: Critical Disease (Heart Attack) - User in New York
        // Should ignore 10km limit and find Mumbai doctors if none in NY
        console.log("\nTest 2: Critical Disease (Heart Attack) - User in Random Location (0,0)");
        const res2 = await axios.get(`${BASE_URL}?disease=heart attack&lat=0&lng=0&isCritical=true`, { headers });
        console.log("Doctors found:", res2.data.doctors.length);
        console.log("First doctor distance:", res2.data.doctors[0]?.distanceDisplay);

    } catch (e) {
        console.error("Test failed:", e.message);
        if (e.response) console.error(e.response.data);
    }
}

testLocationLogic();
