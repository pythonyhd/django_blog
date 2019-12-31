# -*- coding: utf-8 -*-
import re

from django import forms
from captcha.fields import CaptchaField
from django.core.exceptions import ValidationError
from django.forms import ModelForm

from users.models import UserProfile


# 自定义验证规则
def mobile_validate(value):
    mobile_re = re.compile(r'^(13[0-9]|15[012356789]|17[678]|18[0-9]|14[57]|19[0-9])[0-9]{8}$')
    if not mobile_re.match(value):
        raise ValidationError('手机号码格式错误')


class LoginForm(forms.Form):
    """
    登录验证
    """
    # initial 初始默认值
    username = forms.CharField(required=True, min_length=6, max_length=16, label='用户名')
    password = forms.CharField(required=True, min_length=6, widget=forms.widgets.PasswordInput, label='密码')


class RegisterForm(forms.Form):
    """
    注册验证表单
    """
    username = forms.CharField(required=True, min_length=6, max_length=16, label='用户名', error_messages={'required': "用户名6-16位，必须字母开头"})
    email = forms.EmailField(required=True, min_length=6, max_length=32, label='邮箱', error_messages={'required': "必须填写邮箱"})
    mobile = forms.CharField(required=True, max_length=11, label='手机号', error_messages={'required': "必须填写手机号，最大长度11位"})
    password = forms.CharField(required=True, min_length=6, max_length=16, widget=forms.widgets.PasswordInput, label='密码', error_messages={'required': '密码不能为空', 'min_length': '密码小于6', 'max_length': '密码大于12'})
    repassword = forms.CharField(required=True, min_length=6, max_length=32, widget=forms.widgets.PasswordInput, label='重复密码', error_messages={'required': '密码不能为空', 'min_length': '密码小于6', 'max_length': '密码大于12'})
    captcha = CaptchaField(required=True, error_messages={'invalid': '验证码错误'}, label='验证码')

    # def clean_username(self):
    #     """
    #     用户名校验规则
    #     """
    #     username = self.cleaned_data.get('username', '')
    #     result = re.match(r'[a-zA-Z]\w{5,}', username)
    #     if not result:
    #         raise ValidationError('用户名必须字母开头')
    #     return username


# class RegisterForm(ModelForm):
#     """
#     注册表单验证
#     """
#     # widget 密码不显示，label页面显示的文字
#     repassword = forms.CharField(required=True, min_length=6, max_length=32, error_messages={'required': "必须填写确认密码"}, label='确认密码', widget=forms.widgets.PasswordInput)
#
#     class Meta:
#         # 关联的数据库模型
#         model = UserProfile
#         # 自定义页面显示字段
#         fields = ['username', 'email', 'mobile', 'password']
#         # # 显示所有字段
#         # fields = "__all__"
#         # # 需要排除，不显示的字段
#         # exclude = ['first_name', 'last_name']