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
import os
import numpy as np
from googletrans import Translator
####################################################
CLIENT_ID = "db49815c92fde22c57d3c90bafbb37f8"
CLIENT_SECRET = "6ed79ebec4103a1e0da7f201d3356a80"
from kkbox_developer_sdk.auth_flow import KKBOXOAuth
auth = KKBOXOAuth(CLIENT_ID, CLIENT_SECRET)
token = auth.fetch_access_token_by_client_credentials()

from kkbox_developer_sdk.api import KKBOXAPI
kkboxapi = KKBOXAPI(token)
####################################################
print(os.environ['PORT'])
print(type(os.environ['PORT']))
print(int(os.environ['PORT']))
##############################################################
headerslist=['https://www.google.com','https://www.google.co.jp','https://www.google.co.uk','https://www.google.es',
             'https://www.google.ca','https://www.google.com.tw','https://www.google.com.au','https://www.google.co.kr',
             'https://www.google.de','https://www.google.it','https://www.google.fr','https://www.google.com.tr',
             'https://www.google.be','https://www.google.com.gr','https://www.google.co.in','https://www.google.com.mx',
             'https://www.google.dk','https://www.google.com.ar','https://www.google.ch','https://www.google.cl',
             'https://www.google.at','https://www.google.ie','https://www.google.com.co','https://www.google.pl',
             'https://www.google.pt','https://www.google.com.pk','https://www.google.cn','https://www.google.com.my',
             'https://www.google.com.sg','https://www.google.com.af','https://www.google.jo','https://www.google.co.il',
             'https://www.google.com.lb','https://www.google.is','https://www.google.no','https://www.google.se',
             'https://www.google.lt','https://www.google.lu','https://www.google.gr','https://www.google.ru',
             'https://www.google.com.by','https://www.google.gy','https://www.google.co.cr','https://www.google.bs','https://www.google.com.cu']

#dbx = dropbox.Dropbox('f-KAniQltpAAAAAAAAAAJIbsiXs5GHwPExH3wvTg9HyW1TSWv90WITwbAiYWSOmS')
url_host = 'http://www.pixiv.net/'
url_login = 'https://accounts.pixiv.net/login'
url_post = 'https://accounts.pixiv.net/api/login'
headers_default = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'

    #'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24'
}
#########
'''
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
'''
##############################################################
def output(z):
    #artist_fetcher.fetch_top_tracks_of_artist
    #search_fetcher.search
    name=[]
    songurl=[]
    image=[]
    last=0
    z=str(z)
    while 'duration' in z:
        try:
            print('對')
            index1 =z.index('duration',last,len(z))
            index2 =z.rindex('name',0,index1)
            name+=[z[index2+8:index1-4]]
            index3=z.index('url',index1,len(z))
            index4=z.index('\'',index3+7,len(z))
            songurl+=[z[index3+7:index4]]

            index5=z.index('images',index4,len(z))
            index6=z.index(']',index5+10,len(z))

            index7=z.rindex('url',index5+10,index6)
            index8=z.index('\'',index7+7,index6)
            image+=[z[index7+7:index8]]

            last=index6
        except:
            break
    print(name)
    print(songurl)
    print(image)
    return [name,songurl,image]

def songview(songurl):
    resp = requests.get(songurl)
    fin3=re.findall('music:preview_url:url" content="(.*?)"', resp.text)
    return fin3[0]

def output2(z):
    #album_fetcher.fetch_tracks_in_album
    name=[]
    songurl=[]
    last=0
    z=str(z)
    while 'duration' in z:
        try:
            print('對')
            index1 =z.index('duration',last,len(z))
            index2 =z.rindex('name',0,index1)
            name+=[z[index2+8:index1-4]]
            index3=z.index('url',index1,len(z))
            index4=z.index('\'',index3+7,len(z))
            songurl+=[z[index3+7:index4]]
            last=index4
        except:
            break
    print(name)
    print(songurl)
    return [name,songurl]


def artist(z):
    #search
    name=[]
    id=[]
    last=0
    z=str(z)
    while '\'artist\'' in z:
        try: 
            index1 =z.index('\'artist\'',last,len(z))
            index2 =z.index('id',index1,len(z))
            index3 =z.index('\'',index2+6,len(z))
            id+=[z[index2+6:index3]]
            index4 =z.index('name',index3,len(z))
            index5 =z.index('\'',index4+8,len(z))
            name+=[z[index4+8:index5]]
            last=index5
        except:
            break
    print(len(name),len(id))
    name2=[]
    id2=[]
    for i in range(0,len(id)):
        if id[i] not in id2:
            id2+=[id[i]]
            name2+=[name[i]]

    print(name2)
    print(id2)
    return [name2,id2]

def getalbum(z):
    #artist_fetcher.fetch_albums_of_artist
    name=[]
    id=[]
    last=0
    image=[]
    z=str(z)
    
    while 'available_territories' in z:
        try:
            index1 =z.index('available_territories',last,len(z))
            index2 =z.index(']',index1+25,len(z))
            if 'tw' in z[index1+25:index2].lower():
                index3=z.rindex('id',0,index1)
                index4=z.rindex('name',index3+6,index1)
                id+=[z[(index3+6):(index4-4)]]
                
                index5=z.rindex('name',index4,index1)
                index6=z.rindex('url',index5+8,index1)
                name+=[z[(index5+8):(index6-4)]]
                
                index7=z.index('images',index2,len(z))
                index8=z.index(']',index7+10,len(z))

                index9=z.rindex('url',index7+10,index8)
                index10=z.index('\'',index9+7,index8)
                image+=[z[index9+7:index10]]
                
            last=index2
        except:
            break
    print(len(name),len(id),len(image))
    
    return [name,id,image]    
  
