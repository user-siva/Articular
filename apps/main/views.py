from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from taggit.models import Tag 
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

def tag_post_list(request, tag_slug=None):
    
    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        posts = Post.objects.filter(tags__in=[tag])
    
    
    return render(request,'tag_post_list.html',{'posts':posts,'tag':tag})