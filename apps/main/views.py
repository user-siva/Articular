from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Post

def frontpage(request):
    posts = Post.objects.all()
    context = {
        'posts':posts
    }
    return render(request,'frontpage.html',context)

@login_required
def write_post(request):
    
    return render(request,'write_post.html')

