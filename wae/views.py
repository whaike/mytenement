# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from .models import Watermeter,Ammeter

# Create your views here.
def index_views(request):
	"""
	method: 'GET'
	api: '/'
	"""
	return render(request, 'wae/index.html')

def waters_views(request):
	"""
	method: GET
	api: 'wae/waters/'
	"""
	# w = Watermeter.objects.all()
	# print w.image
	return render(request,'wae/waters.html', {"waters":Watermeter.objects.all()})

def elecs_views(request):
	"""
	method: GET
	api: 'wae/elcs/'
	"""

	return render(request,'wae/elecs.html',{"elecs":Ammeter.objects.all()})
# @csrf_exempt
# def water_views(request):

# 	w_id = request.GET.get('water_id')
# 	if request.method == 'POST':
# 		degree = request.POST['degree']
# 		img = request.POST['image']

# 	water = Watermeter.objects.filter(id=w_id) if w_id else None
# 	return render(request, 'wae/water.html', {"water":water})
