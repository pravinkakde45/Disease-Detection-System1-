import 'package:flutter/material.dart';
import '../../services/auth_service.dart';
import 'package:provider/provider.dart';
import '../auth/login_screen.dart';
import 'symptom_input_screen.dart';
import '../history_timeline_screen.dart';
import '../smart_chat_screen.dart';
import '../privacy_settings_screen.dart';
import '../doctor_recommendation_screen.dart';
import '../../services/localization_service.dart';
import '../appointment_screen.dart';
import '../profile_screen.dart';

import 'package:shared_preferences/shared_preferences.dart';
import '../lab/lab_test_home_screen.dart';

class HomeScreen extends StatefulWidget {
  @override
  _HomeScreenState createState() => _HomeScreenState();
}

class _HomeScreenState extends State<HomeScreen> {
  // Medical Color Palette
  final Color primaryColor = Color(0xFF1E88E5); // Soft Blue
  final Color secondaryColor = Color(0xFF43A047); // Soft Green
  final Color backgroundColor = Color(0xFFF5F7FA); // Light Grey/White
  final Color cardColor = Colors.white;

  String _userName = "User";

  @override
  void initState() {
    super.initState();
    _loadUserName();
  }

  void _loadUserName() async {
    final prefs = await SharedPreferences.getInstance();
    setState(() {
      _userName = prefs.getString('userName') ?? "User";
    });
  }

