'''
*****************
Date: 2020-05-10
Author: Allen
*****************
'''

import urllib.request
import re
import time
import json

def test03():
    url = "https://fanyi.qq.com/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36"
    }
    request = urllib.request.Request(url, headers=headers)
    response = urllib.request.urlopen(request)
    content = response.read().decode("UTF-8")

    regex = '\s{8}var\sqtv\s=\s"(.*?)";\n\s{8}var\sqtk\s=\s"(.*)";'
    result = re.search(regex, content)
    if result:
        return (result.group(1), result.group(2))
    else:
        print("匹配失败")

def test04():
    qtv,qtk = test03()
    #print(qtv)
    #print(qtk)

    text = input("请输入你要翻译的文本：")
    print(text)
    data = {
        "source": "auto",
        "target": "zh",
        #"sourceText": input("请输入你要翻译的文本："),
        "sourceText": text,
        "sessionUuid": "translate_uuid" + str(int(time.time() * 1000)),
        "qtv": qtv,
        "qtk": qtk
    }

    data = urllib.parse.urlencode(data).encode('utf-8')
    #print("data:\r\n", data)

    headers = {
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Origin": "https://fanyi.qq.com",
        "Referer": "https://fanyi.qq.com/",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest",
        "Content-length": len(data)
    }
    url = "https://fanyi.qq.com/api/translate"
    req = urllib.request.Request(url, data, headers)
    resp = urllib.request.urlopen(req)

    content = resp.read().decode()
    content = json.loads(content)
    #print(content)
    target_text = content["translate"]["records"][0]["targetText"]
    print("翻译结果为：", target_text)

def translate_demo():
    while True:
        test04()

if __name__ == '__main__':
    translate_demo()