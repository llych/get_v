# coding:GBK
'''
Created on Jun 28, 2015

@author: 黎宇初
@mail: llych#126.com
'''
import glob
import os
import re
import wget
import sys

class default:
    @staticmethod
    def handle(*argv,**kwargs):
        print '''
    暂时不支持 此网站
        '''
        sys.exit(5)

modules = {}
CURR_DIR=os.getcwd()
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
os.chdir(BASE_DIR)
for module_file in  glob.glob("./get_v/plugins/*.py"):
    try:  
       module_name,ext = os.path.splitext(os.path.basename(module_file))  
       #module = __import__('get_v.plugins.%s'+module_name)  
       module = __import__('get_v.plugins.%s'%module_name,{},{},[module_name])
       #modules.append(module) 
       #print module_name
       #print ext
       modules[module_name] = module
    except ImportError: 
        pass
#print modules
modules.pop('__init__')

def help():
    for module in modules:
        print modules[module].description

def Download(url,fileName):
    cmd='wget %s -t 5 -c --referer %s -O "%s"' % (url,url,fileName)
    os.system(cmd)

def main(*argv,**kwargs):
    url=argv[0]
    dir=argv[1]

    if dir == None:
        dir='./'
    try:
        os.chdir(CURR_DIR) 
        if not os.path.exists(dir):
            os.makedirs(dir)
        
        os.chdir(dir)
        #print dir
        site = re.findall('http://(?:\w+\.)?(.*?)\..*',url)[0]
        #print site
        for url,fileName in modules.get(site,default).handle(url):
            fileName=re.sub(r'/','',fileName)
            print fileName
            if os.path.isfile(fileName):
                print '视频已存在,跳过 :',fileName
            else:
                wget.download(url,fileName)
            #Download(url,fileName)
            print ''
    except Exception, e:
        print e
        default.handle()
        