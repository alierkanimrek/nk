#!/usr/bin/python
# -*- coding: utf-8 -*-

''' All rights reserved (c) 2018 Ali Erkan IMREK <alierkanimrek@gmail.com> '''


from .base import Parts


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
                if item["desc"] != "":
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
    