from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class QuestionsModel(models.Model):
    question = models.CharField(max_length=200, null=True)
    option_one = models.CharField(max_length=200, null=True)
    option_two = models.CharField(max_length=200, null=True)
    option_three = models.CharField(max_length=200, null=True)
    option_four = models.CharField(max_length=200, null=True)
    answer = models.CharField(max_length=200, null=True)
    def __str__(self):
        return self.question
    
class TodoModel(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    todos = models.CharField(max_length=20,blank=True)
    def __str__(self):
        return f"User {self.user}"

