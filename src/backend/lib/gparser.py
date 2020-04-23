#!/usr/bin/python
# -*- coding: utf-8 -*-


import requests
from lib import LOG, HTTPLoader
import os












class GForm():




    def __init__(self, url:str="", file:str="", save:bool=False):
        self.__url = url
        self.__save = save
        self.__file = file
        self.raw = ""
        self.items = []
        self.itemsd = {}
        self.titles = []        
        self._log = LOG._.job("GForm")




    async def aload(self):
        if self.__url:
            r = HTTPLoader(self.__url, self.__save)
            if r.status:
                self.raw = r.raw
        elif self.__file:
            try:
                fh = open(self.__file, "r", encoding="UTF-8")
                self.raw = fh.read()            
                fh.close()
            except Exception as inst:
                self._log.e_tb("File error", inst)                
        await self.aparse()




    async def aparse(self):
        c = 0
        if self.raw:
            for item in self.raw.splitlines():
                i = item.split("\t")
                if c > 0:
                    self.items.append(i)
                    self.itemsd[i[0]] = i
                else:
                    self.titles = i 
                c += 1