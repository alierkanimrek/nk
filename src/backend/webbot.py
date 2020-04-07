#!/usr/bin/python
# -*- coding: utf-8 -*-



import os
import glob
from lib import RssApp
from parts import Social
from lib import LOG



FacebookPosts_RSSAPP_URL = "https://rss.app/embed/v1/rmBj2GN3rS39NvvT"
Instagram_RSSAPP_URL = "https://rss.app/embed/v1/z3xerUfwq1l02wtu"
Youtube_RSSAPP_URL = "https://rss.app/embed/v1/Z5V5TP8jI03qGfve"






class Agent(object):




    def __init__(self, heap):
        self._heap = heap
        self._items = []
        self._log = LOG._.job("Social Agent")




    def update(self, url, count=0):
        self._items = []
        c=1
        #fb = RssApp(file="/home/ali/nk/src/backend/rss.app#embed#v1#rmBj2GN3rS39NvvT")
        rss = RssApp(url=url)
        rss.parse()
        for item in rss.items:
            if(c > count and count>0):
                break
            imgFn = self._get_img_name(item["url"])+".jpg"
            imgFullFn = self._heap+"/"+imgFn
            if not os.path.isfile(imgFullFn):
                rss.save_image(item["img"], imgFullFn)
            item["img"] = imgFn
            item["desc"] = self._clear_hashtags(item["desc"])
            self._items.append(item)
            c = c+1




    def _get_img_name(self, url):
        return(url.replace("/","").replace("?","").replace("&",""))




    def _clear_hashtags(self, desc):
        htflag = False
        result = ""
        for p in range(len(desc)):
            c = desc[p:p+1] 
            if c == "#":   htflag = True
            if htflag and c == " ": htflag = False

            if not htflag:
                result += c
        return(result.strip())




    @property
    def items(self):
        return(self._items)




    def clear_heap(self, imgs):
        for fn in glob.glob(self._heap+"/*.jpg"):
            if os.path.basename(fn) not in imgs:
                os.remove(fn)









def social_updater(heap, mode=["ins", "fbk", "ytb"]):
    items = {}
    ytb_items = []
    agent = Agent(heap)
    social = Social("tr-tr")
    items = social.data
    
    #Get posts
    if "ins" in mode:
        agent.update(Instagram_RSSAPP_URL,  1)
        items["ins"] = agent.items
    if "fbk" in mode:
        agent.update(FacebookPosts_RSSAPP_URL, 20)
        items["fbk"] = agent.items
    if "ytb" in mode:
        agent.update(Youtube_RSSAPP_URL, 20)
        for ytb_itm in agent.items:
            ytb_itm["desc"] = ""
            ytb_items.append(ytb_itm)
        items["ytb"] = ytb_items
    
    social.update(items)
    
    agent.clear_heap(social.imgs)








heap = "/home/ali/nk/src/server/heap/social"
#i = InstagramAgent("tr-tr")
#f = FacebookAgent("tr-tr")
#y = YoutubeAgent("tr-tr")
#i.up(heap)
#f.up(heap)
#y.up(heap)
social_updater(heap, ["ins"])

#social = Social("tr-tr")
#print(social.imgs)

