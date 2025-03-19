import 'package:flutter/material.dart';
import 'package:mcqapp/api_services/api_services.dart';
import 'package:mcqapp/data/model/question_model.dart';
import 'package:mcqapp/state_management/option_provider.dart';
import 'package:provider/provider.dart';

class HomePage extends StatelessWidget {
  const HomePage({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('MCQ List')),
      body: Consumer<QuestionProvider>(
        builder: (context, provider, child) {
          if (provider.questionList.isEmpty) {
            provider.getMcq(); // Load data when list is empty
            return Center(child: CircularProgressIndicator());
          } else {
            return ListView.builder(
              itemCount: provider.questionList.length,
              itemBuilder: (context, index) {
                final option = provider.questionList[index].choices;
                int questionIndex = index;
                return Padding(
                  padding: const EdgeInsets.all(8.0),
                  child: Card(
                    color: Colors.red,
                    child: SizedBox(
                      height: 400,
                      width: double.infinity,
                      child: ListTile(
                        title: Text(
                          provider.questionList[index].question,
                          style: TextStyle(
                              fontSize: 25,
                              fontWeight: FontWeight.bold,
                              color: Colors.white),
                        ),
                        subtitle: Padding(
                          padding: const EdgeInsets.only(top: 20),
                          child: SizedBox(
                            height: 300,
                            width: double.infinity,
                            child: ListView.builder(
                              physics: NeverScrollableScrollPhysics(),
                              scrollDirection: Axis.vertical,
                              itemCount: option.length,
                              itemBuilder: (context, index) {
                                return GestureDetector(
                                  onTap: (){
                                    context.read<OptionProvider>().changeOption(optionIndex: index,questionIndex: questionIndex);
                                  },
                                  child: Padding(
                                    padding: const EdgeInsets.all(8.0),
                                    child: Container(
                                      padding: EdgeInsets.symmetric(
                                          horizontal: 20, vertical: 10),
                                      decoration: BoxDecoration(
                                        border: Border.all(color: Colors.white),
                                          color: context.watch<OptionProvider>().isTapped && context.watch<OptionProvider>().questionIndex==questionIndex && context.watch<OptionProvider>().optionIndex==index?Colors.red:Colors.white,
                                          borderRadius:
                                              BorderRadius.circular(10)),
                                      child: Center(
                                        child: Text(
                                          option[index].option,
                                          style: TextStyle(
                                              color: context.watch<OptionProvider>().isTapped && context.watch<OptionProvider>().questionIndex==questionIndex && context.watch<OptionProvider>().optionIndex==index?Colors.white:Colors.black, fontSize: 20),
                                        ),
                                      ),
                                    ),
                                  ),
                                );
                              },
                            ),
                          ),
                        ), // Customize other parts of the UI as per your model
                      ),
                    ),
                  ),
                );
              },
            );
          }
        },
      ),
    );
  }
}
