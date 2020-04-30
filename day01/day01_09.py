'''
*****************
Date: 2020-04-30
Author: Allen
*****************
'''

import re

#result = re.match(r"aaa(\d+)", "aaa123456")
result = re.match(r"aaa(\d+?)", "aaa123456")
if result:
    print(result.group())
else:
    print("匹配失败！")