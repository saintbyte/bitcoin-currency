# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from mainapp.models import ExchangeCurrency

class ExchangeCurrencyAdmin(admin.ModelAdmin):
    pass

admin.site.register(ExchangeCurrency,ExchangeCurrencyAdmin)
