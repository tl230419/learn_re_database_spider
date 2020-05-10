'''
*****************
Date: 2020-05-10
Author: Allen
*****************
'''

import importlib

module = importlib.import_module("brother")
module.say_hi()
print(module.description)
module.TestClass()