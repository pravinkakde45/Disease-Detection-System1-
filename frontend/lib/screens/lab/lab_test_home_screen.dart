import 'package:flutter/material.dart';
import '../../models/lab_test.dart';
import '../../services/lab_test_service.dart';
import 'lab_test_detail_screen.dart';
import 'my_lab_tests_screen.dart';

class LabTestHomeScreen extends StatefulWidget {
  final List<String> userSymptoms;

  LabTestHomeScreen({this.userSymptoms = const []});

  @override
  _LabTestHomeScreenState createState() => _LabTestHomeScreenState();
}

class _LabTestHomeScreenState extends State<LabTestHomeScreen> {
  List<LabTest> _allTests = [];
  List<LabTest> _suggestedTests = [];

  @override
  void initState() {
    super.initState();
    _allTests = LabTestService.getAllTests();
    _suggestedTests = LabTestService.getSuggestedTests(widget.userSymptoms);
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Color(0xFFF5F7FA),
      appBar: AppBar(
        title: Text("Lab Tests", style: TextStyle(color: Colors.black87, fontWeight: FontWeight.bold)),
        backgroundColor: Colors.white,
        elevation: 0,
        iconTheme: IconThemeData(color: Colors.black87),
        actions: [
          IconButton(
            icon: Icon(Icons.history_outlined),
            onPressed: () => Navigator.push(context, MaterialPageRoute(builder: (_) => MyLabTestsScreen())),
          ),
        ],
      ),
      body: SingleChildScrollView(
        padding: EdgeInsets.all(16),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            if (_suggestedTests.isNotEmpty) ...[
              Text("Suggested for You", style: TextStyle(fontSize: 18, fontWeight: FontWeight.bold)),
              SizedBox(height: 12),
              Container(
                height: 160,
                child: ListView.builder(
                  scrollDirection: Axis.horizontal,
                  itemCount: _suggestedTests.length,
                  itemBuilder: (context, index) {
                    return _buildTestCard(_suggestedTests[index], isHorizontal: true);
                  },
                ),
              ),
              SizedBox(height: 24),
            ],
            Text("All Available Tests", style: TextStyle(fontSize: 18, fontWeight: FontWeight.bold)),
            SizedBox(height: 12),
            ListView.builder(
              shrinkWrap: true,
              physics: NeverScrollableScrollPhysics(),
              itemCount: _allTests.length,
              itemBuilder: (context, index) {
                return _buildTestCard(_allTests[index]);
              },
            ),
          ],
        ),
      ),
    );
  }

  Widget _buildTestCard(LabTest test, {bool isHorizontal = false}) {
    return InkWell(
      onTap: () => Navigator.push(context, MaterialPageRoute(builder: (_) => LabTestDetailScreen(test: test))),
      child: Container(
        width: isHorizontal ? 240 : double.infinity,
        margin: EdgeInsets.only(right: isHorizontal ? 12 : 0, bottom: isHorizontal ? 0 : 12),
        padding: EdgeInsets.all(16),
        decoration: BoxDecoration(
          color: Colors.white,
          borderRadius: BorderRadius.circular(16),
          boxShadow: [
            BoxShadow(color: Colors.black.withOpacity(0.02), blurRadius: 5, offset: Offset(0, 2)),
          ],
        ),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            Row(
              children: [
                Container(
                  padding: EdgeInsets.all(10),
                  decoration: BoxDecoration(color: Colors.teal.withOpacity(0.1), shape: BoxShape.circle),
                  child: Icon(Icons.science_outlined, color: Colors.teal, size: 24),
                ),
                SizedBox(width: 12),
                Expanded(
                  child: Column(
                    crossAxisAlignment: CrossAxisAlignment.start,
                    children: [
                      Text(test.name, style: TextStyle(fontWeight: FontWeight.bold, fontSize: 16), maxLines: 1, overflow: TextOverflow.ellipsis),
                      Text(test.sampleType, style: TextStyle(color: Colors.grey, fontSize: 12)),
                    ],
                  ),
                ),
              ],
            ),
            SizedBox(height: 12),
            if (!isHorizontal) 
              Text(test.description, style: TextStyle(color: Colors.grey[600], fontSize: 14), maxLines: 2, overflow: TextOverflow.ellipsis),
            SizedBox(height: 12),
            Row(
              mainAxisAlignment: MainAxisAlignment.spaceBetween,
              children: [
                Text("₹${test.price.toInt()}", style: TextStyle(color: Colors.teal, fontWeight: FontWeight.bold, fontSize: 18)),
                Icon(Icons.arrow_forward_ios, size: 16, color: Colors.grey),
              ],
            ),
          ],
        ),
      ),
    );
  }
}
