#!/usr/bin/python
# -*- coding: utf-8 -*-

''' All rights reserved (c) 2018 Ali Erkan IMREK <alierkanimrek@gmail.com> '''


from .base import Parts
import re
import random


NAME = "social"




class Social(Parts):

    
    def __init__(self, lang:str):
        super(Social, self).__init__(fn=NAME, lang=lang)
        



    def update(self, items):
        self.save(items)



    @property
    def front(self):
        front = []
        try:
            front.append(self.data["ins"][0])
            for item in self.data["fbk"]:
                if item["desc"] != "" and item["desc"][:20] != front[0]["desc"][:20]:
                    front.append(item)
                    break
            front.append(self.data["ytb"][0])
        except:
            pass
        return(front)




    @property
    def imgs(self):
        imgs = []
        for soc in ["ins", "fbk", "ytb"]:
            for item in self.data[soc]:
                imgs.append(item["img"])
        return(imgs)




    @property
    def events(self, max=4):
        events = []
        try:
            for item in self.data["fbk"]:
                if '/events/' in item["url"]:
                    events.append(item)
                if len(events) == max:
                    break
        except:
            pass
        return(events)




    def search(self, terms, social=["fbk", "ins", "ytb"]):
        result={}
        #Search
        for soc in social:
            result[soc] = []
            for item in self.data[soc]:
                for term in terms:
                    if( re.search(term, item["title"], re.IGNORECASE) or re.search(term, item["desc"], re.IGNORECASE)):
                        result[soc].append(item)
        return(result)




    def searchAndChoose(self, terms, social=["fbk", "ins", "ytb"], max=1, rnd=False):
        items = self.search(terms, social)
        result={}
        for soc in social:
            result[soc] = []
            if rnd:
                if max == -1 or len(items[soc]) < max:
                    cmax = len(items[soc])
                else:
                    cmax = max
                indexes = random.sample(list(range(len(items[soc]))), cmax)
                for i in indexes:
                    result[soc].append(items[soc][i])
            else:
                for item in items[soc]:
                    result[soc].append(item)
                    if len(result[soc]) == max:
                        break
        return(result)




    def mix(self, data, social=["fbk", "ins", "ytb"]):
        result = []
        max = 0
        for soc in data.keys():
            if len(data[soc]) > max:
                max = len(data[soc])
        for i in list(range(max)):
            random.shuffle(social)
            for soc in social:
                try:    result.append(data[soc][i])
                except: pass
        return(result)