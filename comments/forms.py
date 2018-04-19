# -*- coding: utf-8 -*-
# @File  : forms
# @Author: 
# @Date  : 2018/4/19
# @Desc  :
from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'url', 'text']
