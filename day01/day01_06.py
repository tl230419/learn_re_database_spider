'''
*****************
Date: 2020-04-30
Author: Allen
*****************
'''

#coding=utf-8

import re

ret = re.match("\w{4,20}@163\.com", "test@163.com")
print(ret.group())

ret = re.match("\w{4,20}@(163|126|qq)\.com", "test@126.com")
print(ret.group())

ret = re.match("\w{4,20}@(163|126|qq)\.com", "test@qq.com")
print(ret.group())

ret = re.match("\w{4,20}@(163|126|qq)\.com", "test@gmail.com")
if ret:
    print(ret.group())
else:
    print("不是163、126、qq邮箱")

# 提取电话号码
result = re.match("(\d{3,4})-(\d{7,8})", "010-12345678")
if result:
    print(result.group(1))
    print(result.group(2))
else:
    print("匹配失败！")
