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
from rest_framework import permissions
class IsAuthorOrReadOnly(permissions.BasePermission):
    # 我们自己定制的类IsAuthorOrReadOnly是从BasePermission继承
    def has_object_permission(self, request, view, obj):
        # 这里对has_object_permission进行重写
        # 如果是读取的情况下,所以req都满足
        if request.method in permissions.SAFE_METHODS:
            # request.method就是查http的动词
            # 判断其是否在SAFE_METHODS里面,这是个元组包括GET,OPTIONS,and HEAD
            # 即读取相关的
            return True
        # 如果进行写入操作比如修改和删除,只有是作者的req满足
        return obj.author == request.user
# 如果不是读取相关的则比如是写入相关的create,put,del,
# we check if the author of the object in question, which is our blog post obj.author matches the user making the request request.user.

