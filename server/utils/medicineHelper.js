const fs = require('fs');
const path = require('path');

let medicines = [];

const loadMedicines = () => {
    if (medicines.length > 0) return; // Already loaded

    try {
        // Path adjusted relative to this file's location (server/utils/medicineHelper.js)
        const filePath = path.join(__dirname, '../../Medicine_Details.csv');
        if (!fs.existsSync(filePath)) {
            console.error("Medicine CSV not found at:", filePath);
            return;
        }

        const csvData = fs.readFileSync(filePath, 'utf8');
        
        const lines = csvData.split(/\r?\n/);
        if (lines.length < 2) return;

        const headers = lines[0].split(',').map(h => h.trim());
        
        for (let i = 1; i < lines.length; i++) {
            if (!lines[i].trim()) continue;
            
            // Split by comma ignoring commas inside quotes
            let cleanRow = lines[i].split(/,(?=(?:(?:[^"]*"){2})*[^"]*$)/);
            cleanRow = cleanRow.map(val => val ? val.replace(/^"|"$/g, '').trim() : '');
            
            const med = {};
            headers.forEach((h, index) => {
                med[h] = cleanRow[index];
            });
            medicines.push(med);
        }
        console.log(`Loaded ${medicines.length} medicines into memory.`);
    } catch (error) {
        console.error("Error loading medicines CSV:", error);
    }
}

const getMedicinesForDisease = (diseaseName) => {
    // 🔹 STEP 1: LOG THE PREDICTED DISEASE
    console.log(`\n--- DEBUG: MEDICINE MATCHING START ---`);
    console.log(`Predicted Disease (raw): "${diseaseName}"`);
    console.log(`Type: ${typeof diseaseName}`);

    if (!diseaseName) {
        console.error("Error: Disease name is undefined/null/empty!");
        return [];
    }

    // 🔹 STEP 2: NORMALIZE DISEASE NAME
    // trim spaces, lowercase, remove extra characters
    let normalizedDisease = String(diseaseName).trim().toLowerCase().replace(/[^a-z0-9 ]/g, '');
    console.log(`Normalized Disease: "${normalizedDisease}"`);

    // 🔹 STEP 3: LOAD MEDICINE DATASET PROPERLY
    console.log(`Total medicines loaded in dataset: ${medicines.length}`);
    if (medicines.length === 0) {
         console.error("Error: Medicine dataset length = 0. Dataset not loaded!");
         return [];
    }

    // 🔹 STEP 4: MATCH DISEASE WITH MEDICINE
    const matches = medicines.filter(med => {
        // According to user, the columns include: Disease Name, Medicine Name, Dosage, Usage Instructions, Precautions.
        // If my CSV parser read different columns (like Uses), we fall back gracefully, but try to use User's expected names first.
        const dName = med['Disease Name'] || med['Uses'] || '';
        const medNormalized = dName.trim().toLowerCase().replace(/[^a-z0-9 ]/g, '');
        // Match condition as close to user request as possible
        return medNormalized === normalizedDisease || medNormalized.includes(normalizedDisease);
    });

    console.log(`Found ${matches.length} matching medicines.`);
    console.log(`--- DEBUG: MEDICINE MATCHING END ---\n`);

    // 🔹 STEP 5: HANDLE MATCH RESULTS
    return matches.slice(0, 3).map(med => ({
        name: med['Medicine Name'] || 'Unknown Medicine',
        dosage: med['Dosage'] || med['Composition'] || 'Standard Dosage',
        howToUse: med['Usage Instructions'] || "Take as prescribed by a qualified doctor.",
        precautions: med['Precautions'] || med['Side_effects'] || "None specified"
    }));
}

module.exports = {
    loadMedicines,
    getMedicinesForDisease
};
