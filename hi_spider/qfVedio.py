import requests
import json
import os
import time
import re

headers = { "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"}

murl = "http://video.mobiletrain.org/course/index/courseId/716"

aa = requests.get(url=murl, headers=headers, allow_redirects=False)


# 批量下载视频

# /html/body/div[2]/div[1]/div[2]/div[2]/ul/li[1]/ul/li[4]/a

/html/body/div[2]/div[1]/div[2]/div[2]/ul/li[1]/ul/li[1]/a



vediourl ="http://7xtcwd.com1.z0.glb.clouddn.com/千锋Web前端教程：004 变量命名和弱引用.mp4"

print(vediourl.split("：")[1])

with open(vediourl.split("：")[1], 'wb') as v:
    try:
        v.write(requests.get(url=vediourl, headers=headers).content)
    except Exception as e:
        print(e)
