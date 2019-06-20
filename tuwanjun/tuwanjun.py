# -*- coding:UTF-8 -*-
from bs4 import BeautifulSoup
from selenium import webdriver
import os
import urllib.request
import time
#设置浏览器为chrome
options = webdriver.ChromeOptions()
options.add_argument(
    'user-agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.81 Safari/537.36"')
browser = webdriver.Chrome(options=options)
browser.get('https://www.tuwanjun.com/')
#设置浏览器滑动
for i in range(1, 5):
    js = "var q=document.documentElement.scrollTop=100000"
    browser.execute_script(js)
    time.sleep(5)
#解析网页
html = browser.page_source
bf1 = BeautifulSoup(html, 'lxml')
#设置路径
path = "C:\\Users\\SXL47\\Desktop"
new_path = os.path.join(path, 'pictures')
if not os.path.isdir(new_path):
    os.mkdir(new_path)
new_path += '\\' #此处需要和windows系统区分开

bf2 = bf1.find_all(class_="grid-item")
imagecount = 1
#下载图片
for bf in bf2:
    bf3=bf.find("img")
    img=bf3.get('src')
    file_name="%s.jpg" % imagecount
    urllib.request.urlretrieve(img, new_path + file_name)
    print("图片%i正在下载"%imagecount)
    imagecount+=1

print("图片下载完成")