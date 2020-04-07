#!/usr/bin/python
# -*- coding: utf-8 -*-

''' All rights reserved (c) 2018 Ali Erkan IMREK <alierkanimrek@gmail.com> '''








import sys, os
sys.path.append(os.getcwd())
from datetime import datetime

from tornado import gen, ioloop, web

from lib import KBConfig, CONF
from lib import KBLogger, LOG
from lib import STM
from lib import Statistics
from webbot import social_updater
from main import mainRouting







conf = None
log = None



"""
    Init configuration and Log system 

"""
try:
    print("Server initializing...")

    conf = KBConfig("config","./")
    log = KBLogger(conf.LOG.log_file, "nk")
    log.level = conf.LOG.log_level
    
    stage1 = log.job("Stage1")
    stage1.i("Configuration loaded", 
        "log_level:"+conf.LOG.log_level, 
        "maintenance:"+conf.SERVER.maintenance)
    LOG._ = log
    CONF._ = conf
except Exception as inst:
    print("Initializing failed")
    print(type(inst))
    print(inst.args)
    print(inst)
    sys.exit(-1)










async def reload():
    if not ioloop.IOLoop.current().reloader.is_running():
        ioloop.IOLoop.current().reloader.start()
    else:
        try:
            conf.reload()
            log.level = conf.LOG.log_level
            stage1.d("Conf updated")
        except Exception as inst:
            stage1.e_tb("Conf updating failed", inst)






async def socUpdate():
    minute = datetime.strftime(datetime.utcnow(), "%M")
    hour = int(datetime.strftime(datetime.utcnow(), "%H"))+3
    
    if not ioloop.IOLoop.current().socLoader.is_running():
        ioloop.IOLoop.current().socLoader.start()
    else:
        try:
            if hour > 8:
                if minute in ["05", "25", "45", "55"]:
                    social_updater(conf.SERVER.heap_path+"/social", ["ins"])
                    stage1.d("Social updated", "ins")
                if minute == "00" and hour in list(range(8,24)):
                    social_updater(conf.SERVER.heap_path+"/social", ["fbk", "ytb"])
                    stage1.d("Social updated", "fbk, ytb")
        except Exception as inst:
            stage1.e_tb("Social updating failed", inst)





routing = mainRouting



application = web.Application(
    routing,
    xheaders = True,
    debug = True,
    conf = conf,
    log = log,
    sts = Statistics("nk"),
    cookie_secret = conf.SERVER.cookie_key,
    xsrf_cookies = True, 
    template_path = conf.SERVER.template_path,
    visitors = STM(120)
    )




if __name__ == "__main__":
    application.listen(8000)
    stage1.i("Server listening...")
    mainloop = ioloop.IOLoop.instance()
    mainloop.reloader = ioloop.PeriodicCallback(reload, 60000)
    mainloop.socLoader = ioloop.PeriodicCallback(socUpdate, 60000)
    mainloop.add_callback(reload)
    mainloop.add_callback(socUpdate)
    mainloop.start()
    
