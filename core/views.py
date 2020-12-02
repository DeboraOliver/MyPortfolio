from django.shortcuts import render
from .filters import PostFilter
from .models import Post

# Create your views here.
def home(request):
    posts = Post.objects.all()
    stack = request.GET.get('stack')
    if stack:
        posts = Post.objects.filter(stack=stack)
    return render(request, 'home.html', {'posts' : posts})


# def post(request, post_id):
#     post = Post.objects.get(pk=post_id)
#     return render(request, 'post.html', {'post':post})

def post_list(request):
    job_list = PostFilter(request.GET, queryset=Post.objects.all())
    return render(request, 'job.html', {'filter': job_list})