#!/usr/bin/python
# -*- coding: utf-8 -*-

''' All rights reserved (c) 2018 Ali Erkan IMREK <alierkanimrek@gmail.com> '''


import os
import json
import glob
import random
from lib import LOG








class Parts():

    


    def __init__(self, fn:str, path:str = "", lang:str = "tr-tr"):
        self._data = {}
        self.data = {}
        self.lang = lang
        filename = fn
        if path == "":
            path, filename = os.path.split(os.path.abspath(__file__))
            self._fn = os.path.join(path, fn+".json")
        else:
            self._fn = os.path.join(path, fn+".json")
        self._log = LOG._.job("Parts Base")
        self.__load()




    def __load(self):
        fh = open(self._fn, "r")
        try:
            self._data = json.loads(fh.read())
            self.data = self._data[self.lang]
        except Exception as inst:
            self._log.e_tb("Loading error", inst)




    def choose(self, path:str, search:str):
        files = glob.glob(path+"/"+search)
        if(files):
            return(os.path.basename(files[random.randrange(len(files))]))
        else:
            return(False)




    def save(self, content):
        swap = self._data
        swap[self.lang] = content
        try:
            jsn = json.dumps(swap, indent=4, separators=(',', ': '), ensure_ascii=False)
            fh = open(self._fn, "w+", encoding='utf8')
            fh.write(jsn)
            fh.close()
        except Exception as inst:
            self._log.e_tb("Save error", inst)
        self.__load()