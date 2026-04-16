const mongoose = require('mongoose');
const dotenv = require('dotenv').config();
const { seedDoctors } = require('./controllers/doctorController');

const connectDB = async () => {
    try {
        console.log('Connecting to:', process.env.MONGO_URI);
        await mongoose.connect(process.env.MONGO_URI);
        console.log('MongoDB Connected');
        
        // Manual seeding logic to debug import
        const count = await mongoose.model('Doctor').countDocuments();
        console.log('Current Doctor Count:', count);
        
        if (count === 0) {
            await seedDoctors();
            console.log('Seed function called');
        } else {
            console.log('Database already has data. Clearing and re-seeding for test...');
            await mongoose.model('Doctor').deleteMany({});
            await seedDoctors();
            console.log('Re-seeded.');
        }

        const newCount = await mongoose.model('Doctor').countDocuments();
        console.log('New Doctor Count:', newCount);

        process.exit();
    } catch (error) {
        console.error(error);
        process.exit(1);
    }
};

connectDB();
