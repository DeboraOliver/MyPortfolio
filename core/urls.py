from django.contrib import admin
from django.urls import path, include
from . import views

app_name= 'core'

urlpatterns = [
    path('', views.home, name='home'),
    path('data_analyst/', views.job_data, name='data'),
    path('developer/', views.job_developer, name='developer'),
    path('all/', views.job , name='all'),

]