'''
*****************
Date: 2020-05-11
Author: Allen
*****************
'''

import unittest

class TestClass02(unittest.TestCase):
    def test_bbb(self):
        print("测试方法test_bbb执行啦！")

    def test_aaa(self):
        print("测试方法test_aaa执行啦！")

if __name__ == '__main__':
    #unittest.main()

    suite = unittest.TestSuite()
    suite.addTest(TestClass02("test_bbb"))
    suite.addTest(TestClass02("test_aaa"))

    text_runner = unittest.TextTestRunner()
    text_runner.run(suite)

class TestClass01(unittest.TestCase):
    num = 1000

    def setUp(self):
        print("执行每个单元测试方法会调用!")

    def test_xxx(self):
        print("测试>>>>:", "TestClass01", self.num)

    def tearDown(self):
        print("执行每个单元测试方法结束时会调用!")

    @unittest.skip("请说出你不想测试的原因")
    def test_skip(self):
        print("测试>>>>:", "skip")

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(TestClass01("test_xxx"))

    text_runner = unittest.TextTestRunner()
    text_runner.run(suite)