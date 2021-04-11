from django.shortcuts import redirect
from .models import *
from django.http import JsonResponse
import json

def post(request):
    data = json.loads(request.body)
    title = data['title']
    content = data['content']

    if request.method == 'POST' and request.user.is_authenticated:
        if title and content is not None:
            Post.objects.create(user=request.user,title=title,content=content)
            print('posted!')
    
    jsonresponse = {'SUCCESS':True}
    return JsonResponse(jsonresponse)
