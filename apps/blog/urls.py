# -*- coding: utf-8 -*-
from django.urls import path

from blog.views import ToolsView


# # 新版本django必须指明app_name
app_name = 'blog'


urlpatterns = [
    # 在线工具
    path('tools/', ToolsView.as_view(), name='tools'),
]