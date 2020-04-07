#!/usr/bin/python
# -*- coding: utf-8 -*-



class LetGlobal:
    #Make someting global

    def __init__(self, default=None):
        self.__ = default

    @property
    def _(self):
        return(self.__)
    
    @_.setter
    def _(self, logger):
        self.__ = logger
