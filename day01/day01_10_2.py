'''
*****************
Date: 2020-04-30
Author: Allen
*****************
'''

import re

str = """class="LazyLoad is-visible DyImg DyListCover-pic"><img src="https://rpic.douyucdn.cn/asrpic/190827/7255777_526583_708c5_2_1048.jpg/webpdy1" class="DyImg-content is-normal "></div>"""
result = re.search("src=\"(.*?)\"", str)
if result:
    print(result.group(1))
else:
    print("匹配失败！")