def peoplesearch(input):
    
    itemnum=0
    initial=input.rindex(')')
    keyword=input[:initial]

    for v in input[initial+1:]:
        if v=='.':
            itemnum+=1
    
    z=kkboxapi.search_fetcher.search(keyword)
    [name2,id2]=artist(z)
    if itemnum==0:
        return name2
    if itemnum==1:
        artistindex=input.index('.',initial+1,len(input))
        artistnum=int(input[artistindex+1:])

        z2=kkboxapi.artist_fetcher.fetch_albums_of_artist(id2[artistnum-1])
        [name3,id3,image]=getalbum(z2)
        return name3
    if itemnum==2:
        artistindex=input.index('.',initial+1,len(input))
        artistindex2=input.rindex('.',initial+1,len(input))
        artistnum=int(input[artistindex+1:artistindex2])
        albumnum=int(input[artistindex2+1:])

        z2=kkboxapi.artist_fetcher.fetch_albums_of_artist(id2[artistnum-1])
        [name3,id3,image]=getalbum(z2)
        
        z3=kkboxapi.album_fetcher.fetch_tracks_in_album(id3[albumnum-1])
    
        [name4,songurl]=output2(z3)
        return name4
    if itemnum==3:
        artistindex=input.index('.',initial+1,len(input))
        artistindex2=input.index('.',artistindex+1,len(input))
        artistindex3=input.rindex('.',initial+1,len(input))

        artistnum=int(input[artistindex+1:artistindex2])
        albumnum=int(input[artistindex2+1:artistindex3])
        songnum=int(input[artistindex3+1:])

        z2=kkboxapi.artist_fetcher.fetch_albums_of_artist(id2[artistnum-1])
        [name3,id3,image]=getalbum(z2)
        
        z3=kkboxapi.album_fetcher.fetch_tracks_in_album(id3[albumnum-1])
    
        [name4,songurl]=output2(z3)
        
        z4=songview(songurl[songnum-1])
        print(z4,image[albumnum-1],songurl[songnum-1],name4[songnum-1])
        return [z4,image[albumnum-1],songurl[songnum-1],name4[songnum-1]]

def hotsearch(input):
    itemnum=0
    initial=input.rindex(')')
    keyword=input[:initial]

    for v in input[initial+1:]:
        if v=='.':
            itemnum+=1
    
    z=kkboxapi.search_fetcher.search(keyword)
    [name2,id2]=artist(z)
    if itemnum==0:
        return name2
    if itemnum==1:
        artindex=input.index('.',initial+1,len(input))
        artnum=int(input[artindex+1:])

        c=kkboxapi.artist_fetcher.fetch_top_tracks_of_artist(id2[artnum-1])
        [name,songurl,image]=output(c)
        return name
    if itemnum==2:
        artistindex=input.index('.',initial+1,len(input))
        artistindex2=input.rindex('.',initial+1,len(input))
        artistnum=int(input[artistindex+1:artistindex2])
        songnum=int(input[artistindex2+1:])

        c=kkboxapi.artist_fetcher.fetch_top_tracks_of_artist(id2[artistnum-1])
        [name,songurl,image]=output(c)

        z4=songview(songurl[songnum-1])
        return [z4,name[songnum-1],songurl[songnum-1],image[songnum-1]]

def songsearch(input):
    itemnum=0
    initial=input.rindex(')')
    keyword=input[:initial]

    for v in input[initial+1:]:
        if v=='.':
            itemnum+=1
    
    z=kkboxapi.search_fetcher.search(keyword)
    [name,songurl,image]=output(z)
    print(len(name),len(songurl),len(image))
    if itemnum==0:
        return name
    if itemnum==1:
        artistindex=input.index('.',initial+1,len(input))
        artistnum=int(input[artistindex+1:])
        
        z4=songview(songurl[artistnum-1])
        return [z4,name[artistnum-1],songurl[artistnum-1],image[artistnum-1]]
##########################################################################
def pixivsearch(string):
    try:   
        url='https://www.pixiv.net/search.php?s_mode=s_tag&order=popular'
        string=(string+'-').lower()
        keyword=(re.findall('p-s(.*?)-', string))[0]
            
        sex=re.findall('-g(.*?)-', string[3+len(keyword):])
        if sex==['b']:
            url=url+'_male'
        if sex==['g']:
            url=url+'_female'
        url=url+'_d'

        r18=re.findall('-r(.*?)-', string[3+len(keyword):])
        if r18==['18']:    
            url=url+'&mode=r18'
        if r18==['n18']:        
            url=url+'&mode=safe'
        url=url+'&word='+keyword+'&p='

        page=re.findall('-p(.*?)-', string[3+len(keyword):])
        if page!=[]: 
            url=url+page[0]
        if page==[]:
            url=url+str(random.choice([1,2,3]))

        item=re.findall('-i(.*?)-', string[3+len(keyword):])
        if item!=[]:
            item=item[0]
        
        #url='https://www.pixiv.net/search.php?s_mode=s_tag&order=popular'+sex+'_d'+r18+'&word='+keyword+'&p='+page
        return [url,item]
    except: 
        return [0,0]    
def itemsellectid(url,item):
    try: 
        r = s.get(url)
        link_list = re.findall('stId&quot;:&quot;(.*?)&quot', r.text)
        
        if item!=[]:
            return link_list[int(item)-1]
        else:
            return random.choice(link_list)
    except:
        return '0'

def resulturl(itemsellect):
    try:
        resulturl=[]
        url2='https://www.pixiv.net/member_illust.php?mode=medium&illust_id='+itemsellect
        r2 = s.get(url2)
        manypage=re.findall('一次性投稿多張作品 (.*?)P', r2.text)
        if manypage==[]:
            resulturl+=['https://pixiv.cat/'+itemsellect+'.jpg']
        if manypage!=[]:
            if int(manypage[0])<3:
                resulturl+=['https://pixiv.cat/'+itemsellect+'-1.jpg','https://pixiv.cat/'+itemsellect+'-2.jpg']
            if int(manypage[0])>=3:
                for i in range(0,3):
                    resulturl+=['https://pixiv.cat/'+itemsellect+'-'+str(i+1)+'.jpg']
        return resulturl
    except:
        return '0'
    
