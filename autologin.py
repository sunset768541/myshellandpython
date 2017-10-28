#!/usr/bin/env python
#coding=utf-8
import urllib
import sys
import http.cookiejar
import ssl 
ssl._create_default_https_context = ssl._create_unverified_context
cookie = http.cookiejar.CookieJar()                                        #保存cookie，为登录后访问其它页面做准备
cjhdr  =  urllib.request.HTTPCookieProcessor(cookie)             
opener = urllib.request.build_opener(cjhdr)

url="https://auth.nfjd.gmcc.net/dana-na/auth/url_default/login.cgi"
#url = "https://auth.nfjd.gmcc.net/dana-na/auth/url_default/login.cgi"
postdata = {'tz_offset':'480','username':'wangbaohui', 'password':'13802885224','realm':'NFJD_CMNET_ACCESS','btnSubmit':'%E7%99%BB%E5%BD%95'}          #用户名、密码和Submit按钮，有的页面要求Submit的值不为空
#tz_offset=480&username=wangbaohui&password=13802885224&realm=NFJD_CMNET_ACCESS&btnSubmit=%E7%99%BB%E5%BD%95

#print (urllib.request.urlopen(url).read().decode("utf8"))                              #输出登录页面    

params = urllib.parse.urlencode(postdata).encode(encoding='UTF8')                          #将用户名、密码转换为 “username=admin&pwd=123456”的形式
opener.open(url,params)                                                     #开始登录
#print (opener.open(url,params).read().decode("utf8"))   #登录成功后，访问其它页面
