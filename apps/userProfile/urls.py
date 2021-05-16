from django.urls import path
from . import views,api

urlpatterns = [
	path('profile/',views.profile_settings,name='profile_settings'),
	path('api/profile_change/',api.api_profile,name='profile_api'),

]