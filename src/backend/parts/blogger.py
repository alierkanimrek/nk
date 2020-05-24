#!/usr/bin/python
# -*- coding: utf-8 -*-

''' All rights reserved (c) 2018 Ali Erkan IMREK <alierkanimrek@gmail.com> '''


from .base import Parts
import random
import re






NAME = "blogger"




class BloggerData:
    def __init__(self):
        self.entries = []






class BloggerEntry:
    def __init__(self):
        self.id = ""
        self.time = ""
        self.title = ""
        self.content = ""
        self.img = ""
        self.sum = ""








class Blogger(Parts):

    
    def __init__(self, lang:str):
        super(Blogger, self).__init__(fn=NAME, lang=lang)
        self.entries =  self.data["entries"]
        self.random = vars(BloggerEntry())
        self.chooseInLast()




    async def update(self, entries):
        new = BloggerData()
        for entry in entries:
            if(entry.published_parsed[0] >= 2020):
                e = BloggerEntry()
                e.id = entry.id.split("-")[2]
                e.title = entry.title
                e.time = entry.published
                e.content = entry.content[0].value
                e.img = self.findImage(e.content)
                e.sum = self.findTxt(e.content)
                new.entries.append(vars(e))
        self.save(vars(new))




    def findImage(self, content):
        imgTag = content.find("<img")
        srcAttr = content.find('src="', imgTag)+5
        endTag = content.find('"', srcAttr)
        f = content[srcAttr:endTag]
        if(f):
            return(f)
        return("")




    def findTxt(self, content):
        st = 0
        end = 0
        while True:
            st = content.find(">", st)+1
            end = content.find("<",st)
            if end == -1:
                break
            if len(content[st:end].strip()) > 0:
                break
        return(content[st:end])




    def find(self, id):
        for entry in self.entries:
            if entry["id"] == id:
                return(entry)
        return(BloggerEntry())




    def chooseInLast(self, last=3):
        if len(self.entries) < last:
            last = len(self.entries)
        pool = self.entries[:last]
        if last:
            self.random = pool[random.randrange(last)-1]
        return(self.random)
        
        


    def search(self, terms):
        result=[]
        #Search
        for entry in self.entries:
            for term in terms:
                if( re.search(term, entry["title"], re.IGNORECASE) or re.search(term, entry["sum"], re.IGNORECASE)):
                    result.append(entry)
        return(result)
