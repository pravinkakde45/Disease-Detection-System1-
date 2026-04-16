import 'package:flutter/material.dart';
import 'package:intl/intl.dart';
import 'package:uuid/uuid.dart';
import '../../models/lab_test.dart';
import '../../services/lab_test_service.dart';

class LabTestBookingScreen extends StatefulWidget {
  final LabTest test;

  LabTestBookingScreen({required this.test});

  @override
  _LabTestBookingScreenState createState() => _LabTestBookingScreenState();
}

class _LabTestBookingScreenState extends State<LabTestBookingScreen> {
  final _formKey = GlobalKey<FormState>();
  final _nameController = TextEditingController();
  final _ageController = TextEditingController();
  DateTime _selectedDate = DateTime.now().add(Duration(days: 1));
  String _selectedSlot = "09:00 AM - 10:00 AM";

  final List<String> _slots = [
    "07:00 AM - 08:00 AM",
    "08:00 AM - 09:00 AM",
    "09:00 AM - 10:00 AM",
    "10:00 AM - 11:00 AM",
    "11:00 AM - 12:00 PM",
    "04:00 PM - 05:00 PM",
    "05:00 PM - 06:00 PM",
  ];

  Future<void> _selectDate(BuildContext context) async {
    final DateTime? picked = await showDatePicker(
      context: context,
      initialDate: _selectedDate,
      firstDate: DateTime.now(),
      lastDate: DateTime.now().add(Duration(days: 30)),
    );
    if (picked != null && picked != _selectedDate) {
      setState(() {
        _selectedDate = picked;
      });
    }
  }

  void _confirmBooking() async {
    if (_formKey.currentState!.validate()) {
      final booking = LabTestBooking(
        id: Uuid().v4(),
        testId: widget.test.id,
        testName: widget.test.name,
        patientName: _nameController.text,
        patientAge: _ageController.text,
        date: DateFormat('yyyy-MM-dd').format(_selectedDate),
        timeSlot: _selectedSlot,
        status: 'Scheduled',
        price: widget.test.price,
      );

      await LabTestService.saveBooking(booking);

      showDialog(
        context: context,
        barrierDismissible: false,
        builder: (context) => AlertDialog(
          shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(16)),
          title: Column(
            children: [
              Icon(Icons.check_circle_outline, color: Colors.green, size: 64),
              SizedBox(height: 16),
              Text("Booking Successful"),
            ],
          ),
          content: Text("Your lab test has been scheduled. Our team will contact you for sample collection."),
          actions: [
            TextButton(
              onPressed: () {
                Navigator.pop(context); // Pop dialog
                Navigator.pop(context); // Pop booking screen
                Navigator.pop(context); // Pop detail screen
              },
              child: Text("Done"),
            ),
          ],
        ),
      );
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.white,
      appBar: AppBar(
        title: Text("Book Test", style: TextStyle(color: Colors.black87, fontWeight: FontWeight.bold)),
        backgroundColor: Colors.white,
        elevation: 0,
        iconTheme: IconThemeData(color: Colors.black87),
      ),
      body: SingleChildScrollView(
        padding: EdgeInsets.all(20),
        child: Form(
          key: _formKey,
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              Text("Selected Test: ${widget.test.name}", style: TextStyle(fontSize: 16, fontWeight: FontWeight.bold, color: Colors.teal)),
              SizedBox(height: 24),
              Text("Patient Details", style: TextStyle(fontSize: 18, fontWeight: FontWeight.bold)),
              SizedBox(height: 16),
              TextFormField(
                controller: _nameController,
                decoration: InputDecoration(
                  labelText: "Patient Full Name",
                  border: OutlineInputBorder(borderRadius: BorderRadius.circular(12)),
                  prefixIcon: Icon(Icons.person_outline),
                ),
                validator: (val) => val == null || val.isEmpty ? "Enter name" : null,
              ),
              SizedBox(height: 16),
              TextFormField(
                controller: _ageController,
                keyboardType: TextInputType.number,
                decoration: InputDecoration(
                  labelText: "Age",
                  border: OutlineInputBorder(borderRadius: BorderRadius.circular(12)),
                  prefixIcon: Icon(Icons.cake_outlined),
                ),
                validator: (val) => val == null || val.isEmpty ? "Enter age" : null,
              ),
              SizedBox(height: 32),
              Text("Schedule Selection", style: TextStyle(fontSize: 18, fontWeight: FontWeight.bold)),
              SizedBox(height: 16),
              InkWell(
                onTap: () => _selectDate(context),
                child: Container(
                  padding: EdgeInsets.all(16),
                  decoration: BoxDecoration(
                    border: Border.all(color: Colors.grey.shade400),
                    borderRadius: BorderRadius.circular(12),
                  ),
                  child: Row(
                    mainAxisAlignment: MainAxisAlignment.spaceBetween,
                    children: [
                      Row(
                        children: [
                          Icon(Icons.calendar_month_outlined, color: Colors.teal),
                          SizedBox(width: 12),
                          Text(DateFormat('MMM dd, yyyy').format(_selectedDate), style: TextStyle(fontSize: 16)),
                        ],
                      ),
                      Icon(Icons.edit_outlined, size: 18, color: Colors.grey),
                    ],
                  ),
                ),
              ),
              SizedBox(height: 16),
              DropdownButtonFormField<String>(
                value: _selectedSlot,
                decoration: InputDecoration(
                  labelText: "Time Slot",
                  border: OutlineInputBorder(borderRadius: BorderRadius.circular(12)),
                  prefixIcon: Icon(Icons.access_time),
                ),
                items: _slots.map((s) => DropdownMenuItem(value: s, child: Text(s))).toList(),
                onChanged: (val) {
                  if (val != null) setState(() => _selectedSlot = val);
                },
              ),
              SizedBox(height: 48),
              SizedBox(
                width: double.infinity,
                height: 56,
                child: ElevatedButton(
                  onPressed: _confirmBooking,
                  style: ElevatedButton.styleFrom(
                    backgroundColor: Colors.teal,
                    shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(12)),
                  ),
                  child: Text("Confirm Booking", style: TextStyle(fontSize: 18, fontWeight: FontWeight.bold, color: Colors.white)),
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }
}
