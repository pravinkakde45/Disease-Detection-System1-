import 'dart:io';

class ApiConfig {
  static String get _serverIp {
    if (Platform.isWindows) {
      return '127.0.0.1';
    } else if (Platform.isAndroid) {
      return '10.219.182.120';
    }
    return '127.0.0.1'; // Default fallback
  }

  static String get baseUrl => 'http://$_serverIp:5000/api';
  
  static const Duration timeoutDuration = Duration(seconds: 15);
}
