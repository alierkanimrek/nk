#!/usr/bin/python
# -*- coding: utf-8 -*-

''' All rights reserved (c) 2018 Ali Erkan IMREK <alierkanimrek@gmail.com> '''



from base import BaseHandler
from parts import Greeting, Prof



class MainHandler(BaseHandler):

    
    async def get(self):
        temp = "main"
        greeting = Greeting(self.lang, self.conf.SERVER.heap_path)
        prof = Prof(self.lang, self.conf.SERVER.heap_path)
        await self.render_page(
            template=temp,
            greeting=greeting,
            prof=prof
            )








mainRouting = [
    (r"/", MainHandler),
    ]
  