from django.shortcuts import render,  get_object_or_404, redirect
from .filters import PostFilter
from .models import Post

# Create your views here.
# def home(request):
#     posts = Post.objects.all()
#     stack = request.GET.get('stack')
#     if stack:
#         posts = Post.objects.filter(stack=stack)
#     return render(request, 'home.html', {'posts' : posts})

def home(request):
    posts = Post.objects.all()
    job_list = PostFilter(request.GET, queryset=posts)
    return render(request, 'job.html', {'filter': job_list})


def post(request, stack):
    post = get_object_or_404(Post, stack=stack)
    return render(request, 'post.html', {'post':post})
#
# def post_list(request):
#     job_list = PostFilter(request.GET, queryset=Post.objects.all())
#     return render(request, 'job.html', {'filter': job_list})