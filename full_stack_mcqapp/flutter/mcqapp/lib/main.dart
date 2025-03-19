import 'package:flutter/material.dart';
import 'package:mcqapp/api_services/api_services.dart';
import 'package:mcqapp/presentation/button.dart';
import 'package:mcqapp/presentation/home_page.dart';
import 'package:mcqapp/state_management/option_provider.dart';
import 'package:provider/provider.dart';

void main() {
  runApp(MultiProvider(
      providers: [
        ChangeNotifierProvider(create: (context)=>QuestionProvider()),
        ChangeNotifierProvider(create: (context)=>OptionProvider()),
      ],
    child: const MyApp(),
  ));
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Flutter Demo',
      theme: ThemeData(
        colorScheme: ColorScheme.fromSeed(seedColor: Colors.deepPurple),
        useMaterial3: true,
      ),
      home: HomePage(),
      debugShowCheckedModeBanner: false,
    );
  }
}

