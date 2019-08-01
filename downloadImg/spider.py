"""
@Author: 郭明德
@Description: 网络图片下载
@Date: 2019/8/1 10:08 
"""
import os
from urllib.request import urlretrieve

import requests


# 图片地址
ImgUrl = 'https://ss0.bdstatic.com/70cFvHSh_Q1YnxGkpoWK1HF6hhy/it/u=147138289,859921715&fm=26&gp=0.jpg'

# 当前工作路径
dic1 = os.getcwd()
# 绝对路径
dic2 = 'E:/Workspace/Python/WorkSpace2019/SpiderDemo/downloadImg'


# 方法一 (相对路径)
def request_download(url):
    res = requests.get(url)
    with open('images/img1.jpg', 'wb') as fp:
        fp.write(res.content)


# 方法二 (绝对路径) 使用该方法时，当前路径文件夹应存在，否则会报错 FileNotFoundError
def urllib_download(url, dics):
    urlretrieve(url, dics+'/images/img2.jpg')


# 方法三 (当前工作路径)
def chunk_download(url, dics):
    res = requests.get(url)
    with open(dics+'/images/img3.jpg', 'wb') as fp:
        for chunk in res.iter_content(32):
            fp.write(chunk)


request_download(ImgUrl)

urllib_download(ImgUrl, dic2)

chunk_download(ImgUrl, dic1)

