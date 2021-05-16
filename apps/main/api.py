from django.shortcuts import get_object_or_404
from .models import *
from django.http import JsonResponse
import json

def post(request):
    data = json.loads(request.body)
    title = data['title']
    content = data['content']
    tags = data['tags']
    print(tags)
    if request.method == 'POST' and request.user.is_authenticated:
        if title and content is not None:
            Post.objects.create(user=request.user,title=title,tags=tags,content=content)
            tag_instance=Post.objects.get(title=title)
            for i in tags:
                tag_instance.tags.add(i)
    
    jsonresponse = {'SUCCESS':True}
    return JsonResponse(jsonresponse)

def reading_list(request):
    data = json.loads(request.body)
    post_id = data['post_id']
    jsonresponse = {'SUCCESS':True}
    if request.method == 'POST' and request.user.is_authenticated:
        posts = get_object_or_404(Post, pk=post_id)
        Reading_list.objects.create(user=request.user,posts=posts)

    return JsonResponse(jsonresponse)