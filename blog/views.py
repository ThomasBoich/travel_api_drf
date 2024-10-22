from django.shortcuts import render, redirect
from .models import Post, Comment
from .forms import CommentForm
# Create your views here.

def blog(request):
    return render(request, 'blog.html', {'posts': Post.objects.all(),})

def post(request, post_id):    
    if request.method == 'POST':
        user = request.user
        subscribe = Post.objects.get(id=post_id)
        text = request.POST.get('text')     

        Comment.objects.create(
            user = user,
            text = text,
            post = subscribe
        )

        return redirect('post', post_id=post_id)
    else:
        post = Post.objects.get(id=post_id)
        return render(request, 'post.html', {'post': post, 'comments': Comment.objects.filter(post__id=post.id)})

from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

@login_required
def toggle_like(request, post_id):
    post = Post.objects.get(id=post_id)
    user = request.user

    if user in post.likes.all():
        post.likes.remove(user)
        liked = False
    else:
        post.likes.add(user)
        liked = True

    return JsonResponse({
        'liked': liked,
        'likes_count': post.likes.count(),
    })