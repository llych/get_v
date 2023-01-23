# coding:GBK
'''
Created on Jun 28, 2015

@author: 黎**
@mail: l**#126.com
'''

import requests
import re
import sys

description = '''
极客学院 (蛋疼,需要vip帐号,注册个小号体验vip
         登录后把cookie 填入插件里 get_v\plugins\jikexueyuan.py)
例如  --url=http://www.jikexueyuan.com/course/1439.html'''

#----------------填入以下cookie 浏览器里获取
cookie='stat_uuid=1434994598214629244303; undefined=; channel=invite_100w_sharebutton_direct1; stat_ssid=1436397140035; stat_isNew=0; uname=jike_tvzmnh71964; uid=3687067; code=7K3IN6; authcode=8ef4VyRgO0VVAIp0VCRVIZ%2BGSm6ovB3ka3iiH0NwGCzkqGH0Qq3BvW28db08JaX900SIM1OhOHpwpBcwALGhHOjamhd2hg9nXw5iGq8ptkFMXORACDIISUY6%2FdqI%2BhlLFVOSow; QINGCLOUDELB=7e36c8b37b8339126ed93010ae808701d562b81daa2a899c46d3a1e304c7eb2b|VZFwr|VZFwm; Hm_lvt_f3c68d41bda15331608595c98e9c3915=1435468507,1435507848,1435530201,1435594856; Hm_lpvt_f3c68d41bda15331608595c98e9c3915=1435594873; MECHAT_LVTime=1435594873477; connect.sid=s%3AikXrRmtHErUDkQ9Ut0ms96Fr3OMPQVl-.Go9eAQtdT3OiOwM%2BBnhW4%2BDzJQHZx%2BTYpuUV4Qvipkg; _ga=GA1.2.807642645.1434994597; _gat=1;'
def handle(url):
    session = requests.session()
    headers = {'User-Agent':'Mozilla/5.0 (Linux; U; Android 4.0.3; zh-cn; M032 Build/IML74K) UC AppleWebKit/534.31 (KHTML, like Gecko) Mobile Safari/534.310'}
    headers['Cookie']=cookie
    session.headers.update(headers)
    def getVideo(url):
        html = session.get(url).content
        try:
            videoUrl = re.findall('<source src="(http://.*?.jikexueyuan.com/.*?)" type="video/.*?" />',html)[0]
            return videoUrl
        except Exception, e:
            print url,'视频未找到'
            
    html = session.get(url).content
    videos = re.findall('<span class="sm-icon ">.*?<a href="(http://.*?)" jktag=".*?">(.*?)</a>',html,re.S)
    print '视频 共 %s 个'%len(videos)
    for url,fileName in videos:
        fileName=fileName.decode('UTF-8').encode('GBK')
        yield getVideo(url),fileName+'.mp4'
if __name__ == '__main__':
    url='http://www.jikexueyuan.com/course/1439_4.html?ss=1'
    url=sys.argv[1]
    handle(url)
