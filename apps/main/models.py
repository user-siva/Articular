from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager

class Post(models.Model):
    user = models.ForeignKey(User,related_name='user',on_delete=models.CASCADE)
    title = models.CharField(max_length=255,blank=True,null=True)
    tags = TaggableManager()
    content = models.TextField(blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
    	ordering = ('-created_at',)
    
    def __str__(self):
        return str(self.id)

class Reading_list(models.Model):
    user = models.ForeignKey(User,related_name='users',on_delete=models.CASCADE,null=True)
    posts = models.ForeignKey(Post,related_name='lists',on_delete=models.CASCADE)

    def __str__(self):
        return str(self.posts.id)+'|'+str(self.user)