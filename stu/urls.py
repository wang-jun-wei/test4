# coding: utf-8
"""
Created On 2019/3/12 13:25

@author : wjw
"""
from django.conf.urls import url

from stu import views

urlpatterns = [
    url(r'^show/', views.show)
]