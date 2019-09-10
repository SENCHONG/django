from django.http import HttpResponse
from django.shortcuts import render, render_to_response, redirect, HttpResponseRedirect
from django.views.decorators import csrf
from LibMysql.models import *


def hello1(request):
    context = {}
    context['hello'] = 'Hello1 World!'
    return render(request, 'hello.html', context)


def hello(request):
    return HttpResponse("Hello world ! ")


def login(request):
    if request.session.get('login_user_name') == None:
        return render(request, 'login.html')
    else:
        return HttpResponseRedirect('/index/')

def logout(request):
    request.session.flush()
    return HttpResponseRedirect('/login/')


def reg(request):
    return render(request, 'reg.html')


def index(request):
    if request.session.get('login_user_name'):
        return render(request, 'index.html')
    else:
        return HttpResponseRedirect('/login/')


def user(request):
    if request.session.get('login_user_name'):
        return render(request, 'user.html')
    else:
        return HttpResponseRedirect('/login/')


def borrow(request):
    if request.session.get('login_user_name'):
        return render(request, 'borrow.html')
    else:
        return HttpResponseRedirect('/login/')


def returnb(request):
    if request.session.get('login_user_name'):
        return render(request, 'return.html')
    else:
        return HttpResponseRedirect('/login/')


def addbook(request):
    if request.session.get('login_user_name'):
        classifyRes = HaveClassify.objects.all()
        stateRes = HaveBookState.objects.all()
        context = {}
        context['bookclassifylist'] = classifyRes
        context['bookstatelist'] = stateRes
        return render(request, 'addbook.html', context)
    else:
        return HttpResponseRedirect('/login/')
