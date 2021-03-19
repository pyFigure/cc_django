from django.db import models


# Create your models here.

class A(models.Model):
    a = models.CharField(verbose_name='a', max_length=10)
    m2m = models.ManyToManyField('B', through='AB')


class B(models.Model):
    b = models.CharField(verbose_name='b', max_length=10)


class AB(models.Model):
    a = models.ForeignKey(A, on_delete=models.CASCADE)
    b = models.ForeignKey(B, on_delete=models.CASCADE)
    c = models.CharField(verbose_name='c', max_length=10)
