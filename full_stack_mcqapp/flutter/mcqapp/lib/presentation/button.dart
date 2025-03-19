import 'package:flutter/material.dart';
import 'package:mcqapp/api_services/api_services.dart';
import 'package:mcqapp/presentation/home_page.dart';

class TestButton extends StatelessWidget {
  const TestButton({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Center(
        child: ElevatedButton(
          onPressed: () {
            print("tapped");
            Navigator.push(context, MaterialPageRoute(builder: (context) => HomePage(),));
          },
          child: Text("NEXT"),
        ),
      ),
    );
  }
}
