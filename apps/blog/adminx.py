# -*- coding: utf-8 -*-
import xadmin
from .models import Tag, Category, Carousel, Article, Comment, FriendLink


class TagAdmin(object):
    """
    xadmin注册标签后台管理
    """
    list_display = ['tag_name', 'create_date']
    search_fields = ['tag_name', 'create_date']
    list_filter = ['tag_name', 'create_date']


class CategoryAdmin(object):
    """
    xadmin注册文章分类管理
    """
    list_display = ['content_type', 'created_time', 'last_mod_time']
    search_fields = ['content_type', 'created_time', 'last_mod_time']
    list_filter = ['content_type', 'created_time', 'last_mod_time']


class CarouselAdmin(object):
    """
    xadmin注册轮播图后台管理
    """
    list_display = ['number', 'title', 'description', 'img_url', 'url']
    search_fields = ['number', 'title', 'description', 'img_url', 'url']
    list_filter = ['number', 'title', 'description', 'img_url', 'url']


class ArticleAdmin(object):
    """
    xadmin注册文章后台管理
    """
    list_display = ['title', 'category', 'date_time', 'content', 'digest', 'author', 'view', 'comment', 'picture', 'create_date', 'update_date']
    search_fields = ['title', 'category', 'date_time', 'content', 'digest', 'author', 'view', 'comment', 'picture', 'update_date']
    list_filter = ['title', 'category', 'date_time', 'content', 'digest', 'author', 'view', 'comment', 'picture', 'create_date', 'update_date']


class CommentAdmin(object):
    """
    xadmin注册评论信息后台管理
    """
    list_display = ['title', 'source_id', 'comment_time', 'user_name', 'url', 'comment']
    search_fields = ['title', 'source_id', 'user_name', 'url', 'comment']
    list_filter = ['title', 'source_id', 'comment_time', 'user_name', 'url', 'comment']


class FriendLinkAdmin(object):
    """
    xadmin注册友情链接后台管理
    """
    list_display = ['site_name', 'description', 'link', 'logo', 'create_time', 'is_active', 'is_show']
    search_fields = ['site_name', 'description', 'link', 'logo', 'is_active', 'is_show']
    list_filter = ['site_name', 'description', 'link', 'logo', 'create_time', 'is_active', 'is_show']


xadmin.site.register(Tag, TagAdmin)
xadmin.site.register(Category, CategoryAdmin)
xadmin.site.register(Carousel, CarouselAdmin)
xadmin.site.register(Article, ArticleAdmin)
xadmin.site.register(Comment, CommentAdmin)
xadmin.site.register(FriendLink, FriendLinkAdmin)