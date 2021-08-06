from django.urls import path
from . import views,api

urlpatterns = [
	path('profile/',views.profile_settings,name='profile_settings'),
	path('api/profile/',api.api_profile,name='profile_api'),
	path('profile_page/<int:pk>/<int:user>',views.profile_page,name='profile_page'),

]