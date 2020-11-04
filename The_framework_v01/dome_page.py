#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：Test_two -> dome_page
@IDE    ：PyCharm
@Author ：hang.zhao
@Date   ：2020/11/2 16:58
@Desc   ：
=================================================='''
from selenium.webdriver.common.by import By

from The_framework_v01.base_page import BasePage


class DemoPage(BasePage):
    # 初始化
    _search_button=(By.ID, 'home_search')
    #todo：po的数据驱动
    def login(self, username, password):
        pass

    def forget_password(self):
        pass

    def search(self, keyword):
        self.po_run('search', keyword=keyword)
        # self.find(self._search_button).click()
        return self

    def back(self):# 跳回功能
        self.po_run('back')
        return self
