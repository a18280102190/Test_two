#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：Test_two -> test_param
@IDE    ：PyCharm
@Author ：hang.zhao
@Date   ：2020/11/11 20:50
@Desc   ：
=================================================='''
import pytest

#迪卡尔积
@pytest.mark.parametrize('a', [1, 2, 3, 4])
@pytest.mark.parametrize('b', [5, 6, 7, 8, 'a', 'b'])
@pytest.mark.parametrize('c', ['x', 'y', 'z'])
def test_case2(a, b, c):
    print(f'a = {a}   b = {b} ')
