#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：Test_two -> mian
@IDE    ：PyCharm
@Author ：hang.zhao
@Date   ：2020/8/23 13:42
@Desc   ：
=================================================='''
from selenium.webdriver.common.by import By

from web_weixin_v1.page.base_page import BasePage
from web_weixin_v1.page.click_add import ClickAdd


class Mian(BasePage):
    #继承BasePage的公共方法
    # _base_url = "https://work.weixin.qq.com/"

    #打开网站

    def goto_department(self):
        self.find(By.ID,"menu_contacts").click()
        return ClickAdd(self._driver)


