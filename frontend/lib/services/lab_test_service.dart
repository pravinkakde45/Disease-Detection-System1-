import 'dart:convert';
import 'package:shared_preferences/shared_preferences.dart';
import '../models/lab_test.dart';

class LabTestService {
  static const String _storageKey = 'lab_test_bookings';

  static final List<LabTest> _allTests = [
    LabTest(
      id: 't1',
      name: 'Complete Blood Count (CBC)',
      description: 'Measures different components of your blood, including red and white cells.',
      sampleType: 'Blood',
      fastingRequirement: 'Not Required',
      reportTime: '24 Hours',
      price: 500.0,
      suggestedForSymptoms: ['fever', 'weakness', 'fatigue', 'infection'],
    ),
    LabTest(
      id: 't2',
      name: 'Diabetic Profile (Basic)',
      description: 'Includes HbA1c and Fasting Blood Sugar tests to monitor glucose levels.',
      sampleType: 'Blood',
      fastingRequirement: '8-10 Hours Fasting',
      reportTime: '12 Hours',
      price: 800.0,
      suggestedForSymptoms: ['polyuria', 'thirst', 'blurred vision', 'diabetes'],
    ),
    LabTest(
      id: 't3',
      name: 'Thyroid Profile (T3, T4, TSH)',
      description: 'Evaluates thyroid gland function.',
      sampleType: 'Blood',
      fastingRequirement: 'Not Required',
      reportTime: '24 Hours',
      price: 600.0,
      suggestedForSymptoms: ['weight gain', 'weight loss', 'hair fall', 'fatigue'],
    ),
    LabTest(
      id: 't4',
      name: 'Lipid Profile',
      description: 'Measures cholesterol and triglyceride levels.',
      sampleType: 'Blood',
      fastingRequirement: '9-12 Hours Fasting',
      reportTime: '24 Hours',
      price: 700.0,
      suggestedForSymptoms: ['chest pain', 'high blood pressure', 'obesity'],
    ),
    LabTest(
      id: 't5',
      name: 'Liver Function Test (LFT)',
      description: 'Checks how well your liver is working.',
      sampleType: 'Blood',
      fastingRequirement: 'Not Required',
      reportTime: '24 Hours',
      price: 900.0,
      suggestedForSymptoms: ['jaundice', 'abdominal pain', 'nausea'],
    ),
    LabTest(
      id: 't6',
      name: 'Kidney Function Test (KFT)',
      description: 'Measures urea, creatinine, and electrolytes.',
      sampleType: 'Blood',
      fastingRequirement: 'Not Required',
      reportTime: '24 Hours',
      price: 850.0,
      suggestedForSymptoms: ['swelling', 'back pain', 'frequent urination'],
    ),
  ];

  static List<LabTest> getAllTests() {
    return _allTests;
  }

  static List<LabTest> getSuggestedTests(List<String> userSymptoms) {
    if (userSymptoms.isEmpty) return [];
    
    return _allTests.where((test) {
      return test.suggestedForSymptoms.any((symptom) => 
        userSymptoms.any((userSymp) => userSymp.toLowerCase().contains(symptom.toLowerCase()))
      );
    }).toList();
  }

  static Future<void> saveBooking(LabTestBooking booking) async {
    final prefs = await SharedPreferences.getInstance();
    final List<String> bookingsJson = prefs.getStringList(_storageKey) ?? [];
    bookingsJson.add(jsonEncode(booking.toJson()));
    await prefs.setStringList(_storageKey, bookingsJson);
  }

  static Future<List<LabTestBooking>> getBookings() async {
    final prefs = await SharedPreferences.getInstance();
    final List<String> bookingsJson = prefs.getStringList(_storageKey) ?? [];
    return bookingsJson.map((item) => LabTestBooking.fromJson(jsonDecode(item))).toList().reversed.toList();
  }
}
