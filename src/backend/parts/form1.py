#!/usr/bin/python
# -*- coding: utf-8 -*-

''' All rights reserved (c) 2018 Ali Erkan IMREK <alierkanimrek@gmail.com> '''


from .base import Parts
import random







NAME = "form1"
IGNORE = ["Yayınlama", "yayınlama"]




class Form1Data:
    def __init__(self):
        self.titles = []
        self.comments = []




class Form1Comment:
    def __init__(self, comment=[]):
        self.time = ""
        self.client = ""
        self.vote = ""
        self.type = ""
        self.comment = ""
        self.nickname = ""
        self.who = ""
        self.approval = ""

        try:        
            self.time = comment[0]
            self.client = comment[1]
            self.vote = comment[2]
            self.type = comment[3]
            self.comment = comment[4]
            self.nickname = comment[5]
            self.who = ""
            self.approval = comment[7]
        except:
            pass








class Form1(Parts):

    
    def __init__(self, lang:str):
        super(Form1, self).__init__(fn=NAME, lang=lang)
        self.formdata = Form1Data()
        self.formdata.titles = self.data["titles"]
        self.random = Form1Comment()
        self.last = Form1Comment()
        for comment in self.data["comments"]:
            com = Form1Comment(comment)
            self.formdata.comments.append(com)
        if len(self.formdata.comments) > 2:
            self.last = self.formdata.comments[len(self.formdata.comments)-1]
        elif len(self.formdata.comments) == 1:
            self.last = self.formdata.comments[0]
        self.choose()




    async def update(self, titles, items):
        new_items = Form1Data()
        new_items.titles = titles
        changed = False
        c = 0
        for item in items:
            if item[7] not in IGNORE:
                new_items.comments.append(item)
            try:
                if item != self.data["comments"][c]:    changed = True
            except: changed = True
            c += 1
        if changed:
            self.save(vars(new_items))




    def choose(self):
        rnd = Form1Comment()
        if len(self.formdata.comments) > 2:
            rnd = self.formdata.comments[random.randrange(len(self.formdata.comments)-1)]
        elif len(self.formdata.comments) == 1:
            rnd = self.formdata.comments[0]
        self.random = rnd
        return(rnd)