import 'dart:convert';
import 'package:http/http.dart' as http;
import 'package:shared_preferences/shared_preferences.dart';
import 'dart:io';
import '../config/api_config.dart';

class ApiService {
  static String get baseUrl => ApiConfig.baseUrl;
  
  static Future<Map<String, String>> getHeaders() async {
    final prefs = await SharedPreferences.getInstance();
    final token = prefs.getString('token');
    return {
      'Content-Type': 'application/json',
      if (token != null) 'Authorization': 'Bearer $token',
    };
  }


  // Fetch combined history
  static Future<List<dynamic>> getCombinedHistory() async {
    final headers = await getHeaders();
    final response = await http
        .get(Uri.parse('$baseUrl/history'), headers: headers)
        .timeout(ApiConfig.timeoutDuration);

    if (response.statusCode == 200) {
      return json.decode(response.body);
    } else {
      throw Exception('Failed to load history');
    }
  }

  // Delete all history
  static Future<void> deleteHistory() async {
    final headers = await getHeaders();
    final response = await http
        .delete(Uri.parse('$baseUrl/history'), headers: headers)
        .timeout(ApiConfig.timeoutDuration);

    if (response.statusCode != 200) {
      throw Exception('Failed to delete history');
    }
  }

  // Fetch health patterns
  static Future<List<dynamic>> getPatterns() async {
    final headers = await getHeaders();
    final response = await http
        .get(Uri.parse('$baseUrl/patterns'), headers: headers)
        .timeout(ApiConfig.timeoutDuration);

    if (response.statusCode == 200) {
      final data = json.decode(response.body);
      return data['patterns'];
    } else {
      throw Exception('Failed to analyze patterns');
    }
  }

  // Smart Chat with AI
  static Future<Map<String, dynamic>> sendSmartChatMessage(String message) async {
    final headers = await getHeaders();
    final response = await http
        .post(
          Uri.parse('$baseUrl/chat/ask'),
          headers: headers,
          body: json.encode({'message': message}),
        )
        .timeout(ApiConfig.timeoutDuration);

    if (response.statusCode == 200) {
      return json.decode(response.body);
    } else {
      throw Exception('Failed to get AI response');
    }
  }

  // Get Recommended Doctors
  static Future<Map<String, dynamic>> getRecommendedDoctors(String disease, String? city, {double? lat, double? lng, bool isCritical = false}) async {
    final headers = await getHeaders();
    String url = '$baseUrl/doctors/recommend?disease=$disease';
    if (city != null && city.isNotEmpty) {
      url += '&city=$city';
    }
    if (lat != null && lng != null) {
      url += '&lat=$lat&lng=$lng';
    }
    if (isCritical) {
      url += '&isCritical=true';
    }

    final response = await http
        .get(
          Uri.parse(url),
          headers: headers,
        )
        .timeout(ApiConfig.timeoutDuration);

    if (response.statusCode == 200) {
      return json.decode(response.body);
    } else {
      throw Exception('Failed to load doctors');
    }
  }

  // Get Enhanced Recommendations
  static Future<Map<String, dynamic>> getRecommendations(String disease, String? city) async {
    final headers = await getHeaders();
    final body = jsonEncode({'disease': disease, 'city': city});

    final response = await http
        .post(
          Uri.parse('$baseUrl/recommendations/doctor'),
          headers: headers,
          body: body,
        )
        .timeout(ApiConfig.timeoutDuration);

    if (response.statusCode == 200) {
      return json.decode(response.body);
    } else {
      throw Exception('Failed to load recommendations');
    }
  }

  // Update User Preferences
  static Future<void> updatePreferences(Map<String, dynamic> preferences) async {
    final headers = await getHeaders();
    final body = jsonEncode(preferences);

    final response = await http
        .put(
          Uri.parse('$baseUrl/auth/preferences'),
          headers: headers,
          body: body,
        )
        .timeout(ApiConfig.timeoutDuration);

    if (response.statusCode != 200) {
      throw Exception('Failed to update preferences');
    }
  }

