#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：Test_two -> test_scope
@IDE    ：PyCharm
@Author ：hang.zhao
@Date   ：2020/11/12 16:47
@Desc   ：
=================================================='''
import pytest



def test_1(connDB):
    print('case1')

class TestDemo:
    def test_a(self,connDB):
        print('testa')

    def test_b(self,connDB):
        print('testb')

class TestDemo1:
    def test_a1(self,connDB):
        print('testa')

    def test_b1(self,connDB):
        print('testb')