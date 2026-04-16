import 'package:flutter/material.dart';
import '../../services/api_service.dart';
import 'package:geolocator/geolocator.dart';
import 'package:url_launcher/url_launcher.dart';
import '../lab/lab_test_home_screen.dart';

class PredictionResultScreen extends StatefulWidget {
  final Map<String, dynamic> result;

  PredictionResultScreen({required this.result});

  @override
  _PredictionResultScreenState createState() => _PredictionResultScreenState();
}

class _PredictionResultScreenState extends State<PredictionResultScreen> {
  bool _isLoading = true;
  Map<String, dynamic>? _recommendations;
  String _errorMessage = '';

  @override
  void initState() {
    super.initState();
    _fetchRecommendations();
  }

  Future<void> _fetchRecommendations() async {
    try {
      // 1. Get Location (Mocking for now as geocoding needs API)
      // In real scenario: GeoLocator -> Lat/Lng -> Reverse Geocode -> City Name
      // For now, defaulting to null to test backend fallback, or "Mumbai" if hardcoded
      String? city; 
      
      // Best effort location
      LocationPermission permission = await Geolocator.checkPermission();
      if (permission == LocationPermission.denied) {
        permission = await Geolocator.requestPermission();
      }

      final disease = widget.result['primary_disease'];
      final data = await ApiService.getRecommendations(disease, city);

      if (mounted) {
        setState(() {
          _recommendations = data;
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
    if (number.isEmpty) return;
    final Uri launchUri = Uri(scheme: 'tel', path: number);
    if (!await launchUrl(launchUri)) {
      ScaffoldMessenger.of(context).showSnackBar(const SnackBar(content: Text('Could not launch dialer')));
    }
  }

  Future<void> _launchMap(dynamic location, String address) async {
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

  Color _confColor(double c) {
      if (c > 80) return Colors.red;
      if (c > 50) return Colors.orange;
      return Colors.green;
  }

  @override
  Widget build(BuildContext context) {
    final primary = widget.result['primary_disease'];
    final confidence = widget.result['confidence'];
    final possible = widget.result['possible_diseases'] as List<dynamic>;

    return Scaffold(
      appBar: AppBar(title: Text("Analysis Result")),
      body: SingleChildScrollView(
        padding: EdgeInsets.all(20),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.stretch,
          children: [
            // Prediction Card
            Card(
                color: Colors.red[50],
                shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(15)),
                child: Padding(
                    padding: EdgeInsets.all(24),
                    child: Column(
                        children: [
                            Text("Most Likely Condition", style: TextStyle(fontSize: 16, color: Colors.grey[700])),
                            SizedBox(height: 10),
                            Text(primary, style: TextStyle(fontSize: 32, fontWeight: FontWeight.bold, color: Colors.blue[900])),
                            SizedBox(height: 10),
                            LinearProgressIndicator(
                                value: (confidence as num).toDouble() / 100, 
                                minHeight: 10, 
                                backgroundColor: Colors.grey[300],
                                valueColor: AlwaysStoppedAnimation<Color>(_confColor((confidence as num).toDouble())),
                            ),
                            SizedBox(height: 10),
                            Text("${confidence}% Match", style: TextStyle(fontWeight: FontWeight.bold, fontSize: 18))
                        ],
                    ),
                ),
            ),
            
            // Inline Recommendation Section
            SizedBox(height: 30),
            if (_isLoading) 
               Center(child: CircularProgressIndicator())
            else ...[
                // Basic Care Section (Only if severity is LOW/MODERATE)
                if (_recommendations != null && _recommendations!['basicCare'] != null && (_recommendations!['basicCare'] as List).isNotEmpty) ...[
                    Text("Basic Care Suggestions", style: TextStyle(fontSize: 20, fontWeight: FontWeight.bold, color: Colors.green[800])),
                    SizedBox(height: 10),
                    Card(
                        color: Colors.green[50],
                        child: Padding(
                            padding: EdgeInsets.all(16),
                            child: Column(
                                crossAxisAlignment: CrossAxisAlignment.start,
                                children: [
                                    ...(_recommendations!['basicCare'] as List).map((tip) => 
                                        Padding(
                                            padding: EdgeInsets.only(bottom: 8),
                                            child: Row(
                                                crossAxisAlignment: CrossAxisAlignment.start,
                                                children: [
                                                    Icon(Icons.check_circle, color: Colors.green, size: 20),
                                                    SizedBox(width: 8),
                                                    Expanded(child: Text(tip, style: TextStyle(fontSize: 16)))
                                                ],
                                            )
                                        )
                                    ).toList(),
                                ],
                            ),
                        ),
                    ),
                    SizedBox(height: 20),
                ],

                // Basic Diagnosis & Medicines Section
                Text("Basic Diagnosis & Medicines", style: TextStyle(fontSize: 20, fontWeight: FontWeight.bold, color: Colors.red[800])),
                SizedBox(height: 10),
                if (_recommendations != null && _recommendations!['medicines'] != null && (_recommendations!['medicines'] as List).isNotEmpty)
                    ...(_recommendations!['medicines'] as List).map((med) => Card(
                        elevation: 2,
                        margin: EdgeInsets.only(bottom: 12),
                        shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(10)),
                        child: Padding(
                            padding: EdgeInsets.all(16),
                            child: Column(
                                crossAxisAlignment: CrossAxisAlignment.start,
                                children: [
                                    Row(
                                      children: [
                                        Icon(Icons.medication, color: Colors.red[400]),
                                        SizedBox(width: 10),
                                        Expanded(child: Text(med['name'] ?? '', style: TextStyle(fontSize: 18, fontWeight: FontWeight.bold))),
                                      ],
                                    ),
                                    Divider(),
                                    SizedBox(height: 4),
                                    Text("💊 Dosage: ${med['dosage'] ?? ''}", style: TextStyle(fontSize: 14, fontWeight: FontWeight.w500)),
                                    SizedBox(height: 6),
                                    Text("🕒 How to use: ${med['howToUse'] ?? ''}", style: TextStyle(fontSize: 14)),
                                    SizedBox(height: 6),
                                    Text("⚠️ Precautions: ${med['precautions'] ?? ''}", style: TextStyle(fontSize: 14, color: Colors.red[700])),
                                ],
                            ),
                        ),
                    )).toList()
                else
                    Card(
                        color: Colors.red[50],
                        shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(10)),
                        child: Padding(
                            padding: EdgeInsets.all(16),
                            child: Row(
                                children: [
                                    Icon(Icons.info_outline, color: Colors.red[600]),
                                    SizedBox(width: 10),
                                    Expanded(
                                        child: Text(
                                            "Basic medicine data is not available for this condition. Please consult a doctor.",
                                            style: TextStyle(fontSize: 14, color: Colors.grey[800]),
                                        ),
                                    ),
                                ],
                            ),
                        ),
                    ),
                
                SizedBox(height: 10),
                Container(
                    padding: EdgeInsets.all(12),
                    color: Colors.amber[50],
                    child: Text(
                        "This is a basic medicine suggestion for awareness only. Consult a certified doctor before taking any medication.",
                        style: TextStyle(color: Colors.brown, fontStyle: FontStyle.italic, fontSize: 12),
                        textAlign: TextAlign.center,
                    ),
                ),
                SizedBox(height: 20),

                // Doctor Recommendations
                Text("Recommended Nearby Doctors", style: TextStyle(fontSize: 20, fontWeight: FontWeight.bold, color: Colors.blue[800])),
                SizedBox(height: 10),
                if (_recommendations == null || _recommendations!['doctors'] == null || (_recommendations!['doctors'] as List).isEmpty)
                    Text("No specialist doctors found nearby. Please visit a hospital.")
                else
                    ...(_recommendations!['doctors'] as List).map((doc) => 
                        Card(
                            margin: EdgeInsets.only(bottom: 12),
                            child: ListTile(
                                leading: CircleAvatar(child: Icon(Icons.person), backgroundColor: Colors.blue[100]),
                                title: Text(doc['name'], style: TextStyle(fontWeight: FontWeight.bold)),
                                subtitle: Column(
                                    crossAxisAlignment: CrossAxisAlignment.start,
                                    children: [
                                        Text("${doc['specialization']} • ${doc['clinicName']}"),
                                        Text("${doc['address']}, ${doc['city']}", style: TextStyle(fontSize: 12)),
                                    ],
                                ),
                                trailing: Row(
                                    mainAxisSize: MainAxisSize.min,
                                    children: [
                                        IconButton(
                                            icon: Icon(Icons.call, color: Colors.green),
                                            onPressed: () => _launchDialer(doc['contactNumber'] ?? ''),
                                        ),
                                        IconButton(
                                            icon: Icon(Icons.map, color: Colors.blue),
                                            onPressed: () => _launchMap(doc['location'], "${doc['address']}, ${doc['city']}"),
                                        ),
                                    ],
                                ),
                            ),
                        )
                    ).toList(),
                
                SizedBox(height: 20),
                Text("Suggested Lab Tests", style: TextStyle(fontSize: 20, fontWeight: FontWeight.bold, color: Colors.teal[800])),
                SizedBox(height: 10),
                Card(
                    color: Colors.teal[50],
                    child: ListTile(
                        leading: CircleAvatar(child: Icon(Icons.science, color: Colors.teal), backgroundColor: Colors.white),
                        title: Text("Detailed Diagnostic Tests", style: TextStyle(fontWeight: FontWeight.bold)),
                        subtitle: Text("Get medical tests related to $primary"),
                        trailing: Icon(Icons.chevron_right, color: Colors.teal),
                        onTap: () => Navigator.push(context, MaterialPageRoute(builder: (_) => LabTestHomeScreen(userSymptoms: [primary]))),
                    ),
                ),

                SizedBox(height: 30),
                ElevatedButton(
                    onPressed: () => Navigator.pop(context),
                    child: Text("Done")
                )
            ],
          ],
        ),
      ),
    );
  }
}
