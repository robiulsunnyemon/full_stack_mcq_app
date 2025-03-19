
import 'dart:convert';
import 'package:flutter/cupertino.dart';
import 'package:http/http.dart' as http;
import 'package:mcqapp/data/model/question_model.dart';

class QuestionProvider with ChangeNotifier {
  List<Question> _questionList = [];
  List<Question> get questionList => _questionList;

  static String baseUrl = 'http://192.168.0.106:8000/api/questions';

  Future<void> getMcq() async {
    try {
      final response = await http.get(Uri.parse(baseUrl), headers: {
        "Content-Type": "application/json",
        "Authorization": "Token 6d3cb5f91c9456f44f69e4682cb3a7e7de1bc59e"
      });

      if (response.statusCode == 200) {
        final jsonData = jsonDecode(response.body);
        print("response_type ${jsonData.runtimeType}");
        List<Question> questions = (jsonDecode(response.body) as List)
            .map((item) => Question.fromJson(item))
            .toList();
        _questionList = questions;  // Assign new list to _questionList
        notifyListeners();  // Notify listeners that data has been updated
      } else {
        print(response.statusCode);
      }
    } catch (e) {
      print(e.toString());
      rethrow;
    }
  }
}
