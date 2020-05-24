#!/usr/bin/python
# -*- coding: utf-8 -*-


import requests
import feedparser
from lib import LOG, HTTPLoader
import os












class BloggerAtom():




    def __init__(self, url:str="", file:str="", save:bool=False):
        self.__url = url
        self.__save = save
        self.__file = file
        self.raw = ""
        self.entries = ""
        self._log = LOG._.job("BloggerAtom")




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
        try:
            self.entries = feedparser.parse(self.raw).entries
        except Exception as inst:
            self._log.e_tb("Parsing error", inst)  