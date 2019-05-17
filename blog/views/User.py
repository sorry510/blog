#! /usr/bin/env python
# -*- coding:utf-8 -*-

from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    return HttpResponse("Hello world ! ")

def index(request):
    context          = {}
    context['index'] = '首页'
    return render(request, 'index.html', context)