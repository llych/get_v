# get_v
音悦台 慕客网 极客学院 视频 下载
====


        K:\llych\github\get_v>get_v.py --help

        Usage:get_v.py --url=http://xxoo.xx  --dir=/data
        --url=视频网址
        --dir=下载视频存放的路径

        目前支持:

        音悦台高清视频
        例如  --url=http://v.yinyuetai.com/video/2316441

        幕客网视频
        例如  --url=http://www.imooc.com/learn/194

        极客学院 (蛋疼,需要vip帐号,注册个小号体验vip
         登录后把cookie 填入插件里 get_v\plugins\jikexueyuan.py)
        例如  --url=http://www.jikexueyuan.com/course/1439.html

## 下载音悦台视频 自动选择最高清晰度
        K:\llych\github\get_v>get_v.py --url http://v.yinyuetai.com/video/2312502 --dir k:/
        董小姐 Cover.flv
        15% [..........                                                              ] 12402688 / 82260939
 
### 下载 慕客网视频
        K:\llych>get_v.py --url http://www.imooc.com/learn/122 --dir k:/test
        视频 共 89 个
        1-1_MySQL概述.mp4
        100% [..........................................................................] 3052254 / 3052254
        1-2_MySQL的安装与配置.mp4
        100% [........................................................................] 49619570 / 49619570
        1-3_启动与停止MySQL服务.mp4
        2% [..                                                                        ]  204800 / 6860931
  
### 下载极客学院 (需要注册个体验vip帐号)
        K:\llych>get_v.py --url http://www.jikexueyuan.com/course/1439.html --dir k:/test
        视频 共 4 个
        1.MongoDB 介绍与安装.mp4
        4% [...                                                                     ]   729088 / 15538391
