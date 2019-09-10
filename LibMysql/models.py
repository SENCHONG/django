from django.db import models

# Create your models here.


# 用户表


class User(models.Model):
    username = models.CharField(max_length=12)  # 学号/用户名
    password = models.CharField(max_length=32)  # 密码 md5加密

# 用户注册时间


class RegUser(models.Model):
    username = models.CharField(max_length=12)  # 学号/用户名
    time = models.DateField(auto_now_add=True)  # 注册时间

# 用户权限


class Auth(models.Model):
    username = models.CharField(max_length=12)  # 学号/用户名
    # 权限等级  0新注册用户未开放借书权限 1普通用户  2浏览所有信息  3可编辑信息
    grade = models.IntegerField(1)

# 最大借书数量
class BorrowMaxBookNum(models.Model):
    username = models.CharField(max_length=12)  # 学号/用户名
    num = models.IntegerField(2)   # 最多借阅几本

# 当前借书数量
class BorrowNowBookNum(models.Model):
    username = models.CharField(max_length=12)  # 学号/用户名
    num = models.IntegerField(2)   # 已经借了多少本

# 用户信息表
class UserInfo(models.Model):
    username = models.CharField(max_length=12)  # 学号/用户名
    name = models.CharField(max_length=32)  # 名字
    qq = models.CharField(max_length=12, null=True)  # qq
    weibo = models.CharField(max_length=64, null=True)  # 微博
    mobile = models.CharField(max_length=11, null=True)  # 11位手机号码
    intro = models.CharField(max_length=255, null=True)  # 个人简介

# 书籍表


class Book(models.Model):
    bookname = models.CharField(max_length=60)  # 书名
    bookid = models.CharField(max_length=12)  # 书籍编号
    author = models.CharField(max_length=32)  # 书籍作者 第一作者
    bookinfo = models.CharField(max_length=255)  # 书籍简介
    time = models.DateField(auto_now_add=True)  # 出版时间

# 图书馆书籍入库表


class AddBook(models.Model):
    bookid = models.CharField(max_length=12)  # 书籍编号
    time = models.DateField(auto_now_add=True)  # 添加书籍时间

# 图书馆书籍位置表


class BookPlace(models.Model):
    bookid = models.CharField(max_length=12)  # 书籍编号
    place = models.CharField(max_length=255)  # 书籍位置

# 借阅表


class BorrowBook(models.Model):
    bookid = models.CharField(max_length=12)  # 书籍编号
    username = models.CharField(max_length=12)  # 读者编号
    time = models.DateField(auto_now_add=True)  # 借阅时间


# 还书表
class ReturnBook(models.Model):
    bookid = models.CharField(max_length=12)  # 书籍编号
    username = models.CharField(max_length=12)  # 读者编号
    time = models.DateField(auto_now_add=True)  # 还书时间

# 书本的分类种类
class HaveClassify(models.Model):
    classifyid = models.IntegerField(3)   # 类别
    classifyname = models.CharField(max_length=32)  # 分类名称

# 书本属于哪一类
class BookClassify(models.Model):
    classifyid = models.IntegerField(3)   # 类别
    bookid = models.CharField(max_length=12)  # 书籍编号

# 书本属于什么状态 可借阅 不可借阅
class BookState(models.Model):
    stateid = models.IntegerField(1)   # 状态id
    bookid = models.CharField(max_length=12)  # 书籍编号

# 书本状态的类别
class HaveBookState(models.Model):
    stateid = models.IntegerField(1)   # 书的状态
    statename = models.CharField(max_length=32)  # 状态名称