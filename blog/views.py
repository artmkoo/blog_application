from django.shortcuts import render, get_object_or_404
from .models import Post

#ponizej do testowania
# from django.http import HttpResponse


# Create your views here.

def post_list(request):
    posts = Post.published.all()
    return render(request, 'blog/post/list.html', {'Posts': posts}) # tu byl ukryty blad zwiazany z custom managerem "Manager isn’t accessible via <<models>> instances" - {'posts': postrs} bym napisany mala litera

    # return HttpResponse("dupa") # do testowania

def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post, status='poblished', publish__year=year, publish__month=month, publish__day=day) # czy ma byc podwojne podkreslenie ?
    return render(request, 'blog/post/detail.html', {'post': post})