#!/usr/bin/python
# -*- coding: utf-8 -*-




import requests
import time
from lib import LOG







HEADERS = {'User-Agent': "Mozilla/5.0 (Linux; U; Android 8.0; tr-tr; SM-T820NZKAXAR) AppleWebKit/604.5.6 (KHTML, like Gecko) Version/8.0 Mobile/15D60 Safari/604.1"}








class HTTPLoader:




    def __init__(self, uri, save=False):
        self.save = save
        self.raw = ""
        self.status = False
        self._load(uri)
        self._log = LOG._.job("HTML Loader")



        
    def _load(self, uri):
        try:
            r = requests.get(uri)
            r.encoding = "UTF-8"
            if r.status_code == 200:
                self.raw = r.text
                self.status = True                
                if self.save:
                    try:
                        fh = open(uri.replace("https://", "").replace("/","#"), "w", encoding="utf-8")
                        fh.write(r.text)
                        fh.close
                    except Exception as inst:
                        self._log.e_tb("File error", inst)
        except Exception as inst:
            self._log.e_tb("Request error", inst)
