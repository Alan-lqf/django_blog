# -*- coding: utf-8 -*-
# @File  : urls
# @Author: 
# @Date  : 2018/4/15
# @Desc  :
# from django.urls import path   2.0版没有path呀？？？
from django.contrib import admin
# from django.conf.urls import url
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    # path('admin/', admin.site.urls)
]
