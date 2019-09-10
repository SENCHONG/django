from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, render_to_response, redirect, HttpResponseRedirect
from django.views.decorators import csrf
from LibMysql.models import *
from . import view
import random


def reg(request):

    data = request.POST
    if request.method != 'POST':
        return HttpResponse("<p>请使用POST方式提交</p><a href='/reg'>返回注册</a>")
    # 应该多一步判断数据合法性 此处省略
    # 查询所有用户 判断用户名是否可用
    us = User.objects.filter(username=data.get('username'))
    if us:  # 用户名存在 不可再注册
        return HttpResponse("<p>用户名存在</p><a href='/login'>返回登录</a>")
    else:  # 用户名可用
        print('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
        # user表插入数据
        user = User(username=data.get('username'),
                    password=data.get('password'))
        user.save()

        # 用户信息表插入数据
        userinfo = UserInfo(name=data.get('name'),
                            username=data.get('username'))
        userinfo.save()

        # 新注册用户的权限
        auth = Auth(username=data.get('username'), grade=0)
        auth.save()

        # 记录新注册用户注册时间
        regUser = RegUser(username=data.get('username'))
        regUser.save()

        # 新注册用户最大借阅书籍数量
        borrowMaxBookNum = BorrowMaxBookNum(
            username=data.get('username'), num=5)
        borrowMaxBookNum.save()

        # 新用户默认已经借阅书籍为0
        borrowNowBookNum = BorrowNowBookNum(
            username=data.get('username'), num=0)
        borrowNowBookNum.save()

        return HttpResponse("<p>注册成功</p><a href='/login'>返回登录</a>")


def login(request):
    data = request.POST
    if request.method != 'POST':
        return HttpResponse("<p>请使用POST方式提交</p><a href='/reg'>返回登录</a>")
    # 应该多一步判断数据合法性 此处省略
    us = User.objects.filter(username=data.get(
        'username'), password=data.get('password'))
    if us:
        request.session['login_user_name'] = us[0].username
        return HttpResponseRedirect('/index/')
    else:
        return HttpResponse("<p>密码错误</p><a href='/login'>返回登录</a>")


def addbook(request):
    data = request.POST
    print(data)
    # 生成一个唯一的书籍id
    baseStr = random.sample("ABCDEFGHIJKLMNPQRSTUVWXY3456789", 12)
    bookid = ''.join(baseStr)
    bookidInSql = Book.objects.filter(bookid=bookid)
    whiletimes = 0
    while bookidInSql:
        bookidInSql = Book.objects.filter(bookid=bookid)
        bookid = ''.join(baseStr)
        whiletimes += 1
        if whiletimes > 10:
            return HttpResponse("<p>添加图书失败</p>")
    book = Book(bookname=data.get('bookname'), bookid=bookid,
                author=data.get('author'), bookinfo=data.get('bookinfo'))
    book.save()

    # 添加图书入库记录
    addbook = AddBook(bookid=bookid)
    addbook.save()

    # 添加图书位置信息
    bookPlace = BookPlace(bookid=bookid, place=data.get('place'))
    bookPlace.save()

    # 添加书籍状态信息 可借阅 不可借阅 挂失 等
    bookState = BookState(bookid=bookid, stateid=data.get('bookstate'))
    bookState.save()

    # 书籍类别信息入库 书本的类别 比如科技 杂志 等
    bookClassify = BookClassify(
        classifyid=data.get('bookclassify'), bookid=bookid)
    bookClassify.save()

    return HttpResponseRedirect('/index/')
