#!/usr/bin/python
# -*- coding: utf-8 -*-



import os
import glob
from lib import InstagramPage, FacebookPage
from parts import Social
from lib import LOG




InstagramPageURL = "https://instagram.com/pranik_arhat"
FacebookPageURL = "https://facebook.com/antalyapraniksifa/posts"








class Agent(object):




    def __init__(self, heap):
        self._heap = heap
        self._items = []
        self._log = LOG._.job("Social Agent")




    async def update(self, parser, count=0):
        self._items = []
        c=1
        for item in parser.items:
            if(c > count and count>0):
                break
            imgFn = self._get_img_name(item["url"])[:200]+".jpg"
            imgFullFn = self._heap+"/"+imgFn
            if not os.path.isfile(imgFullFn):
                await parser.save_image(item["img"], imgFullFn)
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




    async def clear_heap(self, imgs):
        for fn in glob.glob(self._heap+"/*.jpg"):
            if os.path.basename(fn) not in imgs:
                os.remove(fn)









async def social_updater(heap, mode=["ins", "fbk", "ytb"]):
    items = {}
    ytb_items = []
    agent = Agent(heap)
    social = Social("tr-tr")
    items = social.data
    
    #Get posts
    if "ins" in mode:
        parser = InstagramPage(InstagramPageURL, save=True)
        await parser.arender()
        await agent.update(parser,  1)
        items["ins"] = agent.items
    if "fbk" in mode:
        parser = FacebookPage(FacebookPageURL)
        await parser.arender()
        await agent.update(parser)
        items["fbk"] = agent.items
    if "ytb" in mode:
        agent.update(Youtube_RSSAPP_URL, 20)
        for ytb_itm in agent.items:
            ytb_itm["desc"] = ""
            ytb_items.append(ytb_itm)
        items["ytb"] = ytb_items
    
    social.update(items)
    
    await agent.clear_heap(social.imgs)












async def test():
    import logging
    from lib import KBLogger
    log = KBLogger("test.log", "nk")
    log.level = "DEBUG"
    LOG._ = log

    heap = "/home/ali/nk/src/server/heap/social"
    fn="/home/ali/nk/src/backend/instagram.com#pranik_arhat"

    await social_updater(heap, ["ins"])
    ioloop.IOLoop.instance().stop()


#from tornado import ioloop
#loop = loop = ioloop.IOLoop.instance()
#loop.add_callback(test)
#loop.start()