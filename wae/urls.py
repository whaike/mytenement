#-*- coding:utf-8 -*-
from django.conf.urls import url
from .views import *

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
	url(r'^waters/$',waters_views),
	url(r'^elecs/$',elecs_views),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)