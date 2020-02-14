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

from rest_framework import serializers
from .models import Post
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'author', 'title', 'body', 'created_at',)
        model = Post







