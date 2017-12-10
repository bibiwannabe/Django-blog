from django.shortcuts import render
from django.http import HttpResponse
from blog import models
import logging


def index(request):
    art = models.Articles.objects.all()
    return render(request, 'blog/index.html', {'arts': art})


def article_page(request, article_id):
    con = models.Articles.objects.get(pk=article_id)
    return render(request, 'blog/article_page.html', {'arts': con})


def edit_page(request, article_id):
    if str(article_id) == '0':
        return render(request, 'blog/edit_page.html')
    con = models.Articles.objects.get(pk=article_id)
    return render(request, 'blog/edit_page.html', {'arts': con})


def edit_action(request):
    title = request.POST.get('title', 'title')
    cont = request.POST.get('cont', 'content')
    arts_id = request.POST.get('arts_id', '0')
    if arts_id == '0':
        models.Articles.objects.create(title=title, cont=cont)
        art = models.Articles.objects.all()
        return render(request, 'blog/index.html', {'arts': art})
    else:
        con = models.Articles.objects.get(pk=arts_id)
        con.title = title
        con.cont = cont
        con.save()
        return render(request, 'blog/article_page.html', {'arts': con})
