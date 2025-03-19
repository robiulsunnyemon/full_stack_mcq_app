class Question {
  final int id;
  final List<Choice> choices;
  final String question;
  final int timeLimit;
  final String createdAt;
  final int user;
  final int category;

  Question({
    required this.id,
    required this.choices,
    required this.question,
    required this.timeLimit,
    required this.createdAt,
    required this.user,
    required this.category,
  });

  factory Question.fromJson(Map<String, dynamic> json) {
    return Question(
      id: json['id'],
      choices: (json['choices'] as List)
          .map((choice) => Choice.fromJson(choice))
          .toList(),
      question: json['question'],
      timeLimit: json['time_limit'],
      createdAt: json['created_at'],
      user: json['user'],
      category: json['category'],
    );
  }

  Map<String, dynamic> toJson() {
    return {
      'id': id,
      'choices': choices.map((choice) => choice.toJson()).toList(),
      'question': question,
      'time_limit': timeLimit,
      'created_at': createdAt,
      'user': user,
      'category': category,
    };
  }
}

class Choice {
  final int id;
  final String option;
  final bool isCorrect;
  final int user;
  final int question;

  Choice({
    required this.id,
    required this.option,
    required this.isCorrect,
    required this.user,
    required this.question,
  });

  factory Choice.fromJson(Map<String, dynamic> json) {
    return Choice(
      id: json['id'],
      option: json['option'],
      isCorrect: json['is_correct'],
      user: json['user'],
      question: json['question'],
    );
  }

  Map<String, dynamic> toJson() {
    return {
      'id': id,
      'option': option,
      'is_correct': isCorrect,
      'user': user,
      'question': question,
    };
  }
}