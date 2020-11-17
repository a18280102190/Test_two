#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：Test_two -> test_add_department
@IDE    ：PyCharm
@Author ：hang.zhao
@Date   ：2020/8/23 23:42
@Desc   ：
=================================================='''
from selenium.webdriver.common.by import By

from zuoye_weixin_v1.page1.mian import Mian


class TestAddDepartment():

    def setup(self):
        self.mian = Mian()

    def test_Departmen(self):
        # assert self.mian.goto_department().clickadd().click_add_department().department()
        # result = self.find(By.CSS_SELECTOR,"#party_name").text

        result = self.mian.goto_department().clickadd().click_add_department().department()
        print(result)
        assert ' QA部门' in result
        # 对方法进行实例化，并调用

