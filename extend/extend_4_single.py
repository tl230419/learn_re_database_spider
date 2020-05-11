'''
*****************
Date: 2020-05-11
Author: Allen
*****************
'''

import time

class Singleton1():
    _instance = None
    def __new__(cls, *args, **kwargs):
        return object.__new__(cls, *args, **kwargs)

    def __init__(self):
        time.sleep(3)

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = object.__new__(cls);

        return cls._instance