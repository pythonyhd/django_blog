from django.apps import AppConfig


class BlogConfig(AppConfig):
    name = 'apps.blog'
    verbose_name = u'博客信息'  # 修改app名称为中文显示
