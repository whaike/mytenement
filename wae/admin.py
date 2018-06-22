# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Watermeter,Ammeter

# Register your models here.
# @admin.register(Watermeter)
class WaeAdmin(admin.ModelAdmin):
	list_display = ('id','degree','img_date','create_at')
	list_filter = ('img_date',)

admin.site.register(Watermeter,WaeAdmin)
admin.site.register(Ammeter,WaeAdmin)
