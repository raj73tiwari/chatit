from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):

    def __str__(self):
        return self.user.username
    
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=50,null=True)
    about=models.CharField(max_length=500,null=True)
    phone=models.IntegerField(null=True)
    address=models.CharField(max_length=100,null=True)
    profile_pic=models.ImageField(upload_to="user/profile-pic",default="user/img/defaultpic.png")
