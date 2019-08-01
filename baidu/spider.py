"""
@Author: 郭明德
@Description: 爬取百度图片
@Date: 2019/8/1 11:53 
"""
import re
from urllib.request import urlretrieve

import requests

ImgUrl = 'https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&ie=utf-8&word=性感美女'
response = requests.get(ImgUrl)
html = response.text

# 清洗数据，获得图片的链接地址
link = re.findall(r'"middleURL":"(.*?)",', html, re.S)


# 下载图片
def urllib_download(url, pos):
    urlretrieve(url, pos)


# 图片保存的本地地址 地址需要事先存在
position = ""

for i in range(len(link)):
    print(link[i])
    position = 'images/img' + str(i) + '.jpg'
    urllib_download(link[i], position)
