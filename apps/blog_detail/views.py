from django.shortcuts import render,get_object_or_404
from apps.main.models import Post

def blog_detail(request,pk):
    posts = get_object_or_404(Post,pk=pk)
    context={'posts':posts}
    return render(request,'blog_detail.html',context)
