#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：Test_two -> test_set
@IDE    ：PyCharm
@Author ：hang.zhao
@Date   ：2020/11/9 22:28
@Desc   ：
=================================================='''
#setup_module,teardown_module 整个模块的执行前后，分别被调用一次
def setup_module():
    print("setup：模块级别的")

def teardown_module():
    print("teardown:模块级别的")


def setup_function():
    print("setup: 函数级别的")

def teardown_function():
    print("teardown： 函数级别的")

def test_case1():
    print("case1")

class TestA:
    #setup_class,teardown_class 类级别的，在每一个类的只是前后被调用
    def setup_class(self):
        print("开始，类级别的")

    def teardown_class(self):
        print("结束，类级别的")
    #setup ,teardown 是方法级别的，在每一个类里面的测试用例前后分别 被 调用一次
    def setup(self):
        print("开始，方法级别")

    def teardown(self):
        print("结束，方法级别")

    def test_a(self):
        print("test_a")

    def test_b(self):
        print("test_b")