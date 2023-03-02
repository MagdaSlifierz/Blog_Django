from django.shortcuts import render, get_object_or_404
from .models import Post
from django.http import Http404

# Create your views here.
#Python function to recive a web request and return a web response


def post_list(request): #taks a requesr
    posts = Post.published.all()
    return render(request, 'blog/post/list.html', {'posts' : posts}) #context text

def post_detail(request, id):
    # try:
    #     post = Post.published.get(id=id)
    # except Post.DoesNotExist:
    #     return Http404("Not Post found")
    post = get_object_or_404(Post, id=id, status=Post.Status.PUBLISHED)
    return render(request, 'blog/post/detail.html', {'post':post})

