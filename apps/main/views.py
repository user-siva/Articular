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
    if request.method == 'POST' and request.user.is_authenticated:
        title = request.POST.get('title')
        content = request.POST.get('content')
        if title and content is not None:
            Post.objects.create(user=request.user,title=title,content=content)
            return redirect('frontpage')

    context={

    }
    return render(request,'write_post.html',context)