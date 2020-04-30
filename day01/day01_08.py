'''
*****************
Date: 2020-04-30
Author: Allen
*****************
'''

import re

#result = re.match("<([a-zA-Z0-9]*)>.*</\\1>", "<html>helloworld</html>")
result = re.match(r"<([a-zA-Z0-9]*)>.*</\1>", "<html>helloworld</html>")
if result:
    print(result.group())
else:
    print("匹配失败！")