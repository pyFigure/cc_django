from account.forms import UserChangeForm, UserCreationForm
from account.models import User
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin


# Register your models here.


@admin.register(User)
class AccountUserAdmin(UserAdmin):
    fieldsets = [
        ('必填字段', {'classes': ['grp-collapse grp-open'], 'fields': ('username', 'cn_name', 'email', 'mobile')}),
        ('选填字段', {'classes': ['grp-collapse grp-open'], 'fields': ('first_name', 'last_name', 'avatar')}),
        ('联系方式', {'classes': ['grp-collapse grp-open'], 'fields': ('wx', 'qq')}),
        ('群组权限', {'classes': ['grp-collapse grp-closed'], 'fields': ('groups', 'user_permissions')}),
        ('用户权限', {
            'classes': ['grp-collapse grp-open'],
            'fields': ['is_active', 'is_staff', 'is_superuser', 'is_removed']
        }),
        ('时间信息', {'classes': ['grp-collapse grp-open'], 'fields': ['last_login', 'date_joined']}),
    ]

    add_fieldsets = (
        ('用户信息', {
            'classes': ['grp-collapse grp-open'],
            'fields': ['username', 'cn_name', 'email', 'password', 'mobile']}),
    )
    form = UserChangeForm
    add_form = UserCreationForm
    list_display = ['username', 'cn_name', 'email', 'mobile', 'wx', 'qq', 'last_name', 'first_name', 'is_active',
                    'is_superuser',
                    'is_removed']
    list_filter = ['is_active', 'is_staff', 'is_superuser', 'is_removed']
    search_fields = ['email', 'mobile', 'wx', 'qq']
    ordering = ['username']
