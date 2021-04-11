from django.urls import path
from . import views,api

urlpatterns = [
	path('',views.frontpage,name='frontpage'),
	path('write_post/',views.write_post,name='write_post'),
	path('api/post/',api.post,name='post'),

]