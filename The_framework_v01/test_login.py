#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：Test_two -> test_login
@IDE    ：PyCharm
@Author ：hang.zhao
@Date   ：2020/11/2 17:05
@Desc   ：
如何让测试框架丰富起来？
第一个维度，测试步骤的数据驱动
比如写在yaml里，平台的数据库里，让测试框架自动去导
第二个维度，测试数据的数据驱动
第三个维度，PO的数据驱动
=================================================='''
import pytest

from The_framework_v01.dome_page import DemoPage
from The_framework_v01.utils import Utils


class TestLogin:
    data = Utils.from_file('test_search.yaml')# 把返回结果存到变量data里
    def setup_class(self): #  setup_class只执行一次，但是search出来有3个case,所有case都要先执行self.demo.start()
        self.demo = DemoPage()
        self.demo.start() #  别忘了启动
        #启动App

    def setup(self):  #  每个case执行之前都要执行
        pass

    def teardown(self): #每个case 执行完之后都要执行
        self.demo.back()  # 点了取消这个按钮,不是后退

    def teaedown_class(self):
        self.demo.stop()
    #todo:测试数据的数据驱动
    @pytest.mark.parametrize('username ,password',[
            ('user1', 'pass1'),
            ('user2', 'pass2')
    ])

    def test_login(self, username ,password):
        #todo:测试步骤的数据驱动
        self.demo.login(username,password)
        assert 1 == 1

    # @pytest.mark.parametrize('keyword',[
    #     'ailibaba',
    #     # 'baidu',
    #     # 'jd'
    # ])
    #  通过读数据文件，读出三条数据，动态化地传递进来
    @pytest.mark.parametrize(data['keys'],data['values'])
    def test_search(self,keyword):
        # print(keyword)
        self.demo.search(keyword)