#! /usr/bin/env python
# -*- coding:utf-8 -*-

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    context          = {}
    context['index'] = '首页'
    return render(request, 'index.html', context)

def about(request):
    context          = {}
    context['index'] = '首页'
    return render(request, 'about.html', context)


def info(request):
    context          = {}
    context['index'] = '首页'
    return render(request, 'info.html', context)


def articlelist(request):
    context          = {}
    context['index'] = '首页'
    return render(request, 'list.html', context)

def share(request):
    context          = {}
    context['index'] = '首页'
    return render(request, 'share.html', context)

def shareinfo(request):
    context          = {}
    context['index'] = '首页'
    return render(request, 'shareinfo.html', context)