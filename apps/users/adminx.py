# -*- coding: utf-8 -*-
import xadmin
from xadmin import views


class BaseSetting(object):
    enable_themes = True  # 启用主题
    use_bootswatch = True


class GlobalSettings(object):
    site_title = 'King-life博客管理后台'  # 后台标题名称
    site_footer = '华氏集团'  # 底部显示名称
    menu_style = 'accordion'  # 把app进行收缩，点击可以展开


xadmin.site.register(views.BaseAdminView, BaseSetting)  # 启用主题
xadmin.site.register(views.CommAdminView, GlobalSettings)  # 修改头跟底
