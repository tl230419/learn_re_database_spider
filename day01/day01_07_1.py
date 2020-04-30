'''
*****************
Date: 2020-04-30
Author: Allen
*****************
'''

import re

ret = re.search(r"\d+", "阅读次数为 9999")
if ret:
    print(ret.group())
else:
    print("不匹配")

#coding = utf-8

import re

ret = re.findall(r"\d+", "阅读次数:9999次,转发次数:883次,评论次数:3次")
print(ret)

#coding = utf-8

import re

ret = re.sub(r"\d+", "1000", "阅读次数:9999次,转发次数:883次,评论次数:3次")
print(ret)

#coding = utf-8

import re

def add(temp):
    str_num = temp.group()
    num = int(str_num) + 1
    return str(num)

ret = re.sub(r"\d+", add, "python = 997")
print(ret)

ret = re.sub(r"\d+", add, "python = 99")
print(ret)

