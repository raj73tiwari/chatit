from django.db import models
from autoslug import AutoSlugField
from django.contrib.auth.models import User


# Create your models here.

class ChatRoom(models.Model):
    name=models.CharField(max_length=50)
    slug = AutoSlugField(populate_from='name',unique=True)
    desc= models.TextField()

    def __str__(self):
        return self.name
    
class ChatMessage(models.Model):
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    room=models.ForeignKey(ChatRoom,on_delete=models.CASCADE)
    message=models.TextField()
    str_time=models.CharField(max_length=50)
    timestamp=models.DateTimeField(auto_now=True)
