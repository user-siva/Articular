from django.shortcuts import redirect
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