  @override
  Widget build(BuildContext context) {
    var lang = AppLocalizations.of(context)!;
    
    return Scaffold(
      backgroundColor: backgroundColor,
      appBar: AppBar(
        elevation: 0,
        backgroundColor: Colors.white,
        title: Row(
          children: [
            Image.asset('assets/logo.png', height: 32),
            SizedBox(width: 8),
            Text(lang.translate('app_title'), style: TextStyle(color: Colors.black87, fontWeight: FontWeight.bold)),
          ],
        ),
        actions: [
          IconButton(icon: Icon(Icons.notifications_none, color: Colors.grey), onPressed: () {}),
          IconButton(
            icon: Icon(Icons.exit_to_app, color: Colors.grey), 
            onPressed: () {
               // Implement logout - currently just a placeholder
               Navigator.pushReplacement(context, MaterialPageRoute(builder: (_) => LoginScreen()));
            }
          ),
        ],
      ),
      body: SingleChildScrollView(
        physics: BouncingScrollPhysics(),
        padding: EdgeInsets.all(16),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.stretch,
          children: [
            _buildWelcomeSection(lang),
            SizedBox(height: 20),
            _buildSearchBar(),
            SizedBox(height: 24),
            _buildSectionTitle("Health Services"),
            SizedBox(height: 12),
            _buildServicesGrid(context, lang),
            SizedBox(height: 24),
            _buildSectionTitle("Health Tips"),
            SizedBox(height: 12),
            _buildHealthTips(),
             SizedBox(height: 24),
            _buildSectionTitle("Your Activity"),
            SizedBox(height: 12),
            _buildActivityCard(context, lang),
            SizedBox(height: 40),
            _buildFooter(),
            SizedBox(height: 20),
          ],
        ),
      ),
      bottomNavigationBar: BottomNavigationBar(
        selectedItemColor: primaryColor,
        unselectedItemColor: Colors.grey,
        showUnselectedLabels: true,
        type: BottomNavigationBarType.fixed,
        items: [
           BottomNavigationBarItem(icon: Icon(Icons.home), label: "Home"),
           BottomNavigationBarItem(icon: Icon(Icons.calendar_today), label: "Appointments"),
           BottomNavigationBarItem(icon: Icon(Icons.chat_bubble_outline), label: "Chat"),
           BottomNavigationBarItem(icon: Icon(Icons.person_outline), label: "Profile"),
        ],
        onTap: (index) {
          if (index == 1) {
             Navigator.push(context, MaterialPageRoute(builder: (_) => AppointmentScreen()));
          } else if (index == 2) {
             Navigator.push(context, MaterialPageRoute(builder: (_) => SmartChatScreen()));
          } else if (index == 3) {
             Navigator.push(context, MaterialPageRoute(builder: (_) => ProfileScreen()));
          }
        },
      ),
    );
  }

  Widget _buildWelcomeSection(AppLocalizations lang) {
    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        Text(
          "${lang.translate('home_welcome')}, $_userName",
          style: TextStyle(fontSize: 22, fontWeight: FontWeight.bold, color: Colors.black87),
        ),
        SizedBox(height: 4),
        Text(
          "How are you feeling today?",
          style: TextStyle(fontSize: 14, color: Colors.grey[600]),
        ),
      ],
    );
  }

  Widget _buildSearchBar() {
    return Container(
      padding: EdgeInsets.symmetric(horizontal: 16),
      decoration: BoxDecoration(
        color: Colors.white,
        borderRadius: BorderRadius.circular(12),
        boxShadow: [
          BoxShadow(color: Colors.black.withOpacity(0.05), blurRadius: 10, offset: Offset(0, 4)),
        ],
      ),
      child: TextField(
        decoration: InputDecoration(
          border: InputBorder.none,
          icon: Icon(Icons.search, color: Colors.grey),
          hintText: "Search symptoms, doctors...",
          hintStyle: TextStyle(color: Colors.grey[400]),
        ),
      ),
    );
  }

  Widget _buildSectionTitle(String title) {
    return Text(
      title,
      style: TextStyle(fontSize: 18, fontWeight: FontWeight.bold, color: Colors.black87),
    );
  }

  Widget _buildServicesGrid(BuildContext context, AppLocalizations lang) {
    return GridView.count(
      shrinkWrap: true,
      crossAxisCount: 3,
      crossAxisSpacing: 12,
      mainAxisSpacing: 12,
      childAspectRatio: 0.9,
      physics: NeverScrollableScrollPhysics(),
      children: [
        _buildServiceCard(
          context,
          lang.translate('check_symptoms'),
          Icons.coronavirus_outlined,
          Colors.orange.shade100,
          Colors.orange,
          () => Navigator.push(context, MaterialPageRoute(builder: (_) => SymptomInputScreen())),
        ),
        _buildServiceCard(
          context,
          lang.translate('medical_chat'),
          Icons.medical_services_outlined,
          Colors.blue.shade100,
          Colors.blue,
          () => Navigator.push(context, MaterialPageRoute(builder: (_) => SmartChatScreen())),
        ),
        _buildServiceCard(
          context,
          lang.translate('find_specialist'),
          Icons.person_search_outlined,
          Colors.green.shade100,
          Colors.green,
          () => Navigator.push(context, MaterialPageRoute(builder: (_) => DoctorRecommendationScreen(predictedDisease: 'General'))),
        ),
         _buildServiceCard(
          context,
          lang.translate('health_history'),
          Icons.history,
          Colors.purple.shade100,
          Colors.purple,
          () => Navigator.push(context, MaterialPageRoute(builder: (_) => HistoryTimelineScreen())),
        ),
         _buildServiceCard(
          context,
          "Lab Tests",
          Icons.science_outlined,
          Colors.teal.shade100,
          Colors.teal,
          () => Navigator.push(context, MaterialPageRoute(builder: (_) => LabTestHomeScreen())),
        ),
         _buildServiceCard(
          context,
          lang.translate('privacy_settings'),
          Icons.settings_outlined,
          Colors.grey.shade200,
          Colors.grey,
          () => Navigator.push(context, MaterialPageRoute(builder: (_) => PrivacySettingsScreen())),
        ),
      ],
    );
  }

  Widget _buildServiceCard(BuildContext context, String title, IconData icon, Color bgColor, Color iconColor, VoidCallback onTap) {
    return InkWell(
      onTap: onTap,
      child: Container(
        decoration: BoxDecoration(
          color: Colors.white,
          borderRadius: BorderRadius.circular(16),
          boxShadow: [
             BoxShadow(color: Colors.black.withOpacity(0.02), blurRadius: 5, offset: Offset(0, 2)),
          ],
        ),
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            Container(
              padding: EdgeInsets.all(12),
              decoration: BoxDecoration(
                color: bgColor,
                shape: BoxShape.circle,
              ),
              child: Icon(icon, color: iconColor, size: 28),
            ),
            SizedBox(height: 12),
            Text(
              title,
              textAlign: TextAlign.center,
              style: TextStyle(fontSize: 12, fontWeight: FontWeight.w600, color: Colors.grey[800]),
              maxLines: 2,
              overflow: TextOverflow.ellipsis,
            ),
          ],
        ),
      ),
    );
  }

   Widget _buildHealthTips() {
    return Container(
      height: 140,
      child: ListView(
        scrollDirection: Axis.horizontal,
        physics: BouncingScrollPhysics(),
        children: [
          _buildTipCard("Summer Health", "Stay hydrated and wear sunscreen.", Colors.amber.shade100, Colors.amber),
          SizedBox(width: 12),
          _buildTipCard("Heart Health", "30 mins of cardio daily keeps the heart safe.", Colors.red.shade100, Colors.red),
          SizedBox(width: 12),
          _buildTipCard("Mental Peace", "Meditation helps reduce stress.", Colors.blue.shade100, Colors.blue),
        ],
      ),
    );
  }

  Widget _buildTipCard(String title, String subtitle, Color bgColor, Color accentColor) {
    return Container(
      width: 240,
      padding: EdgeInsets.all(16),
      decoration: BoxDecoration(
        color: bgColor,
        borderRadius: BorderRadius.circular(16),
      ),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        mainAxisAlignment: MainAxisAlignment.center,
        children: [
          Container(
             padding: EdgeInsets.symmetric(horizontal: 8, vertical: 4),
             decoration: BoxDecoration(
               color: Colors.white.withOpacity(0.6),
               borderRadius: BorderRadius.circular(8),
             ),
             child: Text(title, style: TextStyle(color: accentColor, fontWeight: FontWeight.bold, fontSize: 12)),
          ),
          SizedBox(height: 8),
          Text(subtitle, style: TextStyle(color: Colors.black87, fontWeight: FontWeight.w600, fontSize: 14), maxLines: 3),
        ],
      ),
    );
  }

   Widget _buildActivityCard(BuildContext context, AppLocalizations lang) {
     return Container(
       padding: EdgeInsets.all(16),
       decoration: BoxDecoration(
         color: Colors.white,
         borderRadius: BorderRadius.circular(16),
         boxShadow: [
             BoxShadow(color: Colors.black.withOpacity(0.02), blurRadius: 5, offset: Offset(0, 2)),
         ],
       ),
       child: Row(
         children: [
           Container(
             padding: EdgeInsets.all(12),
             decoration: BoxDecoration(
               color: Colors.blue.withOpacity(0.1),
               borderRadius: BorderRadius.circular(12),
             ),
             child: Icon(Icons.access_time, color: Colors.blue),
           ),
           SizedBox(width: 16),
           Expanded(
             child: Column(
               crossAxisAlignment: CrossAxisAlignment.start,
               children: [
                 Text("Next Medication", style: TextStyle(fontWeight: FontWeight.bold, fontSize: 16)),
                 Text("Paracetamol - 2:00 PM", style: TextStyle(color: Colors.grey[600], fontSize: 14)),
               ],
             ),
           ),
           Icon(Icons.chevron_right, color: Colors.grey),
         ],
       ),
     );
  }

  Widget _buildFooter() {
    return Column(
      children: [
        Divider(color: Colors.grey[300]),
        SizedBox(height: 16),
        Text(
          "© 2026 Pravin Kakde. All Rights Reserved.",
          style: TextStyle(color: Colors.grey[600], fontSize: 12, fontWeight: FontWeight.bold),
        ),
        SizedBox(height: 4),
        Row(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            InkWell(
              onTap: () {},
              child: Text(
                "Privacy Policy",
                style: TextStyle(color: primaryColor, fontSize: 12, decoration: TextDecoration.underline),
              ),
            ),
            SizedBox(width: 16),
            InkWell(
              onTap: () {},
              child: Text(
                "Terms of Service",
                style: TextStyle(color: primaryColor, fontSize: 12, decoration: TextDecoration.underline),
              ),
            ),
          ],
        ),
        SizedBox(height: 8),
        Text(
          "This app is not a replacement for professional medical advice.",
          style: TextStyle(color: Colors.grey[500], fontSize: 10, fontStyle: FontStyle.italic),
        ),
      ],
    );
  }
}
