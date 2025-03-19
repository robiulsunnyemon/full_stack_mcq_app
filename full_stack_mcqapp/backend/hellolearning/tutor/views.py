
from django.shortcuts import render
from rest_framework import status
from rest_framework import viewsets
from .models import Question,Choice,QuestionAnswer,Categoryquestion,CategoryBlog,Blog,UserDetails
from .serializers import QuestionSerializer,ChoiceSerializer,QuestionAnswerSerializer,CategoryquestionSerializer,CategoryBlogSerializer,BlogSerializer,UserDetailsSerializer,RegisterSerializer
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated



from rest_framework.response import Response
from django.db.models import Sum

# Create your views here.

class CategoryquestionViewSet(viewsets.ModelViewSet):
    queryset=Categoryquestion.objects.all()
    serializer_class=CategoryquestionSerializer


class QuestionViewSet(viewsets.ModelViewSet):
    queryset=Question.objects.all()
    serializer_class=QuestionSerializer

    def get_queryset(self):
        queryset=super().get_queryset()
        category_id=self.request.query_params.get(Categoryquestion)
        if category_id:
            queryset=queryset.filter(category_id=category_id)
        return queryset




class ChoiceViewSet(viewsets.ModelViewSet):
    queryset=Choice.objects.all()
    serializer_class=ChoiceSerializer




class QuestionAnswerViewSet(viewsets.ModelViewSet):
    queryset=QuestionAnswer.objects.all()
    serializer_class=QuestionAnswerSerializer


### community

class CategoryBlogViewSet(viewsets.ModelViewSet):
    queryset=CategoryBlog.objects.all()
    serializer_class=CategoryBlogSerializer



class UserDetailsViewSet(viewsets.ModelViewSet):
    queryset=UserDetails.objects.all()
    serializer_class=UserDetailsSerializer




class BlogViewSet(viewsets.ModelViewSet):
    queryset=Blog.objects.all()
    serializer_class=BlogSerializer


## leaderBoard view


@api_view(['GET'])
def student_leaderboard(request):
    leaderboard = (
        QuestionAnswer.objects.values('user')
        .annotate(total_score=Sum('score')) 
        .order_by('-total_score') 
    )
    return Response(leaderboard)



# ✅ ক্যাটাগরি অনুযায়ী ব্লগ ফিল্টার করার জন্য API
@api_view(['GET'])
def blogs_by_category(request, category_id):
    blogs = Blog.objects.filter(category_id=category_id)  # ✅ নির্দিষ্ট ক্যাটাগরি অনুযায়ী ব্লগ ফিল্টার
    serializer = BlogSerializer(blogs, many=True)
    return Response(serializer.data)



# ✅ ক্যাটাগরি অনুযায়ী প্রশ্ন ফিল্টার করার জন্য API
@api_view(['GET'])
def questions_by_category(request, category_id):
    questions = Question.objects.filter(category_id=category_id) # ✅ নির্দিষ্ট ক্যাটাগরির প্রশ্ন ফিল্টার
    serializer = QuestionSerializer(questions, many=True)
    return Response(serializer.data)


# ✅ ক্যাটাগরি অনুযায়ী প্রশ্ন ফিল্টার করার জন্য API
@api_view(['GET'])
def choice_by_question_id(request, question_id):
    option = Choice.objects.filter(question_id=question_id) # ✅ নির্দিষ্ট ক্যাটাগরির প্রশ্ন ফিল্টার
    serializer = ChoiceSerializer(option, many=True)
    return Response(serializer.data)


## user management

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

class LoginView(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data['token'])
        return Response({'token': token.key, 'user_id': token.user_id, 'username': token.user.username})
    


##bulk question
    
class BulkQuestionCreateView(APIView):
    def post(self, request):
        serializer = QuestionSerializer(data=request.data, many=True)
        if serializer.is_valid():
            questions = [Question(**data) for data in serializer.validated_data]
            Question.objects.bulk_create(questions)
            return Response({"message": "Questions created successfully!"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    ##bulk options

 ##bulk question
    
class BulkOptionsCreateView(APIView):
    def post(self, request):
        serializer = ChoiceSerializer(data=request.data, many=True)
        if serializer.is_valid():
            questions = [Choice(**data) for data in serializer.validated_data]
            Choice.objects.bulk_create(questions)
            return Response({"message": "Options created successfully!"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)   