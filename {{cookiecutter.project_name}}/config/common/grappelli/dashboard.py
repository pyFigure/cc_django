"""
This file was generated with the customdashboard management command and
contains the class for the main dashboard.

To activate your index dashboard add the following to your settings.py::
    GRAPPELLI_INDEX_DASHBOARD = 'config.grappelli.dashboard.CustomIndexDashboard'
"""

from django.utils.translation import gettext_lazy as _

from grappelli.dashboard import modules, Dashboard
from grappelli.dashboard.utils import get_admin_site_name


class CustomIndexDashboard(Dashboard):
    """
    Custom index dashboard for www.
    """

    def init_with_context(self, context):
        site_name = get_admin_site_name(context)

        # 第一列: 站点模型
        self.children.append(modules.AppList(
            _('用户自定义模型'),
            collapsible=True,
            column=1,
            css_classes=('collapse open',),
            # 此处添加模型列表
            models=[
                'account.models.User',
            ]
        ))

        # 第二列: 管理员权限
        self.children.append(modules.ModelList(
            _('管理员权限'),
            column=2,
            collapsible=True,
            models=('django.contrib.*',),
        ))

        self.children.append(modules.ModelList(
            _('周期性任务'),
            collapsible=True,
            column=2,
            css_classes=('collapse open',),
            models=['django_celery_beat.models.*']
        ))

        # 第三列: 第三方链接
        self.children.append(modules.LinkList(
            _('媒体文件管理'),
            column=3,
            children=[
                {
                    'title': _('FileBrowser'),
                    'url': '/admin/filebrowser/browse/',
                    'external': False,
                },
            ]
        ))

        self.children.append(modules.LinkList(
            _('文档支持'),
            column=3,
            children=[
                {
                    'title': _('Django Documentation'),
                    'url': 'http://docs.djangoproject.com/',
                    'external': True,
                },
                {
                    'title': _('Grappelli Documentation'),
                    'url': 'http://packages.python.org/django-grappelli/',
                    'external': True,
                },
                {
                    'title': _('Grappelli Google-Code'),
                    'url': 'http://code.google.com/p/django-grappelli/',
                    'external': True,
                },
            ]
        ))

        self.children.append(modules.Feed(
            _('RSS 订阅'),
            column=3,
            feed_url='http://www.djangoproject.com/rss/weblog/',
            limit=5
        ))

        # 第四列: 最近操作
        self.children.append(modules.RecentActions(
            _('最近操作'),
            column=4,
            collapsible=True,
            limit=10,
        ))
