from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from model_utils.models import TimeStampedModel, SoftDeletableModel, UUIDModel
from django.conf import settings
from utils.common.models import OwnerModel


# Create your models here.


class Project(MPTTModel, UUIDModel, OwnerModel, SoftDeletableModel, TimeStampedModel):
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    name = models.CharField(verbose_name='名称', max_length=50)
    type = models.CharField(verbose_name='类型', max_length=50)
    pic = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='责任人', on_delete=models.CASCADE,
                            related_name='charged_project')
    users = models.ManyToManyField(settings.AUTH_USER_MODEL, verbose_name='成员', related_name='belong_to_project')

    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        return "%s - %s" % (self.type, self.name)
