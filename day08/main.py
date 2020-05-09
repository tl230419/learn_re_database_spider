import urllib
import urllib.request
import re
import pymysql
import db_helper

def main():
    try:
        list_url = "http://www.ygdy8.net/html/gndy/dyzz/list_23_2.html"
        req = request.urlopen(list_url)
        resp = req.read()
        print(req)

        resp_data = resp.decode('gbk', errors="ignore")
        result_list = fetch_list(resp_data)
        for item in result_list:
            detail = fetch_detail(item)
            db_helper.save(detail)
            print(detail)
    except UnicodeDecodeError as e:
        print('d', type(resp))
        print(e)

def fetch_list(data):
    result_list = re.findall('<a href="(.*)" class="ulink">(.*)</a>',data)
    return result_list

def fetch_detail(item):
    url = "http://www.ygdy8.net" + item[0]
    req = request.urlopen(url)
    resp_data = req.read()
    resp_content = resp_data.decode('gbk')

    ret = re.match('<img border="0" src="(.*?)"', resp_content)
    img_url = None
    if ret:
        img_url = ret.group(1)
    else:
        print("没有图片", item[1])
        img_url = "https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2535338893.jpg"

    result = re.search(r'bgcolor="#fdfddf"><a href=\"(.*)\">(\1)</a>',resp_content)
    download_url = result.group(1)

    return (img_url, item[1], download_url)



