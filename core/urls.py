from django.urls import path
from django.contrib.auth import views as auth_views
from .views import (mainPage, aboutPage)

urlpatterns = [
	path('', mainPage, name='main'),
	path('about', aboutPage, name='about')
]