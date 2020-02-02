#!/usr/bin/python
# -*- coding: utf-8 -*-




import requests
from lxml.html import fromstring
import json






HEADERS = {'User-Agent': "Mozilla/5.0 (Linux; U; Android 8.0; tr-tr; SM-T820NZKAXAR) AppleWebKit/604.5.6 (KHTML, like Gecko) Version/8.0 Mobile/15D60 Safari/604.1"}








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





def test_parser(uri="", fn=""):
    parser = Parser(uri, fn, True)
    parser.load()
    if(parser.status):
        for elm in parser.elements:
            print(elm.text_content())



#test_parseruri="https://instagram.com/pranik_arhat")








INS_HOME_INSTRUCTIONS = {
    "dataName": "window._sharedData",
    "linkAttr" : "shortcode",
    "timeAttr": "taken_at_timestamp"
}




class Instagram_Home(Parser):



    
    def __init__(self, url:str="", file:str="", save:bool=False):
        super(Instagram_Home, self).__init__(url, file, save)
        self.links = {}
        self.sorted = []




    def parse(self, count:int=3):
        result = [] #[url,...]
        self.load()
        if(self.status):
            # Get script tags
            for script in self.elements.find("body").findall("script"):
                # Get data 
                if(script.text and script.text.strip().find(INS_HOME_INSTRUCTIONS["dataName"]) == 0):
                    data = (script.text[script.text.find("{"):])
                    try:
                        # Parse to object but data actually broken
                        jdata = json.loads(data, object_hook=self.hook)
                    except:
                        pass
                    self.sorted = sorted(self.links, key=self.links.__getitem__, reverse=True)
                    for n in range(count):
                        result.append(self.links[self.sorted[n]])
        return(result)




    def hook(self, obj):
        if(INS_HOME_INSTRUCTIONS["linkAttr"] in obj):
            link = obj[INS_HOME_INSTRUCTIONS["linkAttr"]]
            timestamp = obj[INS_HOME_INSTRUCTIONS["timeAttr"]]
            self.links[timestamp] = link







INS_PAGE_INSTRUCTIONS = {
    "dataName": "window._sharedData",
    "linkAttr" : "shortcode",
    "timeAttr": "taken_at_timestamp",
    "urlPrefix": "https://instagram.com/p/"
}




class Instagram_Page(Parser):



    
    def __init__(self, url:str="", file:str="", save:bool=False):
        super(Instagram_Page, self).__init__(INS_PAGE_INSTRUCTIONS["urlPrefix"]+url+"/data/shared_data/", file, save)
        self.links = {}
        self.sorted = []




    def parse(self):
        result = [] #[url,...]
        self.load()
        return()
        if(self.status):
            # Get script tags
            for script in self.elements.find("body").findall("script"):
                # Get data 
                if(script.text and script.text.strip().find(INS_HOME_INSTRUCTIONS["dataName"]) == 0):
                    data = (script.text[script.text.find("{"):])
                    try:
                        # Parse to object but data actually broken
                        jdata = json.loads(data, object_hook=self.hook)
                    except:
                        pass
                    self.sorted = sorted(self.links, key=self.links.__getitem__, reverse=True)
                    for n in range(count):
                        result.append(self.links[self.sorted[n]])
        return(result)




    def hook(self, obj):
        if(INS_HOME_INSTRUCTIONS["linkAttr"] in obj):
            link = obj[INS_HOME_INSTRUCTIONS["linkAttr"]]
            timestamp = obj[INS_HOME_INSTRUCTIONS["timeAttr"]]
            self.links[timestamp] = link


def test_I_Home():
    ih = Instagram_Home(file="instagram.com#pranik_arhat")
    p1 = ih.parse()[0]
    print(p1)
    ip = Instagram_Page(p1, save=True)
    ip.parse()




#test_I_Home()