from django.core.paginator import  Paginator
from django.shortcuts import render
from .models import Artical,Comment
from user.models import UserInfo
def index(request,sort,pindex):
    hotest = Artical.objects.filter().order_by('-click')[0:3]
    if sort == 1:
        article_list = Artical.objects.filter().order_by('-modifydate')
    elif sort == 2:
        article_list = Artical.objects.filter().order_by('-click')
    max_page = article_list.count()/10
    paginator = Paginator(article_list, 10)
    page = paginator.page(int(pindex))
    context = {
        'page':page,
        'paginator':paginator,
        'hotest':hotest,
        'max_page':max_page,
    }
    return render(request,'user_articles/index.html',context)

def detail(request,aid,page):
    article = Artical.objects.get(pk=int(aid))
    author =UserInfo.objects.get(pk=int(article.uid))
    comment_list = Comment.objects.filter(aid=int(aid)).order_by('date')
    max_page = comment_list.count()/10
    paginator = Paginator(comment_list,10)
    context = {
        'article':article,
        'author':author,
        'comment':paginator,
        'page':page,
        'max_page':max_page,
    }
    return render(request,'user_articles/detail.html',context)

