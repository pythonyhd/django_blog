# -*- coding: utf-8 -*-
from datetime import datetime

from django.db import models
from django.conf import settings
from ckeditor_uploader.fields import RichTextUploadingField


# Create your models here.
class Tag(models.Model):
    """标签"""
    tag_name = models.CharField(max_length=30, verbose_name=u'标签名称')
    create_date = models.DateTimeField(default=datetime.now, verbose_name='创建时间')

    class Meta:
        verbose_name = u"文章标签"
        verbose_name_plural = verbose_name
        db_table = 'tag'

    def __str__(self):
        return self.tag_name


class Category(models.Model):
    """文章分类"""
    content_type = models.CharField(max_length=30, verbose_name=u'文章类型')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name=u'创建时间')
    last_mod_time = models.DateTimeField(auto_now=True, verbose_name=u'修改时间')

    class Meta:
        ordering = ['content_type']
        verbose_name = u"文章分类"
        verbose_name_plural = verbose_name
        db_table = 'category'

    def __str__(self):
        return self.content_type


# 轮播图
class Carousel(models.Model):
    """轮播图"""
    number = models.IntegerField(help_text='编号决定图片播放的顺序，图片不要多于5张', verbose_name='编号')
    title = models.CharField(max_length=20, blank=True, null=True, help_text='标题可以为空', verbose_name='标题')
    description = models.CharField(max_length=80, verbose_name='描述')
    img_url = models.CharField(max_length=200, verbose_name='图片地址')
    url = models.CharField(max_length=200, default='#', help_text='图片跳转的超链接，默认#表示不跳转', verbose_name='跳转链接')

    class Meta:
        verbose_name = '轮播图'
        verbose_name_plural = verbose_name
        # 编号越小越靠前，添加的时间约晚约靠前
        ordering = ['number', '-id']
        db_table = 'carousel'

    def __str__(self):
        return self.description[:25]


class Article(models.Model):
    """文章"""
    title = models.CharField(max_length=200, verbose_name=u'文章标题')  # 博客标题
    category = models.ForeignKey('Category', verbose_name=u'文章类型', on_delete=models.CASCADE)
    date_time = models.DateField(auto_now_add=True, verbose_name=u'博客日期')  # 博客日期
    # content = models.TextField(blank=True, null=True, verbose_name=u'文章正文')  # 文章正文
    content = RichTextUploadingField(blank=True, null=True, verbose_name=u'文章正文')  # 文章正文，富文本编辑
    digest = models.TextField(blank=True, null=True, verbose_name=u'文章摘要')  # 文章摘要
    author = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=u'作者', on_delete=models.CASCADE)
    view = models.BigIntegerField(default=0, verbose_name=u'阅读数')  # 阅读数
    comment = models.BigIntegerField(default=0, verbose_name=u'评论数')  # 评论数
    picture = models.CharField(max_length=200, verbose_name=u'标题图片地址')  # 标题图片地址
    create_date = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    update_date = models.DateTimeField(verbose_name='修改时间', auto_now=True)

    tag = models.ManyToManyField(Tag)  # 标签

    class Meta:
        verbose_name = '文章内容'
        verbose_name_plural = verbose_name
        ordering = ['-create_date']
        db_table = 'article'

    def __str__(self):
        return self.title


class Comment(models.Model):
    """评论信息"""
    title = models.CharField(max_length=100, verbose_name=u"标题")
    source_id = models.CharField(max_length=25, verbose_name=u'文章id或source名称')
    comment_time = models.DateTimeField(auto_now=True, verbose_name=u'评论时间')
    user_name = models.CharField(max_length=25, verbose_name=u'评论用户')
    url = models.CharField(max_length=100, verbose_name=u'链接')
    comment = models.CharField(max_length=500, verbose_name=u'评论内容')

    class Meta:
        ordering = ['-comment_time']
        verbose_name = u"文章评论"
        verbose_name_plural = verbose_name
        db_table = 'comment'

    def __str__(self):
        return self.title


class FriendLink(models.Model):
    """友情链接"""
    site_name = models.CharField(max_length=50, verbose_name='网站名称')
    description = models.CharField(max_length=100, blank=True, verbose_name='网站描述')
    link = models.URLField(help_text='请填写http或https开头的完整形式地址', verbose_name='友链地址')
    logo = models.URLField(help_text='请填写http或https开头的完整形式地址', blank=True, verbose_name='网站LOGO')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    is_active = models.BooleanField(default=True, verbose_name='是否有效')
    is_show = models.BooleanField(default=False, verbose_name='是否首页展示')

    class Meta:
        verbose_name = '友情链接'
        verbose_name_plural = verbose_name
        ordering = ['create_time']
        db_table = 'friend_link'

    def __str__(self):
        return self.site_name