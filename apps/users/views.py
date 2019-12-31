# -*- coding: utf-8 -*-
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.hashers import make_password
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

from django.views.generic import View

from users.forms import LoginForm, RegisterForm
from users.models import UserProfile


# 重写认证
class CustomBackends(ModelBackend):
    """
    用户认证
    """
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            # 可以同时使用username，email，mobile登录
            user = UserProfile.objects.get(Q(username=username)|Q(email=username)|Q(mobile=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None


# 用户登录
class LoginView(View):
    """
    用户登录模块，只处理get跟post请求
    """

    def get(self, request):
        """
        自动调用get请求
        """
        login_form = LoginForm()
        return render(request, 'user/login.html', context={'login_form': login_form})

    def post(self, request):
        """
        自动调用post
        """
        login_form = LoginForm(request.POST)
        # 检验是否验证成功，不成功会有errors信息
        if login_form.is_valid():
            # 需要跟html页面里面得form表单中的name相对应，html定义的是username就获取username
            user_name = login_form.cleaned_data.get('username', '')
            pass_word = login_form.cleaned_data.get('password', '')
            user = authenticate(username=user_name, password=pass_word)
            if user is not None and user.is_active:
                # 判断用户名密码是否有效
                login(request, user)
                return redirect('home')
            else:
                return render(request, 'user/login.html', locals())
        else:
            login_form = LoginForm()
            return render(request, 'user/login.html', locals())


# 用户注册
class RegisterView(View):
    """
    用户注册模块，只处理get跟post请求
    """
    def get(self, request):
        register_form = RegisterForm()
        return render(request, 'user/register.html', context={'register_form': register_form})

    def post(self, request):
        # 接收前端表单填写的数据
        register_form = RegisterForm(request.POST)
        # 数据校验，返回布尔
        if register_form.is_valid():
            username = register_form.cleaned_data.get('username', '')
            filter_result = UserProfile.objects.filter(username=username)
            if len(filter_result) > 0:
                return render(request, 'user/register.html', context={'error': '用户名已存在'})
            else:
                email = register_form.cleaned_data.get('email', '')
                mobile = register_form.cleaned_data.get('mobile', '')
                password1 = register_form.cleaned_data.get('password1', '')
                password2 = register_form.cleaned_data.get('password2', '')
                errors = []
                if (password2 != password1):
                    errors.append("两次输入的密码不一致!")
                    return render(request, 'user/register.html', context={'error': errors})
                password2 = password1
                user_profile = UserProfile()
                user_profile.username = username
                user_profile.email = email
                user_profile.mobile = mobile
                # 加密后的密码保存到数据库
                user_profile.password = make_password(password2)
                # 校验成功保存到数据库
                user_profile.save()
                # 注册成功跳转到登录页面
                return redirect('users:login')
        else:
            register_form = RegisterForm()
            # Python的内建函数locals()。它返回的字典对所有局部变量的名称与值进行映射
            return render(request, 'user/register.html', locals())


# 用户注销
def user_logout(request):
    logout(request)
    return redirect('home')