# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Watermeter,Ammeter

# Register your models here.
admin.site.register(Watermeter)
admin.site.register(Ammeter)