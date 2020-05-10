import requests
import re
import threading
from models import Movie, Session

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
        movie = Movie()
        movie.name = item["name"]
        movie.icon = item["icon"]
        movie.url = item["url"]

        session = Session()
        session.add(movie)
        session.commit()
        session.close()
        print("保存数据成功")

    def parse_item(self, response):
        response.encoding = "gbk"
        name = re.search('<h1><font color=#07519a>(.*)</font></h1>', response.text).group(1)
        icon = re.search('<br /><br />\s*<img.*?src="(.*?)".*?/>\s*<br /><br />', response.text).group(1)
        print(name + "=====" + icon)
        url = re.search('bgcolor="#fdfddf"><a href="(.*?)">.*?</a>', response.text).group(1)

        return {"name":name, "icon":icon, "url":url}


if __name__ == '__main__':
    MovieSpider.run()