from django.shortcuts import get_object_or_404, render,redirect
from .models import UserProfile
from .forms import UserProfileForm
from django.shortcuts import get_object_or_404


def profile_settings(request):	
	profile = UserProfile.objects.get_or_create(user=request.user)
	if request.method == 'POST':
		form =  UserProfileForm(request.POST,request.FILES,instance=request.user.user_profile)
		img_file=form.save(commit=False)
		img_file.save()
	else:
		form = UserProfileForm()
		
	context = {
		'profile':profile,
		'form':form
	}

	return render(request,'profile_settings.html',context)
