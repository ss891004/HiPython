import requests
from bs4 import BeautifulSoup


response = requests.get("http://video.mobiletrain.org/course/index/courseId/479")
res_html=response.text

from lxml import etree

selector = etree.HTML(res_html)

content=selector.xpath('//a/@data-url') 

for num in content:
    print(num)