def imageid(string):
    try:
        string=string.lower()
        number=0
        for v in string:
            if v=='-':
                number+=1
        if number==0:
            itemsellect=string
            resulturl=[]
            url2='https://www.pixiv.net/member_illust.php?mode=medium&illust_id='+itemsellect
            r2 = s.get(url2)
            manypage=re.findall('一次性投稿多張作品 (.*?)P', r2.text)
            if manypage==[]:
                resulturl=['https://pixiv.cat/'+itemsellect+'.jpg']
            if manypage!=[]:
                if int(manypage[0])<=4:
                    for i in range(0,int(manypage[0])):
                        resulturl+=['https://pixiv.cat/'+itemsellect+'-'+str(i+1)+'.jpg']
                if int(manypage[0])>4:
                    for i in range(0,4):
                        resulturl+=['https://pixiv.cat/'+itemsellect+'-'+str(i+1)+'.jpg']
            return resulturl
        if number==1:
            return ['https://pixiv.cat/'+string+'.jpg']
    except:
        return '0'

def monthsearch(string4):
    try:
        string4=(string4+'-').lower()
        url='https://www.pixiv.net/ranking.php?mode=monthly&content=illust'
        r = s.get(url)
        link_list = re.findall('"illust"data-click-label="(.*?)"data-type', r.text)
        rank = re.findall('-n(.*?)-', string4)
        if rank!=[]:
            return link_list[int(rank[0])-1]
        if rank==[]:
            return random.choice(link_list)
    except:
        return 0
    
def weelsearch(string):
    try:
        string=(string+'-').lower()
        item=re.findall('-n(.*?)-', string)
        if item!=[]:
            item=item[0] 
        if '-r18g' in string:
            url='https://www.pixiv.net/ranking.php?mode=r18g'
            r = s.get(url)
            link_list = re.findall('"illust"data-click-label="(.*?)"data-type', r.text)
            if item!=[]:
                return link_list[int(item)-1]
            if item==[]:
                return random.choice(link_list)
        r18 = re.findall('-r(.*?)-', string)
        url='https://www.pixiv.net/ranking.php?mode=weekly'
        if r18!=[]:
            if r18[0]=='18':
                r18='_r18'
                url=url+r18 
        r = s.get(url)
        link_list = re.findall('"illust"data-click-label="(.*?)"data-type', r.text)
        if item!=[]:
            return link_list[int(item)-1]
        if item==[]:
            return random.choice(link_list)
    except:
        return 0
    
def todaysearch(string):
    try:
        string=string+'-'
        string=string.lower()
        item=re.findall('-n(.*?)-', string)
        if item!=[]:
            item=item[0]
        r18 = re.findall('-r(.*?)-', string)
        url='https://www.pixiv.net/ranking.php?mode=daily'
        if r18!=[]:
            if r18[0]=='18':
                r18='_r18'
                url=url+r18            
        r = s.get(url)
        link_list = re.findall('"illust"data-click-label="(.*?)"data-type', r.text)
        if item!=[]:
            return link_list[int(item)-1]
        if item==[]:
            return random.choice(link_list)
    except:
        return 0
    
def boysearch(string):
    try:
        string=string+'-'
        string=string.lower()
        item=re.findall('-n(.*?)-', string)
        if item!=[]:
            item=item[0]
        r18 = re.findall('-r(.*?)-', string)
        url='https://www.pixiv.net/ranking.php?mode=male'
        if r18!=[]:
            if r18[0]=='18':
                r18='_r18'
                url=url+r18
        r = s.get(url)
        link_list = re.findall('"illust"data-click-label="(.*?)"data-type', r.text)
        if item!=[]:
            return link_list[int(item)-1]
        if item==[]:
            return random.choice(link_list)
    except:
        return 0
    
def girlsearch(string):
    try:
        string=string+'-'
        string=string.lower()
        item=re.findall('-n(.*?)-', string)
        if item!=[]:
            item=item[0]
        r18 = re.findall('-r(.*?)-', string)
        url='https://www.pixiv.net/ranking.php?mode=female'
        if r18!=[]:
            if r18[0]=='18':
                r18='_r18'
                url=url+r18
        r = s.get(url)
        link_list = re.findall('"illust"data-click-label="(.*?)"data-type', r.text)
        if item!=[]:
            return link_list[int(item)-1]
        if item==[]:
            return random.choice(link_list)
    except:
        return 0
    
def intersearch(string):
    try:
        string=string+'-'
        string=string.lower()
        item=re.findall('-n(.*?)-', string)
        if item!=[]:
            item=item[0]
        url='https://www.pixiv.net/ranking_area.php?type=detail&no=6'
        
        r = s.get(url)
        link_list = re.findall('"illust"data-click-label="(.*?)"data-type', r.text)
        if item!=[]:
            return link_list[int(item)-1]
        if item==[]:
            return random.choice(link_list)
    except:
        return 0
##############################################################
from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

app = Flask(__name__)

