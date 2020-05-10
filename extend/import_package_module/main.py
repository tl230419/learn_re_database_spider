'''
*****************
Date: 2020-05-10
Author: Allen
*****************
'''

import importlib

module = importlib.import_module("childpkg.child")
print(module)
print(module.description)