from django.urls import path
from django.conf.urls import url
from . import view, post
 
urlpatterns = [
    url(r'^$', view.index),
    path('index/', view.index),
    path('login/', view.login),
    path('reg/', view.reg),
    path('logout/', view.logout),  # 注销登录
    path('user/', view.user),  # 个人信息
    path('borrow/', view.borrow),  # 个人信息
    path('return/', view.returnb),  # 个人信息
    path('addbook/', view.addbook),  # 个人信息

    path('post/reg', post.reg), # 注册
    path('post/login', post.login), # 登录
    path('post/addbook', post.addbook), # 添加书籍
]