#! /usr/bin/env python
# coding=utf-8
# author:"""HTJ"""
# time:2020/2/14
# Zen of Python:
"""
做自己的項目
　　１．強健的肌肉
　　２．一切都變得有序，井井有條
"""

from django.urls import path
from .views import PostList, PostDetail

urlpatterns = [
    path('<int:pk>/',PostDetail.as_view()),
    path('',PostList.as_view()),
]


