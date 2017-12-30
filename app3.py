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
import dropbox

import httplib2
import os
from apiclient import discovery

##############################################################
dbx = dropbox.Dropbox('f-KAniQltpAAAAAAAAAAJIbsiXs5GHwPExH3wvTg9HyW1TSWv90WITwbAiYWSOmS')
url_host = 'http://www.pixiv.net/'
url_login = 'https://accounts.pixiv.net/login'
url_post = 'https://accounts.pixiv.net/api/login'
headers_default = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'

    #'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24'
}
s = requests.Session()
    # 访问登陆页，获取Cookie和post_key
print('Visiting %s...' % url_login)
r = s.get(url_login, headers=headers_default)

print('Done結束.')
#print('Cookie:', s.cookies)
soup = BeautifulSoup(r.text, "html.parser")
post_key = soup.find(id="old-login").find(attrs={'name': 'post_key'}).get('value')
#print('post_key:', post_key)

# 登陆
data_post = {
        'mode': 'login',
        'pixiv_id': 'a2304101',
        'password': 'johnny782',
        'post_key': post_key
}
print('Logining中...')

r = s.post(url_post, data=data_post, headers=headers_default)
        
def DownloadFile(referer):
        referer2='https://www.pixiv.net/member_illust.php?mode=medium&illust_id='+referer
        #dir_='D:/Dropbox/pixiv2/'+keyword+'/'
        dir2_='/pixiv3/'
        '''
        try:
            if not os.path.exists(dir_):
                os.mkdir(dir_)
            elif os.path.isfile(dir_):
                raise Exception("failed to create directory '%s'" % dir_)
        except:
                print('mkdir造成失敗')
        '''
        indent='\t'
        headers = headers_default.copy()
        headers['Referer'] = referer2
    
    
        try:
            
            r = s.get(referer2,headers=headers_default)    
        
            
            findx=re.findall('https://i.pximg.net/img-original(.*?)"', r.text)
            #print(referer2)
            url= ( 'https://i.pximg.net/img-original'+findx[0])
            #print(referer2)
            #print(url)
            #dir_='PixivBookmarkCrawler/'       
            #file = dir_+str(rank)+'-'+ str(referer)+'-'+star+'.jpg'
            #file = dir_+star+'-'+str(referer)+'.jpg'
            #print('%sdownloading' % indent, file)
            r = s.get(url, headers=headers)
            

            file_to = dir2_+ str(referer)+'.jpg'
            #file_to = dir2_+star+'-'+url[len(url)-15:len(url)-7]+'-'+'.jpg'
            #file_to = url[len(url)-15:len(url)-7]+'.jpg'
            #print(url[len(url)-15:len(url)-7])
        
            x_time = time.time()
            dbx.files_upload(r.content, file_to)
            y_time = time.time()
            #print(y_time-x_time)

            x_time = time.time()
            link = dbx.sharing_create_shared_link(file_to)            
            url = link.url
            y_time = time.time()
            #print(y_time-x_time)
            
            return (url[0:len(url)-4]+'raw=1')
            #Write(file, r.content)
            print(y_time-x_time)
        except:
            print('失敗到album')
       
        
            #result = dbx.files_get_temporary_link('/'+url[len(url)-15:len(url)-7]+'.jpg')
            #link = dbx.sharing_create_shared_link('/'+str(rank)+'-'+ url[len(url)-15:len(url)-7]+'-'+star+'.jpg')
            #url = link.url
            #print(url[0:len(url)-4]+'raw=1')
   
            #print('/'+url[len(url)-15:len(url)-7]+'.jpg')
            #print('%sdone' % indent)
            #return str(url[0:len(url)-4]+'raw=1')


##############################################################
from flask import Flask, request, abort

from linebt2 import (
    LineBotApi, WebhookHandler
)
from linebt2.exceptions import (
    InvalidSignatureError
)
from linebt2.models import *

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
        line_bot_api.push_message(event.source.user_id,TextSendMessage(text='吃屎'),data1=None)
        line_bot_api.push_message(event.source.user_id,TextSendMessage(text='吃屎'))
        line_bot_api.push_message(event.source.user_id,ImageSendMessage('https://mega.nz/#!IIQk3ZCA!FLOQH30n53FpYxIwNhu2jabQgurqjM8Q_nD92hslQ6w','https://mega.nz/#!IIQk3ZCA!FLOQH30n53FpYxIwNhu2jabQgurqjM8Q_nD92hslQ6w'))
        
        return 0
    if event.message.text=='11':
        x_time = time.time()
        keyword='オリジナル'
        r = s.get("https://www.pixiv.net/search.php?word="+keyword+"&s_mode=s_tag_full&order=popular_male_d&mode=r18&p="+str(random.choice([1,2,3])))
        link_list = re.findall('stId&quot;:&quot;(.*?)&quot', r.text)
        x=DownloadFile(random.choice(link_list))
        y_time = time.time()
        line_bot_api.push_message(event.source.user_id,TextSendMessage(text=str(y_time-x_time)))
        line_bot_api.push_message(event.source.user_id,ImageSendMessage(x,x))
        return 0
    if event.message.text.lower().startswith('gooi-',0,len(event.message.text))==1: 
        ss=googlei(event.message.text[5:],1)
        for i in range(0,3):
            line_bot_api.push_message(event.source.user_id,ImageSendMessage(original_content_url=ss[i],preview_image_url=ss[i]))
        return 0
    if event.message.text.lower().startswith('gooil-',0,len(event.message.text))==1: 
        ss=googlei(event.message.text[6:],2)
        for i in range(0,3):
            line_bot_api.push_message(event.source.user_id,ImageSendMessage(original_content_url=ss[i],preview_image_url=ss[i]))
        return 0
    if event.message.text.lower().startswith('gooim-',0,len(event.message.text))==1: 
        ss=googlei(event.message.text[6:],3)
        #image_message = ImageSendMessage(original_content_url=ss[0],preview_image_url=ss[0])
        for i in range(0,3):           
            line_bot_api.push_message(event.source.user_id,ImageSendMessage(original_content_url=ss[i],preview_image_url=ss[i]))       
        return 0
    if event.message.text.lower().startswith('gooih-',0,len(event.message.text))==1: 
        ss=googlei(event.message.text[6:],4)
        for i in range(0,3):           
            line_bot_api.push_message(event.source.user_id,ImageSendMessage(original_content_url=ss[i],preview_image_url=ss[i]))
        return 0
    if event.message.text.lower().startswith('goo-',0,len(event.message.text))==1:    
        #line_bot_api.reply_message(event.reply_token,TextSendMessage(text=googles(event.message.text[4:])))
        line_bot_api.push_message(event.source.user_id,TextSendMessage(text=googles(event.message.text[4:])))
        return 0

import os
if __name__ == "__main__":
    app.run(host='0.0.0.0',port=os.environ['PORT'])
