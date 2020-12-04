from django.contrib import admin
from django.urls import path, include
from . import views

app_name= 'core'

urlpatterns = [
    path('', views.home, name='home'),
    #path('jobs/', views.post_list, name='post'),
    #path('jobs/<int:stack>', views.post, name='post'),
    path('job/<str:stack>/', views.post, name='post'),

]