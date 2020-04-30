'''
*****************
Date: 2020-04-30
Author: Allen
*****************
'''

#coding=utf-8

import re
import urllib.request
from pymysql import *

def get_movie_link():
    url = "http://www.dytt8.net/html/gndy/rihan/list_6_2.html"
    file = urllib.request.urlopen(url)
    file_content = file.read()
    link_list = re.findall(r'<a href="(.*)" class="ulink">(.*)</a>', file_content.decode("GBK", "ignore"))
    film_link = {}
    for num, i in enumerate(link_list):
        file = urllib.request.urlopen("http://www.dytt8.net" + i[0])
        data = file.read()
        #print(data)
        ret = re.findall(r'.*><a href="([^magnet:?xt=].*)">', data.decode("GBK", "ignore"))
        print(ret)
        film_link[i[1]] = ret[1]
        print("已经加载电影数量%d" % num)

    return film_link

if __name__ == '__main__':
    movie_link = get_movie_link()

    for name, link in movie_link.items():
        print("电影名字：", name, "下载链接：", link)