#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：Test_two -> click_add
@IDE    ：PyCharm
@Author ：hang.zhao
@Date   ：2020/8/23 13:18
@Desc   ：
=================================================='''
from selenium.webdriver.common.by import By

from zuoye_weixin.page1.base_page import BasePage
from zuoye_weixin.page1.click_add_department import ClickAddDepartment


class ClickAdd(BasePage):
    def clickadd(self):
        self.find(By.CSS_SELECTOR,".member_colLeft_top_addBtn").click()
        return ClickAddDepartment(self._driver)
