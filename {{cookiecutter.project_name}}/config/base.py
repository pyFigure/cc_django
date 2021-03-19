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

# 允许主机
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
    'django.contrib.sites'
]

INSTALLED_APPS += [
    # 自研应用
    'account.apps.AccountConfig',
    {%- if cookiecutter.use_demo.lower() == 'y' %}
    'demo.apps.DemoConfig',
    {%- endif %}
    {%- if cookiecutter.use_swagger.lower() == 'y' %}
    'drf_yasg2',
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

{%- if cookiecutter.use_shpinx.lower() == 'y' %}
DOCS_ROOT = os.path.join(BASE_DIR, 'docs/build/html/')

# public, login_required, staff, superuser
DOCS_ACCESS = 'public'
{%- endif %}


{%- if cookiecutter.use_celery.lower() == 'y' %}
CELERY_BROKER_URL = env.get('CELERY_BROKER_URL')
{%- endif %}