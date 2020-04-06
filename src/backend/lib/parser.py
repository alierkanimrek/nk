#!/usr/bin/python
# -*- coding: utf-8 -*-




import requests
from lxml.html import fromstring
import json
import shutil
import urllib
import time





HEADERS = {'User-Agent': "Mozilla/5.0 (Linux; U; Android 8.0; tr-tr; SM-T820NZKAXAR) AppleWebKit/604.5.6 (KHTML, like Gecko) Version/8.0 Mobile/15D60 Safari/604.1"}








class SocialItem():

    title = ""
    img = ""
    desc = ""
    url = ""








class Parser:




    def __init__(self, url:str="", file:str="", save:bool=False):
        self.save = save
        self.raw = ""
        self.status = False
        self.elements = None
        self.url = url
        self.file = file



            
    def load(self):
        if(self.url):
            try:
                r = requests.get(self.url, headers=HEADERS, timeout=15)
                r.encoding = "UTF-8"
            except:
                class r:
                    pass
                r.status_code = -1
            if r.status_code == 200:
                self.raw = r.text
                self._parse()
                if self.save:
                    self._save(self.url.replace("https://", "").replace("/","#"), self.raw)                
        elif(self.file):
            fh = open(self.file, "r", encoding="UTF-8")
            self.raw = fh.read()
            fh.close()
            if(self.raw):
                self._parse()




    def _save(self, fn:str, raw:str):
        fh = open(fn, "w", encoding="UTF-8")
        fh.write(raw)
        fh.close()




    def _parse(self):
        self.elements = fromstring(self.raw)
        if(self.elements):   self.status = True




    def save_image(self, url, fn):
        r = requests.get(url, stream=True)
        if r.status_code == 200:
            with open(fn, "wb+") as out_file:
                shutil.copyfileobj(r.raw, out_file)
        else:
            print(r.status_code)
        del r




    def splitter(txt, start, end):
        s = txt.find(start)
        e = txt.find(end, s)
        return(txt[s:e])









def test_parser(uri="", fn=""):
    parser = Parser(uri, fn, True)
    parser.load()
    if(parser.status):
        for elm in parser.elements:
            print(elm.text_content())
#test_parser(uri="https://instagram.com/pranik_arhat")








class RssApp(Parser):



    
    def __init__(self, url:str="", file:str="", save:bool=False):
        super(RssApp, self).__init__(url=url, file=file, save=save)
        self.items = []




    def parse(self):
        self.load()
        if(self.status):
            try:
                data = json.loads(self.elements.find("body").find("script").text)
                id = data["props"]["pageProps"]["id"]
                items = data["props"]["apolloState"]["$Embed:feed-"+id+".feed"]["items"]
                for item in items:
                    post = data["props"]["apolloState"][item["id"]]
                    enclosure = post["enclosure"]["id"]
                    
                    social = SocialItem()
                    social.title = post["title"]
                    social.desc = post["description"]
                    social.url = post["url"]
                    social.img = data["props"]["apolloState"][enclosure]["url"]
                    self.items.append(vars(social))
            except:
                pass