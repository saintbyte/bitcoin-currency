# -*- coding: utf-8 -*-
__author__ = 'SB'
from django.core.management.base import BaseCommand
import json
import math
from django.conf import settings
import os
import time
import sys
import urllib, urllib2


class Command(BaseCommand):
    help = 'Tools for get curs'

    def get_json(self, url):
        response = urllib2.urlopen(url)
        json_src = response.read()
        try:
            return json.loads(json_src)
        except:
            return []

    def store(self, url, filename):
        """
        TODO: Подумать надо локом файла
        :param url:
        :param filename:
        :return:
        """
        try:
            jsdata = self.get_json(url)
        except:
            # Отпала например из сети или json нет тот
            return False
        try:
            price = jsdata['ticker']['price']
        except:
            # INdexError очень может быть
            return False
        fh = open(filename, 'w')
        fh.write(str(price))
        fh.close()
        return True

    def getbtcusd(self):
        self.store('https://api.cryptonator.com/api/ticker/btc-usd', settings.BTCUSD_FILE)
        return True

    def getethusd(self):
        self.store('https://api.cryptonator.com/api/ticker/eth-usd', settings.ETHUSD_FILE)
        return True

    def handle(self, *args, **options):
        while True:
            try:
                self.getbtcusd()
                self.getethusd()
                time.sleep(10)
            except KeyboardInterrupt:
                print 'Quit'
                quit()
            except:
                print str(sys.exc_info()[0])
                print str(sys.exc_info()[1])
