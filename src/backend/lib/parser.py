#!/usr/bin/python
# -*- coding: utf-8 -*-



import asyncio
import requests
from requests_html import HTMLSession, AsyncHTMLSession
from lxml.html import fromstring
import json
import shutil
import urllib
import time
from lib import LOG




HEADERS = {'User-Agent': "Mozilla/5.0 (Linux; U; Android 8.0; tr-tr; SM-T820NZKAXAR) AppleWebKit/604.5.6 (KHTML, like Gecko) Version/8.0 Mobile/15D60 Safari/604.1"}








class SocialItem():

    
    def __init__(self):
        self.title = ""
        self.img = ""
        self.desc = ""
        self.url = ""









class HTMLClient:




    def __init__(self, url:str="", file:str="", save:bool=False):
        self.save = save
        self.raw = ""
        self.status = False
        self.elements = None
        self.url = url
        self.file = file
        self._log = LOG._.job("HTML Parser")



            
    """
    def load(self, mobile=True):
        if(self.url):
            try:
                self._log.d("Loading",self.url)
                if mobile:
                    r = requests.get(self.url, headers=HEADERS)
                else:
                    r = requests.get(self.url)
                r.encoding = "UTF-8"
            except Exception as inst:
                self._log.e_tb("Loading error", inst)
                class r:
                    pass
                r.status_code = -1
            if r.status_code == 200:
                self.raw = r.text
                self._parse()
                if self.save:
                    self._save(self.url.replace("https://", "").replace("/","#"), self.raw)                
            else:
                self._log.e("Loading error", r.status_code)                    
        elif(self.file):
            try:
                fh = open(self.file, "r", encoding="UTF-8")
                self.raw = fh.read()
                fh.close()
            except Exception as inst:
                self._log.e_tb("Loading error", inst)                
            if(self.raw):
                self._parse()"""



    async def aload(self, mobile=True):
        try:
            session = AsyncHTMLSession()
            session.debuglevel = 0
            if mobile:  r = await session.get(self.url, headers=HEADERS)
            else:   r = await session.get(self.url)
            r.encoding = "UTF-8"
            if r.status_code == 200:
                await r.html.arender()
                self.raw = r.html.html
                self._parse()
                if self.save:
                    self._save(self.url.replace("https://", "").replace("/","#"), self.raw)
                return(True)
        except Exception as inst:
            self._log.e_tb("Loading error", inst)
        return(False)




    def load(self, mobile=True):
        try:
            session = HTMLSession()
            session.debuglevel = 0
            if mobile:  r = session.get(self.url, headers=HEADERS)
            else:   r = session.get(self.url)
            r.encoding = "UTF-8"
            if r.status_code == 200:
                r.html.render()
                self.raw = r.html.html
                self._parse()
                if self.save:
                    self._save(self.url.replace("https://", "").replace("/","#"), self.raw)
                return(True)
        except Exception as inst:
            self._log.e_tb("Loading error", inst)
        return(False)




    def load_file(self):
        try:
            fh = open(self.file, "r", encoding="UTF-8")
            self.raw = fh.read()            
            fh.close()
            if(self.raw):
                self._parse()
            return(True)            
        except Exception as inst:
            self._log.e_tb("Loading error", inst)                
        return(False)




    def _save(self, fn:str, raw:str):
        try:
            fh = open(fn, "w", encoding="UTF-8")
            fh.write(raw)
            fh.close()
        except Exception as inst:
            self._log.e_tb("Saving error", inst)




    def _parse(self):
        try:
            self.elements = fromstring(self.raw)
            if(self.elements):   self.status = True
            return(True)
        except Exception as inst:
            self._log.e_tb("Parsing error", inst)
            return(False)



    def save_image(self, url, fn):
        try:
            r = requests.get(url, stream=True)
            if r.status_code == 200:
                with open(fn, "wb+") as out_file:
                    shutil.copyfileobj(r.raw, out_file)
            else:
                self._log.e("IMG not loaded", r.status_code)
            del r
        except Exception as inst:
            self._log.e_tb("IMG Loading error", inst)




    def splitter(txt, start, end):
        s = txt.find(start)
        e = txt.find(end, s)
        return(txt[s:e])








class InstagramPage(HTMLClient):




    def __init__(self, url:str="", file:str="", save:bool=False):
        super(InstagramPage, self).__init__(url=url, file=file, save=save)
        self.items = []
        self._log = LOG._.job("InstaPage")
        self._splitter_start = "window._sharedData = "
        self._splitter_end = ";</script>"
        self._nodes = {}




    async def arender(self):
        await self.aload()
        if(self.status):    self.parse()




    def render(self):
        self.load()
        if(self.status):    self.parse()




    def parse(self):
        try:
            # Parse JSON Data to get nodes in self._nodes
            start = self.raw.find(self._splitter_start)+len(self._splitter_start)
            end = self.raw[start:].find(self._splitter_end)+start
            data = json.loads(self.raw[start:end])
            user = data["entry_data"]["ProfilePage"][0]["graphql"]["user"]
            nodes = user["edge_felix_video_timeline"]["edges"]
            nodes += user["edge_owner_to_timeline_media"]["edges"]
            for node in nodes:
                n = node["node"]
                url = n["shortcode"]
                cap = n["edge_media_to_caption"]["edges"][0]["node"]["text"]
                img = n["thumbnail_resources"][len(n["thumbnail_resources"])-1]["src"]
                self._nodes[url] = {"cap" :cap, "img": img}

            # Parse HTML
            for a in self.elements.xpath("//article")[0].xpath(".//a"):
                social = SocialItem()
                social.url = "https://instagram.com"+a.attrib["href"]
                code = a.attrib["href"][2:].replace("/","")
                social.desc = self._nodes[code]["cap"]
                #social.img = a.xpath(".//img")[0].attrib["src"]
                social.img = self._nodes[code]["img"]
                self.items.append(vars(social))
        except Exception as inst:
            self._log.e_tb("Parsing error", inst)








class FacebookPage(HTMLClient):




    def __init__(self, url:str="", file:str="", save:bool=False):
        super(FacebookPage, self).__init__(url=url, file=file, save=save)
        self.items = []
        self._log = LOG._.job("FacebookPage")
        self._pgname = "antalyapraniksifa"
        self._fbprefix = "https://facebook.com"



    async def arender(self):
        await self.aload(False)
        if(self.status):    self.parse()




    def render(self):
        self.load(False)
        if(self.status):    self.parse()




    def parse(self):
        try:
            for post in self.elements.xpath('//div[@class="_1xnd"]')[0].xpath("div"):
                social = SocialItem()
                if post.xpath('.//p'):
                    social.desc = post.xpath('.//p')[0].text
                imgs = post.xpath('.//img')
                if imgs:
                    del imgs[0] #First is profile img
                    if imgs[0].attrib["src"].find(".png") == -1:
                        social.img = imgs[0].attrib["src"]
                    elif len(imgs) > 1:
                        social.img = imgs[1].attrib["src"]

                for a in post.xpath('.//a'):
                    if a.attrib["href"].find(self._pgname) == 1:
                       social.url = self._fbprefix+a.attrib["href"]
                       break
                    elif a.attrib["href"].find("events") == 1:
                       social.url = self._fbprefix+a.attrib["href"]
                       break
                social.url = social.url[:social.url.find("?")]
                self.items.append(vars(social))
        except Exception as inst:
            self._log.e_tb("Parsing error", inst)
