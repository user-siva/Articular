from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User,related_name='user_profile',on_delete=models.CASCADE)
    profile_image = models.ImageField(upload_to='uploads/',default='default.jpg',null=True,blank=True)
    phone = models.IntegerField(null=True,blank=True)
    age = models.IntegerField(null=True,blank=True)
    address  = models.CharField(max_length=300,null=True,blank=True)
    city  = models.CharField(max_length=300,null=True,blank=True)
    country  = models.CharField(max_length=300,null=True,blank=True)
    postal_code  = models.IntegerField(null=True,blank=True)
    about  = models.TextField(max_length=500,null=True,blank=True)
    work  = models.CharField(max_length=300,null=True,blank=True)
    education  = models.CharField(max_length=300,null=True,blank=True)

    def __str__(self):
        return str(self.user.username)