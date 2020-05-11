'''
*****************
Date: 2020-05-11
Author: Allen
*****************
'''

import unittest
import threading
import extend_4_single
import extend_4_single_2

class TestSingleton(unittest.TestCase):
    def test_singleton1(self):
        for i in range(20):
            threading.Thread(target=lambda :print(extend_4_single.Singleton1())).start()

    def test_singleton2(self):
        for i in range(20):
            threading.Thread(target=lambda :print(extend_4_single_2.Singleton())).start()

if __name__ == '__main__':
    #TestSingleton().test_singleton1()
    TestSingleton().test_singleton2()