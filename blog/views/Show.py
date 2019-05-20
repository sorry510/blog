#! /usr/bin/env python
# -*- coding:utf-8 -*-

from django.http import HttpResponse
from django.shortcuts import render
from sf.models import User, ArticleCategory, Article

def index(request):
    context          = {}
    user = User.objects.all()
    print(user[0].password)
    context['index'] = '首页'
    return render(request, 'index.html', context)

def about(request):
    context          = {}
    context['index'] = '首页'
    return render(request, 'about.html', context)


def info(request, id):
    article = Article.objects.select_related('author').get(id=id)
    # print('id:', article.author)
    return render(request, 'info.html', {'article': article})


def articlelist(request, type=0):
    page = 0
    size = 10
    categoryList = ArticleCategory.objects.filter(is_show=0, parent_id=0).order_by("order")
    if type:
        articleList = Article.objects.filter(is_public=0, is_delete=0, is_verify=1, category=type).order_by("-create_time")[page:size]
    else:
        articleList = Article.objects.filter(is_public=0, is_delete=0, is_verify=1).order_by("-create_time")[page:size]
    return render(request, 'list.html', {'categoryList': categoryList, 'articleList': articleList})

def share(request):
    context          = {}
    context['index'] = '首页'
    return render(request, 'share.html', context)

def shareinfo(request):
    context          = {}
    context['index'] = '首页'
    return render(request, 'shareinfo.html', context)