'''
*****************
Date: 2020-04-30
Author: Allen
*****************
'''

#coding = utf-8

import re

ret = re.match(r"<(?P<name1>\w*)><(?P<name2>\w*)>.*</(?P=name2)></(?P=name1)>", "<html><h1>www.itcast.cn</h1></html>")
if ret:
    print(ret.group())
else:
    print("匹配失败")

ret = re.match(r"<(?P<name1>\w*)><(?P<name2>\w*)>.*</(?P=name2)></(?P=name1)>", "<html><h1>www.itcast.cn</h2></html>")
if ret:
    print(ret.group())
else:
    print("匹配失败")