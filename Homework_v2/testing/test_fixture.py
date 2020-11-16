#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：Test_two -> test_fixture
@IDE    ：PyCharm
@Author ：hang.zhao
@Date   ：2020/11/12 15:57
@Desc   ：
=================================================='''

import pytest
# 当一个方法上面加个@pytest.fixture() 装饰器就变成了了fixture方法
# yield 能够激活fixture teardown 操作，yield相当于return
# 使用pytest xxxx.py --setup-show 追溯fixture的执行过程
# yield python生成器,如果一个方法里面使用yield ，这个方法就办成了生成器
# yield 前面的操作，相当于 setup 操作，yield 语句后面的相当于 teardown操作
# 如果需要返回值，yield 相当于 return 直接写在yield 后面即可

# autouse=Ture 可以应用到所有的测试用例中，不需要传入fixture 参数
#如果需要返回数据，则需要把fixture 名字传入到测试用例里面

@pytest.fixture(autouse=True)
def login():
    print('登录')
    username = 'tom'
    password = 123456
    # return [username,password]
    yield [username, password]
    print("登出")


def test_case1():
    print(f"需要登录 1 {login}")


def test_case2():
    print("需要登录")


def test_case3():
    print(f"需要登录 3 {login}")

# @pytest.mark.usefixtures('login')
# def test_case4():
#     print(f"case4 {login}")
