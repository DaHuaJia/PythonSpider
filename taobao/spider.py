"""
@Author: 郭明德
@Description: 将爬取到的数据持久化到本地csv文件。
csv文件编辑简单，显示清晰，可以使用Excel打开
@Date: 2019/8/1 10:47 
"""
# 正则表达式标准库
import re
import requests

url = 'https://s.taobao.com/search?q=java&ie=utf8'
# 发送get请求，获得网页
response = requests.get(url)
html = response.text

# 通过正则表达式提取关键数据
data = re.findall(r'<div class="footer-hd">(.*?)</div>', html, re.S)[0]
# 清洗数据 去除头尾的空格、回车、分号 等
data.strip(' ;\n')

# 进一步提取数据
link = re.findall(r'<a href="(.*?)">', data, re.S)
title = re.findall(r'">(.*?)</a>', data, re.S)

# 数据持久化 将数据保存到csv文件中
# 打开文件，获得句柄
fb = open('spider.csv', 'w', encoding='utf-8')
# 写入csv文件标题
fb.write('网址名称,网址url\n')

for i in range(len(link)):
    fb.write(title[i]+','+link[i]+'\n')

fb.close()
