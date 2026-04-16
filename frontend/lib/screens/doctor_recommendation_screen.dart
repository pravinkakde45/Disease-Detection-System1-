import 'package:flutter/material.dart';
import 'package:url_launcher/url_launcher.dart';
import 'package:geolocator/geolocator.dart';
import 'package:intl/intl.dart';
import '../services/api_service.dart';
import 'doctor_detail_screen.dart';

class DoctorRecommendationScreen extends StatefulWidget {
  final String predictedDisease;

  const DoctorRecommendationScreen({Key? key, required this.predictedDisease}) : super(key: key);

  @override
  _DoctorRecommendationScreenState createState() => _DoctorRecommendationScreenState();
}

class _DoctorRecommendationScreenState extends State<DoctorRecommendationScreen> {
  bool _isLoading = true;
  String _specialization = '';
  List<dynamic> _doctors = [];
  String? _currentCity;
  String _errorMessage = '';

  @override
  void initState() {
    super.initState();
    _fetchLocationAndDoctors();
  }

  Future<void> _fetchLocationAndDoctors() async {
    // 1. Get Location
    double? lat;
    double? lng;
    
    try {
      LocationPermission permission = await Geolocator.checkPermission();
      if (permission == LocationPermission.denied) {
        permission = await Geolocator.requestPermission();
      }
      
      if (permission == LocationPermission.whileInUse || permission == LocationPermission.always) {
        Position position = await Geolocator.getCurrentPosition(desiredAccuracy: LocationAccuracy.high);
        lat = position.latitude;
        lng = position.longitude;
      }
    } catch (e) {
      print("Error getting location: $e");
      // Continue without location
    }

    // Determine if critical (Simple heuristic for demo)
    bool isCritical = ['heart attack', 'stroke', 'paralysis'].contains(widget.predictedDisease.toLowerCase());

    try {
      final result = await ApiService.getRecommendedDoctors(widget.predictedDisease, _currentCity, lat: lat, lng: lng, isCritical: isCritical);
      if (mounted) {
        setState(() {
          _specialization = result['specialization'];
          _doctors = result['doctors'];
          _isLoading = false;
        });
      }
    } catch (e) {
      if (mounted) {
        setState(() {
          _errorMessage = e.toString();
          _isLoading = false;
        });
      }
    }
  }

  Future<void> _launchDialer(String number) async {
    final Uri launchUri = Uri(scheme: 'tel', path: number);
    if (!await launchUrl(launchUri)) {
      ScaffoldMessenger.of(context).showSnackBar(const SnackBar(content: Text('Could not launch dialer')));
    }
  }

