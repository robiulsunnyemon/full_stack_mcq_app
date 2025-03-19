from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Question,Choice,QuestionAnswer,Categoryquestion,CategoryBlog,UserDetails,Blog



class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user





class CategoryquestionSerializer(serializers.ModelSerializer):
    class Meta:
        model=Categoryquestion
        fields = '__all__'




class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model=Choice
        fields = '__all__'



class QuestionSerializer(serializers.ModelSerializer):
    choices=ChoiceSerializer(many=True,read_only=True)

    class Meta:
        model= Question
        fields = '__all__'



class QuestionAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model= QuestionAnswer
        fields = '__all__'



## community

class CategoryBlogSerializer(serializers.ModelSerializer):
    class Meta:
        model= CategoryBlog
        fields = '__all__'


class UserDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model= UserDetails
        fields = '__all__'


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model= Blog
        fields = '__all__'