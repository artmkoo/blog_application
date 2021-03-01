from django.shortcuts import render, get_object_or_404
from .models import Post

# from django.http import HttpResponse # do testowania


# Create your views here.

def post_list(request):
    posts = Post.published.all()
    return render(request, 'blog/post/list.html', {'posts': posts}) # tu byl ukryty blad zwiazany z custom managerem "Manager isn’t accessible via <<models>> instances" - {'posts': posts} byl napisany mala litera

    # return HttpResponse("dupa") # do testowania

def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post, status='published', publish__year=year, publish__month=month, publish__day=day) # czy ma byc podwojne podkreslenie ?
    return render(request, 'blog/post/detail.html', {'post': post})