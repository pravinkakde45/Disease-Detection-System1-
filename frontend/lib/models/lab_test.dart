class LabTest {
  final String id;
  final String name;
  final String description;
  final String sampleType;
  final String fastingRequirement;
  final String reportTime;
  final double price;
  final List<String> suggestedForSymptoms;

  LabTest({
    required this.id,
    required this.name,
    required this.description,
    required this.sampleType,
    required this.fastingRequirement,
    required this.reportTime,
    required this.price,
    required this.suggestedForSymptoms,
  });

  Map<String, dynamic> toJson() => {
    'id': id,
    'name': name,
    'description': description,
    'sampleType': sampleType,
    'fastingRequirement': fastingRequirement,
    'reportTime': reportTime,
    'price': price,
    'suggestedForSymptoms': suggestedForSymptoms,
  };

  factory LabTest.fromJson(Map<String, dynamic> json) => LabTest(
    id: json['id'],
    name: json['name'],
    description: json['description'],
    sampleType: json['sampleType'],
    fastingRequirement: json['fastingRequirement'],
    reportTime: json['reportTime'],
    price: json['price'].toDouble(),
    suggestedForSymptoms: List<String>.from(json['suggestedForSymptoms'] ?? []),
  );
}

class LabTestBooking {
  final String id;
  final String testId;
  final String testName;
  final String patientName;
  final String patientAge;
  final String date;
  final String timeSlot;
  final String status;
  final double price;

  LabTestBooking({
    required this.id,
    required this.testId,
    required this.testName,
    required this.patientName,
    required this.patientAge,
    required this.date,
    required this.timeSlot,
    required this.status,
    required this.price,
  });

  Map<String, dynamic> toJson() => {
    'id': id,
    'testId': testId,
    'testName': testName,
    'patientName': patientName,
    'patientAge': patientAge,
    'date': date,
    'timeSlot': timeSlot,
    'status': status,
    'price': price,
  };

  factory LabTestBooking.fromJson(Map<String, dynamic> json) => LabTestBooking(
    id: json['id'],
    testId: json['testId'],
    testName: json['testName'],
    patientName: json['patientName'],
    patientAge: json['patientAge'],
    date: json['date'],
    timeSlot: json['timeSlot'],
    status: json['status'],
    price: json['price'].toDouble(),
  );
}
