#!/usr/bin/python
# -*- coding: utf-8 -*-



import os
import glob
from lib import InstagramPage, FacebookPage, YoutubeVideos, GForm, BloggerAtom, InstagramAPIMedia
from parts import Social, Form1, Blogger
from lib import LOG




InstagramPageURL = "https://instagram.com/pranik_arhat"
FacebookPageURL = "https://facebook.com/antalyapraniksifa/posts"
YoutubeVideosURL = "https://www.youtube.com/channel/UCqeqZ7VC4TXdDSaHB9gh2ow/videos"
GForm1TSVURL = "https://docs.google.com/spreadsheets/d/1nEz_9Kqz0g86uSTxzggwS3--GjpiKb9V4xP0ISEZJZM/export?format=tsv&id=1nEz_9Kqz0g86uSTxzggwS3--GjpiKb9V4xP0ISEZJZM&gid=779288960"
BloggerAtomURL = "https://antalyapraniksifa.blogspot.com/feeds/posts/default/"
InstagramAPIMediaURL = "https://graph.instagram.com/me/media?fields=id,caption,media_url,thumbnail_url,permalink,timestamp&access_token="






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









async def social_updater(heap, instagram_access_token="", mode=["ins", "fbk", "ytb", "gf1", "blg"]):
    items = {}
    ytb_items = []
    agent = Agent(heap)
    social = Social("tr-tr")
    form1 = Form1("tr-tr")
    blogger = Blogger("tr-tr")
    items = social.data
    
    #Get posts
    if "ins" in mode:
        parser = InstagramAPIMedia(InstagramAPIMediaURL+instagram_access_token)
        await parser.arender()
        await agent.update(parser)
        if agent.items: items["ins"] = agent.items
    if "fbk" in mode:
        parser = FacebookPage(FacebookPageURL)
        await parser.arender()
        await agent.update(parser)
        if agent.items: items["fbk"] = agent.items
    if "ytb" in mode:
        parser = YoutubeVideos(YoutubeVideosURL)
        await parser.arender()
        await agent.update(parser)
        if agent.items: items["ytb"] = agent.items    
    if "gf1" in mode:
        parser = GForm(GForm1TSVURL)
        await parser.aload()
        if parser.items:   await form1.update(parser.titles, parser.items)
    if "blg" in mode:
        parser = BloggerAtom(BloggerAtomURL)
        await parser.aload()
        if parser.entries:   await blogger.update(parser.entries)

        
    social.update(items)
    
    await agent.clear_heap(social.imgs)












async def test():
    import logging
    from lib import KBLogger
    log = KBLogger("test.log")
    log.level = "DEBUG"
    LOG._ = log

    heap = "/home/ali/nk/src/server/heap/social"

    await social_updater(heap, instagram_access_token, mode=["ins"])
    ioloop.IOLoop.instance().stop()


#fn="antalyapraniksifa.blogspot.com#feeds#posts#default#"
#instagram_access_token="IGQVJYMURJLWN0eUhoOXhxTXpkazloT3JMOHhBSkZAoWVJibEtyV1J2RUlSdjd4VWV1ZATZAHVFROUW9tRURJNGx6QWpmOE15SWN1U0ZA3NDBPSkdDaG5LS0h1ZA0tBUUtsRVNTVHpHaVR4STFjOS1PYWIxLQZDZD"
#from tornado import ioloop
#loop = loop = ioloop.IOLoop.instance()
#loop.add_callback(test)
#loop.start()