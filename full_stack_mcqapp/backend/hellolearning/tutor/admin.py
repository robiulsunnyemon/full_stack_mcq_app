from django.contrib import admin
from .models import Question,Choice,QuestionAnswer,Categoryquestion,CategoryBlog,UserDetails,Blog
# Register your models here.

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display=['id','question','category','user']
    search_fields=['question']


@admin.register(Choice)
class ChoiceAdmin(admin.ModelAdmin):
    list_display=['id','option']
    search_fields=['option']


@admin.register(QuestionAnswer)
class QuestionAnswerAdmin(admin.ModelAdmin):
    list_display=['id','user','score']
    search_fields=['score']


@admin.register(Categoryquestion)
class CategoryQuestionAdmin(admin.ModelAdmin):
    list_display=['id']
    search_fields=['id']


@admin.register(CategoryBlog)
class CategoryBlogAdmin(admin.ModelAdmin):
    list_display=['id','category']
    search_fields=['id']


@admin.register(UserDetails)
class UserDetailsAdmin(admin.ModelAdmin):
    list_display=['id','user_id','firstName','lastName','country','phoneNumber']
    search_fields=['id','user_id','firstName']


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display=['id','title','created_at']
    search_fields=['id']