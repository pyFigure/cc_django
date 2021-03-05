from django.contrib.contenttypes.models import ContentType
from django.core.cache import caches
from django.db import models

from kvtags.models import KvTag, UUIDTaggedItem


class TagManager(models.Manager):
    """标签系统管理"""

    def __init__(self, cache_alias=None):
        super(TagManager, self).__init__()
        if cache_alias:
            try:
                self.CACHE = caches[cache_alias]
            except KeyError:
                self.CACHE = None
        else:
            self.CACHE = None

    @staticmethod
    def add(obj, **kwargs):
        """添加标签"""
        content_type = ContentType.objects.get_for_models(obj)
        for tag in KvTag.objects.filter(**kwargs):
            UUIDTaggedItem.objects.get_or_create(tag=tag, content_type=content_type, object_id=obj.id)

    @staticmethod
    def remove(obj, **kwargs):
        """ Removes tags matched by kwargs from obj. """
        content_type = ContentType.objects.get_for_model(obj)
        for tag in KvTag.objects.filter(**kwargs):
            try:
                item = UUIDTaggedItem.objects.get(tag=tag, content_type=content_type, object_id=obj.id)
                item.delete()
            except UUIDTaggedItem.DoesNotExist:
                pass

    @staticmethod
    def filter(obj, **kwargs):
        """ Returns QuerySet of Tags bound to obj and matched by kwargs. """
        content_type = ContentType.objects.get_for_model(obj)
        tag_ids = UUIDTaggedItem.objects.filter(object_id=obj.id, content_type=content_type).values('tag')
        return KvTag.objects.filter(pk__in=tag_ids, **kwargs)

    @staticmethod
    def get_tags(obj):
        """ Returns a list of Tag model instances bound to obj. """
        content_type = ContentType.objects.get_for_model(obj)
        tags = dict()

        for item in UUIDTaggedItem.objects.filter(content_type=content_type, object_id=obj.id).values('tag'):
            tag = KvTag.objects.prefetch_related('kv_pairs').get(pk=item['tag'])
            tags.update(tag)

        return tags
