'''
*****************
Date: 2020-04-29
Author: Allen
*****************
'''

import re

result = re.match("itcast", "itcast.cn")
if result:
    print(result.group())
else:
    print("匹配失败！")
