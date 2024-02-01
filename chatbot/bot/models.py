from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Message(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    text=models.CharField(max_length=150)
    created=models.DateTimeField(auto_now_add=True)
    
class Answer(models.Model):
    message=models.OneToOneField(Message, on_delete=models.CASCADE, related_name='answer', null=True, blank=True)
    text=models.CharField(max_length=500)
    