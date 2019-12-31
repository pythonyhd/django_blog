# -*- coding: utf-8 -*-
from django.urls import path

from users import views
from users.views import RegisterView, LoginView


app_name = 'users'


urlpatterns = [
    # 登录页
    path('login/', LoginView.as_view(), name='login'),
    # 注册页
    path('register/', RegisterView.as_view(), name='register'),
    # 退出登录
    path('logout/', views.user_logout, name='logout'),
]

