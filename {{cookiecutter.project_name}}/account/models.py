from django.db import models
from django.contrib.auth.models import AbstractUser
from model_utils.models import SoftDeletableModel, UUIDModel
from django.contrib.auth.models import BaseUserManager
from account.avatar import IDAvatar


class UserManager(BaseUserManager):

    def _create_user(self, username, is_staff, is_superuser, **kwargs):
        if not username:
            raise ValueError('username 必须提供')
        user = self.model(username=username,
                          is_staff=is_staff,
                          is_superuser=is_superuser,
                          **kwargs)
        password = kwargs.get('password', None)
        if password:
            user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, **kwargs):
        return self._create_user(username=username, is_staff=False, is_superuser=False, **kwargs)

    def create_superuser(self, username, **kwargs):
        return self._create_user(username, is_staff=True, is_superuser=True, **kwargs)


class User(UUIDModel, SoftDeletableModel, AbstractUser):
    """自定义用户模型"""
    # 必填字段
    username = models.CharField(verbose_name='用户', max_length=40, unique=True)
    cn_name = models.CharField(verbose_name='中文名', max_length=20, blank=True, null=True)

    # 选填字段
    # 第三方登录创建账号时无需密码
    password = models.CharField(verbose_name='密码', max_length=128, blank=True, null=True)
    email = models.EmailField(verbose_name='邮箱', max_length=25, blank=True, null=True)
    mobile = models.CharField(verbose_name='手机', max_length=11, blank=True, null=True)
    avatar = models.CharField(verbose_name='头像', default=IDAvatar(email).wavatar(), max_length=200)
    qq = models.CharField(verbose_name='QQ号', max_length=32, blank=True, null=True)
    wx = models.CharField(verbose_name='微信', max_length=32, blank=True, null=True)

    # 额外用户状态字段，根据不同项目调整

    objects = UserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    class Meta:
        ordering = ['-date_joined']
        verbose_name_plural = verbose_name = '- 用户模型'

    def __str__(self):
        return self.username