line_bot_api = LineBotApi('hFmR9m9K3DCbmZfv6JvrrxN6C3D3wzhGrocfRV6609XMNhMCKYOdkbH1nHiJkc2QBf9Sm1Pz2636PLB4OuxFqxyTmiusaAiG2A1DtEkQMBiEAaFtHetisrSzn/xzt8lkXjpu1Lim53S/kw8UaFFUdgdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('27f59c8d97353a913431ec16b7753947')


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
    headers['Referer'] = np.random.choice(headerslist)
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
        #大於800*600像素
        url = "https://www.google.com/search?q="+query2+"&tbs=isz:lt,islt:svga&tbm=isch&source=lnt"
    if n==3:
        #大於1024*768像素
        url = "https://www.google.com/search?q="+query2+"&tbs=isz:lt,islt:xga&tbm=isch&source=lnt"
    if n==4:
        #大於1600*1200像素
        url = "https://www.google.com/search?q="+query2+"&tbs=isz:lt,islt:2mp&tbm=isch&source=lnt"
    log_file = 'download.log'
    logging.basicConfig(level=logging.DEBUG, filename=log_file, filemode="a+", format="%(asctime)-15s %(levelname)-8s  %(message)s")
    

    headers = {}
    headers['User-Agent'] = generate_user_agent()
    headers['Referer'] = np.random.choice(headerslist)
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

def youtubee(websearch,n):
    #websearch='雪之下'
    query2=urllib.parse.quote_plus(websearch)
    if n==1:
        #url='https://www.youtube.com/results?search_query='+query2+'&gl=TW'
        url='https://www.youtube.com/results?search_query='+query2
    if n==2:
        #上傳日期
        url='https://www.youtube.com/results?search_query='+query2+'&sp=CAI%253D'+'&gl=TW'
    if n==3:
        #觀看次數
        url='https://www.youtube.com/results?search_query='+query2+'&sp=CAM%253D'+'&gl=TW'

    print(url)
    log_file = 'download.log'
    logging.basicConfig(level=logging.DEBUG, filename=log_file, filemode="a+", format="%(asctime)-15s %(levelname)-8s  %(message)s")

    headers = {}
    headers['User-Agent'] = generate_user_agent()
    #headers['Referer'] = 'https://www.google.com.tw'
    #headers['Referer'] = 'http://www.google.co.jp'
    #rrrrrr=np.random.choice(headerslist)
    
    headers['Referer'] =np.random.choice(headerslist)
    req = urllib.request.Request(url, headers = headers)
    resp = urllib.request.urlopen(req) 
    content =  resp.read().decode(resp.headers.get_content_charset())
    #page_content = str(output.read())
    find3=[]
    find4=[]
    find5=[]
    find6=[]
    name=[]
    uploader=[]
    last1=0
    last2=0
    findidd=[]
    manyname=[]
    manyurl=[]
    manyid=[]
    endd=0
    itemcounter=0
    while '"title":{"accessibility":{"accessibilityData":{"label":"' or '{"playlistRenderer":{"playlistId":"' in content:
        if '"title":{"accessibility":{"accessibilityData":{"label":"' in content[last1:]:
            index1=content.index('"title":{"accessibility":{"accessibilityData":{"label":"',last1,len(content))
            #print(index1,'單有')
        if '"title":{"accessibility":{"accessibilityData":{"label":"' not in content[last1:]:    
            index1=float("inf")
            #print(index1,'單無')
        if '{"playlistRenderer":{"playlistId":"' in content[last2:]:
            index2=content.index('{"playlistRenderer":{"playlistId":"',last2,len(content))
            #print(index2,'多有')
        if '{"playlistRenderer":{"playlistId":"' not in content[last2:]:
            index2=float("inf")
            #print(index2,'多無')

        if index1!=[] and index2!=[]:
            if index1<index2:
                #print('index1<index2')

                indexnew1=content.index('"simpleText":"',index1,len(content))
                indexnew2=content.index('}',indexnew1+14,len(content))
                
                if len(content[indexnew1+14:indexnew2-1].replace('\\', ''))>40:
                    name+=[content[indexnew1+14:indexnew2-1].replace('\\', '')[:40]]
                if len(content[indexnew1+14:indexnew2-1].replace('\\', ''))<=40:     
                    name+=[content[indexnew1+14:indexnew2-1].replace('\\', '')]
                    
                indexnew3=content.index('shortBylineText":{"runs":[{"text":"',indexnew2,len(content))
                indexnew4=content.index('"',indexnew3+35,len(content))
                uploader+=[content[indexnew3+35:indexnew4].replace('\\', '')]

                #index3=content.index('}',index1+56,len(content))
                #find3+=[content[index1+56:index3].replace('\\', '')]
                index4=content.rindex('"thumbnail":{"thumbnails":[{"url":"',last1,index1)
                index5=content.index('"',index4+35,index1)
                find4+=[content[index4+35:index5].replace("\\u0026", "&amp;")]

                findidd+=['https://www.youtube.com/watch?v='+re.findall('https://i.ytimg.com/vi/(.*?)/', content[index4+35:index5])[0]]

                last1=indexnew4
                itemcounter+=1
                
            if index2<index1:
                #print('index1>index2')
                index6=content.index(']',index2+35,len(content))
                find5+=[content[index2+35:index6]]

                indexnew6=re.findall('"simpleText":"(.*?)}', content[index2+35:index6])[0]
                if len(indexnew6[0:len(indexnew6)-1].replace('\\', ''))>40:
                    name+=[indexnew6[0:len(indexnew6)-1].replace('\\', '')[:40]]
                if len(indexnew6[0:len(indexnew6)-1].replace('\\', ''))<=40:
                    name+=[indexnew6[0:len(indexnew6)-1].replace('\\', '')]

                indexnew7=re.findall('"url":"(.*?)"', content[index2+35:index6])
                find4+=[indexnew7[len(indexnew7)-1].replace("\\u0026", "&amp;")]

                findidd+=['https://www.youtube.com/watch?v='+re.findall('https://i.ytimg.com/vi/(.*?)/',indexnew7[len(indexnew7)-1])[0]]

                index7=content.index('shortBylineText":{"runs":[{"text":"',index2+35,len(content))
                index8=content.index('"',index7+35,len(content))                
                uploader+=[content[index7+35:index8]]
                last2=index8
                itemcounter+=1
        if itemcounter==10:
            break
        if index1==float("inf") and index2==float("inf"):
            print('結束')
            break
    
    print(['結']+name+[len(name)]+['結'])
    print(['結']+uploader+[len(uploader)]+['結'])
    print(['結']+find4+[len(find4)]+['結'])
    print(['結']+findidd+[len(findidd)]+['結'])
    '''
    print(['結']+find5+[len(find5)]+['結'])
    print(['結']+manyname+[len(manyname)]+['結'])
    print(['結']+manyid+[len(manyid)]+['結'])
    print(['結']+manyurl+[len(manyurl)]+['結'])
    print(['結']+find6+[len(find6)]+['結'])
    '''
    return [name,uploader,find4,findidd]
###################################################################
def qureyenglish(qureyinput,ss,n):
    try:
        sstarget=[]
        keyword2=[]
        if len(ss)>1:
            ss=ss[:1]
        if len(ss)>0:
            for page in range(0,len(ss)):
                resp = requests.get(ss[page])
                #find1=re.findall('<dt>(.*?)<span style="font-weight: normal;">（<span lang="ja" xml:lang="ja">',resp2text)
                #find2=re.findall('<span style="font-weight: normal;">（<span lang="ja" xml:lang="ja">(.*?)</span>',resp2text)
                last=0
                while '<span style="font-weight: normal;">（<span lang="ja" xml:lang="ja">' in resp.text[last:]:  
                    index1=resp.text.index('<span style="font-weight: normal;">（<span lang="ja" xml:lang="ja">',last,len(resp.text))
                    if '<dt>' in resp.text[last:index1]:
                        index2=resp.text.rindex('<dt>',last,index1)
                        keyword=resp.text[(index2+4):index1]
                        if n==2:
                            for char in range(0,len(qureyinput)):
                                if qureyinput[char].lower() in keyword.lower():
                                    #print('有字在裡面')
                                    if '</span>' in resp.text[(index1+66):]:
                                        index3=resp.text.index('</span>',index1+66,len(resp.text))
                                        if '<' not in resp.text[(index1+66):index3] and '>' not in resp.text[(index1+66):index3]:
                                            #print(resp.text[(index1+66):index3])
                                            keyword2+=[resp.text[(index1+66):index3]]
                        if n==1:
                            if qureyinput.lower() in keyword.lower():
                                if '</span>' in resp.text[(index1+66):]:
                                    index3=resp.text.index('</span>',index1+66,len(resp.text))
                                    if '<' not in resp.text[(index1+66):index3] and '>' not in resp.text[(index1+66):index3]:    
                                        #print(resp.text[(index1+66):index3])
                                        keyword2+=[resp.text[(index1+66):index3]]
                    last=index1+66

                #find3=re.findall('<dt>(.*?)<span style="font-weight: normal;">（<span lang="ja">',resp2text)
                #find4=re.findall('<span style="font-weight: normal;">（<span lang="ja">(.*?)</span>',resp2text)
                last=0
                while '<span style="font-weight: normal;">（<span lang="ja">' in resp.text[last:]:  
                    index1=resp.text.index('<span style="font-weight: normal;">（<span lang="ja">',last,len(resp.text))
                    if '<dt>' in resp.text[last:index1]: 
                        index2=resp.text.rindex('<dt>',last,index1)
                        keyword=resp.text[(index2+4):index1]
                        #print(keyword)
                        if n==2:
                            for char in range(0,len(qureyinput)):
                                if qureyinput[char].lower() in keyword.lower():
                                    #print('有字在裡面')
                                    if '</span>' in resp.text[(index1+52):]:
                                        index3=resp.text.index('</span>',index1+52,len(resp.text))
                                        if '<' not in resp.text[(index1+52):index3] and '>' not in resp.text[(index1+52):index3]:
                                            #print(resp.text[(index1+52):index3])
                                            keyword2+=[resp.text[(index1+52):index3]]
                        if n==1:
                            if qureyinput.lower() in keyword.lower():
                                if '</span>' in resp.text[(index1+52):]:
                                    index3=resp.text.index('</span>',index1+52,len(resp.text))
                                    if '<' not in resp.text[(index1+52):index3] and '>' not in resp.text[(index1+52):index3]:
                                        #print(resp.text[(index1+52):index3])
                                        keyword2+=[resp.text[(index1+52):index3]]
                    last=index1+52
                
                              
                find5=re.findall('<span lang="ja" xml:lang="ja"><span lang="ja" xml:lang="ja">(.*?)</span>',resp.text)
                find51=re.findall('<span lang="ja" xml:lang="ja">(.*?)</span>',resp.text)
                if (find5+find51)!=[]:
                    sstarget+=[(find5+find51)[0]]
               
                find6=re.findall('<span lang="ja"><span lang="ja">(.*?)</span>',resp.text)
                find61=re.findall('<span lang="ja">(.*?)</span>',resp.text)
                if (find6+find61)!=[]:
                    sstarget+=[(find6+find61)[0]]
                
            sstargetnew=[] 
            keyword2new=[]
 
            for vv in sstarget:
                if vv not in sstargetnew:
                    sstargetnew.append(vv)
        
            for vv in keyword2:
                if vv not in keyword2new:
                    keyword2new.append(vv)
            #print(keyword2new)
            if len(keyword2new)>5:
                keyword2new=keyword2new[:5]
            
            return [sstargetnew,keyword2new]    
    except:
        return [0,0]   


def transresult(inputtargetstring):
    try:
        translator = Translator()
    
        tStart = time.time()

        if '.' not in inputtargetstring:
            detectlan=translator.detect(inputtargetstring).lang
            qureyeesearch=websearch=inputtargetstring
            if detectlan=='zh-CN' or detectlan=='ja':
                inputn=2
            if detectlan!='zh-CN' and detectlan!='ja':
                inputn=1
        if '.' in inputtargetstring:
            slice=inputtargetstring.index('.')
            websearch=inputtargetstring[:slice]
            qureyeesearch=inputtargetstring[(slice+1):]   
            detectlan=translator.detect(qureyeesearch).lang
 
            if detectlan=='zh-CN' or detectlan=='ja':
                inputn=2
            if detectlan!='zh-CN' and detectlan!='ja':
                inputn=1

        print(inputn)
        log_file = 'download.log'
        logging.basicConfig(level=logging.DEBUG, filename=log_file, filemode="a+", format="%(asctime)-15s %(levelname)-8s  %(message)s")

        headers = {}
        headers['User-Agent'] = generate_user_agent()
        query2=urllib.parse.quote_plus(websearch)
        headers['Referer'] = np.random.choice(headerslist)
        url='https://www.google.com.tw/search?hl=zh-TW&q='+query2+'%20%E7%BB%B4%E5%9F%BA%E7%99%BE%E7%A7%91&meta=&aq=f&oq=%22'
        req = urllib.request.Request(url, headers = headers)
        resp = urllib.request.urlopen(req) 
        page_content = str(resp.read())

        #url=urllib.parse.unquote(url)
        findx=re.findall('<h3 class="r"><a href="(.*?)" onmousedown', page_content)
        ss=[]
        for i in range(0,len(findx)):
            if 'zh.wikipedia.org' in findx[i]:
                ss+=[findx[i]]
        [x5,x6]=qureyenglish(qureyeesearch,ss,inputn)
        x5test=''
        x6test=''
        if x5!=[]:
            for i in range(0,len(x5)):
                x5test+=x5[i]+'\n'
            x5test='標題名或作品名或人物名:'+'\n'+x5test
        if x6!=[]:
            for i in range(0,len(x6)):
                x6test+=x6[i]+'\n'
            x6test='作品其角色名:'+'\n'+x6test

        return (x5test+x6test)
        tend = time.time()
        print(tend-tStart)
    except:
        return 0

def googletran(inppp):
    translator = Translator()
    try:
        if '-' in inppp:
            slice=inppp.rindex('-')
            dest=inppp[4:slice]
            text=inppp[(slice+1):]
            y=translator.translate(text, dest).text 
            return y
    except:
        return 0
      
##############################################################
    
def get_sourceid(event):
    if event.source.type == 'user':
        return event.source.user_id
    elif event.source.type == 'group':
        return event.source.group_id
    elif event.source.type == 'room':
        return event.source.room_id
    else:
        raise Exception('event.source.type:%s' % event.source.type)
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    event.source.user_id=get_sourceid(event)
    if event.message.text=='吃屎':  
        sss=['https://pixiv.cat/45068168.jpg','https://pixiv.cat/45068168.jpg']
        image1=[0]*2
        image2=[TextSendMessage(text='吃屎')]
        for i in range(0,len(image1)):
            image1[i]=ImageSendMessage(sss[i],sss[i])
              
        image2+=image1
        line_bot_api.reply_message(event.reply_token,image2)
        
        #line_bot_api.reply_message(event.reply_token,TextSendMessage(text='吃屎'))
        
        return 0
######################################################################
    if event.message.text.lower().startswith('trw-')==True:
        x=transresult(event.message.text.lower()[4:])    
        if x!=0:
            line_bot_api.reply_message(event.reply_token,TextSendMessage(text=x[:(len(x)-1)]))
        return 0   
    if event.message.text.lower().startswith('trg.')==True:
        y=googletran(event.message.text.lower())
        if y!=0:
            line_bot_api.reply_message(event.reply_token,TextSendMessage(text=y))
        return 0
######################################################################
    if event.message.text.lower().startswith('p-s')==True:
        [url,item]=pixivsearch(event.message.text)  
        itemid=itemsellectid(url,item)
        result=resulturl(itemid)
        if result=='0' or result==0:
            return 0
        image1=[0]*len(result)
        for i in range(0,len(result)):
            image1[i]=ImageSendMessage(result[i],result[i])
             
        if '-sid' in event.message.text:
            image2=[TextSendMessage(text=itemid)]
            image2+=image1
            #line_bot_api.push_message(event.source.user_id,)
            line_bot_api.reply_message(event.reply_token,image2)
            return 0
        line_bot_api.reply_message(event.reply_token,image1)    
        return 0
    
    if event.message.text.lower().startswith('p-id')==True:
        x=imageid(event.message.text.lower()[4:])
        image1=[0]*len(x)
        for i in range(0,len(x)):
            image1[i]=ImageSendMessage(x[i],x[i])
        line_bot_api.reply_message(event.reply_token,image1)    
        return 0    
    
    if event.message.text.lower().startswith('p-mon')==True:
        monthsearchid=monthsearch(event.message.text.lower())
        if monthsearchid==0 or monthsearchid=='0':
            return 0    
        monthresult=imageid(monthsearchid)  
        image1=[0]*len(monthresult)
        for i in range(0,len(monthresult)):
            image1[i]=ImageSendMessage(monthresult[i],monthresult[i])

        if '-sid' in event.message.text.lower():
            image2=[TextSendMessage(text=monthsearchid)]
            image2+=image1
            line_bot_api.reply_message(event.reply_token,image2)
            return 0
        line_bot_api.reply_message(event.reply_token,image1)
        return 0
    
    if event.message.text.lower().startswith('p-wk')==True:
        #number數只有到50個
        weeksearchid=weelsearch(event.message.text.lower()[4:])
        if weeksearchid==0 or weeksearchid=='0':
            return 0
        weekresult=imageid(weeksearchid)
        image1=[0]*len(weekresult)
        for i in range(0,len(weekresult)):
            image1[i]=ImageSendMessage(weekresult[i],weekresult[i])
        if '-sid' in event.message.text.lower():
            image2=[TextSendMessage(text=weeksearchid)]
            image2+=image1
            line_bot_api.reply_message(event.reply_token,image2)
            return 0
        line_bot_api.reply_message(event.reply_token,image1)    
        return 0
   
    if event.message.text.lower().startswith('p-to')==True:
        todaysearchid=todaysearch(event.message.text.lower()[4:])    
        if todaysearchid==0 or todaysearchid=='0':
            return 0
        todayresult=imageid(todaysearchid)
        image1=[0]*len(todayresult)
        for i in range(0,len(todayresult)):
            image1[i]=ImageSendMessage(todayresult[i],todayresult[i])
        if '-sid' in event.message.text.lower():
            image2=[TextSendMessage(text=todaysearchid)]
            image2+=image1
            line_bot_api.reply_message(event.reply_token,image2)
            return 0
        line_bot_api.reply_message(event.reply_token,image1)        
        return 0
    
    if event.message.text.lower().startswith('p-boy')==True:
        boysearchid=boysearch(event.message.text.lower()[5:])    
        if boysearchid==0 or boysearchid=='0':
            return 0
        
        boyresult=imageid(boysearchid)
        image1=[0]*len(boyresult)
        for i in range(0,len(boyresult)):
            image1[i]=ImageSendMessage(boyresult[i],boyresult[i])
        if '-sid' in event.message.text.lower():
            image2=[TextSendMessage(text=boysearchid)]
            image2+=image1
            line_bot_api.reply_message(event.reply_token,image2)
            return 0
        line_bot_api.reply_message(event.reply_token,image1)           
        return 0
    
    if event.message.text.lower().startswith('p-girl')==True:
        girlsearchid=girlsearch(event.message.text.lower()[6:])
        if girlsearchid==0 or girlsearchid=='0':
            return 0
        girlresult=imageid(girlsearchid)
        image1=[0]*len(girlresult)
        for i in range(0,len(girlresult)):
            image1[i]=ImageSendMessage(girlresult[i],girlresult[i])
        if '-sid' in event.message.text.lower():
            image2=[TextSendMessage(text=girlsearchid)]
            image2+=image1
            line_bot_api.reply_message(event.reply_token,image2)
            return 0
        line_bot_api.reply_message(event.reply_token,image1)  
        return 0
    
    if event.message.text.lower().startswith('p-int')==True:
        intersearchid=intersearch(event.message.text.lower()[5:])
        if intersearchid==0 or intersearchid=='0':
            return 0
        interresult=imageid(intersearchid)
        image1=[0]*len(interresult)
        for i in range(0,len(interresult)):
            image1[i]=ImageSendMessage(interresult[i],interresult[i])
        if '-sid' in event.message.text.lower():
            image2=[TextSendMessage(text=intersearchid)]
            image2+=image1
            line_bot_api.reply_message(event.reply_token,image2)
            return 0
        line_bot_api.reply_message(event.reply_token,image1)
        return 0
    
######################################################################
    if event.message.text.lower().startswith('gi-')==True: 
        ss=googlei(event.message.text[3:],1)
        image1=[0]*3
        for i in range(0,3):
            image1[i]=ImageSendMessage(ss[i],ss[i])
        line_bot_api.reply_message(event.reply_token,image1) 
        return 0
    
    if event.message.text.lower().startswith('gil-')==True: 
        ss=googlei(event.message.text[4:],2)
        image1=[0]*3
        for i in range(0,3):
             image1[i]=ImageSendMessage(ss[i],ss[i])
        line_bot_api.reply_message(event.reply_token,image1)         
        return 0
    
    if event.message.text.lower().startswith('gim-')==True: 
        ss=googlei(event.message.text[4:],3)
        #image_message = ImageSendMessage(original_content_url=ss[0],preview_image_url=ss[0])
        image1=[0]*3
        for i in range(0,3):           
            image1[i]=ImageSendMessage(ss[i],ss[i])
        line_bot_api.reply_message(event.reply_token,image1)     
        return 0
    
    if event.message.text.lower().startswith('gih-')==True: 
        ss=googlei(event.message.text[4:],4)
        image1=[0]*3
        for i in range(0,3):           
            image1[i]=ImageSendMessage(ss[i],ss[i])
        line_bot_api.reply_message(event.reply_token,image1)       
        return 0
    
    if event.message.text.lower().startswith('gs-')==True:    
        #line_bot_api.reply_message(event.reply_token,TextSendMessage(text=googles(event.message.text[4:])))
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=googles(event.message.text[3:])))
        #line_bot_api.push_message(event.source.user_id,TextSendMessage(text=googles(event.message.text[3:])))
        return 0
    if event.message.text.lower().startswith('yt')==True:
        
        if event.message.text.lower()[2:].startswith('-'):
            [title,uploader,imageurl,watch]=youtubee(event.message.text[3:],1)
            result=event.message.text[3:]
        if event.message.text.lower()[2:].startswith('d-'):
            [title,uploader,imageurl,watch]=youtubee(event.message.text[4:],2)
            result=event.message.text[4:]
        if event.message.text.lower()[2:].startswith('p-'):
            [title,uploader,imageurl,watch]=youtubee(event.message.text[4:],3)
            result=event.message.text[4:]

        carousel_template_message = TemplateSendMessage(
            alt_text=result+'搜尋結果',
            template=CarouselTemplate(
                columns=[
                    CarouselColumn(thumbnail_image_url=imageurl[0],title=title[0],text=uploader[0],actions=[URITemplateAction(label='開始觀看',uri=watch[0])]),
                    CarouselColumn(thumbnail_image_url=imageurl[1],title=title[1],text=uploader[1],actions=[URITemplateAction(label='開始觀看',uri=watch[1])]),
                    CarouselColumn(thumbnail_image_url=imageurl[2],title=title[2],text=uploader[2],actions=[URITemplateAction(label='開始觀看',uri=watch[2])]),
                    CarouselColumn(thumbnail_image_url=imageurl[3],title=title[3],text=uploader[3],actions=[URITemplateAction(label='開始觀看',uri=watch[3])]),
                    CarouselColumn(thumbnail_image_url=imageurl[4],title=title[4],text=uploader[4],actions=[URITemplateAction(label='開始觀看',uri=watch[4])]),
                    CarouselColumn(thumbnail_image_url=imageurl[5],title=title[5],text=uploader[5],actions=[URITemplateAction(label='開始觀看',uri=watch[5])]),
                    CarouselColumn(thumbnail_image_url=imageurl[6],title=title[6],text=uploader[6],actions=[URITemplateAction(label='開始觀看',uri=watch[6])]),
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token,carousel_template_message)
        return 0
      
    if event.message.text.lower().startswith('測')==True: 
        carousel_template_message = TemplateSendMessage(
            alt_text='搜尋結果',
            template=CarouselTemplate(
                columns=[
                    CarouselColumn(thumbnail_image_url='https://i.ytimg.com/vi/5ecQJhhH2rc/hqdefault.jpg?sqp=-oaymwEXCPYBEIoBSFryq4qpAwkIARUAAIhCGAE=&amp;rs=AOn4CLBfYYHtRK2QL5GSbhqQjJrKUPFPeQ',title='Fate Stay Night   Unlimited BladeUnlimi4',text='中国云南卫视官方频道 China Yunnan TV Official Channel',actions=[URITemplateAction(label='開始觀看',uri='https://www.youtube.com/watch?v=5ecQJhhH2rc')]),
                    CarouselColumn(thumbnail_image_url='https://i.ytimg.com/vi/Iw6MK9_yUcw/hqdefault.jpg?sqp=-oaymwEXCPYBEIoBSFryq4qpAwkIARUAAIZCGAE=&amp;rs=AOn4CLCyRMQkUnLSikVvSSVDX6ULjnBs7w',title='Lee Sun Hee (이선희)_ Fate (인연 姻缘) ',text='月前',actions=[URITemplateAction(label='開始觀看',uri='https://www.youtube.com/watch?v=yqcn3n0BbE4')]),
                    CarouselColumn(thumbnail_image_url='https://i.ytimg.com/vi/Iw6MK9_yUcw/hqdefault.jpg?sqp=-oaymwEXCPYBEIoBSFryq4qpAwkIARUAAIZCGAE=&amp;rs=AOn4CLCyRMQkUnLSikVvSSVDX6ULjnBs7w',title='Fate/Apocrypha - Karna vs Siegfried | ',text='月前',actions=[URITemplateAction(label='開始觀看',uri='https://www.youtube.com/watch?v=yqcn3n0BbE4')]),
                    CarouselColumn(thumbnail_image_url='https://i.ytimg.com/vi/Iw6MK9_yUcw/hqdefault.jpg?sqp=-oaymwEXCPYBEIoBSFryq4qpAwkIARUAAIZCGAE=&amp;rs=AOn4CLCyRMQkUnLSikVvSSVDX6ULjnBs7w',title='Shirou Kotomine Explained - Fate Apocry',text='月前',actions=[URITemplateAction(label='開始觀看',uri='https://www.youtube.com/watch?v=yqcn3n0BbE4')]),
                    CarouselColumn(thumbnail_image_url='https://i.ytimg.com/vi/Iw6MK9_yUcw/hqdefault.jpg?sqp=-oaymwEXCPYBEIoBSFryq4qpAwkIARUAAIZCGAE=&amp;rs=AOn4CLCyRMQkUnLSikVvSSVDX6ULjnBs7w',title='【TVPP】Hyorin(SISTAR) - Fate, 효린(씨스',text='月前',actions=[URITemplateAction(label='開始觀看',uri='https://www.youtube.com/watch?v=yqcn3n0BbE4')]),
                    CarouselColumn(thumbnail_image_url='https://i.ytimg.com/vi/Iw6MK9_yUcw/hqdefault.jpg?sqp=-oaymwEXCPYBEIoBSFryq4qpAwkIARUAAIZCGAE=&amp;rs=AOn4CLCyRMQkUnLSikVvSSVDX6ULjnBs7w',title="'Fate' A Beautiful Chillstep Mix",text='月前',actions=[URITemplateAction(label='開始觀看',uri='https://www.youtube.com/watch?v=yqcn3n0BbE4')]),
                    CarouselColumn(thumbnail_image_url='https://i.ytimg.com/vi/Iw6MK9_yUcw/hqdefault.jpg?sqp=-oaymwEXCPYBEIoBSFryq4qpAwkIARUAAIZCGAE=&amp;rs=AOn4CLCyRMQkUnLSikVvSSVDX6ULjnBs7w',title="Fate/stay night Movie: Heaven's Feel『Of",text='月前',actions=[URITemplateAction(label='開始觀看',uri='https://www.youtube.com/watch?v=yqcn3n0BbE4')]),
                    CarouselColumn(thumbnail_image_url='https://i.ytimg.com/vi/Iw6MK9_yUcw/hqdefault.jpg?sqp=-oaymwEXCPYBEIoBSFryq4qpAwkIARUAAIZCGAE=&amp;rs=AOn4CLCyRMQkUnLSikVvSSVDX6ULjnBs7w',title='Fate/Apocrypha | Trailer [HD] | Netflix',text='月前',actions=[URITemplateAction(label='開始觀看',uri='https://www.youtube.com/watch?v=yqcn3n0BbE4')]),
                    CarouselColumn(thumbnail_image_url='https://i.ytimg.com/vi/Iw6MK9_yUcw/hqdefault.jpg?sqp=-oaymwEXCPYBEIoBSFryq4qpAwkIARUAAIZCGAE=&amp;rs=AOn4CLCyRMQkUnLSikVvSSVDX6ULjnBs7w',title='Worlds Most Epic Music - Fate',text='月前',actions=[URITemplateAction(label='開始觀看',uri='https://www.youtube.com/watch?v=yqcn3n0BbE4')]),
                    CarouselColumn(thumbnail_image_url='https://i.ytimg.com/vi/Iw6MK9_yUcw/hqdefault.jpg?sqp=-oaymwEXCPYBEIoBSFryq4qpAwkIARUAAIZCGAE=&amp;rs=AOn4CLCyRMQkUnLSikVvSSVDX6ULjnBs7w',title='Top 10 Epic Fate Anime Fights [60FP',text='月前',actions=[URITemplateAction(label='開始觀看',uri='https://www.youtube.com/watch?v=yqcn3n0BbE4')])
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token,carousel_template_message)
        return 0
      
    if event.message.text.lower().startswith('225')==True:
      audio_message = AudioSendMessage(
        original_content_url='https://fs-preview.kfs.io/201307/0tclZeokmjg10mpLw_FUBtFAQnzkfdWeKlkkrtwLN8CDky3dVmg=?__gda__=1523541640_72825906b76b7c5f396302e23d80aa76',
        duration=20000
      )
      line_bot_api.reply_message(event.reply_token,audio_message)
      return 0
    if event.message.text.lower().startswith('215')==True:
      imagemap_message = ImagemapSendMessage(
          base_url='https://i.kfs.io/album/global/14646283,0v1/fit/1000x1000.jpg',
          alt_text='ssssssssssss',
          base_size=BaseSize(height=1040, width=1040),
          actions=[
              URIImagemapAction(
                  link_uri='https://example.com/',
                  area=ImagemapArea(
                      x=0, y=0, width=1040, height=1040
                  )
              ),
              MessageImagemapAction(
                  text='hello',
                  area=ImagemapArea(
                      x=520, y=0, width=520, height=1040
                  )
              )
          ]
      )    
      line_bot_api.reply_message(event.reply_token,imagemap_message)
      return 0
      
      
      
import os
if __name__ == "__main__":
    
    app.run(host='0.0.0.0',port=os.environ['PORT'])
