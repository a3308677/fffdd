#!/usr/bin/env python3
# -*- coding: utf8 -*-

from selenium import webdriver
import urllib.parse
from bs4 import BeautifulSoup
import requests
import sys
import lxml
import urllib.request
from urllib.parse import urlencode
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
import json
import os
import time
import simplejson
import time
import logging
import urllib.request
import urllib.error
from urllib.parse import urlparse
import random
from multiprocessing import Pool
from user_agent import generate_user_agent
from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
import re
import logging
import multiprocessing

import httplib2
import os
from apiclient import discovery



from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

app = Flask(__name__)

line_bot_api = LineBotApi('1SmGKlg59CG8VNJQFGSRoHhUbbbtYnyoePC0S3DfEbZkYS0kKfueCEYNQz6L/zPbywLbATf1H6BAWnr+K2Ii5U8Bf5JddLN8LklJ/E74wgS6LP3I4cYTEeNVIPE2vu79qBdsaIwxRfzlkFocAWmIzAdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('9f40c12980e63edb3732a2f7aa4ea7a2')


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

def googles(query):
    query2=urllib.parse.quote_plus(query)
    tStart = time.time()
    url = "https://www.google.com.tw/search?hl=zh-TW&q="+query2+"&meta=&aq=f&oq=%22"
    #url = "https://www.google.com/search?q=%E4%BA%9E%E8%8E%89%E4%BA%9E&source=lnms&tbm=isch"
    log_file = 'download.log'
    logging.basicConfig(level=logging.DEBUG, filename=log_file, filemode="a+", format="%(asctime)-15s %(levelname)-8s  %(message)s")


    headers = {}
    headers['User-Agent'] = generate_user_agent()
    headers['Referer'] = 'https://www.google.com'
    req = urllib.request.Request(url, headers = headers)
    resp = urllib.request.urlopen(req)
       
    page_content = str(resp.read())

    L = ['', '', '', '', '', '']
    L2 = ['', '', '', '', '', '']
    L3 = ''
    #a1 = '\xe7\xb7\x8b\xe5\xbd\x88\xe7\x9a\x84\xe4\xba\x9e\xe8\x8e\x89\xe4\xba\x9e- \xe7\xbb\xb4\xe5\x9f\xba\xe7\x99\xbe\xe7\xa7\x91\xef\xbc\x8c\xe8\x87\xaa\xe7\x94\xb1\xe7\x9a\x84\xe7\x99\xbe\xe7\xa7\x91\xe5\x85\xa8\xe4\xb9\xa6'
    s5=0;s3=0;s4=0;
    i = 0
    while i < 5:
        s3 = page_content.index('<h3 class="r"><a href="',0+s5,len(page_content))
        s4 = page_content.index('"', s3+24,len(page_content))
        L2[i]=page_content[s3+23:s4]
    
        s3=page_content.index('</a></h3>', s4,len(page_content))
        s4=page_content.rindex('event)">',s4 ,s3)

        L[i]=page_content[s4+8:s3]
        c = bytearray()
        c.extend(map(ord, L[i]))
        c4=c.decode('unicode_escape')

        b5 = bytearray()
        b5.extend(map(ord, c4))
        L[i]=b5.decode('utf-8')
        
        s5=s4
        i+=1 
    L3=(L[0]+'\n'+L2[0]+'\n'+'\n'+L[1]+'\n'+L2[1]+'\n'+'\n'+L[2]+'\n'+L2[2]+'\n'+'\n'+L[3]+'\n'+L2[3]+'\n'+'\n'+L[4]+'\n'+L2[4])    
    return (L3)

#url = "https://www.google.com.tw/search?hl=zh-TW&q=%E4%BA%9E%E8%8E%89%E4%BA%9E&meta=&aq=f&oq=%22"
def googlei(query,n):

    query2=urllib.parse.quote_plus(query)
    if n==1: 
        url = "https://www.google.com/search?q="+query2+"&source=lnms&tbm=isch"
    if n==2:
        url = "https://www.google.com/search?q="+query2+"&tbs=isz:lt,islt:svga&tbm=isch&source=lnt"
    if n==3:
        url = "https://www.google.com/search?q="+query2+"&tbs=isz:lt,islt:xga&tbm=isch&source=lnt"
    if n==4:
        url = "https://www.google.com/search?q="+query2+"&tbs=isz:lt,islt:2mp&tbm=isch&source=lnt"
    log_file = 'download.log'
    logging.basicConfig(level=logging.DEBUG, filename=log_file, filemode="a+", format="%(asctime)-15s %(levelname)-8s  %(message)s")
    

    headers = {}
    headers['User-Agent'] = generate_user_agent()
    headers['Referer'] = 'https://www.google.com'
    req = urllib.request.Request(url, headers = headers)
    resp = urllib.request.urlopen(req)
       
    page_content = str(resp.read())

    if page_content:
        link_list = re.findall('"ou":"(.*?)"', page_content)
        if len(link_list) == 0:
            print('get 0 links from page {0}'.format(url))
            logging.info('get 0 links from page {0}'.format(url))
            
        else:
             set(link_list)
    else:
          set()

    link_list3= [None] * 100
    link_list4= [None] * 100
    i = 0
    for var in link_list:
        if var.endswith(".jpg",0,len(var)) or var.endswith(".png",0,len(var)) :
            link_list3[i]=var
            i+=1
    link_list3=list(filter(None, link_list3))  
    i = 0
    for var in link_list3:
        if var.startswith("https",0,len(var)):
            link_list4[i]=var
            i+=1

    x=list(filter(None, link_list4))    
    random.shuffle(x)    
    return x



@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    if event.message.text=='吃屎':        
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text='吃屎'))
        return 0
    if event.message.text=='11':    
        tt='https://dl.dropboxusercontent.com/content_link/fxUa4NG3YlKD2UlGM7TMA9dcj1M9DRGyjM0k2VOwpMEcReaUydn63UOzz0h1GK5N/file'
 
        line_bot_api.push_message(event.source.user_id,ImageSendMessage(original_content_url=tt,preview_image_url=tt))
        
        return 0
    if event.message.text.lower().startswith('gooi-',0,len(event.message.text))==1: 
        ss=googlei(event.message.text[5:],1)
        for i in range(0,3):
            line_bot_api.push_message(event.source.user_id,ImageSendMessage(original_content_url=ss[0],preview_image_url=ss[i]))
        return 0
    if event.message.text.lower().startswith('gooil-',0,len(event.message.text))==1: 
        ss=googlei(event.message.text[6:],2
        for i in range(0,3):
            line_bot_api.push_message(event.source.user_id,ImageSendMessage(original_content_url=ss[0],preview_image_url=ss[i]))
        return 0
    if event.message.text.lower().startswith('gooim-',0,len(event.message.text))==1: 
        ss=googlei(event.message.text[6:],3)
        #image_message = ImageSendMessage(original_content_url=ss[0],preview_image_url=ss[0])
        for i in range(0,3):           
            line_bot_api.push_message(event.source.user_id,ImageSendMessage(original_content_url=ss[0],preview_image_url=ss[i]))       
        return 0
    if event.message.text.lower().startswith('gooih-',0,len(event.message.text))==1: 
        ss=googlei(event.message.text[6:],4)
        for i in range(0,3):           
            line_bot_api.push_message(event.source.user_id,ImageSendMessage(original_content_url=ss[0],preview_image_url=ss[i]))
        return 0
    if event.message.text.lower().startswith('goo-',0,len(event.message.text))==1:    
        #line_bot_api.reply_message(event.reply_token,TextSendMessage(text=googles(event.message.text[4:])))
        line_bot_api.push_message(event.source.user_id,TextSendMessage(text=googles(event.message.text[4:])))
        return 0

import os
if __name__ == "__main__":
    app.run(host='0.0.0.0',port=os.environ['PORT'])
