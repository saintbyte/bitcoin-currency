# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class ExchangeCurrency(models.Model):
    name = models.CharField(max_length=128,verbose_name='Название')
    endpoint = models.CharField(max_length=128,verbose_name='Откуда качать ',
                                help_text='Для пути https://api.cryptonator.com/api/ticker/btc-usd будет btc-usd')
    price = models.CharField(max_length=128, verbose_name="Значение", default='0') #TODO: по хорошему надо цифровое но лениво думать над раземернсотью

    def __str__(self):
        return self.name

    def __unicode__(self):
        return unicode(self.name)

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"