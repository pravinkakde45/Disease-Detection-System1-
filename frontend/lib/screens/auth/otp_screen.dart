import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import '../../services/auth_service.dart';
import 'login_screen.dart';

class OtpScreen extends StatefulWidget {
  final String email;
  OtpScreen({required this.email});

  @override
  _OtpScreenState createState() => _OtpScreenState();
}

class _OtpScreenState extends State<OtpScreen> {
  final _otpController = TextEditingController();
  final _newPasswordController = TextEditingController();
  bool _otpVerified = false;
  bool _isLoading = false;

  void _verify() async {
    setState(() => _isLoading = true);
    try {
      await Provider.of<AuthService>(context, listen: false).verifyOtp(widget.email, _otpController.text);
      setState(() => _otpVerified = true);
      ScaffoldMessenger.of(context).showSnackBar(SnackBar(content: Text("OTP Verified! Set new password.")));
    } catch (e) {
      ScaffoldMessenger.of(context).showSnackBar(SnackBar(content: Text(e.toString())));
    } finally {
      if (mounted) setState(() => _isLoading = false);
    }
  }

  void _resetPassword() async {
    setState(() => _isLoading = true);
    try {
      await Provider.of<AuthService>(context, listen: false).resetPassword(
          widget.email, _otpController.text, _newPasswordController.text);
      
      ScaffoldMessenger.of(context).showSnackBar(SnackBar(content: Text("Password Reset Successful! Login now.")));
      Navigator.of(context).pushAndRemoveUntil(MaterialPageRoute(builder: (_) => LoginScreen()), (route) => false);
    } catch (e) {
      ScaffoldMessenger.of(context).showSnackBar(SnackBar(content: Text(e.toString())));
    } finally {
      if (mounted) setState(() => _isLoading = false);
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.white,
      appBar: AppBar(
        title: Text(_otpVerified ? "Reset Password" : "Verify OTP"),
        elevation: 0,
        backgroundColor: Colors.white,
        foregroundColor: Colors.blue[900],
      ),
      resizeToAvoidBottomInset: true,
      body: SafeArea(
        child: SingleChildScrollView(
          physics: BouncingScrollPhysics(),
          padding: EdgeInsets.all(24),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.stretch,
            children: [
              SizedBox(height: 20),
              Icon(
                _otpVerified ? Icons.password_outlined : Icons.mark_email_read_outlined, 
                size: 80, 
                color: Colors.blue
              ),
              SizedBox(height: 30),
              if (!_otpVerified) ...[
                Text(
                  "Verification",
                  textAlign: TextAlign.center,
                  style: TextStyle(fontSize: 24, fontWeight: FontWeight.bold, color: Colors.blue[900]),
                ),
                SizedBox(height: 10),
                Text(
                  "Enter the 6-digit OTP sent to\n${widget.email}",
                  textAlign: TextAlign.center,
                  style: TextStyle(fontSize: 16, color: Colors.grey),
                ),
                SizedBox(height: 40),
                TextField(
                  controller: _otpController,
                  decoration: InputDecoration(
                    labelText: "6-Digit OTP", 
                    border: OutlineInputBorder(borderRadius: BorderRadius.circular(12)),
                    prefixIcon: Icon(Icons.pin_outlined),
                    counterText: "",
                  ),
                  keyboardType: TextInputType.number,
                  maxLength: 6,
                ),
                SizedBox(height: 30),
                ElevatedButton(
                  onPressed: _isLoading ? null : _verify,
                  style: ElevatedButton.styleFrom(
                    padding: EdgeInsets.symmetric(vertical: 16),
                    shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(12)),
                  ),
                  child: _isLoading ? SizedBox(height: 20, width: 20, child: CircularProgressIndicator(color: Colors.white, strokeWidth: 2)) : Text("Verify OTP"),
                ),
              ],
              if (_otpVerified) ...[
                Text(
                  "New Password",
                  textAlign: TextAlign.center,
                  style: TextStyle(fontSize: 24, fontWeight: FontWeight.bold, color: Colors.blue[900]),
                ),
                SizedBox(height: 10),
                Text(
                  "Please create a strong new password",
                  textAlign: TextAlign.center,
                  style: TextStyle(fontSize: 16, color: Colors.grey),
                ),
                SizedBox(height: 40),
                TextField(
                  controller: _newPasswordController,
                  decoration: InputDecoration(
                    labelText: "New Password", 
                    border: OutlineInputBorder(borderRadius: BorderRadius.circular(12)),
                    prefixIcon: Icon(Icons.lock_outline),
                  ),
                  obscureText: true,
                ),
                SizedBox(height: 30),
                ElevatedButton(
                  onPressed: _isLoading ? null : _resetPassword,
                  style: ElevatedButton.styleFrom(
                    padding: EdgeInsets.symmetric(vertical: 16),
                    shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(12)),
                  ),
                  child: _isLoading ? SizedBox(height: 20, width: 20, child: CircularProgressIndicator(color: Colors.white, strokeWidth: 2)) : Text("Reset Password"),
                ),
              ]
            ],
          ),
        ),
      ),
    );
  }
}
