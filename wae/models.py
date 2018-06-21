# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import django.utils.timezone as timezone
from django.db import models

# Create your models here.
class Watermeter(models.Model):
	class Meta:
		verbose_name = u'水表'
		verbose_name_plural = u'水表'

	degree = models.IntegerField(verbose_name=u'度数')
	image = models.ImageField(verbose_name=u'图片',max_length=100,upload_to='water/%Y/%m/%d')
	img_date = models.DateTimeField(verbose_name=u'拍摄日期',default=timezone.now())
	create_at = models.DateTimeField(verbose_name=u'创建时间',auto_now_add=True)

	def __unicode__(self):
		return str(self.degree)



class Ammeter(models.Model):
	class Meta:
		verbose_name = u'电表'
		verbose_name_plural = u'电表'

	degree = models.IntegerField(verbose_name=u'度数')
	image = models.ImageField(verbose_name=u'图片',max_length=100,upload_to='elec/%Y/%m/%d')
	img_date = models.DateTimeField(verbose_name=u'拍摄日期',default=timezone.now())
	create_at = models.DateTimeField(verbose_name=u'创建时间',auto_now_add=True)

	def __unicode__(self):
		return str(self.degree)
