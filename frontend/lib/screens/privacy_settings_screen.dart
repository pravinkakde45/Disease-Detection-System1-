import 'package:flutter/material.dart';
import '../services/api_service.dart';
import '../services/localization_service.dart';
import 'language_selection_screen.dart';

class PrivacySettingsScreen extends StatefulWidget {
  const PrivacySettingsScreen({Key? key}) : super(key: key);

  @override
  _PrivacySettingsScreenState createState() => _PrivacySettingsScreenState();
}

class _PrivacySettingsScreenState extends State<PrivacySettingsScreen> {
  bool _aiMemoryEnabled = true;

  Future<void> _deleteHistory() async {
    final confirmed = await showDialog<bool>(
      context: context,
      builder: (context) => AlertDialog(
        title: const Text('Delete History?'),
        content: const Text('This action cannot be undone. All your chat and health records will be permanently deleted.'),
        actions: [
          TextButton(onPressed: () => Navigator.pop(context, false), child: const Text('Cancel')),
          TextButton(
            onPressed: () => Navigator.pop(context, true),
            child: const Text('Delete', style: TextStyle(color: Colors.red)),
          ),
        ],
      ),
    );

    if (confirmed == true) {
      try {
        await ApiService.deleteHistory();
        ScaffoldMessenger.of(context).showSnackBar(const SnackBar(content: Text('History deleted successfully')));
      } catch (e) {
        ScaffoldMessenger.of(context).showSnackBar(SnackBar(content: Text('Failed to delete history: $e')));
      }
    }
  }

  Future<void> _exportData() async {
    try {
      final data = await ApiService.exportData();
      // In a real app, we would write this to a file. For now, we simulate success.
      // print(data); 
      ScaffoldMessenger.of(context).showSnackBar(const SnackBar(content: Text('Data exported to console (Simulation)')));
    } catch (e) {
      ScaffoldMessenger.of(context).showSnackBar(SnackBar(content: Text('Failed to export: $e')));
    }
  }

  Future<void> _toggleAIMemory(bool value) async {
    setState(() => _aiMemoryEnabled = value);
    try {
      await ApiService.updatePreferences({'aiMemory': value});
    } catch (e) {
      // Revert if failed
      setState(() => _aiMemoryEnabled = !value);
      ScaffoldMessenger.of(context).showSnackBar(SnackBar(content: Text('Failed to update preference: $e')));
    }
  }

  @override
  Widget build(BuildContext context) {
    var lang = AppLocalizations.of(context)!;
    
    return Scaffold(
      appBar: AppBar(
        title: Text(lang.translate('privacy_settings')),
      ),
      body: ListView(
        children: [
          SwitchListTile(
            title: const Text('Enable AI Memory'), // TODO: Add to JSON
            subtitle: const Text('Allow AI to use your past health records.'),
            value: _aiMemoryEnabled,
            onChanged: _toggleAIMemory,
          ),

          const Divider(),
           ListTile(
            leading: const Icon(Icons.language),
            title: Text(lang.translate('change_language')),
            subtitle: const Text('English / हिन्दी'),
            onTap: () {
              Navigator.push(context, MaterialPageRoute(builder: (_) => const LanguageScreen()));
            },
          ),
          const Divider(),
          ListTile(
            leading: const Icon(Icons.download),
            title: const Text('Export My Data'),
            subtitle: const Text('Download a copy of your health data.'),
            onTap: _exportData,
          ),
          const Divider(),
          ListTile(
            leading: const Icon(Icons.delete, color: Colors.red),
            title: const Text('Delete All History', style: TextStyle(color: Colors.red)),
            subtitle: const Text('Permanently remove your data from our servers.'),
            onTap: _deleteHistory,
          ),
        ],
      ),
    );
  }
}
