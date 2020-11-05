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

from The_framework_v2.base_page import BasePage
from The_framework_v2.common_page import CommonPage

from The_framework_v2.dome_page import DemoPage


from The_framework_v2.utils import Utils



class TestLogin:
    testcase_file = 'test_search.yaml'
    po_lile = 'page_demo.yaml'

    data = Utils.from_file(testcase_file)


    # data = Utils.from_file('test_search.yaml')# 把返回结果存到变量data里
    def setup_class(self): #  setup_class只执行一次，但是search出来有3个case,所有case都要先执行self.demo.start()
        self.app = BasePage()
        self.app.start()

        # self.demo = DemoPage(self.po_lile)
        # self.demo.start() #  别忘了启动
        # print(BasePage._driver)
        # print(DemoPage._driver)
        #启动App

    def setup(self):  #  每个case执行之前都要执行
        pass

    # def teardown(self): #每个case 执行完之后都要执行
    #     self.demo.back()  # 点了取消这个按钮,不是后退

    def teaedown_class(self):
        self.demo.stop()
    #todo:测试数据的数据驱动
    @pytest.mark.parametrize('username ,password',[
            ('user1', 'pass1'),
            ('user2', 'pass2')
    ])

    def test_login_1(self, username ,password):
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
        self.demo = DemoPage(self.po_lile)
        self.demo.search(keyword)
        self.demo.back()

    #使用common page代替
    @pytest.mark.parametrize(data['keys'],data['values'])
    def test_search_common(self,keyword):
        #todo:python元编程实现python语句的数据驱动
        # print(keyword)
        demo = CommonPage(self.po_lile)
        demo.search(keyword=keyword)
        demo.back()

    def test_login(self):
        po_file = 'page_login.yaml'
        login = CommonPage(po_file)
        # login.start()
        #借助于__getattr__方法实现任意方法代理
        #login.xxxx => __getattr
        #login.login_by_password => print
        #print('18280101111','123456')
        # login.login_by_password('18280101111','123456')
        # login.login_by_password(username='13280101112', password='123456')
        login.login_by_password(username='13280101112', password='123456')





