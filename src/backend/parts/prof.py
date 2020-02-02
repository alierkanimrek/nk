#!/usr/bin/python
# -*- coding: utf-8 -*-

''' All rights reserved (c) 2018 Ali Erkan IMREK <alierkanimrek@gmail.com> '''


from .base import Parts


NAME = "prof"




class Prof(Parts):

    
    def __init__(self, lang:str, heap:str):
        super(Prof, self).__init__(fn=NAME, lang=lang)
        self.heap = heap
        self._placePics()




    def _placePics(self):
        for prf in self.data:
            img = self.choose(self.heap, NAME+"/"+self.data[prf]["id"]+"*.jpg")
            if(img):
                self.data[prf]["img"] = img