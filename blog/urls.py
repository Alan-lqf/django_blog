# -*- coding: utf-8 -*-
# @File  : urls
# @Author: 
# @Date  : 2018/4/15
# @Desc  :


from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),  # 注意2.0必须在后边添加name  # 2.0必须添加app_name app_name = 'index'

]
