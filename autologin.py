#!/usr/bin/env python
#coding=utf-8
import urllib
import sys
import http.cookiejar
import ssl 
ssl._create_default_https_context = ssl._create_unverified_context
cookie = http.cookiejar.CookieJar()                                        #����cookie��Ϊ��¼���������ҳ����׼��
cjhdr  =  urllib.request.HTTPCookieProcessor(cookie)             
opener = urllib.request.build_opener(cjhdr)

url="https://auth.nfjd.gmcc.net/dana-na/auth/url_default/login.cgi"
#url = "https://auth.nfjd.gmcc.net/dana-na/auth/url_default/login.cgi"
postdata = {'tz_offset':'480','username':'wangbaohui', 'password':'13802885224','realm':'NFJD_CMNET_ACCESS','btnSubmit':'%E7%99%BB%E5%BD%95'}          #�û����������Submit��ť���е�ҳ��Ҫ��Submit��ֵ��Ϊ��
#tz_offset=480&username=wangbaohui&password=13802885224&realm=NFJD_CMNET_ACCESS&btnSubmit=%E7%99%BB%E5%BD%95

#print (urllib.request.urlopen(url).read().decode("utf8"))                              #�����¼ҳ��    

params = urllib.parse.urlencode(postdata).encode(encoding='UTF8')                          #���û���������ת��Ϊ ��username=admin&pwd=123456������ʽ
opener.open(url,params)                                                     #��ʼ��¼
#print (opener.open(url,params).read().decode("utf8"))   #��¼�ɹ��󣬷�������ҳ��
