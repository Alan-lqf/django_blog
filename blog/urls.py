# -*- coding: utf-8 -*-
# @File  : urls
# @Author: 
# @Date  : 2018/4/15
# @Desc  :


from django.urls import path, re_path
from . import views


app_name = 'blog'
urlpatterns = [
    path('', views.index, name='index'),  # 注意2.0必须在后边添加name  # 2.0必须添加app_name app_name = 'blog'
    # path(r'^post/(?P<pk>[0-9]+)/$', views.detail, name='detail') # ?P<pk>****(?P)为命名捕获，名称为pk
    path('post/<int:pk>/', views.detail, name='detail'),
    path('archives/<int:year>/<int:month>/', views.archives, name='archives'),
    path('category/<int:pk>/', views.category, name='category')


]
