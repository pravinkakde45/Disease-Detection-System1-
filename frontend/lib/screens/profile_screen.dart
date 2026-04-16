import 'package:flutter/material.dart';
import '../services/api_service.dart';
import 'package:shared_preferences/shared_preferences.dart';
import 'auth/login_screen.dart';
import 'lab/my_lab_tests_screen.dart';

class ProfileScreen extends StatefulWidget {
  @override
  _ProfileScreenState createState() => _ProfileScreenState();
}

class _ProfileScreenState extends State<ProfileScreen> {
  Map<String, dynamic>? _userProfile;
  bool _isLoading = true;
  String _errorMessage = '';

  @override
  void initState() {
    super.initState();
    _fetchProfile();
  }

  Future<void> _fetchProfile() async {
    try {
      final profile = await ApiService.getUserProfile();
      setState(() {
        _userProfile = profile;
        _isLoading = false;
      });
    } catch (e) {
      setState(() {
        _errorMessage = e.toString();
        _isLoading = false;
      });
    }
  }

  Future<void> _logout() async {
    final prefs = await SharedPreferences.getInstance();
    await prefs.remove('token');
    Navigator.of(context).pushAndRemoveUntil(
      MaterialPageRoute(builder: (_) => LoginScreen()),
      (route) => false,
    );
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Profile'),
        actions: [
          IconButton(icon: Icon(Icons.logout), onPressed: _logout),
        ],
      ),
      body: _isLoading
          ? Center(child: CircularProgressIndicator())
          : _errorMessage.isNotEmpty
              ? Center(child: Text('Error: $_errorMessage'))
              : SingleChildScrollView(
                  padding: EdgeInsets.all(16),
                  child: Column(
                    children: [
                      CircleAvatar(
                        radius: 50,
                        backgroundColor: Colors.blue[100],
                        child: Icon(Icons.person, size: 50, color: Colors.blue),
                      ),
                      SizedBox(height: 16),
                      Text(
                        _userProfile?['name'] ?? 'User',
                        style: TextStyle(fontSize: 24, fontWeight: FontWeight.bold),
                      ),
                      Text(
                        _userProfile?['email'] ?? '',
                        style: TextStyle(color: Colors.grey),
                      ),
                      SizedBox(height: 32),
                      _buildProfileItem(Icons.phone, "Phone", _userProfile?['phone'] ?? 'Not set'),
                      _buildProfileItem(Icons.location_on, "Location", _userProfile?['city'] ?? 'Not set'),
                      _buildProfileItem(Icons.medical_services, "Gender", _userProfile?['gender'] ?? 'Not set'),
                      _buildProfileItem(Icons.cake, "Age", "${_userProfile?['age'] ?? 'Not set'}"),
                      Divider(),
                      ListTile(
                        leading: Icon(Icons.science_outlined, color: Colors.teal),
                        title: Text("My Lab Tests", style: TextStyle(fontWeight: FontWeight.bold)),
                        subtitle: Text("View booking history"),
                        trailing: Icon(Icons.chevron_right),
                        onTap: () => Navigator.push(context, MaterialPageRoute(builder: (_) => MyLabTestsScreen())),
                      ),
                    ],
                  ),
                ),
    );
  }

  Widget _buildProfileItem(IconData icon, String title, String value) {
    return ListTile(
      leading: Icon(icon, color: Colors.blue),
      title: Text(title, style: TextStyle(fontWeight: FontWeight.bold)),
      subtitle: Text(value),
    );
  }
}
