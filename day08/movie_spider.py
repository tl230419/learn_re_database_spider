import requests
import re
import threading
import models

class MovieSpider():
    start_url = "http://www.ygdy8.net/html/gndy/dyzz/list_23_1.html"

    def run(self):
        response = requests.get(self.start_url)
        self.parse(response)

    def parse(self, response):
        response.encoding = "gbk"
        urls = re.findall('<a href="(.*)" class="ulink">.*</a>', response.text)
        for url in urls:
            url = "http://www.ygdy8.net" + url
            t = threading.Thread(target=self.send_request, args=(url, self.parse_item))
            t.start()

    def send_request(self, url, callback):
        response = requests.get(url)
        item = callback(response)
        t = threading.Thread(target=self.pipeline, args=(item,))
        t.start()

    def pipeline(self, item):
        movie = models.Movie(title=item["name"], img_url=item["icon"], download_url=item["url"])

        session = models.Session()
        session.add(movie)
        session.commit()
        session.close()
        print("保存数据成功")

    def parse_item(self, response):
        response.encoding = "gbk"
        ret = re.search('<h1><font color=#07519a>(.*)</font></h1>', response.text)
        name = None
        if ret:
            name = ret.group(1)
        else:
            print("No name")

        ret = re.search('<img border="0" src="(.*?)"', response.text)
        icon = None
        if ret:
            icon = ret.group(1)
        else:
            ret = re.search('<img border="0" alt="" src="(.*?)"', response.text)
            if ret:
                icon = ret.group(1)
            else:
                print("No icon")
                icon = "https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2535338893.jpg"

        ret = re.search(r'bgcolor="#fdfddf"><a href=\"(.*)\">(\1)</a>', response.text)
        url = None
        if ret:
            url = ret.group(1)
        else:
            print("No url")

        return {"name":name, "icon":icon, "url":url}


if __name__ == '__main__':
    MovieSpider().run()