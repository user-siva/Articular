from django.contrib.auth.models import User
from django.shortcuts import redirect, render,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from taggit.models import Tag 
from .models import Post,Reading_list

def frontpage(request):
    posts = Post.objects.all()
    context = {
        'posts':posts
    }
    return render(request,'frontpage.html',context)

@login_required(login_url='account_login')
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

@login_required(login_url='account_login')
def reading_list(request):
    reading_lists = Reading_list.objects.filter(user=request.user)
    print(reading_list)
    context = {
        'reading_lists':reading_lists
    }
    return render(request,'reading_list.html',context)

@login_required(login_url='account_login')   
def delete_reading_list(request,pk):

    Reading_list.objects.get(user=request.user,posts_id=pk).delete()

    return redirect('/reading_list/')

def myposts(request):

    my_posts = Post.objects.filter(user=request.user)

    context = {
    	'posts':my_posts,
    }
    
    return render(request,'MyPosts.html',context)