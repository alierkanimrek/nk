#!/usr/bin/python
# -*- coding: utf-8 -*-

''' All rights reserved (c) 2018 Ali Erkan IMREK <alierkanimrek@gmail.com> '''








import os
import tornado, tornado.web
import datetime
import glob






FN_ROOT_PATH = "/tmp/"
FN_MONTHLY = "monthly.counter"
FN_DAILY = "daily.counter"
FN_HOURLY = "hourly.counter"
FN_HITS = "counter.hits"
FN_SEP = "_"




class Statistics(object):
    """
    Statistics Lib
    """



    def __init__(self, appname:str="app"):
        self.__name = appname




    def getVisitorId(self, request:tornado.web.RequestHandler):
        header = str(str(request.headers["User-Agent"]+request.headers["X-Real-Ip"]))
        return(abs(int(hash(bytes(header,"utf-8")))))




    def newVisitor(self):
        try:
            fh = open(self.getFn(FN_HITS), "ab")
            fh.write(b'.')
            fh.close()
        except Exception as inst:
            pass
        return()




    def getFn(self, fn:str):
        return(FN_ROOT_PATH+self.__name+FN_SEP+fn)




    def getHits(self):
        try:
            hit = os.path.getsize(self.getFn(FN_HITS))
        except Exception as inst:
            return(0)
        return(hit)