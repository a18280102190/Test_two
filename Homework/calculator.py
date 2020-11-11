#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：Test_two -> calculator
@IDE    ：PyCharm
@Author ：hang.zhao
@Date   ：2020/8/12 21:59
@Desc   ：
=================================================='''
"""
被测试的代码:
计算器：
    1、有个计算机类
    2、有四个方法：加减乘除
"""


class Calculator:
    def add(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

    def mul(self, a, b):
        return a * b

    def div(self, a, b):
        return a / b