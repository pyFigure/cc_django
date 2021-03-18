from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin
from project.models import Project


# Register your models here.


@admin.register(Project)
class ProjectAdmin(DraggableMPTTAdmin):
    list_display = ['tree_actions', 'indented_title', 'name', 'type', 'pic', 'owner', 'is_removed', 'created',
                    'modified']
    list_display_links = ['indented_title']
    list_filter = ['is_removed']
    search_fields = ['name', 'type', 'pic__username', 'owner__username']
    fieldsets = [
        ('基本信息', {'classes': ['grp-collapse grp-open'], 'fields': ['name', 'type', 'pic', 'owner', 'parent']}),
        ('成员管理', {'classes': ['grp-collapse grp-open'], 'fields': ['users']}),
        ('标签管理', {'classes': ['grp-collapse grp-open'], 'fields': ['tags']}),
        ('标记删除', {'classes': ['grp-collapse grp-open'], 'fields': ['is_removed']}),
    ]
    mptt_level_indent = 20
    filter_horizontal = ['users']
