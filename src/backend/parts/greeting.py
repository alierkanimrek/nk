#!/usr/bin/python
# -*- coding: utf-8 -*-

''' All rights reserved (c) 2018 Ali Erkan IMREK <alierkanimrek@gmail.com> '''


from .base import Parts

NAME = "greeting"



class Greeting(Parts):

    
    def __init__(self, lang:str, heap:str):
        super(Greeting, self).__init__(fn=NAME, lang=lang)
        self.heap = heap
        img = self.choose(self.heap, NAME+"/"+self.data["picture"]+"*.jpg")
        if(img):
            self.data["picture"] = img