# -*- coding: utf-8 -*-
from django.urls import path
from django.views.generic import TemplateView
from django.conf.urls import url, include
import xadmin
from django.conf.urls.static import static

from king_blog import settings


urlpatterns = [
    # 后台管理url
    path('xadmin/', xadmin.site.urls),
    # 后台富文本编辑器路由
    path('ckeditor', include('ckeditor_uploader.urls')),
    # 主页面
    url('^$', TemplateView.as_view(template_name='home/index.html'), name='home'),
    # app用户模块
    url(r'', include('users.urls', namespace='user')),
    # app博客管理
    url(r'^king/', include('blog.urls', namespace='blog')),
    # 验证码
    url(r'^captcha/', include('captcha.urls')),
]
# 富文本编辑配置
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)