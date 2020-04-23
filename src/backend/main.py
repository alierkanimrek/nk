#!/usr/bin/python
# -*- coding: utf-8 -*-

''' All rights reserved (c) 2018 Ali Erkan IMREK <alierkanimrek@gmail.com> '''



from base import BaseHandler
from parts import Greeting, Prof, Social, Form1



class MainHandler(BaseHandler):

    
    async def get(self):
        temp = "main"
        greeting = Greeting(self.lang, self.conf.SERVER.heap_path)
        prof = Prof(self.lang, self.conf.SERVER.heap_path)
        soc = Social(self.lang)
        form1 = Form1(self.lang)
        await self.render_page(
            template=temp,
            greeting=greeting,
            prof=prof,
            soc=soc,
            form1=form1
            )







class DanismanlikHandler(BaseHandler):

    
    async def get(self):
        id = "prof1"
        temp = "danismanlik"
        prof = Prof(self.lang, self.conf.SERVER.heap_path)
        form1 = Form1(self.lang)
        await self.render_page(
            template=temp,
            id=id,
            prof=prof,
            form1=form1
            )








class DanismanlikYorumHandler(BaseHandler):

    
    async def get(self):
        id = "prof1"
        temp = "danismanlikyorum"
        prof = Prof(self.lang, self.conf.SERVER.heap_path)
        form1 = Form1(self.lang)
        form1.formdata.comments.reverse()
        await self.render_page(
            template=temp,
            id=id,
            prof=prof,
            form1=form1
            )








class SeminerHandler(BaseHandler):

    
    async def get(self):
        id = "prof2"
        temp = "seminer"
        prof = Prof(self.lang, self.conf.SERVER.heap_path)
        await self.render_page(
            template=temp,
            id=id,
            prof=prof,
            )






class KisiselGHandler(BaseHandler):

    
    async def get(self):
        id = "prof3"
        temp = "kisiselgelisim"
        prof = Prof(self.lang, self.conf.SERVER.heap_path)
        await self.render_page(
            template=temp,
            id=id,
            prof=prof,
            )






mainRouting = [
    (r"/", MainHandler),
    (r"/danismanlik", DanismanlikHandler),
    (r"/danismanlik/yorum", DanismanlikYorumHandler),
    (r"/seminer", SeminerHandler),
    (r"/kisiselgelisim", KisiselGHandler)
    ]
  