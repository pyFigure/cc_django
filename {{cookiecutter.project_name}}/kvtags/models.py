import uuid

from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models


class UUIDModel(models.Model):
    """uuid 作为 id"""
    id = models.UUIDField(verbose_name='id', default=uuid.uuid4, primary_key=True)

    class Meta:
        abstract = True


class TimestampModel(models.Model):
    """提供时间字段"""
    created = models.DateTimeField(verbose_name='创建', auto_now_add=True)
    updated = models.DateTimeField(verbose_name='更新', auto_now=True)

    class Meta:
        abstract = True


class KvTag(UUIDModel, TimestampModel):
    """key-value 标签"""
    key = models.CharField(verbose_name='键', max_length=100)
    value = models.CharField(verbose_name='值', max_length=100, blank=True, null=True)

    class Meta:
        verbose_name_plural = verbose_name = '- 键值标签'
        unique_together = [['key', 'value']]

    def __unicode__(self):
        if self.value:
            return "{key}:{value}".format(key=self.key, value=self.value)
        return self.key


class TaggedItemBase(models.Model):
    tag = models.ForeignKey(KvTag, verbose_name='标签', on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, verbose_name='模型', on_delete=models.CASCADE)
    content_object = GenericForeignKey()

    class Meta:
        abstract = True
        verbose_name_plural = verbose_name = '- 标签管理'
        app_label = "kvtags"
        index_together = [["content_type", "object_id"]]
        unique_together = [["content_type", "object_id", "tag"]]


class UUIDTaggedItemBase(models.Model):
    object_id = models.UUIDField(verbose_name='对象', db_index=True)

    class Meta:
        abstract = True


class UUIDTaggedItem(UUIDTaggedItemBase, TaggedItemBase):
    """UUID 标签"""
    pass
