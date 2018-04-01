from django.shortcuts import render, render_to_response
from django.http import HttpResponse
import json

from .models import Post, Tag

def index(request):
    content = {
        'posts': Post.objects.all(),
        'recents': Post.objects.order_by('-timestamp')[0:3],
    }

    return render(request, 'blog/index.html', content)

def detail(request, id):
    post = Post.objects.get(id=id)
    
    content = {
        'post' : post,
    }
    return render(request,'blog/detail.html', content)

def search(request, keyword, value):
    if keyword == 'tag':
        res = Post.objects.filter(tags__tag=value).distinct()
    elif keyword == 'author':
        res = Post.objects.filter(author=value)

    content = {
        'posts': res,
    }
    return render(request, 'blog/search.html', content)

# res = Post.objects.filter(tags__tag__in=[tag, 'HTML']).distinct()


def live_search(request):
    if request.method == 'GET':
        search_text = request.GET['search_text']
    else:
        search_text = ''
    return_array = []
    posts = Post.objects.filter(title__contains=search_text)

    if search_text == '':
        posts = Post.objects.all()

    for i in posts:
        return_array.append(i)
    return HttpResponse(json.dumps(return_array))
    
