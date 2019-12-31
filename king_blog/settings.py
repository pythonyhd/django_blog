# -*- coding: utf-8 -*-
import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))
sys.path.insert(0, os.path.join(BASE_DIR, 'extra_apps'))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'l==+c9e&r^#@%^y1=l9m7ki!lyc^vcdefnyu#(k7$o21&j%%h$'

DEBUG = True

ALLOWED_HOSTS = []


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog',
    'users',

    # 后台管理修改成xadmin
    'xadmin',
    'crispy_forms',
    'import_export',

    # 富文本编辑器
    'ckeditor',
    # 文件上传
    'ckeditor_uploader',

    # 登录注册简单验证码库
    'captcha',

    # 分页
    # 'pure_pagination',
]

AUTH_USER_MODEL = 'users.UserProfile'  # Django使用两个app创建外键时对‘auth.User’产生了多对多的依赖所以报错
# 自定义后台登录认证
AUTHENTICATION_BACKENDS = (
    'users.views.CustomBackends',
)

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'king_blog.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',

                # 对html里面的图片地址做注册，防止HTML页面找不到media，2.2版本放到template目录
                # 'django.template.context_processors.media',
            ],
        },
    },
]

WSGI_APPLICATION = 'king_blog.wsgi.application'


# Database

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'blog',
        'USER': 'root',
        'PASSWORD': '123456',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        # 'OPTIONS': {
        #     "init_command": "SET foreign_key_checks = 0;",
        # }
    }
}


AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# LANGUAGE_CODE = 'zh-Hans'
LANGUAGE_CODE = 'zh-hans'  # 使用ckeditor的时候，大写后台显示繁体，修改小写之后恢复简体

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False  # 跟本地时间同步，否则会应用UTC时间


# Static files (CSS, JavaScript, Images)

# 放静态文件，css，JS，等等
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]

# 图片上传路径，跟前端页面配合使用，上传文件目录
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# 富文本编辑器文件上传路径
CKEDITOR_UPLOAD_PATH = 'uploads/'
CKEDITOR_JQUERY_URL = 'https://apps.bdimg.com/libs/jquery/2.1.4/jquery.min.js'
CKEDITOR_IMAGE_BACKEND = 'pillow'
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'full',
        # 添加按钮在这里
        'toolbar_Custom': [
            ['Blockquote', 'CodeSnippet'],

        ],
    },
}