#!/usr/bin/python
# -*- coding: utf-8 -*-

''' All rights reserved (c) 2018 Ali Erkan IMREK <alierkanimrek@gmail.com> '''



from base import BaseHandler
from parts import Greeting, Prof, Social, Form1, Blogger
import random



class MainHandler(BaseHandler):

    
    async def get(self):
        temp = "main"
        greeting = Greeting(self.lang, self.conf.SERVER.heap_path)
        prof = Prof(self.lang, self.conf.SERVER.heap_path)
        soc = Social(self.lang)
        form1 = Form1(self.lang)
        blog = Blogger(self.lang)
        await self.render_page(
            template=temp,
            greeting=greeting,
            prof=prof,
            soc=soc,
            form1=form1,
            blog=blog
            )







class DanismanlikHandler(BaseHandler):

    
    async def get(self):
        id = "prof1"
        temp = "danismanlik"
        prof = Prof(self.lang, self.conf.SERVER.heap_path)
        form1 = Form1(self.lang)
        soc = Social(self.lang)
        blog = Blogger(self.lang)
        blgSearched = blog.search(["hasta", "tedavi"])
        if(blgSearched):    blgSearched = random.choice(blgSearched)        

        socAssorted = []
        
        newsDict = soc.searchAndChoose(["şifa"])
        news = soc.mix(newsDict)
        rndDict = soc.searchAndChoose(["şifa"], rnd=True)
        rnd = soc.mix(rndDict)
        items = news + rnd
        for item in items:
            f = False
            for a in socAssorted:
                if item["desc"] == a["desc"]:   
                    f = True
                    break
            if not f:   socAssorted.append(item)

        await self.render_page(
            template=temp,
            id=id,
            prof=prof,
            form1=form1,
            socAssorted=socAssorted,
            blog=blog,
            blogSearched=blgSearched
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
        soc = Social(self.lang)
        blog = Blogger(self.lang)
        blgSearched = blog.search(["seminer", "eğitim", "sunum"])
        if(blgSearched):    blgSearched = random.choice(blgSearched)

        socAssorted = []
        
        newsDict = soc.searchAndChoose(["seminer", "eğitim", "sunum"])
        news = soc.mix(newsDict)
        rndDict = soc.searchAndChoose(["seminer", "eğitim", "sunum"], rnd=True)
        rnd = soc.mix(rndDict)
        items = news + rnd
        for item in items:
            f = False
            for a in socAssorted:
                if item["desc"] == a["desc"]:   
                    f = True
                    break
            if not f:   socAssorted.append(item)

        await self.render_page(
            template=temp,
            id=id,
            prof=prof,
            soc=soc,
            socAssorted=socAssorted,
            blog=blog,
            blogSearched=blgSearched
            )






class KisiselGHandler(BaseHandler):

    
    async def get(self):
        id = "prof3"
        temp = "kisiselgelisim"
        prof = Prof(self.lang, self.conf.SERVER.heap_path)
        soc = Social(self.lang)
        blog = Blogger(self.lang)
        blgSearched = blog.search(["ikiz", "meditasyon"])
        if(blgSearched):    blgSearched = random.choice(blgSearched)
        socAssorted = []
        
        newsDict = soc.searchAndChoose(["ikiz", "meditasyon"])
        news = soc.mix(newsDict)
        rndDict = soc.searchAndChoose(["ikiz", "meditasyon"], rnd=True)
        rnd = soc.mix(rndDict)
        items = news + rnd
        for item in items:
            f = False
            for a in socAssorted:
                if item["desc"][:80] == a["desc"][:80]:
                    f = True
                    break
            if not f:   socAssorted.append(item)
        await self.render_page(
            template=temp,
            id=id,
            prof=prof,
            soc=soc,
            socAssorted=socAssorted,
            blogSearched=blgSearched
            )




class BlogHandler(BaseHandler):

    
    async def get(self):
        temp = "blog"
        blog = Blogger(self.lang)
        await self.render_page(
            template=temp,
            entries=blog.entries
            )




class BlogEntryHandler(BaseHandler):

    
    async def get(self, id):
        temp = "blogentry"
        blog = Blogger(self.lang)
        await self.render_page(
            template=temp,
            entry=blog.find(id),
            entries=blog.entries
            )






mainRouting = [
    (r"/", MainHandler),
    (r"/danismanlik", DanismanlikHandler),
    (r"/danismanlik/yorum", DanismanlikYorumHandler),
    (r"/seminer", SeminerHandler),
    (r"/kisiselgelisim", KisiselGHandler),
    (r"/yazilar", BlogHandler),
    (r"/yazilar/(.*?)", BlogEntryHandler)
    ]
  