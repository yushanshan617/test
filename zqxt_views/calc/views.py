# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
# def add(request):
# #     a = request.GET['a']
# #     b = request.GET['b']
# #     c = int(a)+int(b)
# #     return HttpResponse(str(c))
from calc import models
import pymysql


def index(request):
    string = u'你好，Django！'
    return render(request, 'index.html', {'string': string})


def insert(request):
    if request.method == "POST":
        username = request.POST.get("username", None)
        password = request.POST.get("password", None)
        twz = models.message.objects.create(username=username, password=password)
        twz.save()
    return render(request, 'insert.html')


def list(request):
    people_list = models.message.objects.all()
    return render(request, 'home.html', {"people_list": people_list})
