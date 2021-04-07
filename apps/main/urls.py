from django.urls import path
from . import views

urlpatterns = [
	path('',views.frontpage,name='frontpage'),
	path('write_post/',views.write_post,name='write_post'),

]