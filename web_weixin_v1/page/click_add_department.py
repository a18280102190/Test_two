#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：Test_two -> click_add_department
@IDE    ：PyCharm
@Author ：hang.zhao
@Date   ：2020/8/23 13:30
@Desc   ：
=================================================='''
from selenium.webdriver.common.by import By

from web_weixin_v1.page.base_page import BasePage
from web_weixin_v1.page.department import Department


class ClickAddDepartment(BasePage):
    def click_add_department(self):
        self.find(By.CSS_SELECTOR,".js_create_party").click()
        #点击添加部门按钮
        return Department(self._driver)
