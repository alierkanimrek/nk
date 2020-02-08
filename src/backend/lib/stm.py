#!/usr/bin/python
# -*- coding: utf-8 -*-

''' All rights reserved (c) 2018 Ali Erkan IMREK <alierkanimrek@gmail.com> '''








import time








class STM(object):
    """
    Short Term Memory
    """



    def __init__(self, lifetime=30):
        """
        lifetime = second
                    zero means no lifetime
        
        self._set = {time : {id, id,...}, time : ...}

        self._dellist = [time, time,...]
        """
        #super(IdSet, self).__init__()
        self.lifetime = lifetime
        self._set = dict()
        self._dellist = []




    def add(self,id, t=None):
        if not t:    t=int(time.time())
        else:   t=int(t)
        if not self.isThere(id, t, forAdd=True):
            try:
                self._set[int(t)].add(id)
            except KeyError:
                self._set[int(t)] = set({id})




    def isThere(self, id, t=None, forAdd=False):
        if not t:    t=int(time.time())
        else:   t=int(t)
        for s in self._set.keys():
            #print(t, s)
            #if t - self.lifetime > s and self.lifetime > 0: Zero Fix
            if t - self.lifetime > s and s not in self._dellist:
                self._dellist.append(s)
            else:
                if id in self._set[s]:
                    if t - self.lifetime == s and forAdd:
                        break
                    return(True)
        self._del()
        return(False)




    def whichTime(self, id):
        for s in sorted(self._set.keys(), reverse=True):
            if id in self._set[s]:
                return(s)
        return(False)




    def _del(self):
        for s in self._dellist:
            try:    del self._set[s]
            except: pass
        self._dellist = []




    def count(self, t=None):
        if not t:    t=int(time.time())
        else:   t=int(t)
        self._del()
        l = []
        for s in self._set.keys():
            if t - self.lifetime > s:
                self._dellist.append(s)
            else:
                for k in self._set[s]:
                    if k not in l:
                        l.append(k)
        return(len(l))




"""a = STM(2)

for i in range(0,10):
    a.add(i)

for i in range(10,20):
    a.add(i, time.time())
time.sleep(1)
for i in range(20,30):
    a.add(i, time.time())

time.sleep(1)

for i in range(40,50):
    a.add(i, time.time())

for i in range(0,30):
    print(a.isThere(i))

print(a.count())
"""