from django.contrib import admin
from . import views
from django.urls import path
urlpatterns = [
    path('index/', views.index, name='index'),
    path('aboutus/', views.aboutus, name='about_us'),
    path('contact/', views.aboutus, name='contact'),

]