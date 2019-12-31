# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class UserProfile(AbstractUser):
    """用户基本信息表"""
    author = models.CharField(max_length=60, verbose_name=u'昵称', default="")  # 跟文章作者关联
    nick_name = models.CharField(max_length=60, verbose_name=u'昵称', default="")
    birthday = models.DateField(verbose_name=u'生日', null=True, blank=True)
    gender = models.CharField(choices=(('male', u'男'), ('female', u'女')), max_length=8, default=u'')
    address = models.CharField(max_length=200, verbose_name=u'地址', default=u'')
    mobile = models.CharField(max_length=11, null=True, blank=True, verbose_name=u'手机号')
    image = models.ImageField(upload_to='images/%Y/%m', default=u'image/default.png', max_length=150, verbose_name=u'头像')

    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name
        # 表名，一般不修改
        db_table = 'user_info'

    def __str__(self):
        return self.username