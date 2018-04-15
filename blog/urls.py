# -*- coding: utf-8 -*-
# @File  : urls
# @Author: 
# @Date  : 2018/4/15
# @Desc  :
from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),

]
