# coding:GBK
'''
Created on Jun 28, 2015

@author: 黎宇初
@mail: llych#126.com
'''
import re
import requests
import sys
description = '''
音悦台高清视频 
例如  --url=http://v.yinyuetai.com/video/2316441'''


def handle(url):
    try:
        id = re.findall('video/(\d+)',url)[0]
        apiUrl = 'http://www.yinyuetai.com/api/info/get-video-urls?json=true&videoId=%s'%id
        #print url
        html = requests.get(apiUrl).json()
        reqJson={i:html[i] for i in html if 'Url' in i}
        videoUrl = reqJson.items()[-1][1]
        
        html = requests.get(url).content
        fileName = re.findall('title : "(.*?)"',html)[0].decode('UTF-8').encode('GBK')
        yield str(videoUrl).strip(),fileName+'.flv'
        #return []
    except Exception, e:
        print '抱歉,目前该链接无法解析'
        #print e
        sys.exit(3) 
