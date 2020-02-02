#!/usr/bin/python
# -*- coding: utf-8 -*-

''' All rights reserved (c) 2018 Ali Erkan IMREK <alierkanimrek@gmail.com> '''








import json
import time
import tornado
from parts import Glob








class BaseHandler(tornado.web.RequestHandler):




    def initialize(self):
        self.log = self.settings['log']
        self.conf = self.settings['conf']
        self.__log = self.log.job("UBase")
        self.lang = "tr-tr"
        self.glob = Glob(self.lang, self.conf.SERVER.heap_path)





    async def render_page(self, template, **kwargs):
        try:
            #await self.render(page+".html", kwargs)
            loader = tornado.template.Loader(self.settings['template_path'])
            self.finish(loader.load(template+".html").generate(template=template, glob=self.glob, **kwargs))
        except Exception as inst:
            self.__log.e_tb("Render error", inst)