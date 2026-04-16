import 'package:flutter/material.dart';
import '../../services/api_service.dart';
import 'package:http/http.dart' as http;
import 'dart:convert';
import 'prediction_result_screen.dart';

class SymptomInputScreen extends StatefulWidget {
  @override
  _SymptomInputScreenState createState() => _SymptomInputScreenState();
}

class _SymptomInputScreenState extends State<SymptomInputScreen> {
  // Hardcoded list for demo, ideally fetch from API
  // Using common snake_case codes from our backend
  final List<Map<String, String>> _allSymptoms = [
      {'name': 'Fever', 'code': 'fever'},
      {'name': 'Cough', 'code': 'cough'},
      {'name': 'Chest Pain', 'code': 'chest_pain'},
      {'name': 'Fatigue', 'code': 'fatigue'},
      {'name': 'Headache', 'code': 'headache'},
      {'name': 'Sore Throat', 'code': 'sore_throat'},
      {'name': 'Shortness of Breath', 'code': 'shortness_of_breath'},
      {'name': 'Nausea', 'code': 'nausea'},
      {'name': 'Vomiting', 'code': 'vomiting'},
      {'name': 'Diarrhea', 'code': 'diarrhea'},
      {'name': 'Muscle Pain', 'code': 'muscle_pain'},
      {'name': 'Loss of Smell', 'code': 'loss_of_smell'},
      {'name': 'Rash', 'code': 'rash'},
  ];

  final Set<String> _selectedSymptoms = {};
  bool _isLoading = false;

  void _analyze() async {
    if (_selectedSymptoms.isEmpty) {
        ScaffoldMessenger.of(context).showSnackBar(SnackBar(content: Text("Please select at least one symptom")));
        return;
    }

    setState(() => _isLoading = true);
    
    try {
        final headers = await ApiService.getHeaders();
        final response = await http.post(
            Uri.parse('${ApiService.baseUrl}/disease/predict'),
            headers: headers,
            body: jsonEncode({'symptoms': _selectedSymptoms.toList()})
        );

        if (response.statusCode == 200) {
            final data = jsonDecode(response.body);
            Navigator.push(context, MaterialPageRoute(builder: (_) => PredictionResultScreen(result: data)));
        } else {
            throw Exception('Analysis failed: ${response.statusCode}');
        }

    } catch (e) {
        ScaffoldMessenger.of(context).showSnackBar(SnackBar(content: Text("Error: $e")));
    } finally {
        if (mounted) setState(() => _isLoading = false);
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text("Check Symptoms")),
      body: Column(
        children: [
            Padding(
                padding: EdgeInsets.all(16),
                child: Text("Select all symptoms that apply to you:", style: TextStyle(fontSize: 16)),
            ),
            Expanded(
                child: ListView.builder(
                    itemCount: _allSymptoms.length,
                    itemBuilder: (ctx, i) {
                        final s = _allSymptoms[i];
                        final isSelected = _selectedSymptoms.contains(s['code']);
                        return CheckboxListTile(
                            title: Text(s['name']!),
                            value: isSelected,
                            onChanged: (val) {
                                setState(() {
                                    if (val == true) _selectedSymptoms.add(s['code']!);
                                    else _selectedSymptoms.remove(s['code']!);
                                });
                            }
                        );
                    }
                ),
            ),
            Padding(
                padding: EdgeInsets.all(20),
                child: SizedBox(
                    width: double.infinity,
                    child: ElevatedButton(
                        onPressed: _isLoading ? null : _analyze,
                        style: ElevatedButton.styleFrom(
                          padding: EdgeInsets.symmetric(vertical: 16),
                        ),
                        child: _isLoading ? CircularProgressIndicator(color: Colors.white) : Text("Analyze Symptoms"),
                    )
                )
            )
        ],
      ),
    );
  }
}
