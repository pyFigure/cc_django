from django.contrib import admin

from kvtags.models import KvTag, UUIDTaggedItem


class UUIDTaggedItemInline(admin.StackedInline):
    model = UUIDTaggedItem


@admin.register(KvTag)
class KvTagAdmin(admin.ModelAdmin):
    inlines = [UUIDTaggedItemInline]
    list_display = ['key', 'value', 'created', 'updated']
    ordering = ['key', 'value']
    search_fields = ['key', 'value']
