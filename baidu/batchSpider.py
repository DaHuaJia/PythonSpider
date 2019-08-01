"""
@Author: 郭明德
@Description: 批量爬取百度图片
@Date: 2019/8/1 12:04 
"""
import re
from urllib.request import urlretrieve
import requests

# 获取输入的份数
keyword = input('请输入你要查看的照片的关键词: ')
page = input('请输入你要浏览的页数(每份30张): ')

"""
百度分页图片地址 (随着百度规则的变化，该链接地址可能会不适用)
通过分析百度图片的地址和分页信息 F12 -> Network -> XHR，可以看出 分页的链接回改变的就是 pn、rn、gsm 值
通过尝试这些值重新发送数据，我们可以知道，百度的分页是每页30张，分页的信息通过ajax 传到后台，字段就是 pn
因此我们可以通过修改pn 的值，然后模拟分页，批量下载图片。

"""
targetUrl = 'https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord='+keyword\
            +'&cl=2&lm=-1&ie=utf-8&oe=utf-8&st=-1&word='+keyword+'&face=0&istype=2&qc=&nc=1&pn='

# 本地地址需要提前存在
position = 'images/python'


# 下载每页的图片
def download_img(url, num):
    response = requests.get(url)
    html = response.text
    link = re.findall(r'"middleURL":"(.*?)",', html, re.S)

    for j in range(len(link)):
        print(link[j])
        urlretrieve(link[j], position+'/img'+str(num+j)+'.jpg')


# 循环每页，获取每页的分页地址
for i in range(int(page)):
    pageUrl = targetUrl+str((i+1) * 30)+'&rn=30&gsm=78&1564623813907='
    download_img(pageUrl, i*30)
    print('number=' + str((i+1)*30))
