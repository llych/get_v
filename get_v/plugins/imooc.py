# coding:GBK
'''
Created on Jun 26, 2015

@author: 黎宇初
@mail: llych#126.com
'''

import requests
import re
import sys

description = '''
幕客网视频 
例如  --url=http://www.imooc.com/learn/194'''

def handle(url):
    #url = 'http://www.imooc.com/learn/194'
    #url=sys.argv[1]
    session = requests.session()
    headers = {'User-Agent':'Mozilla/5.0 (Linux; U; Android 4.0.3; zh-cn; M032 Build/IML74K) UC AppleWebKit/534.31 (KHTML, like Gecko) Mobile Safari/534.310'}
    session.headers.update(headers)

    def getVideo(id):
        videoUrl='http://www.imooc.com/course/ajaxmediainfo/?mid=%s&mode=flash'%id
        video_Json = session.get(videoUrl).json()
        return video_Json['data']['result']['name'],video_Json['data']['result']['mpath'][0]

    html = session.get(url).content.decode('UTF-8').encode('GBK')
    video = re.findall('<a data-id="(\d+)" href="/video/\d+">(.*?)</a>', html)
    print '视频 共 %s 个'%len(video)
    for id,name in video:
        #print id,name
        yield getVideo(id)[1], name.replace(' ','_')+'.mp4'
        #print ''
    
