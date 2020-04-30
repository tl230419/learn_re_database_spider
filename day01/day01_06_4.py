'''
*****************
Date: 2020-04-30
Author: Allen
*****************
'''

#coding = utf-8

import re

ret = re.match("[1-9]?\d", "8")
print(ret.group())

ret = re.match("[1-9]?\d", "78")
print(ret.group())

ret = re.match("[1-9]?\d", "08")
print(ret.group())

ret = re.match("[1-9]?\d$", "08")
if ret:
    print(ret.group())
else:
    print("不在0-100之间")

ret = re.match("[1-9]?\d|100", "8")
print(ret.group())

ret = re.match("[1-9]?\d|100", "78")
print(ret.group())

ret = re.match("[1-9]?\d|100", "08")
print(ret.group())

ret = re.match("[1-9]?\d|100", "100")
print(ret.group())