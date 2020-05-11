'''
*****************
Date: 2020-05-11
Author: Allen
*****************
'''

import threading
import time

class Singleton():
    _instance_lock = threading.Lock()

    def __init__(self):
        print("init")
        time.sleep(5)

    def __new__(cls, *args, **kwargs):
        #("new...")
        if not hasattr(cls, "_instance"):
            with cls._instance_lock:
                if not hasattr(cls, "_instance"):
                    cls._instance = object.__new__(cls, *args, **kwargs)

        #print("cls._instance: ", cls._instance)
        return cls._instance