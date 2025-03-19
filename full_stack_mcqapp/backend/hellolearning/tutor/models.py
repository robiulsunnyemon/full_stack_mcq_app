from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now


# Create your models here.


class Categoryquestion(models.Model):
    category=models.CharField(max_length=255,unique=True)
    def __str__(self):
        return self.category
    

class Question(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='question')
    category=models.ForeignKey(Categoryquestion,on_delete=models.CASCADE,related_name='question')
    question=models.CharField(max_length=253)
    time_limit=models.IntegerField(default=30)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question
    

class Choice(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='choice')
    question=models.ForeignKey(Question,related_name='choices',on_delete=models.CASCADE)
    option=models.CharField(max_length=255)
    
    is_correct=models.BooleanField(default=False)

    def __str__(self):
        return self.option
    


class QuestionAnswer(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='qeustionAsnwer')
    question=models.ForeignKey(Question,on_delete=models.CASCADE,related_name='qeustionAsnwer')
    selected_choice=models.ForeignKey(Choice ,on_delete=models.CASCADE)
    is_correct=models.BooleanField(default=False)
    score=models.IntegerField(default=0)


    def save(self,*args,**kwargs):

        if self.selected_choice.is_correct:
            self.is_correct=True
            self.score=1
        else:
            self.score=0
        super().save(*args,**kwargs)
          


## community
        



class CategoryBlog(models.Model):
    user_id=models.ForeignKey(User,on_delete=models.CASCADE,related_name='category_blog')
    category=models.CharField(max_length=255,unique=True)
    def __str__(self):
        return self.category
    


class UserDetails(models.Model):
    user_id=models.ForeignKey(User,on_delete=models.CASCADE,related_name='user_details')
    firstName=models.CharField(max_length=255)
    lastName=models.CharField(max_length=255)
    country=models.CharField(max_length=255, blank=True, null=True)
    phoneNumber=models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.firstName
    

        

class Blog(models.Model):
    user_id=models.ForeignKey(User,on_delete=models.CASCADE,related_name='blog')
    category=models.ForeignKey(CategoryBlog,on_delete=models.CASCADE,related_name='blog')
    user_details_id=models.ForeignKey(UserDetails,on_delete=models.CASCADE,related_name='blog')
    title = models.CharField(max_length=255)
    content = models.TextField()
    image = models.ImageField(upload_to='blog_images/', blank=True, null=True)  
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
