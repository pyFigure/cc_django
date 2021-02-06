"""添加各环境公用配置"""
from utils.env import os, Env
from config.settings import *
from config.common.grappelli.config import *
from config.common.filebrowser import *
from config.common.drf import *
{%- if cookiecutter.use_celery.lower() == 'y' %}
from config.common.celery import *
{%- endif %}
{%- if cookiecutter.use_mdeditor.lower() == 'y' %}
from config.common.mdeditor import *
{%- endif %}
from config.common.logging import *

env = Env()

# 语言/时区
LANGUAGE_CODE = 'zh-hans'
TIME_ZONE = 'Asia/Shanghai'

# todo installed app 中少了  mdeditor

# 允许主机
# todo 生产环境修改为主域名
ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'django.contrib.contenttypes',
    'grappelli.dashboard',
    'grappelli',
    'filebrowser',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

INSTALLED_APPS += [
    # 第三方依赖项目
    {%- if cookiecutter.use_taggit.lower() == 'y' %}
    'taggit',
    'taggit_serializer',
    {%- endif %}
    {%- if cookiecutter.use_mdeditor.lower() == 'y' %}
    'mdeditor',
    {%- endif %}
    'rest_framework',
    'rest_framework_jwt',
    {%- if cookiecutter.use_celery.lower() == 'y' %}
    'django_celery_beat',
    {%- endif %}
    'django.contrib.sites',
    {%- if cookiecutter.use_demo.lower() == 'y' %}
    'mptt',
    {%- endif %}
]

INSTALLED_APPS += [
    # 自研应用
    'account.apps.AccountConfig',
    {%- if cookiecutter.use_demo.lower() == 'y' %}
    'demo.apps.ProjectConfig',
    {%- endif %}
]

SECRET_KEY = env.get('SECRET_KEY')

SITE_ID = 1

# 自定义用户模型
AUTH_USER_MODEL = 'account.User'

# 静态资源路径
STATIC_ROOT = os.path.join(BASE_DIR, 'statics')

# media
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
