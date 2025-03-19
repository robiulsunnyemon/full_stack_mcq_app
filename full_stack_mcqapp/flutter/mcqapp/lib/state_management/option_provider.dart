import 'package:flutter/widgets.dart';

class OptionProvider extends ChangeNotifier{

  bool _isTapped=false;
  bool get isTapped=>_isTapped;
  int _questionIndex=0;
  int _optionIndex=0;
  int get questionIndex=>_questionIndex;
  int get optionIndex=>_optionIndex;

  changeOption({required int questionIndex, required int optionIndex}){
    if(_isTapped==true){
      print("true");
      if(questionIndex!=_questionIndex){
        if(optionIndex!=_optionIndex){
          _isTapped=true;
          _questionIndex=questionIndex;
          _optionIndex=optionIndex;
          notifyListeners();
        }else{
          _isTapped=false;
          _questionIndex=questionIndex;
          _optionIndex=optionIndex;
          notifyListeners();
        }
      }else{

        _isTapped=false;
        _questionIndex=questionIndex;
        _optionIndex=optionIndex;
        notifyListeners();
      }
    }else{
      _isTapped=true;
      _questionIndex=questionIndex;
      _optionIndex=optionIndex;
      notifyListeners();
    }
  }
}