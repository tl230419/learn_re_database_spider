import urllib
import urllib.request
import re
import pymysql
import db_helper

def main():
    try:
        db_helper.create_db()

        list_url = "http://www.ygdy8.net/html/gndy/dyzz/list_23_2.html"
        req = urllib.request.urlopen(list_url)
        resp = req.read()
        print(req)

        resp_data = resp.decode('gbk', errors="ignore")
        result_list = fetch_list(resp_data)
        for item in result_list:
            detail = fetch_detail(item)
            print(item)
            db_helper.save(detail)
            print(detail)
    except UnicodeDecodeError as e:
        print('d', type(resp))
        print(e)

def fetch_list(data):
    result_list = re.findall('<a href="(.*)" class="ulink">(.*)</a>',data)
    return result_list

def fetch_detail(item):
    #print("item:\r\n", item)
    url = "http://www.ygdy8.net" + item[0]
    req = urllib.request.urlopen(url)
    resp_data = req.read()
    resp_content = resp_data.decode('gbk')
    #print("resp_content:\r\n", resp_content)

    ret = re.search('<img border="0" src="(.*?)"', resp_content)
    img_url = None
    if ret:
        img_url = ret.group(1)
    else:
        ret = re.search('<img border="0" alt="" src="(.*?)"', resp_content)
        if ret:
            img_url = ret.group(1)
        else:
            print("没有图片", item[1])
            #print("resp_content:\r\n", resp_content)
            img_url = "https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2535338893.jpg"

    result = re.search(r'bgcolor="#fdfddf"><a href=\"(.*)\">(\1)</a>',resp_content)
    download_url = None
    if result:
        download_url = result.group(1)
    else:
        print("没有下载URL")

    return (img_url, item[1], download_url)

if __name__ == '__main__':
    main()



