# -*- coding: utf8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.conf import settings
from .models import ExchangeCurrency
# Create your views here.
def home(request):
    c = {}
    c['btcusd'] = 'Пока нет значения'
    c['ethusd'] = 'Пока нет значения'
    try:
        c['btcusd'] =  open(settings.BTCUSD_FILE,'r').read()
    except:
        pass
    try:
        c['ethusd'] =  open(settings.ETHUSD_FILE ,'r').read()
    except:
        pass
    c['currlist'] = []
    c['currlist'] = ExchangeCurrency.objects.all()
    return render(request,'index.html',c)