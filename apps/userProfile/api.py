from .models import UserProfile
from django.http import JsonResponse
from django.shortcuts import redirect

def api_profile(request):
    jsonresponse = {'SUCCESS':True}
    print(request.FILES)
    if request.method == 'POST':
        address = request.POST.get('address')
        age = request.POST.get('age')
        country = request.POST.get('country')
        city = request.POST.get('city')
        postal_code = request.POST.get('postal_code')
        work = request.POST.get('work')
        education = request.POST.get('education')
        about = request.POST.get('about')
        profile = UserProfile.objects.filter(user=request.user)
        profile.update(user=request.user,address=address,age=age,country=country,city=city,postal_code=postal_code,work=work,education=education,about=about)
        

    return redirect('profile_settings')