from django.shortcuts import render,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Q
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

    context = {
        'posts':posts,
        'tag':tag,
    } 
   
    return render(request,'tag_post_list.html',context)

def search(request):
	query = request.GET.get("query")
	
	posts = Post.objects.filter(Q(user__username__icontains=query) | Q(tags__name__icontains=query)).distinct()

	context = {
		'query':query,
		'posts':posts
	}

	return render(request,'search.html',context)