from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('upload/', views.upload, name="upload"),

    path('explore/', views.explore, name="explore"),
    
    path('chat/', views.chat, name="chat"),
    path('about/', views.about, name="about"),
    path('accessible/', views.accessible, name="accessible"),
]