  // Export Data
  static Future<Map<String, dynamic>> exportData() async {
    final headers = await getHeaders();
    final response = await http
        .get(Uri.parse('$baseUrl/history/export'), headers: headers)
        .timeout(ApiConfig.timeoutDuration);

    if (response.statusCode == 200) {
      return json.decode(response.body);
    } else {
      throw Exception('Failed to export data');
    }
  }

  // Get User Profile
  static Future<Map<String, dynamic>> getUserProfile() async {
    final headers = await getHeaders();
    final response = await http
        .get(Uri.parse('$baseUrl/auth/profile'), headers: headers)
        .timeout(ApiConfig.timeoutDuration);

    if (response.statusCode == 200) {
      return json.decode(response.body);
    } else {
      throw Exception('Failed to load profile');
    }
  }

  // Get All Doctors
  static Future<List<dynamic>> getDoctors() async {
    final headers = await getHeaders();
    final response = await http
        .get(Uri.parse('$baseUrl/doctors'), headers: headers)
        .timeout(ApiConfig.timeoutDuration);

    if (response.statusCode == 200) {
      return json.decode(response.body);
    } else {
      throw Exception('Failed to load doctors');
    }
  }

  // Get Doctor By ID
  static Future<Map<String, dynamic>> getDoctorById(String id) async {
    final headers = await getHeaders();
    final response = await http
        .get(Uri.parse('$baseUrl/doctors/$id'), headers: headers)
        .timeout(ApiConfig.timeoutDuration);

    if (response.statusCode == 200) {
      return json.decode(response.body);
    } else {
      throw Exception('Failed to load doctor details');
    }
  }

  // Get User Appointments
  static Future<List<dynamic>> getAppointments() async {
    final prefs = await SharedPreferences.getInstance();
    final profileStr = prefs.getString('userProfile');
    String? userId;
    if (profileStr != null) {
      final profile = json.decode(profileStr);
      userId = profile['_id'];
    }
    
    // If not in prefs, we might need to fetch profile first or have it passed
    if (userId == null) {
      final profile = await getUserProfile();
      userId = profile['_id'];
      await prefs.setString('userProfile', json.encode(profile));
    }

    final headers = await getHeaders();
    final response = await http
        .get(Uri.parse('$baseUrl/appointments/user/$userId'), headers: headers)
        .timeout(ApiConfig.timeoutDuration);

    if (response.statusCode == 200) {
      return json.decode(response.body);
    } else {
      throw Exception('Failed to load appointments');
    }
  }

  // Get Doctor Availability
  static Future<List<String>> getDoctorAvailability(String doctorId, String date) async {
    final headers = await getHeaders();
    final response = await http
        .get(
          Uri.parse('$baseUrl/doctors/$doctorId/availability?date=$date'),
          headers: headers,
        )
        .timeout(ApiConfig.timeoutDuration);

    if (response.statusCode == 200) {
      final data = json.decode(response.body);
      return List<String>.from(data['availableSlots']);
    } else {
      throw Exception('Failed to load availability');
    }
  }

  // Book Appointment
  static Future<Map<String, dynamic>> bookAppointment(String doctorId, String date, String timeSlot, String reason) async {
    final headers = await getHeaders();
    final response = await http
        .post(
          Uri.parse('$baseUrl/appointments/book'),
          headers: headers,
          body: jsonEncode({
            'doctor_id': doctorId,
            'date': date,
            'time_slot': timeSlot,
            'reason': reason,
          }),
        )
        .timeout(ApiConfig.timeoutDuration);

    if (response.statusCode == 201) {
      return json.decode(response.body);
    } else {
      final errorData = json.decode(response.body);
      throw Exception(errorData['message'] ?? 'Failed to book appointment');
    }
  }
}
