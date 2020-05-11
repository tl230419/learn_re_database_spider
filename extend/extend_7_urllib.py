'''
*****************
Date: 2020-05-11
Author: Allen
*****************
'''

import urllib.request

def test01():
    url = "https://www.bing.com"
    response = urllib.request.urlopen(url)

    print("获取响应状态码:", response.getcode())
    print("获取所有响应头:", response.getheaders())
    print("获取指定响应头:", response.getheader("Content-Type"))
    print("获取响应体:", response.read().decode())

test01()


def test02():
    """
        发送信息带有请求头
    """
    url = "http://httpbin.org/headers"
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"}
    request = urllib.request.Request(url, headers=headers)

    response = urllib.request.urlopen(request)
    print(response.read().decode())

test02()

def test03():
    """
    发送带参数的get请求
    """
    url = "https://www.bing.com/s?"
    data = urllib.parse.urlencode({"wd":"小凯"})
    # 编码之后将参数拼接到url末尾
    url += data
    # 构建请求对象
    req = urllib.request.Request(url)
    # 发送请求
    response = urllib.request.urlopen(req)
    print(response.read().decode())

#test03()

def test05():
    """
    发送post请求带参数
    """
    url = "http://www.httpbin.org/post"
    # 对参数进行编码
    data = urllib.parse.urlencode({"wd":"小凯"}).encode()
    # 构建请求对象
    req = urllib.request.Request(url,data)
    # 发送请求
    response = urllib.request.urlopen(req)
    # 打印response中的信息
    print(response.read().decode())

test05()