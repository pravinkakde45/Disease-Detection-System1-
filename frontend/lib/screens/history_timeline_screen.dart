import 'package:flutter/material.dart';
import 'package:intl/intl.dart';
import '../services/api_service.dart';

class HistoryTimelineScreen extends StatefulWidget {
  const HistoryTimelineScreen({Key? key}) : super(key: key);

  @override
  _HistoryTimelineScreenState createState() => _HistoryTimelineScreenState();
}

class _HistoryTimelineScreenState extends State<HistoryTimelineScreen> {
  late Future<List<dynamic>> _historyFuture;
  late Future<List<dynamic>> _patternsFuture;
  String _filterType = 'All'; // 'All', 'Chat', 'Disease', 'Record'
  final List<String> _filters = ['All', 'Chat', 'Disease', 'Record'];

  @override
  void initState() {
    super.initState();
    _historyFuture = ApiService.getCombinedHistory();
    _patternsFuture = ApiService.getPatterns();
  }

  Future<void> _refresh() async {
    setState(() {
      _historyFuture = ApiService.getCombinedHistory();
      _patternsFuture = ApiService.getPatterns();
    });
  }

  Widget _buildPatternSection(List<dynamic> patterns) {
    if (patterns.isEmpty) return const SizedBox.shrink();

    return Card(
      color: Colors.orange[50],
      margin: const EdgeInsets.all(16),
      child: Padding(
        padding: const EdgeInsets.all(16),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Row(
              children: const [
                Icon(Icons.warning_amber_rounded, color: Colors.orange),
                SizedBox(width: 8),
                Text('Health Insights Detected', style: TextStyle(fontWeight: FontWeight.bold, fontSize: 16)),
              ],
            ),
            const SizedBox(height: 8),
            ...patterns.map((p) => Padding(
              padding: const EdgeInsets.only(bottom: 4),
              child: Text('• ${p['message']}'),
            )).toList(),
          ],
        ),
      ),
    );
  }

  Widget _buildHistoryItem(Map<String, dynamic> item) {
    String type = item['type'] ?? 'unknown';
    // DateFormats format = DateFormats(); // Removed unused class instantiation
    DateTime date = DateTime.parse(item['date']);
    String dateStr = DateFormat('MMM dd, yyyy - hh:mm a').format(date);
    
    // ... rest of item builder code ...
    IconData icon;
    Color color;
    String title;
    String subtitle;

    switch (type) {
      case 'chat':
        icon = Icons.chat;
        color = Colors.blue;
        title = item['sender'] == 'user' ? 'You said' : 'AI Response';
        subtitle = item['message'] ?? '';
        break;
      case 'disease':
        icon = Icons.medication;
        color = Colors.red;
        title = 'Disease Prediction';
        subtitle = '${item['predictedDisease']} (${item['confidenceScore']}%)';
        break;
      case 'health_record':
        icon = Icons.note;
        color = Colors.green;
        title = 'Health Record';
        subtitle = item['diseaseName'] ?? 'Record';
        break;
      default:
        icon = Icons.info;
        color = Colors.grey;
        title = 'Unknown Activity';
        subtitle = '';
    }

    return Card(
      margin: const EdgeInsets.symmetric(horizontal: 16, vertical: 8),
      child: ListTile(
        leading: CircleAvatar(
          backgroundColor: color.withOpacity(0.1),
          child: Icon(icon, color: color),
        ),
        title: Text(title, style: const TextStyle(fontWeight: FontWeight.bold)),
        subtitle: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Text(subtitle),
            const SizedBox(height: 4),
            Text(dateStr, style: const TextStyle(fontSize: 12, color: Colors.grey)),
          ],
        ),
      ),
    );
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Health Timeline'),
      ),
      body: RefreshIndicator(
        onRefresh: _refresh,
        child: ListView(
          children: [
            // Filter Chips
            Container(
              height: 50,
              padding: const EdgeInsets.symmetric(horizontal: 16),
              child: ListView(
                scrollDirection: Axis.horizontal,
                children: _filters.map((filter) {
                  return Padding(
                    padding: const EdgeInsets.only(right: 8.0),
                    child: ChoiceChip(
                      label: Text(filter),
                      selected: _filterType == filter,
                      selectedColor: Colors.blueAccent.withOpacity(0.2),
                      onSelected: (bool selected) {
                        if (selected) {
                          setState(() {
                            _filterType = filter;
                          });
                        }
                      },
                    ),
                  );
                }).toList(),
              ),
            ),
             FutureBuilder<List<dynamic>>(
              future: _patternsFuture,
              builder: (context, snapshot) {
                if (snapshot.hasData) {
                  return _buildPatternSection(snapshot.data!);
                }
                return const SizedBox.shrink();
              },
            ),
            FutureBuilder<List<dynamic>>(
              future: _historyFuture,
              builder: (context, snapshot) {
                if (snapshot.connectionState == ConnectionState.waiting) {
                  return const Center(child: CircularProgressIndicator());
                } else if (snapshot.hasError) {
                  return Center(child: Padding(
                    padding: const EdgeInsets.all(16.0),
                    child: Text('Error: ${snapshot.error}'),
                  ));
                } 

                var history = snapshot.data!;
                
                // Apply Filter
                if (_filterType != 'All') {
                  history = history.where((item) {
                     String type = item['type'] ?? '';
                     if (_filterType == 'Chat') return type == 'chat';
                     if (_filterType == 'Disease') return type == 'disease';
                     if (_filterType == 'Record') return type == 'health_record';
                     return true;
                  }).toList();
                }

                if (history.isEmpty) {
                  return const Center(child: Padding(
                    padding: EdgeInsets.all(16.0),
                    child: Text('No history found matching filter.'),
                  ));
                }

                return ListView.builder(
                  shrinkWrap: true,
                  physics: const NeverScrollableScrollPhysics(),
                  itemCount: history.length,
                  itemBuilder: (context, index) {
                    return _buildHistoryItem(history[index]);
                  },
                );
              },
            ),
          ],
        ),
      ),
    );
  }
}
class DateFormats {
}
