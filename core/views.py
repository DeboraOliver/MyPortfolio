from django.shortcuts import render,  get_object_or_404, redirect
from .filters import PostFilter
from .models import Post

# Create your views here.
def home(request):
    posts = Post.objects.all()
    return render(request, 'home.html', {'posts' : posts})

# def home(request):
#     posts = Post.objects.all()
#     job_list = PostFilter(request.GET, queryset=posts)
#     return render(request, 'job.html', {'filter': job_list})

#Data Analyst projects
def job_data(request):
    post = Post.objects.filter(stack__startswith='Data')
    return render(request, 'layout.html', {'post':post})

#Developer projects
def job_developer(request):
    post = Post.objects.filter(stack__icontains='Developer')
    return render(request, 'layout.html', {'post':post})

#ALL projects
def job(request):
    post = Post.objects.all()
    return render(request, 'layout.html', {'post':post})

# def post_list(request):
#     job_list = PostFilter(request.GET, queryset=Post.objects.all())
#     return render(request, 'job.html', {'filter': job_list})