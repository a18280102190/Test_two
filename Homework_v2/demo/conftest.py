#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：Test_two -> conftest
@IDE    ：PyCharm
@Author ：hang.zhao
@Date   ：2020/11/12 17:21
@Desc   ：
=================================================='''
import pytest

@pytest.fixture(scope='session')
def connDB():
    print('连接数据库 A')
    yield
    print('断开数据库 A ')