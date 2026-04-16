import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import '../providers/language_provider.dart';
import '../services/localization_service.dart';

class LanguageScreen extends StatelessWidget {
  const LanguageScreen({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    var langProvider = Provider.of<LanguageProvider>(context);
    var lang = AppLocalizations.of(context)!;

    return Scaffold(
      appBar: AppBar(
        title: Text(lang.translate('change_language')),
      ),
      body: ListView(
        children: [
          ListTile(
            title: const Text('English'),
            trailing: langProvider.currentLocale.languageCode == 'en' 
                ? const Icon(Icons.check, color: Colors.blue) 
                : null,
            onTap: () {
              langProvider.changeLanguage(const Locale('en'));
            },
          ),
          const Divider(),
          ListTile(
            title: const Text('हिन्दी (Hindi)'),
            trailing: langProvider.currentLocale.languageCode == 'hi' 
                ? const Icon(Icons.check, color: Colors.blue) 
                : null,
            onTap: () {
              langProvider.changeLanguage(const Locale('hi'));
            },
          ),
        ],
      ),
    );
  }
}