  Future<void> _launchMap(dynamic location, String address) async {
    // If we have lat/lng use that, else query address
    Uri uri;
    if (location != null && location['lat'] != null) {
      uri = Uri.parse('https://www.google.com/maps/search/?api=1&query=${location['lat']},${location['lng']}');
    } else {
      uri = Uri.parse('https://www.google.com/maps/search/?api=1&query=${Uri.encodeComponent(address)}');
    }

    if (!await launchUrl(uri, mode: LaunchMode.externalApplication)) {
       ScaffoldMessenger.of(context).showSnackBar(const SnackBar(content: Text('Could not launch maps')));
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Recommended Doctors')),
      body: Column(
        children: [
           Container(
             padding: const EdgeInsets.all(16),
             color: Colors.blue[50],
             width: double.infinity,
             child: Column(
               children: [
                 Text('Disease: ${widget.predictedDisease}', style: const TextStyle(fontSize: 16)),
                 if (_specialization.isNotEmpty)
                  Text('Specialist Required: $_specialization', style: const TextStyle(fontSize: 18, fontWeight: FontWeight.bold, color: Colors.blue)),
               ],
             ),
           ),
           Expanded(
             child: _isLoading 
              ? const Center(child: CircularProgressIndicator())
              : _errorMessage.isNotEmpty 
                ? Center(child: Text('Error: $_errorMessage'))
                : _doctors.isEmpty 
                  ? const Center(child: Text('No doctors found nearby.'))
                  : ListView.builder(
                      itemCount: _doctors.length,
                      itemBuilder: (context, index) {
                        final doctor = _doctors[index];
                        return Card(
                          margin: const EdgeInsets.symmetric(horizontal: 16, vertical: 8),
                          child: Padding(
                            padding: const EdgeInsets.all(16),
                            child: Column(
                              crossAxisAlignment: CrossAxisAlignment.start,
                              children: [
                                Row(
                                  mainAxisAlignment: MainAxisAlignment.spaceBetween,
                                  children: [
                                    Expanded(child: Text(doctor['name'], style: const TextStyle(fontSize: 18, fontWeight: FontWeight.bold))),
                                    Container(
                                      padding: const EdgeInsets.symmetric(horizontal: 8, vertical: 4),
                                      decoration: BoxDecoration(color: Colors.green[100], borderRadius: BorderRadius.circular(8)),
                                      child: Text(doctor['specialization'], style: const TextStyle(color: Colors.green, fontSize: 12)),
                                    )
                                  ],
                                ),
                                const SizedBox(height: 4),
                                Text(doctor['qualification'] ?? '', style: const TextStyle(color: Colors.blueGrey, fontSize: 13, fontWeight: FontWeight.bold)),
                                const SizedBox(height: 4),
                                Text(doctor['hospital_or_clinic_name'], style: const TextStyle(fontWeight: FontWeight.w500)),
                                Text(doctor['address'], style: const TextStyle(color: Colors.grey)),
                                Row(
                                  children: [
                                    Text(doctor['city']),
                                    if (doctor['distanceDisplay'] != null)
                                      Padding(
                                        padding: const EdgeInsets.only(left: 8.0),
                                        child: Text(
                                          '(${doctor['distanceDisplay']})', 
                                          style: TextStyle(color: Colors.blue[700], fontWeight: FontWeight.bold)
                                        ),
                                      ),
                                  ],
                                ),
                                const SizedBox(height: 4),
                                Row(
                                  children: [
                                    const Icon(Icons.phone, size: 14, color: Colors.grey),
                                    const SizedBox(width: 4),
                                    Text(doctor['phone'] ?? '', style: const TextStyle(color: Colors.grey)),
                                    const Spacer(),
                                    Text('Fees: ₹${doctor['consultation_fee']}', style: const TextStyle(fontWeight: FontWeight.bold, color: Colors.green)),
                                  ],
                                ),
                                const SizedBox(height: 16),
                                Row(
                                  mainAxisAlignment: MainAxisAlignment.spaceEvenly,
                                  children: [
                                    ElevatedButton.icon(
                                      icon: const Icon(Icons.call, size: 18),
                                      label: const Text('Call'),
                                      onPressed: () => _launchDialer(doctor['phone'] ?? ''),
                                      style: ElevatedButton.styleFrom(backgroundColor: Colors.green),
                                    ),
                                    ElevatedButton.icon(
                                      icon: const Icon(Icons.calendar_today, size: 18),
                                      label: const Text('Book'),
                                      onPressed: () {
                                        Navigator.push(
                                          context,
                                          MaterialPageRoute(
                                            builder: (context) => DoctorDetailScreen(doctor: doctor),
                                          ),
                                        ).then((_) => _fetchLocationAndDoctors());
                                      },
                                      style: ElevatedButton.styleFrom(backgroundColor: Colors.blue),
                                    ),
                                    OutlinedButton.icon(
                                      icon: const Icon(Icons.map, size: 18),
                                      label: const Text('Map'),
                                      onPressed: () => _launchMap(doctor['location'], '${doctor['address']}, ${doctor['city']}'),
                                    ),
                                  ],
                                )
                              ],
                            ),
                          ),
                        );
                      },
                    ),
           ),
           Container(
             padding: const EdgeInsets.all(12),
             color: Colors.grey[200],
             child: const Text(
               'Disclaimer: This is an AI prediction. Please consult a qualified doctor for diagnosis and treatment.',
               style: TextStyle(fontSize: 12, color: Colors.black54),
               textAlign: TextAlign.center,
             ),
           )
        ],
      ),
    );
  }
}
