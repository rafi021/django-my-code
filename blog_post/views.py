from django.shortcuts import render
from .models import Post
# Create your views here.
def home(request):
    admin_info = {
        'name': "Mahmud Ibrahim",
    }
    all_post = Post.objects.all()
    context = {
        'all_post_list': all_post,
    }
    return render(request, 'index.html', context)

def post_list(request):
    post_list = Post.objects.all()
    context = {
        'post_list': post_list,
    }
    return render(request, 'post_list.html', context)

def single_post(request, post_id):
    post = Post.objects.get(pk=post_id)
    context = {
        'post': post
    }
    return render(request, 'single_post.html', context)


