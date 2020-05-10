import db_helper
import utils
import re

def generate_content():
    movies = db_helper.fetch_movies()
    str = """
    <div class="item">
            <img src="%s" />
            <p>%s</p>
            <a href="%s">点击下载</a>
        </div>
    """

    result = ""
    for movie in movies:
        ret = re.search("《(.*)》", movie[2])
        result += str%(movie[1], ret.group(1), utils.create_thunder_url(movie[3]))

    return result

def fill_template():
    content = generate_content()
    with open("template.html", "r") as temp:
        temp_content = temp.read(4096)
        result = re.sub('\{\{content\}\}',content,temp_content)
        return result