'''
*****************
Date: 2020-05-11
Author: Allen
*****************
'''

import requests
import  time

response = requests.get("https://www.bing.com")
print(response)

kw = {'wd':'长城'}
response = requests.get("https://www.bing.com", params=kw)
print(response)

kw = {'wd':'长城'}
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}
response = requests.get("https://www.bing.com", params=kw, headers=headers)
print(response)

kw = {"name":"zhangsan"}
headers = {"User-Agent":"a niubility navigator"}
url = "http://httpbin.org/get"
response = requests.get(url, params=kw, headers=headers)
print("响应状态码:{}".format(response.status_code))
print("响应头:{}".format(response.headers))
print("编码:{}".format(response.encoding))
# 这里解码内容,它内部是依靠猜测的方式去解码的
print("解码内容:{}".format(response.text))
print("原始字节信息:{}".format(response.content))
print("完整的响应地址:{}".format(response.url))


#============ post ===============
response = requests.post("https://www.bing.com")
print(response)

data = "你好python"

headers = {
"Accept": "application/json, text/javascript, */*; q=0.01",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Origin": "https://fanyi.qq.com",
    "Referer": "https://fanyi.qq.com/",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36",
    "X-Requested-With": "XMLHttpRequest",
    "Content-length": str(len(data.encode()))
}

keyword = {
    "source": "auto",
    "target": "auto",
    "sourceText": data,
    "sessionUuid": "translate_uuid"+str(int(time.time()*1000))
}

url = "https://fanyi.qq.com/api/translate"
result = requests.post(url, headers=headers, data=keyword).json()
print(result['translate']['records'][0]['targetText'])

# cookie and session
response = requests.get("https://www.bing.com")
cookie_jar = response.cookies
cookie_dict = requests.utils.dict_from_cookiejar(cookie_jar)
print(cookie_dict)

session = requests.session()
response = session.get("https://www.bing.com")
print(response)