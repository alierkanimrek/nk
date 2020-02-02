#!/usr/bin/python
# -*- coding: utf-8 -*-

''' All rights reserved (c) 2018 Ali Erkan IMREK <alierkanimrek@gmail.com> '''


from .base import Parts

NAME = "glob"
TITLES = "titles"


class Glob(Parts):

    
    def __init__(self, lang:str, heap:str):
        super(Glob, self).__init__(fn=NAME, lang=lang)
        self.heap = heap
        img = self.choose(self.heap, NAME+"/"+self.data["background"]+"*")
        if(img):
            self.data["background"] = img        



    def title(self, template:str):
        return(self.data[TITLES][template])
