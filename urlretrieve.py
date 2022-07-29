#!/usr/local/bin/python3
# coding=utf-8
import urllib.request as re
#Python 3
#import urllib.request
def go(a,b,c):
    per = 100.0 * a * b / c
    if per > 100:
        per = 100
        print("%.2f%%" % per)
url = "http://ww2.sinaimg.cn/mw690/8e4023f8gw1f34gs20b4ij20qo0zkthw.jpg"
local = "/Users/marcuschen/temp/g.jpg"
re.urlretrieve(url, local, go)
re.requst
#Python 3
#urllib.request.urlrretrieve(url, local, go)
