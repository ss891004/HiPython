import requests # 响应爬取
from DrissionPage import ChromiumPage # 谷歌
import re # 正则表达式
import os  # 系统查找

os.makedirs("video",exist_ok=True)

headers ={
          "referer":"https://www.douyin.com/user/MS4wLjABAAAAmSQFrU3apOhr3zufcJzKjsxGNQbo7JN5bIMDcMo0fEInSZlt6fOLdKICJUwQJOun?from_tab_name=main&vid=7650795978244607267",
          "user-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36 Edg/148.0.0.0"}

GG =ChromiumPage()
GG.listen.start("aweme/post/")
GG.get("https://www.douyin.com/user/MS4wLjABAAAAmSQFrU3apOhr3zufcJzKjsxGNQbo7JN5bIMDcMo0fEInSZlt6fOLdKICJUwQJOun?from_tab_name=main&vid=7650795978244607267")
returnBody=GG.listen.wait();

jsonbody=returnBody.response.body

data =jsonbody["aweme_list"]


for i in data:
    video_url=i["video"]["play_addr"]["url_list"][0]
    title=i["desc"]
    title_re=re.sub("[,.<>?;=-]","",title)
    print(title_re)
    res=requests.get(url=video_url,headers=headers).content

    with open ("video\\"+title_re+".mp4","wb" ) as  f :
        f.write(res)
